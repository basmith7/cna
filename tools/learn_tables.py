#!/usr/bin/env python3
"""Render data/tables/*.json combat tables as HTML for the site's Learn page (mission Part D).

Errata overlays in data/errata/ are applied first, so the page shows the post-errata values
(base files stay as printed in 1979). Each table carries a spi-ref badge for its case and
names its data file.

  python3 tools/learn_tables.py barrage-results   # prints the HTML fragment
"""
import html
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

RESULT_LABELS = {"no-effect": "no effect", "pinned": "pinned", "lose-1": "lose 1", "lose-2": "lose 2"}
DASH = "—"


def _apply(obj, op):
    """Apply one RFC 6902 add/remove/replace operation in place."""
    parts = [p.replace("~1", "/").replace("~0", "~") for p in op["path"].lstrip("/").split("/")]
    node = obj
    for key in parts[:-1]:
        node = node[int(key)] if isinstance(node, list) else node[key]
    last = parts[-1]
    if isinstance(node, list):
        idx = len(node) if last == "-" else int(last)
        if op["op"] == "add":
            node.insert(idx, op["value"])
        elif op["op"] == "remove":
            del node[idx]
        else:
            node[idx] = op["value"]
    elif op["op"] == "remove":
        del node[last]
    else:
        node[last] = op["value"]


def load_table(name):
    """The table with every errata overlay that targets it applied, in id order."""
    t = json.loads((DATA / "tables" / f"{name}.json").read_text())
    for p in sorted((DATA / "errata").glob("E-*.json")):
        e = json.loads(p.read_text())
        if e["table"] == name:
            for op in e["patches"]:
                _apply(t, op)
    return t


def _case(t):
    return next(s.split(":", 1)[1] for s in t["sources"] if s.startswith("CNA1979:"))


def _rng(r):
    if r is None:
        return DASH
    return str(r["from"]) if r["from"] == r["to"] else f"{r['from']}–{r['to']}"


def _col_label(c):
    return html.escape(c["id"].replace("-", "–") if c["id"][0].isdigit() else c["id"])


def _wrap(t, title, body):
    case = _case(t)
    badge = (f'<p class="learn-table-ref"><span class="spi-badge spi-ref">SPI {case}</span> '
             f'<code>data/tables/{t["table"]}.json</code></p>')
    return f'<div class="learn-table" data-table="{t["table"]}"><h4>{html.escape(title)}</h4>{badge}{body}</div>'


def render_barrage(t):
    cols = t["columns"]
    out = []
    for cls in ("infantry", "armor", "gun", "truck"):
        rows = [r for r in t["rows"] if r["class"] == cls]
        results = [k for k in RESULT_LABELS if any(r["result"] == k for r in rows)]
        head = "".join(f"<th>{_col_label(c)}</th>" for c in cols)
        body = []
        for res in results:
            cells = []
            for c in cols:
                m = [r for r in rows if r["column"] == c["id"] and r["result"] == res]
                cells.append(f"<td>{_rng(m[0]['dice']) if m else DASH}</td>")
            body.append(f"<tr><th>{RESULT_LABELS[res]}</th>{''.join(cells)}</tr>")
        out.append(f'<table class="crt"><caption>vs {cls}</caption><thead><tr><th>result \\ points</th>{head}</tr></thead>'
                   f'<tbody>{"".join(body)}</tbody></table>')
    return _wrap(t, "Barrage against land units", "".join(out))


def render_anti_armour(t):
    cols = t["columns"]
    head = "".join(f"<th>{_col_label(c)}</th>" for c in cols)
    body = "".join(
        f"<tr><th>{html.escape(str(r['dice']))}</th>" + "".join(
            f"<td>{DASH if r['damage'].get(c['id']) is None else r['damage'][c['id']]}</td>" for c in cols) + "</tr>"
        for r in t["rows"])
    table = f'<table class="crt"><thead><tr><th>roll \\ points</th>{head}</tr></thead><tbody>{body}</tbody></table>'
    return _wrap(t, "Anti-armour fire: damage points", table)


SUM_ROWS = {"attacker": [("engaged", "engaged"), ("capture_attacker", "captured")],
            "defender": [("retreat_1", "retreat 1"), ("retreat_2", "retreat 2"), ("retreat_3", "retreat 3"), ("capture_defender", "captured")]}


def render_close_assault(t):
    cols = t["columns"]

    def th(c):
        label = html.escape(c["id"].replace("-", "−"))
        return f'<th class="overrun">{label}</th>' if c.get("overrun") else f"<th>{label}</th>"

    head = "".join(th(c) for c in cols)
    out = []
    for side in ("attacker", "defender"):
        losses = t["losses"][side]
        body = []
        for pct in sorted(losses, key=lambda k: -int(k)):
            body.append(f"<tr><th>{pct} %</th>" + "".join(f"<td>{_rng(losses[pct].get(c['id']))}</td>" for c in cols) + "</tr>")
        for key, label in SUM_ROWS[side]:
            sums = t["sums"][key]
            body.append(f"<tr><th>{label}</th>" + "".join(
                f"<td>{', '.join(str(n) for n in sums[c['id']]) if sums.get(c['id']) else DASH}</td>" for c in cols) + "</tr>")
        out.append(f'<table class="crt"><caption>{side}</caption><thead><tr><th>losses \\ differential</th>{head}</tr></thead>'
                   f'<tbody>{"".join(body)}</tbody></table>')
    return _wrap(t, "Close assault: losses by sequential roll, engaged / retreat / captured by sum", "".join(out))


RENDERERS = {"barrage-results": render_barrage, "anti-armour-results": render_anti_armour,
             "close-assault-results": render_close_assault}


def render(name):
    return RENDERERS[name](load_table(name))


if __name__ == "__main__":
    print(render(sys.argv[1]))
