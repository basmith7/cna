#!/usr/bin/env python3
"""Build the decision board: one local page with every question waiting on Brian.

  python3 tools/decisions_page.py [out] [--probes DIR]   # default build/decisions.html (git-ignored)

It gathers every `proposed` ruling in rulings/ (problem, options, our rationale) and the
non-ruling questions in docs/autopilot/decisions.json. Choices persist in the browser's
localStorage; "Copy as Feedback" puts a Markdown block on the clipboard for the Feedback
section of docs/autopilot/PROGRESS.md, which the next autopilot run acts on.

--probes points at cna-engine's probes/ directory: each <id>.json there is drawn as a chart
inside the card with the same id (a ruling or a decisions.json item).
"""
import html
import json
import pathlib
import re
import sys
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO_URL = "https://github.com/basmith7/cna/blob/main"


def _inline(text: str) -> str:
    s = html.escape(text, quote=False)
    s = re.sub(r"\[\^[^\]]+\]", "", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"&lt;(https?://[^&\s]+)&gt;", r'<a href="\1">\1</a>', s)
    return s


def md_blocks(md: str) -> str:
    """Paragraphs, blockquotes and lists; footnote definitions dropped."""
    out = []
    for block in re.split(r"\n\s*\n", md.strip()):
        lines = block.splitlines()
        if not lines or lines[0].startswith("[^"):
            continue
        if all(l.startswith(">") for l in lines):
            text = " ".join(l.lstrip("> ").strip() for l in lines)
            out.append(f"<blockquote>{_inline(text)}</blockquote>")
        elif re.match(r"\s*([-*]|\d+\.)\s", lines[0]):
            items, cur = [], []
            for l in lines:
                if re.match(r"\s*([-*]|\d+\.)\s", l) and cur:
                    items.append(" ".join(cur))
                    cur = []
                cur.append(re.sub(r"^\s*([-*]|\d+\.)\s+", "", l).strip())
            items.append(" ".join(cur))
            out.append("<ul>" + "".join(f"<li>{_inline(i)}</li>" for i in items) + "</ul>")
        else:
            out.append(f"<p>{_inline(' '.join(l.strip() for l in lines))}</p>")
    return "\n".join(out)


def _section(md: str, name: str) -> str:
    m = re.search(rf"^## {name}\s*\n(.*?)(?=^## |\Z)", md, re.M | re.S)
    return m.group(1) if m else ""


def parse_ruling(md: str) -> dict:
    fm = {k: (re.search(rf"^{k}:\s*(.+?)\s*$", md, re.M) or [None, ""])[1]
          for k in ("id", "status", "affects")}
    title = re.search(r"^#\s+\S+\s+—\s+(.+?)\s*$", md, re.M)
    options = []
    for m in re.finditer(r"^\d+\.\s+(.*?)(?=^\d+\.\s|\Z)", _section(md, "Options"), re.M | re.S):
        body = " ".join(l.strip() for l in m.group(1).splitlines() if l.strip())
        label = re.match(r"\*\*(.+?)\*\*", body)
        options.append({"label": label.group(1) if label else body[:60], "html": _inline(body)})
    return {
        "id": fm["id"],
        "status": fm["status"],
        "affects": ", ".join(x.strip() for x in fm["affects"].strip("[]").split(",") if x.strip()),
        "title": title.group(1) if title else fm["id"],
        "problem": md_blocks(_section(md, "Problem")),
        "rationale": md_blocks(_section(md, "Rationale")),
        "options": options,
    }


def open_rulings(root: pathlib.Path) -> list[dict]:
    out = []
    for p in sorted((root / "rulings").glob("R-*.md")):
        r = parse_ruling(p.read_text())
        if r["status"] == "proposed":
            r["file"] = f"rulings/{p.name}"
            out.append(r)
    return out


SERIES_COLOURS = ["#1f6fb2", "#c7722b", "#6b4fa0", "#2e8b57"]  # validated: dataviz validate_palette.js, light


def _num(v: float) -> str:
    return f"{v:.1f}".rstrip("0").rstrip(".")


