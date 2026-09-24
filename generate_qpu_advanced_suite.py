#!/usr/bin/env python3
"""
GENERATE ADVANCED 12-BLOCK QUANTUM SUITE (SPANISH EDITION)
===========================================================
Generates 4 print-ready A4 PDF documents for older kids, teens & students:
1. tablero_cuantico_avanzado_12bloques_a4.pdf  - 2-page A4: 12-Block Reward Board + Cut-out 12 pieces
2. pasaporte_cuantico_avanzado_12retos_a4.pdf  - 1-page A4: 12-Challenge Quantum Passport & Stamp Sheet
3. esquema_circuito_cuantico_12bloques_a4.pdf  - 1-page A4: 12-Zone Blueprint & Schematic Tracing
4. hoja_combinada_cuantica_expres_a4.pdf       - 1-page A4: All-in-one Single Sheet (12-block Map + Coupon)
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
QPU_DIR = os.path.join(KIDS_DIR, "qpu_advanced_12blocks")
os.makedirs(QPU_DIR, exist_ok=True)

# Register Fonts
DEJAVU_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
DEJAVU_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

pdfmetrics.registerFont(TTFont("DejaVu", DEJAVU_REG))
pdfmetrics.registerFont(TTFont("DejaVuBold", DEJAVU_BOLD))

MM = 72.0 / 25.4  # Points per mm
PAGE_W, PAGE_H = A4  # 595.27 x 841.89 pt (210 x 297 mm)

# Assets
ASSET_FULL_2D = os.path.join(QPU_DIR, "qpu_2d_full_color.png")
ASSET_HERO_3D = os.path.join(QPU_DIR, "qpu_2d_isometric_hero.png")
ASSET_LINEART = os.path.join(QPU_DIR, "qpu_circuit_lineart.png")
ASSET_GRID_2D = os.path.join(QPU_DIR, "qpu_2d_12blocks_grid.png")

BLOCK_ASSETS = [os.path.join(QPU_DIR, f"qpu_block_{i}.png") for i in range(1, 13)]

# Comprehensive Technical Metadata for the 12 Blocks of the QPU Chip
QPU_BLOCKS_DATA = [
    {
        "num": 1,
        "title": "Anilla & Wirebond NW",
        "category": "Interconexión Criogénica",
        "color": colors.HexColor("#0284c7"),  # Cian
        "challenge": "La anilla soporta el anclaje criogénico. ¿A qué temperatura (-273 °C) opera para mantener resistencia cero?",
        "answer_hint": "T ≈ 15 milikelvin (-273.135 °C)",
        "tech_spec": "Ø4.6 mm Through-hole • 4 pads Au",
    },
    {
        "num": 2,
        "title": "Placa HPC&A & Pads N1",
        "category": "Arquitectura de Control",
        "color": colors.HexColor("#b45309"),  # Ámbar
        "challenge": "El acrónimo HPC&A identifica la arquitectura. ¿Por qué se usan hilos de oro ultrafino de 25 micras para wirebonding?",
        "answer_hint": "Alta conductividad térmica y eléctrica",
        "tech_spec": "Grabado láser en oro • 6 pads N1",
    },
    {
        "num": 3,
        "title": "Logo QUANTUM & Pads N2",
        "category": "Filtrado RF",
        "color": colors.HexColor("#0d9488"),  # Turquesa
        "challenge": "Las microondas controlan los cúbits. ¿En qué rango de frecuencias (GHz) operan los pulsos de control?",
        "answer_hint": "Banda de 4.0 a 8.5 GHz",
        "tech_spec": "Líneas coplanares de microondas",
    },
    {
        "num": 4,
        "title": "Almohadillas NE",
        "category": "Terminación de Línea",
        "color": colors.HexColor("#4f46e5"),  # Índigo
        "challenge": "Los atenuadores criogénicos reducen el ruido térmico. ¿Por qué el ruido cuántico debe ser mínimo?",
        "answer_hint": "Evita la decoherencia de fase",
        "tech_spec": "Impedancia característica Z0 = 50 Ω",
    },
    {
        "num": 5,
        "title": "Bus I/O & Cúbit Q0",
        "category": "Cúbit Transmon",
        "color": colors.HexColor("#06b6d4"),  # Cian eléctrico
        "challenge": "Un cúbit transmon es un circuito LC no lineal. ¿Qué componente cuántico crea la no-linealidad?",
        "answer_hint": "La Unión Josephson de Aluminio",
        "tech_spec": "Transmon en cruz • Ec/Ej ≈ 50",
    },
    {
        "num": 6,
        "title": "Resonador CPW R0",
        "category": "Lectura Dispersiva",
        "color": colors.HexColor("#2563eb"),  # Azul Real
        "challenge": "El resonador serpentín actúa como cavidad cuántica. ¿Por qué tiene forma de serpentín en vez de línea recta?",
        "answer_hint": "Para medir λ/4 ocupando menos silicio",
        "tech_spec": "Guía de onda coplanar λ/4",
    },
    {
        "num": 7,
        "title": "Cúbit Central Q1",
        "category": "Procesador Central",
        "color": colors.HexColor("#7c3aed"),  # Púrpura
        "challenge": "El cúbit central puede entrelazarse con sus vecinos. ¿Qué puerta cuántica genera entrelazamiento bi-cúbit?",
        "answer_hint": "Puerta CNOT o iSWAP",
        "tech_spec": "Nodo central de entrelazamiento",
    },
    {
        "num": 8,
        "title": "Acoplamiento Este",
        "category": "Bus Colectivo",
        "color": colors.HexColor("#9333ea"),  # Violeta
        "challenge": "La lectura dispersiva permite saber el estado (|0> o |1>) sin destruirlo. ¿Cómo se llama este tipo de medida?",
        "answer_hint": "Medición cuántica no destructiva (QND)",
        "tech_spec": "Desplazamiento dispersivo χ",
    },
    {
        "num": 9,
        "title": "Retorno a Masa & Q2",
        "category": "Plano de Referencia",
        "color": colors.HexColor("#ea580c"),  # Naranja
        "challenge": "El plano de masa continuo de niobio evita corrientes parásitas. ¿Qué efecto superconductor expulsa el campo magnético?",
        "answer_hint": "Efecto Meissner-Ochsenfeld",
        "tech_spec": "Película fina de Niobio (Nb)",
    },
    {
        "num": 10,
        "title": "Resonador CPW R2",
        "category": "Multiplexación FDM",
        "color": colors.HexColor("#16a34a"),  # Verde
        "challenge": "Podemos leer muchos cúbits con un solo cable coaxial. ¿Cómo se llama leer diferentes frecuencias a la vez?",
        "answer_hint": "Multiplexación por frecuencia (FDM)",
        "tech_spec": "Picos de resonancia f0 = 6.2 GHz",
    },
    {
        "num": 11,
        "title": "Línea Flux Z & Pads S1",
        "category": "Sintonización Rápida",
        "color": colors.HexColor("#059669"),  # Esmeralda
        "challenge": "Una corriente continua ajusta la frecuencia del cúbit en nanosegundos. ¿Qué propiedad se altera con el flujo?",
        "answer_hint": "Energía Josephson efectiva Ej(Φ)",
        "tech_spec": "Línea de flujo magnético rápido Z",
    },
    {
        "num": 12,
        "title": "Almohadillas SE",
        "category": "Blindaje Criogénico",
        "color": colors.HexColor("#d97706"),  # Ámbar oscuro
        "challenge": "¡Circuito completo! El chip se encapsula en una caja de cobre dorado libre de oxígeno (OFHC). ¿Para qué?",
        "answer_hint": "Blindaje contra radiación infrarroja",
        "tech_spec": "Cavidad cerrada OFHC Cu-Au",
    },
]


def draw_qpu_header(c: canvas.Canvas, title: str, subtitle: str, badge: str = "HPC&A QUANTUM HARDWARE LAB • NIVEL AVANZADO"):
    """Draws a high-tech dark slate & gold header banner on A4 page."""
    c.setFillColor(colors.HexColor("#090d16"))  # Deep Dark Navy
    c.rect(0, PAGE_H - 82 * MM, PAGE_W, 82 * MM, fill=True, stroke=False)

    # Gold accent line
    c.setFillColor(colors.HexColor("#f59e0b"))
    c.rect(0, PAGE_H - 84 * MM, PAGE_W, 2 * MM, fill=True, stroke=False)

    # Badge Pill
    c.setFillColor(colors.HexColor("#1e293b"))
    c.roundRect(18 * MM, PAGE_H - 16 * MM, 105 * MM, 6.5 * MM, 3 * MM, fill=True, stroke=False)
    c.setFont("DejaVuBold", 7.2)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(22 * MM, PAGE_H - 12.5 * MM, badge)

    # Main Title
    c.setFont("DejaVuBold", 15.5)
    c.setFillColor(colors.white)
    c.drawString(18 * MM, PAGE_H - 24 * MM, title)

    # Subtitle
    c.setFont("DejaVu", 8.5)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawString(18 * MM, PAGE_H - 30 * MM, subtitle)

    # Participant Info Fields
    info_y = PAGE_H - 42 * MM
    c.setStrokeColor(colors.HexColor("#334155"))
    c.setFillColor(colors.HexColor("#111827"))
    c.roundRect(18 * MM, info_y, PAGE_W - 36 * MM, 9 * MM, 2 * MM, fill=True, stroke=True)

    c.setFont("DejaVuBold", 7.8)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawString(22 * MM, info_y + 3 * MM, "Investigador/a Junior:")
    c.drawString(110 * MM, info_y + 3 * MM, "Fecha:")
    c.drawString(150 * MM, info_y + 3 * MM, "Estación / Stand:")

    c.setStrokeColor(colors.HexColor("#64748b"))
    c.setLineWidth(0.8)
    c.line(62 * MM, info_y + 2.5 * MM, 105 * MM, info_y + 2.5 * MM)
    c.line(122 * MM, info_y + 2.5 * MM, 146 * MM, info_y + 2.5 * MM)
    c.line(178 * MM, info_y + 2.5 * MM, PAGE_W - 22 * MM, info_y + 2.5 * MM)

    # 3D Hero image in banner
    if os.path.exists(ASSET_HERO_3D):
        c.drawImage(ASSET_HERO_3D, PAGE_W - 52 * MM, PAGE_H - 40 * MM, width=44 * MM, height=34 * MM, preserveAspectRatio=True, mask='auto')


# ==============================================================================
# 1. TABLERO DE ENSAMBLAJE CUÁNTICO (12 BLOQUES) - 2 PÁGINAS A4
# ==============================================================================

def generate_qpu_puzzle_board_pdf(output_path: str):
    """Generates 2-page A4: Page 1 = 12-Slot Board, Page 2 = 12 Cut-out Pieces."""
    c = canvas.Canvas(output_path, pagesize=A4)

    # ---------------- PÁGINA 1: TABLERO BASE DE 12 BLOQUES ----------------
    draw_qpu_header(
        c,
        title="DESAFÍO AVANZADO: ENSAMBLAJE DE CHIP CUÁNTICO (QPU)",
        subtitle="Reconstruye la arquitectura de 12 bloques del procesador superconductor para canjear tu Llavero 3D Real",
        badge="HARDWARE CUÁNTICO HPC&A • EDICIÓN TÉCNICA 12 BLOQUES"
    )

    # Instructions Box
    inst_y = PAGE_H - 56 * MM
    c.setFillColor(colors.HexColor("#f8fafc"))
    c.setStrokeColor(colors.HexColor("#cbd5e1"))
    c.roundRect(18 * MM, inst_y, PAGE_W - 36 * MM, 10 * MM, 2 * MM, fill=True, stroke=True)

    c.setFont("DejaVuBold", 8)
    c.setFillColor(colors.HexColor("#0f172a"))
    c.drawString(22 * MM, inst_y + 5.5 * MM, "PROTOCOLO DE LABORATORIO:")
    c.setFont("DejaVu", 7.2)
    c.setFillColor(colors.HexColor("#475569"))
    c.drawString(22 * MM, inst_y + 1.8 * MM, "1. Recorta las 12 piezas de la lámina técnica  2. Alinea las guías de microondas y los cúbits  3. Completa el chip y canjea tu premio 3D")

    # 12 Slots Grid (4 columns x 3 rows)
    grid_x0 = 18 * MM
    grid_y0 = PAGE_H - 195 * MM
    grid_total_w = PAGE_W - 36 * MM  # 174 mm
    grid_total_h = 135 * MM

    col_w = (grid_total_w - 6 * MM) / 4.0   # ~42.0 mm each
    row_h = (grid_total_h - 6 * MM) / 3.0   # ~43.0 mm each

    idx = 0
    for r in range(3):
        for col in range(4):
            data = QPU_BLOCKS_DATA[idx]
            bx = grid_x0 + col * (col_w + 2 * MM)
            by = grid_y0 + (2 - r) * (row_h + 3 * MM)

            # Slot Box
            c.setFillColor(colors.HexColor("#f1f5f9"))
            c.setStrokeColor(data["color"])
            c.setLineWidth(1.0)
            c.setDash(3, 2)
            c.roundRect(bx, by, col_w, row_h, 2.5 * MM, fill=True, stroke=True)
            c.setDash()

            # Slot Header Pill
            c.setFillColor(data["color"])
            c.roundRect(bx + 2 * MM, by + row_h - 7 * MM, col_w - 4 * MM, 5.5 * MM, 1.5 * MM, fill=True, stroke=False)
            c.setFont("DejaVuBold", 6.5)
            c.setFillColor(colors.white)
            c.drawCentredString(bx + col_w / 2.0, by + row_h - 4 * MM, f"BLOQUE #{data['num']}")

            # Watermark Number in Center
            c.setFont("DejaVuBold", 24)
            c.setFillColor(colors.HexColor("#cbd5e1"))
            c.drawCentredString(bx + col_w / 2.0, by + row_h / 2.0 - 4 * MM, str(data["num"]))

            # Component Title & Hint
            c.setFont("DejaVuBold", 5.8)
            c.setFillColor(colors.HexColor("#1e293b"))
            c.drawCentredString(bx + col_w / 2.0, by + 12 * MM, data["title"])

            c.setFont("DejaVu", 5.2)
            c.setFillColor(colors.HexColor("#64748b"))
            c.drawCentredString(bx + col_w / 2.0, by + 7 * MM, data["category"])

            # Glue indicator
            c.setFont("DejaVu", 5)
            c.setFillColor(data["color"])
            c.drawCentredString(bx + col_w / 2.0, by + 2 * MM, "[ PEGAR BLOQUE ]")

            idx += 1

    # Bottom Certification Box
    cert_y = 12 * MM
    cert_h = 38 * MM
    c.setFillColor(colors.HexColor("#090d16"))
    c.roundRect(18 * MM, cert_y, PAGE_W - 36 * MM, cert_h, 3 * MM, fill=True, stroke=False)

    c.setStrokeColor(colors.HexColor("#f59e0b"))
    c.setLineWidth(1.2)
    c.roundRect(20 * MM, cert_y + 2 * MM, PAGE_W - 40 * MM, cert_h - 4 * MM, 2 * MM, fill=False, stroke=True)

    c.setFillColor(colors.HexColor("#f59e0b"))
    c.roundRect(26 * MM, cert_y + cert_h - 8 * MM, 85 * MM, 5.5 * MM, 1.5 * MM, fill=True, stroke=False)
    c.setFont("DejaVuBold", 7.2)
    c.setFillColor(colors.HexColor("#090d16"))
    c.drawCentredString(26 * MM + 42.5 * MM, cert_y + cert_h - 4.5 * MM, "VERIFICACIÓN CIENTÍFICA & CANJE DE PREMIO 3D")

    c.setFont("DejaVuBold", 9.5)
    c.setFillColor(colors.white)
    c.drawString(26 * MM, cert_y + cert_h - 15 * MM, "¡ARQUITECTURA CUÁNTICA ENSAMBLADA AL 100%!")

    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawString(26 * MM, cert_y + cert_h - 20 * MM, "El investigador/a ha ubicado los 12 bloques (cúbits transmon, resonadores CPW y wirebonds).")
    c.drawString(26 * MM, cert_y + cert_h - 25 * MM, "Válido para canje por 1 Llavero 3D Real del Chip Cuántico QPU impreso en el laboratorio.")

    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(26 * MM, cert_y + 4.5 * MM, "[ ✓ ] 12 Bloques Validados")
    c.drawString(75 * MM, cert_y + 4.5 * MM, "[ ✓ ] Premio 3D Entregado")

    c.setFillColor(colors.white)
    c.drawString(125 * MM, cert_y + 4.5 * MM, "Firma del Investigador:")
    c.setStrokeColor(colors.HexColor("#64748b"))
    c.line(160 * MM, cert_y + 4 * MM, PAGE_W - 26 * MM, cert_y + 4 * MM)

    c.showPage()

    # ---------------- PÁGINA 2: LÁMINA DE 12 PIEZAS PARA RECORTAR ----------------
    draw_qpu_header(
        c,
        title="LÁMINA DE 12 PIEZAS PARA RECORTAR: CHIP QPU",
        subtitle="Recorta con tijeras siguiendo las líneas de puntos y ensambla la arquitectura en el Tablero",
        badge="LÁMINA TÉCNICA DE RECORTABLES • EDICIÓN DE PRECISIÓN 12 PIEZAS"
    )

    # Notice
    c.setFillColor(colors.HexColor("#eff6ff"))
    c.setStrokeColor(colors.HexColor("#93c5fd"))
    c.roundRect(18 * MM, PAGE_H - 56 * MM, PAGE_W - 36 * MM, 9 * MM, 2 * MM, fill=True, stroke=True)
    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#1e40af"))
    c.drawString(22 * MM, PAGE_H - 51 * MM, "✂ INSTRUCCIONES DE CORTE TÉCNICO:")
    c.setFont("DejaVu", 7)
    c.setFillColor(colors.HexColor("#1e3a8a"))
    c.drawString(22 * MM, PAGE_H - 54.5 * MM, "Recorta cada bloque con cuidado por el borde punteado. Los trazos de circuito azul deben alinearse entre bloques vecinos.")

    # 12 Pieces in 4 columns x 3 rows
    p_x0 = 18 * MM
    p_y0 = PAGE_H - 245 * MM
    p_col_w = (grid_total_w - 6 * MM) / 4.0
    p_row_h = 59 * MM

    idx = 0
    for r in range(3):
        for col in range(4):
            data = QPU_BLOCKS_DATA[idx]
            bx = p_x0 + col * (p_col_w + 2 * MM)
            by = p_y0 + (2 - r) * (p_row_h + 3 * MM)

            # Piece card border
            c.setStrokeColor(data["color"])
            c.setLineWidth(1.0)
            c.setDash(4, 2)
            c.roundRect(bx, by, p_col_w, p_row_h, 2.5 * MM, fill=False, stroke=True)
            c.setDash()

            # Small scissor icon
            c.setFont("DejaVuBold", 6.5)
            c.setFillColor(data["color"])
            c.drawString(bx + 2 * MM, by + p_row_h - 4.5 * MM, "✂")

            # Header pill
            c.setFillColor(data["color"])
            c.roundRect(bx + 7 * MM, by + p_row_h - 5.5 * MM, p_col_w - 9 * MM, 4.5 * MM, 1.2 * MM, fill=True, stroke=False)
            c.setFont("DejaVuBold", 6)
            c.setFillColor(colors.white)
            c.drawCentredString(bx + 7 * MM + (p_col_w - 9 * MM) / 2.0, by + p_row_h - 2.5 * MM, f"PIEZA #{data['num']}")

            # Block image
            block_img_path = BLOCK_ASSETS[idx]
            if os.path.exists(block_img_path):
                img_w = p_col_w - 4 * MM
                img_h = p_row_h - 18 * MM
                c.drawImage(block_img_path, bx + 2 * MM, by + 12 * MM, width=img_w, height=img_h, preserveAspectRatio=True, mask='auto')

            # Tech label at bottom of piece
            c.setFont("DejaVuBold", 5.8)
            c.setFillColor(colors.HexColor("#0f172a"))
            c.drawString(bx + 2 * MM, by + 7 * MM, data["title"][:22])

            c.setFont("DejaVu", 5)
            c.setFillColor(colors.HexColor("#64748b"))
            c.drawString(bx + 2 * MM, by + 3 * MM, data["tech_spec"][:24])

            idx += 1

    # Footer
    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawCentredString(PAGE_W / 2.0, 8 * MM, "HPC&A Quantum Computing & Architecture • 100% 3D Printable Hardware Souvenirs")

    c.showPage()
    c.save()
    print(f"Generated: {output_path}")


# ==============================================================================
# 2. PASAPORTE CUÁNTICO AVANZADO (12 RETOS CIENTÍFICOS)
# ==============================================================================

def generate_qpu_passport_pdf(output_path: str):
    """Generates 1-page A4: 12-Challenge Quantum Hardware Passport & Stamp Sheet."""
    c = canvas.Canvas(output_path, pagesize=A4)

    draw_qpu_header(
        c,
        title="PASAPORTE CIENTÍFICO: 12 RETOS DEL PROCESADOR QPU",
        subtitle="Supera los 12 hitos de física cuántica y microelectrónica para ganar el Llavero 3D Real del Chip QPU",
        badge="PASAPORTE TÉCNICO DE LABORATORIO • EDICIÓN AVANZADA (12 BLOQUES)"
    )

    # Intro Box
    intro_y = PAGE_H - 55 * MM
    c.setFillColor(colors.HexColor("#f8fafc"))
    c.setStrokeColor(colors.HexColor("#cbd5e1"))
    c.roundRect(18 * MM, intro_y, PAGE_W - 36 * MM, 9 * MM, 2 * MM, fill=True, stroke=True)
    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#0369a1"))
    c.drawString(22 * MM, intro_y + 5 * MM, "REGISTRO DE EXPERIMENTACIÓN CUÁNTICA:")
    c.setFont("DejaVu", 7)
    c.setFillColor(colors.HexColor("#334155"))
    c.drawString(22 * MM, intro_y + 1.8 * MM, "Cada bloque corresponde a una etapa real del chip transmon superconductor. Resuelve el reto o escribe la respuesta para obtener tu sello.")

    # 12 Challenge Cards (3 columns x 4 rows)
    c_x0 = 18 * MM
    c_y0 = PAGE_H - 225 * MM
    c_col_w = (PAGE_W - 36 * MM - 4 * MM) / 3.0  # ~56.6 mm each
    c_row_h = 40 * MM

    for idx, data in enumerate(QPU_BLOCKS_DATA):
        col = idx % 3
        row = idx // 3
        bx = c_x0 + col * (c_col_w + 2 * MM)
        by = c_y0 + (3 - row) * (c_row_h + 2.5 * MM)

        # Card container
        c.setFillColor(colors.white)
        c.setStrokeColor(colors.HexColor("#cbd5e1"))
        c.setLineWidth(0.8)
        c.roundRect(bx, by, c_col_w, c_row_h, 2 * MM, fill=True, stroke=True)

        # Left color bar
        c.setFillColor(data["color"])
        c.roundRect(bx, by, 2.5 * MM, c_row_h, 1.2 * MM, fill=True, stroke=False)

        # Title
        c.setFont("DejaVuBold", 6.8)
        c.setFillColor(data["color"])
        c.drawString(bx + 4.5 * MM, by + c_row_h - 5 * MM, f"#{data['num']} {data['title'][:16]}")

        # Challenge question (2 lines)
        c.setFont("DejaVu", 5.6)
        c.setFillColor(colors.HexColor("#1e293b"))
        words = data["challenge"].split(" ")
        w_mid = len(words) // 2
        line1 = " ".join(words[:w_mid])
        line2 = " ".join(words[w_mid: w_mid * 2])
        line3 = " ".join(words[w_mid * 2:])
        c.drawString(bx + 4.5 * MM, by + c_row_h - 10 * MM, line1)
        c.drawString(bx + 4.5 * MM, by + c_row_h - 14 * MM, line2)
        if line3:
            c.drawString(bx + 4.5 * MM, by + c_row_h - 18 * MM, line3)

        # Tech Spec Badge
        c.setFont("DejaVuBold", 5.2)
        c.setFillColor(colors.HexColor("#64748b"))
        c.drawString(bx + 4.5 * MM, by + 9 * MM, f"▶ {data['tech_spec'][:22]}")

        # Stamp Circle
        stamp_cx = bx + c_col_w - 9 * MM
        stamp_cy = by + 9 * MM
        c.setStrokeColor(data["color"])
        c.setLineWidth(0.8)
        c.setDash(2, 2)
        c.circle(stamp_cx, stamp_cy, 6.5 * MM, fill=False, stroke=True)
        c.setDash()

        c.setFont("DejaVuBold", 5)
        c.setFillColor(data["color"])
        c.drawCentredString(stamp_cx, stamp_cy + 0.8 * MM, f"SELLO")
        c.drawCentredString(stamp_cx, stamp_cy - 2.2 * MM, f"#{data['num']}")

        # Mini block image thumbnail
        block_img_path = BLOCK_ASSETS[idx]
        if os.path.exists(block_img_path):
            c.drawImage(block_img_path, bx + 4.5 * MM, by + 1.5 * MM, width=12 * MM, height=7 * MM, preserveAspectRatio=True, mask='auto')

    # Bottom Tear-off Prize Voucher
    v_y = 10 * MM
    v_h = 30 * MM

    c.setStrokeColor(colors.HexColor("#f59e0b"))
    c.setLineWidth(1.0)
    c.setDash(4, 4)
    c.line(18 * MM, v_y + v_h + 3 * MM, PAGE_W - 18 * MM, v_y + v_h + 3 * MM)
    c.setDash()

    c.setFont("DejaVuBold", 7)
    c.setFillColor(colors.HexColor("#f59e0b"))
    c.drawString(18 * MM, v_y + v_h + 4.5 * MM, "✂ - - - - - CORTAR AQUÍ PARA CANJEAR EL PREMIO 3D EN EL STAND - - - - - ✂")

    c.setFillColor(colors.HexColor("#090d16"))
    c.roundRect(18 * MM, v_y, PAGE_W - 36 * MM, v_h, 3 * MM, fill=True, stroke=False)

    c.setStrokeColor(colors.HexColor("#f59e0b"))
    c.setLineWidth(1.0)
    c.roundRect(20 * MM, v_y + 2 * MM, PAGE_W - 40 * MM, v_h - 4 * MM, 2 * MM, fill=False, stroke=True)

    c.setFont("DejaVuBold", 9.5)
    c.setFillColor(colors.HexColor("#f59e0b"))
    c.drawString(25 * MM, v_y + v_h - 8.5 * MM, "★ VALE CIENTÍFICO: 1 LLAVERO 3D DE CHIP CUÁNTICO QPU ★")

    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawString(25 * MM, v_y + v_h - 14 * MM, "Certifica que los 12 hitos de arquitectura cuántica han sido completados con éxito.")
    c.drawString(25 * MM, v_y + v_h - 19 * MM, "Entregar en el stand de HPC&A para recibir el llavero superconductor 3D.")

    # Validation box
    c.setStrokeColor(colors.HexColor("#38bdf8"))
    c.roundRect(PAGE_W - 62 * MM, v_y + 4 * MM, 38 * MM, 21 * MM, 2 * MM, fill=False, stroke=True)
    c.setFont("DejaVuBold", 6.2)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawCentredString(PAGE_W - 43 * MM, v_y + 15 * MM, "SELLO DE ACREDITACIÓN")
    c.setFont("DejaVu", 5.8)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawCentredString(PAGE_W - 43 * MM, v_y + 8 * MM, "[ PREMIO ENTREGADO ]")

    c.showPage()
    c.save()
    print(f"Generated: {output_path}")


# ==============================================================================
# 3. ESQUEMA DE CIRCUITO CUÁNTICO DE 12 BLOQUES (BLUEPRINT & COLORING)
# ==============================================================================

def generate_qpu_blueprint_pdf(output_path: str):
    """Generates 1-page A4: 12-Zone Circuit Blueprint & Lineart Tracing."""
    c = canvas.Canvas(output_path, pagesize=A4)

    draw_qpu_header(
        c,
        title="ESQUEMÁTICO TÉCNICO: PROCESADOR CUÁNTICO (12 BLOQUES)",
        subtitle="Identifica y colorea las 12 zonas de microondas del chip para comprender la arquitectura cuántica",
        badge="ESQUEMÁTICO DE INGENIERÍA • BLUEPRINT TÉCNICO 12 ZONAS"
    )

    # Color code legend for 12 zones
    leg_y = PAGE_H - 68 * MM
    c.setFillColor(colors.HexColor("#090d16"))
    c.roundRect(18 * MM, leg_y, PAGE_W - 36 * MM, 20 * MM, 2 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 7.5)
    c.setFillColor(colors.HexColor("#f59e0b"))
    c.drawString(22 * MM, leg_y + 15 * MM, "GUÍA DE CODIFICACIÓN POR COLORES DEL HARDWARE:")

    # 12 Legend pills (6 on top row, 6 on bottom row)
    for i, data in enumerate(QPU_BLOCKS_DATA):
        col = i % 6
        row = i // 6
        lx = 22 * MM + col * ((PAGE_W - 44 * MM) / 6.0)
        ly = leg_y + 8.5 * MM - row * 6.5 * MM

        c.setFillColor(data["color"])
        c.circle(lx + 2.5 * MM, ly + 2 * MM, 2.5 * MM, fill=True, stroke=False)
        c.setFont("DejaVuBold", 6.5)
        c.setFillColor(colors.white)
        c.drawCentredString(lx + 2.5 * MM, ly + 0.8 * MM, str(data["num"]))

        c.setFont("DejaVu", 5.5)
        c.setFillColor(colors.HexColor("#cbd5e1"))
        c.drawString(lx + 6 * MM, ly + 1 * MM, data["title"][:11])

    # Central Blueprint Box
    art_y = PAGE_H - 225 * MM
    art_w = PAGE_W - 36 * MM
    art_h = 150 * MM

    c.setFillColor(colors.white)
    c.setStrokeColor(colors.HexColor("#0f172a"))
    c.setLineWidth(1.2)
    c.roundRect(18 * MM, art_y, art_w, art_h, 3 * MM, fill=True, stroke=True)

    if os.path.exists(ASSET_LINEART):
        img_w = art_w - 12 * MM
        img_h = art_h - 25 * MM
        c.drawImage(ASSET_LINEART, 24 * MM, art_y + 16 * MM, width=img_w, height=img_h, preserveAspectRatio=True, mask='auto')

    # Draw 12 Zone badges over blueprint
    dx = (art_w - 12 * MM) / 4.0
    dy = (art_h - 25 * MM) / 3.0
    b_idx = 1
    for r in range(3):
        for col in range(4):
            bx = 26 * MM + col * dx
            by = art_y + 16 * MM + (2 - r) * dy + dy - 9 * MM

            c.setFillColor(colors.HexColor("#0f172a"))
            c.circle(bx + 4 * MM, by + 3 * MM, 3.5 * MM, fill=True, stroke=False)
            c.setFont("DejaVuBold", 6.8)
            c.setFillColor(colors.white)
            c.drawCentredString(bx + 4 * MM, by + 1.2 * MM, str(b_idx))

            c.setFont("DejaVuBold", 5.5)
            c.setFillColor(colors.HexColor("#475569"))
            c.drawString(bx + 9 * MM, by + 1.8 * MM, QPU_BLOCKS_DATA[b_idx - 1]["title"][:13])

            b_idx += 1

    # Bottom Prize Claim Box
    bot_y = 10 * MM
    bot_h = 28 * MM
    c.setFillColor(colors.HexColor("#090d16"))
    c.roundRect(18 * MM, bot_y, PAGE_W - 36 * MM, bot_h, 3 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 9)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(24 * MM, bot_y + bot_h - 8 * MM, "¡COMPLETA EL TRAZADO DE LOS 12 BLOQUES Y CANJEA TU PREMIO!")

    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#e2e8f0"))
    c.drawString(24 * MM, bot_y + bot_h - 14 * MM, "Muestra tu blueprint completado para obtener el Llavero 3D Real del Chip Cuántico.")
    c.drawString(24 * MM, bot_y + bot_h - 19 * MM, "Diseñado por Nima • HPC&A Research Group • FDM 100% Sin Soportes")

    c.setFont("DejaVuBold", 10)
    c.setFillColor(colors.HexColor("#f59e0b"))
    c.drawString(24 * MM, bot_y + 3.5 * MM, "★★★★★ EXCELENCIA EN INGENIERÍA CUÁNTICA")

    c.setFont("DejaVu", 7.2)
    c.setFillColor(colors.white)
    c.drawString(PAGE_W - 85 * MM, bot_y + 5 * MM, "Firma del Docente: [                    ]")

    c.showPage()
    c.save()
    print(f"Generated: {output_path}")


# ==============================================================================
# 4. HOJA COMBINADA CUÁNTICA EXPRÉS (ALL-IN-ONE)
# ==============================================================================

def generate_qpu_combo_pdf(output_path: str):
    """Generates 1-page A4: Combo sheet with 12-block Master Grid + Quick Check-ins + Voucher."""
    c = canvas.Canvas(output_path, pagesize=A4)

    draw_qpu_header(
        c,
        title="DESAFÍO EXPRÉS: CHIP CUÁNTICO EN 12 BLOQUES",
        subtitle="Hoja todo-en-uno: analiza los 12 bloques y canjea tu Llavero 3D del procesador QPU",
        badge="EDICIÓN EXPRÉS A4 • DESAFÍO TÉCNICO 12 BLOQUES"
    )

    # Top Half: Master Grid with 12 Blocks Visual
    top_y = PAGE_H - 142 * MM
    if os.path.exists(ASSET_GRID_2D):
        img_w = PAGE_W - 36 * MM
        img_h = 80 * MM
        c.drawImage(ASSET_GRID_2D, 18 * MM, top_y + 4 * MM, width=img_w, height=img_h, preserveAspectRatio=True, mask='auto')

    # Middle: 12 Quick Check-in Badges (4 cols x 3 rows)
    q_y0 = PAGE_H - 225 * MM
    q_col_w = (PAGE_W - 36 * MM - 6 * MM) / 4.0
    q_card_h = 24 * MM

    for idx, data in enumerate(QPU_BLOCKS_DATA):
        col = idx % 4
        row = idx // 4
        bx = 18 * MM + col * (q_col_w + 2 * MM)
        by = q_y0 + (2 - row) * (q_card_h + 2.5 * MM)

        c.setFillColor(colors.HexColor("#f8fafc"))
        c.setStrokeColor(data["color"])
        c.setLineWidth(0.8)
        c.roundRect(bx, by, q_col_w, q_card_h, 2 * MM, fill=True, stroke=True)

        c.setFillColor(data["color"])
        c.roundRect(bx + 1.5 * MM, by + q_card_h - 5 * MM, q_col_w - 3 * MM, 4 * MM, 1 * MM, fill=True, stroke=False)
        c.setFont("DejaVuBold", 5.8)
        c.setFillColor(colors.white)
        c.drawCentredString(bx + q_col_w / 2.0, by + q_card_h - 3.2 * MM, f"#{data['num']} {data['title'][:11]}")

        c.setFont("DejaVu", 5)
        c.setFillColor(colors.HexColor("#475569"))
        c.drawString(bx + 2 * MM, by + q_card_h - 9 * MM, data["category"][:16])

        # Checkbox
        c.setStrokeColor(data["color"])
        c.setLineWidth(0.7)
        c.rect(bx + q_col_w - 9 * MM, by + 2 * MM, 7 * MM, 7 * MM, fill=False, stroke=True)
        c.setFont("DejaVuBold", 5.5)
        c.setFillColor(data["color"])
        c.drawCentredString(bx + q_col_w - 5.5 * MM, by + 4.5 * MM, "[✓]")

    # Bottom Half: Cut-off Claim Coupon
    v_y = 10 * MM
    v_h = 30 * MM

    c.setStrokeColor(colors.HexColor("#f59e0b"))
    c.setLineWidth(1.0)
    c.setDash(4, 4)
    c.line(18 * MM, v_y + v_h + 3 * MM, PAGE_W - 18 * MM, v_y + v_h + 3 * MM)
    c.setDash()

    c.setFont("DejaVuBold", 6.8)
    c.setFillColor(colors.HexColor("#f59e0b"))
    c.drawString(18 * MM, v_y + v_h + 4.5 * MM, "✂ - - - - - CORTAR Y CANJEAR POR 1 LLAVERO 3D DE CHIP CUÁNTICO QPU - - - - - ✂")

    c.setFillColor(colors.HexColor("#090d16"))
    c.roundRect(18 * MM, v_y, PAGE_W - 36 * MM, v_h, 3 * MM, fill=True, stroke=False)

    c.setFont("DejaVuBold", 9.5)
    c.setFillColor(colors.HexColor("#38bdf8"))
    c.drawString(24 * MM, v_y + v_h - 8.5 * MM, "VALE OFICIAL: 1 LLAVERO 3D SUPERCONDUCTOR QPU")

    c.setFont("DejaVu", 7.5)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    c.drawString(24 * MM, v_y + v_h - 14 * MM, "Acreditación de completitud de los 12 bloques del procesador cuántico.")
    c.drawString(24 * MM, v_y + v_h - 19 * MM, "HPC&A Research Group • High Performance Computing & Architecture")

    c.setFillColor(colors.HexColor("#f59e0b"))
    c.drawString(PAGE_W - 65 * MM, v_y + 11 * MM, "[ CANJEADO ]")

    c.showPage()
    c.save()
    print(f"Generated: {output_path}")


def main():
    print("Generating full Advanced 12-Block Quantum Suite...")

    puz_pdf = os.path.join(QPU_DIR, "tablero_cuantico_avanzado_12bloques_a4.pdf")
    pas_pdf = os.path.join(QPU_DIR, "pasaporte_cuantico_avanzado_12retos_a4.pdf")
    blu_pdf = os.path.join(QPU_DIR, "esquema_circuito_cuantico_12bloques_a4.pdf")
    com_pdf = os.path.join(QPU_DIR, "hoja_combinada_cuantica_expres_a4.pdf")

    generate_qpu_puzzle_board_pdf(puz_pdf)
    generate_qpu_passport_pdf(pas_pdf)
    generate_qpu_blueprint_pdf(blu_pdf)
    generate_qpu_combo_pdf(com_pdf)

    print("All 4 Advanced 12-Block PDFs generated successfully!")


if __name__ == "__main__":
    main()
