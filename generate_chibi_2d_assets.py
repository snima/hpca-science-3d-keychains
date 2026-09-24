#!/usr/bin/env python3
"""
GENERATE PURE 2D VECTOR ASSETS FOR CHIBI GPU (100% MESH-FREE)
==============================================================
Generates ultra-clean, flat 2D graphic illustrations directly from CAD geometry:
- ZERO 3D mesh wireframe or black facets
- Numbers positioned correctly relative to horizontal middle cut:
  * TOP ROW (Blocks 1, 2, 3): numbers at the TOP
  * BOTTOM ROW (Blocks 4, 5, 6): numbers at the BOTTOM (پایین شکل)
- Clean, minimal text for easy cutting along dashed lines
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
KIDS_DIR = os.path.join(BASE_DIR, "kids_reward_challenge")
os.makedirs(KIDS_DIR, exist_ok=True)

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def draw_pure_2d_chibi(ax, outline_only=False):
    """Draws pure 2D mathematical vector geometry of Chibi GPU (zero mesh)."""
    body_fill = 'white' if outline_only else '#2dd4bf'
    body_edge = '#0f172a' if outline_only else '#0f766e'
    body = patches.FancyBboxPatch((-25.0, -13.0), 50.0, 26.0,
                                 boxstyle='round,pad=0,rounding_size=3.2',
                                 facecolor=body_fill, edgecolor=body_edge, linewidth=2.8)
    ax.add_patch(body)

    # Eyelet Tab
    eye_fill = 'white' if outline_only else '#f59e0b'
    eye_edge = '#0f172a' if outline_only else '#b45309'
    eyelet_outer = patches.Circle((-25.0, 13.0), 5.2, facecolor=eye_fill, edgecolor=eye_edge, linewidth=2.8)
    eyelet_inner = patches.Circle((-25.0, 13.0), 2.3, facecolor='white', edgecolor=eye_edge, linewidth=2.2)
    ax.add_patch(eyelet_outer)
    ax.add_patch(eyelet_inner)

    # Boots
    boot_fill = 'white' if outline_only else '#38bdf8'
    boot_edge = '#0f172a' if outline_only else '#0284c7'
    toe_fill = 'white' if outline_only else '#fde047'
    for bx in [-10.0, 6.0]:
        boot = patches.FancyBboxPatch((bx - 4.5, -16.2), 9.0, 3.2,
                                     boxstyle='round,pad=0,rounding_size=1.4',
                                     facecolor=boot_fill, edgecolor=boot_edge, linewidth=2.4)
        ax.add_patch(boot)
        toe = patches.Circle((bx, -14.6), 0.9, facecolor=toe_fill, edgecolor=boot_edge, linewidth=1.4)
        ax.add_patch(toe)

    # Fan well
    well_fill = 'white' if outline_only else '#14b8a6'
    well_edge = '#0f172a' if outline_only else '#0d9488'
    well = patches.Circle((-5.0, -1.8), 8.8, facecolor=well_fill, edgecolor=well_edge, linewidth=2.2)
    ax.add_patch(well)

    # Petals
    petal_fill = 'white' if outline_only else '#c084fc'
    petal_edge = '#0f172a' if outline_only else '#7e22ce'
    for ang in np.linspace(0, 360, 8, endpoint=False):
        rad = np.radians(ang)
        px = -5.0 + 6.2 * np.cos(rad)
        py = -1.8 + 6.2 * np.sin(rad)
        petal = patches.Circle((px, py), 2.2, facecolor=petal_fill, edgecolor=petal_edge, linewidth=1.8)
        ax.add_patch(petal)

    # Face hub
    hub_fill = 'white' if outline_only else '#ffedd5'
    hub_edge = '#0f172a' if outline_only else '#ea580c'
    face_hub = patches.Circle((-5.0, -1.8), 4.6, facecolor=hub_fill, edgecolor=hub_edge, linewidth=2.2)
    ax.add_patch(face_hub)

    # Eyes & sparkles
    for ex in [-1.8, 1.8]:
        eye_color = 'white' if outline_only else '#1e1b4b'
        eye = patches.Circle((-5.0 + ex, -1.8 + 1.0), 0.85, facecolor=eye_color, edgecolor='#0f172a', linewidth=1.2)
        ax.add_patch(eye)
        if not outline_only:
            sparkle = patches.Circle((-5.0 + ex + 0.25, -1.8 + 1.0 + 0.25), 0.32, facecolor='white', edgecolor='none')
            ax.add_patch(sparkle)

    # Rosy Cheeks
    for cx in [-2.9, 2.9]:
        cheek_color = 'white' if outline_only else '#fb7185'
        edge = '#0f172a' if outline_only else 'none'
        cheek = patches.Circle((-5.0 + cx, -1.8 - 0.2), 0.65, facecolor=cheek_color, edgecolor=edge, linewidth=1.0)
        ax.add_patch(cheek)

    # Mouth
    mouth_fill = 'white' if outline_only else '#e11d48'
    mouth = patches.Wedge((-5.0, -1.8 - 0.8), 1.2, 200, 340, facecolor=mouth_fill, edgecolor='#0f172a', linewidth=1.2)
    ax.add_patch(mouth)

    # Banner
    ban_fill = 'white' if outline_only else '#f43f5e'
    ban_edge = '#0f172a' if outline_only else '#be123c'
    banner = patches.FancyBboxPatch((-11.0, 7.9), 22.0, 4.2,
                                   boxstyle='round,pad=0,rounding_size=1.4',
                                   facecolor=ban_fill, edgecolor=ban_edge, linewidth=2.4)
    ax.add_patch(banner)
    txt_col = '#0f172a' if outline_only else 'white'
    ax.text(0.0, 10.0, 'HPC&A', color=txt_col, fontsize=15, fontweight='bold',
            ha='center', va='center', family='sans-serif')

    # Side vents
    vent_fill = 'white' if outline_only else '#0f172a'
    for vy in [-5.0, -1.5, 2.0, 5.5]:
        vent = patches.FancyBboxPatch((16.0 - 2.25, vy - 0.8), 4.5, 1.6,
                                     boxstyle='round,pad=0,rounding_size=0.7',
                                     facecolor=vent_fill, edgecolor='#0f172a', linewidth=1.6)
        ax.add_patch(vent)


def render_chibi_vector_image(output_path: str, outline_only: bool = False):
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300, facecolor='white')
    ax.set_facecolor('white')
    draw_pure_2d_chibi(ax, outline_only=outline_only)
    ax.set_xlim(-33.5, 27.5)
    ax.set_ylim(-19.0, 19.0)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, facecolor='white', bbox_inches='tight', pad_inches=0.04)
    plt.close()


def crop_to_content(image_path: str, margin: int = 24) -> Image.Image:
    img = Image.open(image_path).convert('RGBA')
    arr = np.array(img)
    mask = ~((arr[:, :, 0] > 248) & (arr[:, :, 1] > 248) & (arr[:, :, 2] > 248))
    coords = np.argwhere(mask)
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


def split_into_6_blocks_corrected_positions(full_img_path: str, out_grid_path: str, block_out_dir: str):
    """
    Splits into 6 blocks with:
    - TOP ROW (1, 2, 3): numbers placed at the TOP
    - BOTTOM ROW (4, 5, 6): numbers placed at the BOTTOM (پایین شکل)
    - Clean horizontal cut line through the middle with zero collisions!
    """
    img = Image.open(full_img_path).convert('RGB')
    W, H = img.size

    dx = W / 3.0
    dy = H / 2.0

    grid_img = img.copy()
    draw = ImageDraw.Draw(grid_img)

    font_huge = ImageFont.truetype(FONT_PATH, size=52)
    font_large = ImageFont.truetype(FONT_PATH, size=30)
    font_scis = ImageFont.truetype(FONT_PATH, size=24)

    # 1. Dashed cutting lines on master grid
    for c in range(1, 3):
        x = int(round(c * dx))
        for y in range(0, H, 20):
            draw.line([(x, y), (x, min(y + 11, H))], fill=(219, 39, 119), width=4)

    # Horizontal cut line through the middle
    y_mid = int(round(dy))
    for x in range(0, W, 20):
        draw.line([(x, y_mid), (min(x + 11, W), y_mid)], fill=(219, 39, 119), width=4)

    # Scissors markings along the middle cut line
    draw.text((int(dx * 0.45), y_mid - 28), '✂ - - - - - - - -', fill=(219, 39, 119), font=font_scis)
    draw.text((int(dx * 1.45), y_mid - 28), '✂ - - - - - - - -', fill=(219, 39, 119), font=font_scis)
    draw.text((int(dx * 2.45), y_mid - 28), '✂ - - - - - - - -', fill=(219, 39, 119), font=font_scis)

    # 2. Number Badges: TOP ROW -> at TOP, BOTTOM ROW -> at BOTTOM!
    badge_r = 38
    for i in range(1, 7):
        col = (i - 1) % 3
        row = (i - 1) // 3
        cx = int(round((col + 0.5) * dx))

        if row == 0:
            cy = 22 + badge_r  # TOP
        else:
            cy = H - 22 - badge_r  # BOTTOM (پایین شکل!)

        bx1 = cx - badge_r
        by1 = cy - badge_r
        bx2 = cx + badge_r
        by2 = cy + badge_r

        # Shadow
        draw.ellipse([(bx1 + 3, by1 + 3), (bx2 + 3, by2 + 3)], fill=(15, 23, 42))
        # Circle
        draw.ellipse([(bx1, by1), (bx2, by2)], fill=(219, 39, 119), outline=(255, 255, 255), width=4)

        # Number
        num_str = str(i)
        bbox = font_huge.getbbox(num_str)
        nw = bbox[2] - bbox[0]
        nh = bbox[3] - bbox[1]
        nx = cx - nw / 2.0 - bbox[0]
        ny = cy - nh / 2.0 - bbox[1]
        draw.text((nx, ny), num_str, fill=(255, 255, 255), font=font_huge)

    grid_img.save(out_grid_path)
    print(f"  Saved master grid: {out_grid_path}")

    # 3. Individual block cropped cards
    block_names_es = [
        "1. ANILLA DE VIAJE",
        "2. CEREBRO HPC&A",
        "3. RADIADOR SUPERIOR",
        "4. BOTA PCIE IZQUIERDA",
        "5. SONRISA KAWAII",
        "6. ESCAPE TURBO",
    ]

    for i in range(1, 7):
        col = (i - 1) % 3
        row = (i - 1) // 3

        x1 = int(round(col * dx))
        x2 = int(round((col + 1) * dx)) if col < 2 else W
        y1 = int(round(row * dy))
        y2 = int(round((row + 1) * dy)) if row < 1 else H

        piece = img.crop((x1, y1, x2, y2))
        pw, ph = piece.size

        # Card with header if top row, or footer if bottom row!
        bar_h = 56
        card = Image.new("RGB", (pw + 24, ph + bar_h + 16), color=(255, 255, 255))
        cdraw = ImageDraw.Draw(card)

        if row == 0:
            # Top row: number bar at top
            card.paste(piece, (12, bar_h + 8))
            cdraw.rectangle([(4, 4), (pw + 19, ph + bar_h + 11)], outline=(219, 39, 119), width=3)
            cdraw.rectangle([(8, 8), (pw + 15, bar_h)], fill=(219, 39, 119))
            cdraw.text((18, 12), f"#{i}", fill=(255, 255, 255), font=font_large)
            cdraw.text((85, 18), block_names_es[i - 1], fill=(255, 255, 255), font=ImageFont.truetype(FONT_PATH, size=18))
        else:
            # Bottom row: number bar at BOTTOM (پایین شکل!)
            card.paste(piece, (12, 10))
            cdraw.rectangle([(4, 4), (pw + 19, ph + bar_h + 11)], outline=(219, 39, 119), width=3)
            cdraw.rectangle([(8, ph + 14), (pw + 15, ph + 14 + bar_h - 8)], fill=(219, 39, 119))
            cdraw.text((18, ph + 18), f"#{i}", fill=(255, 255, 255), font=font_large)
            cdraw.text((85, ph + 24), block_names_es[i - 1], fill=(255, 255, 255), font=ImageFont.truetype(FONT_PATH, size=18))

        block_file = os.path.join(block_out_dir, f"block_{i}.png")
        card.save(block_file)
        print(f"  Saved block #{i}: {block_file}")


def main():
    print("Generating corrected pure 2D Chibi GPU assets...")
    raw_2d = os.path.join(KIDS_DIR, "chibi_gpu_2d_full_color.png")
    raw_lineart = os.path.join(KIDS_DIR, "chibi_gpu_coloring_lineart.png")
    grid_img = os.path.join(KIDS_DIR, "chibi_gpu_2d_6blocks_grid.png")

    render_chibi_vector_image(raw_2d, outline_only=False)
    crop_to_content(raw_2d, margin=24)

    render_chibi_vector_image(raw_lineart, outline_only=True)
    crop_to_content(raw_lineart, margin=24)

    split_into_6_blocks_corrected_positions(raw_2d, grid_img, KIDS_DIR)
    print("Chibi assets generated successfully!")


if __name__ == "__main__":
    main()
