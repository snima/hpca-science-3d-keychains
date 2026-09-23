#!/usr/bin/env python3
"""
GENERATE COMPANION DISPLAY CARDS (A6, A7 & A4 MULTI-UP PRINT SHEETS)
===================================================================
Produces exhibition placards and tabletop companion cards for all keychains:
  1. cards_a6.pdf               - Standalone A6 placards (105 x 148 mm), 1 card/page
  2. cards_a7.pdf               - Compact A7 placards (74 x 105 mm), 1 card/page
  3. print_sheet_a6_on_a4.pdf   - A4 ready-to-print sheets (4x A6 cards/page with cut guides)
  4. print_sheet_a7_on_a4.pdf   - A4 ready-to-print sheets (8x A7 cards/page with cut guides)
  5. index.html                 - Web display dashboard & browser print with @media print
  6. cards_preview.png          - High-resolution visual showcase
"""

import os
import sys
import arabic_reshaper
from bidi.algorithm import get_display
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

# Register Fonts
ARABIC_REG = "/usr/share/fonts/truetype/noto/NotoSansArabic-Regular.ttf"
ARABIC_BOLD = "/usr/share/fonts/truetype/noto/NotoSansArabic-Bold.ttf"

pdfmetrics.registerFont(TTFont("NotoArabic", ARABIC_REG))
pdfmetrics.registerFont(TTFont("NotoArabicBold", ARABIC_BOLD))

MM = 72.0 / 25.4  # Points per millimeter


def fa(text: str) -> str:
    """Reshape and reorder Persian/Arabic text for correct right-to-left rendering."""
    if not text:
        return ""
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)


