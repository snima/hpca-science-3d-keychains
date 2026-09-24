#!/usr/bin/env python3
"""
HPC&A QUANTUM DILUTION CHANDELIER 2D VECTOR & 12-BLOCK PUZZLE ASSET GENERATOR
============================================================================
Pure 2D vector graphic generation (zero 3D mesh wireframe artifacts).
Generates:
1. High-resolution master illustration of the Multi-Tiered 15 mK Cryostat Keychain.
2. 12-Block puzzle grid (3 columns x 4 rows) with:
   - Row 0 numbers at TOP
   - Row 1 & 2 numbers safely in block centers / away from seams
   - Row 3 numbers at BOTTOM (پایین شکل)
   - Left column numbers at LEFT, Right column at RIGHT
   - Clean, unobstructed horizontal and vertical cut lines with scissor guides
3. 12 individual cropped block cards.
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
KIDS_DIR = os.path.join(BASE_DIR, "kids_reward_challenge")
CHAND_DIR = os.path.join(KIDS_DIR, "chandelier_advanced_12blocks")
CHAND_BLOCKS_DIR = os.path.join(CHAND_DIR, "blocks")
os.makedirs(CHAND_BLOCKS_DIR, exist_ok=True)

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def draw_quantum_chandelier_vector(output_png: str):
    """Draws a magnificent pure 2D vector illustration of the dilution refrigerator."""
    fig, ax = plt.subplots(figsize=(10, 16), dpi=160)
    fig.patch.set_facecolor('#090d16')
    ax.set_facecolor('#090d16')

    # Coordinates: X: -36 to 36, Y: -62 to 50
    ax.set_xlim(-36, 36)
    ax.set_ylim(-62, 50)
    ax.set_aspect('equal')
    ax.axis('off')

    # Background Cryogenic Grid & Deep Cooling Gradient
    for gx in np.linspace(-33, 33, 19):
        ax.plot([gx, gx], [-60, 48], color='#1e293b', lw=0.7, alpha=0.5, zorder=1)
    for gy in np.linspace(-58, 46, 27):
        ax.plot([-33, 33], [gy, gy], color='#1e293b', lw=0.7, alpha=0.5, zorder=1)

    # Ambient cryogenic glow around the bottom mixing chamber
    mc_glow = patches.Circle((0, -42), radius=16, facecolor='#0284c7', alpha=0.25, zorder=2)
    ax.add_patch(mc_glow)
    mc_glow2 = patches.Circle((0, -42), radius=8, facecolor='#06b6d4', alpha=0.35, zorder=2)
    ax.add_patch(mc_glow2)

    # 1. KEYRING HANGING EYELET AT TOP (Y = 40 to 48)
    eyelet_outer = patches.Circle((0, 41.5), radius=7.0, facecolor='#d97706', edgecolor='#fde68a', lw=2.2, zorder=5)
    ax.add_patch(eyelet_outer)
    eyelet_inner = patches.Circle((0, 41.5), radius=3.6, facecolor='#090d16', edgecolor='#b45309', lw=1.8, zorder=6)
    ax.add_patch(eyelet_inner)

    # 2. TIERED BASE SILHOUETTE (Golden trapezoidal chassis)
    # Tapers smoothly from Top (width 34) down to bottom (width 16)
    body_pts = [
        (-18.0, 35.0),
        (18.0, 35.0),
        (9.0, -48.0),
        (-9.0, -48.0),
    ]
    chassis = patches.Polygon(body_pts, closed=True, facecolor='#1e293b', edgecolor='#334155', lw=2.0, zorder=3)
    ax.add_patch(chassis)

    # 3. VERTICAL RF COAXIAL MICROWAVE LINES (Silver & Cyan transmission cables)
    coax_x = [-9.5, -5.5, -2.0, 2.0, 5.5, 9.5]
    for cx in coax_x:
        # Cable tapers slightly inward towards bottom
        bot_cx = cx * 0.55
        ax.plot([cx, bot_cx], [34, -40], color='#cbd5e1', lw=2.2, zorder=4)
        ax.plot([cx, bot_cx], [34, -40], color='#38bdf8', lw=1.0, ls=':', zorder=5)

    # 4. FIVE GOLDEN STAGE PLATES (Dilution Cryostat Levels)
    # Level 1: 300 K / 50 K Top Flange
    stage1 = patches.FancyBboxPatch((-22.0, 31.0), 44.0, 6.0, boxstyle="round,pad=0.5",
                                   facecolor='#f59e0b', edgecolor='#fef3c7', lw=2.5, zorder=10)
    ax.add_patch(stage1)
    # HPC&A Plate inscription
    ax.text(0, 34.0, "HPC&A CRYOSTAT • 300 K", color='#0f172a', fontsize=8.5, fontweight='bold',
            ha='center', va='center', zorder=11)

    # Level 2: 4 K Pulse Tube Condenser Plate
    stage2 = patches.FancyBboxPatch((-19.0, 15.0), 38.0, 5.0, boxstyle="round,pad=0.5",
                                   facecolor='#fbbf24', edgecolor='#fef3c7', lw=2.2, zorder=10)
    ax.add_patch(stage2)
    ax.text(0, 17.5, "LIQUID HELIUM STAGE • 4.2 K", color='#0f172a', fontsize=8.0, fontweight='bold',
            ha='center', va='center', zorder=11)

    # Level 3: Still Stage (800 mK / 0.8 K)
    stage3 = patches.FancyBboxPatch((-16.0, -1.0), 32.0, 4.5, boxstyle="round,pad=0.5",
                                   facecolor='#facc15', edgecolor='#fef3c7', lw=2.0, zorder=10)
    ax.add_patch(stage3)
    ax.text(0, 1.2, "STILL EVAPORATOR • 800 mK", color='#0f172a', fontsize=7.5, fontweight='bold',
            ha='center', va='center', zorder=11)

    # Level 4: 100 mK Cold Plate
    stage4 = patches.FancyBboxPatch((-13.5, -16.0), 27.0, 4.2, boxstyle="round,pad=0.4",
                                   facecolor='#eab308', edgecolor='#fef3c7', lw=2.0, zorder=10)
    ax.add_patch(stage4)
    ax.text(0, -13.9, "COLD PLATE • 100 mK", color='#0f172a', fontsize=7.5, fontweight='bold',
            ha='center', va='center', zorder=11)

    # Level 5: Mixing Chamber Plate (15 mK)
    stage5 = patches.FancyBboxPatch((-11.0, -29.0), 22.0, 4.0, boxstyle="round,pad=0.4",
                                   facecolor='#ca8a04', edgecolor='#fef3c7', lw=1.8, zorder=10)
    ax.add_patch(stage5)
    ax.text(0, -27.0, "MIXING CHAMBER • 15 mK", color='#ffffff', fontsize=7.0, fontweight='bold',
            ha='center', va='center', zorder=11)

    # 5. HELICAL HEAT EXCHANGER COILS (Sides of cryostat)
    # Spiraling cooling coils on left and right flanks
    coil_ys = [24.0, 8.0, -8.0, -22.0]
    for y_c in coil_ys:
        for sgn in [-1, 1]:
            x_c = sgn * (15.5 - (30.0 - y_c) * 0.12)
            c_outer = patches.Circle((x_c, y_c), radius=2.8, facecolor='#06b6d4', edgecolor='#e0f2fe', lw=1.5, zorder=8)
            c_inner = patches.Circle((x_c, y_c), radius=1.3, facecolor='#090d16', edgecolor='#0284c7', lw=1.0, zorder=9)
            ax.add_patch(c_outer)
            ax.add_patch(c_inner)
            # Connecting coil tubing
            ax.plot([x_c, x_c * 0.7], [y_c, y_c - 4], color='#06b6d4', lw=1.8, zorder=7)

    # 6. BOTTOM CYLINDRICAL GOLD QPU SHIELDING CAN (15 mK Core)
    can_box = patches.FancyBboxPatch((-7.5, -46.0), 15.0, 15.0, boxstyle="round,pad=0.6",
                                    facecolor='#d97706', edgecolor='#fde68a', lw=2.4, zorder=12)
    ax.add_patch(can_box)

    # Gold Can Reflection & Details
    can_inner = patches.FancyBboxPatch((-6.0, -44.5), 12.0, 12.0, boxstyle="round,pad=0.4",
                                      facecolor='#b45309', edgecolor='#f59e0b', lw=1.2, zorder=13)
    ax.add_patch(can_inner)

    # Quantum Processor Chip Graphic inside Can
    chip_box = patches.Rectangle((-3.5, -40.5), 7.0, 7.0, facecolor='#090d16', edgecolor='#38bdf8', lw=1.2, zorder=14)
    ax.add_patch(chip_box)
    ax.scatter([0], [-37.0], s=30, color='#38bdf8', marker='+', zorder=15)

    # QPU Can debossed label
    ax.text(0, -43.0, "QPU 15 mK", color='#fef3c7', fontsize=7.5, fontweight='bold',
            ha='center', va='center', zorder=16)

    # 7. TEMPERATURE LADDER SCALE ANNOTATIONS (Left & Right margins)
    temps = [
        (34.0, "300 K\nRoom Temp", '#f59e0b'),
        (17.5, "4.2 K\nLiquid He", '#fbbf24'),
        (1.2, "800 mK\nHelium-3", '#facc15'),
        (-13.9, "100 mK\nCold Stage", '#eab308'),
        (-37.0, "15 mK\nSuperconducting", '#38bdf8'),
    ]
    for yt, label, col in temps:
        ax.text(26.5, yt, label, color=col, fontsize=6.8, fontweight='bold',
                ha='left', va='center', zorder=17)
        ax.plot([19.5, 25.0], [yt, yt], color=col, lw=1.2, ls='--', zorder=17)

    # Header & Footer text
    ax.text(0, 48.5, "⚛️ DILUTION REFRIGERATOR CHANDELIER ⚛️", color='#38bdf8', fontsize=11, fontweight='bold',
            ha='center', va='bottom', zorder=18)
    ax.text(0, -59.5, "HPC&A QUANTUM ARCHITECTURE • AVANZADO (12 BLOQUES)", color='#94a3b8', fontsize=8.0,
            ha='center', va='center', zorder=18)

    plt.subplots_adjust(left=0.03, right=0.97, top=0.97, bottom=0.03)
    fig.savefig(output_png, facecolor=fig.get_facecolor(), edgecolor='none', dpi=160)
    plt.close(fig)
    print(f"Generated Vector Quantum Chandelier: {output_png}")


def crop_image_tight(image_path: str, margin: int = 15):
    """Crops transparent/black border to make illustration tightly centered."""
    img = Image.open(image_path).convert('RGB')
    gray = img.convert('L')
    np_gray = np.array(gray)
    coords = np.argwhere(np_gray > 25)
    if coords.size == 0:
        return img
    y0, x0 = coords.min(axis=0)
    y1, x1 = coords.max(axis=0) + 1
    x0 = max(0, x0 - margin)
    y0 = max(0, y0 - margin)
    x1 = min(img.width, x1 + margin)
    y1 = min(img.height, y1 + margin)
    cropped = img.crop((x0, y0, x1, y1))
    cropped.save(image_path)
    return cropped


def split_chandelier_into_12_blocks(full_img_path: str, out_grid_path: str, block_out_dir: str):
    """
    Splits Quantum Chandelier into 12 blocks (3 columns x 4 rows):
    - Row 0 (Blocks 1-3): numbers at TOP
    - Row 1 (Blocks 4-6): numbers in upper-middle
    - Row 2 (Blocks 7-9): numbers in lower-middle
    - Row 3 (Blocks 10-12): numbers at BOTTOM (پایین شکل)
    - Column 0 numbers at LEFT, Column 2 numbers at RIGHT
    - All 3 horizontal cuts and 2 vertical cuts completely unobstructed!
    """
    img = Image.open(full_img_path).convert('RGB')
    W, H = img.size

    dx = W / 3.0
    dy = H / 4.0

    grid_img = img.copy()
    draw = ImageDraw.Draw(grid_img)

    font_huge = ImageFont.truetype(FONT_PATH, size=46)
    font_large = ImageFont.truetype(FONT_PATH, size=24)
    font_scis = ImageFont.truetype(FONT_PATH, size=20)

    # 1. Dashed cutting lines
    # Vertical cut lines (2 lines)
    for c in range(1, 3):
        x = int(round(c * dx))
        for y in range(0, H, 20):
            draw.line([(x, y), (x, min(y + 11, H))], fill=(245, 158, 11), width=4)

    # Horizontal cut lines (3 lines)
    for r in range(1, 4):
        y = int(round(r * dy))
        for x in range(0, W, 20):
            draw.line([(x, y), (min(x + 11, W), y)], fill=(245, 158, 11), width=4)

        # Scissor markers
        draw.text((int(dx * 0.4), y - 24), '✂ - - - -', fill=(245, 158, 11), font=font_scis)
        draw.text((int(dx * 1.4), y - 24), '✂ - - - -', fill=(245, 158, 11), font=font_scis)
        draw.text((int(dx * 2.4), y - 24), '✂ - - - -', fill=(245, 158, 11), font=font_scis)

    # 2. Number Badges: 12 blocks (3 cols x 4 rows)
    # Row 0: Top
    # Row 1: Upper-Mid
    # Row 2: Lower-Mid
    # Row 3: Bottom (پایین شکل!)
    badge_r = 34

    for i in range(1, 13):
        col = (i - 1) % 3
        row = (i - 1) // 3

        # Center X: push outer columns away from vertical cut lines
        if col == 0:
            cx = int(round(dx * 0.35))
        elif col == 1:
            cx = int(round(dx * 1.5))
        else:
            cx = int(round(dx * 2.65))

        # Center Y:
        if row == 0:
            cy = 20 + badge_r  # TOP
        elif row == 1:
            cy = int(round((row + 0.4) * dy))  # Upper mid
        elif row == 2:
            cy = int(round((row + 0.6) * dy))  # Lower mid
        else:
            cy = H - 20 - badge_r  # BOTTOM (پایین شکل!)

        bx1 = cx - badge_r
        by1 = cy - badge_r
        bx2 = cx + badge_r
        by2 = cy + badge_r

        # Shadow
        draw.ellipse([(bx1 + 3, by1 + 3), (bx2 + 3, by2 + 3)], fill=(9, 13, 22))
        # Golden Badge
        draw.ellipse([(bx1, by1), (bx2, by2)], fill=(245, 158, 11), outline=(255, 255, 255), width=3)

        # Number
        num_str = str(i)
        bbox = font_huge.getbbox(num_str)
        nw = bbox[2] - bbox[0]
        nh = bbox[3] - bbox[1]
        nx = cx - nw / 2.0 - bbox[0]
        ny = cy - nh / 2.0 - bbox[1]
        draw.text((nx, ny), num_str, fill=(255, 255, 255), font=font_huge)

    grid_img.save(out_grid_path)
    print(f"  Saved master Quantum Chandelier grid: {out_grid_path}")

    # 3. Individual block cropped cards
    block_names_es = [
        "1. ANILLA & BRIDA 300K (OESTE)",
        "2. PLACA HPC&A 300K (CENTRO)",
        "3. BRIDA 300K & ESCALA (ESTE)",
        "4. LÍNEAS RF & COAXIAL (OESTE)",
        "5. ETAPA HELIO 4.2K (CENTRO)",
        "6. SERPENTÍN CONDENSADOR (ESTE)",
        "7. EVAPORADOR STILL (OESTE)",
        "8. INTERCAMBIADOR 800mK (CENTRO)",
        "9. SERPENTÍN STILL (ESTE)",
        "10. PLACA FRÍA 100mK (OESTE)",
        "11. CÁMARA 15mK & QPU (CENTRO)",
        "12. BLINDAJE TÉRMICO 15mK (ESTE)",
    ]

    for i in range(1, 13):
        col = (i - 1) % 3
        row = (i - 1) // 3

        x1 = int(round(col * dx))
        x2 = int(round((col + 1) * dx)) if col < 2 else W
        y1 = int(round(row * dy))
        y2 = int(round((row + 1) * dy)) if row < 3 else H

        piece = img.crop((x1, y1, x2, y2))
        pw, ph = piece.size

        # Card
        bar_h = 50
        card = Image.new("RGB", (pw + 24, ph + bar_h + 16), color=(255, 255, 255))
        cdraw = ImageDraw.Draw(card)

        if row == 0:
            # Top row: number bar at top
            cdraw.rectangle([(12, 10), (pw + 12, 10 + bar_h)], fill=(245, 158, 11))
            cdraw.text((20, 20), f"BLOQUE #{i} • {block_names_es[i-1][:26]}", fill=(255, 255, 255), font=font_large)
            card.paste(piece, (12, 10 + bar_h))
        else:
            # Middle and bottom rows: footer bar at bottom (پایین شکل!)
            card.paste(piece, (12, 10))
            cdraw.rectangle([(12, ph + 10), (pw + 12, ph + 10 + bar_h)], fill=(245, 158, 11))
            cdraw.text((20, ph + 18), f"BLOQUE #{i} • {block_names_es[i-1][:26]}", fill=(255, 255, 255), font=font_large)

        # Outer border
        cdraw.rectangle([(0, 0), (card.width - 1, card.height - 1)], outline=(245, 158, 11), width=3)

        out_piece = os.path.join(block_out_dir, f"chand_block_{i}.png")
        card.save(out_piece)

    print(f"  Cropped 12 individual cards to: {block_out_dir}")


def main():
    print("Generating HPC&A Quantum Chandelier 2D Vector Illustration & 12-Block Challenge...")
    master_png = os.path.join(CHAND_DIR, "chandelier_2d_master.png")
    grid_png = os.path.join(CHAND_DIR, "chandelier_2d_12blocks_grid.png")

    draw_quantum_chandelier_vector(master_png)
    crop_image_tight(master_png, margin=20)
    split_chandelier_into_12_blocks(master_png, grid_png, CHAND_BLOCKS_DIR)
    print("Quantum Chandelier 2D assets generated successfully!")


if __name__ == "__main__":
    main()
