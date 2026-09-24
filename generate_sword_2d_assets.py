#!/usr/bin/env python3
"""
HPC&A CYBER SWORD 2D VECTOR & 6-BLOCK PUZZLE ASSET GENERATOR
===========================================================
Pure 2D vector graphic generation (zero 3D mesh wireframe artifacts).
Generates:
1. High-resolution master illustration of the Cyber Sword Keychain.
2. 6-Block puzzle grid with:
   - Row 0 numbers at TOP
   - Row 2 numbers at BOTTOM (پایین شکل)
   - Left column numbers at LEFT, Right column at RIGHT (away from central vertical cut)
   - All cut lines unobstructed with scissor guides
3. 6 individual cropped block cards.
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
SWORD_BLOCKS_DIR = os.path.join(KIDS_DIR, "sword_blocks")
os.makedirs(SWORD_BLOCKS_DIR, exist_ok=True)

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def draw_cyber_sword_vector(output_png: str):
    """Draws a stunning pure 2D vector cyber sword illustration."""
    fig, ax = plt.subplots(figsize=(10, 16), dpi=160)
    fig.patch.set_facecolor('#090d16')
    ax.set_facecolor('#090d16')

    # Coordinate system: X: -35 to 35, Y: -60 to 52
    ax.set_xlim(-35, 35)
    ax.set_ylim(-60, 52)
    ax.set_aspect('equal')
    ax.axis('off')

    # Background Cyber Grid & Energy Radiance
    for gx in np.linspace(-32, 32, 17):
        ax.plot([gx, gx], [-58, 50], color='#1e293b', lw=0.8, alpha=0.5, zorder=1)
    for gy in np.linspace(-56, 48, 27):
        ax.plot([-32, 32], [gy, gy], color='#1e293b', lw=0.8, alpha=0.5, zorder=1)

    # Ambient energy aura behind the blade
    aura = patches.Polygon([
        (0, 48), (14, 28), (16, 0), (14, -12),
        (-14, -12), (-16, 0), (-14, 28)
    ], closed=True, facecolor='#0284c7', alpha=0.22, zorder=2)
    ax.add_patch(aura)

    # 1. BLADE OUTER CONTOUR (Sharp Energy Blade)
    # Outer blade edge (Cyan glowing plasma)
    blade_outer = [
        (0.0, 46.0),     # Blade point
        (9.0, 30.0),     # Upper taper
        (11.0, 10.0),    # Mid blade
        (10.0, -10.0),   # Blade base
        (-10.0, -10.0),  # Base left
        (-11.0, 10.0),   # Mid left
        (-9.0, 30.0),    # Upper left
    ]
    poly_outer = patches.Polygon(blade_outer, closed=True, facecolor='#0284c7', edgecolor='#38bdf8', lw=3.0, zorder=3)
    ax.add_patch(poly_outer)

    # Inner Blade Core (Bright cyan / aqua energy)
    blade_inner = [
        (0.0, 43.5),
        (6.8, 28.5),
        (8.2, 9.5),
        (7.2, -9.5),
        (-7.2, -9.5),
        (-8.2, 9.5),
        (-6.8, 28.5),
    ]
    poly_inner = patches.Polygon(blade_inner, closed=True, facecolor='#06b6d4', edgecolor='#e0f2fe', lw=1.8, zorder=4)
    ax.add_patch(poly_inner)

    # Blade Core Highlight (Electric white center beam)
    ax.plot([0, 0], [-8, 41], color='#ffffff', lw=2.5, alpha=0.9, zorder=5)

    # Fuller / Circuit Channel (Dark navy contrast channel)
    fuller = patches.FancyBboxPatch((-3.2, -8.0), 6.4, 40.0,
                                   boxstyle="round,pad=0.3",
                                   facecolor='#0f172a', edgecolor='#38bdf8', lw=1.5, zorder=6)
    ax.add_patch(fuller)

    # Circuit traces along fuller
    for y_trace in [-2, 8, 18, 28]:
        ax.plot([-2.0, 2.0], [y_trace, y_trace], color='#38bdf8', lw=1.2, zorder=7)
        ax.scatter([-2.0, 2.0], [y_trace, y_trace], color='#e0f2fe', s=16, zorder=8)

    # "HPC&A" Runes on blade
    for i, ch in enumerate(["H", "P", "C", "&", "A"]):
        ax.text(0, 24 - i * 6.5, ch, color='#ffffff', fontsize=11, fontweight='bold',
                ha='center', va='center', zorder=9,
                bbox=dict(boxstyle='square,pad=0.1', facecolor='#0284c7', edgecolor='none', alpha=0.7))

    # 2. FUTURISTIC WINGED CROSSGUARD
    # Guard Base Wings (Golden / Amber bronze)
    guard_pts = [
        (0.0, -9.0),
        (13.0, -8.0),
        (24.0, -12.0),
        (25.0, -16.0),
        (18.0, -18.0),
        (6.0, -18.0),
        (5.5, -20.0),
        (-5.5, -20.0),
        (-6.0, -18.0),
        (-18.0, -18.0),
        (-25.0, -16.0),
        (-24.0, -12.0),
        (-13.0, -8.0),
    ]
    guard_poly = patches.Polygon(guard_pts, closed=True, facecolor='#d97706', edgecolor='#fef3c7', lw=2.5, zorder=10)
    ax.add_patch(guard_poly)

    # Guard Top Wing Plates (Brilliant Gold)
    guard_top_r = patches.Polygon([(4, -10), (16, -9), (22, -13), (14, -16), (4, -16)],
                                 closed=True, facecolor='#f59e0b', edgecolor='#fde68a', lw=1.5, zorder=11)
    guard_top_l = patches.Polygon([(-4, -10), (-16, -9), (-22, -13), (-14, -16), (-4, -16)],
                                 closed=True, facecolor='#f59e0b', edgecolor='#fde68a', lw=1.5, zorder=11)
    ax.add_patch(guard_top_r)
    ax.add_patch(guard_top_l)

    # Central Power Diamond (Energy Core)
    core_diamond = patches.RegularPolygon((0, -14.5), numVertices=4, radius=5.5,
                                         facecolor='#06b6d4', edgecolor='#ffffff', lw=2.0, zorder=12)
    ax.add_patch(core_diamond)
    core_inner = patches.RegularPolygon((0, -14.5), numVertices=4, radius=3.0,
                                       facecolor='#ffffff', edgecolor='#38bdf8', lw=1.0, zorder=13)
    ax.add_patch(core_inner)

    # 3. CYBER HILT / GRIP
    # Handle base
    grip_box = patches.FancyBboxPatch((-4.5, -39.0), 9.0, 19.0,
                                     boxstyle="round,pad=0.4",
                                     facecolor='#1e293b', edgecolor='#64748b', lw=1.8, zorder=10)
    ax.add_patch(grip_box)

    # Ribbed ergonomic grip rings
    for yr in np.linspace(-36, -23, 6):
        rib = patches.FancyBboxPatch((-4.0, yr - 0.9), 8.0, 1.8,
                                    boxstyle="round,pad=0.2",
                                    facecolor='#0284c7', edgecolor='#38bdf8', lw=1.0, zorder=11)
        ax.add_patch(rib)

    # 4. POMMEL & KEYRING HANGING EYELET
    # Pommel gold cap
    pommel_cap = patches.FancyBboxPatch((-7.0, -42.5), 14.0, 4.5,
                                       boxstyle="round,pad=0.3",
                                       facecolor='#d97706', edgecolor='#fde68a', lw=1.5, zorder=12)
    ax.add_patch(pommel_cap)

    # Integrated Keyring Eyelet Ring
    eyelet_outer = patches.Circle((0, -49.5), radius=8.2, facecolor='#f59e0b', edgecolor='#fef3c7', lw=2.5, zorder=12)
    ax.add_patch(eyelet_outer)
    eyelet_inner = patches.Circle((0, -49.5), radius=4.4, facecolor='#090d16', edgecolor='#b45309', lw=2.0, zorder=13)
    ax.add_patch(eyelet_inner)

    # Keychain Chain Ring Indicator
    keychain_ring = patches.Circle((0, -49.5), radius=5.8, fill=False, edgecolor='#38bdf8', ls='--', lw=1.2, zorder=14)
    ax.add_patch(keychain_ring)

    # Title Banner (Top)
    ax.text(0, 49.5, "⚔️ HPC&A CYBER SWORD ⚔️", color='#38bdf8', fontsize=12, fontweight='bold',
            ha='center', va='bottom', zorder=15)

    # Subtitle
    ax.text(0, -58.0, "HEROIC SCIENCE KEYCHAIN • PRIMARIA", color='#94a3b8', fontsize=8.5,
            ha='center', va='center', zorder=15)

    plt.subplots_adjust(left=0.03, right=0.97, top=0.97, bottom=0.03)
    fig.savefig(output_png, facecolor=fig.get_facecolor(), edgecolor='none', dpi=160)
    plt.close(fig)
    print(f"Generated Vector Sword: {output_png}")


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


def split_sword_into_6_blocks(full_img_path: str, out_grid_path: str, block_out_dir: str):
    """
    Splits Cyber Sword into 6 blocks (2 columns x 3 rows):
    - Row 0 (Blocks 1, 2): numbers at TOP
    - Row 1 (Blocks 3, 4): numbers at outer edges (Col 0: left, Col 1: right)
    - Row 2 (Blocks 5, 6): numbers at BOTTOM (پایین شکل)
    - Central vertical cut line and both horizontal cut lines completely unobstructed!
    """
    img = Image.open(full_img_path).convert('RGB')
    W, H = img.size

    dx = W / 2.0
    dy = H / 3.0

    grid_img = img.copy()
    draw = ImageDraw.Draw(grid_img)

    font_huge = ImageFont.truetype(FONT_PATH, size=52)
    font_large = ImageFont.truetype(FONT_PATH, size=28)
    font_scis = ImageFont.truetype(FONT_PATH, size=24)

    # 1. Dashed cutting lines
    # Vertical cut down the center
    x_mid = int(round(dx))
    for y in range(0, H, 22):
        draw.line([(x_mid, y), (x_mid, min(y + 12, H))], fill=(6, 182, 212), width=4)

    # Horizontal cuts (2 lines)
    for r in range(1, 3):
        y_h = int(round(r * dy))
        for x in range(0, W, 22):
            draw.line([(x, y_h), (min(x + 12, W), y_h)], fill=(6, 182, 212), width=4)

        # Scissor markers
        draw.text((int(dx * 0.35), y_h - 28), '✂ - - - - - -', fill=(6, 182, 212), font=font_scis)
        draw.text((int(dx * 1.35), y_h - 28), '✂ - - - - - -', fill=(6, 182, 212), font=font_scis)

    # Vertical cut scissor markings
    draw.text((x_mid - 24, int(dy * 0.45)), '✂', fill=(6, 182, 212), font=font_scis)
    draw.text((x_mid - 24, int(dy * 1.45)), '✂', fill=(6, 182, 212), font=font_scis)
    draw.text((x_mid - 24, int(dy * 2.45)), '✂', fill=(6, 182, 212), font=font_scis)

    # 2. Number Badges placement:
    # 6 blocks: 2 cols x 3 rows:
    # Block 1: col 0, row 0 -> TOP-LEFT
    # Block 2: col 1, row 0 -> TOP-RIGHT
    # Block 3: col 0, row 1 -> MID-LEFT
    # Block 4: col 1, row 1 -> MID-RIGHT
    # Block 5: col 0, row 2 -> BOTTOM-LEFT (پایین شکل!)
    # Block 6: col 1, row 2 -> BOTTOM-RIGHT (پایین شکل!)

    badge_r = 40
    badge_positions = [
        # (cx, cy) for blocks 1 to 6
        (int(dx * 0.35), 24 + badge_r),               # #1 Top Left
        (int(dx * 1.65), 24 + badge_r),               # #2 Top Right
        (int(dx * 0.28), int(round(1.5 * dy))),       # #3 Mid Left (far from center cut)
        (int(dx * 1.72), int(round(1.5 * dy))),       # #4 Mid Right (far from center cut)
        (int(dx * 0.35), H - 24 - badge_r),           # #5 Bottom Left (پایین شکل!)
        (int(dx * 1.65), H - 24 - badge_r),           # #6 Bottom Right (پایین شکل!)
    ]

    for i in range(1, 7):
        cx, cy = badge_positions[i - 1]
        bx1 = cx - badge_r
        by1 = cy - badge_r
        bx2 = cx + badge_r
        by2 = cy + badge_r

        # Outer Shadow
        draw.ellipse([(bx1 + 3, by1 + 3), (bx2 + 3, by2 + 3)], fill=(9, 13, 22))
        # Colorful Badge
        draw.ellipse([(bx1, by1), (bx2, by2)], fill=(6, 182, 212), outline=(255, 255, 255), width=4)

        # Number text
        num_str = str(i)
        bbox = font_huge.getbbox(num_str)
        nw = bbox[2] - bbox[0]
        nh = bbox[3] - bbox[1]
        nx = cx - nw / 2.0 - bbox[0]
        ny = cy - nh / 2.0 - bbox[1]
        draw.text((nx, ny), num_str, fill=(255, 255, 255), font=font_huge)

    grid_img.save(out_grid_path)
    print(f"  Saved master Cyber Sword grid: {out_grid_path}")

    # 3. Individual block cropped cards
    block_names_es = [
        "1. PUNTA DE PLASMA (IZQ)",
        "2. PUNTA DE PLASMA (DER)",
        "3. CANAL RÚNICO HPC&A (IZQ)",
        "4. CANAL RÚNICO HPC&A (DER)",
        "5. ALA DEFENSA & MANGO (IZQ)",
        "6. ANILLA POMO & CRISTAL (DER)",
    ]

    for i in range(1, 7):
        col = (i - 1) % 2
        row = (i - 1) // 2

        x1 = int(round(col * dx))
        x2 = int(round((col + 1) * dx)) if col < 1 else W
        y1 = int(round(row * dy))
        y2 = int(round((row + 1) * dy)) if row < 2 else H

        piece = img.crop((x1, y1, x2, y2))
        pw, ph = piece.size

        # Card with header if top row, or footer if bottom row
        bar_h = 56
        card = Image.new("RGB", (pw + 24, ph + bar_h + 16), color=(255, 255, 255))
        cdraw = ImageDraw.Draw(card)

        if row == 0:
            # Top row: number bar at top
            cdraw.rectangle([(12, 10), (pw + 12, 10 + bar_h)], fill=(6, 182, 212))
            cdraw.text((22, 20), f"BLOQUE #{i} • {block_names_es[i-1]}", fill=(255, 255, 255), font=font_large)
            card.paste(piece, (12, 10 + bar_h))
        else:
            # Middle and bottom rows: footer bar at bottom (پایین شکل!)
            card.paste(piece, (12, 10))
            cdraw.rectangle([(12, ph + 10), (pw + 12, ph + 10 + bar_h)], fill=(6, 182, 212))
            cdraw.text((22, ph + 20), f"BLOQUE #{i} • {block_names_es[i-1]}", fill=(255, 255, 255), font=font_large)

        # Outer border
        cdraw.rectangle([(0, 0), (card.width - 1, card.height - 1)], outline=(6, 182, 212), width=3)

        out_piece = os.path.join(block_out_dir, f"sword_block_{i}.png")
        card.save(out_piece)

    print(f"  Cropped 6 individual cards to: {block_out_dir}")


def main():
    print("Generating HPC&A Cyber Sword 2D Vector Illustration & 6-Block Challenge...")
    master_png = os.path.join(KIDS_DIR, "sword_2d_master.png")
    grid_png = os.path.join(KIDS_DIR, "sword_2d_6blocks_grid.png")

    draw_cyber_sword_vector(master_png)
    crop_image_tight(master_png, margin=20)
    split_sword_into_6_blocks(master_png, grid_png, SWORD_BLOCKS_DIR)
    print("Cyber Sword 2D assets generated successfully!")


if __name__ == "__main__":
    main()
