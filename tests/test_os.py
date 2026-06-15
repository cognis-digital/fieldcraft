"""Tests for the Modern Soldier OS expansion (v0.2): lessons, SOPs, new roles."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fieldcraft import TOOL_VERSION, lessons, sop, get_role, catalog  # noqa: E402
from fieldcraft.cli import main  # noqa: E402


def test_version_bumped():
    major, minor = (int(x) for x in TOOL_VERSION.split(".")[:2])
    assert (major, minor) >= (0, 2)   # Modern Soldier OS line


def test_lessons():
    assert lessons.count() >= 8
    drone = lessons.list_lessons("drones_uas")
    assert drone and all(l.domain == "drones_uas" for l in drone)
    l = lessons.get_lesson("L-MED-01")
    assert l and "prolonged" in (l.lesson + l.takeaway).lower()
    # every lesson carries a defensive/individual takeaway
    assert all(x.takeaway for x in lessons.list_lessons())


def test_sops():
    keys = {s.key for s in sop.list_sops()}
    assert {"tlp", "priorities-of-work", "pcc-pci", "aar", "pace"} <= keys
    assert sop.get_sop("aar") and len(sop.get_sop("aar").steps) >= 4
    assert sop.get_sop("nope") is None


def test_new_roles():
    for k in ("team_leader", "uas_observer", "pioneer"):
        r = get_role(k)
        assert r and r.skills and r.kit


def test_new_wiki_pages_exist():
    pages = catalog.wiki_pages()
    for k in ("lessons", "camouflage-concealment", "night", "cbrn",
              "tactical-fitness", "field-hygiene", "sop-battle-rhythm"):
        assert k in pages
        fn = pages[k][0]
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", fn)
        assert os.path.exists(path) and os.path.getsize(path) > 500


def test_new_checklists():
    assert catalog.checklist("field-hygiene")
    assert catalog.checklist("drone-threat-react")


def test_os_cli():
    assert main(["os"]) == 0
    assert main(["lessons", "--format", "json"]) == 0
    assert main(["lessons", "--domain", "ew_comms"]) == 0
    assert main(["lesson", "L-UAS-01", "--format", "json"]) == 0
    assert main(["lesson", "NOPE"]) == 1
    assert main(["sop"]) == 0
    assert main(["sop", "pace", "--format", "json"]) == 0
    assert main(["sop", "nope"]) == 1
    assert main(["loadout", "team_leader,uas_observer,pioneer", "--tier", "sustainment"]) == 0
