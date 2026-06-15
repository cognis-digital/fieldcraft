"""
Role / loadout builder — "build your character, but for real life."

Pick a role (medic, navigator, comms, rucker, survivalist, logistics, scout) and
get a realistic, layered loadout: the kit you'd carry, the skills it assumes, and
the reference pages/manuals to learn it. Roles compose — build a fireteam-equivalent
of complementary roles for a group. This is preparedness/readiness gear planning,
not a combat configurator.

Data is seeded here and can be extended from data/roles.json.
"""
from __future__ import annotations
from dataclasses import dataclass, field, asdict
import json
import os

TOOL_NAME = "fieldcraft"
TOOL_VERSION = "0.2.0"

TIERS = ["edc", "24h", "72h", "sustainment"]   # escalating preparedness levels


@dataclass
class Role:
    key: str
    name: str
    summary: str
    skills: list = field(default_factory=list)       # skill areas to train
    kit: dict = field(default_factory=dict)          # tier -> [items]
    references: list = field(default_factory=list)   # wiki page keys / manuals
    cognis: list = field(default_factory=list)       # related cognis repos

    def to_dict(self): return asdict(self)


_SEED = [
    Role("survivalist", "Survivalist", "Water, fire, shelter, signaling — the core priorities of survival.",
         ["water procurement & purification", "fire-craft", "shelter-building", "signaling", "foraging safety"],
         {"edc": ["lighter + ferro rod", "fixed-blade knife", "water filter straw", "cordage (paracord)",
                  "emergency blanket", "whistle"],
          "72h": ["water filter + tablets", "metal canteen/cup", "tarp + stakes", "sleeping bag/bivy",
                  "headlamp + spares", "fire kit (multiple methods)", "signal mirror", "first-aid kit"]},
         ["survival", "food-water", "environment"], ["labforge"]),
    Role("medic", "Medic / TCC-aware first responder", "Hemorrhage control and field first aid (Stop the Bleed / TCCC-informed).",
         ["MARCH assessment", "tourniquet application", "wound packing", "airway basics", "wilderness first aid"],
         {"edc": ["tourniquet (CoTCCC-recommended)", "compressed gauze", "gloves", "trauma shears", "marker"],
          "72h": ["IFAK (TQ, hemostatic gauze, chest seals, NPA, pressure bandage)", "burn dressing",
                  "splint (SAM)", "OTC meds", "first-aid manual", "PPE"]},
         ["medical-tccc"], []),
    Role("navigator", "Navigator", "Move accurately with map, compass, and terrain — no batteries required.",
         ["map reading", "compass + declination", "MGRS/UTM", "pace count", "terrain association"],
         {"edc": ["baseplate compass", "area map (waterproof)", "pace beads", "pencil"],
          "72h": ["topo maps + protractor", "GPS + spare batteries", "altimeter/watch", "map case"]},
         ["land-nav", "mil-reference"], ["labforge"]),
    Role("comms", "Comms operator", "Keep a group connected with a PACE plan and licensed radio.",
         ["PACE planning", "radio operation & etiquette", "antennas/propagation basics", "phonetics & prowords"],
         {"edc": ["GMRS/FRS handheld", "freq/PACE card", "spare batteries"],
          "72h": ["programmable HT (licensed)", "roll-up antenna", "notepad", "power bank", "AM/FM/weather radio"]},
         ["comms"], ["edgemesh"]),
    Role("rucker", "Rucker / load-bearer", "Move weight over distance without getting injured.",
         ["load packing & distribution", "foot care", "pacing", "progressive conditioning"],
         {"edc": ["broken-in boots", "good socks (wool)", "blister kit"],
          "sustainment": ["rucksack/frame", "load ~1/3 bodyweight max", "hydration", "weight plate/sandbag",
                          "dry bags", "trekking poles"]},
         ["rucking"], []),
    Role("logistics", "Logistics / sustainment", "Plan food, water, power, and supply for days, not hours.",
         ["ration/calorie planning", "water storage", "power/energy", "inventory & rotation"],
         {"72h": ["3 days food (~2000+ kcal/day)", "water 1 gal/person/day", "stove + fuel", "power bank/solar",
                  "cash", "documents copy"],
          "sustainment": ["bulk food + rotation log", "water containers + purification", "fuel store",
                          "generator/solar", "spares"]},
         ["food-water", "preparedness"], ["labforge"]),
    Role("scout", "Scout / observer", "Situational awareness, observation, and reporting (descriptive).",
         ["observation & reporting (SALUTE/SITREP)", "terrain analysis (OAKOC)", "low-signature movement",
          "optics use"],
         {"edc": ["binoculars/monocular", "notebook + pencil", "watch", "map"],
          "72h": ["spotting optics", "range card/notebook", "camera", "comms (see comms role)"]},
         ["land-nav", "mil-reference"], ["maritimeint", "geoaoi"]),
    Role("team_leader", "Team leader", "Plan, decide, and coordinate a small team (C2 / mission command).",
         ["troop-leading procedures", "PACE planning", "priorities of work", "AAR / mission command",
          "risk management"],
         {"edc": ["notebook + waterproof pen", "map + protractor", "comms card", "watch"],
          "72h": ["radio (see comms)", "team roster + PACE card", "casualty/evac plan card", "rehearsal kit"]},
         ["sop-battle-rhythm", "mil-reference"], ["jtf-meridian", "agentforge"]),
    Role("uas_observer", "Drone-threat / counter-UAS observer", "Detect and react to overhead drone threats (defensive awareness).",
         ["drone visual/acoustic recognition", "overhead-cover discipline", "dispersion", "signature management"],
         {"edc": ["binoculars", "notebook", "whistle/alert signal"],
          "72h": ["spotting optics", "acoustic awareness aids", "overhead-cover materials", "comms"]},
         ["lessons", "camouflage-concealment"], ["awesome-drone-warfare-osint", "frontline-drones"]),
    Role("pioneer", "Pioneer / field engineer", "Field-expedient construction and protective works (cover, shelter, obstacles) — protective, not demolitions.",
         ["protective position construction", "field-expedient shelter", "knots & lashings", "obstacle awareness"],
         {"edc": ["multitool", "cordage", "gloves", "folding saw"],
          "sustainment": ["entrenching tool", "wire/cordage", "tarps", "sandbags", "hand tools", "overhead-cover materials"]},
         ["camouflage-concealment", "survival"], ["labforge"]),
]

