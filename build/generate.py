# -*- coding: utf-8 -*-
import sys, os, importlib
sys.path.insert(0, os.path.dirname(__file__))
from ui_strings import UI

LANG = sys.argv[1] if len(sys.argv) > 1 else "pt"
SUFFIX = "" if LANG == "pt" else f"_{LANG}"
T = UI[LANG]

def mod(name):
    return importlib.import_module(f"{name}{SUFFIX}")

b1 = mod("block1"); b2 = mod("block2"); b3 = mod("block3"); b4 = mod("block4")
wk = mod("weeks")

BLOCK1, BLOCK1_META = b1.BLOCK1, b1.BLOCK1_META
BLOCK2, BLOCK2_META = b2.BLOCK2, b2.BLOCK2_META
BLOCK3, BLOCK3_META = b3.BLOCK3, b3.BLOCK3_META
BLOCK4, BLOCK4_META = b4.BLOCK4, b4.BLOCK4_META
WEEKS, DAY_INTROS = wk.WEEKS, wk.DAY_INTROS

METAS = [BLOCK1_META, BLOCK2_META, BLOCK3_META, BLOCK4_META]
BLOCKS = [BLOCK1, BLOCK2, BLOCK3, BLOCK4]

assert len(BLOCK1) == 30 and len(BLOCK2) == 30 and len(BLOCK3) == 30 and len(BLOCK4) == 30

OUT_NAMES = {
    "pt": "ginastica-cerebral-30-dias.html",
    "en": "brain-gym-kids-30-days.html",
    "es": "gimnasia-cerebral-ninos-30-dias.html",
}
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", OUT_NAMES[LANG])