# Comprehensive Metadata for All 9 Keychains
CARDS_DATA = [
    {
        "id": "quantum_chandelier",
        "title_en": "Quantum Dilution Chandelier",
        "title_fa": "لوستر برودتی رقت کوانتومی",
        "badge_en": "QUANTUM INSTRUMENTATION",
        "badge_color": colors.HexColor("#b45309"),  # Amber / Gold
        "subtitle_en": "15 mK Dilution Cryostat & QPU Shield",
        "subtitle_fa": "کرایواستات برودتی ۱۵ میلی‌کلوین و محفظه پردازنده",
        "desc_en": "Superconducting quantum processors must operate at near absolute zero (15 mK / -273.135°C), colder than deep space, to maintain quantum coherence. This iconic golden chandelier acts as a multi-stage thermal shield, routing coaxial microwave lines through 5 cryogenic plates down to the quantum processor (QPU) can at the bottom.",
        "desc_fa": "پردازنده‌های کوانتومی ابررسانا برای حفظ همدوسی باید در دمای ۱۵ میلی‌کلوین (نزدیک به صفر مطلق و سردتر از فضای کیهانی) کار کنند. این لوستر طلایی نمادین با ۵ طبقه حرارتی، کابل‌های مایکروویو را تا محفظه شیلد QPU در پایین‌ترین طبقه هدایت می‌کند.",
        "dims": "31.2 × 61.7 × 4.4 mm",
        "weight": "~3.9 g PLA (~20 min)",
        "swap_z": "Z = 3.00 mm (Layer 16)",
        "support": "0% (None)",
        "image": os.path.join(OUTPUT_DIR, "quantum_chandelier_render.png"),
    },
    {
        "id": "qpu_keychain_hpca",
        "title_en": "Superconducting QPU Chip",
        "title_fa": "تراشه پردازش کوانتومی ابررسانا",
        "badge_en": "QUANTUM HARDWARE",
        "badge_color": colors.HexColor("#0284c7"),  # Blue / Cyan
        "subtitle_en": "Transmon Qubits & CPW Resonators",
        "subtitle_fa": "آرایه کیوبیت‌های ترانزمون و رزوناتورهای موج‌بر",
        "desc_en": "A modern quantum processor unit (QPU) fabricated on high-purity silicon. Features superconducting aluminum transmon qubits with Josephson junctions, serpentine coplanar waveguide (CPW) readout resonators, and peripheral wirebond gold pads for microwave control pulses.",
        "desc_fa": "پردازنده کوانتومی مدرن ساخته‌شده بر پایه ویفر سیلیکونی با خلوص بالا. شامل کیوبیت‌های ترانزمون پیوند جوزفسون، موج‌برهای مارپیچی هم‌صفحه (CPW) برای بازخوانی و پدهای پیرامونی اتصال طلا برای امواج کنترلی.",
        "dims": "56.7 × 36.0 × 3.9 mm",
        "weight": "~4.4 g PLA (~22 min)",
        "swap_z": "Z = 3.40 mm (Layer 18)",
        "support": "0% (None)",
        "image": os.path.join(OUTPUT_DIR, "qpu_render_hero.png"),
    },
    {
        "id": "quantum_bloch",
        "title_en": "Bloch Sphere Quantum Medallion",
        "title_fa": "مدالیون کوانتومی کره بلاخ",
        "badge_en": "QUANTUM INFORMATION",
        "badge_color": colors.HexColor("#0d9488"),  # Teal
        "subtitle_en": "Single-Qubit State Space |psi>",
        "subtitle_fa": "فضای هندسی حالت برهم‌نهی کیوبیت",
        "desc_en": "The fundamental geometric representation of a pure two-level quantum system (qubit). The north pole represents |0>, south pole represents |1>, and points on the spherical surface represent arbitrary quantum superpositions |psi> = α|0> + β|1>, manipulated via quantum logic gates.",
        "desc_fa": "نمایش هندسی بنیادین حالت یک کیوبیت کوانتومی. قطب شمال معرف حالت پایه |0>، قطب جنوب |1> و هر نقطه روی پوسته کروی معرف برهم‌نهی کوانتومی |psi> است که با اعمال گیت‌های منطقی دوران می‌یابد.",
        "dims": "43.7 × 49.0 × 3.9 mm",
        "weight": "~3.4 g PLA (~18 min)",
        "swap_z": "Z = 3.40 mm (Layer 18)",
        "support": "0% (None)",
        "image": os.path.join(OUTPUT_DIR, "quantum_bloch_render.png"),
    },
    {
        "id": "gpu_fantasy_chibi",
        "title_en": "Chibi Anime GPU Keychain",
        "title_fa": "کارت گرافیک فانتزی چیبی",
        "badge_en": "FANTASY ARCHITECTURE",
        "badge_color": colors.HexColor("#db2777"),  # Pink / Rose
        "subtitle_en": "Playful Anime Character Graphics Card",
        "subtitle_fa": "کارت گرافیک مینیاتوری سبک کاراکتر ژاپنی",
        "desc_en": "Reimagines high-performance computer graphics in a playful Japanese chibi aesthetic. Features a curved shroud with smiling anime face hub, petal fan blades, cute rounded feet replacing PCIe fingers, side cooling pill-vents, and a curved 'HPC&A' banner.",
        "desc_fa": "بازآفرینی هنری و شاداب کارت گرافیک در قالب کاراکتر چیبی ژاپنی. دارای بدنه بالشتکی با هاب فن خندان، پره‌های گلبرگی، پایه‌های کفشی گرد به جای پین‌های PCIe، منافذ جانبی قرصی‌شکل و نشان بالایی HPC&A.",
        "dims": "55.2 × 34.4 × 4.3 mm",
        "weight": "~4.0 g PLA (~20 min)",
        "swap_z": "Z = 3.40 mm (Layer 18)",
        "support": "0% (None)",
        "image": os.path.join(OUTPUT_DIR, "gpu_fantasy_chibi_render.png"),
    },
    {
        "id": "gpu_fantasy_mecha",
        "title_en": "Sci-Fi Mecha Starfighter GPU",
        "title_fa": "کارت گرافیک سفینه فضایی مکا",
        "badge_en": "AEROSPACE SCI-FI",
        "badge_color": colors.HexColor("#4f46e5"),  # Indigo
        "subtitle_en": "Supersonic Scramjet Turbine GPU",
        "subtitle_fa": "سفینه رهگیر مافوق‌صوت با توربین اگزوز رانشگر",
        "desc_en": "Futuristic aerospace interpretation of an extreme accelerator card. Swept-back stabilizer winglets transform the cooling fan into a supersonic scramjet turbine with bullet nose cone, flanked by a 7-slat plasma radiator grille, armored 'HPC&A' nameplate, and twin thrusters.",
        "desc_fa": "تلفیق آینده‌نگرانه کارت گرافیک با جنگنده رهگیر فضایی. بال‌های پس‌گرا توربین خنک‌کننده را به موتور جت مافوق‌صوت با دماغه مخروطی بدل کرده و در کنار رادیاتور پلاسمایی و پلاک زرهی HPC&A قرار گرفته است.",
        "dims": "63.4 × 29.9 × 4.4 mm",
        "weight": "~3.7 g PLA (~19 min)",
        "swap_z": "Z = 3.40 mm (Layer 18)",
        "support": "0% (None)",
        "image": os.path.join(OUTPUT_DIR, "gpu_fantasy_mecha_render.png"),
    },
    {
        "id": "gpu_fantasy_rune",
        "title_en": "Cyber-Runic Arcane GPU",
        "title_fa": "کارت گرافیک تالیسمان سایبر-رونیک",
        "badge_en": "TECHNO-SORCERY",
        "badge_color": colors.HexColor("#9333ea"),  # Purple
        "subtitle_en": "Alchemical Talisman & Mana Crystals",
        "subtitle_fa": "لوح جادویی کیمیاگری و کریستال‌های مانا",
        "desc_en": "Blends ancient dwarven runecraft with advanced silicon electronics. Features an 8-spoke arcane summoning circle, hexagonal glowing mana crystal cluster acting as power delivery inductors, heraldic shield crest, and etched runic protection glyphs.",
        "desc_fa": "آمیزه‌ای از جادوی باستانی و مدارات الکترونیک سیلیکونی. شامل دایره احضار ۸ وجهی، خوشه‌ای از کریستال‌های شش‌ضلعی مانا به عنوان چوک‌های تغذیه برق، نشان سپر سلطنتی و خطوط رمزآلود باستانی.",
        "dims": "64.7 × 28.5 × 4.4 mm",
        "weight": "~4.2 g PLA (~21 min)",
        "swap_z": "Z = 3.40 mm (Layer 18)",
        "support": "0% (None)",
        "image": os.path.join(OUTPUT_DIR, "gpu_fantasy_rune_render.png"),
    },
    {
        "id": "cpu_fantasy_chibi",
        "title_en": "Heterogeneous Multi-Core CPU",
        "title_fa": "پردازنده چندهسته‌ای ناهمگن",
        "badge_en": "SILICON ARCHITECTURE",
        "badge_color": colors.HexColor("#ea580c"),  # Orange
        "subtitle_en": "Big.LITTLE Core Dies & Nickel IHS",
        "subtitle_fa": "پردازنده مدرن با هسته‌های قدرتی، کم‌مصرف و کش L3",
        "desc_en": "Realistic scale model of modern asymmetric multi-core processors. Features two large high-performance cores (P0, P1), a quad-core efficiency cluster (E0-E3), unified L3 cache die, etched nickel integrated heat spreader (IHS), and gold edge solder pads.",
        "desc_fa": "مدل دقیق معماری پردازنده‌های ناهمگن مدرن. شامل ۲ هسته پرقدرت محاسباتی (P-Cores)، کلاستر ۴ هسته‌ای کم‌مصرف (E-Cores)، کش اشتراکی سطح ۳، درپوش فلزی خنک‌کننده (IHS) و پدهای لحیم پیرامونی.",
        "dims": "51.2 × 49.2 × 5.9 mm",
        "weight": "~4.8 g PLA (~24 min)",
        "swap_z": "Z = 3.40 mm (Layer 18)",
        "support": "0% (None)",
        "image": os.path.join(OUTPUT_DIR, "cpu_render_isometric.png"),
    },
    {
        "id": "ram_ddr_hpca",
        "title_en": "DDR RAM Memory Module",
        "title_fa": "ماژول حافظه رم DDR کامپیوتر",
        "badge_en": "SILICON ARCHITECTURE",
        "badge_color": colors.HexColor("#16a34a"),  # Green
        "subtitle_en": "DDR5 Desktop Memory Stick & Spreader",
        "subtitle_fa": "ماژول حافظه رم پرسرعت با پین‌های طلایی و هیت‌سینک",
        "desc_en": "Miniature desktop DDR memory module featuring 8 integrated memory IC packages, precision gold-finger edge connector tab with polarizing alignment notch, top aluminum thermal spreader fin rail with debossed 'HPC&A', and corner eyelet.",
        "desc_fa": "ماژول مینیاتوری حافظه رم DDR دسکتاپ. شامل ۸ پکیج آی‌سی حافظه، پین‌های طلایی اسلات همراه با شیار کلیدی موقعیت‌دهی، شانه هیت‌سینک آلومینیومی با نشان برجسته HPC&A و حلقه آویز.",
        "dims": "68.2 × 22.3 × 4.6 mm",
        "weight": "~3.6 g PLA (~18 min)",
        "swap_z": "Z = 3.40 mm (Layer 18)",
        "support": "0% (None)",
        "image": os.path.join(OUTPUT_DIR, "ram_ddr_render.png"),
    },
    {
        "id": "gpu_spinning_body",
        "title_en": "Kinetic Spinning Fan GPU",
        "title_fa": "کارت گرافیک تعاملی فن چرخان",
        "badge_en": "KINETIC ENGINEERING",
        "badge_color": colors.HexColor("#0891b2"),  # Cyan/Blue
        "subtitle_en": "Press-to-Spin Aerodynamic Impeller Kit",
        "subtitle_fa": "جاکلیدی مکانیکی تعاملی با فن قابل چرخش با انگشت",
        "desc_en": "Interactive 3D print featuring snap-fit 11-blade impellers that spin freely when flicked. Utilizes compliant cantilever spindle axle pins with retention lips and 0.22 mm low-friction radial clearances, printing 100% support-free flat on the build plate.",
        "desc_fa": "جاکلیدی مکانیکی تعاملی مجهز به پروانه‌های ۱۱ پره با چرخش روان و بی‌اصطکاک. دارای پین‌های ارتجاعی چفت‌شونده (Snap-fit) با تلرانس ۰.۲۲ میلی‌متر، با قابلیت چاپ کاملاً مسطح و بدون نیاز به ساپورت.",
        "dims": "64.0 × 28.0 × 4.2 mm",
        "weight": "~4.5 g PLA (~22 min)",
        "swap_z": "Z = 3.40 mm (Layer 18)",
        "support": "0% (None)",
        "image": os.path.join(OUTPUT_DIR, "spinning_fan_assembly_render.png"),
    },
]


