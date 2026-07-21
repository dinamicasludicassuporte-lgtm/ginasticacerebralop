# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from weeks import WEEKS

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "ginastica-cerebral-prompts-imagens.html")

STYLE_TAG = ("Ilustração vetorial infantil em flat design, traços arredondados e amigáveis, "
             "paleta de cores vivas e aconchegantes (verde-água #2f8f7a, laranja #c1611a, rosa #b23b6b, "
             "azul #2e6fb0 e amarelo-sol #f4b73f), crianças de 3 a 10 anos com tons de pele, cabelo e "
             "vestuário diversos, expressões alegres, tranquilas e acolhedoras (nunca assustadas, "
             "irritadas ou chorando), ambiente interno ou externo simples e aconchegante, iluminação "
             "suave e uniforme, composição limpa com espaço negativo generoso, sem texto, sem letras, "
             "sem números, sem logotipos, sem marca d'água, sem elementos fotorrealistas")

NEGATIVE = ("texto, letras, palavras, números, marca d'água, assinatura, logotipo, fotografia realista, "
            "rostos assustadores, crianças chorando ou com raiva, adultos em primeiro plano, armas, "
            "elementos de terror, proporções corporais distorcidas, mãos deformadas")

IMAGES = [
    {
        "id": "IMG-CAPA",
        "onde": "Capa do guia (página 1) — imagem principal de abertura",
        "dim": "Paisagem larga, aproximadamente 1600×950px (proporção ~16:9)",
        "prompt": (STYLE_TAG + ". Cena única mostrando quatro pequenos grupos de crianças brincando "
                   "ao mesmo tempo em um quintal ensolarado e aconchegante, cada grupo representando uma "
                   "categoria de atividade: no canto superior esquerdo, duas crianças tocando o joelho "
                   "oposto com a mão em um movimento de coordenação; no canto superior direito, uma criança "
                   "empurrando uma grande almofada macia com esforço alegre; no canto inferior esquerdo, uma "
                   "criança sentada em posição de equilíbrio tranquila, mãos no coração, sorrindo; no canto "
                   "inferior direito, uma criança soprando bolhas de sabão grandes e devagar. Composição "
                   "harmoniosa, cores vivas, sensação de alegria e calma ao mesmo tempo."),
    },
]
for w in WEEKS:
    IMAGES.append({
        "id": f"IMG-SEMANA-{w['num']}",
        "onde": f"Divisória da Semana {w['num']} ({w['titulo']}, dias {w['dias'][0]}–{w['dias'][1]}) — banner no topo da página",
        "dim": "Paisagem bem larga, aproximadamente 2000×860px (proporção ~21:9, banner horizontal)",
        "prompt": STYLE_TAG + ". " + w["img_prompt_tema"][0].upper() + w["img_prompt_tema"][1:] + ".",
    })

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

CSS = """
:root{
  --ink:#23324a; --ink-soft:#5c6c85; --paper:#fffdf6; --paper-2:#fbf6e9; --line:#e9e1cb;
  --coral:#ef7a5e; --sun:#f4b73f;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --round:"Arial Rounded MT Bold","Baloo 2","Segoe UI",var(--sans);
  --mono:"SFMono-Regular",Consolas,"Liberation Mono",Menlo,monospace;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{font-family:var(--sans);color:var(--ink);background:#ddd6c2;-webkit-print-color-adjust:exact;print-color-adjust:exact;line-height:1.5}
.page{width:210mm;min-height:297mm;padding:16mm 15mm 14mm;margin:10mm auto;background:var(--paper);position:relative;overflow:hidden;box-shadow:0 6px 30px rgba(35,50,74,.18);display:flex;flex-direction:column}
.page::after{content:attr(data-pg);position:absolute;bottom:6mm;right:15mm;font-size:8.5px;letter-spacing:.16em;color:var(--ink-soft);opacity:.65;font-weight:700}
.brandfoot{position:absolute;bottom:6mm;left:15mm;font-size:8.5px;letter-spacing:.14em;color:var(--ink-soft);opacity:.65;text-transform:uppercase;font-weight:700}
@media print{
  html,body{margin:0;padding:0;background:#fff;width:210mm}
  .page{margin:0;box-shadow:none;width:210mm;min-height:297mm;page-break-after:always;break-after:page}
  .page:last-child{page-break-after:auto;break-after:auto}
}
@page{size:210mm 297mm;margin:0}
h1,h2,h3{font-family:var(--round);margin:0;color:var(--ink)}
.eyebrow{text-transform:uppercase;letter-spacing:.2em;font-size:10px;font-weight:800;color:var(--coral);margin:0 0 8px}
.hr{height:3px;border-radius:3px;margin:4px 0 14px;width:56px;background:linear-gradient(90deg,var(--coral),var(--sun))}
.lead{font-size:12.5px;color:var(--ink-soft);max-width:70ch}
p{margin:0 0 8px}
.note{border-radius:12px;padding:12px 15px;font-size:11px;background:#fdf0d4;border:1px solid #ecd7a4;margin-bottom:6px}
.note strong{color:#8a5a12}
ul.clean{list-style:none;margin:0;padding:0}
ul.clean li{position:relative;padding-left:20px;margin-bottom:7px;font-size:11.5px}
ul.clean li::before{content:"";position:absolute;left:0;top:6px;width:8px;height:8px;border-radius:50%;background:var(--coral)}
.imgcard{border:1.4px solid var(--line);border-radius:16px;padding:16px 18px;margin-bottom:14px;background:#fff}
.imgcard .tophead{display:flex;justify-content:space-between;align-items:center;margin-bottom:4px}
.imgcard .idtag{font-family:var(--mono);font-size:12px;font-weight:800;color:#fff;background:var(--coral);padding:3px 10px;border-radius:8px}
.imgcard .dim{font-size:10px;color:var(--ink-soft)}
.imgcard .onde{font-size:11.5px;color:var(--ink-soft);margin:4px 0 10px}
.imgcard .promptbox{font-family:var(--mono);font-size:10.3px;line-height:1.55;background:var(--paper-2);border:1px dashed #cfc4a0;border-radius:10px;padding:10px 12px;white-space:pre-wrap}
.imgcard .label{font-size:9px;text-transform:uppercase;letter-spacing:.1em;font-weight:800;color:#a99b6f;margin-bottom:4px}
"""

