"""Tests for fieldcraft. No network; all data is local/seeded."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fieldcraft import (  # noqa: E402
    TOOL_NAME, TOOL_VERSION, TIERS, list_roles, get_role, build,
    acronyms, catalog,
)
from fieldcraft.cli import main  # noqa: E402


def test_metadata():
    assert TOOL_NAME == "fieldcraft"
    assert TOOL_VERSION.count(".") == 2


def test_roles():
    rs = list_roles()
    keys = {r.key for r in rs}
    assert {"survivalist", "medic", "navigator", "comms", "rucker", "logistics", "scout"} <= keys
    medic = get_role("medic")
    assert medic and "MARCH assessment" in medic.skills
    assert any("tourniquet" in i.lower() for items in medic.kit.values() for i in items)


def test_build_loadout_composes():
    b = build(["medic", "navigator"], tier="72h")
    assert "medic" in b["roles"] and "navigator" in b["roles"]
    # kit accumulates across roles & tiers up to the chosen tier
    flat = [i for items in b["kit"].values() for i in items]
    assert any("compass" in i.lower() for i in flat)
    assert any("tourniquet" in i.lower() or "ifak" in i.lower() for i in flat)
    assert "MARCH assessment" in b["skills"]
    assert b["references"]
    json.dumps(b)


def test_acronyms():
    assert acronyms.count() >= 20
    d = acronyms.lookup("march")  # case-insensitive
    assert d and "hemorrhage" in d["expansion"].lower()
    assert acronyms.lookup("METT-TC")
    assert acronyms.lookup("nope_term") is None
    assert any(x["term"] == "PACE" for x in acronyms.search("redundancy") + acronyms.search("pace"))


def test_resources_and_cognis():
    rs = catalog.resources()
    assert len(rs) >= 12
    assert any("stopthebleed" in r["url"] for r in rs)
    med = catalog.resources("medical")
    assert med and all(r["domain"] == "medical" for r in med)
    assert any(c["repo"] == "labforge" for c in catalog.cognis_resources())


def test_checklists():
    cl = catalog.checklists()
    assert "go-bag-72h" in cl and "ifak" in cl
    assert catalog.checklist("ifak")
    assert catalog.checklist("nope") is None


def test_wiki_registry():
    pages = catalog.wiki_pages()
    assert "survival" in pages and "medical-tccc" in pages and "acronyms" in pages


def test_cli():
    assert main(["roles"]) == 0
    assert main(["loadout", "medic,navigator", "--tier", "72h"]) == 0
    assert main(["loadout", "medic,navigator", "--format", "json"]) == 0
    assert main(["loadout", "nope_role"]) == 2
    assert main(["acronym", "MARCH"]) == 0
    assert main(["acronym", "nope_term"]) == 1
    assert main(["acronyms", "--search", "medevac", "--format", "json"]) == 0
    assert main(["resources", "--domain", "comms"]) == 0
    assert main(["cognis"]) == 0
    assert main(["checklist", "go-bag-72h"]) == 0
    assert main(["checklists"]) == 0
    assert main(["wiki"]) == 0
    assert main(["wiki", "survival"]) == 0
    assert main(["search", "tourniquet", "--format", "json"]) == 0
