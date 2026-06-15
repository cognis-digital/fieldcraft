"""
Acronym & terminology glossary — military / tactical / survival / medical / comms.
Seeded baseline here; the full set is merged from data/acronyms.json (research-built).
"""
from __future__ import annotations
import json
import os

# baseline seed (term -> [expansion, domain, note])
_SEED = {
    "METT-TC": ["Mission, Enemy, Terrain & weather, Troops, Time available, Civil considerations",
                "doctrine", "Factors for analyzing a situation."],
    "OAKOC": ["Observation & fields of fire, Avenues of approach, Key terrain, Obstacles, Cover & concealment",
              "doctrine", "Military terrain analysis (a.k.a. KOCOA)."],
    "MARCH": ["Massive hemorrhage, Airway, Respiration, Circulation, Hypothermia/Head",
              "medical", "TCCC trauma assessment sequence."],
    "TCCC": ["Tactical Combat Casualty Care", "medical", "Battlefield-derived trauma care; TECC is the civilian analog."],
    "IFAK": ["Individual First Aid Kit", "medical", "Personal trauma kit (TQ, gauze, seals…)."],
    "TQ": ["Tourniquet", "medical", "Limb hemorrhage control device."],
    "PACE": ["Primary, Alternate, Contingency, Emergency", "comms", "Communications (or any) redundancy plan."],
    "MGRS": ["Military Grid Reference System", "navigation", "Grid coordinate system over UTM."],
    "UTM": ["Universal Transverse Mercator", "navigation", "Projected coordinate system."],
    "SERE": ["Survival, Evasion, Resistance, Escape", "survival", "Military survival training program."],
    "EDC": ["Every Day Carry", "gear", "Items carried daily."],
    "BOB": ["Bug-Out Bag", "preparedness", "72-hour grab-and-go kit (a.k.a. GHB/INCH variants)."],
    "SHTF": ["Stuff Hits The Fan", "preparedness", "Slang for a serious emergency scenario."],
    "AAR": ["After-Action Review", "doctrine", "Structured review of what happened and lessons."],
    "SITREP": ["Situation Report", "comms", "Concise status report."],
    "SALUTE": ["Size, Activity, Location, Unit, Time, Equipment", "doctrine", "Observation report format."],
    "MEDEVAC": ["Medical Evacuation", "medical", "Evacuation of casualties (9-line request)."],
    "CASEVAC": ["Casualty Evacuation", "medical", "Casualty transport on non-dedicated assets."],
    "OODA": ["Observe, Orient, Decide, Act", "doctrine", "Boyd's decision cycle."],
    "MRE": ["Meal, Ready-to-Eat", "food", "Self-contained field ration."],
    "RTO": ["Radio Telephone Operator", "comms", "The person running comms."],
    "NATO phonetic": ["Alfa Bravo Charlie … Zulu", "comms", "Spelling alphabet for clarity over radio."],
    "9-line": ["9-line MEDEVAC request", "medical", "Standard format to request medical evacuation."],
    "CCP": ["Casualty Collection Point", "medical", "Where casualties are gathered for treatment/evac."],
    "LZ": ["Landing Zone", "navigation", "Helicopter landing area."],
    "RV": ["Rendezvous (point)", "navigation", "Pre-planned meeting point (rally point)."],
}

_TERMS = {}


def _load():
    _TERMS.clear()
    for k, v in _SEED.items():
        _TERMS[k.upper()] = {"term": k, "expansion": v[0],
                             "domain": v[1] if len(v) > 1 else "", "note": v[2] if len(v) > 2 else ""}
    path = os.path.join(os.path.dirname(__file__), "..", "data", "acronyms.json")
    if os.path.exists(path):
        try:
            for d in json.load(open(path, encoding="utf-8")):
                t = d.get("term", "").strip()
                if t:
                    _TERMS[t.upper()] = {"term": t, "expansion": d.get("expansion", ""),
                                         "domain": d.get("domain", ""), "note": d.get("note", "")}
        except Exception:
            pass


_load()


def lookup(term: str):
    return _TERMS.get((term or "").strip().upper())


def all_terms() -> list:
    return sorted(_TERMS.values(), key=lambda d: d["term"].upper())


def search(q: str) -> list:
    q = (q or "").lower()
    return [d for d in _TERMS.values()
            if q in d["term"].lower() or q in d["expansion"].lower() or q in d.get("note", "").lower()]


def count() -> int:
    return len(_TERMS)
