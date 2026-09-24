#!/usr/bin/env python3
"""
GENERATE KIDS 2D REWARD SUITE (SPANISH EDITION)
================================================
Generates 4 print-ready A4 PDF documents for distributing 3D-printed souvenirs:
1. tablero_puzle_recompensa_a4.pdf  - 2-page A4: Reward Board + Cut-out 6 pieces
2. pasaporte_misiones_chibi_a4.pdf  - 1-page A4: 6-Challenge Science Passport & Stamp Sheet
3. colorea_tu_gpu_chibi_a4.pdf     - 1-page A4: 6-Block Color & Reveal Challenge
4. hoja_combinada_todo_en_uno_a4.pdf - 1-page A4: All-in-one Single Sheet (Passport + Coupon)
"""

import os
import sys
from PIL import Image

import reportlab
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Directories
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
KIDS_DIR = os.path.join(BASE_DIR, "kids_reward_challenge")
os.makedirs(KIDS_DIR, exist_ok=True)

# Register Fonts
DEJAVU_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
DEJAVU_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

pdfmetrics.registerFont(TTFont("DejaVu", DEJAVU_REG))
pdfmetrics.registerFont(TTFont("DejaVuBold", DEJAVU_BOLD))

MM = 72.0 / 25.4  # Points per mm
PAGE_W, PAGE_H = A4  # 595.27 x 841.89 pt (210 x 297 mm)

# Assets
ASSET_FULL_2D = os.path.join(KIDS_DIR, "chibi_gpu_2d_full_color.png")
ASSET_HERO_3D = os.path.join(KIDS_DIR, "chibi_gpu_2d_isometric_hero.png")
ASSET_LINEART = os.path.join(KIDS_DIR, "chibi_gpu_coloring_lineart.png")
ASSET_GRID_2D = os.path.join(KIDS_DIR, "chibi_gpu_2d_6blocks_grid.png")

BLOCK_ASSETS = [os.path.join(KIDS_DIR, f"block_{i}.png") for i in range(1, 7)]

# Mission & Educational Data for 6 Blocks
BLOCKS_DATA = [
    {
        "num": 1,
        "title": "Anilla de Viaje",
        "subtitle": "Conector & Movilidad",
        "color": colors.HexColor("#0284c7"),  # Azul cian
        "quest_title": "Misión 1: La Anilla Viajera",
        "question": "¿Por qué la ciencia viaja por el mundo? Los investigadores comparten sus descubrimientos entre universidades.",
        "task": "Dibuja una estrella o pon un sello en la anilla para activar el viaje científico.",
        "fun_fact": "La anilla mide Ø4.6 mm, perfecta para mochilas.",
    },
    {
        "num": 2,
        "title": "Cerebro HPC&A",
        "subtitle": "Núcleo de Supercómputo",
        "color": colors.HexColor("#db2777"),  # Rosa Chibi
        "quest_title": "Misión 2: El Cerebro HPC&A",
        "question": "HPC&A significa Arquitectura y Computación de Altas Prestaciones. ¿Cuántos destellos de luz ves en los ojos?",
        "task": "Escribe cuántos destellos mágicos brillan en los ojos de la GPU: [   ]",
        "fun_fact": "Las GPU calculan millones de números a la vez.",
    },
    {
        "num": 3,
        "title": "Radiador Superior",
        "subtitle": "Disipador Térmico",
        "color": colors.HexColor("#0d9488"),  # Turquesa
        "quest_title": "Misión 3: El Radiador Frío",
        "question": "Cuando un ordenador piensa muy rápido, ¡se calienta! ¿Cómo enfriamos este procesador?",
        "task": "Sopla sobre esta casilla simulando una ráfaga de aire helado y marca la casilla.",
        "fun_fact": "El aluminio transfiere el calor al aire exterior.",
    },
    {
        "num": 4,
        "title": "Botas PCIe Izquierda",
        "subtitle": "Bus de Datos Rápido",
        "color": colors.HexColor("#4f46e5"),  # Índigo
        "quest_title": "Misión 4: Las Botas de Datos",
        "question": "En vez de pines de plástico, ¡nuestra Chibi GPU calza botitas para correr a la placa base!",
        "task": "Une con una línea la bota izquierda con la base del ordenador.",
        "fun_fact": "El bus PCIe transporta miles de millones de bits.",
    },
    {
        "num": 5,
        "title": "Sonrisa Kawaii",
        "subtitle": "Ventilador Lógico",
        "color": colors.HexColor("#ea580c"),  # Naranja
        "quest_title": "Misión 5: El Ventilador Alegre",
        "question": "El ventilador tiene 8 pétalos suaves que giran y una gran carita sonriente.",
        "task": "Cuenta los 8 pétalos y dibuja una sonrisa en la casilla de comprobación.",
        "fun_fact": "Los pétalos curvados mueven el aire sin hacer ruido.",
    },
    {
        "num": 6,
        "title": "Escape Turbo",
        "subtitle": "Rejillas de Ventilación",
        "color": colors.HexColor("#16a34a"),  # Verde
        "quest_title": "Misión 6: Rejillas de Escape",
        "question": "¡El calor sale por estas 4 rejillas ovaladas para mantener todo el sistema seguro!",
        "task": "Firma con tu nombre de científico/a para validar la misión final.",
        "fun_fact": "¡Has completado los 6 bloques! Ya puedes canjear tu premio 3D.",
    },
]


