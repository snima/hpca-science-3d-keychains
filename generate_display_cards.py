#!/usr/bin/env python3
"""
GENERATE COMPANION DISPLAY CARDS IN SPANISH (A6, A7 & A4 MULTI-UP PRINT SHEETS)
================================================================================
Generates professional exhibition placards and tabletop companion cards in Spanish:
  1. cards_a6.pdf               - Standalone A6 placards (105 x 148 mm), 1 card/page
  2. cards_a7.pdf               - Compact A7 placards (74 x 105 mm), 1 card/page
  3. print_sheet_a6_on_a4.pdf   - A4 ready-to-print sheets (4x A6 cards/page with cut guides)
  4. print_sheet_a7_on_a4.pdf   - A4 ready-to-print sheets (8x A7 cards/page with cut guides)
  5. index.html                 - Web display dashboard & browser print with @media print
  6. cards_preview.png          - High-resolution visual showcase
"""

import os
import sys
from PIL import Image

import reportlab
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, A6, A7
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
CARDS_DIR = os.path.join(BASE_DIR, "display_cards")
os.makedirs(CARDS_DIR, exist_ok=True)

# Register Fonts for Unicode / Spanish accents
DEJAVU_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
DEJAVU_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

pdfmetrics.registerFont(TTFont("DejaVu", DEJAVU_REG))
pdfmetrics.registerFont(TTFont("DejaVuBold", DEJAVU_BOLD))

MM = 72.0 / 25.4  # Points per millimeter

