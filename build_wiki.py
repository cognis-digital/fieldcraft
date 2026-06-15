"""Generate the fieldcraft wiki (docs/*.md) + data overlays (data/*.json) from the
fieldcraft-research workflow output. Run after the research completes:
    python build_wiki.py <research_output.json>
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(HERE, "docs")
DATA = os.path.join(HERE, "data")
os.makedirs(DOCS, exist_ok=True)
os.makedirs(DATA, exist_ok=True)

# research domain key -> (docs filename, wiki page title)
PAGE = {
    "survival": ("survival.md", "Survival fundamentals"),
    "food_water_rations": ("food-water.md", "Food, water & rations"),
    "medical_tccc": ("medical.md", "Field & tactical medicine (educational)"),
    "rucking_load": ("rucking.md", "Rucking & load-bearing"),
    "land_nav_terrain": ("land-nav.md", "Land navigation & terrain"),
    "comms": ("comms.md", "Field communications"),
    "gear_edc": ("gear.md", "Gear, kit & EDC"),
    "preparedness": ("preparedness.md", "Emergency preparedness"),
    "mil_reference": ("mil-reference.md", "Military reference (educational)"),
    "environment_sere": ("environment.md", "Environmental survival"),
    "opensource_tools": ("tools.md", "Open-source tools"),
}
DISC = ("> **Disclaimer:** Educational / reference / preparedness material with links "
        "to public and open-source resources. Not operational instructions for "
        "violence or weapons. Verify against primary sources; train with qualified "
        "instructors. Follow all applicable laws.")


def page_md(d):
    title = PAGE.get(d["domain"], (None, d["domain"]))[1]
    out = [f"# {title}", "", DISC, "", d.get("overview", "").strip(), ""]
    for s in d.get("sections", []):
        out.append(f"## {s['title']}\n\n{s['content'].strip()}\n")
    for cl in d.get("checklists", []):
        out.append(f"### Checklist: {cl['name']}\n")
        out += [f"- [ ] {i}" for i in cl.get("items", [])]
        out.append("")
    if d.get("resources"):
        out.append("## Resources & links\n")
        for r in d["resources"]:
            note = f" — {r['note']}" if r.get("note") else ""
            out.append(f"- [{r.get('name','link')}]({r['url']}){note}")
        out.append("")
    return "\n".join(out)


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else None
    doc = json.load(open(src, encoding="utf-8"))
    domains = doc.get("domains") or doc.get("result", {}).get("domains") or doc
    if isinstance(domains, dict):
        domains = domains.get("domains", [])

    all_acr, all_res, all_cl = {}, {}, {}
    written = []
    for d in domains:
        dk = d.get("domain")
        if dk in PAGE:
            fn = PAGE[dk][0]
            open(os.path.join(DOCS, fn), "w", encoding="utf-8").write(page_md(d))
            written.append(fn)
        for a in d.get("acronyms", []):
            t = (a.get("term") or "").strip()
            if t:
                all_acr[t.upper()] = {"term": t, "expansion": a.get("expansion", ""),
                                      "domain": dk, "note": a.get("note", "")}
        for r in d.get("resources", []):
            if r.get("url"):
                all_res[r["url"]] = {"name": r.get("name", ""), "type": r.get("type", ""),
                                     "url": r["url"], "domain": dk, "note": r.get("note", "")}
        for cl in d.get("checklists", []):
            if cl.get("name"):
                all_cl[cl["name"].lower().replace(" ", "-")] = cl.get("items", [])

    json.dump(list(all_acr.values()), open(os.path.join(DATA, "acronyms.json"), "w", encoding="utf-8"), indent=2)
    json.dump(list(all_res.values()), open(os.path.join(DATA, "resources.json"), "w", encoding="utf-8"), indent=2)
    json.dump(all_cl, open(os.path.join(DATA, "checklists.json"), "w", encoding="utf-8"), indent=2)

    # acronyms.md
    am = ["# Acronyms & terminology", "", DISC, "",
          f"{len(all_acr)} terms across military / tactical / survival / medical / comms.", ""]
    for a in sorted(all_acr.values(), key=lambda x: x["term"].upper()):
        note = f" — {a['note']}" if a.get("note") else ""
        am.append(f"- **{a['term']}** — {a['expansion']}{note}")
    open(os.path.join(DOCS, "acronyms.md"), "w", encoding="utf-8").write("\n".join(am))

    # HOME index
    home = ["# fieldcraft — field & preparedness knowledge base", "", DISC, "",
            "A practical, wiki-style reference for soldiers and civilians: survival, "
            "food/water, field medicine, rucking, navigation, comms, gear, preparedness, "
            "and a role/loadout builder. Use the `fieldcraft` CLI to query it.", "",
            "## Pages", ""]
    for dk, (fn, title) in PAGE.items():
        home.append(f"- [{title}](docs/{fn})")
    home += ["- [Acronyms & terminology](docs/acronyms.md)",
             "- [Roles & loadouts](docs/roles-loadouts.md)", ""]
    open(os.path.join(DOCS, "HOME.md"), "w", encoding="utf-8").write("\n".join(home))

    print(f"wiki: {len(written)} domain pages + acronyms.md + HOME.md")
    print(f"data: {len(all_acr)} acronyms, {len(all_res)} resources, {len(all_cl)} checklists")


if __name__ == "__main__":
    main()