def draw_header_banner(c: canvas.Canvas, title: str, subtitle: str, badge: str = "HPC&A SCIENCE FOR KIDS"):
    """Draws a premium header banner on A4 page."""
    # Top banner background
    c.setFillColor(colors.HexColor("#0f172a"))  # Slate 900
    c.rect(0, PAGE_H - 85 * MM, PAGE_W, 85 * MM, fill=True, stroke=False)

    # Accent decorative bottom line
    c.setFillColor(colors.HexColor("#db2777"))  # Rose / Pink
    c.rect(0, PAGE_H - 87 * MM, PAGE_W, 2 * MM, fill=True, stroke=False)

    # Top Badge
    c.setFillColor(colors.HexColor("#334155"))  # Slate 700
    c.roundRect(20 * MM, PAGE_H - 18 * MM, 82 * MM, 6.5 * MM, 3 * MM, fill=True, stroke=False)
    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#38bdf8"))  # Sky cyan
    c.drawString(25 * MM, PAGE_H - 14 * MM, badge)

    # Main Title
    c.setFont("DejaVuBold", 17)
    c.setFillColor(colors.white)
    c.drawString(20 * MM, PAGE_H - 26 * MM, title)

    # Subtitle
    c.setFont("DejaVu", 9)
    c.setFillColor(colors.HexColor("#cbd5e1"))  # Slate 300
    c.drawString(20 * MM, PAGE_H - 32 * MM, subtitle)

    # Participant Info Fields in Banner
    info_y = PAGE_H - 44 * MM
    c.setStrokeColor(colors.HexColor("#334155"))
    c.setFillColor(colors.HexColor("#1e293b"))
    c.roundRect(20 * MM, info_y, PAGE_W - 40 * MM, 9 * MM, 2 * MM, fill=True, stroke=True)

    c.setFont("DejaVuBold", 8)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawString(24 * MM, info_y + 3 * MM, "Nombre del Explorador/a:")
    c.drawString(115 * MM, info_y + 3 * MM, "Fecha:")
    c.drawString(155 * MM, info_y + 3 * MM, "Puesto / Stand:")

    c.setStrokeColor(colors.HexColor("#64748b"))
    c.setLineWidth(0.8)
    c.line(65 * MM, info_y + 2.5 * MM, 110 * MM, info_y + 2.5 * MM)
    c.line(126 * MM, info_y + 2.5 * MM, 150 * MM, info_y + 2.5 * MM)
    c.line(178 * MM, info_y + 2.5 * MM, PAGE_W - 25 * MM, info_y + 2.5 * MM)

    # Insert 3D Hero Mini Image in top right corner of banner
    if os.path.exists(ASSET_HERO_3D):
        hero_w = 40 * MM
        hero_h = 32 * MM
        c.drawImage(ASSET_HERO_3D, PAGE_W - 55 * MM, PAGE_H - 42 * MM, width=hero_w, height=hero_h, preserveAspectRatio=True, mask='auto')


# ==============================================================================
# 1. TABLERO DE RECOMPENSA (2-PAGE PUZZLE BOARD + CUT-OUT SHEET)
# ==============================================================================

