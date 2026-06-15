"""
Resource catalog + checklists + wiki-page registry.

Resources are curated links to PUBLIC / open-source tools, educational materials,
and public-domain manuals — plus the Cognis repos that complement field/preparedness
work. Seeded here; expanded from data/resources.json (research-built). Checklists are
practical, printable lists. The wiki registry maps page keys to the docs/ markdown.
"""
from __future__ import annotations
import json
import os

_DATA = os.path.join(os.path.dirname(__file__), "..", "data")

# seed resources: name, type, url, domain, note
_RESOURCES_SEED = [
    ["FM 21-76 US Army Survival Manual", "manual", "https://armypubs.army.mil/", "survival", "Public-domain survival doctrine."],
    ["TC 3-25.26 Map Reading & Land Navigation", "manual", "https://armypubs.army.mil/", "navigation", "Public land-nav manual."],
    ["Ranger Handbook (TC 3-21.76)", "manual", "https://armypubs.army.mil/", "mil-reference", "Public small-unit field reference."],
    ["Stop the Bleed", "education", "https://www.stopthebleed.org/", "medical", "Public hemorrhage-control training."],
    ["NAEMT TCCC / TECC", "education", "https://www.naemt.org/education/naemt-tccc", "medical", "Tactical/Emergency casualty care courses."],
    ["Ready.gov", "education", "https://www.ready.gov/", "preparedness", "US gov emergency-preparedness guidance."],
    ["FEMA", "education", "https://www.fema.gov/", "preparedness", "Disaster prep + free courses (IS series)."],
    ["American Red Cross", "education", "https://www.redcross.org/", "medical", "First aid / CPR / preparedness."],
    ["ARRL (amateur radio)", "education", "http://www.arrl.org/", "comms", "Ham radio licensing + resources."],
    ["CHIRP (radio programming)", "open-source", "https://chirpmyradio.com/", "comms", "Open-source radio programming tool."],
    ["QGIS", "open-source", "https://qgis.org/", "navigation", "Open-source GIS / mapping."],
    ["OpenStreetMap", "open-source", "https://www.openstreetmap.org/", "navigation", "Free editable world map."],
    ["OsmAnd", "open-source", "https://osmand.net/", "navigation", "Offline maps + navigation."],
    ["ATAK-CIV / CivTAK", "open-source", "https://tak.gov/", "navigation", "Team awareness mapping (civilian build)."],
    ["Kiwix", "open-source", "https://www.kiwix.org/", "preparedness", "Offline Wikipedia/medical references."],
    ["awesome-survival", "open-source", "https://github.com/leandromoreira/survival-manuals", "survival", "Collected survival/reference material."],
]

# cognis repos relevant to field/preparedness work
COGNIS = [
    {"repo": "labforge", "use": "Plan/scale the hardware & kit for a comms/logistics node or offline-AI field kit."},
    {"repo": "edgemesh", "use": "Run offline AI/reference models across field devices behind one endpoint."},
    {"repo": "maritimeint / geoaoi / awesome-drone-warfare-osint", "use": "Situational-awareness / OSINT reference (descriptive)."},
    {"repo": "jtf-meridian", "use": "Organize a group into roles/command structure (decision-support)."},
    {"repo": "agentforge", "use": "Stand up an AI 'org' of assistant roles for planning/checklists."},
]

