import csv, json, collections
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPoly

BG = '#0d1117'; FG = '#f0f0ee'; MUTED = '#8b949e'
FIRE = '#ff5a1f'; ACCENT = '#ffb000'

rows = list(csv.DictReader(open('../dados/focos_paragominas_ago2025_ago2026.csv', encoding='utf-8')))
lats = [float(r['Latitude']) for r in rows]
lons = [float(r['Longitude']) for r in rows]

geo = json.load(open('../dados/municipios_para.json', encoding='utf-8'))
alvo = None
for f in geo['features']:
    nome = (f['properties'].get('name') or f['properties'].get('NOME') or '').upper()
    if 'PARAGOMINAS' in nome:
        alvo = f
        break

def anel_para_poly(coords):
    return [(c[0], c[1]) for c in coords]

# ---------- MAPA ----------
fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
ax.set_facecolor(BG)

if alvo:
    g = alvo['geometry']
    partes = g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]
    for parte in partes:
        anel = parte[0][0] if g['type'] == 'MultiPolygon' and isinstance(parte[0][0][0], list) else parte[0]
        ax.add_patch(MplPoly(anel_para_poly(anel), closed=True,
                             facecolor='#161b22', edgecolor=ACCENT, linewidth=2.5, zorder=1))

ax.scatter(lons, lats, s=110, c=FIRE, alpha=0.85, edgecolors='#ffd7c2',
           linewidths=0.6, zorder=3, marker='o')

ax.set_title('304 focos de calor em Paragominas', color=FG, fontsize=30, pad=46, loc='left', fontweight='bold')
ax.text(0.0, 1.012, 'ago/2025 a ago/2026  ·  satélite de referência AQUA_M-T  ·  fonte: INPE / Programa Queimadas',
        transform=ax.transAxes, color=MUTED, fontsize=13, va='bottom')
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig('../docs/mapa-focos-paragominas.png', dpi=180, facecolor=BG, bbox_inches='tight')
plt.close()

# ---------- SAZONALIDADE ----------
m = collections.Counter(r['DataHora'][:7] for r in rows)
ordem = ['2025/08','2025/09','2025/10','2025/11','2025/12','2026/01','2026/02',
         '2026/03','2026/04','2026/05','2026/06','2026/07','2026/08']
rot = ['Ago','Set','Out','Nov','Dez','Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago']
val = [m.get(k, 0) for k in ordem]
cores = [FIRE if k.startswith('2025/') and k[5:] in ('08','09','10','11','12') else '#3d4450' for k in ordem]

fig, ax = plt.subplots(figsize=(16, 8), facecolor=BG)
ax.set_facecolor(BG)
xs = list(range(len(ordem)))
barras = ax.bar(xs, val, color=cores, edgecolor='none', width=0.68)
ax.set_xticks(xs)
ax.set_xticklabels(['Ago\n25','Set','Out','Nov','Dez','Jan\n26','Fev','Mar','Abr','Mai','Jun','Jul','Ago'])
for b, v in zip(barras, val):
    if v:
        ax.text(b.get_x() + b.get_width()/2, v + 1.5, str(v), ha='center',
                color=FG, fontsize=15, fontweight='bold')

ax.set_title('75% dos focos aconteceram no tempo de seca', color=FG, fontsize=30, pad=46, loc='left', fontweight='bold')
ax.text(0.0, 1.012, 'Focos por mês em Paragominas  ·  228 dos 304 entre agosto e dezembro  ·  fonte: INPE',
        transform=ax.transAxes, color=MUTED, fontsize=13, va='bottom')
ax.tick_params(colors=MUTED, labelsize=15, length=0)
for s in ax.spines.values():
    s.set_visible(False)
ax.get_yaxis().set_visible(False)
plt.tight_layout()
plt.savefig('../docs/grafico-sazonalidade.png', dpi=180, facecolor=BG, bbox_inches='tight')
plt.close()
print('ok')
