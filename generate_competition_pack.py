#!/usr/bin/env python3
"""
GENERATE MINIMAL COMPETITION PRINT PACK (CONCURSO LISTO PARA IMPRIMIR)
======================================================================
Genera el paquete oficial de hojas de impresión A4 para el concurso de llaveros 3D:
- Todo en Español (Castellano)
- Diseños gigantes que ocupan >80% de la hoja A4 con rotación de 90°
- Textos mínimos y líneas de corte ✂ amplias
- Números de la fila superior arriba, y números de la fila inferior abajo (پایین شکل)
- LÍNEA CENTRAL DE CORTE COMPLETAMENTE LIBRE
- 4 Modelos: GPU Chibi, GPU con Espada, Chip Cuántico QPU, Candelabro Cuántico
- 2 Modos: Con Números (Principiantes) y Sin Números (Puzle Visual Puro)
"""

import os
import sys

import reportlab
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
KIDS_DIR = os.path.join(BASE_DIR, "kids_reward_challenge")
QPU_DIR = os.path.join(KIDS_DIR, "qpu_advanced_12blocks")
CHAND_DIR = os.path.join(KIDS_DIR, "chandelier_advanced_12blocks")
PACK_DIR = os.path.join(BASE_DIR, "concurso_listo_para_imprimir")
os.makedirs(PACK_DIR, exist_ok=True)

DEJAVU_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
DEJAVU_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

pdfmetrics.registerFont(TTFont("DejaVu", DEJAVU_REG))
pdfmetrics.registerFont(TTFont("DejaVuBold", DEJAVU_BOLD))

MM = 72.0 / 25.4
PAGE_W, PAGE_H = A4  # 595.27 x 841.89 pt (210 x 297 mm)

# Image Assets - With Numbers
CHIBI_ROT_IMG = os.path.join(KIDS_DIR, "chibi_gpu_2d_6blocks_grid_rot90.png")
GPU_SWORD_ROT_IMG = os.path.join(KIDS_DIR, "gpu_sword_2d_6blocks_grid_rot90.png")
QPU_ROT_IMG = os.path.join(QPU_DIR, "qpu_2d_12blocks_grid_rot90.png")
CHAND_GRID_IMG = os.path.join(CHAND_DIR, "chandelier_2d_12blocks_grid.png")

# Image Assets - Without Numbers (Puzle Visual Puro)
CHIBI_ROT_NO_NUM_IMG = os.path.join(KIDS_DIR, "chibi_gpu_2d_6blocks_grid_rot90_no_num.png")
GPU_SWORD_ROT_NO_NUM_IMG = os.path.join(KIDS_DIR, "gpu_sword_2d_6blocks_grid_rot90_no_num.png")
QPU_ROT_NO_NUM_IMG = os.path.join(QPU_DIR, "qpu_2d_12blocks_grid_rot90_no_num.png")
CHAND_GRID_NO_NUM_IMG = os.path.join(CHAND_DIR, "chandelier_2d_12blocks_grid_no_num.png")


# ==============================================================================
# 0. GUÍA OFICIAL DEL CONCURSO (1 PÁGINA)
# ==============================================================================

