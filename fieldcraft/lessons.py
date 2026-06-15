"""
Modern-conflict lessons layer — analytical, defensive, individual-focused.

Distilled "lessons learned" from recent and ongoing conflicts (in the spirit of
RUSI / West Point Modern War Institute / CSIS briefs), framed for what they mean to
an INDIVIDUAL on the ground: the protective, medical, survival, comms, and resilience
takeaways. This is analysis and readiness education — NOT instructions to operate
weapons, conduct attacks, or build munitions.

Seeded here; extended from data/lessons.json (research-built).
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
import json
import os

DOMAINS = ["drones_uas", "counter_uas", "ew_comms", "isr_signature",
           "combat_medicine", "logistics", "small_unit", "resilience"]


@dataclass
class Lesson:
    id: str
    domain: str
    lesson: str          # what changed / what was observed
    conflict: str        # where it was observed
    takeaway: str        # the DEFENSIVE/protective/individual takeaway
    sources: list

    def to_dict(self): return asdict(self)


_SEED = [
    Lesson("L-UAS-01", "drones_uas",
           "Cheap small UAS and FPV/loitering munitions now saturate the battlefield; "
           "almost anything seen can be struck, and the front is transparent to overhead view.",
           "Ukraine 2022-2026, Nagorno-Karabakh 2020",
           "Assume you are observed from above at all times. Disperse, minimize time in the open, "
           "use overhead cover and terrain, and control thermal/visual/acoustic signature.",
           ["https://www.understandingwar.org/", "https://rusi.org/"]),
    Lesson("L-UAS-02", "counter_uas",
           "Detecting and countering small drones is hard; individual awareness and passive "
           "protection matter as much as any active counter-measure.",
           "Ukraine 2022-2026",
           "Learn drone sound/sight cues, keep overhead cover within a few seconds' reach, "
           "spread out (don't cluster), and harden fighting/rest positions with overhead protection.",
           ["https://rusi.org/", "https://mwi.westpoint.edu/"]),
    Lesson("L-EW-01", "ew_comms",
           "Pervasive electronic warfare degrades GPS and radios; emissions get located and targeted.",
           "Ukraine 2022-2026",
           "Keep a real PACE comms plan, train land navigation WITHOUT GPS (map/compass/terrain), "
           "minimize transmissions, and practice emission discipline.",
           ["https://rusi.org/", "https://warontherocks.com/"]),
    Lesson("L-ISR-01", "isr_signature",
           "Ubiquitous ISR (drones, thermal, satellites) makes hiding the central survival problem.",
           "Ukraine, Gaza",
           "Manage signature across spectra: shape/shine/shadow/silhouette/movement + thermal. "
           "Move at limited visibility, avoid patterns, and keep heat sources concealed.",
           ["https://mwi.westpoint.edu/"]),
    Lesson("L-MED-01", "combat_medicine",
           "Evacuation is often delayed for hours/days because drones threaten the routes, forcing "
           "Prolonged Field Care far beyond the classic 'golden hour'.",
           "Ukraine 2022-2026",
           "Train beyond immediate TCCC: hemorrhage control PLUS prolonged care — hypothermia "
           "prevention, tourniquet conversion, hydration, documentation, casualty sheltering.",
           ["https://www.naemt.org/", "https://prolongedfieldcare.org/"]),
    Lesson("L-LOG-01", "logistics",
           "Resupply, batteries, and casualty movement are all harder under precision/drone threat; "
           "stockpiles must be dispersed and power is a constant constraint.",
           "Ukraine 2022-2026",
           "Plan power (batteries/solar) and water/food redundancy; disperse caches; assume "
           "resupply may be delayed; keep an individual sustainment load.",
           ["https://rusi.org/"]),
    Lesson("L-SU-01", "small_unit",
           "Forces have dispersed, decentralized, and re-learned field fortification; massed or "
           "static positions are quickly found and struck.",
           "Ukraine 2022-2026",
           "Small, dispersed, dug-in/covered, and self-reliant survives; build protective positions, "
           "avoid clustering, and be able to operate with minimal external support.",
           ["https://mwi.westpoint.edu/", "https://rusi.org/"]),
    Lesson("L-RES-01", "resilience",
           "Constant drone observation and sustained operations impose severe psychological load.",
           "Ukraine 2022-2026",
           "Build mental resilience and sustainment habits: sleep discipline when possible, routine, "
           "small-team cohesion, and deliberate recovery; manage fear with training and competence.",
           ["https://mwi.westpoint.edu/"]),
]

_BY_ID = {}


def _load():
    _BY_ID.clear()
    for l in _SEED:
        _BY_ID[l.id] = l
    path = os.path.join(os.path.dirname(__file__), "..", "data", "lessons.json")
    if os.path.exists(path):
        try:
            for d in json.load(open(path, encoding="utf-8")):
                _BY_ID[d["id"]] = Lesson(id=d["id"], domain=d.get("domain", ""),
                                         lesson=d.get("lesson", ""), conflict=d.get("conflict", ""),
                                         takeaway=d.get("takeaway", ""), sources=d.get("sources", []))
        except Exception:
            pass


_load()


def list_lessons(domain: str = None) -> list:
    items = list(_BY_ID.values())
    return [l for l in items if l.domain == domain] if domain else items


def get_lesson(lid: str):
    return _BY_ID.get((lid or "").upper())


def count() -> int:
    return len(_BY_ID)
