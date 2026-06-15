"""
Military equipment reference — DESCRIPTIVE / encyclopedic only.

A "what exists" catalog of military equipment, vehicles, and aircraft: designation,
type, country of origin, role, era, class, and operators — the same kind of neutral
reference data found in public encyclopedias and the U.S. Army's public ODIN /
Worldwide Equipment Guide. It is identification/recognition/reference material.

It deliberately contains NO employment, targeting, lethality, or how-to-use/defeat
content — only what a system is and where it comes from. For the comprehensive,
authoritative datasets (orders of magnitude larger than any hand-curated seed), use
the linked public sources in `fieldcraft/sources.py` (ODIN, Wikipedia lists, etc.).

Entries load from every JSON file under data/equipment/*.json (each file is a
category), so the catalog grows by adding files.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
import glob
import json
import os

CATEGORIES = [
    "small-arms", "crew-served", "armored-vehicles", "artillery", "air-defense",
    "aircraft-fixed-wing", "aircraft-rotary", "uas", "naval", "missiles",
    "support-vehicles", "c2-ew-sensors", "individual-kit",
]

# descriptive fields only
FIELDS = ["id", "name", "category", "type", "origin", "role", "era", "status",
          "class", "operators"]


@dataclass
class Item:
    id: str
    name: str
    category: str
    type: str = ""
    origin: str = ""
    role: str = ""
    era: str = ""
    status: str = ""
    cls: str = ""              # 'class' is reserved; stored as cls, serialized as class
    operators: list = None

    def to_dict(self):
        d = asdict(self)
        d["class"] = d.pop("cls")
        if d["operators"] is None:
            d["operators"] = []
        return d


_ITEMS = []
_BY_ID = {}


def _coerce(d: dict) -> Item:
    return Item(id=d.get("id") or d.get("name", ""), name=d.get("name", ""),
                category=d.get("category", ""), type=d.get("type", ""),
                origin=d.get("origin", ""), role=d.get("role", ""),
                era=d.get("era", ""), status=d.get("status", ""),
                cls=d.get("class", d.get("cls", "")), operators=d.get("operators", []))


def _load():
    _ITEMS.clear(); _BY_ID.clear()
    base = os.path.join(os.path.dirname(__file__), "..", "data", "equipment")
    for path in sorted(glob.glob(os.path.join(base, "*.json"))):
        try:
            for d in json.load(open(path, encoding="utf-8")):
                it = _coerce(d)
                if it.id and it.id not in _BY_ID:
                    _BY_ID[it.id] = it
                    _ITEMS.append(it)
        except Exception:
            continue


_load()


def all_items(category: str = None, origin: str = None) -> list:
    items = _ITEMS
    if category:
        items = [i for i in items if i.category == category]
    if origin:
        items = [i for i in items if origin.lower() in (i.origin or "").lower()]
    return items


def get(item_id: str):
    return _BY_ID.get(item_id) or next(
        (i for i in _ITEMS if i.name.lower() == (item_id or "").lower()), None)


def search(q: str) -> list:
    q = (q or "").lower()
    return [i for i in _ITEMS
            if q in i.name.lower() or q in (i.type or "").lower()
            or q in (i.role or "").lower() or q in (i.cls or "").lower()]


def categories() -> dict:
    out = {}
    for i in _ITEMS:
        out[i.category] = out.get(i.category, 0) + 1
    return out


def count() -> int:
    return len(_ITEMS)