def draw_card(c: canvas.Canvas, x: float, y: float, w: float, h: float, item: dict, is_compact: bool = False):
    """Draws a single high-aesthetic companion card inside the rectangle (x, y, w, h)."""
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
    badge_text = item["badge_en"]
    badge_w = len(badge_text) * (1.6 * MM if is_compact else 2.1 * MM) + 6 * MM
    badge_h = 4.0 * MM if is_compact else 5.2 * MM
    badge_x = x + 5 * MM
    badge_y = y + h - (9 * MM if is_compact else 12 * MM)

    c.setFillColor(accent_col)
    c.roundRect(badge_x, badge_y, badge_w, badge_h, radius=1.5 * MM, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 6.0 if is_compact else 7.5)
    c.drawString(badge_x + 3 * MM, badge_y + (1.2 * MM if is_compact else 1.6 * MM), badge_text)

    # English Title
    title_y = badge_y - (5.0 * MM if is_compact else 6.5 * MM)
    c.setFont("Helvetica-Bold", 9.5 if is_compact else 13.0)
    c.setFillColor(colors.HexColor("#f8fafc"))
    c.drawString(x + 5 * MM, title_y, item["title_en"])

    # Persian Title
    fa_title_y = title_y - (4.2 * MM if is_compact else 5.5 * MM)
    c.setFont("NotoArabicBold", 8.0 if is_compact else 10.5)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawRightString(x + w - 5 * MM, fa_title_y, fa(item["title_fa"]))

    # 3D Render Image Frame
    img_pad = 4.5 * MM if is_compact else 6 * MM
    img_x = x + img_pad
    img_w = w - 2 * img_pad
    img_h = 24 * MM if is_compact else 42 * MM
    img_y = fa_title_y - img_h - (2.5 * MM if is_compact else 4.0 * MM)

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

    # Scientific Narrative (English & Persian)
    text_y = img_y - (3.5 * MM if is_compact else 4.5 * MM)
    
    # English description (word wrap)
    c.setFont("Helvetica", 5.2 if is_compact else 7.2)
    c.setFillColor(colors.HexColor("#cbd5e1"))
    
    words = item["desc_en"].split()
    lines = []
    cur_line = []
    max_chars = 48 if is_compact else 65
    for word in words:
        if sum(len(w) for w in cur_line) + len(cur_line) + len(word) <= max_chars:
            cur_line.append(word)
        else:
            lines.append(" ".join(cur_line))
            cur_line = [word]
    if cur_line:
        lines.append(" ".join(cur_line))
    
    en_line_count = 3 if is_compact else 4
    for i, line_str in enumerate(lines[:en_line_count]):
        c.drawString(x + 5 * MM, text_y - i * (2.8 * MM if is_compact else 3.6 * MM), line_str)

    # Persian description
    fa_start_y = text_y - en_line_count * (2.8 * MM if is_compact else 3.6 * MM) - (1.0 * MM if is_compact else 2.0 * MM)
    c.setFont("NotoArabic", 5.2 if is_compact else 7.0)
    c.setFillColor(colors.HexColor("#94a3b8"))
    
    fa_words = item["desc_fa"].split()
    fa_lines = []
    fa_cur = []
    fa_max_chars = 44 if is_compact else 60
    for word in fa_words:
        if sum(len(w) for w in fa_cur) + len(fa_cur) + len(word) <= fa_max_chars:
            fa_cur.append(word)
        else:
            fa_lines.append(" ".join(fa_cur))
            fa_cur = [word]
    if fa_cur:
        fa_lines.append(" ".join(fa_cur))
    
    fa_line_count = 2 if is_compact else 3
    for i, f_line in enumerate(fa_lines[:fa_line_count]):
        c.drawRightString(x + w - 5 * MM, fa_start_y - i * (3.0 * MM if is_compact else 3.8 * MM), fa(f_line))

    # Specifications Table / Pill Grid
    grid_y = y + (9.5 * MM if is_compact else 16 * MM)
    grid_h = 7.0 * MM if is_compact else 12 * MM
    grid_w = w - 10 * MM
    
    c.setFillColor(colors.HexColor("#1e293b"))
    c.setStrokeColor(colors.HexColor("#334155"))
    c.roundRect(x + 5 * MM, grid_y, grid_w, grid_h, radius=2 * MM, fill=1, stroke=1)
    
    # Specs Items
    c.setFont("Helvetica-Bold", 5.0 if is_compact else 6.8)
    c.setFillColor(colors.HexColor("#38bdf8"))  # Sky blue
    
    col1_x = x + 7 * MM
    col2_x = x + grid_w / 2.0 + 3 * MM
    
    if is_compact:
        c.drawString(col1_x, grid_y + 4.0 * MM, f"Dims: {item['dims']}")
        c.drawString(col2_x, grid_y + 4.0 * MM, f"Pause: {item['swap_z']}")
        c.setFont("Helvetica", 4.8)
        c.setFillColor(colors.HexColor("#94a3b8"))
        c.drawString(col1_x, grid_y + 1.5 * MM, f"Weight: {item['weight']}")
        c.drawString(col2_x, grid_y + 1.5 * MM, f"Support: {item['support']}")
    else:
        c.setFont("Helvetica-Bold", 6.0)
        c.drawString(col1_x, grid_y + 7.5 * MM, f"Dims: {item['dims']}")
        c.drawString(col2_x, grid_y + 7.5 * MM, f"Swap (M600): {item['swap_z']}")
        c.setFont("Helvetica", 5.8)
        c.setFillColor(colors.HexColor("#cbd5e1"))
        c.drawString(col1_x, grid_y + 2.5 * MM, f"Material: {item['weight']}")
        c.drawString(col2_x, grid_y + 2.5 * MM, f"Support: {item['support']}")

    # Footer Attribution
    footer_y = y + (3.0 * MM if is_compact else 5.5 * MM)
    c.setFont("Helvetica-Bold", 5.0 if is_compact else 7.0)
    c.setFillColor(colors.HexColor("#64748b"))
    c.drawString(x + 5 * MM, footer_y, "DESIGNED BY NIMA | HPC&A RESEARCH GROUP")
    
    c.setFont("Helvetica", 4.5 if is_compact else 6.5)
    c.drawRightString(x + w - 5 * MM, footer_y, "CC BY-NC-SA 4.0")

    c.restoreState()


