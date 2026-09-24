#!/usr/bin/env python3
"""
Builds a high-resolution 3x3 showcase poster of all 9 competition sheets:
[00_GUIA]       [01_CHIBI_BASE]   [02_CHIBI_CUT]
[03_SWORD_BASE] [04_SWORD_CUT]    [05_QPU_BASE]
[06_QPU_CUT]    [07_CHAND_BASE]   [08_CHAND_CUT]
"""
import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PACK_DIR = os.path.join(BASE_DIR, "concurso_listo_para_imprimir")
PREVIEW_DIR = "/tmp/pdf_previews"
os.makedirs(PREVIEW_DIR, exist_ok=True)

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Convert all PDFs to png at 120 DPI
pdf_files = [
    ("00_GUIA_DEL_CONCURSO.pdf", "00_GUIA"),
    ("01_CHIBI_TABLERO_BASE_A4.pdf", "01_CHIBI_BASE"),
    ("02_CHIBI_PIEZAS_RECORTAR_A4.pdf", "02_CHIBI_RECORTAR"),
    ("03_SWORD_TABLERO_BASE_A4.pdf", "03_SWORD_BASE"),
    ("04_SWORD_PIEZAS_RECORTAR_A4.pdf", "04_SWORD_RECORTAR"),
    ("05_QPU_TABLERO_BASE_A4.pdf", "05_QPU_BASE"),
    ("06_QPU_PIEZAS_RECORTAR_A4.pdf", "06_QPU_RECORTAR"),
    ("07_CHANDELIER_TABLERO_BASE_A4.pdf", "07_CHAND_BASE"),
    ("08_CHANDELIER_PIEZAS_RECORTAR_A4.pdf", "08_CHAND_RECORTAR"),
]

imgs = []
for fname, key in pdf_files:
    pdf_path = os.path.join(PACK_DIR, fname)
    out_prefix = os.path.join(PREVIEW_DIR, key)
    subprocess.run(["pdftoppm", "-png", "-r", "120", pdf_path, out_prefix], check=True)
    img_path = f"{out_prefix}-1.png"
    im = Image.open(img_path).convert("RGB")
    imgs.append((fname, im))

# Grid dimensions: 3 columns x 3 rows
cell_w, cell_h = imgs[0][1].size
gap = 28
header_h = 130
margin = 32

total_w = margin * 2 + cell_w * 3 + gap * 2
total_h = margin * 2 + header_h + cell_h * 3 + gap * 2

canvas = Image.new("RGB", (total_w, total_h), color=(15, 23, 42))
draw = ImageDraw.Draw(canvas)

font_title = ImageFont.truetype(FONT_PATH, size=40)
font_sub = ImageFont.truetype(FONT_REG, size=20)
font_label = ImageFont.truetype(FONT_PATH, size=18)

# Banner
draw.text((margin, margin + 10), "HPC&A • PACK OFICIAL LISTO PARA IMPRIMIR (CONCURSO DE LLAVEROS 3D)", fill=(56, 189, 248), font=font_title)
draw.text((margin, margin + 65), "4 Desafíos Completos (Primaria y Secundaria) • Hojas A4 Grandes con Líneas ✂ y Números Protegidos", fill=(203, 213, 225), font=font_sub)

# Draw 3x3 Grid
for idx, (fname, im) in enumerate(imgs):
    r = idx // 3
    c = idx % 3
    x = margin + c * (cell_w + gap)
    y = margin + header_h + r * (cell_h + gap)

    # Shadow
    draw.rectangle([(x + 6, y + 6), (x + cell_w + 6, y + cell_h + 6)], fill=(5, 8, 15))
    # Border
    draw.rectangle([(x - 2, y - 2), (x + cell_w + 1, y + cell_h + 1)], outline=(56, 189, 248), width=2)
    canvas.paste(im, (x, y))

    # Label box
    draw.rectangle([(x, y + cell_h - 36), (x + cell_w, y + cell_h)], fill=(15, 23, 42))
    label_txt = fname.replace(".pdf", "")
    draw.text((x + 12, y + cell_h - 28), label_txt, fill=(255, 255, 255), font=font_label)

out_showcase = os.path.join(PACK_DIR, "competition_pack_showcase.png")
canvas.save(out_showcase)
print(f"Showcase generated: {out_showcase} ({total_w}x{total_h})")