def generate_puzzle_board_pdf(output_path: str):
    """Generates 2-page A4: Page 1 = Base Board, Page 2 = Cut-out pieces."""
    c = canvas.Canvas(output_path, pagesize=A4)

    # ---------------- PAGE 1: TABLERO BASE DE RECOMPENSA ----------------
    draw_header_banner(
        c,
        title="¡CONSTRUYE TU GPU CHIBI Y GANA EL PREMIO 3D!",
        subtitle="Pega los 6 bloques en su casilla correspondiente para canjear tu llavero 3D real",
        badge="RETO DE INGENIERÍA Y COMPU-CIENCIA • EDICIÓN INFANTIL"
    )

    # Instructions Box
    inst_y = PAGE_H - 58 * MM
    c.setFillColor(colors.HexColor("#f8fafc"))
    c.setStrokeColor(colors.HexColor("#e2e8f0"))
    c.roundRect(20 * MM, inst_y, PAGE_W - 40 * MM, 11 * MM, 2 * MM, fill=True, stroke=True)

    c.setFont("DejaVuBold", 8.5)
    c.setFillColor(colors.HexColor("#0f172a"))
    c.drawString(24 * MM, inst_y + 6.5 * MM, "INSTRUCCIONES DE LA MISIÓN:")
    c.setFont("DejaVu", 7.8)
    c.setFillColor(colors.HexColor("#475569"))
    c.drawString(24 * MM, inst_y + 2.2 * MM, "1. Recorta los 6 bloques de la lámina adjunta  2. Pégalos en el orden 1 al 6  3. ¡Acércate al stand para recibir tu llavero!")

    # 6 Blocks Target Slots Grid (3 columns x 2 rows)
    grid_x0 = 20 * MM
    grid_y0 = PAGE_H - 192 * MM
    grid_total_w = PAGE_W - 40 * MM  # 170 mm
    grid_total_h = 130 * MM

    col_w = (grid_total_w - 6 * MM) / 3.0   # ~54.6 mm each
    row_h = (grid_total_h - 4 * MM) / 2.0   # ~63 mm each

    idx = 0
    for r in range(2):
        for col in range(3):
            data = BLOCKS_DATA[idx]
            bx = grid_x0 + col * (col_w + 3 * MM)
            by = grid_y0 + (1 - r) * (row_h + 4 * MM)

            # Slot background card
            c.setFillColor(colors.HexColor("#f1f5f9"))
            c.setStrokeColor(data["color"])
            c.setLineWidth(1.2)
            c.setDash(4, 3)
            c.roundRect(bx, by, col_w, row_h, 3 * MM, fill=True, stroke=True)
            c.setDash()  # reset dash

            # Slot Header Pill
            c.setFillColor(data["color"])
            c.roundRect(bx + 3 * MM, by + row_h - 9 * MM, col_w - 6 * MM, 6.5 * MM, 2 * MM, fill=True, stroke=False)
            c.setFont("DejaVuBold", 7.5)
            c.setFillColor(colors.white)
            c.drawCentredString(bx + col_w / 2.0, by + row_h - 5 * MM, f"BLOQUE #{data['num']}: {data['title'].upper()}")

            # Big Watermark Number in Center
            c.setFont("DejaVuBold", 32)
            c.setFillColor(colors.HexColor("#cbd5e1"))
            c.drawCentredString(bx + col_w / 2.0, by + row_h / 2.0 - 5 * MM, str(data["num"]))

            # Glue indicator text
            c.setFont("DejaVu", 7)
            c.setFillColor(colors.HexColor("#64748b"))
            c.drawCentredString(bx + col_w / 2.0, by + 12 * MM, "[ PEGAR PIEZA AQUÍ ]")
            c.drawCentredString(bx + col_w / 2.0, by + 7 * MM, data["subtitle"])

            # Small Scissors icon / glue hint
            c.setFont("DejaVuBold", 9)
            c.setFillColor(data["color"])
            c.drawCentredString(bx + col_w / 2.0, by + 2 * MM, "✂ - - - - - - - - - ✂")

            idx += 1

    # Bottom Official Certification & Voucher
    cert_y = 14 * MM
    cert_h = 42 * MM
    c.setFillColor(colors.HexColor("#0f172a"))
    c.roundRect(20 * MM, cert_y, PAGE_W - 40 * MM, cert_h, 4 * MM, fill=True, stroke=False)

    # Decorative Border
    c.setStrokeColor(colors.HexColor("#db2777"))
    c.setLineWidth(1.5)
    c.roundRect(22 * MM, cert_y + 2 * MM, PAGE_W - 44 * MM, cert_h - 4 * MM, 3 * MM, fill=False, stroke=True)

    # Badge in Cert Box
    c.setFillColor(colors.HexColor("#db2777"))
    c.roundRect(28 * MM, cert_y + cert_h - 9 * MM, 75 * MM, 6 * MM, 2 * MM, fill=True, stroke=False)
    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.white)
    c.drawCentredString(28 * MM + 37.5 * MM, cert_y + cert_h - 5 * MM, "CERTIFICADO CIENTÍFICO DE CANJE")

    # Certificate Text
    c.setFont("DejaVuBold", 10.5)
    c.setFillColor(colors.HexColor("#f8fafc"))
    c.drawString(28 * MM, cert_y + cert_h - 16 * MM, "¡RETOS SUPERADOS CON ÉXITO!")

    c.setFont("DejaVu", 8)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawString(28 * MM, cert_y + cert_h - 22 * MM, "El portador ha ensamblado correctamente los 6 bloques de la arquitectura GPU Chibi.")
    c.drawString(28 * MM, cert_y + cert_h - 27 * MM, "Queda acreditado para recibir el Llavero 3D Real fabricado en el laboratorio.")

    # Checkboxes & Signature
    c.setFont("DejaVuBold", 8)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(28 * MM, cert_y + 5 * MM, "[ ✓ ] 6 Bloques Verificados")
    c.drawString(75 * MM, cert_y + 5 * MM, "[ ✓ ] Premio 3D Entregado")

    c.setFillColor(colors.white)
    c.drawString(125 * MM, cert_y + 5 * MM, "Firma del Investigador:")
    c.setStrokeColor(colors.HexColor("#64748b"))
    c.line(160 * MM, cert_y + 4.5 * MM, PAGE_W - 28 * MM, cert_y + 4.5 * MM)

    c.showPage()

    # ---------------- PAGE 2: LÁMINA DE PIEZAS PARA RECORTAR ----------------
    draw_header_banner(
        c,
        title="PIEZAS PARA RECORTAR: GPU CHIBI",
        subtitle="Recorta con tijeras por las líneas de puntos y pégalas en el Tablero de Recompensa",
        badge="LÁMINA DE RECORTABLES • EDICIÓN DE IMPRESIÓN A COLOR"
    )

    # Top Notice
    c.setFillColor(colors.HexColor("#fef2f2"))
    c.setStrokeColor(colors.HexColor("#f87171"))
    c.roundRect(20 * MM, PAGE_H - 58 * MM, PAGE_W - 40 * MM, 10 * MM, 2 * MM, fill=True, stroke=True)
    c.setFont("DejaVuBold", 8)
    c.setFillColor(colors.HexColor("#991b1b"))
    c.drawString(24 * MM, PAGE_H - 52 * MM, "✂ INSTRUCCIONES DE CORTE:")
    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#7f1d1d"))
    c.drawString(24 * MM, PAGE_H - 56 * MM, "Usa tijeras escolares de punta redonda. Pide ayuda a un tutor si lo necesitas. Cada pieza encaja exactamente en el tablero.")

    # Draw the 6 Individual Puzzle Pieces Cards
    p_x0 = 20 * MM
    p_y0 = PAGE_H - 245 * MM
    p_col_w = (grid_total_w - 6 * MM) / 3.0
    p_row_h = 88 * MM

    idx = 0
    for r in range(2):
        for col in range(3):
            data = BLOCKS_DATA[idx]
            bx = p_x0 + col * (p_col_w + 3 * MM)
            by = p_y0 + (1 - r) * (p_row_h + 5 * MM)

            # Draw outer cut card border
            c.setStrokeColor(colors.HexColor("#db2777"))
            c.setLineWidth(1.2)
            c.setDash(5, 3)
            c.roundRect(bx, by, p_col_w, p_row_h, 3 * MM, fill=False, stroke=True)
            c.setDash()

            # Small scissor symbol & cut guide
            c.setFont("DejaVuBold", 7.5)
            c.setFillColor(colors.HexColor("#db2777"))
            c.drawString(bx + 2 * MM, by + p_row_h - 5 * MM, "✂ Recortar")

            # Piece Header
            c.setFillColor(data["color"])
            c.roundRect(bx + 20 * MM, by + p_row_h - 7 * MM, p_col_w - 22 * MM, 5.5 * MM, 1.5 * MM, fill=True, stroke=False)
            c.setFont("DejaVuBold", 7)
            c.setFillColor(colors.white)
            c.drawCentredString(bx + 20 * MM + (p_col_w - 22 * MM) / 2.0, by + p_row_h - 3.5 * MM, f"PIEZA #{data['num']}")

            # Insert the block cropped image
            block_img_path = BLOCK_ASSETS[idx]
            if os.path.exists(block_img_path):
                img_w = p_col_w - 6 * MM
                img_h = p_row_h - 26 * MM
                c.drawImage(block_img_path, bx + 3 * MM, by + 18 * MM, width=img_w, height=img_h, preserveAspectRatio=True, mask='auto')

            # Scientific Fun Fact at bottom of each piece
            c.setFont("DejaVuBold", 6.8)
            c.setFillColor(colors.HexColor("#0f172a"))
            c.drawString(bx + 3 * MM, by + 11 * MM, data["title"])
            c.setFont("DejaVu", 6)
            c.setFillColor(colors.HexColor("#64748b"))
            c.drawString(bx + 3 * MM, by + 6 * MM, data["fun_fact"][:36])

            idx += 1

    # Bottom Footer
    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawCentredString(PAGE_W / 2.0, 10 * MM, "HPC&A Research Group • High Performance Computing & Architecture • 100% 3D Printable Science")

    c.showPage()
    c.save()
    print(f"Generated: {output_path}")