# Comprehensive Metadata for All 9 Keychains in Spanish
CARDS_DATA = [
    {
        "id": "quantum_chandelier",
        "title_es": "Candelabro de Dilución Cuántica",
        "subtitle_en": "Quantum Dilution Chandelier — 15 mK Cryostat",
        "badge_es": "INSTRUMENTACIÓN CUÁNTICA",
        "badge_color": colors.HexColor("#b45309"),  # Ámbar / Oro
        "desc_es": "Los procesadores cuánticos superconductores deben operar a temperaturas cercanas al cero absoluto (15 milikelvin / -273.135 °C), un ambiente más frío que el espacio profundo, para mantener la coherencia cuántica. Este icónico candelabro dorado actúa como un escudo térmico multietapa, guiando cables coaxiales de microondas a través de 5 placas criogénicas hasta la cámara del procesador (QPU) en la base.",
        "dims": "31.2 × 61.7 × 4.4 mm",
        "weight": "~3.9 g PLA (~20 min)",
        "swap_z": "Z = 3.00 mm (Capa 16)",
        "support": "0% (Sin soportes)",
        "image": os.path.join(OUTPUT_DIR, "quantum_chandelier_render.png"),
    },
    {
        "id": "qpu_keychain_hpca",
        "title_es": "Chip Procesador Cuántico QPU",
        "subtitle_en": "Superconducting Transmon QPU Chip",
        "badge_es": "HARDWARE CUÁNTICO",
        "badge_color": colors.HexColor("#0284c7"),  # Azul / Cian
        "desc_es": "Un procesador cuántico moderno fabricado sobre sustrato de silicio de alta pureza. Incorpora cúbits superconductores tipo transmon con uniones Josephson de aluminio, resonadores coplanares en serpentín (CPW) para la lectura del estado cuántico y contactos periféricos de oro para el control mediante pulsos de microondas.",
        "dims": "56.7 × 36.0 × 3.9 mm",
        "weight": "~4.4 g PLA (~22 min)",
        "swap_z": "Z = 3.40 mm (Capa 18)",
        "support": "0% (Sin soportes)",
        "image": os.path.join(OUTPUT_DIR, "qpu_render_hero.png"),
    },
    {
        "id": "quantum_bloch",
        "title_es": "Medallón de la Esfera de Bloch",
        "subtitle_en": "Bloch Sphere Quantum Info Medallion",
        "badge_es": "INFORMACIÓN CUÁNTICA",
        "badge_color": colors.HexColor("#0d9488"),  # Turquesa
        "desc_es": "Representación geométrica fundamental del espacio de estados de un cúbit de dos niveles. El polo norte representa el estado |0>, el polo sur representa el |1>, y la superficie esférica describe estados de superposición continua |psi> = a|0> + b|1>, manipulados mediante puertas lógicas cuánticas.",
        "dims": "43.7 × 49.0 × 3.9 mm",
        "weight": "~3.4 g PLA (~18 min)",
        "swap_z": "Z = 3.40 mm (Capa 18)",
        "support": "0% (Sin soportes)",
        "image": os.path.join(OUTPUT_DIR, "quantum_bloch_render.png"),
    },
    {
        "id": "gpu_fantasy_chibi",
        "title_es": "Tarjeta Gráfica Chibi Animada",
        "subtitle_en": "Chibi Kawaii Anime GPU Keychain",
        "badge_es": "ARQUITECTURA FANTASÍA",
        "badge_color": colors.HexColor("#db2777"),  # Rosa
        "desc_es": "Reimagina una tarjeta gráfica de alto rendimiento bajo la estética lúdica de animación japonesa 'chibi'. Presenta un carenado curvado con un ventilador de pétalos centrado en una carita sonriente, botas redondeadas en lugar de conectores PCIe, rejillas de ventilación laterales y el emblema superior 'HPC&A'.",
        "dims": "55.2 × 34.4 × 4.3 mm",
        "weight": "~4.0 g PLA (~20 min)",
        "swap_z": "Z = 3.40 mm (Capa 18)",
        "support": "0% (Sin soportes)",
        "image": os.path.join(OUTPUT_DIR, "gpu_fantasy_chibi_render.png"),
    },
    {
        "id": "gpu_fantasy_mecha",
        "title_es": "GPU Caza Estelar Mecha",
        "subtitle_en": "Sci-Fi Mecha Starfighter GPU Keychain",
        "badge_es": "CIENCIA FICCIÓN AEROESPACIAL",
        "badge_color": colors.HexColor("#4f46e5"),  # Índigo
        "desc_es": "Interpretación aeroespacial futurista de un acelerador de cómputo extremo. Alerones estabilizadores transforman el disipador en una turbina supersónica scramjet con cono aerodinámico, flanqueada por una rejilla de radiador de plasma, placa blindada con grabado 'HPC&A' y doble tobera de propulsión iónica.",
        "dims": "63.4 × 29.9 × 4.4 mm",
        "weight": "~3.7 g PLA (~19 min)",
        "swap_z": "Z = 3.40 mm (Capa 18)",
        "support": "0% (Sin soportes)",
        "image": os.path.join(OUTPUT_DIR, "gpu_fantasy_mecha_render.png"),
    },
    {
        "id": "gpu_fantasy_rune",
        "title_es": "GPU Talismán Ciber-Rúnico",
        "subtitle_en": "Cyber-Runic Arcane GPU Talisman",
        "badge_es": "TECNO-HECHICERÍA",
        "badge_color": colors.HexColor("#9333ea"),  # Púrpura
        "desc_es": "Fusión mística entre forja rúnica ancestral y microelectrónica de silicio. Cuenta con un círculo de invocación arcano de 8 rayos, un cúmulo de cristales hexagonales de maná que emulan inductores de potencia, escudo heráldico protector y glifos rúnicos grabados sobre el chasis.",
        "dims": "64.7 × 28.5 × 4.4 mm",
        "weight": "~4.2 g PLA (~21 min)",
        "swap_z": "Z = 3.40 mm (Capa 18)",
        "support": "0% (Sin soportes)",
        "image": os.path.join(OUTPUT_DIR, "gpu_fantasy_rune_render.png"),
    },
    {
        "id": "cpu_fantasy_chibi",
        "title_es": "CPU Multinúcleo Heterogénea",
        "subtitle_en": "Heterogeneous Multi-Core CPU Keychain",
        "badge_es": "ARQUITECTURA DE SILICIO",
        "badge_color": colors.HexColor("#ea580c"),  # Naranja
        "desc_es": "Modelo a escala de la arquitectura asimétrica de los procesadores modernos. Incorpora dos grandes núcleos de alto rendimiento (P0, P1), un clúster de cuatro núcleos de alta eficiencia (E0-E3), memoria caché L3 compartida, difusor térmico integrado (IHS) de níquel grabado y contactos periféricos de soldadura.",
        "dims": "51.2 × 49.2 × 5.9 mm",
        "weight": "~4.8 g PLA (~24 min)",
        "swap_z": "Z = 3.40 mm (Capa 18)",
        "support": "0% (Sin soportes)",
        "image": os.path.join(OUTPUT_DIR, "cpu_render_isometric.png"),
    },
    {
        "id": "ram_ddr_hpca",
        "title_es": "Módulo de Memoria RAM DDR",
        "subtitle_en": "DDR5 High-Speed RAM Memory Stick",
        "badge_es": "ARQUITECTURA DE SILICIO",
        "badge_color": colors.HexColor("#16a34a"),  # Verde
        "desc_es": "Módulo miniatura de memoria RAM DDR para ordenador. Incorpora 8 paquetes de circuitos integrados (IC), pestaña inferior con contactos dorados y muesca polarizadora de alineación, perfil disipador térmico de aluminio con relieve 'HPC&A' y anilla para llavero.",
        "dims": "68.2 × 22.3 × 4.6 mm",
        "weight": "~3.6 g PLA (~18 min)",
        "swap_z": "Z = 3.40 mm (Capa 18)",
        "support": "0% (Sin soportes)",
        "image": os.path.join(OUTPUT_DIR, "ram_ddr_render.png"),
    },
    {
        "id": "gpu_spinning_body",
        "title_es": "GPU Cinética con Rotor Giratorio",
        "subtitle_en": "Kinetic Interactive Press-to-Spin Fan GPU",
        "badge_es": "INGENIERÍA CINÉTICA",
        "badge_color": colors.HexColor("#0891b2"),  # Cian / Azul
        "desc_es": "Llavero interactivo con rotor aerodinámico de 11 aspas que gira libremente al soplar o impulsarlo con los dedos. Emplea un eje flexible con ranura elástica y reborde de retención que se fija a presión tras la impresión, con holgura radial de baja fricción (0.22 mm) e impresión plana sin soportes.",
        "dims": "64.0 × 28.0 × 4.2 mm",
        "weight": "~4.5 g PLA (~22 min)",
        "swap_z": "Z = 3.40 mm (Capa 18)",
        "support": "0% (Sin soportes)",
        "image": os.path.join(OUTPUT_DIR, "spinning_fan_assembly_render.png"),
    },
]