def generate_a6_pdf():
    """Generates standalone A6 cards (1 card per page)."""
    pdf_path = os.path.join(CARDS_DIR, "cards_a6.pdf")
    print(f"Generating A6 Display Cards PDF: {pdf_path}...")
    c = canvas.Canvas(pdf_path, pagesize=A6)
    w, h = A6
    margin = 5 * MM

    for item in CARDS_DATA:
        draw_card(c, margin, margin, w - 2 * margin, h - 2 * margin, item, is_compact=False)
        c.showPage()

    c.save()
    print("A6 PDF generated successfully.")


def generate_a7_pdf():
    """Generates standalone A7 mini placards (1 card per page)."""
    pdf_path = os.path.join(CARDS_DIR, "cards_a7.pdf")
    print(f"Generating A7 Display Cards PDF: {pdf_path}...")
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
    print(f"Generating A4 Print Sheet (4x A6 per page): {pdf_path}...")
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
        c.setFont("Helvetica", 7.0)
        c.setFillColor(colors.HexColor("#475569"))
        c.drawString(15 * MM, page_h - 7 * MM, f"HPC&A 3D Keychains Companion Cards (A6 on A4) — Sheet {p+1}/{num_pages} — Cut along dashed lines")
        c.drawRightString(page_w - 15 * MM, page_h - 7 * MM, "Designed by Nima | Slicer Pause: Z = 3.40 mm")
        c.restoreState()

        c.showPage()

    c.save()
    print("A4 (A6 Multi-Up) PDF generated successfully.")