def generate_guide_pdf(output_path: str):
    """Genera la guía rápida oficial de 1 página A4 para organizadores y monitores."""
    c = canvas.Canvas(output_path, pagesize=A4)

    # Cabecera superior
    c.setFillColor(colors.HexColor("#0f172a"))
    c.rect(0, PAGE_H - 36 * MM, PAGE_W, 36 * MM, fill=True, stroke=False)
    c.setFillColor(colors.HexColor("#0284c7"))
    c.rect(0, PAGE_H - 38 * MM, PAGE_W, 2 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(16 * MM, PAGE_H - 12 * MM, "HPC&A RESEARCH GROUP • GUÍA OFICIAL DEL CONCURSO DE LLAVEROS 3D")

    c.setFont("DejaVuBold", 15)
    c.setFillColor(colors.white)
    c.drawString(16 * MM, PAGE_H - 22 * MM, "GUÍA RÁPIDA DE DINAMIZACIÓN: STAND Y CONCURSO DE RECOMPENSA 3D")

    c.setFont("DejaVu", 8)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawString(16 * MM, PAGE_H - 29 * MM, "Instrucciones de impresión y entrega para los 4 modelos de llaveros reales en 2 modalidades")

    y = PAGE_H - 45 * MM

    def section_box(title, items, h_mm, accent_hex):
        nonlocal y
        c.setFillColor(colors.HexColor("#f8fafc"))
        c.setStrokeColor(colors.HexColor(accent_hex))
        c.setLineWidth(1.3)
        c.roundRect(16 * MM, y - h_mm * MM, PAGE_W - 32 * MM, h_mm * MM, 2.5 * MM, fill=True, stroke=True)

        c.setFillColor(colors.HexColor(accent_hex))
        c.roundRect(19 * MM, y - 5.5 * MM, 105 * MM, 5.0 * MM, 1.5 * MM, fill=True, stroke=False)
        c.setFont("DejaVuBold", 7.0)
        c.setFillColor(colors.white)
        c.drawCentredString(19 * MM + 52.5 * MM, y - 2.5 * MM, title)

        item_y = y - 9.5 * MM
        for bullet, text in items:
            c.setFont("DejaVuBold", 7.0)
            c.setFillColor(colors.HexColor(accent_hex))
            c.drawString(20 * MM, item_y, bullet)
            c.setFont("DejaVu", 7.0)
            c.setFillColor(colors.HexColor("#1e293b"))
            c.drawString(48 * MM, item_y, text)
            item_y -= 4.0 * MM

        y -= (h_mm + 4.0) * MM

    section_box(
        "1. MATERIALES BÁSICOS EN MESA",
        [
            ("Papel A4:", "Hojas A4 estándar a color (80-100 g/m²)."),
            ("Tijeras y Pegamento:", "Tijeras escolares de punta redonda y barras de pegamento en stick."),
            ("Premios 3D Reales:", "Llaveros 3D de PLA: GPU Chibi, GPU con Espada, Chip QPU y Criostato."),
            ("2 Modos Disponibles:", "Con Números (para niños pequeños) y Sin Números (puzle visual puro)."),
        ],
        25,
        "#0284c7"
    )

    section_box(
        "2. NIVEL INFANTIL / PRIMARIA (6 A 11 AÑOS) — 6 BLOQUES",
        [
            ("Opción A (GPU Chibi):", "Hojas 01 (Tablero Base) y 02 (Recortar). Personaje animado de tarjeta gráfica."),
            ("Opción B (GPU con Espada):", "Hojas 03 (Tablero Base) y 04 (Recortar). Acelerador con espada de plasma y turbina."),
            ("Modo Sin Números:", "Hojas 09 (Chibi) y 10 (GPU Espada). Puzle visual puro sin números sobre el arte."),
            ("Recompensa 3D:", "Al completar los 6 bloques, canjea el llavero 3D correspondiente."),
        ],
        25,
        "#db2777"
    )

    section_box(
        "3. NIVEL AVANZADO / SECUNDARIA (12 A 18+ AÑOS) — 12 BLOQUES",
        [
            ("Opción A (Chip QPU):", "Hojas 05 (Tablero Base) y 06 (Recortar). Procesador cuántico con 12 bloques técnicos."),
            ("Opción B (Criostato):", "Hojas 07 (Tablero Base) y 08 (Recortar). Candelabro de dilución cuántica a 15 mK."),
            ("Modo Sin Números:", "Hojas 11 (QPU) y 12 (Criostato). Ensamble identificando resonadores y etapas."),
            ("Recompensa 3D:", "Al ensamblar la arquitectura, entrega del llavero 3D del procesador o criostato."),
        ],
        25,
        "#d97706"
    )

    section_box(
        "4. PROTOCOLO DE VALIDACIÓN Y ENTREGA",
        [
            ("Paso 1:", "El participante entrega su Tablero Base completado con los bloques pegados."),
            ("Paso 2:", "El monitor revisa que la ilustración coincida (en modo guiado o modo visual)."),
            ("Paso 3:", "Firma en el recuadro inferior [ ✓ ] Verificado y sella [ CANJEADO ★ ]."),
            ("Paso 4:", "¡Se hace entrega del Llavero 3D real fabricado en el laboratorio HPC&A!"),
        ],
        25,
        "#16a34a"
    )

    c.setFont("DejaVu", 7.0)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawCentredString(PAGE_W / 2.0, 7 * MM, "Diseñado por Nima • HPC&A Research Group • High Performance Computing & Architecture")

    c.showPage()
    c.save()
    print(f"Generated Guide: {output_path}")


# ==============================================================================
# HELPER: HOJA DE RECORTAR A4 (GRANDE, TEXTO MÍNIMO, CON O SIN NÚMEROS)
# ==============================================================================

def generate_cutout_sheet(output_path: str, img_path: str, title: str, subtitle: str,
                          border_color_hex: str, img_w_mm: float, img_h_mm: float):
    """Genera una hoja A4 de recortar con la imagen gigante y texto mínimo."""
    c = canvas.Canvas(output_path, pagesize=A4)

    # 1. Cabecera Mínima (15 mm)
    header_h = 15 * MM
    c.setFillColor(colors.HexColor("#0f172a"))
    c.rect(0, PAGE_H - header_h, PAGE_W, header_h, fill=True, stroke=False)
    c.setFillColor(colors.HexColor(border_color_hex))
    c.rect(0, PAGE_H - header_h - 1.5 * MM, PAGE_W, 1.5 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 10.0)
    c.setFillColor(colors.white)
    c.drawCentredString(PAGE_W / 2.0, PAGE_H - 9.0 * MM, f"✂ RECORTA POR LAS LÍNEAS DE PUNTOS • {title}")

    c.setFont("DejaVu", 6.8)
    c.setFillColor(colors.HexColor(border_color_hex))
    c.drawCentredString(PAGE_W / 2.0, PAGE_H - 13.2 * MM, subtitle)

    # 2. Imagen Central Gigante
    img_w = img_w_mm * MM
    img_h = img_h_mm * MM
    img_x = (PAGE_W - img_w) / 2.0
    img_y = (PAGE_H - img_h) / 2.0 - 1.5 * MM

    # Marco exterior con tijeras
    c.setStrokeColor(colors.HexColor(border_color_hex))
    c.setLineWidth(1.8)
    c.roundRect(img_x - 2.5 * MM, img_y - 2.5 * MM, img_w + 5.0 * MM, img_h + 5.0 * MM, 3.0 * MM, fill=False, stroke=True)

    if os.path.exists(img_path):
        c.drawImage(img_path, img_x, img_y, width=img_w, height=img_h, preserveAspectRatio=True)

    # Indicaciones en borde
    c.setFont("DejaVuBold", 6.8)
    c.setFillColor(colors.HexColor(border_color_hex))
    c.drawString(img_x, img_y + img_h + 3.2 * MM, "✂ Recortar por el contorno exterior")
    c.drawRightString(img_x + img_w, img_y + img_h + 3.2 * MM, "✂ LÍNEAS DE CORTE FÁCIL")

    # 3. Pie de página Mínimo (12 mm)
    bot_y = 5 * MM
    bot_h = 12 * MM
    c.setFillColor(colors.HexColor("#0f172a"))
    c.roundRect(img_x, bot_y, img_w, bot_h, 2.5 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 7.8)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawCentredString(PAGE_W / 2.0, bot_y + 7.0 * MM, "¡PEGA LAS PIEZAS EN EL TABLERO BASE PARA CANJEAR TU LLAVERO 3D REAL!")

    c.setFont("DejaVu", 6.0)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawCentredString(PAGE_W / 2.0, bot_y + 2.5 * MM, "Corta primero por las líneas divisorias ✂ y pega cada pieza en su lugar correspondiente")

    c.showPage()
    c.save()
    print(f"Generated Cut-out Sheet: {output_path}")


# ==============================================================================
# HELPER: TABLERO BASE A4 CORRESPONDIENTE (1:1 CON LAS PIEZAS)
# ==============================================================================

def generate_base_board(output_path: str, title: str, subtitle: str, prize_name: str,
                        slots_data: list, cols: int, rows: int,
                        border_color_hex: str, grid_w_mm: float, grid_h_mm: float):
    """Genera el tablero base de pegado exacto 1:1 con las piezas recortadas."""
    c = canvas.Canvas(output_path, pagesize=A4)

    # 1. Cabecera (22 mm)
    header_h = 22 * MM
    c.setFillColor(colors.HexColor("#0f172a"))
    c.rect(0, PAGE_H - header_h, PAGE_W, header_h, fill=True, stroke=False)
    c.setFillColor(colors.HexColor(border_color_hex))
    c.rect(0, PAGE_H - header_h - 1.5 * MM, PAGE_W, 1.5 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 11.5)
    c.setFillColor(colors.white)
    c.drawString(16 * MM, PAGE_H - 9.5 * MM, f"TABLERO DE DESAFÍO: {title}")

    c.setFont("DejaVu", 6.8)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawString(16 * MM, PAGE_H - 14.5 * MM, subtitle)

    c.setFont("DejaVuBold", 6.8)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(16 * MM, PAGE_H - 19.5 * MM, "Participante: __________________________________   Fecha: ____________   Mesa: ______")

    # 2. Cuadrícula de Casillas Exactas 1:1
    grid_w = grid_w_mm * MM
    grid_h = grid_h_mm * MM
    grid_x = (PAGE_W - grid_w) / 2.0
    grid_y = (PAGE_H - grid_h) / 2.0 - 2.5 * MM

    col_w = grid_w / float(cols)
    row_h = grid_h / float(rows)

    c.setStrokeColor(colors.HexColor(border_color_hex))
    c.setLineWidth(1.8)
    c.roundRect(grid_x - 1.5 * MM, grid_y - 1.5 * MM, grid_w + 3.0 * MM, grid_h + 3.0 * MM, 2.5 * MM, fill=False, stroke=True)

    idx = 0
    for r in range(rows):
        for col in range(cols):
            if idx >= len(slots_data):
                break
            data = slots_data[idx]
            bx = grid_x + col * col_w
            by = grid_y + (rows - 1 - r) * row_h

            # Casilla
            c.setFillColor(colors.HexColor("#f8fafc"))
            c.setStrokeColor(colors.HexColor("#cbd5e1"))
            c.setLineWidth(1.0)
            c.rect(bx, by, col_w, row_h, fill=True, stroke=True)

            # Marca de agua central grande
            watermark_fs = 36 if len(slots_data) > 6 else 44
            c.setFont("DejaVuBold", watermark_fs)
            c.setFillColor(colors.HexColor("#e2e8f0"))
            c.drawCentredString(bx + col_w / 2.0, by + row_h / 2.0 - 5 * MM, str(data["num"]))

            # Pastilla informativa:
            # Fila superior -> arriba
            # Fila inferior -> ABAJO (پایین شکل!)
            if r == 0:
                pill_y = by + row_h - 7.0 * MM
            elif r == rows - 1:
                pill_y = by + 2.5 * MM
            elif r == 1 and rows > 3:
                pill_y = by + row_h - 7.0 * MM
            else:
                pill_y = by + row_h / 2.0 - 3.0 * MM

            pill_w = min(col_w - 6.0 * MM, 45 * MM)
            pill_x = bx + (col_w - pill_w) / 2.0

            c.setFillColor(data["color"])
            c.roundRect(pill_x, pill_y, pill_w, 5.2 * MM, 1.5 * MM, fill=True, stroke=False)
            c.setFont("DejaVuBold", 6.8)
            c.setFillColor(colors.white)
            c.drawCentredString(bx + col_w / 2.0, pill_y + 1.5 * MM, f"#{data['num']} {data['title'][:14]}")

            idx += 1

    # 3. Certificado de Canje Inferior (18 mm)
    bot_y = 5 * MM
    bot_h = 18 * MM
    c.setFillColor(colors.HexColor("#0f172a"))
    c.roundRect(grid_x, bot_y, grid_w, bot_h, 2.5 * MM, fill=True, stroke=False)

    c.setStrokeColor(colors.HexColor(border_color_hex))
    c.setLineWidth(1.0)
    c.roundRect(grid_x + 1.2 * MM, bot_y + 1.2 * MM, grid_w - 2.4 * MM, bot_h - 2.4 * MM, 1.8 * MM, fill=False, stroke=True)

    c.setFont("DejaVuBold", 7.8)
    c.setFillColor(colors.HexColor(border_color_hex))
    c.drawString(grid_x + 5 * MM, bot_y + bot_h - 6.2 * MM, f"CERTIFICADO DE CANJE: 1 LLAVERO 3D REAL DE {prize_name.upper()}")

    c.setFont("DejaVuBold", 6.8)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(grid_x + 5 * MM, bot_y + 3.5 * MM, f"[ ✓ ] {len(slots_data)} Bloques Verificados")

    c.setFillColor(colors.white)
    c.drawString(grid_x + 48 * MM, bot_y + 3.5 * MM, "Firma del Monitor/a: ___________________________")

    c.setFillColor(colors.HexColor("#f59e0b"))
    c.drawRightString(grid_x + grid_w - 5 * MM, bot_y + 3.5 * MM, "[ CANJEADO ★ ]")

    c.showPage()
    c.save()
    print(f"Generated Matching Base Board: {output_path}")


# ==============================================================================
# DEFINICIONES DE CASILLAS PARA CADA MODELO
# ==============================================================================

# 1. Chibi GPU (6 bloques, rotado 90°: 2 cols x 3 filas)
CHIBI_ROT_SLOTS = [
    {"num": 3, "title": "Radiador Superior", "color": colors.HexColor("#0d9488")},
    {"num": 6, "title": "Escape Turbo", "color": colors.HexColor("#16a34a")},
    {"num": 2, "title": "Cerebro HPC&A", "color": colors.HexColor("#db2777")},
    {"num": 5, "title": "Sonrisa Kawaii", "color": colors.HexColor("#ea580c")},
    {"num": 1, "title": "Anilla de Viaje", "color": colors.HexColor("#0284c7")},
    {"num": 4, "title": "Bota PCIe", "color": colors.HexColor("#4f46e5")},
]

# 2. GPU con Espada (6 bloques, rotado 90°: 2 cols x 3 filas)
GPU_SWORD_ROT_SLOTS = [
    {"num": 3, "title": "Punta de Espada", "color": colors.HexColor("#06b6d4")},
    {"num": 6, "title": "Guarda & Pomo", "color": colors.HexColor("#d97706")},
    {"num": 2, "title": "Aletas & HPC&A", "color": colors.HexColor("#0284c7")},
    {"num": 5, "title": "Pines PCIe", "color": colors.HexColor("#b45309")},
    {"num": 1, "title": "Anilla & Fan", "color": colors.HexColor("#0284c7")},
    {"num": 4, "title": "Conector PCIe", "color": colors.HexColor("#4f46e5")},
]

# 3. QPU Chip (12 bloques, rotado 90°: 3 cols x 4 filas)
QPU_ROT_SLOTS = [
    {"num": 4, "title": "Pads NE", "color": colors.HexColor("#4f46e5")},
    {"num": 8, "title": "Acople Este", "color": colors.HexColor("#9333ea")},
    {"num": 12, "title": "Pads SE", "color": colors.HexColor("#d97706")},
    {"num": 3, "title": "QUANTUM", "color": colors.HexColor("#0d9488")},
    {"num": 7, "title": "Cúbit Q1", "color": colors.HexColor("#7c3aed")},
    {"num": 11, "title": "Línea Flux Z", "color": colors.HexColor("#059669")},
    {"num": 2, "title": "Placa HPC&A", "color": colors.HexColor("#b45309")},
    {"num": 6, "title": "Resonador R0", "color": colors.HexColor("#2563eb")},
    {"num": 10, "title": "Resonador R2", "color": colors.HexColor("#16a34a")},
    {"num": 1, "title": "Wirebond NW", "color": colors.HexColor("#0284c7")},
    {"num": 5, "title": "Cúbit Q0", "color": colors.HexColor("#06b6d4")},
    {"num": 9, "title": "Tierra Q2", "color": colors.HexColor("#ea580c")},
]

# 4. Candelabro Cuántico (12 bloques, portrait nativo: 3 cols x 4 filas)
CHANDELIER_SLOTS = [
    {"num": 1, "title": "Brida 300K (O)", "color": colors.HexColor("#f59e0b")},
    {"num": 2, "title": "Anilla & HPC&A", "color": colors.HexColor("#f59e0b")},
    {"num": 3, "title": "Brida 300K (E)", "color": colors.HexColor("#f59e0b")},
    {"num": 4, "title": "Coax 4K (O)", "color": colors.HexColor("#fbbf24")},
    {"num": 5, "title": "Placa Helio 4K", "color": colors.HexColor("#fbbf24")},
    {"num": 6, "title": "Coax 4K (E)", "color": colors.HexColor("#fbbf24")},
    {"num": 7, "title": "Still 800mK (O)", "color": colors.HexColor("#06b6d4")},
    {"num": 8, "title": "Placa Fría 100mK", "color": colors.HexColor("#0284c7")},
    {"num": 9, "title": "Still 800mK (E)", "color": colors.HexColor("#06b6d4")},
    {"num": 10, "title": "Blindaje 15mK", "color": colors.HexColor("#ca8a04")},
    {"num": 11, "title": "QPU Can 15mK", "color": colors.HexColor("#d97706")},
    {"num": 12, "title": "Blindaje 15mK", "color": colors.HexColor("#ca8a04")},
]


# ==============================================================================
# MAIN ENTRY POINT
# ==============================================================================

def main():
    print("Generando Paquete de Impresión Completo para el Concurso (13 PDFs)...")

    # 0. Guía del Concurso
    f_guide = os.path.join(PACK_DIR, "00_GUIA_DEL_CONCURSO.pdf")
    generate_guide_pdf(f_guide)

    # --------------------------------------------------------------------------
    # MODO GUIADO: CON NÚMEROS (Hojas 01 a 08)
    # --------------------------------------------------------------------------

    # 1 & 2: GPU Chibi Kawaii (Infantil - 6 Bloques)
    f_chibi_b = os.path.join(PACK_DIR, "01_CHIBI_TABLERO_BASE_A4.pdf")
    f_chibi_c = os.path.join(PACK_DIR, "02_CHIBI_PIEZAS_RECORTAR_A4.pdf")
    generate_base_board(
        output_path=f_chibi_b,
        title="GPU CHIBI KAWAII (6 BLOQUES)",
        subtitle="Pega cada bloque sobre su casilla para reconstruir el personaje y ganar el llavero 3D",
        prize_name="GPU Chibi Kawaii",
        slots_data=CHIBI_ROT_SLOTS,
        cols=2, rows=3,
        border_color_hex="#db2777",
        grid_w_mm=154.0, grid_h_mm=243.9
    )
    generate_cutout_sheet(
        output_path=f_chibi_c,
        img_path=CHIBI_ROT_IMG,
        title="GPU CHIBI KAWAII (6 BLOQUES)",
        subtitle="Gira la hoja para recortar • Corta por la línea del medio ✂ y separa los 6 bloques",
        border_color_hex="#db2777",
        img_w_mm=154.0, img_h_mm=243.9
    )

    # 3 & 4: GPU con Espada (Infantil - 6 Bloques)
    f_sword_b = os.path.join(PACK_DIR, "03_GPU_ESPADA_TABLERO_BASE_A4.pdf")
    f_sword_c = os.path.join(PACK_DIR, "04_GPU_ESPADA_PIEZAS_RECORTAR_A4.pdf")
    generate_base_board(
        output_path=f_sword_b,
        title="GPU CON ESPADA HEROICA (6 BLOQUES)",
        subtitle="Reconstruye la tarjeta gráfica con su espada de plasma para canjear el llavero 3D",
        prize_name="GPU con Espada Heroica",
        slots_data=GPU_SWORD_ROT_SLOTS,
        cols=2, rows=3,
        border_color_hex="#06b6d4",
        grid_w_mm=155.0, grid_h_mm=237.0
    )
    generate_cutout_sheet(
        output_path=f_sword_c,
        img_path=GPU_SWORD_ROT_IMG,
        title="GPU CON ESPADA HEROICA (6 BLOQUES)",
        subtitle="Gira la hoja para recortar • Corta por la línea del medio ✂ y separa los 6 bloques",
        border_color_hex="#06b6d4",
        img_w_mm=155.0, img_h_mm=237.0
    )

    # 5 & 6: Chip Cuántico QPU (Avanzado - 12 Bloques)
    f_qpu_b = os.path.join(PACK_DIR, "05_QPU_TABLERO_BASE_A4.pdf")
    f_qpu_c = os.path.join(PACK_DIR, "06_QPU_PIEZAS_RECORTAR_A4.pdf")
    generate_base_board(
        output_path=f_qpu_b,
        title="CHIP CUÁNTICO SUPERCONDUCTOR QPU (12 BLOQUES)",
        subtitle="Pega los 12 módulos técnicos de microondas y resonadores para validar el procesador cuántico",
        prize_name="Chip Cuántico QPU",
        slots_data=QPU_ROT_SLOTS,
        cols=3, rows=4,
        border_color_hex="#f59e0b",
        grid_w_mm=155.0, grid_h_mm=241.0
    )
    generate_cutout_sheet(
        output_path=f_qpu_c,
        img_path=QPU_ROT_IMG,
        title="CHIP CUÁNTICO SUPERCONDUCTOR QPU (12 BLOQUES)",
        subtitle="Gira la hoja para recortar • Corta siguiendo las guías de tijeras ✂ para separar los 12 bloques",
        border_color_hex="#f59e0b",
        img_w_mm=155.0, img_h_mm=241.0
    )

    # 7 & 8: Candelabro Cuántico (Avanzado - 12 Bloques)
    f_chand_b = os.path.join(PACK_DIR, "07_CHANDELIER_TABLERO_BASE_A4.pdf")
    f_chand_c = os.path.join(PACK_DIR, "08_CHANDELIER_PIEZAS_RECORTAR_A4.pdf")
    generate_base_board(
        output_path=f_chand_b,
        title="CANDELABRO DE DILUCIÓN CUÁNTICA (12 BLOQUES)",
        subtitle="Reconstruye las 5 etapas térmicas desde 300 K hasta 15 mK para canjear el criostato 3D",
        prize_name="Candelabro de Dilución Cuántica",
        slots_data=CHANDELIER_SLOTS,
        cols=3, rows=4,
        border_color_hex="#d97706",
        grid_w_mm=150.0, grid_h_mm=244.5
    )
    generate_cutout_sheet(
        output_path=f_chand_c,
        img_path=CHAND_GRID_IMG,
        title="CANDELABRO DE DILUCIÓN CUÁNTICA (12 BLOQUES)",
        subtitle="Corta las 3 líneas horizontales y 2 verticales ✂ para obtener las 12 piezas criogénicas",
        border_color_hex="#d97706",
        img_w_mm=150.0, img_h_mm=244.5
    )

    # --------------------------------------------------------------------------
    # MODO RETO EXPERTO: SIN NÚMEROS (Puzle Visual Puro - Hojas 09 a 12)
    # --------------------------------------------------------------------------

    # 09: GPU Chibi Sin Números
    f_chibi_no_num = os.path.join(PACK_DIR, "09_CHIBI_RECORTAR_SIN_NUMEROS_A4.pdf")
    generate_cutout_sheet(
        output_path=f_chibi_no_num,
        img_path=CHIBI_ROT_NO_NUM_IMG,
        title="GPU CHIBI (MODO PUZLE VISUAL SIN NÚMEROS)",
        subtitle="Desafío experto: Recorta por las líneas ✂ y ensambla el puzle reconociendo la carita y ventiladores",
        border_color_hex="#db2777",
        img_w_mm=154.0, img_h_mm=243.9
    )

    # 10: GPU con Espada Sin Números
    f_sword_no_num = os.path.join(PACK_DIR, "10_GPU_ESPADA_RECORTAR_SIN_NUMEROS_A4.pdf")
    generate_cutout_sheet(
        output_path=f_sword_no_num,
        img_path=GPU_SWORD_ROT_NO_NUM_IMG,
        title="GPU CON ESPADA (MODO PUZLE VISUAL SIN NÚMEROS)",
        subtitle="Desafío experto: Recorta por las líneas ✂ y reconstruye la espada y la turbina de la tarjeta gráfica",
        border_color_hex="#06b6d4",
        img_w_mm=155.0, img_h_mm=237.0
    )

    # 11: Chip QPU Sin Números
    f_qpu_no_num = os.path.join(PACK_DIR, "11_QPU_RECORTAR_SIN_NUMEROS_A4.pdf")
    generate_cutout_sheet(
        output_path=f_qpu_no_num,
        img_path=QPU_ROT_NO_NUM_IMG,
        title="CHIP CUÁNTICO QPU (MODO PUZLE VISUAL SIN NÚMEROS)",
        subtitle="Desafío experto: Identifica la ubicación de los cúbits y líneas de microondas para armar el chip",
        border_color_hex="#f59e0b",
        img_w_mm=155.0, img_h_mm=241.0
    )

    # 12: Candelabro Cuántico Sin Números
    f_chand_no_num = os.path.join(PACK_DIR, "12_CHANDELIER_RECORTAR_SIN_NUMEROS_A4.pdf")
    generate_cutout_sheet(
        output_path=f_chand_no_num,
        img_path=CHAND_GRID_NO_NUM_IMG,
        title="CANDELABRO CUÁNTICO (MODO PUZLE VISUAL SIN NÚMEROS)",
        subtitle="Desafío experto: Ordena las 5 etapas criogénicas de caliente (300 K) a frío (15 mK) sin ayuda numérica",
        border_color_hex="#d97706",
        img_w_mm=150.0, img_h_mm=244.5
    )

    print("\n¡ÉXITO: Todos los 13 PDFs del Concurso generados perfectamente!")


if __name__ == "__main__":
    main()
