# fieldcraft

> A practical, wiki-style **preparedness, survival & field-reference knowledge base**
> for soldiers and civilians — plus a **role/loadout builder** ("build your character,
> but for real life"). Survival, food & water, field medicine, rucking, land-nav,
> comms, gear, and emergency preparedness, with a CLI to query it all and links to
> public + open-source resources.

[![Code License: COCL 1.0](https://img.shields.io/badge/License-COCL%201.0-6b46c1.svg)](LICENSE)
[![tests](https://img.shields.io/badge/tests-15%20passing-2ea44f.svg)](tests/)
[![version](https://img.shields.io/badge/Modern%20Soldier%20OS-v0.2-1f6feb.svg)](docs/HOME.md)

> **Disclaimer — read first.** fieldcraft is **educational / reference / preparedness**
> material with links to public and open-source resources (public-domain field
> manuals, FEMA/Ready.gov, Red Cross, Stop the Bleed / TCCC, recognized outdoors and
> radio orgs, open-source tools). It is **not** operational instructions for violence
> and contains **nothing** about making weapons, ammunition, or explosives; military
> doctrine is referenced descriptively (what it is and where the public manual lives).
> Medical content is general first-aid education — **not** a substitute for training
> or professional care. Train with qualified instructors, verify against primary
> sources, and follow all applicable laws.

<!-- cognis:layman:start -->
## What is this?

If you've ever wanted one organized place that tells you *what to carry, what to
learn, and where to learn it* for being ready in the field — whether you're a soldier,
a prepper, a hiker, a volunteer first responder, or just someone who wants a solid
go-bag — that's fieldcraft. It's a small, offline, no-dependency toolkit plus a
wiki: ask it to build a "loadout" for a role (medic, navigator, comms, rucker,
survivalist, logistics, scout) and it gives you a realistic, layered kit list, the
skills that role assumes, and the reference pages to learn them. Look up any acronym
(METT-TC, MARCH, PACE, IFAK…). Pull a printable checklist (72-hour go-bag, IFAK, ruck
packing, water). And browse curated links to the best free, public, and open-source
material on each topic. Build your real-life character — kit, skills, and knowledge.
<!-- cognis:layman:end -->

## Modern Soldier OS (v0.2)

fieldcraft is organized as a personal readiness "OS" — run `fieldcraft os` for the
module map. On top of the survival/preparedness base it adds:

- **Lessons from recent & ongoing conflicts** (`fieldcraft lessons`) — analytical,
  individual-focused takeaways (drones/UAS, counter-UAS, EW & GPS denial, pervasive
  ISR & signature management, prolonged combat medicine, logistics, dispersion,
  resilience) in the spirit of RUSI / West Point MWI / CSIS lessons-learned. The
  emphasis is **protective, medical, survival, and resilience** takeaways — what
  changed and how to *survive and endure* it, not how to attack.
- **Defensive/readiness domains** — camouflage & concealment (incl. thermal/drone-era),
  night & limited visibility, CBRN protective basics, tactical fitness & human
  performance, field hygiene & disease prevention.
- **SOPs & battle rhythm** (`fieldcraft sop`) — TLP, priorities of work, PCC/PCI, AAR,
  PACE, security halts, stand-to — readiness discipline (descriptive).
- **More roles** — team leader, drone-threat/counter-UAS observer, pioneer/field
  engineer (protective works), alongside medic, navigator, comms, rucker, survivalist,
  logistics, scout.

## Use it

```sh
fieldcraft roles                                   # the roles you can build
fieldcraft loadout medic,navigator --tier 72h      # compose a kit + skills + refs
fieldcraft acronym MARCH                            # look up a term
fieldcraft acronyms --search medevac                # search the glossary
fieldcraft checklist go-bag-72h                     # a printable checklist
fieldcraft resources --domain medical               # curated public/open links
fieldcraft wiki                                      # the docs/ knowledge base pages
fieldcraft cognis                                    # related Cognis repos for field use
```

## What's inside

- **Loadout builder** (`fieldcraft/loadouts.py`) — 7 composable roles → tiered kit
  (EDC → 24h → 72h → sustainment) + skills + references.
- **Acronym glossary** (`fieldcraft/acronyms.py` + `data/acronyms.json`) — military /
  tactical / survival / medical / comms terms.
- **Resource catalog** (`fieldcraft/catalog.py` + `data/resources.json`) — public
  manuals, FEMA/Red Cross/Stop-the-Bleed, ARRL, and open-source tools (QGIS, OSM,
  OsmAnd, CivTAK, CHIRP, Kiwix…).
- **Checklists** — go-bag, IFAK, ruck-packing, water.
- **Wiki** (`docs/`) — pages on survival, food & water, field medicine, rucking,
  land-nav, comms, gear, preparedness, military reference, environment, built from
  sourced research.

## Interoperates with the Cognis suite

`fieldcraft cognis` maps field/preparedness work to our tools: **labforge** (plan the
hardware/kit for a comms or offline-AI field node), **edgemesh** (run offline
reference models across field devices), **agentforge** (stand up assistant roles for
planning/checklists), and the OSINT/awareness repos (descriptive situational
awareness). Links to popular open-source tools throughout.

<!-- cognis:install:start -->
## Install

```sh
curl -fsSL https://raw.githubusercontent.com/cognis-digital/fieldcraft/HEAD/install.sh | sh   # Linux/macOS
```
```powershell
irm https://raw.githubusercontent.com/cognis-digital/fieldcraft/HEAD/install.ps1 | iex        # Windows
```
```sh
pipx install "git+https://github.com/cognis-digital/fieldcraft.git"   # or uv tool install / pip install
git clone https://github.com/cognis-digital/fieldcraft.git && cd fieldcraft && pip install .  # source
```
Then: `fieldcraft --help`
<!-- cognis:install:end -->

## Topics / Domains

`survival` · `preparedness` · `first-aid` · `land-navigation` · `rucking` · `edc` ·
`emergency-preparedness` · `reference` · part of the **Cognis Neural Suite**.

## License

Cognis Open Collaboration License (COCL) 1.0 — see [LICENSE](LICENSE).