CHECKLISTS_SEED = {
    "go-bag-72h": ["Water (1 gal/person/day x3) + filter/tablets", "Food ~2000 kcal/day x3",
                   "First-aid/IFAK", "Layered clothing + rain shell", "Headlamp + batteries",
                   "Multitool + knife", "Fire kit", "Emergency blanket/bivy", "Radio (NOAA/GMRS)",
                   "Phone power bank", "Cash + ID/doc copies", "Maps + compass", "Whistle", "Hygiene kit"],
    "ifak": ["Tourniquet (CoTCCC)", "Hemostatic gauze", "Pressure bandage", "Chest seals (vented)",
             "Nasopharyngeal airway + lube", "Gloves", "Trauma shears", "Tape", "Marker", "Mylar blanket"],
    "ruck-packing": ["Heavy items high & close to back", "Hydration accessible", "Rain protection / dry bags",
                     "Frequently-used items on top/pockets", "Test weight ≤ ~1/3 bodyweight", "Hot-spot/blister kit handy"],
    "water": ["Source identification", "Pre-filter (cloth) sediment", "Filter (0.1-0.2 micron) or boil 1 min",
              "Chemical backup (tabs)", "Safe storage (1 gal/person/day)"],
    "field-hygiene": ["Treat all water (boil/filter/chemical)", "Hand wash/sanitize before eating + after latrine",
                      "Latrine sited downhill + away from water/sleep", "Dry socks + foot care at halts",
                      "Manage hot spots before blisters", "Brush teeth", "Cover/treat minor wounds early",
                      "Insect/tick protection", "Rotate rest; watch for run-down teammates"],
    "drone-threat-react": ["Stop + listen/look on drone cue", "Get under overhead cover within seconds",
                           "Freeze movement; minimize signature", "Disperse — do not cluster",
                           "Account for team; move to better cover when clear", "Report (SALUTE/SITREP)"],
}


def _load_json(name):
    p = os.path.join(_DATA, name)
    if os.path.exists(p):
        try:
            return json.load(open(p, encoding="utf-8"))
        except Exception:
            return None
    return None


def resources(domain: str = None) -> list:
    seed = [{"name": r[0], "type": r[1], "url": r[2], "domain": r[3], "note": r[4]}
            for r in _RESOURCES_SEED]
    extra = _load_json("resources.json") or []
    by_url = {r["url"]: r for r in seed}
    for r in extra:
        if r.get("url"):
            by_url[r["url"]] = {"name": r.get("name", ""), "type": r.get("type", ""),
                                "url": r["url"], "domain": r.get("domain", ""), "note": r.get("note", "")}
    items = list(by_url.values())
    return [r for r in items if r.get("domain") == domain] if domain else items


def cognis_resources() -> list:
    return list(COGNIS)


def checklists() -> dict:
    cl = dict(CHECKLISTS_SEED)
    extra = _load_json("checklists.json") or {}
    cl.update(extra)
    return cl


def checklist(name: str):
    return checklists().get((name or "").lower())


# wiki pages (docs/) — key -> (filename, title)
WIKI = {
    "home": ("HOME.md", "fieldcraft — field & preparedness knowledge base"),
    "survival": ("survival.md", "Survival fundamentals"),
    "food-water": ("food-water.md", "Food, water & rations"),
    "medical-tccc": ("medical.md", "Field & tactical medicine"),
    "rucking": ("rucking.md", "Rucking & load-bearing"),
    "land-nav": ("land-nav.md", "Land navigation & terrain"),
    "comms": ("comms.md", "Field communications"),
    "gear-edc": ("gear.md", "Gear, kit & EDC"),
    "preparedness": ("preparedness.md", "Emergency preparedness"),
    "mil-reference": ("mil-reference.md", "Military reference (educational)"),
    "environment": ("environment.md", "Environmental survival"),
    "tools": ("tools.md", "Open-source tools"),
    "acronyms": ("acronyms.md", "Acronyms & terminology"),
    "resources": ("resources.md", "Resources & links"),
    "roles": ("roles-loadouts.md", "Roles & loadouts"),
    # Modern Soldier OS (v0.2) — analytical lessons + defensive/readiness domains
    "lessons": ("lessons.md", "Lessons from recent conflicts (analytical/defensive)"),
    "camouflage-concealment": ("camouflage-concealment.md", "Camouflage & concealment"),
    "night": ("night.md", "Night & limited visibility"),
    "cbrn": ("cbrn.md", "CBRN protective basics (defensive)"),
    "tactical-fitness": ("tactical-fitness.md", "Tactical fitness & human performance"),
    "field-hygiene": ("field-hygiene.md", "Field hygiene & disease prevention"),
    "sop-battle-rhythm": ("sop.md", "SOPs & battle rhythm"),
    "equipment": ("equipment.md", "Military equipment reference (descriptive)"),
}


def wiki_pages() -> dict:
    return dict(WIKI)