def generate_a4_sheet_a7():
    """Generates ready-to-print A4 sheets with 8x A7 cards per page and cutting guidelines."""
    pdf_path = os.path.join(CARDS_DIR, "print_sheet_a7_on_a4.pdf")
    print(f"Generating A4 Print Sheet (8x A7 per page): {pdf_path}...")
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
        c.setFont("Helvetica", 7.0)
        c.setFillColor(colors.HexColor("#475569"))
        c.drawString(15 * MM, page_h - 7 * MM, f"HPC&A 3D Keychains Companion Cards (A7 Mini on A4) — Sheet {p+1}/{num_pages} — Cut along dashed lines")
        c.drawRightString(page_w - 15 * MM, page_h - 7 * MM, "Designed by Nima | Slicer Pause: Z = 3.40 mm")
        c.restoreState()

        c.showPage()

    c.save()
    print("A4 (A7 Multi-Up) PDF generated successfully.")


def generate_interactive_html():
    """Generates a responsive and browser-printable HTML document with @media print rules."""
    html_path = os.path.join(CARDS_DIR, "index.html")
    print(f"Generating interactive & printable HTML: {html_path}...")

    cards_html = ""
    for item in CARDS_DATA:
        badge_hex = item["badge_color"].hexval()[2:]
        rel_img = os.path.relpath(item["image"], CARDS_DIR)

        cards_html += f"""
        <div class="card" data-category="{item['badge_en']}">
            <div class="card-stripe" style="background-color: #{badge_hex};"></div>
            <div class="card-inner">
                <div class="card-header">
                    <span class="badge" style="background-color: #{badge_hex};">{item['badge_en']}</span>
                    <h2 class="title-en">{item['title_en']}</h2>
                    <h3 class="title-fa" dir="rtl">{item['title_fa']}</h3>
                </div>

                <div class="img-box">
                    <img src="{rel_img}" alt="{item['title_en']}" loading="lazy" />
                </div>

                <div class="narrative">
                    <p class="desc-en">{item['desc_en']}</p>
                    <p class="desc-fa" dir="rtl">{item['desc_fa']}</p>
                </div>

                <div class="specs-grid">
                    <div class="spec-item">
                        <span class="spec-label">DIMENSIONS</span>
                        <span class="spec-val">{item['dims']}</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">FILAMENT SWAP</span>
                        <span class="spec-val highlight">{item['swap_z']}</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">WEIGHT / TIME</span>
                        <span class="spec-val">{item['weight']}</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">SUPPORT NEEDED</span>
                        <span class="spec-val">{item['support']}</span>
                    </div>
                </div>

                <div class="card-footer">
                    <span class="author">DESIGNED BY NIMA | HPC&A</span>
                    <span class="lic">CC BY-NC-SA 4.0</span>
                </div>
            </div>
        </div>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HPC&A Science & Fantasy 3D Keychains — Companion Display Cards</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Inter:wght@400;600;700;800&family=Vazirmatn:wght@400;600;700;800&display=swap" rel="stylesheet">
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
            min-height: 540px;
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

        .title-en {{
            font-size: 16.5px;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 2px;
            letter-spacing: -0.2px;
        }}

        .title-fa {{
            font-family: 'Vazirmatn', sans-serif;
            font-size: 13px;
            font-weight: 700;
            color: #94a3b8;
            margin-bottom: 12px;
        }}

        .img-box {{
            width: 100%;
            height: 155px;
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
            margin-bottom: 12px;
            flex-grow: 1;
        }}

        .desc-en {{
            font-size: 11px;
            color: #cbd5e1;
            line-height: 1.45;
            margin-bottom: 8px;
        }}

        .desc-fa {{
            font-family: 'Vazirmatn', sans-serif;
            font-size: 10.5px;
            color: #94a3b8;
            line-height: 1.5;
            border-top: 1px dashed #334155;
            padding-top: 6px;
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
            <h1>HPC&A Science & Fantasy 3D Keychains — Companion Cards</h1>
            <p>Designed by Nima | High-Resolution Tabletop Placards & Exhibition Info Cards</p>
        </div>
        <div class="actions">
            <button class="btn" onclick="window.print()">🖨️ Print Direct (Ctrl+P)</button>
            <a href="cards_a6.pdf" class="btn btn-outline" download>📥 Download A6 PDF</a>
            <a href="cards_a7.pdf" class="btn btn-outline" download>📥 Download A7 Mini PDF</a>
            <a href="print_sheet_a6_on_a4.pdf" class="btn btn-outline" download>📄 A4 Sheet (4x A6)</a>
            <a href="print_sheet_a7_on_a4.pdf" class="btn btn-outline" download>📄 A4 Sheet (8x A7)</a>
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
    print("HTML dashboard generated successfully.")


def generate_preview_collage():
    """Generates a showcase preview collage image of the companion cards."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    print("Generating visual preview collage of cards...")
    fig, axes = plt.subplots(3, 3, figsize=(18, 22), facecolor="#0b0f19")
    plt.subplots_adjust(wspace=0.15, hspace=0.25)

    fig.suptitle("HPC&A 3D KEYCHAINS — COMPANION EXHIBITION CARDS\nStandard A6 / A7 Ready-to-Print Format (Designed by Nima)", 
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

        badge = item['badge_en']
        title = item['title_en']
        swap = item['swap_z']
        dims = item['dims']

        ax.set_title(f"[{badge}]\n{title}\n{dims} | Pause: {swap}", 
                     fontsize=11, fontweight='bold', color="#38bdf8", pad=8)

    preview_path = os.path.join(CARDS_DIR, "cards_preview.png")
    plt.savefig(preview_path, facecolor="#0b0f19", bbox_inches='tight', dpi=160)
    plt.close()
    print(f"Cards preview collage saved: {preview_path}")


def main():
    print("==================================================================")
    print("Generating HPC&A Companion Exhibition Display Cards (A6, A7, A4)...")
    print("==================================================================")
    generate_a6_pdf()
    generate_a7_pdf()
    generate_a4_sheet_a6()
    generate_a4_sheet_a7()
    generate_interactive_html()
    generate_preview_collage()
    print("\nAll display card formats generated successfully in display_cards/!")


if __name__ == "__main__":
    main()
