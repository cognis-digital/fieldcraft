"""fieldcraft — a practical preparedness, survival & field-reference knowledge base
+ loadout builder, for soldiers and civilians. Educational/reference use.

  roles                          list roles you can "build"
  loadout <role>[,<role>...] [--tier edc|24h|72h|sustainment]   compose a kit
  acronym <TERM>                 look up a term
  acronyms [--search Q]          list / search the glossary
  resources [--domain D]         curated public/open-source links
  guides [--domain D]            public mil/IC doctrine & manuals (FM/TC/ATP/JP/NIST/STIG)
  cognis                         related Cognis repos for field use
  checklist <name>               a printable checklist (go-bag-72h, ifak, ...)
  checklists                     list available checklists
  wiki [page]                    list wiki pages (docs/) or show where one lives
  search <Q>                     search acronyms + resources

--format table|json
"""
from __future__ import annotations
import argparse
import json
import os

from . import (loadouts, acronyms, catalog, lessons as lessonsmod, sop as sopmod,
               equipment as equipmod, sources as srcmod)
from .loadouts import TOOL_NAME, TOOL_VERSION


def _j(o): print(json.dumps(o, indent=2, default=lambda x: getattr(x, "to_dict", lambda: str(x))()))


def cmd_roles(a):
    rs = loadouts.list_roles()
    if a.format == "json": _j([r.to_dict() for r in rs]); return 0
    for r in rs:
        print(f"{r.key:14} {r.name:34} {r.summary}")
    return 0


def cmd_loadout(a):
    roles = [r.strip() for r in a.roles.split(",") if r.strip()]
    unknown = [r for r in roles if not loadouts.get_role(r)]
    if unknown:
        print(f"unknown role(s): {', '.join(unknown)}; see `fieldcraft roles`"); return 2
    b = loadouts.build(roles, a.tier)
    if a.format == "json": _j(b); return 0
    print(f"# Loadout — {', '.join(b['roles'])}  (tier: {b['tier']})\n")
    for tier, items in b["kit"].items():
        print(f"## {tier}")
        for it in items:
            print(f"  - {it}")
    print(f"\nskills: {', '.join(b['skills'])}")
    print(f"learn: {', '.join(b['references'])}  (see `fieldcraft wiki`)")
    if b["cognis_repos"]:
        print(f"cognis: {', '.join(b['cognis_repos'])}")
    return 0


def cmd_acronym(a):
    d = acronyms.lookup(a.term)
    if not d:
        hits = acronyms.search(a.term)
        if hits:
            print(f"no exact match; did you mean: {', '.join(h['term'] for h in hits[:8])}"); return 1
        print(f"unknown term '{a.term}'"); return 1
    if a.format == "json": _j(d); return 0
    print(f"{d['term']} — {d['expansion']}" + (f"  [{d['domain']}]" if d['domain'] else ""))
    if d.get("note"): print(f"  {d['note']}")
    return 0


def cmd_acronyms(a):
    items = acronyms.search(a.search) if a.search else acronyms.all_terms()
    if a.format == "json": _j(items); return 0
    for d in items:
        print(f"{d['term']:16} {d['expansion']}")
    print(f"\n({len(items)} of {acronyms.count()} terms)")
    return 0


def cmd_resources(a):
    rs = catalog.resources(a.domain)
    if a.format == "json": _j(rs); return 0
    for r in rs:
        print(f"[{r.get('domain',''):12}] {r['name']:38} {r['url']}")
    return 0


def cmd_guides(a):
    rs = catalog.military_guides(a.domain)
    if a.format == "json": _j(rs); return 0
    for r in rs:
        print(f"[{r.get('domain',''):12}] {r['name']:48} {r['url']}")
    print(f"\n{len(rs)} guide(s). Domains: weapons, tactics, recon, fires, comms, "
          "aviation, medical, cbrn, engineer, counter-uas, fieldcraft, doctrine, cyber, intel, reference")
    return 0


def cmd_cognis(a):
    rs = catalog.cognis_resources()
    if a.format == "json": _j(rs); return 0
    for r in rs:
        print(f"{r['repo']:42} {r['use']}")
    return 0


def cmd_checklist(a):
    items = catalog.checklist(a.name)
    if items is None:
        print(f"unknown checklist '{a.name}'; see `fieldcraft checklists`"); return 1
    if a.format == "json": _j({a.name: items}); return 0
    print(f"# {a.name}")
    for it in items:
        print(f"  [ ] {it}")
    return 0


def cmd_checklists(a):
    cl = catalog.checklists()
    if a.format == "json": _j(list(cl)); return 0
    for k, v in cl.items():
        print(f"{k:16} ({len(v)} items)")
    return 0


def cmd_wiki(a):
    pages = catalog.wiki_pages()
    if a.page:
        p = pages.get(a.page)
        if not p:
            print(f"unknown page '{a.page}'; see `fieldcraft wiki`"); return 1
        print(f"docs/{p[0]}  —  {p[1]}"); return 0
    if a.format == "json": _j(pages); return 0
    for k, (fn, title) in pages.items():
        print(f"{k:14} docs/{fn:22} {title}")
    return 0


