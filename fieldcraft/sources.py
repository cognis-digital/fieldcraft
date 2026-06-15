"""
Authoritative public sources for military-equipment reference data.

The fieldcraft equipment catalog is a curated, descriptive starter set. The complete,
authoritative datasets — the ones with tens of thousands of systems — are maintained
by the organizations below. This module is the gateway to them. ODIN (the U.S. Army
TRADOC OE Data Integration Network, which hosts the Worldwide Equipment Guide / WEG)
is the canonical public threat-equipment reference.
"""

SOURCES = [
    {"name": "ODIN — OE Data Integration Network (WEG)", "org": "U.S. Army TRADOC G-2",
     "url": "https://odin.tradoc.army.mil/", "type": "primary-database",
     "note": "Public Worldwide Equipment Guide: thousands of systems with descriptive data."},
    {"name": "Wikipedia — Lists of military equipment", "org": "Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Lists_of_weapons", "type": "encyclopedia",
     "note": "Extensive 'List of …' sets per country/type/era."},
    {"name": "Military-Today", "org": "Military-Today", "url": "https://www.military-today.com/",
     "type": "reference", "note": "Descriptive specs/photos across categories."},
    {"name": "GlobalSecurity.org", "org": "GlobalSecurity", "url": "https://www.globalsecurity.org/military/systems/",
     "type": "reference", "note": "Systems reference and background."},
    {"name": "The Military Balance (IISS)", "org": "IISS", "url": "https://www.iiss.org/publications/the-military-balance/",
     "type": "reference", "note": "Annual order-of-battle / inventories (paywalled summary)."},
    {"name": "SIPRI Arms Transfers Database", "org": "SIPRI", "url": "https://www.sipri.org/databases/armstransfers",
     "type": "database", "note": "Who operates/transfers what (open)."},
    {"name": "Oryx (visually-confirmed losses)", "org": "Oryx", "url": "https://www.oryxspioenkop.com/",
     "type": "osint", "note": "OSINT equipment-loss documentation (recent conflicts)."},
    {"name": "WWII / historical: Tank Encyclopedia", "org": "tanks-encyclopedia.com",
     "url": "https://tanks-encyclopedia.com/", "type": "reference", "note": "Historical armor reference."},
    {"name": "FAS World Forces / weapons", "org": "Federation of American Scientists",
     "url": "https://fas.org/", "type": "reference", "note": "Open analysis + system references."},
    {"name": "Cognis: awesome-drone-warfare-osint", "org": "cognis-digital",
     "url": "https://github.com/cognis-digital/awesome-drone-warfare-osint", "type": "cognis",
     "note": "Citation-grade drone/component OSINT dataset."},
    {"name": "Cognis: frontline-drones", "org": "cognis-digital",
     "url": "https://github.com/cognis-digital/frontline-drones", "type": "cognis",
     "note": "Descriptive drone + autonomy-platform catalog."},
]


def sources(kind: str = None) -> list:
    return [s for s in SOURCES if not kind or s["type"] == kind] if kind else list(SOURCES)