def draw_card(c: canvas.Canvas, x: float, y: float, w: float, h: float, item: dict, is_compact: bool = False):
    """Draws a single high-aesthetic companion card in Spanish inside the rectangle (x, y, w, h)."""
    c.saveState()

    # Outer Border & Card Background
    card_bg = colors.HexColor("#0f172a")      # Slate 900
    border_col = colors.HexColor("#334155")   # Slate 700
    accent_col = item["badge_color"]

    c.setFillColor(card_bg)
    c.setStrokeColor(border_col)
    c.setLineWidth(1.0)
    c.roundRect(x, y, w, h, radius=4 * MM, fill=1, stroke=1)

    # Top Accent Stripe
    c.setFillColor(accent_col)
    c.roundRect(x + 1 * MM, y + h - 3.5 * MM, w - 2 * MM, 2.5 * MM, radius=1 * MM, fill=1, stroke=0)

    # Top Badge
    badge_text = item["badge_es"]
    badge_w = len(badge_text) * (1.5 * MM if is_compact else 1.9 * MM) + 6 * MM
    badge_h = 4.0 * MM if is_compact else 5.2 * MM
    badge_x = x + 5 * MM
    badge_y = y + h - (9 * MM if is_compact else 12 * MM)

    c.setFillColor(accent_col)
    c.roundRect(badge_x, badge_y, badge_w, badge_h, radius=1.5 * MM, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("DejaVuBold", 5.5 if is_compact else 7.0)
    c.drawString(badge_x + 3 * MM, badge_y + (1.2 * MM if is_compact else 1.6 * MM), badge_text)

    # Spanish Title
    title_y = badge_y - (5.0 * MM if is_compact else 6.5 * MM)
    c.setFont("DejaVuBold", 8.8 if is_compact else 12.2)
    c.setFillColor(colors.HexColor("#f8fafc"))
    c.drawString(x + 5 * MM, title_y, item["title_es"])

    # English Subtitle
    sub_title_y = title_y - (3.8 * MM if is_compact else 5.0 * MM)
    c.setFont("DejaVu", 6.0 if is_compact else 8.2)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawString(x + 5 * MM, sub_title_y, item["subtitle_en"])

    # 3D Render Image Frame
    img_pad = 4.5 * MM if is_compact else 6 * MM
    img_x = x + img_pad
    img_w = w - 2 * img_pad
    img_h = 24 * MM if is_compact else 42 * MM
    img_y = sub_title_y - img_h - (2.5 * MM if is_compact else 4.0 * MM)

    # Image frame background
    c.setFillColor(colors.HexColor("#020617"))  # Slate 950
    c.setStrokeColor(colors.HexColor("#1e293b"))
    c.roundRect(img_x, img_y, img_w, img_h, radius=2.5 * MM, fill=1, stroke=1)

    # Draw image if available
    img_path = item.get("image")
    if img_path and os.path.exists(img_path):
        try:
            c.drawImage(img_path, img_x + 1 * MM, img_y + 1 * MM, width=img_w - 2 * MM, height=img_h - 2 * MM, preserveAspectRatio=True, anchor='c')
        except Exception:
            pass

    # Spanish Scientific Narrative
    text_y = img_y - (3.5 * MM if is_compact else 4.5 * MM)
    words = item["desc_es"].split()
    lines = []
    cur_line = []
    max_chars = 44 if is_compact else 58
    for word in words:
        if sum(len(w) for w in cur_line) + len(cur_line) + len(word) <= max_chars:
            cur_line.append(word)
        else:
            lines.append(" ".join(cur_line))
            cur_line = [word]
    if cur_line:
        lines.append(" ".join(cur_line))

    font_sz = 4.7 if is_compact else 6.2
    line_spacing = 2.4 * MM if is_compact else 3.1 * MM
    c.setFont("DejaVu", font_sz)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    for i, line_str in enumerate(lines):
        c.drawString(x + 5 * MM, text_y - i * line_spacing, line_str)

    # Specifications Table in Spanish
    grid_y = y + (9.5 * MM if is_compact else 16 * MM)
    grid_h = 7.0 * MM if is_compact else 12 * MM
    grid_w = w - 10 * MM

    c.setFillColor(colors.HexColor("#1e293b"))
    c.setStrokeColor(colors.HexColor("#334155"))
    c.roundRect(x + 5 * MM, grid_y, grid_w, grid_h, radius=2 * MM, fill=1, stroke=1)

    col1_x = x + 7 * MM
    col2_x = x + grid_w / 2.0 + 3 * MM

    if is_compact:
        c.setFont("DejaVuBold", 4.5)
        c.setFillColor(colors.HexColor("#38bdf8"))
        c.drawString(col1_x, grid_y + 4.0 * MM, f"Dim: {item['dims']}")
        c.drawString(col2_x, grid_y + 4.0 * MM, f"Pausa: {item['swap_z']}")
        c.setFont("DejaVu", 4.2)
        c.setFillColor(colors.HexColor("#94a3b8"))
        c.drawString(col1_x, grid_y + 1.5 * MM, f"Peso: {item['weight']}")
        c.drawString(col2_x, grid_y + 1.5 * MM, f"Soportes: {item['support']}")
    else:
        c.setFont("DejaVuBold", 5.2)
        c.setFillColor(colors.HexColor("#38bdf8"))
        c.drawString(col1_x, grid_y + 7.5 * MM, f"Dim: {item['dims']}")
        c.drawString(col2_x, grid_y + 7.5 * MM, f"Pausa (M600): {item['swap_z']}")
        c.setFont("DejaVu", 5.0)
        c.setFillColor(colors.HexColor("#cbd5e1"))
        c.drawString(col1_x, grid_y + 2.5 * MM, f"Material: {item['weight']}")
        c.drawString(col2_x, grid_y + 2.5 * MM, f"Soportes: {item['support']}")

    # Footer Attribution
    footer_y = y + (3.0 * MM if is_compact else 5.5 * MM)
    c.setFont("DejaVuBold", 4.6 if is_compact else 6.5)
    c.setFillColor(colors.HexColor("#64748b"))
    c.drawString(x + 5 * MM, footer_y, "DISEÑADO POR NIMA | GRUPO HPC&A")

    c.setFont("DejaVu", 4.5 if is_compact else 6.5)
    c.drawRightString(x + w - 5 * MM, footer_y, "CC BY-NC-SA 4.0")

    c.restoreState()


def generate_a6_pdf():
    """Generates standalone A6 cards in Spanish (1 card per page)."""
    pdf_path = os.path.join(CARDS_DIR, "cards_a6.pdf")
    print(f"Generating Spanish A6 Display Cards PDF: {pdf_path}...")
    c = canvas.Canvas(pdf_path, pagesize=A6)
    w, h = A6
    margin = 5 * MM

    for item in CARDS_DATA:
        draw_card(c, margin, margin, w - 2 * margin, h - 2 * margin, item, is_compact=False)
        c.showPage()

    c.save()
    print("A6 PDF generated successfully.")


def generate_a7_pdf():
    """Generates standalone A7 mini placards in Spanish (1 card per page)."""
    pdf_path = os.path.join(CARDS_DIR, "cards_a7.pdf")
    print(f"Generating Spanish A7 Display Cards PDF: {pdf_path}...")
    c = canvas.Canvas(pdf_path, pagesize=A7)
    w, h = A7
    margin = 4 * MM

    for item in CARDS_DATA:
        draw_card(c, margin, margin, w - 2 * margin, h - 2 * margin, item, is_compact=True)
        c.showPage()

    c.save()
    print("A7 PDF generated successfully.")


def generate_a4_sheet_a6():
    """Generates ready-to-print A4 sheets with 4x A6 cards per page and cutting guidelines."""
    pdf_path = os.path.join(CARDS_DIR, "print_sheet_a6_on_a4.pdf")
    print(f"Generating Spanish A4 Print Sheet (4x A6 per page): {pdf_path}...")
    c = canvas.Canvas(pdf_path, pagesize=A4)
    page_w, page_h = A4

    card_w = 93 * MM
    card_h = 132 * MM
    margin_x = (page_w - 2 * card_w) / 3.0
    header_space = 14 * MM
    margin_y = (page_h - header_space - 2 * card_h) / 3.0

    positions = [
        (margin_x, margin_y + card_h + margin_y),                     # Top-Left
        (margin_x + card_w + margin_x, margin_y + card_h + margin_y), # Top-Right
        (margin_x, margin_y),                                         # Bottom-Left
        (margin_x + card_w + margin_x, margin_y),                     # Bottom-Right
    ]

    total_cards = len(CARDS_DATA)
    cards_per_page = 4
    num_pages = (total_cards + cards_per_page - 1) // cards_per_page

    for p in range(num_pages):
        c.saveState()
        c.setStrokeColor(colors.HexColor("#94a3b8"))
        c.setLineWidth(0.5)
        c.setDash(3, 3)
        c.line(page_w / 2.0, 10 * MM, page_w / 2.0, page_h - 14 * MM)
        c.line(10 * MM, (page_h - header_space) / 2.0, page_w - 10 * MM, (page_h - header_space) / 2.0)
        c.restoreState()

        batch = CARDS_DATA[p * cards_per_page : (p + 1) * cards_per_page]
        for idx, item in enumerate(batch):
            cx, cy = positions[idx]
            draw_card(c, cx, cy, card_w, card_h, item, is_compact=False)

        c.saveState()
        c.setFont("DejaVu", 6.8)
        c.setFillColor(colors.HexColor("#475569"))
        c.drawString(15 * MM, page_h - 7 * MM, f"Llaveros 3D HPC&A (A6 en A4) — Hoja {p+1}/{num_pages} — Cortar por líneas punteadas")
        c.drawRightString(page_w - 15 * MM, page_h - 7 * MM, "Diseñado por Nima | Pausa: Z = 3.40 mm")
        c.restoreState()

        c.showPage()

    c.save()
    print("A4 (A6 Multi-Up) PDF generated successfully.")


def generate_a4_sheet_a7():
    """Generates ready-to-print A4 sheets with 8x A7 cards per page and cutting guidelines."""
    pdf_path = os.path.join(CARDS_DIR, "print_sheet_a7_on_a4.pdf")
    print(f"Generating Spanish A4 Print Sheet (8x A7 per page): {pdf_path}...")
    c = canvas.Canvas(pdf_path, pagesize=A4)
    page_w, page_h = A4

    card_w = 66 * MM
    card_h = 92 * MM
    margin_x = (page_w - 2 * card_w) / 3.0
    header_space = 14 * MM
    margin_y = (page_h - header_space - 4 * card_h) / 5.0

    positions = []
    for r in range(4):
        for col in range(2):
            cx = margin_x + col * (card_w + margin_x)
            cy = page_h - header_space - (r + 1) * card_h - r * margin_y
            positions.append((cx, cy))

    total_cards = len(CARDS_DATA)
    cards_per_page = 8
    num_pages = (total_cards + cards_per_page - 1) // cards_per_page

    for p in range(num_pages):
        c.saveState()
        c.setStrokeColor(colors.HexColor("#94a3b8"))
        c.setLineWidth(0.5)
        c.setDash(3, 3)
        c.line(page_w / 2.0, 10 * MM, page_w / 2.0, page_h - 14 * MM)
        for r in range(1, 4):
            line_y = page_h - header_space - r * (card_h + margin_y) + margin_y / 2.0
            c.line(10 * MM, line_y, page_w - 10 * MM, line_y)
        c.restoreState()

        batch = CARDS_DATA[p * cards_per_page : (p + 1) * cards_per_page]
        for idx, item in enumerate(batch):
            cx, cy = positions[idx]
            draw_card(c, cx, cy, card_w, card_h, item, is_compact=True)

        c.saveState()
        c.setFont("DejaVu", 6.8)
        c.setFillColor(colors.HexColor("#475569"))
        c.drawString(15 * MM, page_h - 7 * MM, f"Llaveros 3D HPC&A (A7 Mini en A4) — Hoja {p+1}/{num_pages} — Cortar por líneas punteadas")
        c.drawRightString(page_w - 15 * MM, page_h - 7 * MM, "Diseñado por Nima | Pausa: Z = 3.40 mm")
        c.restoreState()

        c.showPage()

    c.save()
    print("A4 (A7 Multi-Up) PDF generated successfully.")


def generate_interactive_html():
    """Generates a responsive and browser-printable HTML document in Spanish."""
    html_path = os.path.join(CARDS_DIR, "index.html")
    print(f"Generating interactive & printable HTML in Spanish: {html_path}...")

    cards_html = ""
    for item in CARDS_DATA:
        badge_hex = item["badge_color"].hexval()[2:]
        rel_img = os.path.relpath(item["image"], CARDS_DIR)

        cards_html += f"""
        <div class="card" data-category="{item['badge_es']}">
            <div class="card-stripe" style="background-color: #{badge_hex};"></div>
            <div class="card-inner">
                <div class="card-header">
                    <span class="badge" style="background-color: #{badge_hex};">{item['badge_es']}</span>
                    <h2 class="title-es">{item['title_es']}</h2>
                    <h3 class="subtitle-en">{item['subtitle_en']}</h3>
                </div>

                <div class="img-box">
                    <img src="{rel_img}" alt="{item['title_es']}" loading="lazy" />
                </div>

                <div class="narrative">
                    <p class="desc-es">{item['desc_es']}</p>
                </div>

                <div class="specs-grid">
                    <div class="spec-item">
                        <span class="spec-label">DIMENSIONES</span>
                        <span class="spec-val">{item['dims']}</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">CAMBIO DE FILAMENTO</span>
                        <span class="spec-val highlight">{item['swap_z']}</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">PESO / TIEMPO</span>
                        <span class="spec-val">{item['weight']}</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">SOPORTES</span>
                        <span class="spec-val">{item['support']}</span>
                    </div>
                </div>

                <div class="card-footer">
                    <span class="author">DISEÑADO POR NIMA | HPC&A</span>
                    <span class="lic">CC BY-NC-SA 4.0</span>
                </div>
            </div>
        </div>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Llaveros 3D de Ciencia y Fantasía HPC&A — Tarjetas Informativas de Exposición</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #0b0f19;
            --surface-color: #0f172a;
            --border-color: #334155;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --text-muted: #64748b;
            --accent-blue: #38bdf8;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            padding: 24px;
            line-height: 1.5;
        }}

        .no-print {{
            max-width: 1240px;
            margin: 0 auto 32px auto;
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 20px 28px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 16px;
        }}

        .header-title h1 {{
            font-size: 20px;
            font-weight: 800;
            color: #fff;
            margin-bottom: 4px;
        }}

        .header-title p {{
            font-size: 13px;
            color: #94a3b8;
        }}

        .actions {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .btn {{
            background: #2563eb;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 13px;
            cursor: pointer;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
        }}

        .btn:hover {{
            background: #1d4ed8;
            transform: translateY(-1px);
        }}

        .btn-outline {{
            background: transparent;
            border: 1px solid #475569;
            color: #cbd5e1;
        }}

        .btn-outline:hover {{
            background: #334155;
            color: white;
        }}

        .grid-container {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
            gap: 28px;
            max-width: 1240px;
            margin: 0 auto;
            justify-items: center;
        }}

        .card {{
            width: 380px;
            min-height: 520px;
            background: var(--surface-color);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            position: relative;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
            page-break-inside: avoid;
            break-inside: avoid;
        }}

        .card-stripe {{
            height: 7px;
            width: 100%;
        }}

        .card-inner {{
            padding: 16px 20px 14px 20px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }}

        .badge {{
            display: inline-block;
            padding: 3px 8px;
            border-radius: 5px;
            font-size: 9px;
            font-weight: 700;
            letter-spacing: 0.5px;
            color: white;
            margin-bottom: 8px;
            text-transform: uppercase;
        }}

        .title-es {{
            font-size: 17px;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 2px;
            letter-spacing: -0.2px;
        }}

        .subtitle-en {{
            font-size: 11.5px;
            font-weight: 600;
            color: #94a3b8;
            margin-bottom: 12px;
        }}

        .img-box {{
            width: 100%;
            height: 160px;
            background: #020617;
            border: 1px solid #1e293b;
            border-radius: 9px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 12px;
            overflow: hidden;
        }}

        .img-box img {{
            max-width: 94%;
            max-height: 94%;
            object-fit: contain;
        }}

        .narrative {{
            margin-bottom: 14px;
            flex-grow: 1;
        }}

        .desc-es {{
            font-size: 11.5px;
            color: #cbd5e1;
            line-height: 1.5;
        }}

        .specs-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 7px;
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 8px;
            padding: 9px 12px;
            margin-bottom: 12px;
        }}

        .spec-item {{
            display: flex;
            flex-direction: column;
        }}

        .spec-label {{
            font-size: 8px;
            font-weight: 700;
            color: #94a3b8;
            letter-spacing: 0.5px;
        }}

        .spec-val {{
            font-size: 10.5px;
            font-family: 'Fira Code', monospace;
            font-weight: 600;
            color: #e2e8f0;
        }}

        .spec-val.highlight {{
            color: #38bdf8;
            font-weight: 700;
        }}

        .card-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid #1e293b;
            padding-top: 8px;
            font-size: 9px;
            color: #64748b;
            font-weight: 600;
        }}

        @media print {{
            body {{
                background: white !important;
                color: black !important;
                padding: 0 !important;
            }}

            .no-print {{
                display: none !important;
            }}

            .grid-container {{
                display: block !important;
            }}

            .card {{
                box-shadow: none !important;
                border: 1px solid #64748b !important;
                page-break-after: always;
                break-after: page;
                margin: 0 auto;
                width: 105mm !important;
                height: 148mm !important;
                max-width: 105mm !important;
                max-height: 148mm !important;
                padding: 0 !important;
            }}

            @page {{
                size: A6 portrait;
                margin: 0;
            }}
        }}
    </style>
</head>
<body>

    <div class="no-print">
        <div class="header-title">
            <h1>Llaveros 3D de Ciencia y Fantasía HPC&A — Tarjetas Informativas</h1>
            <p>Diseñado por Nima | Carteles de Mesa y Tarjetas de Exposición en Alta Resolución</p>
        </div>
        <div class="actions">
            <button class="btn" onclick="window.print()">🖨️ Imprimir (Ctrl+P)</button>
            <a href="cards_a6.pdf" class="btn btn-outline" download>📥 PDF A6 Individual</a>
            <a href="cards_a7.pdf" class="btn btn-outline" download>📥 PDF A7 Mini</a>
            <a href="print_sheet_a6_on_a4.pdf" class="btn btn-outline" download>📄 Hoja A4 (4x A6)</a>
            <a href="print_sheet_a7_on_a4.pdf" class="btn btn-outline" download>📄 Hoja A4 (8x A7)</a>
        </div>
    </div>

    <div class="grid-container">
        {cards_html}
    </div>

</body>
</html>
"""

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("HTML dashboard in Spanish generated successfully.")


def generate_preview_collage():
    """Generates a showcase preview collage image of the companion cards in Spanish."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    print("Generating visual preview collage of Spanish cards...")
    fig, axes = plt.subplots(3, 3, figsize=(18, 22), facecolor="#0b0f19")
    plt.subplots_adjust(wspace=0.15, hspace=0.25)

    fig.suptitle("LLAVEROS 3D HPC&A — TARJETAS INFORMATIVAS DE EXPOSICIÓN\nFormato A6 / A7 Listo para Imprimir (Diseñado por Nima)", 
                 fontsize=18, fontweight='bold', color="#f8fafc", y=0.96)

    for idx, item in enumerate(CARDS_DATA):
        r, col = idx // 3, idx % 3
        ax = axes[r, col]
        ax.set_facecolor("#0f172a")

        img_p = item.get("image")
        if img_p and os.path.exists(img_p):
            img = mpimg.imread(img_p)
            ax.imshow(img)
        ax.axis('off')

        badge = item['badge_es']
        title = item['title_es']
        swap = item['swap_z']
        dims = item['dims']

        ax.set_title(f"[{badge}]\n{title}\n{dims} | Pausa: {swap}", 
                     fontsize=11, fontweight='bold', color="#38bdf8", pad=8)

    preview_path = os.path.join(CARDS_DIR, "cards_preview.png")
    plt.savefig(preview_path, facecolor="#0b0f19", bbox_inches='tight', dpi=160)
    plt.close()
    print(f"Cards preview collage saved: {preview_path}")


def main():
    print("==================================================================")
    print("Generando Tarjetas de Exposición en Español (A6, A7, A4)...")
    print("==================================================================")
    generate_a6_pdf()
    generate_a7_pdf()
    generate_a4_sheet_a6()
    generate_a4_sheet_a7()
    generate_interactive_html()
    generate_preview_collage()
    print("\n¡Todos los formatos de tarjetas en español generados con éxito en display_cards/!")


if __name__ == "__main__":
    main()