# ----------------------------------------------------------------------------
CSS = """
:root{
  --ink:#23324a;
  --ink-soft:#5c6c85;
  --paper:#fffdf6;
  --paper-2:#fbf6e9;
  --line:#e9e1cb;
  --sun:#f4b73f;
  --sun-soft:#fdf0d4;
  --b1:#2f8f7a; --b1-soft:#e2f5ef;
  --b2:#c1611a; --b2-soft:#fdead9;
  --b3:#b23b6b; --b3-soft:#fbe4ee;
  --b4:#2e6fb0; --b4-soft:#e3eefb;
  --coral:#ef7a5e;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --round:"Arial Rounded MT Bold","Baloo 2","Segoe UI",var(--sans);
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{
  font-family:var(--sans);
  color:var(--ink);
  background:#ddd6c2;
  -webkit-print-color-adjust:exact; print-color-adjust:exact;
  line-height:1.45;
}
.page{
  width:210mm; min-height:297mm; padding:14mm 14mm 13mm;
  margin:10mm auto; background:var(--paper); position:relative;
  overflow:hidden; box-shadow:0 6px 30px rgba(35,50,74,.18);
  display:flex; flex-direction:column;
}
.page::after{
  content:attr(data-pg); position:absolute; bottom:6mm; right:14mm;
  font-size:8.5px; letter-spacing:.16em; color:var(--ink-soft); opacity:.65; font-weight:700;
}
.brandfoot{
  position:absolute; bottom:6mm; left:14mm; font-size:8.5px; letter-spacing:.14em;
  color:var(--ink-soft); opacity:.65; text-transform:uppercase; font-weight:700;
}
@media print{
  html,body{margin:0;padding:0;background:#fff;width:210mm}
  .page{margin:0;box-shadow:none;width:210mm;height:297mm;min-height:297mm;overflow:hidden;
    page-break-after:always; break-after:page; break-inside:avoid;}
  .page:last-child{page-break-after:auto;break-after:auto}
}
@page{ size:210mm 297mm; margin:0; }

h1,h2,h3,h4{font-family:var(--round);margin:0;color:var(--ink)}
p{margin:0 0 8px}
.eyebrow{font-family:var(--sans);text-transform:uppercase;letter-spacing:.2em;font-size:10px;font-weight:800;color:var(--coral);margin:0 0 8px}
.hr{height:3px;border-radius:3px;margin:4px 0 14px;width:56px;background:linear-gradient(90deg,var(--coral),var(--sun))}
.small{font-size:10.5px;color:var(--ink-soft)}
strong{color:var(--ink)}

.imgph{
  border:2.2px dashed #c9c0a4; border-radius:16px; background:var(--paper-2);
  display:flex; flex-direction:column; align-items:center; justify-content:center;
  text-align:center; color:var(--ink-soft); padding:10px; gap:4px;
}
.imgph .ico{font-size:26px}
.imgph .lbl{font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;font-weight:800;color:#a99b6f}
.imgph .cap{font-size:9px;max-width:70%}

/* ---------------- CAPA ---------------- */
.cover{
  background:linear-gradient(160deg,#2f8f7a 0%,#2e6fb0 55%,#23324a 100%);
  color:#fff; padding:0; justify-content:center; align-items:center; text-align:center;
}
.cover .deco{position:absolute;inset:0}
.cover .blob{position:absolute;border-radius:50%;opacity:.16;background:#fff}
.cover-inner{position:relative;padding:0 34px;max-width:160mm;display:flex;flex-direction:column;align-items:center;gap:14px}
.cover-eyebrow{font-size:12px;letter-spacing:.38em;text-transform:uppercase;color:var(--sun);font-weight:800}
.cover h1{font-size:44px;line-height:1.08;color:#fff;text-shadow:0 2px 14px rgba(0,0,0,.15)}
.cover h1 .accent{color:var(--sun)}
.cover .sub{font-size:14.5px;color:#eef3ff;max-width:120mm;line-height:1.5}
.cover .catrow{display:flex;gap:10px;margin-top:6px;flex-wrap:wrap;justify-content:center}
.cover .catpill{font-size:10px;font-weight:800;padding:5px 12px;border-radius:999px;background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.3)}
.cover .coverimg{width:120mm;height:70mm;margin-top:6px;border-radius:18px;object-fit:cover;
  border:3px solid rgba(255,255,255,.5);box-shadow:0 10px 30px rgba(0,0,0,.25)}
.cover .foot{font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:#cfe0ff;margin-top:10px}

/* ---------------- COMO USAR / listas ---------------- */
.title-blk{margin-bottom:14px}
.title-blk h2{font-size:26px}
.lead{font-size:12.5px;color:var(--ink-soft);max-width:66ch}

.card{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 16px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
ul.clean{list-style:none;margin:0;padding:0}
ul.clean li{position:relative;padding-left:20px;margin-bottom:7px;font-size:11.5px}
ul.clean li::before{content:"";position:absolute;left:0;top:6px;width:8px;height:8px;border-radius:50%;background:var(--coral)}
ol.steps{margin:0;padding-left:18px}
ol.steps li{font-size:11.5px;margin-bottom:5px}

.note{border-radius:12px;padding:10px 13px;font-size:10.8px;background:var(--sun-soft);border:1px solid #ecd7a4}
.note strong{color:#8a5a12}

/* ---------------- CATEGORIAS ---------------- */
.catcard{border-radius:16px;padding:14px 16px;border:1.5px solid; }
.catcard h3{font-size:15px;margin-bottom:4px}
.catcard .icon{font-size:22px}
.catcard p{font-size:11px;color:var(--ink-soft);margin:4px 0 0}

/* ---------------- VISÃO GERAL / TABELA ---------------- */
table.overview{width:100%;border-collapse:collapse;font-size:11px}
table.overview th{text-align:left;font-size:9.5px;text-transform:uppercase;letter-spacing:.06em;color:var(--ink-soft);border-bottom:2px solid var(--line);padding:6px 8px}
table.overview td{padding:7px 8px;border-bottom:1px solid var(--line);vertical-align:top}
table.overview tr:nth-child(even) td{background:#faf7ee}

/* ---------------- DIVISOR DE SEMANA ---------------- */
.weekpage{justify-content:flex-start}
.weeknum{font-family:var(--round);font-size:70px;line-height:1;color:var(--paper-2);-webkit-text-stroke:2px var(--coral);color:transparent}
.weekpage h2{font-size:30px;margin-top:2px}
.weekpage .sub{font-size:13.5px;color:var(--ink-soft);margin-bottom:16px}
.weekpage .msg{font-size:13.5px;line-height:1.6;background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px 20px;max-width:170mm}
.weekbanner{width:100%;height:78mm;margin:18px 0;object-fit:cover;border-radius:16px;box-shadow:0 6px 20px rgba(35,50,74,.15)}
.weekdays{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:20px}
.weekday-chip{border-radius:12px;border:1px solid var(--line);background:#fff;padding:11px 13px;font-size:11px;line-height:1.5}
.weekday-chip b{display:block;font-size:12.5px;color:var(--coral);margin-bottom:4px}

/* ---------------- PÁGINA DE DIA ---------------- */
.daypage{}
.dayhead{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:8px}
.dayhead .dtag{font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--coral);font-weight:800}
.dayhead h2{font-size:22px;margin-top:2px}
.dayintro{font-size:10.8px;color:var(--ink-soft);max-width:150mm;margin-bottom:10px}
.progress{width:100%;height:6px;border-radius:6px;background:var(--line);overflow:hidden;margin-bottom:12px}
.progress > i{display:block;height:100%;background:linear-gradient(90deg,var(--coral),var(--sun))}

.acards{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:10px;flex:1}
.acard{border-radius:14px;padding:12px 14px 10px;border:1.4px solid var(--accent-soft);background:var(--accent-soft);
  display:flex;flex-direction:column;gap:5px;overflow:hidden}
.acard .ahead{display:flex;align-items:center;gap:6px}
.acard .aicon{font-size:16px}
.acard .acat{font-size:9.3px;text-transform:uppercase;letter-spacing:.08em;font-weight:800;color:var(--accent)}
.acard h3{font-size:14.5px;line-height:1.2;color:var(--ink);margin-top:2px}
.acard .ameta{font-size:9.3px;color:var(--ink-soft);display:flex;gap:10px;flex-wrap:wrap;margin:2px 0 3px}
.acard .ameta b{color:var(--ink)}
.acard .adesc{font-size:10.6px;color:var(--ink-soft);margin-bottom:3px;line-height:1.4}
.acard ol{margin:0 0 4px;padding-left:15px}
.acard ol li{font-size:10.2px;margin-bottom:3px;line-height:1.36}
.acard .abox{font-size:9.8px;border-radius:9px;padding:5px 8px;margin-bottom:3px;line-height:1.38;background:rgba(255,255,255,.65)}
.acard .abox b{color:var(--accent)}
.acard .afoot{margin-top:auto;display:flex;justify-content:space-between;align-items:center;font-size:9px;color:var(--ink-soft);padding-top:2px}
.acard .afoot label{display:flex;align-items:center;gap:4px}
.acard .afoot input{width:11px;height:11px}

/* ---------------- FECHAMENTO ---------------- */
.closepage{justify-content:center;align-items:center;text-align:center;
  background:linear-gradient(160deg,#f4b73f 0%,#ef7a5e 60%,#b23b6b 100%);color:#fff;padding:0}
.closepage .inner{max-width:150mm;padding:0 30px}
.closepage h2{color:#fff;font-size:30px}
.closepage p{color:#fff6ea;font-size:12.5px}
"""