# ==============================================================================
# 2. PASAPORTE DE MISIONES CIENTÍFICAS (6 CHALLENGES & STAMPS)
# ==============================================================================

def generate_passport_missions_pdf(output_path: str):
    """Generates 1-page A4: 6-Challenge Science Passport with Stamp Boxes & Prize Voucher."""
    c = canvas.Canvas(output_path, pagesize=A4)

    draw_header_banner(
        c,
        title="PASAPORTE DE MISIONES CIENTÍFICAS: GPU CHIBI",
        subtitle="Supera los 6 retos para completar el mapa de la GPU y ganar tu premio 3D",
        badge="PASAPORTE DE ACTIVIDAD • FERIA DE LA CIENCIA Y TALLERES"
    )

    # Introduction Box
    intro_y = PAGE_H - 58 * MM
    c.setFillColor(colors.HexColor("#eff6ff"))
    c.setStrokeColor(colors.HexColor("#bfdbfe"))
    c.roundRect(20 * MM, intro_y, PAGE_W - 40 * MM, 10 * MM, 2 * MM, fill=True, stroke=True)
    c.setFont("DejaVuBold", 8)
    c.setFillColor(colors.HexColor("#1e40af"))
    c.drawString(24 * MM, intro_y + 5.5 * MM, "¡BIENVENIDO AL LABORATORIO DE SUPERCOMPUTACIÓN!")
    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#1e3a8a"))
    c.drawString(24 * MM, intro_y + 2 * MM, "Cada bloque de la GPU Chibi esconde un reto. Responde la pregunta o realiza la prueba para obtener tu sello de aprobación.")

    # 6 Mission Cards in 2 columns x 3 rows
    m_x0 = 20 * MM
    m_y0 = PAGE_H - 225 * MM
    col_w = (PAGE_W - 40 * MM - 5 * MM) / 2.0  # ~82.5 mm each
    card_h = 52 * MM

    for idx, data in enumerate(BLOCKS_DATA):
        col = idx % 2
        row = idx // 2
        bx = m_x0 + col * (col_w + 5 * MM)
        by = m_y0 + (2 - row) * (card_h + 3.5 * MM)

        # Card container
        c.setFillColor(colors.white)
        c.setStrokeColor(colors.HexColor("#cbd5e1"))
        c.setLineWidth(1.0)
        c.roundRect(bx, by, col_w, card_h, 3 * MM, fill=True, stroke=True)

        # Left color strip
        c.setFillColor(data["color"])
        c.roundRect(bx, by, 3.5 * MM, card_h, 1.5 * MM, fill=True, stroke=False)

        # Mission Title
        c.setFont("DejaVuBold", 8.5)
        c.setFillColor(data["color"])
        c.drawString(bx + 6 * MM, by + card_h - 7 * MM, data["quest_title"])

        # Question / Explanation
        c.setFont("DejaVu", 7.2)
        c.setFillColor(colors.HexColor("#334155"))
        # Split text into 2 lines
        words = data["question"].split(" ")
        line1 = " ".join(words[: len(words)//2 + 1])
        line2 = " ".join(words[len(words)//2 + 1:])
        c.drawString(bx + 6 * MM, by + card_h - 13 * MM, line1)
        c.drawString(bx + 6 * MM, by + card_h - 17.5 * MM, line2)

        # Action Task
        c.setFont("DejaVuBold", 7)
        c.setFillColor(colors.HexColor("#0f172a"))
        c.drawString(bx + 6 * MM, by + card_h - 24 * MM, "▶ RETO:")
        c.setFont("DejaVu", 6.8)
        c.setFillColor(colors.HexColor("#475569"))
        t_words = data["task"].split(" ")
        t_line1 = " ".join(t_words[: len(t_words)//2 + 1])
        t_line2 = " ".join(t_words[len(t_words)//2 + 1:])
        c.drawString(bx + 6 * MM, by + card_h - 29 * MM, t_line1)
        c.drawString(bx + 6 * MM, by + card_h - 33.5 * MM, t_line2)

        # Stamp / Sticker Target Circle
        stamp_cx = bx + col_w - 14 * MM
        stamp_cy = by + 14 * MM
        c.setStrokeColor(data["color"])
        c.setLineWidth(1.2)
        c.setDash(3, 2)
        c.circle(stamp_cx, stamp_cy, 10 * MM, fill=False, stroke=True)
        c.setDash()

        c.setFont("DejaVuBold", 6)
        c.setFillColor(data["color"])
        c.drawCentredString(stamp_cx, stamp_cy + 1.5 * MM, "SELLO")
        c.drawCentredString(stamp_cx, stamp_cy - 2.5 * MM, f"MISIÓN #{data['num']}")

        # Mini Block image on left
        block_img_path = BLOCK_ASSETS[idx]
        if os.path.exists(block_img_path):
            c.drawImage(block_img_path, bx + 6 * MM, by + 3 * MM, width=20 * MM, height=14 * MM, preserveAspectRatio=True, mask='auto')

    # Perforated Tear-off Prize Voucher at Bottom
    v_y = 12 * MM
    v_h = 32 * MM

    # Perforation cutting line
    c.setStrokeColor(colors.HexColor("#db2777"))
    c.setLineWidth(1.0)
    c.setDash(4, 4)
    c.line(20 * MM, v_y + v_h + 3 * MM, PAGE_W - 20 * MM, v_y + v_h + 3 * MM)
    c.setDash()

    c.setFont("DejaVuBold", 7)
    c.setFillColor(colors.HexColor("#db2777"))
    c.drawString(20 * MM, v_y + v_h + 4.5 * MM, "✂ - - - - - - - - CORTAR AQUÍ PARA CANJEAR EL PREMIO - - - - - - - - ✂")

    # Voucher Background Card
    c.setFillColor(colors.HexColor("#0f172a"))
    c.roundRect(20 * MM, v_y, PAGE_W - 40 * MM, v_h, 3 * MM, fill=True, stroke=False)

    # Golden border on voucher
    c.setStrokeColor(colors.HexColor("#fbbf24"))
    c.setLineWidth(1.2)
    c.roundRect(22 * MM, v_y + 2 * MM, PAGE_W - 44 * MM, v_h - 4 * MM, 2 * MM, fill=False, stroke=True)

    # Voucher Texts
    c.setFont("DejaVuBold", 10)
    c.setFillColor(colors.HexColor("#fbbf24"))
    c.drawString(28 * MM, v_y + v_h - 9 * MM, "★ VALE OFICIAL POR 1 LLAVERO 3D CHIBI GPU ★")

    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#e2e8f0"))
    c.drawString(28 * MM, v_y + v_h - 15 * MM, "Presenta este cupón sellado en el stand de HPC&A para recibir tu llavero original.")
    c.drawString(28 * MM, v_y + v_h - 20 * MM, "Diseñado por Nima • Fabricado mediante impresión 3D FDM • Soporte 0%")

    # Validation Stamp Box on Voucher
    c.setStrokeColor(colors.HexColor("#38bdf8"))
    c.setLineWidth(1.0)
    c.roundRect(PAGE_W - 65 * MM, v_y + 4 * MM, 40 * MM, 22 * MM, 2 * MM, fill=False, stroke=True)
    c.setFont("DejaVuBold", 6.5)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawCentredString(PAGE_W - 45 * MM, v_y + 16 * MM, "SELLO FINAL DE CANJE")
    c.setFont("DejaVu", 6)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawCentredString(PAGE_W - 45 * MM, v_y + 9 * MM, "[ ENTREGADO ]")

    c.showPage()
    c.save()
    print(f"Generated: {output_path}")


# ==============================================================================
# 3. LÁMINA PARA COLOREAR POR BLOQUES (COLOR & REVEAL CHALLENGE)
# ==============================================================================

def generate_coloring_challenge_pdf(output_path: str):
    """Generates 1-page A4: 6-Block Color & Reveal Sheet with Palette Guide."""
    c = canvas.Canvas(output_path, pagesize=A4)

    draw_header_banner(
        c,
        title="¡COLOREA Y DESCUBRE TU GPU CHIBI!",
        subtitle="Pinta los 6 bloques de la arquitectura para activar los circuitos y recibir tu premio 3D",
        badge="ARTE & TECNOLOGÍA • RETO DE COLOREAR POR BLOQUES"
    )

    # Color Palette Legend Box
    leg_y = PAGE_H - 64 * MM
    c.setFillColor(colors.HexColor("#f8fafc"))
    c.setStrokeColor(colors.HexColor("#e2e8f0"))
    c.roundRect(20 * MM, leg_y, PAGE_W - 40 * MM, 16 * MM, 2 * MM, fill=True, stroke=True)

    c.setFont("DejaVuBold", 8)
    c.setFillColor(colors.HexColor("#0f172a"))
    c.drawString(24 * MM, leg_y + 11 * MM, "CÓDIGO DE COLORES CIENTÍFICOS (O USA TU IMAGINACIÓN):")

    palette = [
        ("1", "#0284c7", "Azul Cielo"),
        ("2", "#db2777", "Rosa Fresa"),
        ("3", "#0d9488", "Turquesa"),
        ("4", "#7c3aed", "Lavanda"),
        ("5", "#f59e0b", "Oro / Amarillo"),
        ("6", "#10b981", "Verde Menta"),
    ]

    p_w = (PAGE_W - 48 * MM) / 6.0
    for i, (num, hex_col, name) in enumerate(palette):
        px = 24 * MM + i * p_w
        c.setFillColor(colors.HexColor(hex_col))
        c.circle(px + 4 * MM, leg_y + 5 * MM, 3.5 * MM, fill=True, stroke=False)
        c.setFont("DejaVuBold", 7.5)
        c.setFillColor(colors.white)
        c.drawCentredString(px + 4 * MM, leg_y + 3.5 * MM, num)

        c.setFont("DejaVuBold", 6.8)
        c.setFillColor(colors.HexColor("#1e293b"))
        c.drawString(px + 9 * MM, leg_y + 4 * MM, name)

    # Central Coloring Lineart Box
    art_y = PAGE_H - 225 * MM
    art_w = PAGE_W - 40 * MM
    art_h = 155 * MM

    c.setFillColor(colors.white)
    c.setStrokeColor(colors.HexColor("#0f172a"))
    c.setLineWidth(1.5)
    c.roundRect(20 * MM, art_y, art_w, art_h, 4 * MM, fill=True, stroke=True)

    # Insert Lineart Image
    if os.path.exists(ASSET_LINEART):
        img_disp_w = art_w - 12 * MM
        img_disp_h = art_h - 28 * MM
        c.drawImage(ASSET_LINEART, 26 * MM, art_y + 18 * MM, width=img_disp_w, height=img_disp_h, preserveAspectRatio=True, mask='auto')

    # Draw 6 Zone Badges on the drawing
    dx = (art_w - 12 * MM) / 3.0
    dy = (art_h - 28 * MM) / 2.0
    b_idx = 1
    for r in range(2):
        for col in range(3):
            badge_x = 28 * MM + col * dx
            badge_y = art_y + 18 * MM + (1 - r) * dy + dy - 12 * MM

            c.setFillColor(colors.HexColor("#0f172a"))
            c.circle(badge_x + 6 * MM, badge_y + 4 * MM, 4 * MM, fill=True, stroke=False)
            c.setFont("DejaVuBold", 8)
            c.setFillColor(colors.white)
            c.drawCentredString(badge_x + 6 * MM, badge_y + 1.8 * MM, str(b_idx))

            c.setFont("DejaVuBold", 7)
            c.setFillColor(colors.HexColor("#475569"))
            c.drawString(badge_x + 12 * MM, badge_y + 2.5 * MM, BLOCKS_DATA[b_idx - 1]["title"])

            b_idx += 1

    # Bottom Prize Claim Box
    bot_y = 12 * MM
    bot_h = 28 * MM
    c.setFillColor(colors.HexColor("#0f172a"))
    c.roundRect(20 * MM, bot_y, PAGE_W - 40 * MM, bot_h, 3 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 9.5)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(26 * MM, bot_y + bot_h - 8 * MM, "¡COMPLETA LOS 6 BLOQUES DE COLOR Y RECLAMA TU LLAVERO 3D!")

    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#e2e8f0"))
    c.drawString(26 * MM, bot_y + bot_h - 14 * MM, "Muestra tu obra de arte al instructor del stand para certificar tu diseño.")
    c.drawString(26 * MM, bot_y + bot_h - 19 * MM, "Recibirás la edición coleccionable de la GPU Chibi impresa en 3D.")

    # Rating stars
    c.setFont("DejaVuBold", 11)
    c.setFillColor(colors.HexColor("#fbbf24"))
    c.drawString(26 * MM, bot_y + 3 * MM, "★★★★★ EXCELENCIA CIENTÍFICA")

    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.white)
    c.drawString(PAGE_W - 85 * MM, bot_y + 5 * MM, "Sello de Canje: [                    ]")

    c.showPage()
    c.save()
    print(f"Generated: {output_path}")


# ==============================================================================
# 4. HOJA COMBINADA TODO-EN-UNO (ECO SINGLE SHEET)
# ==============================================================================

def generate_combo_single_sheet_pdf(output_path: str):
    """Generates 1-page A4: Combo sheet containing 6-block challenges + colored illustration + voucher."""
    c = canvas.Canvas(output_path, pagesize=A4)

    draw_header_banner(
        c,
        title="DESAFÍO EXPRÉS: GPU CHIBI EN 6 BLOQUES",
        subtitle="Hoja todo-en-uno: resuelve, une los 6 bloques y canjea tu premio 3D",
        badge="EDICIÓN A4 TODO-EN-UNO • HOJA DE ACTIVIDAD Y PREMIO"
    )

    # Top Half: Master Grid with 6 Blocks Visual (100 mm height)
    top_y = PAGE_H - 145 * MM
    if os.path.exists(ASSET_GRID_2D):
        img_w = PAGE_W - 40 * MM
        img_h = 80 * MM
        c.drawImage(ASSET_GRID_2D, 20 * MM, top_y + 5 * MM, width=img_w, height=img_h, preserveAspectRatio=True, mask='auto')

    # Middle Half: 6 Check-in Quests
    q_y0 = PAGE_H - 225 * MM
    q_col_w = (PAGE_W - 40 * MM - 5 * MM) / 3.0
    q_card_h = 36 * MM

    for idx, data in enumerate(BLOCKS_DATA):
        col = idx % 3
        row = idx // 3
        bx = 20 * MM + col * (q_col_w + 2.5 * MM)
        by = q_y0 + (1 - row) * (q_card_h + 3 * MM)

        c.setFillColor(colors.HexColor("#f8fafc"))
        c.setStrokeColor(data["color"])
        c.setLineWidth(1.0)
        c.roundRect(bx, by, q_col_w, q_card_h, 2 * MM, fill=True, stroke=True)

        c.setFillColor(data["color"])
        c.roundRect(bx + 2 * MM, by + q_card_h - 6 * MM, q_col_w - 4 * MM, 4.5 * MM, 1.5 * MM, fill=True, stroke=False)
        c.setFont("DejaVuBold", 6.8)
        c.setFillColor(colors.white)
        c.drawCentredString(bx + q_col_w / 2.0, by + q_card_h - 4 * MM, f"BLOQUE #{data['num']}: {data['title'][:14]}")

        c.setFont("DejaVu", 6.2)
        c.setFillColor(colors.HexColor("#334155"))
        words = data["task"].split(" ")
        c.drawString(bx + 3 * MM, by + q_card_h - 11 * MM, " ".join(words[:5]))
        c.drawString(bx + 3 * MM, by + q_card_h - 15 * MM, " ".join(words[5:10]))

        # Mini checkbox / stamp slot
        c.setStrokeColor(data["color"])
        c.setLineWidth(0.8)
        c.rect(bx + q_col_w - 12 * MM, by + 3 * MM, 9 * MM, 9 * MM, fill=False, stroke=True)
        c.setFont("DejaVuBold", 6)
        c.setFillColor(data["color"])
        c.drawCentredString(bx + q_col_w - 7.5 * MM, by + 6 * MM, "[ ✓ ]")

    # Bottom Half: Cut-off Claim Coupon
    v_y = 12 * MM
    v_h = 32 * MM

    c.setStrokeColor(colors.HexColor("#db2777"))
    c.setLineWidth(1.0)
    c.setDash(4, 4)
    c.line(20 * MM, v_y + v_h + 3 * MM, PAGE_W - 20 * MM, v_y + v_h + 3 * MM)
    c.setDash()

    c.setFont("DejaVuBold", 7)
    c.setFillColor(colors.HexColor("#db2777"))
    c.drawString(20 * MM, v_y + v_h + 4.5 * MM, "✂ - - - - - - - - CORTAR Y ENTREGAR PARA RECOGER EL LLAVERO 3D - - - - - - - - ✂")

    c.setFillColor(colors.HexColor("#0f172a"))
    c.roundRect(20 * MM, v_y, PAGE_W - 40 * MM, v_h, 3 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 10)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(26 * MM, v_y + v_h - 9 * MM, "VALE DE RECOMPENSA: 1 LLAVERO 3D CHIBI GPU")

    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#e2e8f0"))
    c.drawString(26 * MM, v_y + v_h - 15 * MM, "Certifico que el/la explorador/a ha completado satisfactoriamente los 6 bloques.")
    c.drawString(26 * MM, v_y + v_h - 20 * MM, "HPC&A Research Group • High Performance Computing & Architecture")

    c.setFillColor(colors.HexColor("#fbbf24"))
    c.drawString(PAGE_W - 70 * MM, v_y + 12 * MM, "[ CANJEADO ]")

    c.showPage()
    c.save()
    print(f"Generated: {output_path}")


def main():
    print("Generating full Kids Reward Challenge Suite...")

    puz_pdf = os.path.join(KIDS_DIR, "tablero_puzle_recompensa_a4.pdf")
    pas_pdf = os.path.join(KIDS_DIR, "pasaporte_misiones_chibi_a4.pdf")
    col_pdf = os.path.join(KIDS_DIR, "colorea_tu_gpu_chibi_a4.pdf")
    com_pdf = os.path.join(KIDS_DIR, "hoja_combinada_todo_en_uno_a4.pdf")

    generate_puzzle_board_pdf(puz_pdf)
    generate_passport_missions_pdf(pas_pdf)
    generate_coloring_challenge_pdf(col_pdf)
    generate_combo_single_sheet_pdf(com_pdf)

    print("All 4 PDFs generated successfully!")


if __name__ == "__main__":
    main()