def cmd_lessons(a):
    items = lessonsmod.list_lessons(a.domain)
    if a.format == "json": _j([l.to_dict() for l in items]); return 0
    for l in items:
        print(f"{l.id:10} [{l.domain:16}] {l.lesson}")
        print(f"            -> {l.takeaway}")
    print(f"\n({len(items)} of {lessonsmod.count()} lessons; domains: {', '.join(lessonsmod.DOMAINS)})")
    return 0


def cmd_lesson(a):
    l = lessonsmod.get_lesson(a.id)
    if not l:
        print(f"unknown lesson '{a.id}'; see `fieldcraft lessons`"); return 1
    _j(l.to_dict()); return 0


def cmd_sop(a):
    if a.name:
        s = sopmod.get_sop(a.name)
        if not s:
            print(f"unknown SOP '{a.name}'; see `fieldcraft sop`"); return 1
        if a.format == "json": _j(s.to_dict()); return 0
        print(f"# {s.name}\n{s.purpose}\n")
        for st in s.steps:
            print(f"  {st}")
        return 0
    sl = sopmod.list_sops()
    if a.format == "json": _j([s.to_dict() for s in sl]); return 0
    for s in sl:
        print(f"{s.key:20} {s.name:38} {s.purpose}")
    return 0


def cmd_os(a):
    modules = {
        "roles / loadout": "build a role's kit + skills + references (`fieldcraft roles`/`loadout`)",
        "wiki": f"{len(catalog.wiki_pages())} reference pages (`fieldcraft wiki`)",
        "acronyms": f"{acronyms.count()} terms (`fieldcraft acronyms`)",
        "lessons": f"{lessonsmod.count()} modern-conflict lessons, defensive takeaways (`fieldcraft lessons`)",
        "sop": "readiness SOPs & battle rhythm (`fieldcraft sop`)",
        "checklists": "printable checklists (`fieldcraft checklists`)",
        "resources": "curated public + open-source links (`fieldcraft resources`)",
        "cognis": "interop with the Cognis suite (`fieldcraft cognis`)",
    }
    if a.format == "json": _j(modules); return 0
    print(f"# fieldcraft — Modern Soldier OS v{TOOL_VERSION}\n"
          f"An educational/reference readiness OS for soldiers and civilians.\n")
    for k, v in modules.items():
        print(f"  {k:18} {v}")
    print("\nEducational/reference only — see the disclaimer in README.md.")
    return 0


def cmd_equipment(a):
    items = equipmod.all_items(a.category, a.origin)
    if a.search:
        items = [i for i in equipmod.search(a.search)
                 if (not a.category or i.category == a.category)]
    if a.format == "json": _j([i.to_dict() for i in items]); return 0
    for i in items:
        print(f"{i.name:30} {i.category:18} {i.origin:16} {i.role}")
    cats = equipmod.categories()
    print(f"\n({len(items)} shown · {equipmod.count()} total across {len(cats)} categories) "
          f"— full datasets via `fieldcraft sources`")
    return 0


def cmd_equip_show(a):
    it = equipmod.get(a.id)
    if not it:
        print(f"unknown item '{a.id}'"); return 1
    _j(it.to_dict()); return 0


def cmd_sources(a):
    s = srcmod.sources()
    if a.format == "json": _j(s); return 0
    for r in s:
        print(f"[{r['type']:16}] {r['name']:42} {r['url']}")
    print("\nODIN (TRADOC) is the canonical public threat-equipment reference.")
    return 0


def cmd_search(a):
    out = {"acronyms": acronyms.search(a.query),
           "resources": [r for r in catalog.resources()
                         if a.query.lower() in (r["name"] + r.get("note", "")).lower()]}
    _j(out); return 0


def build_parser():
    p = argparse.ArgumentParser(prog=TOOL_NAME, description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--version", action="version", version=f"{TOOL_NAME} {TOOL_VERSION}")
    sub = p.add_subparsers(dest="command")

    def add(n, fn):
        sp = sub.add_parser(n); sp.add_argument("--format", choices=["table", "json"], default="table")
        sp.set_defaults(func=fn); return sp

    add("roles", cmd_roles)
    sp = add("loadout", cmd_loadout); sp.add_argument("roles"); sp.add_argument("--tier", default="72h")
    sp = add("acronym", cmd_acronym); sp.add_argument("term")
    sp = add("acronyms", cmd_acronyms); sp.add_argument("--search")
    sp = add("resources", cmd_resources); sp.add_argument("--domain")
    sp = add("guides", cmd_guides); sp.add_argument("--domain")
    add("cognis", cmd_cognis)
    sp = add("checklist", cmd_checklist); sp.add_argument("name")
    add("checklists", cmd_checklists)
    sp = add("wiki", cmd_wiki); sp.add_argument("page", nargs="?")
    sp = add("lessons", cmd_lessons); sp.add_argument("--domain")
    sp = add("lesson", cmd_lesson); sp.add_argument("id")
    sp = add("sop", cmd_sop); sp.add_argument("name", nargs="?")
    add("os", cmd_os)
    sp = add("equipment", cmd_equipment); sp.add_argument("--category")
    sp.add_argument("--origin"); sp.add_argument("--search")
    sp = add("equip-show", cmd_equip_show); sp.add_argument("id")
    add("sources", cmd_sources)
    sp = add("search", cmd_search); sp.add_argument("query")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    if not getattr(args, "command", None):
        build_parser().print_help(); return 2
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