_BY_KEY = {}


def _load():
    _BY_KEY.clear()
    for r in _SEED:
        _BY_KEY[r.key] = r
    path = os.path.join(os.path.dirname(__file__), "..", "data", "roles.json")
    if os.path.exists(path):
        try:
            for d in json.load(open(path, encoding="utf-8")):
                _BY_KEY[d["key"]] = Role(**{k: v for k, v in d.items()
                                            if k in Role.__annotations__})
        except Exception:
            pass


_load()


def list_roles() -> list:
    return list(_BY_KEY.values())


def get_role(key: str):
    return _BY_KEY.get((key or "").lower())


def build(roles: list, tier: str = "72h") -> dict:
    """Compose a group loadout from several roles at a preparedness tier."""
    chosen = [get_role(r) for r in roles if get_role(r)]
    kit, skills, refs, cognis = {}, set(), set(), set()
    for r in chosen:
        for t in TIERS:
            if TIERS.index(t) <= TIERS.index(tier) if tier in TIERS else True:
                for item in r.kit.get(t, []):
                    kit.setdefault(t, [])
                    if item not in kit[t]:
                        kit[t].append(item)
        skills.update(r.skills); refs.update(r.references); cognis.update(r.cognis)
    return {"roles": [r.key for r in chosen], "tier": tier, "kit": kit,
            "skills": sorted(skills), "references": sorted(refs),
            "cognis_repos": sorted(cognis)}
