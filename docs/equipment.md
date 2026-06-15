# Military equipment reference (descriptive)

> **Disclaimer:** This is a **descriptive / identification** reference — designation,
> type, country of origin, role, era, class, operators — the same neutral, encyclopedic
> data found in public references and the U.S. Army's public ODIN / Worldwide Equipment
> Guide. It contains **no** employment, targeting, lethality, or how-to-use/defeat
> content. For recognition, study, and reference only.

## What's here

A curated, descriptive catalog of military systems organized by category under
`data/equipment/*.json` (add a file to add a category). Query it:

```sh
fieldcraft equipment                       # everything
fieldcraft equipment --category armored-vehicles
fieldcraft equipment --origin "United States"
fieldcraft equipment --search fighter
fieldcraft equip-show m1-abrams
fieldcraft sources                          # the authoritative public databases
```

Categories: small arms, crew-served, armored vehicles, artillery, air defense,
fixed-wing aircraft, rotary aircraft, UAS, naval, missiles, support vehicles,
C2/EW/sensors, individual kit.

## Scale & sourcing — use the authoritative public databases

This catalog is a **curated starter set** of well-known systems. The complete,
authoritative datasets — with tens of thousands of entries — are maintained by the
public sources in `fieldcraft sources`, chief among them:

- **ODIN (OE Data Integration Network)** — U.S. Army TRADOC G-2's public Worldwide
  Equipment Guide: <https://odin.tradoc.army.mil/>
- **Wikipedia "Lists of weapons / military equipment"**, **Military-Today**,
  **GlobalSecurity**, **IISS Military Balance**, **SIPRI**, and OSINT efforts like
  **Oryx**.

We link these rather than fabricate entries to inflate a count — accurate descriptive
data + a gateway to the comprehensive sources is more useful (and honest) than invented
specs. To extend the local catalog, add real, sourced entries as new files under
`data/equipment/`.

## See also

`fieldcraft cognis` (drone-OSINT datasets: awesome-drone-warfare-osint, frontline-drones) ·
`mil-reference` · `lessons`.
