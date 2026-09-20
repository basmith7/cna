---
title: Learn
layout: page
sidebar: false
---
<div class="learn">
<style>
.learn h1{margin:0 0 4px;font-size:26px}
.learn .sub{color:var(--learn-muted,#666);margin:0 0 20px}
.learn .part{margin:34px 0 4px;font-size:24px;color:var(--learn-accent,#5a3d1a);border-top:3px solid var(--learn-rule,#c9b98f);padding-top:18px}
.learn .panel{background:var(--learn-panel,#fff);border:1px solid var(--learn-line,#d8cfb5);border-radius:8px;padding:16px 20px;margin:0 0 22px}
.learn .panel h2{margin:0 0 12px;font-size:18px;color:var(--learn-accent,#5a3d1a)}
.learn .row{display:flex;gap:20px;align-items:flex-start;flex-wrap:wrap}
.learn .map{flex:1 1 560px;min-width:0}
.learn .note{flex:1 1 300px;font-size:14px;line-height:1.45}
.learn .panel svg{display:block;max-width:100%;height:auto}
.learn .note p{margin:0 0 10px}
.learn .note ol{margin:0 0 10px 18px;padding:0}
.learn .note li{margin:0 0 6px}
.learn .cols{display:flex;gap:14px;align-items:stretch;flex-wrap:wrap}
.learn .cols .calc{flex:1 1 280px;margin-top:0}
.learn .esc{border-bottom:4px solid #7a3b1e}
.learn .rough{background:repeating-linear-gradient(135deg,#e2cf9e 0 3px,#a88d55 3px 4px);padding:0 3px}
.learn .calc{margin-top:14px;background:var(--learn-calc,#f7f1de);border:1px solid var(--learn-line,#d8cfb5);border-radius:6px;padding:10px 14px;font-size:13px}
.learn .calc h3{margin:0 0 8px;font-size:15px}
.learn table{border-collapse:collapse;width:100%}
.learn th, .learn td{text-align:left;vertical-align:top;padding:4px 8px;border-bottom:1px solid var(--learn-line,#e3dac1)}
.learn th{white-space:nowrap;color:var(--learn-accent,#5a3d1a);font-weight:600}
.learn .ledger th{border-bottom:2px solid var(--learn-rule,#c9b98f)}
.learn .bad{color:var(--learn-bad,#b00);font-weight:bold}
.learn .warn{color:var(--learn-warn,#b8600b);font-weight:bold}
.learn .fine{color:var(--learn-muted,#666);font-size:12px;margin:8px 0 0}
.learn .legend{display:flex;gap:18px;font-size:13px;color:var(--learn-muted,#444);margin:0 0 18px;flex-wrap:wrap}
.learn .sw{display:inline-block;width:22px;height:14px;vertical-align:middle;border:1px solid var(--learn-swatch,#222);margin-right:5px;border-radius:2px}
.learn{max-width:1240px;margin:0 auto;padding:24px 32px 96px;line-height:1.5} .learn .panel{overflow-x:auto}
.dark .learn{--learn-accent:#d9b46a;--learn-rule:#5a4a2e;--learn-line:var(--vp-c-divider);--learn-panel:var(--vp-c-bg-soft);--learn-calc:var(--vp-c-bg-alt);--learn-muted:var(--vp-c-text-2);--learn-swatch:var(--vp-c-text-3);--learn-bad:#f0776a;--learn-warn:#e0a24a}
.learn a{color:var(--vp-c-brand-1);text-decoration:underline;text-underline-offset:2px}
.learn code{font-family:var(--vp-font-family-mono);font-size:0.9em;background:var(--vp-c-default-soft);padding:2px 5px;border-radius:4px}
.learn .learn-table{margin:0 0 18px;overflow-x:auto} .learn .learn-table h4{margin:0 0 4px;font-size:15px} .learn .learn-table-ref{margin:0 0 8px}
.learn .learn-table .spi-badge{margin:0} .learn table.crt{margin:0 0 12px;font-size:13px} .learn table.crt td{white-space:nowrap} .learn table.crt caption{text-align:left;font-weight:600;padding:4px 0}
@media (max-width:640px){.learn{padding:16px 16px 64px} .learn .panel{padding:12px 14px}}
</style>
<h1>The Campaign for North Africa — illustrated</h1>
<p class="sub">Terrain costs [<a href="rules/40-movement#spi-8.37">8.37</a>], CP costs [<a href="rules/30-capability-points#spi-6.3">6.3</a>], CRT [<a href="rules/60-combat#spi-15.79">15.79</a>] and the tables are the real 1979 values from <code>data/tables/</code>; unit ratings in Part A are illustrative. Case numbers in brackets link into the rules.</p>
<h1 id="part-a" class="part" style="margin-top:8px;border:0;padding:0;font-size:22px">Part A · One Operations Stage</h1>
<p class="sub">Player A's half of Operations Stage 1, Game-Turn 1 (Sept 1940), on a small sketch map.</p>
<div class="legend">
<span><span class="sw" style="background:#8fa77a"></span>Italian</span>
<span><span class="sw" style="background:#d9b46a"></span>Commonwealth</span>
<span><span class="sw" style="background:#f3e6bf"></span>Clear (2 CP)</span>
<span><span class="sw rough"></span>Rough (3/4 CP, L2 assault)</span>
<span><span class="sw" style="background:#333"></span>Road (1 / ½ CP)</span>
<span><span class="sw" style="border:2px dashed #7a5a2a;background:none"></span>Track (halves the hex)</span>
<span><span class="sw" style="background:#7a3b1e"></span>Escarpment hexside (+6 up, no vehicles)</span>
<span><span class="sw" style="background:#9ec9e2"></span>Sea</span>
</div>
<section class="panel"><h2>1 · Start of Player A's half</h2><div class="row"><div class="map"><svg viewBox="0 0 721 564" width="721" height="564" xmlns="http://www.w3.org/2000/svg">
<defs>
 <pattern id="rough" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#e2cf9e"/><path d="M0 8 L8 0" stroke="#a88d55" stroke-width="1.2"/></pattern>
 <marker id="arr-b00" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#b00"/></marker>
 <marker id="arr-1d4ed8" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#1d4ed8"/></marker>
</defs>
<polygon points="114.0,40.0 87.0,86.8 33.0,86.8 6.0,40.0 33.0,-6.8 87.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="114.0,133.5 87.0,180.3 33.0,180.3 6.0,133.5 33.0,86.8 87.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">0-01</text>
<polygon points="114.0,227.1 87.0,273.8 33.0,273.8 6.0,227.1 33.0,180.3 87.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">0-02</text>
<polygon points="114.0,320.6 87.0,367.4 33.0,367.4 6.0,320.6 33.0,273.8 87.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">0-03</text>
<polygon points="114.0,414.1 87.0,460.9 33.0,460.9 6.0,414.1 33.0,367.4 87.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">0-04</text>
<polygon points="195.0,86.8 168.0,133.5 114.0,133.5 87.0,86.8 114.0,40.0 168.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="195.0,180.3 168.0,227.1 114.0,227.1 87.0,180.3 114.0,133.5 168.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">1-01</text>
<polygon points="195.0,273.8 168.0,320.6 114.0,320.6 87.0,273.8 114.0,227.1 168.0,227.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">1-02</text>
<polygon points="195.0,367.4 168.0,414.1 114.0,414.1 87.0,367.4 114.0,320.6 168.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">1-03</text>
<polygon points="195.0,460.9 168.0,507.7 114.0,507.7 87.0,460.9 114.0,414.1 168.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">1-04</text>
<polygon points="276.0,40.0 249.0,86.8 195.0,86.8 168.0,40.0 195.0,-6.8 249.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="276.0,133.5 249.0,180.3 195.0,180.3 168.0,133.5 195.0,86.8 249.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">2-01</text>
<polygon points="276.0,227.1 249.0,273.8 195.0,273.8 168.0,227.1 195.0,180.3 249.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">2-02</text>
<polygon points="276.0,320.6 249.0,367.4 195.0,367.4 168.0,320.6 195.0,273.8 249.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">2-03</text>
<polygon points="276.0,414.1 249.0,460.9 195.0,460.9 168.0,414.1 195.0,367.4 249.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">2-04</text>
<polygon points="357.0,86.8 330.0,133.5 276.0,133.5 249.0,86.8 276.0,40.0 330.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="357.0,180.3 330.0,227.1 276.0,227.1 249.0,180.3 276.0,133.5 330.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">3-01</text>
<polygon points="357.0,273.8 330.0,320.6 276.0,320.6 249.0,273.8 276.0,227.1 330.0,227.1" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">3-02</text>
<polygon points="357.0,367.4 330.0,414.1 276.0,414.1 249.0,367.4 276.0,320.6 330.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">3-03</text>
<polygon points="357.0,460.9 330.0,507.7 276.0,507.7 249.0,460.9 276.0,414.1 330.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">3-04</text>
<polygon points="438.0,40.0 411.0,86.8 357.0,86.8 330.0,40.0 357.0,-6.8 411.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="438.0,133.5 411.0,180.3 357.0,180.3 330.0,133.5 357.0,86.8 411.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">4-01</text>
<polygon points="438.0,227.1 411.0,273.8 357.0,273.8 330.0,227.1 357.0,180.3 411.0,180.3" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">4-02</text>
<polygon points="438.0,320.6 411.0,367.4 357.0,367.4 330.0,320.6 357.0,273.8 411.0,273.8" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">4-03</text>
<polygon points="438.0,414.1 411.0,460.9 357.0,460.9 330.0,414.1 357.0,367.4 411.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">4-04</text>
<polygon points="519.0,86.8 492.0,133.5 438.0,133.5 411.0,86.8 438.0,40.0 492.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="519.0,180.3 492.0,227.1 438.0,227.1 411.0,180.3 438.0,133.5 492.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">5-01</text>
<polygon points="519.0,273.8 492.0,320.6 438.0,320.6 411.0,273.8 438.0,227.1 492.0,227.1" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">5-02</text>
<polygon points="519.0,367.4 492.0,414.1 438.0,414.1 411.0,367.4 438.0,320.6 492.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">5-03</text>
<polygon points="519.0,460.9 492.0,507.7 438.0,507.7 411.0,460.9 438.0,414.1 492.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">5-04</text>
<polygon points="600.0,40.0 573.0,86.8 519.0,86.8 492.0,40.0 519.0,-6.8 573.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="600.0,133.5 573.0,180.3 519.0,180.3 492.0,133.5 519.0,86.8 573.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">6-01</text>
<polygon points="600.0,227.1 573.0,273.8 519.0,273.8 492.0,227.1 519.0,180.3 573.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">6-02</text>
<polygon points="600.0,320.6 573.0,367.4 519.0,367.4 492.0,320.6 519.0,273.8 573.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">6-03</text>
<polygon points="600.0,414.1 573.0,460.9 519.0,460.9 492.0,414.1 519.0,367.4 573.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">6-04</text>
<polygon points="681.0,86.8 654.0,133.5 600.0,133.5 573.0,86.8 600.0,40.0 654.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="681.0,180.3 654.0,227.1 600.0,227.1 573.0,180.3 600.0,133.5 654.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">7-01</text>
<polygon points="681.0,273.8 654.0,320.6 600.0,320.6 573.0,273.8 600.0,227.1 654.0,227.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">7-02</text>
<polygon points="681.0,367.4 654.0,414.1 600.0,414.1 573.0,367.4 600.0,320.6 654.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">7-03</text>
<polygon points="681.0,460.9 654.0,507.7 600.0,507.7 573.0,460.9 600.0,414.1 654.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">7-04</text>
<polyline points="60.0,133.5 141.0,180.3 222.0,133.5 303.0,180.3 384.0,133.5 465.0,180.3 546.0,133.5 627.0,180.3" fill="none" stroke="#333" stroke-width="4"/>
<polyline points="60.0,133.5 141.0,180.3 222.0,133.5 303.0,180.3 384.0,133.5 465.0,180.3 546.0,133.5 627.0,180.3" fill="none" stroke="#f3e6bf" stroke-width="1.5" stroke-dasharray="6 6"/>
<polyline points="384.0,133.5 384.0,227.1 384.0,320.6 465.0,367.4 546.0,320.6" fill="none" stroke="#7a5a2a" stroke-width="2.5" stroke-dasharray="7 5"/>
<line x1="33.0" y1="180.3" x2="87.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="114.0" y1="227.1" x2="168.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="195.0" y1="180.3" x2="168.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="87.0" y1="180.3" x2="114.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="249.0" y1="180.3" x2="195.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="330.0" y1="227.1" x2="276.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="357.0" y1="180.3" x2="330.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="249.0" y1="180.3" x2="276.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="492.0" y1="227.1" x2="438.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="519.0" y1="180.3" x2="492.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="411.0" y1="180.3" x2="438.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="573.0" y1="180.3" x2="519.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="654.0" y1="227.1" x2="600.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="573.0" y1="180.3" x2="600.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<circle cx="546.0" cy="306.6" r="5" fill="#2b6cb0"/><text x="546.0" y="298.6" font-size="10" text-anchor="middle" fill="#2b6cb0">Bir Sofafi</text>
<text x="90.0" y="44.0" font-size="13" fill="#2b5c7a" font-style="italic">Mediterranean</text>
<text x="388.0" y="191.5" font-size="10" fill="#7a3b1e" font-weight="bold" text-anchor="middle">Halfaya Pass</text>
<text x="141.0" y="464.9" font-size="11" fill="#8a7a55" font-style="italic" text-anchor="middle">Libyan plateau</text>
<g><rect x="30.0" y="124.5" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="60.0" y="135.5" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">I/1 Libyan</text>
<text x="60.0" y="145.5" font-size="8" text-anchor="middle" fill="#222">Inf regt · CPA 8 · M−1</text></g>
<g><rect x="111.0" y="171.3" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="141.0" y="182.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">1 Lib Art</text>
<text x="141.0" y="192.3" font-size="8" text-anchor="middle" fill="#222">Arty · Bar 9 · CPA 8</text></g>
<g><rect x="117.0" y="141.3" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="147.0" y="152.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">II/1 Libyan</text>
<text x="147.0" y="162.3" font-size="8" text-anchor="middle" fill="#222">Inf regt · CPA 8 · M−1</text></g>
<g><rect x="30.0" y="218.1" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="60.0" y="229.1" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">IX L3</text>
<text x="60.0" y="239.1" font-size="8" text-anchor="middle" fill="#222">Tankette bn · CPA 25</text></g>
<g><rect x="273.0" y="171.3" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="303.0" y="182.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">11 Hussars</text>
<text x="303.0" y="192.3" font-size="8" text-anchor="middle" fill="#222">Armd cars · CPA 25 · M+2</text></g>
<g><rect x="354.0" y="218.1" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="384.0" y="229.1" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">1 RNF</text>
<text x="384.0" y="239.1" font-size="8" text-anchor="middle" fill="#222">MG bn · CPA 8 · M+1</text></g>
<g><rect x="435.0" y="264.8" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="465.0" y="275.8" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">4 RHA</text>
<text x="465.0" y="285.8" font-size="8" text-anchor="middle" fill="#222">Arty · Bar 9 · CPA 10</text></g>
</svg></div><div class="note">
<p><b>Sept 1940, Operations Stage 1, Player A = Italy.</b> Italy won Initiative (rating 1 + die) and chose to go first.</p>
<p>Coast road along the strip; the <span class="esc">escarpment</span> blocks vehicles going up except at the <b>Halfaya Pass track</b>. <span class="rough">Hatched</span> = Rough.</p>
<p>Each unit has a <b>CPA</b> to spend this stage: cross Clear = 2 CP, Rough = 3 (non-mot) / 4 (mot), road hex = 1 (non-mot) / ½ (mot), track = 1, up an escarpment = +6 non-mot, <b>prohibited</b> for motorised [<a href="rules/40-movement#spi-8.37">8.37</a>].</p>
<p>Both sides' CPs count for the <i>whole</i> stage, including what B spends reacting during A's half [<a href="rules/30-capability-points#spi-6.14">6.14</a>].</p></div></div></section><section class="panel"><h2>2 · Reserve Designation + Movement Segment (cycle 1)</h2><div class="row"><div class="map"><svg viewBox="0 0 721 564" width="721" height="564" xmlns="http://www.w3.org/2000/svg">
<defs>
 <pattern id="rough" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#e2cf9e"/><path d="M0 8 L8 0" stroke="#a88d55" stroke-width="1.2"/></pattern>
 <marker id="arr-b00" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#b00"/></marker>
 <marker id="arr-1d4ed8" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#1d4ed8"/></marker>
</defs>
<polygon points="114.0,40.0 87.0,86.8 33.0,86.8 6.0,40.0 33.0,-6.8 87.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="114.0,133.5 87.0,180.3 33.0,180.3 6.0,133.5 33.0,86.8 87.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">0-01</text>
<polygon points="114.0,227.1 87.0,273.8 33.0,273.8 6.0,227.1 33.0,180.3 87.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">0-02</text>
<polygon points="114.0,320.6 87.0,367.4 33.0,367.4 6.0,320.6 33.0,273.8 87.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">0-03</text>
<polygon points="114.0,414.1 87.0,460.9 33.0,460.9 6.0,414.1 33.0,367.4 87.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">0-04</text>
<polygon points="195.0,86.8 168.0,133.5 114.0,133.5 87.0,86.8 114.0,40.0 168.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="195.0,180.3 168.0,227.1 114.0,227.1 87.0,180.3 114.0,133.5 168.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">1-01</text>
<polygon points="195.0,273.8 168.0,320.6 114.0,320.6 87.0,273.8 114.0,227.1 168.0,227.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">1-02</text>
<polygon points="195.0,367.4 168.0,414.1 114.0,414.1 87.0,367.4 114.0,320.6 168.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">1-03</text>
<polygon points="195.0,460.9 168.0,507.7 114.0,507.7 87.0,460.9 114.0,414.1 168.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">1-04</text>
<polygon points="276.0,40.0 249.0,86.8 195.0,86.8 168.0,40.0 195.0,-6.8 249.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="276.0,133.5 249.0,180.3 195.0,180.3 168.0,133.5 195.0,86.8 249.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">2-01</text>
<polygon points="276.0,227.1 249.0,273.8 195.0,273.8 168.0,227.1 195.0,180.3 249.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">2-02</text>
<polygon points="276.0,320.6 249.0,367.4 195.0,367.4 168.0,320.6 195.0,273.8 249.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">2-03</text>
<polygon points="276.0,414.1 249.0,460.9 195.0,460.9 168.0,414.1 195.0,367.4 249.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">2-04</text>
<polygon points="357.0,86.8 330.0,133.5 276.0,133.5 249.0,86.8 276.0,40.0 330.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="357.0,180.3 330.0,227.1 276.0,227.1 249.0,180.3 276.0,133.5 330.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">3-01</text>
<polygon points="357.0,273.8 330.0,320.6 276.0,320.6 249.0,273.8 276.0,227.1 330.0,227.1" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">3-02</text>
<polygon points="357.0,367.4 330.0,414.1 276.0,414.1 249.0,367.4 276.0,320.6 330.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">3-03</text>
<polygon points="357.0,460.9 330.0,507.7 276.0,507.7 249.0,460.9 276.0,414.1 330.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">3-04</text>
<polygon points="438.0,40.0 411.0,86.8 357.0,86.8 330.0,40.0 357.0,-6.8 411.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="438.0,133.5 411.0,180.3 357.0,180.3 330.0,133.5 357.0,86.8 411.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">4-01</text>
<polygon points="438.0,227.1 411.0,273.8 357.0,273.8 330.0,227.1 357.0,180.3 411.0,180.3" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">4-02</text>
<polygon points="438.0,320.6 411.0,367.4 357.0,367.4 330.0,320.6 357.0,273.8 411.0,273.8" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">4-03</text>
<polygon points="438.0,414.1 411.0,460.9 357.0,460.9 330.0,414.1 357.0,367.4 411.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">4-04</text>
<polygon points="519.0,86.8 492.0,133.5 438.0,133.5 411.0,86.8 438.0,40.0 492.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="519.0,180.3 492.0,227.1 438.0,227.1 411.0,180.3 438.0,133.5 492.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">5-01</text>
<polygon points="519.0,273.8 492.0,320.6 438.0,320.6 411.0,273.8 438.0,227.1 492.0,227.1" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">5-02</text>
<polygon points="519.0,367.4 492.0,414.1 438.0,414.1 411.0,367.4 438.0,320.6 492.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">5-03</text>
<polygon points="519.0,460.9 492.0,507.7 438.0,507.7 411.0,460.9 438.0,414.1 492.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">5-04</text>
<polygon points="600.0,40.0 573.0,86.8 519.0,86.8 492.0,40.0 519.0,-6.8 573.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="600.0,133.5 573.0,180.3 519.0,180.3 492.0,133.5 519.0,86.8 573.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">6-01</text>
<polygon points="600.0,227.1 573.0,273.8 519.0,273.8 492.0,227.1 519.0,180.3 573.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">6-02</text>
<polygon points="600.0,320.6 573.0,367.4 519.0,367.4 492.0,320.6 519.0,273.8 573.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">6-03</text>
<polygon points="600.0,414.1 573.0,460.9 519.0,460.9 492.0,414.1 519.0,367.4 573.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">6-04</text>
<polygon points="681.0,86.8 654.0,133.5 600.0,133.5 573.0,86.8 600.0,40.0 654.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="681.0,180.3 654.0,227.1 600.0,227.1 573.0,180.3 600.0,133.5 654.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">7-01</text>
<polygon points="681.0,273.8 654.0,320.6 600.0,320.6 573.0,273.8 600.0,227.1 654.0,227.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">7-02</text>
<polygon points="681.0,367.4 654.0,414.1 600.0,414.1 573.0,367.4 600.0,320.6 654.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">7-03</text>
<polygon points="681.0,460.9 654.0,507.7 600.0,507.7 573.0,460.9 600.0,414.1 654.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">7-04</text>
<polyline points="60.0,133.5 141.0,180.3 222.0,133.5 303.0,180.3 384.0,133.5 465.0,180.3 546.0,133.5 627.0,180.3" fill="none" stroke="#333" stroke-width="4"/>
<polyline points="60.0,133.5 141.0,180.3 222.0,133.5 303.0,180.3 384.0,133.5 465.0,180.3 546.0,133.5 627.0,180.3" fill="none" stroke="#f3e6bf" stroke-width="1.5" stroke-dasharray="6 6"/>
<polyline points="384.0,133.5 384.0,227.1 384.0,320.6 465.0,367.4 546.0,320.6" fill="none" stroke="#7a5a2a" stroke-width="2.5" stroke-dasharray="7 5"/>
<line x1="33.0" y1="180.3" x2="87.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="114.0" y1="227.1" x2="168.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="195.0" y1="180.3" x2="168.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="87.0" y1="180.3" x2="114.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="249.0" y1="180.3" x2="195.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="330.0" y1="227.1" x2="276.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="357.0" y1="180.3" x2="330.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="249.0" y1="180.3" x2="276.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="492.0" y1="227.1" x2="438.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="519.0" y1="180.3" x2="492.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="411.0" y1="180.3" x2="438.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="573.0" y1="180.3" x2="519.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="654.0" y1="227.1" x2="600.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="573.0" y1="180.3" x2="600.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<circle cx="546.0" cy="306.6" r="5" fill="#2b6cb0"/><text x="546.0" y="298.6" font-size="10" text-anchor="middle" fill="#2b6cb0">Bir Sofafi</text>
<text x="90.0" y="44.0" font-size="13" fill="#2b5c7a" font-style="italic">Mediterranean</text>
<text x="388.0" y="191.5" font-size="10" fill="#7a3b1e" font-weight="bold" text-anchor="middle">Halfaya Pass</text>
<text x="141.0" y="464.9" font-size="11" fill="#8a7a55" font-style="italic" text-anchor="middle">Libyan plateau</text>
<g opacity="0.45"><rect x="30.0" y="124.5" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="60.0" y="135.5" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">I/1 Libyan</text>
<text x="60.0" y="145.5" font-size="8" text-anchor="middle" fill="#222">Inf regt · CPA 8 · M−1</text></g>
<g opacity="0.45"><rect x="111.0" y="171.3" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="141.0" y="182.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">1 Lib Art</text>
<text x="141.0" y="192.3" font-size="8" text-anchor="middle" fill="#222">Arty · Bar 9 · CPA 8</text></g>
<g opacity="0.45"><rect x="117.0" y="141.3" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="147.0" y="152.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">II/1 Libyan</text>
<text x="147.0" y="162.3" font-size="8" text-anchor="middle" fill="#222">Inf regt · CPA 8 · M−1</text></g>
<g><rect x="30.0" y="218.1" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="60.0" y="229.1" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">IX L3</text>
<text x="60.0" y="239.1" font-size="8" text-anchor="middle" fill="#222">Tankette bn · CPA 25</text></g>
<rect x="78.0" y="209.1" width="30" height="14" rx="2" fill="#fff" stroke="#b00" stroke-width="1.2"/>
<text x="93.0" y="219.1" font-size="8" text-anchor="middle" fill="#b00" font-weight="bold">RES I</text>
<path d="M 60.0,133.5 L 141.0,180.3 L 222.0,133.5 L 303.0,180.3" fill="none" stroke="#b00" stroke-width="3" marker-end="url(#arr-b00)"/>
<g><rect x="273.0" y="171.3" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="303.0" y="182.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">I/1 Libyan</text>
<text x="303.0" y="192.3" font-size="8" text-anchor="middle" fill="#222">Inf regt · CPA 8 · M−1</text></g>
<path d="M 141.0,180.3 L 222.0,133.5 L 303.0,180.3" fill="none" stroke="#b00" stroke-width="3" marker-end="url(#arr-b00)"/>
<g><rect x="279.0" y="141.3" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="309.0" y="152.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">II/1 Libyan</text>
<text x="309.0" y="162.3" font-size="8" text-anchor="middle" fill="#222">Inf regt · CPA 8 · M−1</text></g>
<path d="M 141.0,180.3 L 222.0,133.5" fill="none" stroke="#b00" stroke-width="3" marker-end="url(#arr-b00)"/>
<g><rect x="192.0" y="124.5" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="222.0" y="135.5" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">1 Lib Art</text>
<text x="222.0" y="145.5" font-size="8" text-anchor="middle" fill="#222">Arty · Bar 9 · CPA 8</text></g>
<path d="M 303.0,180.3 L 384.0,133.5 L 465.0,180.3" fill="none" stroke="#1d4ed8" stroke-width="3" marker-end="url(#arr-1d4ed8)" stroke-dasharray="6 4"/>
<text x="343.0" y="146.3" font-size="10" fill="#1d4ed8" font-weight="bold" text-anchor="middle">React −2 CP</text>
<g><rect x="435.0" y="171.3" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="465.0" y="182.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">11 Hussars</text>
<text x="465.0" y="192.3" font-size="8" text-anchor="middle" fill="#222">Armd cars · CPA 25 · M+2</text></g>
<g><rect x="354.0" y="218.1" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="384.0" y="229.1" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">1 RNF</text>
<text x="384.0" y="239.1" font-size="8" text-anchor="middle" fill="#222">MG bn · CPA 8 · M+1</text></g>
<g><rect x="435.0" y="264.8" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="465.0" y="275.8" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">4 RHA</text>
<text x="465.0" y="285.8" font-size="8" text-anchor="middle" fill="#222">Arty · Bar 9 · CPA 10</text></g>
</svg></div><div class="note">
<p><b>F. Reserve Designation.</b> Italy puts the L3 tankettes in <b>Reserve</b> (0 CP). Reserves may move again later even if far from the enemy [<a href="rules/40-movement#spi-8.23">8.23</a>, <a href="rules/50-stacking-and-zoc#spi-18.0">18.0</a>].</p>
<p><b>G1. Movement Segment.</b> Both Libyan regiments march 3 road hexes: <b>3 CP</b> each (road = 1 CP/hex for non-motorised). The artillery follows 1 hex (1 CP).</p>
<p>The 11th Hussars, non-phasing, use <b>Reaction</b> to fall back 2 road hexes as the Italians close: motorised road cost ½ × 2 = 1, plus Reaction is limited and costs CPs against their own CPA. Call it <b>2 CP</b>.</p>
<p>Result: two regiments stacked at 3-01 on the coast, directly below the RNF at the top of the pass at 4-02. They are adjacent and in the RNF's <b>Zone of Control</b> — combat is now mandatory [10, 11].</p></div></div></section><section class="panel"><h2>3 · Breakdown Determination Segment</h2><div class="row"><div class="map"><svg viewBox="0 0 721 564" width="721" height="564" xmlns="http://www.w3.org/2000/svg">
<defs>
 <pattern id="rough" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#e2cf9e"/><path d="M0 8 L8 0" stroke="#a88d55" stroke-width="1.2"/></pattern>
 <marker id="arr-b00" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#b00"/></marker>
 <marker id="arr-1d4ed8" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#1d4ed8"/></marker>
</defs>
<polygon points="114.0,40.0 87.0,86.8 33.0,86.8 6.0,40.0 33.0,-6.8 87.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="114.0,133.5 87.0,180.3 33.0,180.3 6.0,133.5 33.0,86.8 87.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">0-01</text>
<polygon points="114.0,227.1 87.0,273.8 33.0,273.8 6.0,227.1 33.0,180.3 87.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">0-02</text>
<polygon points="114.0,320.6 87.0,367.4 33.0,367.4 6.0,320.6 33.0,273.8 87.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">0-03</text>
<polygon points="114.0,414.1 87.0,460.9 33.0,460.9 6.0,414.1 33.0,367.4 87.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">0-04</text>
<polygon points="195.0,86.8 168.0,133.5 114.0,133.5 87.0,86.8 114.0,40.0 168.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="195.0,180.3 168.0,227.1 114.0,227.1 87.0,180.3 114.0,133.5 168.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">1-01</text>
<polygon points="195.0,273.8 168.0,320.6 114.0,320.6 87.0,273.8 114.0,227.1 168.0,227.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">1-02</text>
<polygon points="195.0,367.4 168.0,414.1 114.0,414.1 87.0,367.4 114.0,320.6 168.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">1-03</text>
<polygon points="195.0,460.9 168.0,507.7 114.0,507.7 87.0,460.9 114.0,414.1 168.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">1-04</text>
<polygon points="276.0,40.0 249.0,86.8 195.0,86.8 168.0,40.0 195.0,-6.8 249.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="276.0,133.5 249.0,180.3 195.0,180.3 168.0,133.5 195.0,86.8 249.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">2-01</text>
<polygon points="276.0,227.1 249.0,273.8 195.0,273.8 168.0,227.1 195.0,180.3 249.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">2-02</text>
<polygon points="276.0,320.6 249.0,367.4 195.0,367.4 168.0,320.6 195.0,273.8 249.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">2-03</text>
<polygon points="276.0,414.1 249.0,460.9 195.0,460.9 168.0,414.1 195.0,367.4 249.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">2-04</text>
<polygon points="357.0,86.8 330.0,133.5 276.0,133.5 249.0,86.8 276.0,40.0 330.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="357.0,180.3 330.0,227.1 276.0,227.1 249.0,180.3 276.0,133.5 330.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">3-01</text>
<polygon points="357.0,273.8 330.0,320.6 276.0,320.6 249.0,273.8 276.0,227.1 330.0,227.1" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">3-02</text>
<polygon points="357.0,367.4 330.0,414.1 276.0,414.1 249.0,367.4 276.0,320.6 330.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">3-03</text>
<polygon points="357.0,460.9 330.0,507.7 276.0,507.7 249.0,460.9 276.0,414.1 330.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">3-04</text>
<polygon points="438.0,40.0 411.0,86.8 357.0,86.8 330.0,40.0 357.0,-6.8 411.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="438.0,133.5 411.0,180.3 357.0,180.3 330.0,133.5 357.0,86.8 411.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">4-01</text>
<polygon points="438.0,227.1 411.0,273.8 357.0,273.8 330.0,227.1 357.0,180.3 411.0,180.3" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">4-02</text>
<polygon points="438.0,320.6 411.0,367.4 357.0,367.4 330.0,320.6 357.0,273.8 411.0,273.8" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">4-03</text>
<polygon points="438.0,414.1 411.0,460.9 357.0,460.9 330.0,414.1 357.0,367.4 411.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">4-04</text>
<polygon points="519.0,86.8 492.0,133.5 438.0,133.5 411.0,86.8 438.0,40.0 492.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="519.0,180.3 492.0,227.1 438.0,227.1 411.0,180.3 438.0,133.5 492.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">5-01</text>
<polygon points="519.0,273.8 492.0,320.6 438.0,320.6 411.0,273.8 438.0,227.1 492.0,227.1" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">5-02</text>
<polygon points="519.0,367.4 492.0,414.1 438.0,414.1 411.0,367.4 438.0,320.6 492.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">5-03</text>
<polygon points="519.0,460.9 492.0,507.7 438.0,507.7 411.0,460.9 438.0,414.1 492.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">5-04</text>
<polygon points="600.0,40.0 573.0,86.8 519.0,86.8 492.0,40.0 519.0,-6.8 573.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="600.0,133.5 573.0,180.3 519.0,180.3 492.0,133.5 519.0,86.8 573.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">6-01</text>
<polygon points="600.0,227.1 573.0,273.8 519.0,273.8 492.0,227.1 519.0,180.3 573.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">6-02</text>
<polygon points="600.0,320.6 573.0,367.4 519.0,367.4 492.0,320.6 519.0,273.8 573.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">6-03</text>
<polygon points="600.0,414.1 573.0,460.9 519.0,460.9 492.0,414.1 519.0,367.4 573.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">6-04</text>
<polygon points="681.0,86.8 654.0,133.5 600.0,133.5 573.0,86.8 600.0,40.0 654.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="681.0,180.3 654.0,227.1 600.0,227.1 573.0,180.3 600.0,133.5 654.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">7-01</text>
<polygon points="681.0,273.8 654.0,320.6 600.0,320.6 573.0,273.8 600.0,227.1 654.0,227.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">7-02</text>
<polygon points="681.0,367.4 654.0,414.1 600.0,414.1 573.0,367.4 600.0,320.6 654.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">7-03</text>
<polygon points="681.0,460.9 654.0,507.7 600.0,507.7 573.0,460.9 600.0,414.1 654.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">7-04</text>
<polyline points="60.0,133.5 141.0,180.3 222.0,133.5 303.0,180.3 384.0,133.5 465.0,180.3 546.0,133.5 627.0,180.3" fill="none" stroke="#333" stroke-width="4"/>
<polyline points="60.0,133.5 141.0,180.3 222.0,133.5 303.0,180.3 384.0,133.5 465.0,180.3 546.0,133.5 627.0,180.3" fill="none" stroke="#f3e6bf" stroke-width="1.5" stroke-dasharray="6 6"/>
<polyline points="384.0,133.5 384.0,227.1 384.0,320.6 465.0,367.4 546.0,320.6" fill="none" stroke="#7a5a2a" stroke-width="2.5" stroke-dasharray="7 5"/>
<line x1="33.0" y1="180.3" x2="87.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="114.0" y1="227.1" x2="168.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="195.0" y1="180.3" x2="168.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="87.0" y1="180.3" x2="114.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="249.0" y1="180.3" x2="195.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="330.0" y1="227.1" x2="276.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="357.0" y1="180.3" x2="330.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="249.0" y1="180.3" x2="276.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="492.0" y1="227.1" x2="438.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="519.0" y1="180.3" x2="492.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="411.0" y1="180.3" x2="438.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="573.0" y1="180.3" x2="519.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="654.0" y1="227.1" x2="600.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="573.0" y1="180.3" x2="600.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<circle cx="546.0" cy="306.6" r="5" fill="#2b6cb0"/><text x="546.0" y="298.6" font-size="10" text-anchor="middle" fill="#2b6cb0">Bir Sofafi</text>
<text x="90.0" y="44.0" font-size="13" fill="#2b5c7a" font-style="italic">Mediterranean</text>
<text x="388.0" y="191.5" font-size="10" fill="#7a3b1e" font-weight="bold" text-anchor="middle">Halfaya Pass</text>
<text x="141.0" y="464.9" font-size="11" fill="#8a7a55" font-style="italic" text-anchor="middle">Libyan plateau</text>
<g><rect x="273.0" y="171.3" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="303.0" y="182.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">I/1 Libyan</text>
<text x="303.0" y="192.3" font-size="8" text-anchor="middle" fill="#222">Inf regt · CPA 8 · M−1</text></g>
<g><rect x="279.0" y="141.3" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="309.0" y="152.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">II/1 Libyan</text>
<text x="309.0" y="162.3" font-size="8" text-anchor="middle" fill="#222">Inf regt · CPA 8 · M−1</text></g>
<g><rect x="192.0" y="124.5" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="222.0" y="135.5" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">1 Lib Art</text>
<text x="222.0" y="145.5" font-size="8" text-anchor="middle" fill="#222">Arty · Bar 9 · CPA 8</text></g>
<g><rect x="30.0" y="218.1" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="60.0" y="229.1" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">IX L3</text>
<text x="60.0" y="239.1" font-size="8" text-anchor="middle" fill="#222">Tankette bn · CPA 25</text></g>
<rect x="78.0" y="209.1" width="30" height="14" rx="2" fill="#fff" stroke="#b00" stroke-width="1.2"/>
<text x="93.0" y="219.1" font-size="8" text-anchor="middle" fill="#b00" font-weight="bold">RES I</text>
<g><rect x="435.0" y="171.3" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="465.0" y="182.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">11 Hussars</text>
<text x="465.0" y="192.3" font-size="8" text-anchor="middle" fill="#222">Armd cars · CPA 25 · M+2</text></g>
<rect x="483.0" y="162.3" width="30" height="14" rx="2" fill="#fff" stroke="#b00" stroke-width="1.2"/>
<text x="498.0" y="172.3" font-size="8" text-anchor="middle" fill="#b00" font-weight="bold">BD 1</text>
<g><rect x="354.0" y="218.1" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="384.0" y="229.1" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">1 RNF</text>
<text x="384.0" y="239.1" font-size="8" text-anchor="middle" fill="#222">MG bn · CPA 8 · M+1</text></g>
<g><rect x="435.0" y="264.8" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="465.0" y="275.8" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">4 RHA</text>
<text x="465.0" y="285.8" font-size="8" text-anchor="middle" fill="#222">Arty · Bar 9 · CPA 10</text></g>
</svg></div><div class="note">
<p><b>G2. Breakdown Determination.</b> Every vehicle unit of <i>both</i> sides that moved rolls for breakdown. Breakdown Points accumulate per hex type — road hex ½, clear 4, rough 8, desert 24, down-escarpment +6 — against the vehicle's Breakdown Adjustment Rating [21].</p>
<p>The Hussars moved 2 road hexes (1 BP): a bad roll leaves <b>one armoured-car TOE point broken down</b>. It needs towing to a repair facility or a field repair attempt in the Repair Phase [22]. The L3s haven't moved yet, so no roll.</p>
<p>Desert attrition, no shots fired. In the full Logistics Game each of these moves also burned fuel per vehicle per hex.</p></div></div></section><section class="panel"><h2>4 · Combat Segment</h2><div class="row"><div class="map"><svg viewBox="0 0 721 564" width="721" height="564" xmlns="http://www.w3.org/2000/svg">
<defs>
 <pattern id="rough" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#e2cf9e"/><path d="M0 8 L8 0" stroke="#a88d55" stroke-width="1.2"/></pattern>
 <marker id="arr-b00" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#b00"/></marker>
 <marker id="arr-1d4ed8" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#1d4ed8"/></marker>
</defs>
<polygon points="114.0,40.0 87.0,86.8 33.0,86.8 6.0,40.0 33.0,-6.8 87.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="114.0,133.5 87.0,180.3 33.0,180.3 6.0,133.5 33.0,86.8 87.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">0-01</text>
<polygon points="114.0,227.1 87.0,273.8 33.0,273.8 6.0,227.1 33.0,180.3 87.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">0-02</text>
<polygon points="114.0,320.6 87.0,367.4 33.0,367.4 6.0,320.6 33.0,273.8 87.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">0-03</text>
<polygon points="114.0,414.1 87.0,460.9 33.0,460.9 6.0,414.1 33.0,367.4 87.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">0-04</text>
<polygon points="195.0,86.8 168.0,133.5 114.0,133.5 87.0,86.8 114.0,40.0 168.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="195.0,180.3 168.0,227.1 114.0,227.1 87.0,180.3 114.0,133.5 168.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">1-01</text>
<polygon points="195.0,273.8 168.0,320.6 114.0,320.6 87.0,273.8 114.0,227.1 168.0,227.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">1-02</text>
<polygon points="195.0,367.4 168.0,414.1 114.0,414.1 87.0,367.4 114.0,320.6 168.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">1-03</text>
<polygon points="195.0,460.9 168.0,507.7 114.0,507.7 87.0,460.9 114.0,414.1 168.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">1-04</text>
<polygon points="276.0,40.0 249.0,86.8 195.0,86.8 168.0,40.0 195.0,-6.8 249.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="276.0,133.5 249.0,180.3 195.0,180.3 168.0,133.5 195.0,86.8 249.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">2-01</text>
<polygon points="276.0,227.1 249.0,273.8 195.0,273.8 168.0,227.1 195.0,180.3 249.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">2-02</text>
<polygon points="276.0,320.6 249.0,367.4 195.0,367.4 168.0,320.6 195.0,273.8 249.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">2-03</text>
<polygon points="276.0,414.1 249.0,460.9 195.0,460.9 168.0,414.1 195.0,367.4 249.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">2-04</text>
<polygon points="357.0,86.8 330.0,133.5 276.0,133.5 249.0,86.8 276.0,40.0 330.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="357.0,180.3 330.0,227.1 276.0,227.1 249.0,180.3 276.0,133.5 330.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">3-01</text>
<polygon points="357.0,273.8 330.0,320.6 276.0,320.6 249.0,273.8 276.0,227.1 330.0,227.1" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">3-02</text>
<polygon points="357.0,367.4 330.0,414.1 276.0,414.1 249.0,367.4 276.0,320.6 330.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">3-03</text>
<polygon points="357.0,460.9 330.0,507.7 276.0,507.7 249.0,460.9 276.0,414.1 330.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">3-04</text>
<polygon points="438.0,40.0 411.0,86.8 357.0,86.8 330.0,40.0 357.0,-6.8 411.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="438.0,133.5 411.0,180.3 357.0,180.3 330.0,133.5 357.0,86.8 411.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">4-01</text>
<polygon points="438.0,227.1 411.0,273.8 357.0,273.8 330.0,227.1 357.0,180.3 411.0,180.3" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">4-02</text>
<polygon points="438.0,320.6 411.0,367.4 357.0,367.4 330.0,320.6 357.0,273.8 411.0,273.8" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">4-03</text>
<polygon points="438.0,414.1 411.0,460.9 357.0,460.9 330.0,414.1 357.0,367.4 411.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">4-04</text>
<polygon points="519.0,86.8 492.0,133.5 438.0,133.5 411.0,86.8 438.0,40.0 492.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="519.0,180.3 492.0,227.1 438.0,227.1 411.0,180.3 438.0,133.5 492.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">5-01</text>
<polygon points="519.0,273.8 492.0,320.6 438.0,320.6 411.0,273.8 438.0,227.1 492.0,227.1" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">5-02</text>
<polygon points="519.0,367.4 492.0,414.1 438.0,414.1 411.0,367.4 438.0,320.6 492.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">5-03</text>
<polygon points="519.0,460.9 492.0,507.7 438.0,507.7 411.0,460.9 438.0,414.1 492.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">5-04</text>
<polygon points="600.0,40.0 573.0,86.8 519.0,86.8 492.0,40.0 519.0,-6.8 573.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="600.0,133.5 573.0,180.3 519.0,180.3 492.0,133.5 519.0,86.8 573.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">6-01</text>
<polygon points="600.0,227.1 573.0,273.8 519.0,273.8 492.0,227.1 519.0,180.3 573.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">6-02</text>
<polygon points="600.0,320.6 573.0,367.4 519.0,367.4 492.0,320.6 519.0,273.8 573.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">6-03</text>
<polygon points="600.0,414.1 573.0,460.9 519.0,460.9 492.0,414.1 519.0,367.4 573.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">6-04</text>
<polygon points="681.0,86.8 654.0,133.5 600.0,133.5 573.0,86.8 600.0,40.0 654.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="681.0,180.3 654.0,227.1 600.0,227.1 573.0,180.3 600.0,133.5 654.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">7-01</text>
<polygon points="681.0,273.8 654.0,320.6 600.0,320.6 573.0,273.8 600.0,227.1 654.0,227.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">7-02</text>
<polygon points="681.0,367.4 654.0,414.1 600.0,414.1 573.0,367.4 600.0,320.6 654.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">7-03</text>
<polygon points="681.0,460.9 654.0,507.7 600.0,507.7 573.0,460.9 600.0,414.1 654.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">7-04</text>
<polyline points="60.0,133.5 141.0,180.3 222.0,133.5 303.0,180.3 384.0,133.5 465.0,180.3 546.0,133.5 627.0,180.3" fill="none" stroke="#333" stroke-width="4"/>
<polyline points="60.0,133.5 141.0,180.3 222.0,133.5 303.0,180.3 384.0,133.5 465.0,180.3 546.0,133.5 627.0,180.3" fill="none" stroke="#f3e6bf" stroke-width="1.5" stroke-dasharray="6 6"/>
<polyline points="384.0,133.5 384.0,227.1 384.0,320.6 465.0,367.4 546.0,320.6" fill="none" stroke="#7a5a2a" stroke-width="2.5" stroke-dasharray="7 5"/>
<line x1="33.0" y1="180.3" x2="87.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="114.0" y1="227.1" x2="168.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="195.0" y1="180.3" x2="168.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="87.0" y1="180.3" x2="114.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="249.0" y1="180.3" x2="195.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="330.0" y1="227.1" x2="276.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="357.0" y1="180.3" x2="330.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="249.0" y1="180.3" x2="276.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="492.0" y1="227.1" x2="438.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="519.0" y1="180.3" x2="492.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="411.0" y1="180.3" x2="438.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="573.0" y1="180.3" x2="519.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="654.0" y1="227.1" x2="600.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="573.0" y1="180.3" x2="600.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<circle cx="546.0" cy="306.6" r="5" fill="#2b6cb0"/><text x="546.0" y="298.6" font-size="10" text-anchor="middle" fill="#2b6cb0">Bir Sofafi</text>
<text x="90.0" y="44.0" font-size="13" fill="#2b5c7a" font-style="italic">Mediterranean</text>
<text x="388.0" y="191.5" font-size="10" fill="#7a3b1e" font-weight="bold" text-anchor="middle">Halfaya Pass</text>
<text x="141.0" y="464.9" font-size="11" fill="#8a7a55" font-style="italic" text-anchor="middle">Libyan plateau</text>
<g><rect x="273.0" y="171.3" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="303.0" y="182.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">I/1 Libyan</text>
<text x="303.0" y="192.3" font-size="8" text-anchor="middle" fill="#222">Inf regt · CPA 8 · M−1</text></g>
<g><rect x="279.0" y="141.3" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="309.0" y="152.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">II/1 Libyan</text>
<text x="309.0" y="162.3" font-size="8" text-anchor="middle" fill="#222">Inf regt · CPA 8 · M−1</text></g>
<g><rect x="192.0" y="124.5" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="222.0" y="135.5" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">1 Lib Art</text>
<text x="222.0" y="145.5" font-size="8" text-anchor="middle" fill="#222">Arty · Bar 9 · CPA 8</text></g>
<rect x="240.0" y="115.5" width="30" height="14" rx="2" fill="#fff" stroke="#b00" stroke-width="1.2"/>
<text x="255.0" y="125.5" font-size="8" text-anchor="middle" fill="#b00" font-weight="bold">FWD</text>
<g><rect x="30.0" y="218.1" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="60.0" y="229.1" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">IX L3</text>
<text x="60.0" y="239.1" font-size="8" text-anchor="middle" fill="#222">Tankette bn · CPA 25</text></g>
<rect x="78.0" y="209.1" width="30" height="14" rx="2" fill="#fff" stroke="#b00" stroke-width="1.2"/>
<text x="93.0" y="219.1" font-size="8" text-anchor="middle" fill="#b00" font-weight="bold">RES I</text>
<polygon points="435.3,227.1 413.9,239.5 420.3,263.3 396.4,257.0 384.0,278.4 371.6,257.0 347.7,263.3 354.1,239.5 332.7,227.1 354.1,214.7 347.7,190.8 371.6,197.1 384.0,175.8 396.4,197.1 420.3,190.8 413.9,214.7" fill="#ff5a36" opacity="0.35" stroke="#b00" stroke-width="1.5"/><text x="384.0" y="293.1" font-size="10" fill="#b00" font-weight="bold" text-anchor="middle">Barrage 3 pts → RNF</text>
<path d="M 303.0,180.3 L 384.0,227.1" fill="none" stroke="#b00" stroke-width="3" marker-end="url(#arr-b00)"/>
<text x="343.0" y="146.3" font-size="10" fill="#b00" font-weight="bold" text-anchor="middle">Close Assault</text>
<g><rect x="435.0" y="171.3" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="465.0" y="182.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">11 Hussars</text>
<text x="465.0" y="192.3" font-size="8" text-anchor="middle" fill="#222">Armd cars · CPA 25 · M+2</text></g>
<g><rect x="354.0" y="218.1" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="384.0" y="229.1" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">1 RNF</text>
<text x="384.0" y="239.1" font-size="8" text-anchor="middle" fill="#222">MG bn · CPA 8 · M+1</text></g>
<g><rect x="435.0" y="264.8" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="465.0" y="275.8" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">4 RHA</text>
<text x="465.0" y="285.8" font-size="8" text-anchor="middle" fill="#222">Arty · Bar 9 · CPA 10</text></g>
<rect x="483.0" y="255.8" width="30" height="14" rx="2" fill="#fff" stroke="#b00" stroke-width="1.2"/>
<text x="498.0" y="265.8" font-size="8" text-anchor="middle" fill="#b00" font-weight="bold">BACK</text>
</svg></div><div class="note">
<p><b>G3. Combat Segment</b> — strict order:</p>
<ol>
<li><b>Position.</b> Italian guns go <b>Forward</b> (can split fire; vulnerable if overrun). RHA stays <b>Back</b>.</li>
<li><b>Barrage.</b> Both plot secretly. Italy fires at "the infantry in 4-02" — target by <i>type</i>, not unit; it mostly fights blind [<a href="rules/60-combat#spi-12.24">12.24</a>]. RNF pays <b>3 CP</b> for being barraged. Italian guns: 3 TOE × Barrage 9 = 27 Raw → <b>3 Actual</b>; on the Barrage table [<a href="rules/60-combat#spi-12.6">12.6</a>] the 3–4 column vs Infantry gives <i>No effect</i> on 11–44, <i>Pinned</i> on 45–66 — losses need 5+ points. Italy rolls 52 → <b>RNF is Pinned</b>. RHA's 3 points at the stack below: 23 → no effect.</li>
<li><b>Retreat Before Assault.</b> Pinned units may not retreat [12.6 note] — the RNF must stand. That is what barrage is for.</li>
<li><b>Force Assignment.</b> Both secretly assign TOE points to Anti-Armor or Close Assault. No armour is engaged, so everything to Close Assault.</li>
<li><b>Anti-Armor.</b> Nothing to shoot at.</li>
<li><b>Close Assault.</b> Costs attacker <b>5 CP</b>, defender <b>3 CP</b>. Maths in the box below.</li>
</ol></div></div>
<div class="calc">
<h3>Close Assault: 2 Libyan regiments (3-01) vs 1 RNF (4-02)</h3>
<table>
<tr><th>Rule of ten [<a href="rules/60-combat#spi-11.32">11.32</a>]</th><td><b>Actual</b> points = (Rating × TOE points used) ÷ 10, rounded (11.4→11, 11.5→12). Everything in combat is compared in Actual points.</td></tr>
<tr><th>Attacker</th><td>2 regts × 12 TOE × Off rating 1 = 24 Raw → <b>2 Actual</b></td></tr>
<tr><th>Defender</th><td>1 RNF: 7 TOE × Def rating 2 = 14 Raw → <b>1 Actual</b></td></tr>
<tr><th>Differential</th><td>2 − 1 = <b>+1</b></td></tr>
<tr><th>2:1 Raw superiority [<a href="rules/60-combat#spi-15.51">15.51</a>]</th><td>24 vs 14 — not double → no shift</td></tr>
<tr><th>Terrain [<a href="rules/40-movement#spi-8.37">8.37</a>]</th><td>Rough <b>L2</b>, Up Escarpment <b>L3</b> → five columns left → <b>−4</b></td></tr>
<tr><th>Morale [<a href="rules/60-combat#spi-15.6">15.6</a>, <a href="rules/10-units-and-state#spi-17.2">17.2</a>]</th><td>Each side rolls on the Morale Modification Table for its Cohesion (both 0 → no change). Italians −1, RNF +1 → attacker minus defender = −2 → two columns left → <b>−6</b></td></tr>
<tr><th>Size [<a href="rules/60-combat#spi-15.53">15.53</a>]</th><td>Largest unit regiment (≈ brigade) vs battalion → 2 columns to the larger side → <b>−4</b></td></tr>
<tr><th>Final column</th><td><b>−4/−5</b> on the CRT [<a href="rules/60-combat#spi-15.79">15.79</a>]</td></tr>
<tr><th>Attacker rolls 3,4 → "34"</th><td>−4 column, attacker losses: 15% band is 34–44 → <b>Italians lose 15%</b> ≈ 4 of 24 TOE points</td></tr>
<tr><th>Same dice, summed = 7</th><td>Engaged row at −4 is "12" only → <b>not Engaged</b>; Captured row for attacker at −4: 2–4 → no</td></tr>
<tr><th>Defender rolls 1,2 → "12"</th><td>−4 column, defender losses: 15% band is "11", so 12 falls in the 10% band → <b>RNF loses 10%</b> ≈ 1 TOE point. Sum 3 → Captured possible (2–3 at −4): one more die decides what fraction of the loss is prisoners [<a href="rules/60-combat#spi-15.89">15.89</a>]</td></tr>
<tr><th>Outcome</th><td>RNF holds the pass at 6 TOE. Italians bloodied: 4 points gone, 3 DP each from over-CPA (next box). Both remain adjacent, in contact.</td></tr>
</table>
<p class="fine">Five column shifts for terrain is why nobody storms an escarpment frontally. In real play the Italians would send the Bersaglieri and tankettes round by a track, or barrage for two stages first. The escarpment also blocks vehicles entirely, so no Combined Arms bonus is even possible here.</p>
</div></section><section class="panel"><h2>5 · The ledger: Capability Points and Cohesion</h2><div class="row"><div class="map"><svg viewBox="0 0 721 564" width="721" height="564" xmlns="http://www.w3.org/2000/svg">
<defs>
 <pattern id="rough" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#e2cf9e"/><path d="M0 8 L8 0" stroke="#a88d55" stroke-width="1.2"/></pattern>
 <marker id="arr-b00" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#b00"/></marker>
 <marker id="arr-1d4ed8" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#1d4ed8"/></marker>
</defs>
<polygon points="114.0,40.0 87.0,86.8 33.0,86.8 6.0,40.0 33.0,-6.8 87.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="114.0,133.5 87.0,180.3 33.0,180.3 6.0,133.5 33.0,86.8 87.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">0-01</text>
<polygon points="114.0,227.1 87.0,273.8 33.0,273.8 6.0,227.1 33.0,180.3 87.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">0-02</text>
<polygon points="114.0,320.6 87.0,367.4 33.0,367.4 6.0,320.6 33.0,273.8 87.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">0-03</text>
<polygon points="114.0,414.1 87.0,460.9 33.0,460.9 6.0,414.1 33.0,367.4 87.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">0-04</text>
<polygon points="195.0,86.8 168.0,133.5 114.0,133.5 87.0,86.8 114.0,40.0 168.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="195.0,180.3 168.0,227.1 114.0,227.1 87.0,180.3 114.0,133.5 168.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">1-01</text>
<polygon points="195.0,273.8 168.0,320.6 114.0,320.6 87.0,273.8 114.0,227.1 168.0,227.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">1-02</text>
<polygon points="195.0,367.4 168.0,414.1 114.0,414.1 87.0,367.4 114.0,320.6 168.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">1-03</text>
<polygon points="195.0,460.9 168.0,507.7 114.0,507.7 87.0,460.9 114.0,414.1 168.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">1-04</text>
<polygon points="276.0,40.0 249.0,86.8 195.0,86.8 168.0,40.0 195.0,-6.8 249.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="276.0,133.5 249.0,180.3 195.0,180.3 168.0,133.5 195.0,86.8 249.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">2-01</text>
<polygon points="276.0,227.1 249.0,273.8 195.0,273.8 168.0,227.1 195.0,180.3 249.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">2-02</text>
<polygon points="276.0,320.6 249.0,367.4 195.0,367.4 168.0,320.6 195.0,273.8 249.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">2-03</text>
<polygon points="276.0,414.1 249.0,460.9 195.0,460.9 168.0,414.1 195.0,367.4 249.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">2-04</text>
<polygon points="357.0,86.8 330.0,133.5 276.0,133.5 249.0,86.8 276.0,40.0 330.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="357.0,180.3 330.0,227.1 276.0,227.1 249.0,180.3 276.0,133.5 330.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">3-01</text>
<polygon points="357.0,273.8 330.0,320.6 276.0,320.6 249.0,273.8 276.0,227.1 330.0,227.1" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">3-02</text>
<polygon points="357.0,367.4 330.0,414.1 276.0,414.1 249.0,367.4 276.0,320.6 330.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">3-03</text>
<polygon points="357.0,460.9 330.0,507.7 276.0,507.7 249.0,460.9 276.0,414.1 330.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">3-04</text>
<polygon points="438.0,40.0 411.0,86.8 357.0,86.8 330.0,40.0 357.0,-6.8 411.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="438.0,133.5 411.0,180.3 357.0,180.3 330.0,133.5 357.0,86.8 411.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">4-01</text>
<polygon points="438.0,227.1 411.0,273.8 357.0,273.8 330.0,227.1 357.0,180.3 411.0,180.3" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">4-02</text>
<polygon points="438.0,320.6 411.0,367.4 357.0,367.4 330.0,320.6 357.0,273.8 411.0,273.8" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">4-03</text>
<polygon points="438.0,414.1 411.0,460.9 357.0,460.9 330.0,414.1 357.0,367.4 411.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">4-04</text>
<polygon points="519.0,86.8 492.0,133.5 438.0,133.5 411.0,86.8 438.0,40.0 492.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="519.0,180.3 492.0,227.1 438.0,227.1 411.0,180.3 438.0,133.5 492.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">5-01</text>
<polygon points="519.0,273.8 492.0,320.6 438.0,320.6 411.0,273.8 438.0,227.1 492.0,227.1" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">5-02</text>
<polygon points="519.0,367.4 492.0,414.1 438.0,414.1 411.0,367.4 438.0,320.6 492.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">5-03</text>
<polygon points="519.0,460.9 492.0,507.7 438.0,507.7 411.0,460.9 438.0,414.1 492.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">5-04</text>
<polygon points="600.0,40.0 573.0,86.8 519.0,86.8 492.0,40.0 519.0,-6.8 573.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="600.0,133.5 573.0,180.3 519.0,180.3 492.0,133.5 519.0,86.8 573.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">6-01</text>
<polygon points="600.0,227.1 573.0,273.8 519.0,273.8 492.0,227.1 519.0,180.3 573.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">6-02</text>
<polygon points="600.0,320.6 573.0,367.4 519.0,367.4 492.0,320.6 519.0,273.8 573.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">6-03</text>
<polygon points="600.0,414.1 573.0,460.9 519.0,460.9 492.0,414.1 519.0,367.4 573.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">6-04</text>
<polygon points="681.0,86.8 654.0,133.5 600.0,133.5 573.0,86.8 600.0,40.0 654.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="681.0,180.3 654.0,227.1 600.0,227.1 573.0,180.3 600.0,133.5 654.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">7-01</text>
<polygon points="681.0,273.8 654.0,320.6 600.0,320.6 573.0,273.8 600.0,227.1 654.0,227.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">7-02</text>
<polygon points="681.0,367.4 654.0,414.1 600.0,414.1 573.0,367.4 600.0,320.6 654.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">7-03</text>
<polygon points="681.0,460.9 654.0,507.7 600.0,507.7 573.0,460.9 600.0,414.1 654.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">7-04</text>
<polyline points="60.0,133.5 141.0,180.3 222.0,133.5 303.0,180.3 384.0,133.5 465.0,180.3 546.0,133.5 627.0,180.3" fill="none" stroke="#333" stroke-width="4"/>
<polyline points="60.0,133.5 141.0,180.3 222.0,133.5 303.0,180.3 384.0,133.5 465.0,180.3 546.0,133.5 627.0,180.3" fill="none" stroke="#f3e6bf" stroke-width="1.5" stroke-dasharray="6 6"/>
<polyline points="384.0,133.5 384.0,227.1 384.0,320.6 465.0,367.4 546.0,320.6" fill="none" stroke="#7a5a2a" stroke-width="2.5" stroke-dasharray="7 5"/>
<line x1="33.0" y1="180.3" x2="87.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="114.0" y1="227.1" x2="168.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="195.0" y1="180.3" x2="168.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="87.0" y1="180.3" x2="114.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="249.0" y1="180.3" x2="195.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="330.0" y1="227.1" x2="276.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="357.0" y1="180.3" x2="330.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="249.0" y1="180.3" x2="276.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="492.0" y1="227.1" x2="438.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="519.0" y1="180.3" x2="492.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="411.0" y1="180.3" x2="438.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="573.0" y1="180.3" x2="519.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="654.0" y1="227.1" x2="600.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="573.0" y1="180.3" x2="600.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<circle cx="546.0" cy="306.6" r="5" fill="#2b6cb0"/><text x="546.0" y="298.6" font-size="10" text-anchor="middle" fill="#2b6cb0">Bir Sofafi</text>
<text x="90.0" y="44.0" font-size="13" fill="#2b5c7a" font-style="italic">Mediterranean</text>
<text x="388.0" y="191.5" font-size="10" fill="#7a3b1e" font-weight="bold" text-anchor="middle">Halfaya Pass</text>
<text x="141.0" y="464.9" font-size="11" fill="#8a7a55" font-style="italic" text-anchor="middle">Libyan plateau</text>
<g><rect x="273.0" y="171.3" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="303.0" y="182.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">I/1 Libyan</text>
<text x="303.0" y="192.3" font-size="8" text-anchor="middle" fill="#222">Inf regt · CPA 8 · M−1</text></g>
<g><rect x="279.0" y="141.3" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="309.0" y="152.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">II/1 Libyan</text>
<text x="309.0" y="162.3" font-size="8" text-anchor="middle" fill="#222">Inf regt · CPA 8 · M−1</text></g>
<g><rect x="192.0" y="124.5" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="222.0" y="135.5" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">1 Lib Art</text>
<text x="222.0" y="145.5" font-size="8" text-anchor="middle" fill="#222">Arty · Bar 9 · CPA 8</text></g>
<g><rect x="30.0" y="218.1" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="60.0" y="229.1" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">IX L3</text>
<text x="60.0" y="239.1" font-size="8" text-anchor="middle" fill="#222">Tankette bn · CPA 25</text></g>
<rect x="78.0" y="209.1" width="30" height="14" rx="2" fill="#fff" stroke="#b00" stroke-width="1.2"/>
<text x="93.0" y="219.1" font-size="8" text-anchor="middle" fill="#b00" font-weight="bold">RES I</text>
<g><rect x="435.0" y="171.3" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="465.0" y="182.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">11 Hussars</text>
<text x="465.0" y="192.3" font-size="8" text-anchor="middle" fill="#222">Armd cars · CPA 25 · M+2</text></g>
<rect x="483.0" y="162.3" width="30" height="14" rx="2" fill="#fff" stroke="#b00" stroke-width="1.2"/>
<text x="498.0" y="172.3" font-size="8" text-anchor="middle" fill="#b00" font-weight="bold">BD 1</text>
<g><rect x="354.0" y="218.1" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="384.0" y="229.1" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">1 RNF</text>
<text x="384.0" y="239.1" font-size="8" text-anchor="middle" fill="#222">MG bn · CPA 8 · M+1</text></g>
<g><rect x="435.0" y="264.8" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="465.0" y="275.8" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">4 RHA</text>
<text x="465.0" y="285.8" font-size="8" text-anchor="middle" fill="#222">Arty · Bar 9 · CPA 10</text></g>
</svg></div><div class="note">
<p><b>What the ledger says.</b> The Italians took the fight to the pass and paid for it in Cohesion: at −3 each, both regiments now get a morale penalty in their next assault, and only recover +5 per stage of doing <i>nothing</i> [<a href="rules/10-units-and-state#spi-6.24">6.24</a>].</p>
<p>The RNF held, but it has 2 CP left for the Commonwealth half. Pinned by the barrage this segment; pinned by arithmetic next.</p>
<p>In the Logistics Game, add: fuel burned by the Hussars, ammo per TOE point for every shot, water drawn at Bir Sofafi, stores issued at turn start. That's the paperwork.</p></div></div>
<div class="calc">
<h3>CP ledger after cycle 1 — the whole game in one table</h3>
<table class="ledger">
<tr><th>Unit</th><th>CPA</th><th>Spent so far</th><th>Left</th><th>Cohesion</th><th>Notes</th></tr>
<tr><td>I/1 Libyan</td><td>8</td><td>3 move + 3 barraged + 5 assault = <b>11</b></td><td>−3</td><td class="bad">−3</td><td>Exceeded CPA by 3 → 3 Disorganization Points [<a href="rules/10-units-and-state#spi-6.21">6.21</a>]; lost ~2 TOE in the assault</td></tr>
<tr><td>II/1 Libyan</td><td>8</td><td>3 + 3 + 5 = <b>11</b></td><td>−3</td><td class="bad">−3</td><td>Same. Both regiments will fight at worse morale next time.</td></tr>
<tr><td>1 Lib Art</td><td>8</td><td>1 move + 5 barrage (phasing "barrage and/or assault" = 5) = <b>6</b></td><td>2</td><td>0</td><td>Ammo spent from the Supply Unit.</td></tr>
<tr><td>IX L3</td><td>25</td><td><b>0</b></td><td>25</td><td>0</td><td>In Reserve, untouched.</td></tr>
<tr><td>1 RNF</td><td>8</td><td>3 barraged + 3 defend = <b>6</b></td><td class="warn">2</td><td>0</td><td>Pinned this segment; 6 TOE left. Only 2 CP for <i>its own</i> half of the stage [<a href="rules/30-capability-points#spi-6.14">6.14</a>] — it cannot both move and fight.</td></tr>
<tr><td>11 Hussars</td><td>25</td><td>2 react = <b>2</b></td><td>23</td><td>0</td><td>1 TOE point broken down.</td></tr>
<tr><td>4 RHA</td><td>10</td><td>3 barrage = <b>3</b></td><td>7</td><td>0</td><td></td></tr>
</table>
</div></section><section class="panel"><h2>6 · Reserve Release and the Continual Movement decision</h2><div class="row"><div class="map"><svg viewBox="0 0 721 564" width="721" height="564" xmlns="http://www.w3.org/2000/svg">
<defs>
 <pattern id="rough" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#e2cf9e"/><path d="M0 8 L8 0" stroke="#a88d55" stroke-width="1.2"/></pattern>
 <marker id="arr-b00" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#b00"/></marker>
 <marker id="arr-1d4ed8" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#1d4ed8"/></marker>
</defs>
<polygon points="114.0,40.0 87.0,86.8 33.0,86.8 6.0,40.0 33.0,-6.8 87.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="114.0,133.5 87.0,180.3 33.0,180.3 6.0,133.5 33.0,86.8 87.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">0-01</text>
<polygon points="114.0,227.1 87.0,273.8 33.0,273.8 6.0,227.1 33.0,180.3 87.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">0-02</text>
<polygon points="114.0,320.6 87.0,367.4 33.0,367.4 6.0,320.6 33.0,273.8 87.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">0-03</text>
<polygon points="114.0,414.1 87.0,460.9 33.0,460.9 6.0,414.1 33.0,367.4 87.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="60.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">0-04</text>
<polygon points="195.0,86.8 168.0,133.5 114.0,133.5 87.0,86.8 114.0,40.0 168.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="195.0,180.3 168.0,227.1 114.0,227.1 87.0,180.3 114.0,133.5 168.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">1-01</text>
<polygon points="195.0,273.8 168.0,320.6 114.0,320.6 87.0,273.8 114.0,227.1 168.0,227.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">1-02</text>
<polygon points="195.0,367.4 168.0,414.1 114.0,414.1 87.0,367.4 114.0,320.6 168.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">1-03</text>
<polygon points="195.0,460.9 168.0,507.7 114.0,507.7 87.0,460.9 114.0,414.1 168.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="141.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">1-04</text>
<polygon points="276.0,40.0 249.0,86.8 195.0,86.8 168.0,40.0 195.0,-6.8 249.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="276.0,133.5 249.0,180.3 195.0,180.3 168.0,133.5 195.0,86.8 249.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">2-01</text>
<polygon points="276.0,227.1 249.0,273.8 195.0,273.8 168.0,227.1 195.0,180.3 249.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">2-02</text>
<polygon points="276.0,320.6 249.0,367.4 195.0,367.4 168.0,320.6 195.0,273.8 249.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">2-03</text>
<polygon points="276.0,414.1 249.0,460.9 195.0,460.9 168.0,414.1 195.0,367.4 249.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="222.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">2-04</text>
<polygon points="357.0,86.8 330.0,133.5 276.0,133.5 249.0,86.8 276.0,40.0 330.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="357.0,180.3 330.0,227.1 276.0,227.1 249.0,180.3 276.0,133.5 330.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">3-01</text>
<polygon points="357.0,273.8 330.0,320.6 276.0,320.6 249.0,273.8 276.0,227.1 330.0,227.1" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">3-02</text>
<polygon points="357.0,367.4 330.0,414.1 276.0,414.1 249.0,367.4 276.0,320.6 330.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">3-03</text>
<polygon points="357.0,460.9 330.0,507.7 276.0,507.7 249.0,460.9 276.0,414.1 330.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="303.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">3-04</text>
<polygon points="438.0,40.0 411.0,86.8 357.0,86.8 330.0,40.0 357.0,-6.8 411.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="438.0,133.5 411.0,180.3 357.0,180.3 330.0,133.5 357.0,86.8 411.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">4-01</text>
<polygon points="438.0,227.1 411.0,273.8 357.0,273.8 330.0,227.1 357.0,180.3 411.0,180.3" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">4-02</text>
<polygon points="438.0,320.6 411.0,367.4 357.0,367.4 330.0,320.6 357.0,273.8 411.0,273.8" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">4-03</text>
<polygon points="438.0,414.1 411.0,460.9 357.0,460.9 330.0,414.1 357.0,367.4 411.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="384.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">4-04</text>
<polygon points="519.0,86.8 492.0,133.5 438.0,133.5 411.0,86.8 438.0,40.0 492.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="519.0,180.3 492.0,227.1 438.0,227.1 411.0,180.3 438.0,133.5 492.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">5-01</text>
<polygon points="519.0,273.8 492.0,320.6 438.0,320.6 411.0,273.8 438.0,227.1 492.0,227.1" fill="url(#rough)" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">5-02</text>
<polygon points="519.0,367.4 492.0,414.1 438.0,414.1 411.0,367.4 438.0,320.6 492.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">5-03</text>
<polygon points="519.0,460.9 492.0,507.7 438.0,507.7 411.0,460.9 438.0,414.1 492.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="465.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">5-04</text>
<polygon points="600.0,40.0 573.0,86.8 519.0,86.8 492.0,40.0 519.0,-6.8 573.0,-6.8" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="600.0,133.5 573.0,180.3 519.0,180.3 492.0,133.5 519.0,86.8 573.0,86.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="179.5" font-size="9" fill="#8a7a55" text-anchor="middle">6-01</text>
<polygon points="600.0,227.1 573.0,273.8 519.0,273.8 492.0,227.1 519.0,180.3 573.0,180.3" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="273.1" font-size="9" fill="#8a7a55" text-anchor="middle">6-02</text>
<polygon points="600.0,320.6 573.0,367.4 519.0,367.4 492.0,320.6 519.0,273.8 573.0,273.8" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="366.6" font-size="9" fill="#8a7a55" text-anchor="middle">6-03</text>
<polygon points="600.0,414.1 573.0,460.9 519.0,460.9 492.0,414.1 519.0,367.4 573.0,367.4" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="546.0" y="460.1" font-size="9" fill="#8a7a55" text-anchor="middle">6-04</text>
<polygon points="681.0,86.8 654.0,133.5 600.0,133.5 573.0,86.8 600.0,40.0 654.0,40.0" fill="#9ec9e2" stroke="#8a7a55" stroke-width="1"/>
<polygon points="681.0,180.3 654.0,227.1 600.0,227.1 573.0,180.3 600.0,133.5 654.0,133.5" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="226.3" font-size="9" fill="#8a7a55" text-anchor="middle">7-01</text>
<polygon points="681.0,273.8 654.0,320.6 600.0,320.6 573.0,273.8 600.0,227.1 654.0,227.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="319.8" font-size="9" fill="#8a7a55" text-anchor="middle">7-02</text>
<polygon points="681.0,367.4 654.0,414.1 600.0,414.1 573.0,367.4 600.0,320.6 654.0,320.6" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="413.4" font-size="9" fill="#8a7a55" text-anchor="middle">7-03</text>
<polygon points="681.0,460.9 654.0,507.7 600.0,507.7 573.0,460.9 600.0,414.1 654.0,414.1" fill="#f3e6bf" stroke="#8a7a55" stroke-width="1"/>
<text x="627.0" y="506.9" font-size="9" fill="#8a7a55" text-anchor="middle">7-04</text>
<polyline points="60.0,133.5 141.0,180.3 222.0,133.5 303.0,180.3 384.0,133.5 465.0,180.3 546.0,133.5 627.0,180.3" fill="none" stroke="#333" stroke-width="4"/>
<polyline points="60.0,133.5 141.0,180.3 222.0,133.5 303.0,180.3 384.0,133.5 465.0,180.3 546.0,133.5 627.0,180.3" fill="none" stroke="#f3e6bf" stroke-width="1.5" stroke-dasharray="6 6"/>
<polyline points="384.0,133.5 384.0,227.1 384.0,320.6 465.0,367.4 546.0,320.6" fill="none" stroke="#7a5a2a" stroke-width="2.5" stroke-dasharray="7 5"/>
<line x1="33.0" y1="180.3" x2="87.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="114.0" y1="227.1" x2="168.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="195.0" y1="180.3" x2="168.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="87.0" y1="180.3" x2="114.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="249.0" y1="180.3" x2="195.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="330.0" y1="227.1" x2="276.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="357.0" y1="180.3" x2="330.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="249.0" y1="180.3" x2="276.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="492.0" y1="227.1" x2="438.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="519.0" y1="180.3" x2="492.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="411.0" y1="180.3" x2="438.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="573.0" y1="180.3" x2="519.0" y2="180.3" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="654.0" y1="227.1" x2="600.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<line x1="573.0" y1="180.3" x2="600.0" y2="227.1" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>
<circle cx="546.0" cy="306.6" r="5" fill="#2b6cb0"/><text x="546.0" y="298.6" font-size="10" text-anchor="middle" fill="#2b6cb0">Bir Sofafi</text>
<text x="90.0" y="44.0" font-size="13" fill="#2b5c7a" font-style="italic">Mediterranean</text>
<text x="388.0" y="191.5" font-size="10" fill="#7a3b1e" font-weight="bold" text-anchor="middle">Halfaya Pass</text>
<text x="141.0" y="464.9" font-size="11" fill="#8a7a55" font-style="italic" text-anchor="middle">Libyan plateau</text>
<g opacity="0.45"><rect x="273.0" y="171.3" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="303.0" y="182.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">I/1 Libyan</text>
<text x="303.0" y="192.3" font-size="8" text-anchor="middle" fill="#222">Inf regt · CPA 8 · M−1</text></g>
<g opacity="0.45"><rect x="279.0" y="141.3" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="309.0" y="152.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">II/1 Libyan</text>
<text x="309.0" y="162.3" font-size="8" text-anchor="middle" fill="#222">Inf regt · CPA 8 · M−1</text></g>
<g><rect x="192.0" y="124.5" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="222.0" y="135.5" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">1 Lib Art</text>
<text x="222.0" y="145.5" font-size="8" text-anchor="middle" fill="#222">Arty · Bar 9 · CPA 8</text></g>
<path d="M 60.0,227.1 L 141.0,273.8 L 222.0,227.1 L 303.0,273.8" fill="none" stroke="#b00" stroke-width="3" marker-end="url(#arr-b00)"/>
<text x="100.0" y="193.1" font-size="10" fill="#b00" font-weight="bold" text-anchor="middle">Released: 2 clear + 1 rough = 8 CP</text>
<g><rect x="273.0" y="264.8" width="60" height="26" rx="3" fill="#8fa77a" stroke="#222" stroke-width="1.2"/>
<text x="303.0" y="275.8" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">IX L3</text>
<text x="303.0" y="285.8" font-size="8" text-anchor="middle" fill="#222">Tankette bn · CPA 25</text></g>
<g><rect x="435.0" y="171.3" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="465.0" y="182.3" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">11 Hussars</text>
<text x="465.0" y="192.3" font-size="8" text-anchor="middle" fill="#222">Armd cars · CPA 25 · M+2</text></g>
<g><rect x="354.0" y="218.1" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="384.0" y="229.1" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">1 RNF</text>
<text x="384.0" y="239.1" font-size="8" text-anchor="middle" fill="#222">MG bn · CPA 8 · M+1</text></g>
<g><rect x="435.0" y="264.8" width="60" height="26" rx="3" fill="#d9b46a" stroke="#222" stroke-width="1.2"/>
<text x="465.0" y="275.8" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">4 RHA</text>
<text x="465.0" y="285.8" font-size="8" text-anchor="middle" fill="#222">Arty · Bar 9 · CPA 10</text></g>
<text x="303.0" y="248.3" font-size="10" fill="#b00" text-anchor="middle" font-weight="bold">within 2 hexes: may move again</text>
</svg></div><div class="note">
<p><b>G4. Reserve Release, then Player A chooses: another cycle?</b></p>
<p>Under <b>Continual Movement</b> [<a href="rules/40-movement#spi-8.2">8.2</a>] Italy may repeat Move → Breakdown → Combat as often as it likes. Only units that ended within two hexes of the enemy may move again — the two regiments qualify; the artillery does not [<a href="rules/40-movement#spi-8.23">8.23</a>]. The L3s, released from Reserve, may move regardless.</p>
<p><b>Option A:</b> assault again now with the regiments. Cost another 5 CP each → cohesion −8, a Morale Modification roll at −8 likely costs them another column, and they attack at −4 again with 20 TOE instead of 24. The RNF, no longer Pinned, may now Retreat Before Assault at 2 CP/hex — it has exactly 2.</p>
<p><b>Option B:</b> stop. Release the L3s along the plateau (Clear 2 CP × 2 + Rough 4 = 8 of 25) to threaten the RNF's flank at 3-02 next stage, let the regiments rest a stage to recover 5 cohesion, and barrage the pass again first.</p>
<p>That choice — push exhausted units now for tempo, or accept the delay to keep them coherent — is the game. Then Player B does phases F–L with what it has left.</p></div></div></section>
<h1 id="part-b" class="part">Part B · The combat maths, in full</h1>
<p class="sub">Every combat step uses the same currency and the same dice convention. Once you have those two, the tables are just lookups.</p>
<section class="panel">
<h2>B1 · Two conventions that run all of combat</h2>
<div class="cols">
<div class="calc">
<h3>Raw → Actual [<a href="rules/60-combat#spi-11.3">11.3</a>]</h3>
<p><b>Raw points</b> = Combat Rating × TOE Strength Points used. <b>Actual points</b> = Raw ÷ 10, rounded to nearest (11.4 → 11, 11.5 → 12). Under 5 Raw = 0 Actual [<a href="rules/60-combat#spi-11.33">11.33</a>]. All Raw points from every unit firing at the same target are summed <i>before</i> dividing [<a href="rules/60-combat#spi-11.34">11.34</a>].</p>
<p>Example from the rules [<a href="rules/60-combat#spi-11.35">11.35</a>]: 90th Leichte's artillery, 3 TOE × Barrage 9 = 27 Raw plus 3 TOE × 9 = 27 Raw → 54 Raw → <b>5 Actual Barrage Points</b>.</p>
<p>Consequence: a single battalion's 8 TOE × rating 1 = 8 Raw = <b>1 Actual</b>. Small units round to almost nothing. Concentration is forced on you by arithmetic.</p>
</div>
<div class="calc">
<h3>Two dice, read three ways [<a href="rules/60-combat#spi-15.73">15.73</a>]</h3>
<p>Every roll is two dice of different sizes. The <b>same</b> throw is read:</p>
<ol>
<li><b>Sequentially</b>, big die first: 3 and 4 = "34". Range 11–66. Used for losses on every table.</li>
<li><b>Summed</b>: 3 + 4 = 7. Used for Engaged (attacker) and Retreat (defender) rows on the Close Assault CRT.</li>
<li><b>Summed again</b> against the Captured row: if it hits, one more die on the Prisoners table [<a href="rules/60-combat#spi-15.89">15.89</a>] says what fraction of the losses are prisoners.</li>
</ol>
<p>Each player throws once per assault and gets all their results from it. Barrage and Anti-Armor only use the sequential read.</p>
</div>
</div>
</section>
<section class="panel">
<h2>B2 · Barrage [12]</h2>
<div class="row">
<div class="map"><div class="learn-table" data-table="barrage-results"><h4>Barrage against land units</h4><p class="learn-table-ref"><span class="spi-badge spi-ref">SPI 12.6</span> <code>data/tables/barrage-results.json</code></p><table class="crt"><caption>vs infantry</caption><thead><tr><th>result \ points</th><th>1–2</th><th>3–4</th><th>5–6</th><th>7–8</th><th>9–10</th><th>11–12</th><th>13–14</th><th>15–16</th><th>17+</th></tr></thead><tbody><tr><th>no effect</th><td>11–53</td><td>11–44</td><td>11–41</td><td>11–34</td><td>11–24</td><td>11–16</td><td>—</td><td>—</td><td>—</td></tr><tr><th>pinned</th><td>54–66</td><td>45–66</td><td>42–65</td><td>35–64</td><td>25–61</td><td>21–44</td><td>11–35</td><td>11–32</td><td>11–31</td></tr><tr><th>lose 1</th><td>—</td><td>—</td><td>66</td><td>65–66</td><td>62–66</td><td>45–66</td><td>36–64</td><td>33–56</td><td>32–55</td></tr><tr><th>lose 2</th><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>65–66</td><td>61–66</td><td>56–66</td></tr></tbody></table><table class="crt"><caption>vs armor</caption><thead><tr><th>result \ points</th><th>1–2</th><th>3–4</th><th>5–6</th><th>7–8</th><th>9–10</th><th>11–12</th><th>13–14</th><th>15–16</th><th>17+</th></tr></thead><tbody><tr><th>no effect</th><td>11–62</td><td>11–54</td><td>11–45</td><td>11–36</td><td>11–31</td><td>11–22</td><td>11–14</td><td>—</td><td>—</td></tr><tr><th>pinned</th><td>63–66</td><td>55–66</td><td>46–66</td><td>41–66</td><td>32–66</td><td>23–66</td><td>15–63</td><td>11–62</td><td>11–54</td></tr><tr><th>lose 1</th><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>64–66</td><td>63–66</td><td>55–66</td></tr></tbody></table><table class="crt"><caption>vs gun</caption><thead><tr><th>result \ points</th><th>1–2</th><th>3–4</th><th>5–6</th><th>7–8</th><th>9–10</th><th>11–12</th><th>13–14</th><th>15–16</th><th>17+</th></tr></thead><tbody><tr><th>no effect</th><td>11–61</td><td>11–54</td><td>11–46</td><td>11–36</td><td>11–26</td><td>11–22</td><td>11–12</td><td>—</td><td>—</td></tr><tr><th>lose 1</th><td>62–66</td><td>55–66</td><td>51–66</td><td>41–66</td><td>31–66</td><td>23–64</td><td>13–56</td><td>11–54</td><td>11–36</td></tr><tr><th>lose 2</th><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>65–66</td><td>61–66</td><td>55–66</td><td>41–66</td></tr></tbody></table><table class="crt"><caption>vs truck</caption><thead><tr><th>result \ points</th><th>1–2</th><th>3–4</th><th>5–6</th><th>7–8</th><th>9–10</th><th>11–12</th><th>13–14</th><th>15–16</th><th>17+</th></tr></thead><tbody><tr><th>no effect</th><td>11–66</td><td>11–64</td><td>11–62</td><td>11–56</td><td>11–55</td><td>11–53</td><td>11–46</td><td>11–42</td><td>11–32</td></tr><tr><th>lose 1</th><td>—</td><td>65–66</td><td>63–66</td><td>61–66</td><td>56–63</td><td>54–63</td><td>51–61</td><td>43–61</td><td>33–61</td></tr><tr><th>lose 2</th><td>—</td><td>—</td><td>—</td><td>—</td><td>64–66</td><td>64–66</td><td>62–66</td><td>62–66</td><td>62–66</td></tr></tbody></table></div></div>
<div class="note">
<p><b>Who:</b> anything with a Barrage Rating and ammo, into an <i>adjacent</i> hex. Ranges are abstracted away — that is the big simplification in CNA.</p>
<p><b>Position first.</b> Each gun unit is Forward or Back [<a href="rules/60-combat#spi-12.1">12.1</a>]. Forward guns can coordinate with other Forward guns on one target and can split fire between targets; Back guns fire alone. Forward guns are exposed: their Vulnerability rating decides whether they get captured or destroyed if the hex is overrun. Italian guns have extra restrictions on coordinating.</p>
<p><b>Target by type.</b> You barrage "the infantry in 4-02", not a named unit, unless a patrol has told you what is there [<a href="rules/60-combat#spi-12.24">12.24</a>]. The table has four target classes: Infantry, Armor, Gun, Truck. You roll separately for the trucks in the hex.</p>
<p><b>Reading the table.</b> Column = Actual Barrage Points. Find where your sequential roll falls. Results: <i>No effect</i>; <i>Pinned</i> = may not Retreat Before Assault, may not assault; <i>1</i> / <i>2</i> = lose that many TOE points (and Pinned for infantry/armor).</p>
<p><b>What the numbers say.</b> With 3–4 points vs Infantry you can only Pin (45–66). You need 5–6 points for any chance of a kill (66 only), 13+ for a real one. Killing with artillery is expensive; <b>pinning is the job</b> — it strips the defender's option to retreat and sets up the assault.</p>
<p><b>Cost.</b> Firing costs the unit 5 CP (phasing) and ammo per TOE point fired [50.14] — 4 TOE of German 150mm at ammo rate 4 = 16 Ammo Points for one shoot, regardless of result. Being barraged costs the target 3 CP.</p>
</div>
</div>
</section>
<section class="panel">
<h2>B3 · Anti-Armor fire [14]</h2>
<div class="row">
<div class="map"><div class="learn-table" data-table="anti-armour-results"><h4>Anti-armour fire: damage points</h4><p class="learn-table-ref"><span class="spi-badge spi-ref">SPI 14.6</span> <code>data/tables/anti-armour-results.json</code></p><table class="crt"><thead><tr><th>roll \ points</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th><th>16+</th></tr></thead><tbody><tr><th>11</th><td>—</td><td>—</td><td>—</td><td>1</td><td>2</td><td>3</td><td>4</td><td>6</td><td>8</td><td>10</td><td>11</td><td>12</td><td>14</td><td>16</td><td>18</td><td>20</td><td>22</td></tr><tr><th>13</th><td>—</td><td>—</td><td>—</td><td>1</td><td>3</td><td>4</td><td>5</td><td>6</td><td>8</td><td>10</td><td>11</td><td>13</td><td>15</td><td>17</td><td>19</td><td>20</td><td>22</td></tr><tr><th>15</th><td>—</td><td>—</td><td>1</td><td>1</td><td>3</td><td>4</td><td>5</td><td>7</td><td>9</td><td>10</td><td>12</td><td>13</td><td>15</td><td>17</td><td>19</td><td>21</td><td>23</td></tr><tr><th>21</th><td>—</td><td>—</td><td>1</td><td>2</td><td>4</td><td>5</td><td>6</td><td>8</td><td>9</td><td>11</td><td>12</td><td>14</td><td>16</td><td>18</td><td>20</td><td>21</td><td>23</td></tr><tr><th>23</th><td>—</td><td>—</td><td>1</td><td>2</td><td>4</td><td>5</td><td>6</td><td>8</td><td>10</td><td>11</td><td>13</td><td>14</td><td>16</td><td>18</td><td>20</td><td>22</td><td>24</td></tr><tr><th>25</th><td>—</td><td>—</td><td>2</td><td>3</td><td>4</td><td>6</td><td>7</td><td>9</td><td>10</td><td>12</td><td>13</td><td>15</td><td>17</td><td>19</td><td>20</td><td>22</td><td>24</td></tr><tr><th>31</th><td>—</td><td>1</td><td>2</td><td>3</td><td>5</td><td>6</td><td>8</td><td>9</td><td>11</td><td>12</td><td>14</td><td>15</td><td>17</td><td>19</td><td>21</td><td>23</td><td>25</td></tr><tr><th>33</th><td>—</td><td>1</td><td>2</td><td>3</td><td>5</td><td>7</td><td>8</td><td>10</td><td>11</td><td>13</td><td>14</td><td>16</td><td>18</td><td>20</td><td>21</td><td>23</td><td>25</td></tr><tr><th>35</th><td>—</td><td>1</td><td>3</td><td>4</td><td>5</td><td>7</td><td>9</td><td>10</td><td>12</td><td>13</td><td>15</td><td>16</td><td>18</td><td>20</td><td>22</td><td>24</td><td>26</td></tr><tr><th>41</th><td>—</td><td>2</td><td>3</td><td>4</td><td>6</td><td>7</td><td>9</td><td>11</td><td>12</td><td>14</td><td>15</td><td>17</td><td>19</td><td>21</td><td>22</td><td>24</td><td>26</td></tr><tr><th>43</th><td>—</td><td>2</td><td>3</td><td>5</td><td>6</td><td>8</td><td>10</td><td>11</td><td>13</td><td>14</td><td>16</td><td>17</td><td>19</td><td>21</td><td>23</td><td>25</td><td>27</td></tr><tr><th>45</th><td>—</td><td>2</td><td>4</td><td>5</td><td>7</td><td>8</td><td>10</td><td>12</td><td>13</td><td>15</td><td>16</td><td>18</td><td>20</td><td>22</td><td>23</td><td>25</td><td>27</td></tr><tr><th>51</th><td>1</td><td>3</td><td>4</td><td>6</td><td>7</td><td>9</td><td>11</td><td>12</td><td>14</td><td>15</td><td>17</td><td>19</td><td>20</td><td>22</td><td>24</td><td>26</td><td>28</td></tr><tr><th>53</th><td>1</td><td>3</td><td>4</td><td>6</td><td>8</td><td>9</td><td>11</td><td>13</td><td>14</td><td>16</td><td>17</td><td>20</td><td>21</td><td>23</td><td>25</td><td>27</td><td>29</td></tr><tr><th>55</th><td>1</td><td>3</td><td>5</td><td>7</td><td>8</td><td>10</td><td>12</td><td>13</td><td>15</td><td>16</td><td>19</td><td>21</td><td>22</td><td>24</td><td>26</td><td>28</td><td>30</td></tr><tr><th>61</th><td>1</td><td>4</td><td>5</td><td>7</td><td>8</td><td>10</td><td>12</td><td>14</td><td>15</td><td>17</td><td>19</td><td>22</td><td>23</td><td>25</td><td>27</td><td>29</td><td>31</td></tr><tr><th>63</th><td>1</td><td>4</td><td>6</td><td>8</td><td>9</td><td>11</td><td>13</td><td>14</td><td>16</td><td>18</td><td>21</td><td>22</td><td>24</td><td>26</td><td>28</td><td>29</td><td>32</td></tr><tr><th>65</th><td>2</td><td>4</td><td>6</td><td>8</td><td>9</td><td>11</td><td>13</td><td>15</td><td>17</td><td>19</td><td>21</td><td>23</td><td>24</td><td>26</td><td>28</td><td>30</td><td>32</td></tr></tbody></table></div></div>
<div class="note">
<p><b>Who:</b> anything with an Anti-Armor rating — AT guns, tanks, some infantry — at a hex containing units with an <b>Armor Protection Rating</b>. Both sides fire, simultaneously, before Close Assault.</p>
<p><b>Assignment.</b> Before this step both players secretly split each unit's TOE points between Anti-Armor and Close Assault, or withhold them. A TOE point does one or the other this segment, never both [<a href="rules/60-combat#spi-14.0">14.0</a>]. Withheld armor cannot be hit.</p>
<p><b>Reading the table.</b> Column = Actual Anti-Armor Points; row = sequential roll; cell = <b>Damage Points</b>. The phasing player reads one row <i>higher</i> (the defender is dug in, the attacker is moving) [14.6 note]. Terrain shifts columns left: rough/vegetation/L1 fort −1, mountain/L2–3 fort −2, attacking up a slope −1, up a ridge −2.</p>
<p><b>Absorbing damage [<a href="rules/60-combat#spi-14.4">14.4</a>].</b> The target owner must remove TOE points whose Armor Protection ratings <i>sum to at least</i> the Damage Points. Rules example: 5 Actual points, roll 35 → 7 Damage. Target hex has M11s (protection 2) and M13s (protection 3). Owner removes one M13 (3) + two M11 (4) = 7. Thick armour absorbs more per point lost — Matildas shrug off what would gut a tankette company.</p>
<p><b>Then:</b> a Destroyed Tanks marker goes in the hex. Dead tanks are recoverable — by either side — through the Repair and Tank Delivery rules [<a href="rules/80-engineering#spi-22.4">22.4</a>, <a href="rules/60-combat#spi-14.5">14.5</a>]. In the desert the wrecks were the prize.</p>
</div>
</div>
</section>
<section class="panel">
<h2>B4 · Close Assault [15] — the modifier ladder</h2>
<div class="row">
<div class="map"><div class="learn-table" data-table="close-assault-results"><h4>Close assault: losses by sequential roll, engaged / retreat / captured by sum</h4><p class="learn-table-ref"><span class="spi-badge spi-ref">SPI 15.79</span> <code>data/tables/close-assault-results.json</code></p><table class="crt"><caption>attacker</caption><thead><tr><th>losses \ differential</th><th>−11</th><th>−8</th><th>−6</th><th>−4</th><th>−3</th><th>−2</th><th>−1</th><th>0</th><th>+1</th><th>+2</th><th>+3</th><th>+4</th><th>+5</th><th>+7</th><th>+9</th><th class="overrun">+11</th><th class="overrun">+14</th><th class="overrun">+17</th></tr></thead><tbody><tr><th>50 %</th><td>11–15</td><td>11–12</td><td>11</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><th>40 %</th><td>16–24</td><td>13–16</td><td>12–14</td><td>11</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><th>30 %</th><td>25–33</td><td>21–26</td><td>15–23</td><td>12–15</td><td>11–12</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><th>25 %</th><td>34–36</td><td>31–34</td><td>24–32</td><td>16–23</td><td>13–16</td><td>11–12</td><td>11</td><td>11</td><td>11</td><td>11</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><th>20 %</th><td>41–46</td><td>35–43</td><td>33–41</td><td>24–33</td><td>21–26</td><td>13–18</td><td>12–13</td><td>12</td><td>12</td><td>12</td><td>11–12</td><td>11–12</td><td>11</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><th>15 %</th><td>51–56</td><td>44–53</td><td>42–51</td><td>34–44</td><td>31–36</td><td>21–33</td><td>14–26</td><td>13–24</td><td>13–22</td><td>13–16</td><td>13–16</td><td>13–15</td><td>12–13</td><td>11–12</td><td>11</td><td>—</td><td>—</td><td>—</td></tr><tr><th>10 %</th><td>61–63</td><td>54–62</td><td>52–56</td><td>45–53</td><td>41–46</td><td>34–44</td><td>31–42</td><td>25–36</td><td>23–33</td><td>21–31</td><td>21–26</td><td>16–25</td><td>14–21</td><td>13–21</td><td>12–16</td><td>11–16</td><td>11–13</td><td>11–12</td></tr><tr><th>5 %</th><td>64–66</td><td>63–65</td><td>61–63</td><td>54–61</td><td>51–56</td><td>45–54</td><td>43–52</td><td>41–51</td><td>34–46</td><td>32–44</td><td>31–42</td><td>26–41</td><td>22–35</td><td>22–33</td><td>21–31</td><td>21–26</td><td>14–21</td><td>13–16</td></tr><tr><th>0 %</th><td>—</td><td>66</td><td>64–66</td><td>62–66</td><td>61–66</td><td>55–66</td><td>53–66</td><td>52–66</td><td>51–66</td><td>45–66</td><td>43–66</td><td>42–66</td><td>36–66</td><td>34–66</td><td>32–66</td><td>31–66</td><td>22–66</td><td>21–66</td></tr><tr><th>engaged</th><td>10, 11, 12</td><td>10, 11</td><td>11, 12</td><td>12</td><td>11, 12</td><td>10, 11</td><td>10, 11, 12</td><td>9, 10, 12</td><td>9, 10, 11</td><td>9, 10, 11, 12</td><td>8, 9, 10, 12</td><td>8, 9, 10</td><td>9, 10, 12</td><td>10, 11, 12</td><td>9, 10, 11</td><td>—</td><td>—</td><td>—</td></tr><tr><th>captured</th><td>2, 3, 4, 5, 6, 7</td><td>2, 3, 4, 5, 6</td><td>2, 3, 4, 5</td><td>2, 3, 4</td><td>2, 3</td><td>2</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr></tbody></table><table class="crt"><caption>defender</caption><thead><tr><th>losses \ differential</th><th>−11</th><th>−8</th><th>−6</th><th>−4</th><th>−3</th><th>−2</th><th>−1</th><th>0</th><th>+1</th><th>+2</th><th>+3</th><th>+4</th><th>+5</th><th>+7</th><th>+9</th><th class="overrun">+11</th><th class="overrun">+14</th><th class="overrun">+17</th></tr></thead><tbody><tr><th>50 %</th><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>11–13</td><td>11–16</td></tr><tr><th>40 %</th><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>11</td><td>11–12</td><td>11–13</td><td>14–25</td><td>21–26</td></tr><tr><th>30 %</th><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>11</td><td>12–14</td><td>13–16</td><td>14–22</td><td>26–33</td><td>31–36</td></tr><tr><th>25 %</th><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>11</td><td>11</td><td>11–12</td><td>12–14</td><td>15–22</td><td>21–26</td><td>23–33</td><td>34–43</td><td>41–46</td></tr><tr><th>20 %</th><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>11</td><td>11</td><td>11–12</td><td>11–13</td><td>12–13</td><td>12–14</td><td>13–16</td><td>15–23</td><td>23–31</td><td>31–41</td><td>34–46</td><td>44–55</td><td>51–56</td></tr><tr><th>15 %</th><td>—</td><td>—</td><td>—</td><td>11</td><td>11–13</td><td>12–13</td><td>12–16</td><td>13–23</td><td>14–22</td><td>14–23</td><td>15–25</td><td>21–33</td><td>24–36</td><td>32–45</td><td>42–56</td><td>51–62</td><td>56–63</td><td>61–63</td></tr><tr><th>10 %</th><td>11</td><td>11</td><td>11–13</td><td>12–15</td><td>14–21</td><td>14–23</td><td>21–26</td><td>24–32</td><td>23–33</td><td>24–33</td><td>26–42</td><td>34–45</td><td>41–54</td><td>46–61</td><td>61–63</td><td>63–64</td><td>64</td><td>64–65</td></tr><tr><th>5 %</th><td>12–16</td><td>12–23</td><td>14–26</td><td>16–31</td><td>22–41</td><td>24–44</td><td>31–46</td><td>33–51</td><td>34–51</td><td>41–52</td><td>43–54</td><td>46–56</td><td>55–62</td><td>62–64</td><td>64–65</td><td>65</td><td>65–66</td><td>66</td></tr><tr><th>0 %</th><td>21–66</td><td>24–66</td><td>31–66</td><td>32–66</td><td>42–66</td><td>45–66</td><td>51–66</td><td>52–66</td><td>52–66</td><td>53–66</td><td>55–66</td><td>61–66</td><td>63–66</td><td>65–66</td><td>66</td><td>66</td><td>—</td><td>—</td></tr><tr><th>retreat 1</th><td>—</td><td>—</td><td>—</td><td>—</td><td>10</td><td>9</td><td>8</td><td>5, 6</td><td>4, 5, 6</td><td>5, 6, 7</td><td>4, 5, 6, 7</td><td>3, 4, 5, 6, 7</td><td>7, 8, 9</td><td>7, 8, 9, 12</td><td>4, 5, 6, 7, 12</td><td>3, 4, 6, 7, 8, 9</td><td>2, 5, 6, 7, 9, 11</td><td>2, 3, 4, 5, 6, 7, 8, 9, 11</td></tr><tr><th>retreat 2</th><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>11</td><td>11</td><td>5</td><td>5</td><td>8</td><td>12</td><td>8, 10</td><td>10</td></tr><tr><th>retreat 3</th><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>11</td><td>12</td><td>12</td></tr><tr><th>captured</th><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>2</td><td>2</td><td>2</td><td>2, 3</td><td>2, 3</td><td>2, 3, 4</td><td>2, 3, 4</td><td>2, 3, 4, 5</td><td>2, 3, 4, 5, 6</td><td>2, 3, 4, 5, 6, 7</td><td>2, 3, 4, 5, 6, 7, 8</td></tr></tbody></table></div></div>
<div class="note">
<p>Start with <b>Actual Off − Actual Def = Differential</b>, then walk the ladder. Every step is a <i>column shift</i> on the CRT, not a number change:</p>
<table class="ledger">
<tr><th>Step</th><th>Rule</th><th>Shift</th></tr>
<tr><td>Probe?</td><td>Attacker may declare a 2-CP Probe: same fight, restricted losses, gives information [<a href="rules/60-combat#spi-15.9">15.9</a>]</td><td>—</td></tr>
<tr><td>2:1 Raw</td><td>Either side with ≥ double the other's Raw points [<a href="rules/60-combat#spi-15.51">15.51</a>]</td><td>2 in their favour</td></tr>
<tr><td>Terrain</td><td>Terrain Effects Chart, Close Assault column [<a href="rules/40-movement#spi-8.37">8.37</a>]: Rough L2, Mountain L3, Up Escarpment L3, Wadi L1, Ridge L2, Fortifications up to L6 …</td><td>as listed</td></tr>
<tr><td>Combined Arms</td><td>Tanks need ≥ equal infantry TOE in the same hex; each 1–3 unsupported tank TOE = −1 Actual (max −4) [<a href="rules/60-combat#spi-15.4">15.4</a>]</td><td>changes points, not columns</td></tr>
<tr><td>Morale</td><td>Each side: Basic Morale ± a roll on the Morale Modification Table for its Cohesion [<a href="rules/10-units-and-state#spi-17.2">17.2</a>], clamped ±3. Attacker minus defender = columns [<a href="rules/60-combat#spi-15.6">15.6</a>]</td><td>±1 per point</td></tr>
<tr><td>Size</td><td>Largest organisation on each side [<a href="rules/60-combat#spi-15.53">15.53</a>]: Div vs Bn 4, Bde vs Bn 2, Bn vs Coy 2, Div vs Coy 8</td><td>to the larger</td></tr>
<tr><td>Minefields / engineers</td><td>Enemy minefield: defender L1 [8.37 n.13]; engineers help the attacker</td><td>as listed</td></tr>
<tr><td>Gun alone</td><td>A gun unit with no defensive rating, alone: attacker takes no losses, +3 columns [<a href="rules/60-combat#spi-15.54">15.54</a>]</td><td>+3</td></tr>
</table>
<p>Then each side throws once. <b>Attacker</b> section: losses by sequential read, Engaged by sum, Captured by sum. <b>Defender</b> section: losses, Retreat (1/2/3 hexes, or 10% more instead), Captured. Overrun columns (+11 and up) are where whole units vanish.</p>
<p><b>Losses</b> are a percentage of the TOE points committed, rounded, taken by the owner from any committed unit [<a href="rules/60-combat#spi-15.8">15.8</a>]. A side losing 30%+ in one assault also takes 3 Disorganization Points [<a href="rules/10-units-and-state#spi-6.21">6.21</a>] — a rout feeds on itself.</p>
<p><b>Ammo:</b> both sides pay per TOE point that fought [50.12]. The defender pays to be attacked. Running a defence out of ammunition is a legitimate way to win.</p>
</div>
</div>
</section>
<h1 id="part-c" class="part">Part C · How supply actually flows (Logistics Game, §47–58)</h1>
<p class="sub">Replace §32's abstract Supply Units with this. Four commodities, three truck lines, and every arrow below is bookkeeping a human had to do by hand.</p>
<section class="panel"><h2>C1 · The pipeline</h2><svg viewBox="0 0 1180 215" width="1180" height="215" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="fa" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#5a3d1a"/></marker></defs>
<rect x="10" y="40" width="150" height="160" rx="8" fill="#e8eef7" stroke="#5a3d1a" stroke-width="1.5"/>
<text x="85.0" y="62" font-size="14" font-weight="bold" text-anchor="middle" fill="#222">Italy / Sicily</text>
<text x="85.0" y="82" font-size="11.5" text-anchor="middle" fill="#333">Naval Convoy Stage</text>
<text x="85.0" y="98" font-size="11.5" text-anchor="middle" fill="#333">planned 1 turn ahead [56]</text>
<text x="85.0" y="114" font-size="11.5" text-anchor="middle" fill="#333">Ammo · Fuel · Stores</text>
<text x="85.0" y="130" font-size="11.5" text-anchor="middle" fill="#333">Replacement Points</text>
<text x="85.0" y="146" font-size="11.5" text-anchor="middle" fill="#333">RN + Malta can sink it</text>
<line x1="160" y1="120" x2="213" y2="120" stroke="#5a3d1a" stroke-width="3" marker-end="url(#fa)"/>
<text x="186.5" y="108" font-size="10.5" text-anchor="middle" fill="#7a3b1e" font-weight="bold">sea</text>
<rect x="215" y="40" width="175" height="160" rx="8" fill="#f3e6bf" stroke="#5a3d1a" stroke-width="1.5"/>
<text x="302.5" y="62" font-size="14" font-weight="bold" text-anchor="middle" fill="#222">Port of entry</text>
<text x="302.5" y="82" font-size="11.5" text-anchor="middle" fill="#333">Tripoli 15,000 t/stage</text>
<text x="302.5" y="98" font-size="11.5" text-anchor="middle" fill="#333">Benghazi 2,500 · Tobruk 1,700</text>
<text x="302.5" y="114" font-size="11.5" text-anchor="middle" fill="#333">Bardia 400 · Sollum 250</text>
<text x="302.5" y="130" font-size="11.5" text-anchor="middle" fill="#333">Efficiency Level ÷ bombing</text>
<text x="302.5" y="146" font-size="11.5" text-anchor="middle" fill="#333">1 Fuel Pt = ⅛ t · 1 Ammo Pt = 4 t</text>
<text x="302.5" y="162" font-size="11.5" text-anchor="middle" fill="#333">Stores 1 t · Water ⅙ t [54.5]</text>
<line x1="390" y1="120" x2="443" y2="120" stroke="#5a3d1a" stroke-width="3" marker-end="url(#fa)"/>
<text x="416.5" y="108" font-size="10.5" text-anchor="middle" fill="#7a3b1e" font-weight="bold">3rd-line trucks</text>
<rect x="445" y="40" width="195" height="160" rx="8" fill="#f3e6bf" stroke="#5a3d1a" stroke-width="1.5"/>
<text x="542.5" y="62" font-size="14" font-weight="bold" text-anchor="middle" fill="#222">Forward dump(s)</text>
<text x="542.5" y="82" font-size="11.5" text-anchor="middle" fill="#333">any hex; cities are dumps</text>
<text x="542.5" y="98" font-size="11.5" text-anchor="middle" fill="#333">one OpStage truck ride apart [54.16]</text>
<text x="542.5" y="114" font-size="11.5" text-anchor="middle" fill="#333">capacity by hex type [54.12]</text>
<text x="542.5" y="130" font-size="11.5" text-anchor="middle" fill="#333">evaporation −6 % / turn (CW −9 %)</text>
<text x="542.5" y="146" font-size="11.5" text-anchor="middle" fill="#333">+5 % in hot weather [49.3]</text>
<text x="542.5" y="162" font-size="11.5" text-anchor="middle" fill="#333">can be blown, bombed, captured</text>
<line x1="640" y1="120" x2="693" y2="120" stroke="#5a3d1a" stroke-width="3" marker-end="url(#fa)"/>
<text x="666.5" y="108" font-size="10.5" text-anchor="middle" fill="#7a3b1e" font-weight="bold">2nd-line trucks</text>
<rect x="695" y="40" width="195" height="160" rx="8" fill="#e6efd9" stroke="#5a3d1a" stroke-width="1.5"/>
<text x="792.5" y="62" font-size="14" font-weight="bold" text-anchor="middle" fill="#222">Divisional / 1st-line</text>
<text x="792.5" y="82" font-size="11.5" text-anchor="middle" fill="#333">trucks attached to the unit</text>
<text x="792.5" y="98" font-size="11.5" text-anchor="middle" fill="#333">carry men or supply, not both</text>
<text x="792.5" y="114" font-size="11.5" text-anchor="middle" fill="#333">unit takes truck CPA when riding</text>
<text x="792.5" y="130" font-size="11.5" text-anchor="middle" fill="#333">load / unload = 2 CP</text>
<text x="792.5" y="146" font-size="11.5" text-anchor="middle" fill="#333">(0 in Organization Phase)</text>
<text x="792.5" y="162" font-size="11.5" text-anchor="middle" fill="#333">cannot detach if cohesion ≤ −5</text>
<line x1="890" y1="120" x2="928" y2="120" stroke="#5a3d1a" stroke-width="3" marker-end="url(#fa)"/>
<text x="909.0" y="108" font-size="10.5" text-anchor="middle" fill="#7a3b1e" font-weight="bold">in hex</text>
<rect x="930" y="40" width="240" height="160" rx="8" fill="#fbe3d6" stroke="#5a3d1a" stroke-width="1.5"/>
<text x="1050.0" y="62" font-size="14" font-weight="bold" text-anchor="middle" fill="#222">Consumption per unit</text>
<text x="1050.0" y="82" font-size="11.5" text-anchor="middle" fill="#333">Fuel: rate × ⌈CP moved ÷ 5⌉ per TOE pt [49.13]</text>
<text x="1050.0" y="98" font-size="11.5" text-anchor="middle" fill="#333">Ammo: rate × TOE pts that fired [50.14]</text>
<text x="1050.0" y="114" font-size="11.5" text-anchor="middle" fill="#333">each pt carries one shot's worth</text>
<text x="1050.0" y="130" font-size="11.5" text-anchor="middle" fill="#333">Stores: 4 per TOE pt per turn [51.11]</text>
<text x="1050.0" y="146" font-size="11.5" text-anchor="middle" fill="#333">Water: 1 per bn + 1 per vehicle pt</text>
<text x="1050.0" y="162" font-size="11.5" text-anchor="middle" fill="#333">per stage [52.4]; +1 pasta pt (Italian bns)</text>
<text x="1050.0" y="178" font-size="11.5" text-anchor="middle" fill="#333">Weekly issue; without → DPs, attrition</text>
</svg>
<div class="cols" style="margin-top:14px">
<div class="calc"><h3>The truck itself [53, 54.2]</h3>
<p>1 Truck Point = 10 lorries. <b>Light</b>: carries 50 fuel / 2 ammo / 6 stores / 40 water, convoy CPA 40. <b>Medium</b>: 120 / 4 / 15 / 100, CPA 30. <b>Heavy</b>: 250 / 8 / 30 / 200, CPA 30.</p>
<p>Convoys are restricted to the dedicated truck-movement sub-phase and can never spend beyond their extended CPA (they break down on the spot if forced to). Road hex = ½ CP → about 60 road hexes per stage.</p>
<p>Every truck point burns 1 Fuel Point per 5 CP moved, drinks 1 Water Point per stage, and rolls for Breakdown like any vehicle.</p>
<p>Third-line: port → dump. Second-line: dump → units. First-line: on the unit's own sheet, not a counter. A recommended system, not a rule [53.14].</p></div>
<div class="calc"><h3>Rail and sea (Commonwealth)</h3>
<p>Railway Alexandria → Mersa Matruh: 1,500 t per stage, one commodity at a time, troops or supplies not both; rail hexes count as water pipeline [54.3]. One stage a month it carries only water.</p>
<p>Coastal shipping between African ports limited only by port capacity [5.2 II.B]. The Axis have coastal-ship counters instead, and must run them past the RAF and the Mediterranean Fleet.</p></div>
<div class="calc"><h3>Worked example: one medium truck point, Tripoli → Sollum</h3>
<p>Loaded with 120 Fuel Points. Route: Tripoli → Nofilia is off-map, 2 OpStages [<a href="rules/40-movement#spi-8.89">8.89</a>]; Nofilia → Bardia is 138 road hexes [56.26] = 69 CP = 3 stages at CPA 30. <b>Five stages one way</b> (≈ 1⅔ Game-Turns), ten round trip.</p>
<p>Truck's own fuel: 30 CP per stage ÷ 5 × rate 1 = 6 FP per stage → 30 FP out, 30 FP home. It arrives with 90 of its 120 and needs 30 of those to get back: <b>half the cargo goes to the trip</b> [49.18].</p>
<p>Meanwhile every dump it passed lost 6 % per turn to evaporation, it drank 10 Water Points, and rolled Breakdown ten times (≈ 70 BP of road vs its 2L rating). Ten such trips is one division's fuel for a week of movement.</p></div>
</div>
</section>
<section class="panel">
<h2>C2 · Why it dominates</h2>
<div class="cols">
<div class="calc"><h3>Distance is the enemy</h3><p>Tripoli is the only big Axis port (15,000 t/stage). Tobruk takes 1,700 and starts damaged; Bardia and Sollum are rounding errors. Benghazi is 2,500 but its harbour was blocked historically. Everything for the front either lands at Tripoli and drives ~1,000 km, or comes through Tobruk under the RAF. The Commonwealth mirror image: Alexandria 15,000 t, a railway to Mersa Matruh, then trucks. Whoever is far from their port is starving — which is why the front oscillated between El Agheila and El Alamein for two years, and why the game does too.</p></div>
<div class="calc"><h3>Trucks are the binding constraint</h3><p>Trucks are mobility <i>and</i> supply. The Graziani scenario gives Italy 205 truck points at Tripoli plus 155 "anywhere in Libya", and each division has only 20–50 of its own [60.31, 60.33]. Every truck point hauling fuel is a truck point not motorising infantry. The Logistics Commander's whole job is deciding that split, then keeping the convoys moving every stage so nothing sits idle. The rules say it plainly: "Trucks are the game" [53.0].</p></div>
<div class="calc"><h3>Four commodities, four failure modes</h3><p><b>No fuel:</b> vehicles don't move; fuel must be in the hex, no debt. <b>No ammo:</b> can't fire — and a unit only carries one shot's worth itself. <b>No stores:</b> a Disorganization Point per turn, then 2 %, 4 %, 6 % attrition [51.2]. <b>No water:</b> vehicles can't move or assault; infantry can't exceed CPA, then worse [52.5]; Italian battalions without their pasta point at −10 cohesion disintegrate outright [52.6]. Each is tracked per unit on its TOE sheet. There are 1,800 counters.</p></div>
</div>
</section>
<h1 class="part">Part D · Graziani's Offensive on the real map</h1>
<p class="sub">Part D walks Scenario 1 (§60) across Map C hex by hex. It is published when the map sub-project has redrawn Map C as our own; until then it lives in the local build of this primer only.</p>
<p class="fine">Generated by <code>tools/learn_page.py --site</code> from our own prose, SVGs and CC0 data; no SPI material.</p>
</div>