# ----------------------------------------------------------------------------
def li(items):
    return "".join(f"<li>{x}</li>" for x in items)

def page_cover():
    cats = "".join(f'<span class="catpill">{m["icone"]} {m["nome_curto"]}</span>' for m in METAS)
    return f"""
<section class="page cover" data-pg="{T['pg_capa']}">
  <div class="deco">
    <div class="blob" style="width:260px;height:260px;top:-60px;left:-70px"></div>
    <div class="blob" style="width:180px;height:180px;bottom:-40px;right:-50px"></div>
    <div class="blob" style="width:120px;height:120px;bottom:120px;left:-40px;opacity:.10"></div>
  </div>
  <div class="cover-inner">
    <div class="cover-eyebrow">{T['cover_eyebrow']}</div>
    <h1>{T['cover_title_1']} <span class="accent">{T['cover_title_2']}</span></h1>
    <div class="sub">{T['cover_sub']}</div>
    <div class="catrow">{cats}</div>
    <img class="coverimg" src="ginastica-cerebral-imagens/img-capa.jpg" alt="{T['cover_img_alt']}">
    <div class="foot">{T['cover_foot']}</div>
  </div>
</section>"""

def page_como_usar():
    return f"""
<section class="page" data-pg="{T['pg_intro']}">
  <div class="eyebrow">{T['cu_eyebrow']}</div>
  <div class="title-blk"><h2>{T['cu_title']}</h2>
  <div class="hr"></div>
  <p class="lead">{T['cu_lead']}</p></div>

  <div class="grid2" style="margin-bottom:12px">
    <div class="card">
      <h3 style="font-size:13.5px;margin-bottom:6px">{T['cu_box1_title']}</h3>
      <ul class="clean">{li(T['cu_box1_items'])}</ul>
    </div>
    <div class="card">
      <h3 style="font-size:13.5px;margin-bottom:6px">{T['cu_box2_title']}</h3>
      <ul class="clean">{li(T['cu_box2_items'])}</ul>
    </div>
  </div>

  <div class="grid2" style="margin-bottom:12px">
    <div class="card">
      <h3 style="font-size:13.5px;margin-bottom:6px">{T['cu_box3_title']}</h3>
      <ul class="clean">{li(T['cu_box3_items'])}</ul>
    </div>
    <div class="card">
      <h3 style="font-size:13.5px;margin-bottom:6px">{T['cu_box4_title']}</h3>
      <ul class="clean">{li(T['cu_box4_items'])}</ul>
    </div>
  </div>

  <div class="note" style="margin-bottom:12px">{T['cu_note']}</div>

  <div class="card">
    <h3 style="font-size:13.5px;margin-bottom:8px">{T['cu_kit_title']}</h3>
    <p class="small" style="margin-bottom:8px">{T['cu_kit_lead']}</p>
    <div class="grid2" style="gap:6px 18px">
      <ul class="clean" style="margin:0">{li(T['cu_kit_col1'])}</ul>
      <ul class="clean" style="margin:0">{li(T['cu_kit_col2'])}</ul>
    </div>
  </div>
</section>"""