def render_probe(p: dict) -> str:
    """One probe result as an inline SVG chart, legend, finding and a data table."""
    esc = lambda t: html.escape(str(t))
    xs, series = p["x"]["values"], p["series"][: len(SERIES_COLOURS)]
    W, H, L, R, T, B = 640, 260, 44, 12, 12, 44
    top = max([v for s in series for v in s["values"]] + [1.0])
    top = next(n for n in (1, 2, 5, 10, 20, 25, 50, 100, 200, 500, 1000, 10**9) if n >= top)
    y = lambda v: T + (H - T - B) * (1 - v / top)
    step = (W - L - R) / max(len(xs), 1)
    cx = lambda i: L + step * (i + 0.5)
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{esc(p["question"])}" class="probe-svg">']
    for k in range(5):
        v = top * k / 4
        out.append(f'<line x1="{L}" x2="{W - R}" y1="{y(v):.1f}" y2="{y(v):.1f}" class="grid"/>'
                   f'<text x="{L - 6}" y="{y(v) + 4:.1f}" class="tick" text-anchor="end">{_num(v)}</text>')
    every = max(1, len(xs) // 9)
    for i, x in enumerate(xs):
        if i % every == 0 or i == len(xs) - 1:
            out.append(f'<text x="{cx(i):.1f}" y="{H - B + 16}" class="tick" text-anchor="middle">{esc(x)}</text>')
    out.append(f'<text x="{(L + W - R) / 2}" y="{H - 6}" class="axis" text-anchor="middle">{esc(p["x"]["label"])}</text>')
    if p.get("kind") == "bar":
        n = len(series)
        bw = max(4.0, (step - 8) / n - 2)
        for si, s in enumerate(series):
            for i, v in enumerate(s["values"]):
                x0 = cx(i) - (n * (bw + 2)) / 2 + si * (bw + 2)
                out.append(f'<rect x="{x0:.1f}" y="{y(v):.1f}" width="{bw:.1f}" height="{max(y(0) - y(v), 0):.1f}" '
                           f'rx="2" fill="{SERIES_COLOURS[si]}"><title>{esc(s["label"])}, {esc(xs[i])}: {_num(v)}</title></rect>')
    else:
        for si, s in enumerate(series):
            pts = " ".join(f"{cx(i):.1f},{y(v):.1f}" for i, v in enumerate(s["values"]))
            out.append(f'<polyline points="{pts}" fill="none" stroke="{SERIES_COLOURS[si]}" stroke-width="2"/>')
            for i, v in enumerate(s["values"]):
                out.append(f'<circle cx="{cx(i):.1f}" cy="{y(v):.1f}" r="4" fill="{SERIES_COLOURS[si]}" stroke="#f6f7f3" stroke-width="2">'
                           f'<title>{esc(s["label"])}, {esc(xs[i])}: {_num(v)}</title></circle>')
    out.append("</svg>")
    legend = "".join(f'<li><span class="swatch" style="background:{SERIES_COLOURS[i]}"></span>{esc(s["label"])}</li>'
                     for i, s in enumerate(series)) if len(series) > 1 else ""
    rows = "".join(f"<tr><th>{esc(x)}</th>" + "".join(f"<td>{_num(s['values'][i])}</td>" for s in series) + "</tr>"
                   for i, x in enumerate(xs))
    table = (f'<details><summary>Data table</summary><table><thead><tr><th>{esc(p["x"]["label"])}</th>'
             + "".join(f"<th>{esc(s['label'])}</th>" for s in series) + f"</tr></thead><tbody>{rows}</tbody></table></details>")
    return (f'<figure class="probe"><figcaption><strong>Probe:</strong> {esc(p["question"])} '
            f'<span class="unit">({esc(p["y"]["label"])})</span></figcaption>'
            + "".join(out) + (f'<ul class="legend">{legend}</ul>' if legend else "")
            + f'<p class="finding">{esc(p["finding"])}</p>{table}'
            + f'<p class="prov">cna-engine, rules at {esc(p["rules_commit"][:10])}</p></figure>')


def _probes(d: pathlib.Path | None) -> dict[str, str]:
    if d is None or not d.is_dir():
        return {}
    out = {}
    for f in sorted(d.glob("*.json")):
        p = json.loads(f.read_text())
        out[p["id"]] = render_probe(p)
    return out


def _items(root: pathlib.Path) -> tuple[dict, list[dict]]:
    data = json.loads((root / "docs/autopilot/decisions.json").read_text())
    groups = {"copy": data["groups"]["copy"], "rulings": "Rulings"} | data["groups"]
    items = [{
        "id": r["id"], "group": "rulings", "title": r["title"],
        "meta": f"SPI {r['affects']}", "link": f"{REPO_URL}/{r['file']}",
        "context": r["problem"], "rationale": r["rationale"],
        "options": [{"label": o["label"], "html": o["html"]} for o in r["options"]]
        + [{"label": "Reject all options", "html": "Reject: none of these; say why in the note."}],
    } for r in open_rulings(root)]
    for it in data["items"]:
        items.append({
            "id": it["id"], "group": it["group"], "title": it["title"], "meta": "",
            "link": "", "context": f"<p>{_inline(it['context'])}</p>", "rationale": "",
            "options": [{"label": o, "html": _inline(o)} for o in it["options"]],
        })
    return groups, items


def build(root: pathlib.Path, out: pathlib.Path, probes: pathlib.Path | None = None) -> None:
    groups, items = _items(root)
    charts = _probes(probes)
    for it in items:
        it["probe"] = charts.get(it["id"], "")
    payload = json.dumps({"groups": groups, "items": items, "built": date.today().isoformat()})
    page = TEMPLATE.replace("/*DATA*/", payload.replace("</", "<\\/"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)


TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CNA decision board</title>
<style>
:root {
  --paper: #e8ebe4; --panel: #f6f7f3; --ink: #1d2629; --muted: #58645f;
  --rule: #b9c1b8; --axis: #6f7b68; --sand: #d8b46a; --sand-deep: #9c7a2f;
  --defer: #8a9aa8;
  --head: "Bahnschrift", "DIN Alternate", "Barlow Condensed", "Roboto Condensed", "Arial Narrow", sans-serif;
  --body: "Charter", "Iowan Old Style", "Noto Serif", Georgia, serif;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--paper); color: var(--ink); font: 17px/1.6 var(--body); }
a { color: var(--ink); }
:focus-visible { outline: 3px solid var(--sand-deep); outline-offset: 2px; }
.shell { display: grid; grid-template-columns: 17rem 1fr; min-height: 100vh; }
nav { position: sticky; top: 0; height: 100vh; overflow-y: auto; padding: 1.5rem 1rem 2rem;
  background: var(--ink); color: #dfe4dc; font-family: var(--head); }
nav h1 { font-size: 1.6rem; line-height: 1.05; margin: 0 0 .25rem; font-weight: 700; letter-spacing: .01em; }
nav .tally { font-size: 1rem; color: #aab4a8; margin: 0 0 1.25rem; }
nav .tally b { color: var(--sand); font-size: 1.35rem; }
nav h2 { font-size: .95rem; font-weight: 600; color: #aab4a8; margin: 1.1rem 0 .35rem; }
nav ol { list-style: none; margin: 0; padding: 0; }
nav li a { display: grid; grid-template-columns: .8rem 1fr; gap: .5rem; align-items: baseline;
  padding: .15rem .25rem; color: #dfe4dc; text-decoration: none; font-size: .95rem; line-height: 1.25; }
nav li a:hover { background: #2c383b; }
nav li a::before { content: ""; width: .7rem; height: .7rem; border: 1.5px solid #7d8a80; transform: translateY(.05rem); }
nav li.done a::before { background: var(--sand); border-color: var(--sand); }
nav li.later a::before { background: var(--defer); border-color: var(--defer); }
.actions { display: grid; gap: .5rem; margin-bottom: 1rem; }
button { font: 600 1rem var(--head); cursor: pointer; border: 2px solid var(--ink); background: var(--panel);
  color: var(--ink); padding: .45rem .8rem; }
nav button { border-color: var(--sand); background: var(--sand); }
nav button.quiet { background: transparent; color: #dfe4dc; border-color: #58645f; }
main { padding: 2.5rem clamp(1rem, 4vw, 3.5rem) 6rem; max-width: 52rem; }
.intro { font-size: 1rem; color: var(--muted); max-width: 40rem; margin: 0 0 2rem; }
.group-title { font: 700 2.4rem/1 var(--head); margin: 3rem 0 1rem; color: var(--axis); }
article { background: var(--panel); border-left: 6px solid var(--rule); padding: 1.25rem 1.5rem 1.4rem;
  margin: 0 0 1.25rem; scroll-margin-top: 1rem; }
article.done { border-left-color: var(--sand); }
article.later { border-left-color: var(--defer); }
article header { display: flex; gap: .75rem; align-items: baseline; flex-wrap: wrap; }
article .id { font: 700 1rem var(--head); color: var(--muted); }
article h3 { font: 600 1.45rem/1.2 var(--head); margin: 0; flex: 1 1 20rem; }
article .meta { font-size: .9rem; color: var(--muted); margin: .2rem 0 .6rem; }
.context { font-size: 1rem; }
.context p { margin: .5rem 0; }
blockquote { margin: .6rem 0; padding: .1rem 0 .1rem 1rem; border-left: 3px solid var(--rule); color: var(--muted); }
code { font-size: .88em; background: #e3e7df; padding: 0 .2em; }
details { font-size: .95rem; margin: .5rem 0; }
summary { cursor: pointer; font-family: var(--head); font-weight: 600; color: var(--muted); }
fieldset { border: 0; padding: 0; margin: 1rem 0 0; display: grid; gap: .5rem; }
legend { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }
.chit { display: grid; grid-template-columns: 2.1rem 1fr; gap: .8rem; align-items: start; cursor: pointer;
  padding: .55rem .7rem; border: 1.5px solid var(--rule); background: #fff; font-size: .97rem; line-height: 1.45; }
.chit input { position: absolute; opacity: 0; }
.chit .mark { width: 2.1rem; height: 2.1rem; border: 2px solid var(--axis); display: grid; place-items: center;
  font: 700 1.05rem var(--head); color: var(--axis); }
.chit:hover { border-color: var(--axis); }
.chit:has(input:focus-visible) { outline: 3px solid var(--sand-deep); outline-offset: 2px; }
.chit:has(input:checked) { border-color: var(--sand-deep); background: #fbf3df; }
.chit:has(input:checked) .mark { background: var(--sand); border-color: var(--sand-deep); color: var(--ink);
  box-shadow: 2px 2px 0 var(--sand-deep); }
.row { display: flex; gap: .75rem; align-items: flex-start; margin-top: .75rem; flex-wrap: wrap; }
textarea { flex: 1 1 20rem; min-height: 2.6rem; font: .95rem/1.4 var(--body); padding: .45rem .6rem;
  border: 1.5px solid var(--rule); background: #fff; color: var(--ink); resize: vertical; }
.row button { font-size: .9rem; padding: .35rem .7rem; border-width: 1.5px; }
.row button[aria-pressed="true"] { background: var(--defer); color: #fff; border-color: var(--defer); }
.probe { margin: 1.1rem 0 0; padding: .9rem 1rem; background: #fff; border: 1.5px solid var(--rule); }
.probe figcaption { font-size: .95rem; }
.probe .unit { color: var(--muted); }
.probe-svg { width: 100%; height: auto; display: block; margin: .5rem 0; }
.probe-svg .grid { stroke: #dde2da; stroke-width: 1; }
.probe-svg .tick, .probe-svg .axis { font: 12px var(--head); fill: var(--muted); }
.legend { list-style: none; display: flex; flex-wrap: wrap; gap: .3rem 1.1rem; padding: 0; margin: 0; font: .9rem var(--head); }
.legend .swatch { display: inline-block; width: .8rem; height: .8rem; border-radius: 2px; margin-right: .35rem; vertical-align: -.05rem; }
.finding { font-size: .98rem; margin: .6rem 0 .2rem; }
.prov { font: .8rem var(--head); color: var(--muted); margin: .2rem 0 0; }
.probe table { border-collapse: collapse; font: .85rem var(--head); margin-top: .4rem; }
.probe th, .probe td { border-bottom: 1px solid #e3e7df; padding: .15rem .6rem; text-align: right; }
dialog { max-width: 46rem; width: 92vw; border: 3px solid var(--ink); padding: 1.25rem; background: var(--panel); }
dialog pre { white-space: pre-wrap; font-size: .85rem; max-height: 60vh; overflow: auto; background: #fff; padding: .75rem; }
.toast { position: fixed; bottom: 1.25rem; right: 1.25rem; background: var(--ink); color: var(--sand);
  font: 600 1rem var(--head); padding: .6rem 1rem; opacity: 0; transition: opacity .2s; pointer-events: none; }
.toast.show { opacity: 1; }
@media (max-width: 760px) {
  .shell { grid-template-columns: 1fr; }
  nav { position: static; height: auto; }
  nav ol { display: none; }
}
@media (prefers-reduced-motion: reduce) { * { transition: none !important; scroll-behavior: auto !important; } }
</style>
</head>
<body>
<div class="shell">
<nav aria-label="Questions">
  <h1>Decision board</h1>
  <p class="tally"><b id="n-done">0</b> of <span id="n-all">0</span> decided</p>
  <div class="actions">
    <button id="copy">Copy as Feedback</button>
    <button id="show" class="quiet">Preview Feedback</button>
    <button id="reset" class="quiet">Clear all choices</button>
  </div>
  <div id="toc"></div>
</nav>
<main>
  <p class="intro">The autopilot decides everything here that is cheap to reverse. Only the first group
  needs you, and only if you want to check your printed copy; until then those stay as read. You can still
  override anything else: pick an option, add a note, then copy the Feedback block into
  <code>docs/autopilot/PROGRESS.md</code>. Choices are saved in this browser.</p>
  <div id="board"></div>
</main>
</div>
<dialog id="dlg"><pre id="out"></pre><button id="close">Close</button></dialog>
<div class="toast" id="toast" role="status"></div>
<script>
const DATA = /*DATA*/;
const KEY = "cna-decisions-v1";
const state = JSON.parse(localStorage.getItem(KEY) || "{}");
const save = () => localStorage.setItem(KEY, JSON.stringify(state));
const $ = (s, el = document) => el.querySelector(s);
const esc = s => s.replace(/[&<>"]/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]));

function render() {
  const board = $("#board"), toc = $("#toc");
  for (const [g, name] of Object.entries(DATA.groups)) {
    const its = DATA.items.filter(i => i.group === g);
    if (!its.length) continue;
    board.insertAdjacentHTML("beforeend", `<h2 class="group-title" id="g-${g}">${esc(name)}</h2>`);
    toc.insertAdjacentHTML("beforeend", `<h2>${esc(name)} (${its.length})</h2><ol>` +
      its.map(i => `<li data-id="${i.id}"><a href="#${i.id}">${esc(i.title)}</a></li>`).join("") + "</ol>");
    for (const it of its) {
      const s = state[it.id] || {};
      const opts = it.options.map((o, n) => `
        <label class="chit"><input type="radio" name="${it.id}" value="${n}" ${s.choice === n ? "checked" : ""}>
        <span class="mark" aria-hidden="true">${n + 1}</span><span>${o.html}</span></label>`).join("");
      board.insertAdjacentHTML("beforeend", `
      <article id="${it.id}">
        <header><span class="id">${it.group === "rulings" ? it.id : ""}</span><h3>${esc(it.title)}</h3></header>
        ${it.meta || it.link ? `<p class="meta">${esc(it.meta)}${it.link ? ` · <a href="${it.link}">full ruling</a>` : ""}</p>` : ""}
        <div class="context">${it.context}</div>
        ${it.rationale ? `<details><summary>Our rationale so far</summary>${it.rationale}</details>` : ""}
        <fieldset><legend>${esc(it.title)}</legend>${opts}</fieldset>
        ${it.probe}
        <div class="row">
          <textarea aria-label="Note for ${esc(it.title)}" placeholder="Note (optional)">${esc(s.note || "")}</textarea>
          <button type="button" class="later" aria-pressed="${!!s.later}">Later</button>
        </div>
      </article>`);
      const art = $(`#${CSS.escape(it.id)}`);
      art.addEventListener("change", e => {
        if (e.target.type !== "radio") return;
        state[it.id] = {...state[it.id], choice: +e.target.value, later: false};
        $(".later", art).setAttribute("aria-pressed", "false");
        save(); refresh();
      });
      $("textarea", art).addEventListener("input", e => { state[it.id] = {...state[it.id], note: e.target.value}; save(); refresh(); });
      $(".later", art).addEventListener("click", e => {
        const on = !(state[it.id] || {}).later;
        state[it.id] = {...state[it.id], later: on};
        if (on) { delete state[it.id].choice; art.querySelectorAll("input").forEach(r => r.checked = false); }
        e.target.setAttribute("aria-pressed", on); save(); refresh();
      });
    }
  }
  $("#n-all").textContent = DATA.items.length;
  refresh();
}

function status(id) {
  const s = state[id] || {};
  return s.choice !== undefined ? "done" : s.later ? "later" : "";
}

function refresh() {
  let done = 0;
  for (const it of DATA.items) {
    const st = status(it.id);
    if (st === "done") done++;
    $(`#${CSS.escape(it.id)}`).className = st;
    $(`li[data-id="${it.id}"]`).className = st;
  }
  $("#n-done").textContent = done;
}

function feedback() {
  const today = new Date().toISOString().slice(0, 10);
  const lines = [`- ${today} (Brian) answers from the decision board (built ${DATA.built}):`];
  for (const it of DATA.items) {
    const s = state[it.id] || {};
    const note = (s.note || "").trim().replace(/\s+/g, " ");
    if (s.choice !== undefined) {
      const o = it.options[s.choice];
      const verb = it.group === "rulings"
        ? (o.label.startsWith("Reject") ? "reject every option" : `accept option ${s.choice + 1}, ${o.label.replace(/\.$/, "")}`)
        : o.label;
      lines.push(`  - **${it.id}** (${it.title}): ${verb}.${note ? " Note: " + note : ""}`);
    } else if (note) {
      lines.push(`  - **${it.id}** (${it.title}): no choice yet. Note: ${note}`);
    }
  }
  if (lines.length === 1) return "";
  lines.push("  - For rulings: an accepted option means edit the ruling's Decision and Rationale, set `status: accepted`, update the rules prose with the `::: ruling` badge, and regenerate the register (rulings/README.md, Process step 3). One PR per ruling.");
  return lines.join("\n");
}

function toast(msg) { const t = $("#toast"); t.textContent = msg; t.classList.add("show"); setTimeout(() => t.classList.remove("show"), 1800); }
$("#copy").onclick = async () => {
  const text = feedback();
  if (!text) return toast("Nothing decided yet");
  try { await navigator.clipboard.writeText(text); toast("Copied Feedback"); }
  catch { $("#out").textContent = text; $("#dlg").showModal(); }
};
$("#show").onclick = () => { $("#out").textContent = feedback() || "Nothing decided yet."; $("#dlg").showModal(); };
$("#close").onclick = () => $("#dlg").close();
$("#reset").onclick = () => { if (confirm("Clear every choice and note?")) { localStorage.removeItem(KEY); location.reload(); } };
render();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("out", nargs="?", default=ROOT / "build/decisions.html", type=pathlib.Path)
    ap.add_argument("--probes", type=pathlib.Path, help="cna-engine probes/ directory")
    a = ap.parse_args()
    out = a.out
    build(ROOT, out, a.probes)
    print(out)
