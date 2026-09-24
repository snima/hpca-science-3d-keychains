#!/usr/bin/env python3
"""
GENERATE MINIMAL COMPETITION PRINT PACK (CONCURSO LISTO PARA IMPRIMIR)
======================================================================
Generates the minimal, essential A4 PDF sheets required to run the competition:
1. 00_GUIA_DEL_CONCURSO.pdf           - 1-Page Organizer & Instructor Quick-Guide
2. 01_CHIBI_TABLERO_BASE_A4.pdf       - 1-Page Base Board (Kids / 6 Blocks)
3. 02_CHIBI_PIEZAS_RECORTAR_A4.pdf    - 1-Page Cut-out Sheet (Kids / 6 Blocks - Tijeras ✂️)
4. 03_QPU_TABLERO_BASE_A4.pdf         - 1-Page Base Board (Teens / 12 Blocks)
5. 04_QPU_PIEZAS_RECORTAR_A4.pdf      - 1-Page Cut-out Sheet (Teens / 12 Blocks - Tijeras ✂️)
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
PAGE_W, PAGE_H = A4

# Chibi 6 Blocks Assets
CHIBI_BLOCKS = [os.path.join(KIDS_DIR, f"block_{i}.png") for i in range(1, 7)]
CHIBI_HERO = os.path.join(KIDS_DIR, "chibi_gpu_2d_full_color.png")

# QPU 12 Blocks Assets
QPU_BLOCKS = [os.path.join(QPU_DIR, f"qpu_block_{i}.png") for i in range(1, 13)]
QPU_HERO = os.path.join(QPU_DIR, "qpu_2d_full_color.png")

CHIBI_DATA = [
    {"num": 1, "title": "Anilla de Viaje", "color": colors.HexColor("#0284c7")},
    {"num": 2, "title": "Cerebro HPC&A", "color": colors.HexColor("#db2777")},
    {"num": 3, "title": "Radiador Superior", "color": colors.HexColor("#0d9488")},
    {"num": 4, "title": "Bota PCIe Izquierda", "color": colors.HexColor("#4f46e5")},
    {"num": 5, "title": "Sonrisa Kawaii", "color": colors.HexColor("#ea580c")},
    {"num": 6, "title": "Escape Turbo", "color": colors.HexColor("#16a34a")},
]

QPU_DATA = [
    {"num": 1, "title": "Wirebond NW & Ojal", "color": colors.HexColor("#0284c7")},
    {"num": 2, "title": "Placa HPC&A & Pads N1", "color": colors.HexColor("#b45309")},
    {"num": 3, "title": "QUANTUM & Pads N2", "color": colors.HexColor("#0d9488")},
    {"num": 4, "title": "Almohadillas NE", "color": colors.HexColor("#4f46e5")},
    {"num": 5, "title": "Bus I/O & Cúbit Q0", "color": colors.HexColor("#06b6d4")},
    {"num": 6, "title": "Resonador CPW R0", "color": colors.HexColor("#2563eb")},
    {"num": 7, "title": "Cúbit Central Q1", "color": colors.HexColor("#7c3aed")},
    {"num": 8, "title": "Acoplamiento Este", "color": colors.HexColor("#9333ea")},
    {"num": 9, "title": "Retorno Tierra Q2", "color": colors.HexColor("#ea580c")},
    {"num": 10, "title": "Resonador CPW R2", "color": colors.HexColor("#16a34a")},
    {"num": 11, "title": "Flux Z & Pads S1", "color": colors.HexColor("#059669")},
    {"num": 12, "title": "Almohadillas SE", "color": colors.HexColor("#d97706")},
]


# ==============================================================================
# 0. GUÍA RÁPIDA DEL CONCURSO (INSTRUCTOR & ORGANIZADOR)
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

    # Content Boxes
    y = PAGE_H - 52 * MM

    def section_box(title, items, h_mm, accent_hex):
        nonlocal y
        c.setFillColor(colors.HexColor("#f8fafc"))
        c.setStrokeColor(colors.HexColor(accent_hex))
        c.setLineWidth(1.5)
        c.roundRect(20 * MM, y - h_mm * MM, PAGE_W - 40 * MM, h_mm * MM, 3 * MM, fill=True, stroke=True)

        c.setFillColor(colors.HexColor(accent_hex))
        c.roundRect(24 * MM, y - 6 * MM, 80 * MM, 5.5 * MM, 1.5 * MM, fill=True, stroke=False)
        c.setFont("DejaVuBold", 7.5)
        c.setFillColor(colors.white)
        c.drawCentredString(24 * MM + 40 * MM, y - 2.5 * MM, title)

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

    # Box 1: Materiales
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

    # Box 2: Qué imprimir para el Nivel Infantil
    section_box(
        "2. NIVEL INFANTIL (PRIMARIA) — GPU CHIBI EN 6 BLOQUES",
        [
            ("Público:", "Niños/as de 6 a 11 años. Reto visual y de motricidad."),
            ("Hoja 1:", "01_CHIBI_TABLERO_BASE_A4.pdf (1 copia por participante)."),
            ("Hoja 2:", "02_CHIBI_PIEZAS_RECORTAR_A4.pdf (1 copia por participante para recortar)."),
            ("Mecánica:", "El niño/a recorta las 6 piezas (#1 al #6) y las pega en las casillas numeradas."),
            ("Recompensa:", "Al completar los 6 bloques, canjea el Llavero 3D de la GPU Chibi."),
        ],
        36,
        "#db2777"
    )

    # Box 3: Qué imprimir para el Nivel Avanzado
    section_box(
        "3. NIVEL AVANZADO (SECUNDARIA) — CHIP QPU EN 12 BLOQUES",
        [
            ("Público:", "Estudiantes de 12 a 18+ años. Reto de hardware cuántico real."),
            ("Hoja 1:", "03_QPU_TABLERO_BASE_A4.pdf (1 copia por estudiante)."),
            ("Hoja 2:", "04_QPU_PIEZAS_RECORTAR_A4.pdf (1 copia para recortar las 12 piezas técnicas)."),
            ("Mecánica:", "Alinear cúbits transmon, resonadores serpentín y pads wirebond en 12 casillas."),
            ("Recompensa:", "Al ensamblar los 12 bloques técnicos, recibe el Llavero 3D del Chip QPU."),
        ],
        36,
        "#d97706"
    )

    # Box 4: Protocolo de Entrega del Llavero 3D
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

    # Footer
    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawCentredString(PAGE_W / 2.0, 10 * MM, "Diseñado por Nima • HPC&A Research Group • High Performance Computing & Architecture")

    c.showPage()
    c.save()
    print(f"Generated Guide: {output_path}")


# ==============================================================================
# 1. NIVEL INFANTIL: TABLERO BASE DE 6 BLOQUES (1 PÁGINA A4)
# ==============================================================================

def generate_chibi_board_pdf(output_path: str):
    """Generates the 1-page A4 base board for Chibi GPU with EXTRA LARGE numbers."""
    c = canvas.Canvas(output_path, pagesize=A4)

    # Header
    c.setFillColor(colors.HexColor("#0f172a"))
    c.rect(0, PAGE_H - 52 * MM, PAGE_W, 52 * MM, fill=True, stroke=False)
    c.setFillColor(colors.HexColor("#db2777"))
    c.rect(0, PAGE_H - 54 * MM, PAGE_W, 2 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(20 * MM, PAGE_H - 12 * MM, "HPC&A SCIENCE FOR KIDS • CONCURSO DE CIENCIA")

    c.setFont("DejaVuBold", 16)
    c.setFillColor(colors.white)
    c.drawString(20 * MM, PAGE_H - 22 * MM, "TABLERO DE DESAFÍO: ¡CONSTRUYE TU GPU CHIBI!")

    c.setFont("DejaVu", 8.5)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawString(20 * MM, PAGE_H - 28 * MM, "Pega los 6 bloques en su casilla numerada para canjear tu Llavero 3D Real")

    # Name Line
    info_y = PAGE_H - 46 * MM
    c.setFillColor(colors.HexColor("#1e293b"))
    c.setStrokeColor(colors.HexColor("#334155"))
    c.roundRect(20 * MM, info_y, PAGE_W - 40 * MM, 8 * MM, 2 * MM, fill=True, stroke=True)

    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawString(24 * MM, info_y + 2.5 * MM, "Nombre del Explorador/a:")
    c.drawString(120 * MM, info_y + 2.5 * MM, "Fecha:")
    c.drawString(155 * MM, info_y + 2.5 * MM, "Mesa:")

    c.setStrokeColor(colors.HexColor("#64748b"))
    c.line(65 * MM, info_y + 2 * MM, 115 * MM, info_y + 2 * MM)
    c.line(130 * MM, info_y + 2 * MM, 150 * MM, info_y + 2 * MM)
    c.line(166 * MM, info_y + 2 * MM, PAGE_W - 25 * MM, info_y + 2 * MM)

    # 6 Slots Grid (3 cols x 2 rows)
    grid_x0 = 20 * MM
    grid_y0 = PAGE_H - 220 * MM
    grid_total_w = PAGE_W - 40 * MM  # 170 mm
    grid_total_h = 160 * MM

    col_w = (grid_total_w - 6 * MM) / 3.0   # ~54.6 mm
    row_h = (grid_total_h - 6 * MM) / 2.0   # ~77 mm

    idx = 0
    for r in range(2):
        for col in range(3):
            data = CHIBI_DATA[idx]
            bx = grid_x0 + col * (col_w + 3 * MM)
            by = grid_y0 + (1 - r) * (row_h + 6 * MM)

            # Slot Box
            c.setFillColor(colors.HexColor("#f8fafc"))
            c.setStrokeColor(data["color"])
            c.setLineWidth(1.5)
            c.setDash(4, 3)
            c.roundRect(bx, by, col_w, row_h, 3 * MM, fill=True, stroke=True)
            c.setDash()

            # Slot Header Pill with BIG Number
            c.setFillColor(data["color"])
            c.roundRect(bx + 3 * MM, by + row_h - 11 * MM, col_w - 6 * MM, 8 * MM, 2 * MM, fill=True, stroke=False)
            c.setFont("DejaVuBold", 9)
            c.setFillColor(colors.white)
            c.drawCentredString(bx + col_w / 2.0, by + row_h - 6 * MM, f"BLOQUE #{data['num']}")

            # EXTRA LARGE WATERMARK NUMBER IN CENTER (56 PT!)
            c.setFont("DejaVuBold", 56)
            c.setFillColor(colors.HexColor("#cbd5e1"))
            c.drawCentredString(bx + col_w / 2.0, by + row_h / 2.0 - 10 * MM, str(data["num"]))

            # Title & Glue hint
            c.setFont("DejaVuBold", 7.5)
            c.setFillColor(colors.HexColor("#1e293b"))
            c.drawCentredString(bx + col_w / 2.0, by + 12 * MM, data["title"])

            c.setFont("DejaVu", 6.8)
            c.setFillColor(data["color"])
            c.drawCentredString(bx + col_w / 2.0, by + 6 * MM, "[ PEGAR PIEZA AQUÍ ]")

            idx += 1

    # Bottom Certification Box
    cert_y = 12 * MM
    cert_h = 36 * MM
    c.setFillColor(colors.HexColor("#0f172a"))
    c.roundRect(20 * MM, cert_y, PAGE_W - 40 * MM, cert_h, 3 * MM, fill=True, stroke=False)

    c.setStrokeColor(colors.HexColor("#db2777"))
    c.setLineWidth(1.2)
    c.roundRect(22 * MM, cert_y + 2 * MM, PAGE_W - 44 * MM, cert_h - 4 * MM, 2 * MM, fill=False, stroke=True)

    c.setFont("DejaVuBold", 9.5)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(26 * MM, cert_y + cert_h - 9 * MM, "CERTIFICADO DE CANJE: 1 LLAVERO 3D DE LA GPU CHIBI")

    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawString(26 * MM, cert_y + cert_h - 15 * MM, "Certifico que el/la explorador/a ha completado correctamente los 6 bloques.")
    c.drawString(26 * MM, cert_y + cert_h - 20 * MM, "Entrega este certificado en el stand de HPC&A para recibir tu premio 3D.")

    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#f472b6"))
    c.drawString(26 * MM, cert_y + 5 * MM, "[ ✓ ] 6 Bloques Verificados")
    c.drawString(75 * MM, cert_y + 5 * MM, "[ ✓ ] Premio 3D Entregado")

    c.setFillColor(colors.white)
    c.drawString(125 * MM, cert_y + 5 * MM, "Firma del Monitor/a:")
    c.setStrokeColor(colors.HexColor("#64748b"))
    c.line(160 * MM, cert_y + 4.5 * MM, PAGE_W - 26 * MM, cert_y + 4.5 * MM)

    c.showPage()
    c.save()
    print(f"Generated Chibi Board: {output_path}")


# ==============================================================================
# 2. NIVEL INFANTIL: PIEZAS PARA RECORTAR EN 6 BLOQUES (1 PÁGINA A4)
# ==============================================================================

def generate_chibi_cutouts_pdf(output_path: str):
    """Generates the 1-page A4 cut-out sheet for Chibi GPU with EXTRA LARGE numbers."""
    c = canvas.Canvas(output_path, pagesize=A4)

    # Header
    c.setFillColor(colors.HexColor("#0f172a"))
    c.rect(0, PAGE_H - 46 * MM, PAGE_W, 46 * MM, fill=True, stroke=False)
    c.setFillColor(colors.HexColor("#db2777"))
    c.rect(0, PAGE_H - 48 * MM, PAGE_W, 2 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#f472b6"))
    c.drawString(20 * MM, PAGE_H - 12 * MM, "LÁMINA DE RECORTABLES • TIJERAS ✂️")

    c.setFont("DejaVuBold", 16)
    c.setFillColor(colors.white)
    c.drawString(20 * MM, PAGE_H - 22 * MM, "PIEZAS PARA RECORTAR: GPU CHIBI (6 BLOQUES)")

    c.setFont("DejaVu", 8.5)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawString(20 * MM, PAGE_H - 28 * MM, "Recorta por las líneas discontinuas con tijeras de punta redonda y pégalas en el Tablero")

    # Scissor guide
    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(20 * MM, PAGE_H - 40 * MM, "✂ CORTA POR LA LÍNEA DE PUNTOS DE CADA PIEZA • CADA PIEZA TIENE SU NÚMERO (#1 AL #6)")

    # 6 Cut Pieces (3 cols x 2 rows)
    p_x0 = 20 * MM
    p_y0 = PAGE_H - 265 * MM
    p_total_w = PAGE_W - 40 * MM
    p_col_w = (p_total_w - 6 * MM) / 3.0
    p_row_h = 102 * MM

    idx = 0
    for r in range(2):
        for col in range(3):
            data = CHIBI_DATA[idx]
            bx = p_x0 + col * (p_col_w + 3 * MM)
            by = p_y0 + (1 - r) * (p_row_h + 6 * MM)

            # Dashed outer cutting border
            c.setStrokeColor(colors.HexColor("#db2777"))
            c.setLineWidth(1.4)
            c.setDash(5, 3)
            c.roundRect(bx, by, p_col_w, p_row_h, 3 * MM, fill=False, stroke=True)
            c.setDash()

            # Scissor symbol
            c.setFont("DejaVuBold", 8)
            c.setFillColor(colors.HexColor("#db2777"))
            c.drawString(bx + 3 * MM, by + p_row_h - 5 * MM, "✂ Recortar")

            # Header Badge with BIG Number
            c.setFillColor(data["color"])
            c.roundRect(bx + 20 * MM, by + p_row_h - 7 * MM, p_col_w - 23 * MM, 6 * MM, 1.5 * MM, fill=True, stroke=False)
            c.setFont("DejaVuBold", 8.5)
            c.setFillColor(colors.white)
            c.drawCentredString(bx + 20 * MM + (p_col_w - 23 * MM) / 2.0, by + p_row_h - 3.5 * MM, f"PIEZA #{data['num']}")

            # Block image
            img_path = CHIBI_BLOCKS[idx]
            if os.path.exists(img_path):
                img_w = p_col_w - 6 * MM
                img_h = p_row_h - 20 * MM
                c.drawImage(img_path, bx + 3 * MM, by + 10 * MM, width=img_w, height=img_h, preserveAspectRatio=True, mask='auto')

            # Footer of piece
            c.setFont("DejaVuBold", 7.5)
            c.setFillColor(colors.HexColor("#0f172a"))
            c.drawCentredString(bx + p_col_w / 2.0, by + 3.5 * MM, data["title"])

            idx += 1

    # Footer
    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawCentredString(PAGE_W / 2.0, 8 * MM, "HPC&A Research Group • High Performance Computing & Architecture • 100% 3D Printable")

    c.showPage()
    c.save()
    print(f"Generated Chibi Cut-outs: {output_path}")


# ==============================================================================
# 3. NIVEL AVANZADO: TABLERO BASE DE 12 BLOQUES (1 PÁGINA A4)
# ==============================================================================

def generate_qpu_board_pdf(output_path: str):
    """Generates the 1-page A4 base board for QPU Chip with EXTRA LARGE numbers."""
    c = canvas.Canvas(output_path, pagesize=A4)

    # Header
    c.setFillColor(colors.HexColor("#090d16"))
    c.rect(0, PAGE_H - 52 * MM, PAGE_W, 52 * MM, fill=True, stroke=False)
    c.setFillColor(colors.HexColor("#f59e0b"))
    c.rect(0, PAGE_H - 54 * MM, PAGE_W, 2 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(18 * MM, PAGE_H - 12 * MM, "HPC&A QUANTUM LAB • CONCURSO TÉCNICO AVANZADO")

    c.setFont("DejaVuBold", 15.5)
    c.setFillColor(colors.white)
    c.drawString(18 * MM, PAGE_H - 22 * MM, "TABLERO DE ENSAMBLAJE: CHIP CUÁNTICO (12 BLOQUES)")

    c.setFont("DejaVu", 8.5)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawString(18 * MM, PAGE_H - 28 * MM, "Reconstruye la arquitectura de microondas en 12 bloques para canjear tu Llavero 3D Real")

    # Name Line
    info_y = PAGE_H - 46 * MM
    c.setFillColor(colors.HexColor("#111827"))
    c.setStrokeColor(colors.HexColor("#334155"))
    c.roundRect(18 * MM, info_y, PAGE_W - 36 * MM, 8 * MM, 2 * MM, fill=True, stroke=True)

    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawString(22 * MM, info_y + 2.5 * MM, "Investigador/a Junior:")
    c.drawString(110 * MM, info_y + 2.5 * MM, "Fecha:")
    c.drawString(150 * MM, info_y + 2.5 * MM, "Estación:")

    c.setStrokeColor(colors.HexColor("#64748b"))
    c.line(62 * MM, info_y + 2 * MM, 105 * MM, info_y + 2 * MM)
    c.line(122 * MM, info_y + 2 * MM, 146 * MM, info_y + 2 * MM)
    c.line(175 * MM, info_y + 2 * MM, PAGE_W - 22 * MM, info_y + 2 * MM)

    # 12 Slots Grid (4 cols x 3 rows)
    grid_x0 = 18 * MM
    grid_y0 = PAGE_H - 222 * MM
    grid_total_w = PAGE_W - 36 * MM  # 174 mm
    grid_total_h = 162 * MM

    col_w = (grid_total_w - 6 * MM) / 4.0   # ~42.0 mm
    row_h = (grid_total_h - 6 * MM) / 3.0   # ~52 mm

    idx = 0
    for r in range(3):
        for col in range(4):
            data = QPU_DATA[idx]
            bx = grid_x0 + col * (col_w + 2 * MM)
            by = grid_y0 + (2 - r) * (row_h + 3 * MM)

            # Slot Box
            c.setFillColor(colors.HexColor("#f8fafc"))
            c.setStrokeColor(data["color"])
            c.setLineWidth(1.2)
            c.setDash(3, 2)
            c.roundRect(bx, by, col_w, row_h, 2.5 * MM, fill=True, stroke=True)
            c.setDash()

            # Slot Header Pill
            c.setFillColor(data["color"])
            c.roundRect(bx + 2 * MM, by + row_h - 8 * MM, col_w - 4 * MM, 6 * MM, 1.5 * MM, fill=True, stroke=False)
            c.setFont("DejaVuBold", 7.5)
            c.setFillColor(colors.white)
            c.drawCentredString(bx + col_w / 2.0, by + row_h - 4.5 * MM, f"BLOQUE #{data['num']}")

            # EXTRA LARGE WATERMARK NUMBER IN CENTER (44 PT!)
            c.setFont("DejaVuBold", 44)
            c.setFillColor(colors.HexColor("#cbd5e1"))
            c.drawCentredString(bx + col_w / 2.0, by + row_h / 2.0 - 7 * MM, str(data["num"]))

            # Title & Glue hint
            c.setFont("DejaVuBold", 5.8)
            c.setFillColor(colors.HexColor("#0f172a"))
            c.drawCentredString(bx + col_w / 2.0, by + 8 * MM, data["title"])

            c.setFont("DejaVu", 5)
            c.setFillColor(data["color"])
            c.drawCentredString(bx + col_w / 2.0, by + 3 * MM, "[ PEGAR BLOQUE ]")

            idx += 1

    # Bottom Certification Box
    cert_y = 12 * MM
    cert_h = 36 * MM
    c.setFillColor(colors.HexColor("#090d16"))
    c.roundRect(18 * MM, cert_y, PAGE_W - 36 * MM, cert_h, 3 * MM, fill=True, stroke=False)

    c.setStrokeColor(colors.HexColor("#f59e0b"))
    c.setLineWidth(1.2)
    c.roundRect(20 * MM, cert_y + 2 * MM, PAGE_W - 40 * MM, cert_h - 4 * MM, 2 * MM, fill=False, stroke=True)

    c.setFont("DejaVuBold", 9.5)
    c.setFillColor(colors.HexColor("#f59e0b"))
    c.drawString(25 * MM, cert_y + cert_h - 9 * MM, "VERIFICACIÓN TÉCNICA: 1 LLAVERO 3D DEL CHIP CUÁNTICO QPU")

    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawString(25 * MM, cert_y + cert_h - 15 * MM, "Acreditación oficial: los 12 bloques del procesador superconductor han sido ensamblados correctamente.")
    c.drawString(25 * MM, cert_y + cert_h - 20 * MM, "Válido para canje directo por el modelo 3D original fabricado en el laboratorio.")

    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(25 * MM, cert_y + 5 * MM, "[ ✓ ] 12 Bloques Verificados")
    c.drawString(75 * MM, cert_y + 5 * MM, "[ ✓ ] Premio 3D Entregado")

    c.setFillColor(colors.white)
    c.drawString(125 * MM, cert_y + 5 * MM, "Firma del Investigador:")
    c.setStrokeColor(colors.HexColor("#64748b"))
    c.line(160 * MM, cert_y + 4.5 * MM, PAGE_W - 25 * MM, cert_y + 4.5 * MM)

    c.showPage()
    c.save()
    print(f"Generated QPU Board: {output_path}")


# ==============================================================================
# 4. NIVEL AVANZADO: PIEZAS PARA RECORTAR EN 12 BLOQUES (1 PÁGINA A4)
# ==============================================================================

def generate_qpu_cutouts_pdf(output_path: str):
    """Generates the 1-page A4 cut-out sheet for QPU Chip with EXTRA LARGE numbers."""
    c = canvas.Canvas(output_path, pagesize=A4)

    # Header
    c.setFillColor(colors.HexColor("#090d16"))
    c.rect(0, PAGE_H - 46 * MM, PAGE_W, 46 * MM, fill=True, stroke=False)
    c.setFillColor(colors.HexColor("#f59e0b"))
    c.rect(0, PAGE_H - 48 * MM, PAGE_W, 2 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#f59e0b"))
    c.drawString(18 * MM, PAGE_H - 12 * MM, "LÁMINA TÉCNICA DE RECORTABLES • TIJERAS ✂️")

    c.setFont("DejaVuBold", 15.5)
    c.setFillColor(colors.white)
    c.drawString(18 * MM, PAGE_H - 22 * MM, "PIEZAS PARA RECORTAR: CHIP QPU (12 BLOQUES)")

    c.setFont("DejaVu", 8.5)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawString(18 * MM, PAGE_H - 28 * MM, "Recorta las 12 piezas por la línea discontinua y alinea las pistas de microondas en el Tablero")

    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(18 * MM, PAGE_H - 40 * MM, "✂ CORTE DE PRECISIÓN • CADA PIEZA TIENE SU NÚMERO (#1 AL #12) Y ETIQUETA DE HARDWARE")

    # 12 Cut Pieces (4 cols x 3 rows)
    p_x0 = 18 * MM
    p_y0 = PAGE_H - 265 * MM
    p_total_w = PAGE_W - 36 * MM
    p_col_w = (p_total_w - 6 * MM) / 4.0
    p_row_h = 68 * MM

    idx = 0
    for r in range(3):
        for col in range(4):
            data = QPU_DATA[idx]
            bx = p_x0 + col * (p_col_w + 2 * MM)
            by = p_y0 + (2 - r) * (p_row_h + 4 * MM)

            # Dashed cutting border
            c.setStrokeColor(data["color"])
            c.setLineWidth(1.2)
            c.setDash(4, 2)
            c.roundRect(bx, by, p_col_w, p_row_h, 2.5 * MM, fill=False, stroke=True)
            c.setDash()

            # Scissor icon
            c.setFont("DejaVuBold", 6.5)
            c.setFillColor(data["color"])
            c.drawString(bx + 2 * MM, by + p_row_h - 4.5 * MM, "✂")

            # Header badge with BIG Number
            c.setFillColor(data["color"])
            c.roundRect(bx + 8 * MM, by + p_row_h - 6 * MM, p_col_w - 10 * MM, 5 * MM, 1.2 * MM, fill=True, stroke=False)
            c.setFont("DejaVuBold", 7)
            c.setFillColor(colors.white)
            c.drawCentredString(bx + 8 * MM + (p_col_w - 10 * MM) / 2.0, by + p_row_h - 3 * MM, f"PIEZA #{data['num']}")

            # Block image
            img_path = QPU_BLOCKS[idx]
            if os.path.exists(img_path):
                img_w = p_col_w - 4 * MM
                img_h = p_row_h - 14 * MM
                c.drawImage(img_path, bx + 2 * MM, by + 7 * MM, width=img_w, height=img_h, preserveAspectRatio=True, mask='auto')

            # Footer label
            c.setFont("DejaVuBold", 5.5)
            c.setFillColor(colors.HexColor("#0f172a"))
            c.drawCentredString(bx + p_col_w / 2.0, by + 2.5 * MM, data["title"])

            idx += 1

    # Footer
    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawCentredString(PAGE_W / 2.0, 8 * MM, "HPC&A Quantum Computing & Architecture • 100% 3D Printable Hardware Souvenirs")

    c.showPage()
    c.save()
    print(f"Generated QPU Cut-outs: {output_path}")


def main():
    print("Generating Minimal Competition Print Pack...")

    f_guide = os.path.join(PACK_DIR, "00_GUIA_DEL_CONCURSO.pdf")
    f_chibi_b = os.path.join(PACK_DIR, "01_CHIBI_TABLERO_BASE_A4.pdf")
    f_chibi_c = os.path.join(PACK_DIR, "02_CHIBI_PIEZAS_RECORTAR_A4.pdf")
    f_qpu_b = os.path.join(PACK_DIR, "03_QPU_TABLERO_BASE_A4.pdf")
    f_qpu_c = os.path.join(PACK_DIR, "04_QPU_PIEZAS_RECORTAR_A4.pdf")

    generate_guide_pdf(f_guide)
    generate_chibi_board_pdf(f_chibi_b)
    generate_chibi_cutouts_pdf(f_chibi_c)
    generate_qpu_board_pdf(f_qpu_b)
    generate_qpu_cutouts_pdf(f_qpu_c)

    print("All 5 Competition Print Pack PDFs generated successfully in concurso_listo_para_imprimir/!")


if __name__ == "__main__":
    main()
