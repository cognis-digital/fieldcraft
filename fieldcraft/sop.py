"""
SOP / battle-rhythm / readiness-discipline layer (descriptive & organizational).

The standing procedures and habits that keep an individual or small team ready and
organized — priorities of work, troop-leading procedures, pre-combat checks, the
after-action review, security halts. This is readiness and organizational discipline,
referenced descriptively from public doctrine — not assault drills or how to attack.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
import json
import os


@dataclass
class SOP:
    key: str
    name: str
    purpose: str
    steps: list

    def to_dict(self): return asdict(self)


_SEED = [
    SOP("tlp", "Troop-Leading Procedures (TLP)",
        "The eight-step thinking process for planning and preparing for any task (descriptive).",
        ["1. Receive the mission", "2. Issue a warning order", "3. Make a tentative plan",
         "4. Initiate movement", "5. Conduct reconnaissance", "6. Complete the plan",
         "7. Issue the order", "8. Supervise and refine"]),
    SOP("priorities-of-work", "Priorities of Work",
        "The ordered tasks a team does on occupying a position, so nothing critical is missed.",
        ["Security first (observation, sectors)", "Communications check (PACE)",
         "Mission-essential tasks / weapons & equipment checks", "Crew-served / key equipment positioned",
         "Fields of fire / observation & protective works (cover, overhead)",
         "Water/rations/rest plan", "Hygiene & maintenance", "Rehearsals & inspections", "Rest rotation"]),
    SOP("pcc-pci", "Pre-Combat Checks / Inspections (PCC/PCI)",
        "Systematic readiness checks of people, equipment, and knowledge before any operation.",
        ["Weapons & optics function (if applicable) / tools serviceable",
         "Comms: radios programmed, PACE briefed, batteries + spares",
         "Navigation: maps, compass, GPS + spares, routes briefed",
         "Medical: IFAK complete, CCP/evac plan known, blood type marked",
         "Water & rations for the duration", "Mission knowledge: every person can state the plan",
         "Signature: light/noise/thermal discipline set", "Seasonal: cold/heat/wet protection"]),
    SOP("aar", "After-Action Review (AAR)",
        "Structured learning review after any event to capture and apply lessons.",
        ["What was supposed to happen?", "What actually happened?", "Why were there differences?",
         "What went well — sustain?", "What did not — improve?", "Assign fixes and follow up"]),
    SOP("security-halt", "Security Halt (5 and 25)",
        "Immediate-area security routine when stopping (readiness/safety).",
        ["Stop, look, listen — scan your immediate ~5 m", "Then scan out to ~25 m",
         "Establish 360° observation / sectors", "Stay quiet and still; minimize signature",
         "Account for everyone before moving on"]),
    SOP("stand-to", "Stand-To",
        "Heightened-alert routine at the highest-risk transition times (dawn/dusk).",
        ["All-hands alert at first/last light", "Full observation of sectors",
         "Comms and equipment check", "Confirm everyone present & ready",
         "Stand down deliberately, resume priorities of work"]),
    SOP("pace", "PACE Plan",
        "Build redundancy into any critical capability (especially communications).",
        ["Primary — the normal method", "Alternate — first fallback",
         "Contingency — works when the first two fail", "Emergency — last resort / signal",
         "Brief it, rehearse it, write it on a card everyone carries"]),
]

_BY_KEY = {}


def _load():
    _BY_KEY.clear()
    for s in _SEED:
        _BY_KEY[s.key] = s
    path = os.path.join(os.path.dirname(__file__), "..", "data", "sops.json")
    if os.path.exists(path):
        try:
            for d in json.load(open(path, encoding="utf-8")):
                _BY_KEY[d["key"]] = SOP(**{k: v for k, v in d.items() if k in SOP.__annotations__})
        except Exception:
            pass


_load()


def list_sops() -> list:
    return list(_BY_KEY.values())


def get_sop(key: str):
    return _BY_KEY.get((key or "").lower())
