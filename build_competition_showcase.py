#!/usr/bin/env python3
"""
Builds an updated showcase poster of the complete Competition Print Pack:
- Header Banner
- Panel 1: Modo Estándar con Números (Guía + 4 Tableros + 4 Recortables)
- Panel 2: Modo Desafío Experto Sin Números (4 Hojas de Puzle Visual Puro)
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

files_ordered = [
    # Guia
    ("00_GUIA_DEL_CONCURSO.pdf", "00_GUIA", "00. GUÍA OFICIAL"),
    # Con Numeros: Infantil
    ("01_CHIBI_TABLERO_BASE_A4.pdf", "01_CHIBI_B", "01. TABLERO CHIBI"),
    ("02_CHIBI_PIEZAS_RECORTAR_A4.pdf", "02_CHIBI_C", "02. RECORTAR CHIBI (90°)"),
    ("03_GPU_ESPADA_TABLERO_BASE_A4.pdf", "03_SWORD_B", "03. TABLERO GPU ESPADA"),
    ("04_GPU_ESPADA_PIEZAS_RECORTAR_A4.pdf", "04_SWORD_C", "04. RECORTAR GPU ESPADA (90°)"),
    # Con Numeros: Avanzado
    ("05_QPU_TABLERO_BASE_A4.pdf", "05_QPU_B", "05. TABLERO CHIP QPU"),
    ("06_QPU_PIEZAS_RECORTAR_A4.pdf", "06_QPU_C", "06. RECORTAR CHIP QPU (90°)"),
    ("07_CHANDELIER_TABLERO_BASE_A4.pdf", "07_CHAND_B", "07. TABLERO CANDELABRO"),
    ("08_CHANDELIER_PIEZAS_RECORTAR_A4.pdf", "08_CHAND_C", "08. RECORTAR CANDELABRO"),
    # Sin Numeros: Desafio Visual
    ("09_CHIBI_RECORTAR_SIN_NUMEROS_A4.pdf", "09_CHIBI_NN", "09. CHIBI (SIN NÚMEROS)"),
    ("10_GPU_ESPADA_RECORTAR_SIN_NUMEROS_A4.pdf", "10_SWORD_NN", "10. GPU ESPADA (SIN NÚMEROS)"),
    ("11_QPU_RECORTAR_SIN_NUMEROS_A4.pdf", "11_QPU_NN", "11. CHIP QPU (SIN NÚMEROS)"),
    ("12_CHANDELIER_RECORTAR_SIN_NUMEROS_A4.pdf", "12_CHAND_NN", "12. CANDELABRO (SIN NÚMEROS)"),
]

# Convert all PDFs to png at 100 DPI
imgs = []
for fname, key, label in files_ordered:
    pdf_path = os.path.join(PACK_DIR, fname)
    out_prefix = os.path.join(PREVIEW_DIR, key)
    subprocess.run(["pdftoppm", "-png", "-r", "100", pdf_path, out_prefix], check=True)
    img_path = f"{out_prefix}-1.png"
    im = Image.open(img_path).convert("RGB")
    imgs.append((fname, label, im))

# Lay out in 4 columns:
# Row 0: Guía + Chibi Tablero + Chibi Recortar + Chibi Sin Números
# Row 1: Espacio + GPU Espada Tablero + GPU Espada Recortar + GPU Espada Sin Números
# Row 2: Espacio + QPU Tablero + QPU Recortar + QPU Sin Números
# Row 3: Espacio + Chandelier Tablero + Chandelier Recortar + Chandelier Sin Números
# This is a matrix!
cell_w, cell_h = imgs[0][2].size
gap_x = 24
gap_y = 28
header_h = 130
margin = 28

total_w = margin * 2 + cell_w * 4 + gap_x * 3
total_h = margin * 2 + header_h + cell_h * 4 + gap_y * 3

canvas = Image.new("RGB", (total_w, total_h), color=(15, 23, 42))
draw = ImageDraw.Draw(canvas)

font_title = ImageFont.truetype(FONT_PATH, size=36)
font_sub = ImageFont.truetype(FONT_REG, size=18)
font_label = ImageFont.truetype(FONT_PATH, size=16)

# Main Banner
draw.text((margin, margin + 10), "HPC&A • PACK DE IMPRESIÓN COMPLETO (CONCURSO DE LLAVEROS 3D)", fill=(56, 189, 248), font=font_title)
draw.text((margin, margin + 60), "Modo Guiado con Números + Modo Reto Sin Números • Diseños Grandes A4 con Rotación 90° y Líneas ✂", fill=(203, 213, 225), font=font_sub)

# Placement map: (row, col)
# Row 0: Chibi GPU
# Row 1: GPU con Espada
# Row 2: Chip Cuántico QPU
# Row 3: Candelabro Cuántico
# Column 0: Tableros Base (o Guía en Row 0)
# Column 1: Piezas Recortar (Con Números)
# Column 2: Piezas Recortar (Sin Números)
# Column 3: Extras / Tableros

slots_map = [
    # (row, col, img_index)
    (0, 0, 0),   # 00 Guia
    (0, 1, 1),   # 01 Chibi Base
    (0, 2, 2),   # 02 Chibi Recortar
    (0, 3, 9),   # 09 Chibi Sin Numeros

    (1, 1, 3),   # 03 GPU Espada Base
    (1, 2, 4),   # 04 GPU Espada Recortar
    (1, 3, 10),  # 10 GPU Espada Sin Numeros

    (2, 1, 5),   # 05 QPU Base
    (2, 2, 6),   # 06 QPU Recortar
    (2, 3, 11),  # 11 QPU Sin Numeros

    (3, 1, 7),   # 07 Chandelier Base
    (3, 2, 8),   # 08 Chandelier Recortar
    (3, 3, 12),  # 12 Chandelier Sin Numeros
]

# Draw column headers
col_names = ["GUÍA ORGANIZADOR", "1. TABLERO BASE A4", "2. RECORTAR (CON NÚMEROS)", "3. RECORTAR (SIN NÚMEROS)"]
for c_idx, c_title in enumerate(col_names):
    cx = margin + c_idx * (cell_w + gap_x)
    draw.text((cx + 10, margin + 98), c_title, fill=(245, 158, 11), font=font_label)

for r, c, idx in slots_map:
    fname, label, im = imgs[idx]
    x = margin + c * (cell_w + gap_x)
    y = margin + header_h + r * (cell_h + gap_y)

    # Shadow
    draw.rectangle([(x + 4, y + 4), (x + cell_w + 4, y + cell_h + 4)], fill=(5, 8, 15))
    # Border
    draw.rectangle([(x - 2, y - 2), (x + cell_w + 1, y + cell_h + 1)], outline=(56, 189, 248), width=2)
    canvas.paste(im, (x, y))

    # Label box
    draw.rectangle([(x, y + cell_h - 32), (x + cell_w, y + cell_h)], fill=(15, 23, 42))
    draw.text((x + 10, y + cell_h - 25), label, fill=(255, 255, 255), font=font_label)

out_showcase = os.path.join(PACK_DIR, "competition_pack_showcase.png")
canvas.save(out_showcase)
print(f"Showcase generated: {out_showcase} ({total_w}x{total_h})")