def build():
    entries = "".join(f"""
    <div class="imgcard">
      <div class="tophead"><span class="idtag">{img['id']}</span><span class="dim">{esc(img['dim'])}</span></div>
      <div class="onde"><strong>Onde usar:</strong> {esc(img['onde'])}</div>
      <div class="label">Prompt exato (copiar e colar)</div>
      <div class="promptbox">{esc(img['prompt'])}</div>
    </div>""" for img in IMAGES)

    html = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ginástica Cerebral · Prompts de Imagens</title>
<style>{CSS}</style></head><body>

<section class="page" data-pg="1">
  <div class="eyebrow">Material de apoio à produção</div>
  <h1 style="font-size:26px">Prompts de Imagens — Ginástica Cerebral para Crianças</h1>
  <div class="hr"></div>
  <p class="lead">Este documento reúne o prompt exato para gerar cada uma das {len(IMAGES)} ilustrações usadas como placeholder no guia principal (<em>ginastica-cerebral-30-dias.html</em>). Gere as imagens em qualquer ferramenta de IA de sua preferência (Midjourney, DALL·E, Ideogram, Stable Diffusion etc.) e substitua os placeholders correspondentes pelo ID indicado em cada bloco.</p>

  <div class="note"><strong>Como usar:</strong> copie o texto da caixa "Prompt exato" de cada imagem e cole diretamente na ferramenta de geração escolhida. Ajuste a proporção (aspect ratio) conforme a dimensão recomendada indicada em cada bloco.</div>

  <h3 style="font-size:14px;margin:16px 0 6px">Estilo visual consistente (já incluído em todos os prompts abaixo)</h3>
  <div class="imgcard" style="margin-bottom:10px">
    <div class="label">Descritor de estilo</div>
    <div class="promptbox">{esc(STYLE_TAG)}</div>
  </div>

  <h3 style="font-size:14px;margin:10px 0 6px">Prompt negativo sugerido (se a ferramenta aceitar)</h3>
  <div class="imgcard">
    <div class="label">Negative prompt</div>
    <div class="promptbox">{esc(NEGATIVE)}</div>
  </div>

  <ul class="clean" style="margin-top:14px">
    <li>Gere todas as {len(IMAGES)} imagens na mesma ferramenta e, se possível, na mesma sessão/seed base para manter a coerência visual entre elas.</li>
    <li>Depois de gerar, exporte em PNG ou JPG de alta resolução e substitua a respectiva caixa pontilhada no arquivo HTML do guia (procure pelo comentário/ID correspondente).</li>
    <li>Caso a ferramenta gere texto ou letras acidentalmente na imagem, regenere — os placeholders não devem conter nenhum texto.</li>
  </ul>
  <div class="brandfoot">Ginástica Cerebral · 30 Dias</div>
</section>

<section class="page" data-pg="2">
  <div class="eyebrow">Lista completa</div>
  <h1 style="font-size:22px">{len(IMAGES)} imagens do guia</h1>
  <div class="hr"></div>
  {entries}
  <div class="brandfoot">Ginástica Cerebral · 30 Dias</div>
</section>

</body></html>"""
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote", OUT_PATH)

if __name__ == "__main__":
    build()
