"""Tests for the descriptive equipment reference."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fieldcraft import equipment, sources  # noqa: E402
from fieldcraft.cli import main  # noqa: E402


def test_catalog_loads():
    assert equipment.count() >= 90
    cats = equipment.categories()
    assert "armored-vehicles" in cats and "aircraft-fixed-wing" in cats
    # descriptive fields only — no employment/lethality keys
    it = equipment.get("m1-abrams")
    assert it and it.origin == "United States" and it.role
    d = it.to_dict()
    assert set(d) <= {"id", "name", "category", "type", "origin", "role", "era",
                      "status", "class", "operators"}


def test_filter_and_search():
    us = equipment.all_items(origin="United States")
    assert us and all("united states" in i.origin.lower() for i in us)
    fighters = equipment.search("fighter")
    assert any("F-16" in i.name for i in fighters)
    assert equipment.all_items("aircraft-rotary")


def test_sources_hub_has_odin():
    s = sources.sources()
    assert any("odin" in r["url"].lower() for r in s)
    assert any(r["type"] == "primary-database" for r in s)


def test_cli():
    assert main(["equipment", "--category", "air-defense"]) == 0
    assert main(["equipment", "--search", "tank", "--format", "json"]) == 0
    assert main(["equip-show", "f-35", "--format", "json"]) == 0
    assert main(["equip-show", "nope"]) == 1
    assert main(["sources"]) == 0