def page_categorias():
    cards = ""
    for m in METAS:
        cards += f"""<div class="catcard" style="background:{m['cor_soft']};border-color:{m['cor']}22">
          <span class="icon">{m['icone']}</span>
          <h3 style="color:{m['cor']}">{m['nome']}</h3>
          <p>{m['resumo']}</p>
        </div>"""
    return f"""
<section class="page" data-pg="{T['pg_categorias']}">
  <div class="eyebrow">{T['cat_eyebrow']}</div>
  <div class="title-blk"><h2>{T['cat_title']}</h2><div class="hr"></div>
  <p class="lead">{T['cat_lead']}</p></div>
  <div class="grid2" style="gap:14px">{cards}</div>
  <div class="note" style="margin-top:14px">{T['cat_note']}</div>
</section>"""

def page_visao_geral():
    rows = ""
    for w in WEEKS:
        d0, d1 = w["dias"]
        rows += f"""<tr><td><strong>{T['semana_word']} {w['num']}</strong></td><td>{T['dias_word']} {d0}–{d1}</td><td>{w['titulo']}</td><td>{w['foco']}</td></tr>"""
    th = "".join(f"<th>{x}</th>" for x in T['vg_th'])
    return f"""
<section class="page" data-pg="{T['pg_visao']}">
  <div class="eyebrow">{T['vg_eyebrow']}</div>
  <div class="title-blk"><h2>{T['vg_title']}</h2><div class="hr"></div>
  <p class="lead">{T['vg_lead']}</p></div>
  <table class="overview">
    <thead><tr>{th}</tr></thead>
    <tbody>{rows}</tbody>
  </table>
  <div class="note" style="margin-top:16px">{T['vg_note']}</div>
</section>"""

