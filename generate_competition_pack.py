#!/usr/bin/env python3
"""
GENERATE MINIMAL COMPETITION PRINT PACK (CONCURSO LISTO PARA IMPRIMIR)
======================================================================
Generates the minimal, essential A4 PDF sheets required to run the competition:
- Full-page LARGE illustrations easy to cut along dashed lines
- Minimal text, maximum cutting clarity
- Middle cut line: Top row numbers at TOP, Bottom row numbers at BOTTOM (پایین شکل)
1. 00_GUIA_DEL_CONCURSO.pdf           - 1-Page Organizer & Instructor Quick-Guide
2. 01_CHIBI_TABLERO_BASE_A4.pdf       - 1-Page Matching Base Board (6 Blocks)
3. 02_CHIBI_PIEZAS_RECORTAR_A4.pdf    - 1-Page LARGE Cut-out Sheet (6 Blocks - Tijeras ✂️)
4. 03_QPU_TABLERO_BASE_A4.pdf         - 1-Page Matching Base Board (12 Blocks)
5. 04_QPU_PIEZAS_RECORTAR_A4.pdf      - 1-Page LARGE Cut-out Sheet (12 Blocks - Tijeras ✂️)
"""

import os
import sys

import reportlab
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
KIDS_DIR = os.path.join(BASE_DIR, "kids_reward_challenge")
QPU_DIR = os.path.join(KIDS_DIR, "qpu_advanced_12blocks")
PACK_DIR = os.path.join(BASE_DIR, "concurso_listo_para_imprimir")
os.makedirs(PACK_DIR, exist_ok=True)

DEJAVU_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
DEJAVU_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

pdfmetrics.registerFont(TTFont("DejaVu", DEJAVU_REG))
pdfmetrics.registerFont(TTFont("DejaVuBold", DEJAVU_BOLD))

MM = 72.0 / 25.4
PAGE_W, PAGE_H = A4  # 595.27 x 841.89 pt (210 x 297 mm)

# Large Grid Image Assets (Full illustration with dashed lines and big numbers)
CHIBI_GRID_IMG = os.path.join(KIDS_DIR, "chibi_gpu_2d_6blocks_grid.png")
QPU_GRID_IMG = os.path.join(QPU_DIR, "qpu_2d_12blocks_grid.png")

CHIBI_SLOTS = [
    {"num": 1, "title": "Anilla de Viaje", "color": colors.HexColor("#0284c7")},
    {"num": 2, "title": "Cerebro HPC&A", "color": colors.HexColor("#db2777")},
    {"num": 3, "title": "Radiador Superior", "color": colors.HexColor("#0d9488")},
    {"num": 4, "title": "Bota PCIe Izquierda", "color": colors.HexColor("#4f46e5")},
    {"num": 5, "title": "Sonrisa Kawaii", "color": colors.HexColor("#ea580c")},
    {"num": 6, "title": "Escape Turbo", "color": colors.HexColor("#16a34a")},
]

QPU_SLOTS = [
    {"num": 1, "title": "Wirebond NW", "color": colors.HexColor("#0284c7")},
    {"num": 2, "title": "Placa HPC&A", "color": colors.HexColor("#b45309")},
    {"num": 3, "title": "QUANTUM", "color": colors.HexColor("#0d9488")},
    {"num": 4, "title": "Almohadillas NE", "color": colors.HexColor("#4f46e5")},
    {"num": 5, "title": "Cúbit Q0", "color": colors.HexColor("#06b6d4")},
    {"num": 6, "title": "Resonador R0", "color": colors.HexColor("#2563eb")},
    {"num": 7, "title": "Cúbit Central Q1", "color": colors.HexColor("#7c3aed")},
    {"num": 8, "title": "Acoplamiento E", "color": colors.HexColor("#9333ea")},
    {"num": 9, "title": "Retorno Q2", "color": colors.HexColor("#ea580c")},
    {"num": 10, "title": "Resonador R2", "color": colors.HexColor("#16a34a")},
    {"num": 11, "title": "Flux Z & S1", "color": colors.HexColor("#059669")},
    {"num": 12, "title": "Almohadillas SE", "color": colors.HexColor("#d97706")},
]


# ==============================================================================
# 0. GUÍA RÁPIDA DEL CONCURSO
# ==============================================================================

def generate_guide_pdf(output_path: str):
    """Generates the 1-page quick guide for competition operators."""
    c = canvas.Canvas(output_path, pagesize=A4)

    # Top Banner
    c.setFillColor(colors.HexColor("#0f172a"))
    c.rect(0, PAGE_H - 42 * MM, PAGE_W, 42 * MM, fill=True, stroke=False)
    c.setFillColor(colors.HexColor("#db2777"))
    c.rect(0, PAGE_H - 44 * MM, PAGE_W, 2 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(20 * MM, PAGE_H - 14 * MM, "HPC&A RESEARCH GROUP • GUÍA OFICIAL DEL CONCURSO")

    c.setFont("DejaVuBold", 17)
    c.setFillColor(colors.white)
    c.drawString(20 * MM, PAGE_H - 24 * MM, "GUÍA DE IMPRESIÓN Y DINAMIZACIÓN DEL CONCURSO")

    c.setFont("DejaVu", 9)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawString(20 * MM, PAGE_H - 32 * MM, "Instrucciones paso a paso para entregar los llaveros 3D mediante el reto de 6 y 12 bloques")

    y = PAGE_H - 52 * MM

    def section_box(title, items, h_mm, accent_hex):
        nonlocal y
        c.setFillColor(colors.HexColor("#f8fafc"))
        c.setStrokeColor(colors.HexColor(accent_hex))
        c.setLineWidth(1.5)
        c.roundRect(20 * MM, y - h_mm * MM, PAGE_W - 40 * MM, h_mm * MM, 3 * MM, fill=True, stroke=True)

        c.setFillColor(colors.HexColor(accent_hex))
        c.roundRect(24 * MM, y - 6 * MM, 85 * MM, 5.5 * MM, 1.5 * MM, fill=True, stroke=False)
        c.setFont("DejaVuBold", 7.5)
        c.setFillColor(colors.white)
        c.drawCentredString(24 * MM + 42.5 * MM, y - 2.5 * MM, title)

        c.setFont("DejaVu", 7.5)
        c.setFillColor(colors.HexColor("#1e293b"))
        item_y = y - 11 * MM
        for bullet, text in items:
            c.setFont("DejaVuBold", 7.5)
            c.drawString(26 * MM, item_y, bullet)
            c.setFont("DejaVu", 7.5)
            c.drawString(48 * MM, item_y, text)
            item_y -= 4.8 * MM

        y -= (h_mm + 5) * MM

    section_box(
        "1. MATERIALES MÍNIMOS NECESARIOS",
        [
            ("Impresión:", "Papel A4 estándar (210 x 297 mm), preferiblemente a color."),
            ("Tijeras:", "Tijeras escolares de punta redonda (1 por participante o mesa)."),
            ("Pegamento:", "Barras de pegamento en barra (stick de pegamento)."),
            ("Premios 3D:", "Llaveros reales impresos en PLA (Chibi GPU y Chip QPU)."),
            ("Acreditación:", "Bolígrafo o sello oficial para firmar el certificado de entrega."),
        ],
        36,
        "#0284c7"
    )

    section_box(
        "2. NIVEL INFANTIL (PRIMARIA) — GPU CHIBI EN 6 BLOQUES",
        [
            ("Público:", "Niños/as de 6 a 11 años. Reto visual y de motricidad."),
            ("Hoja 1:", "01_CHIBI_TABLERO_BASE_A4.pdf (1 copia por participante)."),
            ("Hoja 2:", "02_CHIBI_PIEZAS_RECORTAR_A4.pdf (1 copia por participante para recortar)."),
            ("Corte fácil:", "Corta primero por la línea central horizontal ✂ y luego las dos verticales."),
            ("Recompensa:", "Al pegar los 6 bloques, canjea el Llavero 3D de la GPU Chibi."),
        ],
        36,
        "#db2777"
    )

    section_box(
        "3. NIVEL AVANZADO (SECUNDARIA) — CHIP QPU EN 12 BLOQUES",
        [
            ("Público:", "Estudiantes de 12 a 18+ años. Reto de hardware cuántico real."),
            ("Hoja 1:", "03_QPU_TABLERO_BASE_A4.pdf (1 copia por estudiante)."),
            ("Hoja 2:", "04_QPU_PIEZAS_RECORTAR_A4.pdf (1 copia para recortar las 12 piezas técnicas)."),
            ("Corte fácil:", "Corta las 2 líneas horizontales y las 3 verticales siguiendo los puntos ✂."),
            ("Recompensa:", "Al ensamblar los 12 bloques técnicos, recibe el Llavero 3D del Chip QPU."),
        ],
        36,
        "#d97706"
    )

    section_box(
        "4. PROTOCOLO DE VALIDACIÓN Y ENTREGA",
        [
            ("Paso 1:", "El participante muestra su Tablero completado con todos los bloques pegados."),
            ("Paso 2:", "El instructor comprueba que los números (#1 al #6 o #1 al #12) coincidan."),
            ("Paso 3:", "El instructor marca la casilla [✓] Verificado y firma en el recuadro inferior."),
            ("Paso 4:", "¡Se hace entrega del Llavero 3D original fabricado en el laboratorio HPC&A!"),
        ],
        32,
        "#16a34a"
    )

    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawCentredString(PAGE_W / 2.0, 10 * MM, "Diseñado por Nima • HPC&A Research Group • High Performance Computing & Architecture")

    c.showPage()
    c.save()
    print(f"Generated Guide: {output_path}")


# ==============================================================================
# 2. CHIBI GPU: HOJA GRANDE A4 PARA RECORTAR (MINIMAL TEXT, BIG CUT LINES)
# ==============================================================================

def generate_chibi_cutouts_large_pdf(output_path: str):
    """
    Generates a LARGE A4 sheet with the complete 6-block Chibi GPU illustration.
    - Large cutting image across the page
    - Middle horizontal cut line clearly marked with scissors
    - Top row (1, 2, 3) numbers at TOP
    - Bottom row (4, 5, 6) numbers at BOTTOM (پایین شکل)
    - Minimal text
    """
    c = canvas.Canvas(output_path, pagesize=A4)

    # Minimal Top Bar
    c.setFillColor(colors.HexColor("#0f172a"))
    c.rect(0, PAGE_H - 24 * MM, PAGE_W, 24 * MM, fill=True, stroke=False)
    c.setFillColor(colors.HexColor("#db2777"))
    c.rect(0, PAGE_H - 25.5 * MM, PAGE_W, 1.5 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 13)
    c.setFillColor(colors.white)
    c.drawCentredString(PAGE_W / 2.0, PAGE_H - 14 * MM, "HPC&A • RECORTA POR LAS LÍNEAS DE PUNTOS ✂")

    c.setFont("DejaVu", 8)
    c.setFillColor(colors.HexColor("#f472b6"))
    c.drawCentredString(PAGE_W / 2.0, PAGE_H - 20 * MM, "Corta primero por la línea del medio y luego separa los 6 bloques")

    # LARGE Image in center of A4 page:
    # Width: 180 mm, Height: 112.5 mm
    img_w = 180 * MM
    img_h = 112.5 * MM
    img_x = (PAGE_W - img_w) / 2.0
    img_y = (PAGE_H - img_h) / 2.0 - 5 * MM

    # White card frame with cutting border
    c.setStrokeColor(colors.HexColor("#db2777"))
    c.setLineWidth(2.0)
    c.roundRect(img_x - 3 * MM, img_y - 3 * MM, img_w + 6 * MM, img_h + 6 * MM, 4 * MM, fill=False, stroke=True)

    if os.path.exists(CHIBI_GRID_IMG):
        c.drawImage(CHIBI_GRID_IMG, img_x, img_y, width=img_w, height=img_h, preserveAspectRatio=True)

    # Outer Cutting Guidelines (Border scissors)
    c.setFont("DejaVuBold", 8)
    c.setFillColor(colors.HexColor("#db2777"))
    c.drawString(img_x, img_y + img_h + 4 * MM, "✂ Recortar contorno exterior")
    c.drawRightString(img_x + img_w, img_y + img_h + 4 * MM, "6 BLOQUES TOTALES ✂")

    # Minimal Bottom Footer
    bot_y = 14 * MM
    c.setFillColor(colors.HexColor("#0f172a"))
    c.roundRect(img_x, bot_y, img_w, 18 * MM, 3 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 9)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawCentredString(PAGE_W / 2.0, bot_y + 10.5 * MM, "¡PEGA LAS 6 PIEZAS EN EL TABLERO BASE PARA GANAR TU LLAVERO 3D REAL!")

    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawCentredString(PAGE_W / 2.0, bot_y + 4.5 * MM, "Los bloques 1, 2 y 3 van arriba • Los bloques 4, 5 y 6 van abajo")

    c.showPage()
    c.save()
    print(f"Generated Large Chibi Cut-out: {output_path}")


# ==============================================================================
# 1. CHIBI GPU: TABLERO BASE A4 CORRESPONDIENTE (MATCHING BASE BOARD)
# ==============================================================================

def generate_chibi_board_matching_pdf(output_path: str):
    """
    Generates a 1-page A4 base board matching the exact 1:1 size of the cutting image:
    - Slots 1, 2, 3: numbers at TOP
    - Slots 4, 5, 6: numbers at BOTTOM (پایین شکل)
    - Minimal text, maximum pasting area
    """
    c = canvas.Canvas(output_path, pagesize=A4)

    # Minimal Top Bar
    c.setFillColor(colors.HexColor("#0f172a"))
    c.rect(0, PAGE_H - 32 * MM, PAGE_W, 32 * MM, fill=True, stroke=False)
    c.setFillColor(colors.HexColor("#db2777"))
    c.rect(0, PAGE_H - 33.5 * MM, PAGE_W, 1.5 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 14)
    c.setFillColor(colors.white)
    c.drawString(15 * MM, PAGE_H - 14 * MM, "TABLERO DE DESAFÍO: GPU CHIBI (6 BLOQUES)")

    c.setFont("DejaVu", 8)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawString(15 * MM, PAGE_H - 20 * MM, "Pega cada pieza recortada sobre su casilla correspondiente")

    # Name Line in header
    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(15 * MM, PAGE_H - 28 * MM, "Nombre: __________________________________   Fecha: ____________   Mesa: ______")

    # 6 Target Slots: Exact 180 x 112.5 mm grid centered
    grid_w = 180 * MM
    grid_h = 112.5 * MM
    grid_x = (PAGE_W - grid_w) / 2.0
    grid_y = (PAGE_H - grid_h) / 2.0 - 5 * MM

    col_w = grid_w / 3.0   # 60 mm
    row_h = grid_h / 2.0   # 56.25 mm

    # Outer Frame
    c.setStrokeColor(colors.HexColor("#db2777"))
    c.setLineWidth(2.0)
    c.roundRect(grid_x - 1.5 * MM, grid_y - 1.5 * MM, grid_w + 3 * MM, grid_h + 3 * MM, 3 * MM, fill=False, stroke=True)

    idx = 0
    for r in range(2):
        for col in range(3):
            data = CHIBI_SLOTS[idx]
            bx = grid_x + col * col_w
            by = grid_y + (1 - r) * row_h

            # Slot Box
            c.setFillColor(colors.HexColor("#f8fafc"))
            c.setStrokeColor(colors.HexColor("#cbd5e1"))
            c.setLineWidth(1.0)
            c.rect(bx, by, col_w, row_h, fill=True, stroke=True)

            # Central Big Watermark Number
            c.setFont("DejaVuBold", 42)
            c.setFillColor(colors.HexColor("#e2e8f0"))
            c.drawCentredString(bx + col_w / 2.0, by + row_h / 2.0 - 6 * MM, str(data["num"]))

            # Badge pill: TOP ROW -> at TOP; BOTTOM ROW -> at BOTTOM (پایین شکل!)
            if r == 0:
                # Top row: badge at TOP
                pill_y = by + row_h - 9 * MM
                c.setFillColor(data["color"])
                c.roundRect(bx + 4 * MM, pill_y, col_w - 8 * MM, 6.5 * MM, 2 * MM, fill=True, stroke=False)
                c.setFont("DejaVuBold", 8)
                c.setFillColor(colors.white)
                c.drawCentredString(bx + col_w / 2.0, pill_y + 1.8 * MM, f"BLOQUE #{data['num']}")

                c.setFont("DejaVu", 6.5)
                c.setFillColor(colors.HexColor("#64748b"))
                c.drawCentredString(bx + col_w / 2.0, by + 5 * MM, data["title"])
            else:
                # Bottom row: badge at BOTTOM (پایین شکل!)
                pill_y = by + 3 * MM
                c.setFillColor(data["color"])
                c.roundRect(bx + 4 * MM, pill_y, col_w - 8 * MM, 6.5 * MM, 2 * MM, fill=True, stroke=False)
                c.setFont("DejaVuBold", 8)
                c.setFillColor(colors.white)
                c.drawCentredString(bx + col_w / 2.0, pill_y + 1.8 * MM, f"BLOQUE #{data['num']}")

                c.setFont("DejaVu", 6.5)
                c.setFillColor(colors.HexColor("#64748b"))
                c.drawCentredString(bx + col_w / 2.0, by + row_h - 7 * MM, data["title"])

            idx += 1

    # Minimal Bottom Certification Footer
    bot_y = 14 * MM
    bot_h = 28 * MM
    c.setFillColor(colors.HexColor("#0f172a"))
    c.roundRect(grid_x, bot_y, grid_w, bot_h, 3 * MM, fill=True, stroke=False)

    c.setStrokeColor(colors.HexColor("#db2777"))
    c.setLineWidth(1.2)
    c.roundRect(grid_x + 1.5 * MM, bot_y + 1.5 * MM, grid_w - 3 * MM, bot_h - 3 * MM, 2 * MM, fill=False, stroke=True)

    c.setFont("DejaVuBold", 9.5)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(grid_x + 6 * MM, bot_y + bot_h - 8.5 * MM, "CERTIFICADO DE CANJE: 1 LLAVERO 3D DE LA GPU CHIBI")

    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawString(grid_x + 6 * MM, bot_y + bot_h - 15 * MM, "El participante ha completado los 6 bloques de la arquitectura correctamente.")

    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#f472b6"))
    c.drawString(grid_x + 6 * MM, bot_y + 4.5 * MM, "[ ✓ ] 6 Bloques Verificados")

    c.setFillColor(colors.white)
    c.drawString(grid_x + 65 * MM, bot_y + 4.5 * MM, "Firma del Monitor/a: ___________________________")

    c.setFillColor(colors.HexColor("#f59e0b"))
    c.drawString(grid_x + grid_w - 45 * MM, bot_y + 4.5 * MM, "[ CANJEADO ★ ]")

    c.showPage()
    c.save()
    print(f"Generated Matching Chibi Board: {output_path}")


# ==============================================================================
# 4. QPU CHIP: HOJA GRANDE A4 PARA RECORTAR (MINIMAL TEXT, BIG CUT LINES)
# ==============================================================================

def generate_qpu_cutouts_large_pdf(output_path: str):
    """
    Generates a LARGE A4 sheet with the complete 12-block QPU Chip illustration.
    - Large cutting image across the page
    - Row 0 (top): numbers at top
    - Row 1 (middle): numbers in center
    - Row 2 (bottom): numbers at bottom (پایین شکل)
    - Minimal text
    """
    c = canvas.Canvas(output_path, pagesize=A4)

    # Minimal Top Bar
    c.setFillColor(colors.HexColor("#090d16"))
    c.rect(0, PAGE_H - 24 * MM, PAGE_W, 24 * MM, fill=True, stroke=False)
    c.setFillColor(colors.HexColor("#f59e0b"))
    c.rect(0, PAGE_H - 25.5 * MM, PAGE_W, 1.5 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 13)
    c.setFillColor(colors.white)
    c.drawCentredString(PAGE_W / 2.0, PAGE_H - 14 * MM, "HPC&A QUANTUM LAB • RECORTA LAS 12 PIEZAS TÉCNICAS ✂")

    c.setFont("DejaVu", 8)
    c.setFillColor(colors.HexColor("#f59e0b"))
    c.drawCentredString(PAGE_W / 2.0, PAGE_H - 20 * MM, "Corta siguiendo las líneas de puntos y ensambla la arquitectura cuántica")

    # LARGE Image in center
    # Width: 180 mm, Height: 114.3 mm
    img_w = 180 * MM
    img_h = 114.3 * MM
    img_x = (PAGE_W - img_w) / 2.0
    img_y = (PAGE_H - img_h) / 2.0 - 5 * MM

    c.setStrokeColor(colors.HexColor("#f59e0b"))
    c.setLineWidth(2.0)
    c.roundRect(img_x - 3 * MM, img_y - 3 * MM, img_w + 6 * MM, img_h + 6 * MM, 4 * MM, fill=False, stroke=True)

    if os.path.exists(QPU_GRID_IMG):
        c.drawImage(QPU_GRID_IMG, img_x, img_y, width=img_w, height=img_h, preserveAspectRatio=True)

    # Cut guide lines
    c.setFont("DejaVuBold", 8)
    c.setFillColor(colors.HexColor("#f59e0b"))
    c.drawString(img_x, img_y + img_h + 4 * MM, "✂ Recortar contorno exterior")
    c.drawRightString(img_x + img_w, img_y + img_h + 4 * MM, "12 BLOQUES CUÁNTICOS ✂")

    # Minimal Bottom Footer
    bot_y = 14 * MM
    c.setFillColor(colors.HexColor("#090d16"))
    c.roundRect(img_x, bot_y, img_w, 18 * MM, 3 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 9)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawCentredString(PAGE_W / 2.0, bot_y + 10.5 * MM, "¡ENSAMBLA LOS 12 BLOQUES EN EL TABLERO Y CANJEA TU LLAVERO 3D REAL!")

    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawCentredString(PAGE_W / 2.0, bot_y + 4.5 * MM, "Bloques 1 al 4 (Arriba) • Bloques 5 al 8 (Centro) • Bloques 9 al 12 (Abajo)")

    c.showPage()
    c.save()
    print(f"Generated Large QPU Cut-out: {output_path}")


# ==============================================================================
# 3. QPU CHIP: TABLERO BASE A4 CORRESPONDIENTE (MATCHING BASE BOARD)
# ==============================================================================

def generate_qpu_board_matching_pdf(output_path: str):
    """
    Generates a 1-page A4 base board matching the exact 1:1 size of the cutting image:
    - 12 slots (4 cols x 3 rows)
    - Row 0: numbers at top
    - Row 1: numbers in center
    - Row 2: numbers at bottom (پایین شکل)
    - Minimal text, maximum pasting area
    """
    c = canvas.Canvas(output_path, pagesize=A4)

    # Minimal Top Bar
    c.setFillColor(colors.HexColor("#090d16"))
    c.rect(0, PAGE_H - 32 * MM, PAGE_W, 32 * MM, fill=True, stroke=False)
    c.setFillColor(colors.HexColor("#f59e0b"))
    c.rect(0, PAGE_H - 33.5 * MM, PAGE_W, 1.5 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 14)
    c.setFillColor(colors.white)
    c.drawString(15 * MM, PAGE_H - 14 * MM, "TABLERO DE ENSAMBLAJE: CHIP CUÁNTICO (12 BLOQUES)")

    c.setFont("DejaVu", 8)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawString(15 * MM, PAGE_H - 20 * MM, "Pega cada bloque técnico sobre su casilla para reconstruir el procesador")

    # Name Line
    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(15 * MM, PAGE_H - 28 * MM, "Investigador/a: ________________________________  Fecha: ____________  Estación: _____")

    # 12 Target Slots: Exact 180 x 114.3 mm grid centered
    grid_w = 180 * MM
    grid_h = 114.3 * MM
    grid_x = (PAGE_W - grid_w) / 2.0
    grid_y = (PAGE_H - grid_h) / 2.0 - 5 * MM

    col_w = grid_w / 4.0   # 45 mm
    row_h = grid_h / 3.0   # 38.1 mm

    # Outer Frame
    c.setStrokeColor(colors.HexColor("#f59e0b"))
    c.setLineWidth(2.0)
    c.roundRect(grid_x - 1.5 * MM, grid_y - 1.5 * MM, grid_w + 3 * MM, grid_h + 3 * MM, 3 * MM, fill=False, stroke=True)

    idx = 0
    for r in range(3):
        for col in range(4):
            data = QPU_SLOTS[idx]
            bx = grid_x + col * col_w
            by = grid_y + (2 - r) * row_h

            # Slot Box
            c.setFillColor(colors.HexColor("#f8fafc"))
            c.setStrokeColor(colors.HexColor("#cbd5e1"))
            c.setLineWidth(1.0)
            c.rect(bx, by, col_w, row_h, fill=True, stroke=True)

            # Central Big Watermark Number
            c.setFont("DejaVuBold", 32)
            c.setFillColor(colors.HexColor("#e2e8f0"))
            c.drawCentredString(bx + col_w / 2.0, by + row_h / 2.0 - 5 * MM, str(data["num"]))

            # Badge pill: Row 0 at top, Row 1 in center, Row 2 at bottom (پایین شکل!)
            if r == 0:
                # Top row: pill at top
                pill_y = by + row_h - 7.5 * MM
            elif r == 1:
                # Middle row: pill in center
                pill_y = by + row_h / 2.0 - 3 * MM
            else:
                # Bottom row: pill at bottom (پایین شکل!)
                pill_y = by + 2 * MM

            c.setFillColor(data["color"])
            c.roundRect(bx + 3 * MM, pill_y, col_w - 6 * MM, 5.5 * MM, 1.5 * MM, fill=True, stroke=False)
            c.setFont("DejaVuBold", 7)
            c.setFillColor(colors.white)
            c.drawCentredString(bx + col_w / 2.0, pill_y + 1.5 * MM, f"#{data['num']} {data['title'][:11]}")

            idx += 1

    # Minimal Bottom Certification Footer
    bot_y = 14 * MM
    bot_h = 28 * MM
    c.setFillColor(colors.HexColor("#090d16"))
    c.roundRect(grid_x, bot_y, grid_w, bot_h, 3 * MM, fill=True, stroke=False)

    c.setStrokeColor(colors.HexColor("#f59e0b"))
    c.setLineWidth(1.2)
    c.roundRect(grid_x + 1.5 * MM, bot_y + 1.5 * MM, grid_w - 3 * MM, bot_h - 3 * MM, 2 * MM, fill=False, stroke=True)

    c.setFont("DejaVuBold", 9.5)
    c.setFillColor(colors.HexColor("#f59e0b"))
    c.drawString(grid_x + 6 * MM, bot_y + bot_h - 8.5 * MM, "VERIFICACIÓN TÉCNICA: 1 LLAVERO 3D DEL CHIP CUÁNTICO QPU")

    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawString(grid_x + 6 * MM, bot_y + bot_h - 15 * MM, "Los 12 bloques de microondas del procesador cuántico han sido verificados con éxito.")

    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(grid_x + 6 * MM, bot_y + 4.5 * MM, "[ ✓ ] 12 Bloques Verificados")

    c.setFillColor(colors.white)
    c.drawString(grid_x + 65 * MM, bot_y + 4.5 * MM, "Firma del Investigador: ___________________________")

    c.setFillColor(colors.HexColor("#f59e0b"))
    c.drawString(grid_x + grid_w - 45 * MM, bot_y + 4.5 * MM, "[ CANJEADO ★ ]")

    c.showPage()
    c.save()
    print(f"Generated Matching QPU Board: {output_path}")


def main():
    print("Generating Minimal Competition Print Pack with LARGE A4 cutting sheets and correct number positions...")

    f_guide = os.path.join(PACK_DIR, "00_GUIA_DEL_CONCURSO.pdf")
    f_chibi_b = os.path.join(PACK_DIR, "01_CHIBI_TABLERO_BASE_A4.pdf")
    f_chibi_c = os.path.join(PACK_DIR, "02_CHIBI_PIEZAS_RECORTAR_A4.pdf")
    f_qpu_b = os.path.join(PACK_DIR, "03_QPU_TABLERO_BASE_A4.pdf")
    f_qpu_c = os.path.join(PACK_DIR, "04_QPU_PIEZAS_RECORTAR_A4.pdf")

    generate_guide_pdf(f_guide)
    generate_chibi_board_matching_pdf(f_chibi_b)
    generate_chibi_cutouts_large_pdf(f_chibi_c)
    generate_qpu_board_matching_pdf(f_qpu_b)
    generate_qpu_cutouts_large_pdf(f_qpu_c)

    print("All 5 Competition Print Pack PDFs generated successfully!")


if __name__ == "__main__":
    main()