def page_week_divider(w):
    d0, d1 = w["dias"]
    chips = ""
    for d in range(d0, d1 + 1):
        i = d - 1
        names = [BLOCK1[i]["nome"], BLOCK2[i]["nome"], BLOCK3[i]["nome"], BLOCK4[i]["nome"]]
        chips += f"""<div class="weekday-chip"><b>{T['dia_word']} {d}</b>{" · ".join(names)}</div>"""
    return f"""
<section class="page weekpage" data-pg="{T['semana_word'].lower()} {w['num']}">
  <div class="weeknum">{T['semana_word']} {w['num']}</div>
  <h2>{w['titulo']}</h2>
  <div class="sub">{w['subtitulo']}</div>
  <img class="weekbanner" src="ginastica-cerebral-imagens/img-semana-{w['num']}.jpg" alt="{w['titulo']}">
  <div class="msg">{w['mensagem']}</div>
  <div class="weekdays">{chips}</div>
</section>"""

def render_card(a, meta):
    steps = "".join(f"<li>{s}</li>" for s in a["passos"])
    return f"""<div class="acard" style="--accent:{meta['cor']};--accent-soft:{meta['cor_soft']}">
      <div class="ahead"><span class="aicon">{meta['icone']}</span><span class="acat">{meta['nome_curto']}</span></div>
      <h3>{a['nome']}</h3>
      <div class="ameta"><span><b>{T['card_idade']}</b> {a['idade']}</span><span><b>{T['card_duracao']}</b> {a['duracao']}</span></div>
      <div class="adesc">{a['descricao']}</div>
      <ol>{steps}</ol>
      <div class="abox"><b>{T['card_beneficio']}</b> {a['beneficio']}</div>
      <div class="abox"><b>{T['card_dica']}</b> {a['dica']}</div>
      <div class="afoot"><span>{T['card_materiais']} {a['materiais']}</span><label><input type="checkbox"/> {T['card_feito']}</label></div>
    </div>"""

def page_day(day_num, week):
    i = day_num - 1
    acts = [BLOCK1[i], BLOCK2[i], BLOCK3[i], BLOCK4[i]]
    cards = "".join(render_card(a, m) for a, m in zip(acts, METAS))
    pct = int(day_num / 30 * 100)
    intro = DAY_INTROS[i]
    return f"""
<section class="page daypage" data-pg="{T['dia_word'].lower()} {day_num}/30">
  <div class="dayhead">
    <div><div class="dtag">{T['semana_word']} {week['num']} · {week['titulo']}</div><h2>{T['dia_word']} {day_num} <span style="color:var(--ink-soft);font-size:14px;font-weight:600">{T['de_30']}</span></h2></div>
  </div>
  <div class="dayintro">{intro}</div>
  <div class="progress"><i style="width:{pct}%"></i></div>
  <div class="acards">{cards}</div>
  <div class="brandfoot">{T['brand']}</div>
</section>"""

def page_closing():
    stats = ["30", "120", "4"]
    stat_html = ""
    for num, lbl in zip(stats, T['cl_stat_labels']):
        stat_html += f"""<div style="background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.4);border-radius:14px;padding:14px 22px">
        <div style="font-family:var(--round);font-size:26px">{num}</div><div style="font-size:9.5px;letter-spacing:.1em;text-transform:uppercase">{lbl}</div>
      </div>"""
    return f"""
<section class="page closepage" data-pg="{T['pg_fim']}">
  <div class="inner">
    <div class="cover-eyebrow" style="color:#fff">{T['cl_eyebrow']}</div>
    <h2>{T['cl_title']}</h2>
    <p>{T['cl_p1']}</p>
    <p>{T['cl_p2']}</p>
    <div style="display:flex;gap:14px;justify-content:center;margin-top:26px;flex-wrap:wrap">{stat_html}</div>
    <p style="margin-top:26px;font-size:11px;opacity:.9">{T['cl_final']}</p>
  </div>
</section>"""

# ----------------------------------------------------------------------------
def build():
    parts = [page_cover(), page_como_usar(), page_categorias(), page_visao_geral()]
    for w in WEEKS:
        parts.append(page_week_divider(w))
        d0, d1 = w["dias"]
        for d in range(d0, d1 + 1):
            parts.append(page_day(d, w))
    parts.append(page_closing())

    html = f"""<!doctype html>
<html lang="{T['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{T['doc_title']}</title>
<style>{CSS}</style>
</head>
<body>
{''.join(parts)}
</body>
</html>"""
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote", OUT_PATH, "-", len(parts), "pages")

if __name__ == "__main__":
    build()
