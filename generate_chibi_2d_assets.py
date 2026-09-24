#!/usr/bin/env python3
"""
GENERATE PURE 2D VECTOR ASSETS FOR CHIBI GPU (100% MESH-FREE)
==============================================================
Generates ultra-clean, flat 2D graphic illustrations directly from CAD geometry:
- ZERO 3D mesh wireframe or black facets
- Radiant, cheerful colors
- EXTRA LARGE, high-visibility numbers for kids
1. chibi_gpu_2d_full_color.png - Pure 2D vector colored illustration
2. chibi_gpu_2d_isometric_hero.png - 3D smooth cel-shaded perspective
3. chibi_gpu_coloring_lineart.png - Clean cartoon line-art outline
4. chibi_gpu_2d_6blocks_grid.png - 2D illustration with 6-block grid & EXTRA LARGE numbers
5. block_1.png to block_6.png - Individual cropped puzzle blocks with BIG number badges
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
KIDS_DIR = os.path.join(BASE_DIR, "kids_reward_challenge")
os.makedirs(KIDS_DIR, exist_ok=True)

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def draw_pure_2d_chibi(ax, outline_only=False):
    """Draws pure 2D mathematical vector geometry of Chibi GPU (zero mesh)."""
    # 1. Main Turquoise Body (50 x 26 mm, fillet 3.2 mm)
    body_fill = 'white' if outline_only else '#2dd4bf'
    body_edge = '#0f172a' if outline_only else '#0f766e'
    body = patches.FancyBboxPatch((-25.0, -13.0), 50.0, 26.0,
                                 boxstyle='round,pad=0,rounding_size=3.2',
                                 facecolor=body_fill, edgecolor=body_edge, linewidth=2.8)
    ax.add_patch(body)

    # 2. Keyring Eyelet Tab on Top Left: (-25.0, 13.0), outer r=5.2, inner r=2.3
    eye_fill = 'white' if outline_only else '#f59e0b'
    eye_edge = '#0f172a' if outline_only else '#b45309'
    eyelet_outer = patches.Circle((-25.0, 13.0), 5.2, facecolor=eye_fill, edgecolor=eye_edge, linewidth=2.8)
    eyelet_inner = patches.Circle((-25.0, 13.0), 2.3, facecolor='white', edgecolor=eye_edge, linewidth=2.2)
    ax.add_patch(eyelet_outer)
    ax.add_patch(eyelet_inner)

    # 3. Boots at bottom (PCIe connectors): [-10.0, 6.0]
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

    # 4. Circular Fan Well: (-5.0, -1.8), r=8.8
    well_fill = 'white' if outline_only else '#14b8a6'
    well_edge = '#0f172a' if outline_only else '#0d9488'
    well = patches.Circle((-5.0, -1.8), 8.8, facecolor=well_fill, edgecolor=well_edge, linewidth=2.2)
    ax.add_patch(well)

    # 5. Petal Fan Blades (8 blades)
    petal_fill = 'white' if outline_only else '#c084fc'
    petal_edge = '#0f172a' if outline_only else '#7e22ce'
    for ang in np.linspace(0, 360, 8, endpoint=False):
        rad = np.radians(ang)
        px = -5.0 + 6.2 * np.cos(rad)
        py = -1.8 + 6.2 * np.sin(rad)
        petal = patches.Circle((px, py), 2.2, facecolor=petal_fill, edgecolor=petal_edge, linewidth=1.8)
        ax.add_patch(petal)

    # 6. Chubby Smiling Face Hub: r=4.6
    hub_fill = 'white' if outline_only else '#ffedd5'
    hub_edge = '#0f172a' if outline_only else '#ea580c'
    face_hub = patches.Circle((-5.0, -1.8), 4.6, facecolor=hub_fill, edgecolor=hub_edge, linewidth=2.2)
    ax.add_patch(face_hub)

    # 7. Eyes with Sparkle Pupils
    for ex in [-1.8, 1.8]:
        eye_color = 'white' if outline_only else '#1e1b4b'
        eye = patches.Circle((-5.0 + ex, -1.8 + 1.0), 0.85, facecolor=eye_color, edgecolor='#0f172a', linewidth=1.2)
        ax.add_patch(eye)
        if not outline_only:
            sparkle = patches.Circle((-5.0 + ex + 0.25, -1.8 + 1.0 + 0.25), 0.32, facecolor='white', edgecolor='none')
            ax.add_patch(sparkle)

    # 8. Rosy Cheeks
    if not outline_only:
        for cx in [-2.9, 2.9]:
            cheek = patches.Circle((-5.0 + cx, -1.8 - 0.2), 0.65, facecolor='#fb7185', edgecolor='none')
            ax.add_patch(cheek)
    else:
        for cx in [-2.9, 2.9]:
            cheek = patches.Circle((-5.0 + cx, -1.8 - 0.2), 0.65, facecolor='white', edgecolor='#0f172a', linewidth=1.0)
            ax.add_patch(cheek)

    # 9. Open Smiling Mouth
    mouth_fill = 'white' if outline_only else '#e11d48'
    mouth = patches.Wedge((-5.0, -1.8 - 0.8), 1.2, 200, 340, facecolor=mouth_fill, edgecolor='#0f172a', linewidth=1.2)
    ax.add_patch(mouth)

    # 10. Top Banner with HPC&A
    ban_fill = 'white' if outline_only else '#f43f5e'
    ban_edge = '#0f172a' if outline_only else '#be123c'
    banner = patches.FancyBboxPatch((-11.0, 7.9), 22.0, 4.2,
                                   boxstyle='round,pad=0,rounding_size=1.4',
                                   facecolor=ban_fill, edgecolor=ban_edge, linewidth=2.4)
    ax.add_patch(banner)
    txt_col = '#0f172a' if outline_only else 'white'
    ax.text(0.0, 10.0, 'HPC&A', color=txt_col, fontsize=15, fontweight='bold',
            ha='center', va='center', family='sans-serif')

    # 11. Right Side Pill Vents
    vent_fill = 'white' if outline_only else '#0f172a'
    for vy in [-5.0, -1.5, 2.0, 5.5]:
        vent = patches.FancyBboxPatch((16.0 - 2.25, vy - 0.8), 4.5, 1.6,
                                     boxstyle='round,pad=0,rounding_size=0.7',
                                     facecolor=vent_fill, edgecolor='#0f172a', linewidth=1.6)
        ax.add_patch(vent)


def render_chibi_vector_image(output_path: str, outline_only: bool = False):
    """Renders pure 2D vector graphic at high resolution."""
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
    """Crops white border around the image and returns tight PIL Image."""
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


def split_into_6_blocks_big_numbers(full_img_path: str, out_grid_path: str, block_out_dir: str):
    """
    Splits the 2D illustration into 6 blocks with EXTRA LARGE, HIGH-VISIBILITY NUMBERS.
    """
    img = Image.open(full_img_path).convert('RGB')
    W, H = img.size

    dx = W / 3.0
    dy = H / 2.0

    grid_img = img.copy()
    draw = ImageDraw.Draw(grid_img)

    font_huge = ImageFont.truetype(FONT_PATH, size=58)
    font_large = ImageFont.truetype(FONT_PATH, size=32)
    font_medium = ImageFont.truetype(FONT_PATH, size=22)

    block_names_es = [
        "1. ANILLA DE VIAJE",
        "2. CEREBRO HPC&A",
        "3. RADIADOR SUPERIOR",
        "4. BOTA PCIE IZQUIERDA",
        "5. SONRISA KAWAII",
        "6. ESCAPE TURBO",
    ]

    block_num = 1
    for r in range(2):
        for c in range(3):
            x1 = int(round(c * dx))
            x2 = int(round((c + 1) * dx)) if c < 2 else W
            y1 = int(round(r * dy))
            y2 = int(round((r + 1) * dy)) if r < 1 else H

            piece = img.crop((x1, y1, x2, y2))

            pw, ph = piece.size
            # Card with large header for high-visibility number
            header_h = 68
            card = Image.new("RGB", (pw + 28, ph + header_h + 20), color=(255, 255, 255))
            card.paste(piece, (14, header_h + 8))
            cdraw = ImageDraw.Draw(card)

            # Outer border
            cdraw.rectangle([(4, 4), (pw + 23, ph + header_h + 15)], outline=(219, 39, 119), width=4)
            # Big Header Badge
            cdraw.rectangle([(10, 8), (pw + 18, header_h)], fill=(219, 39, 119))

            # EXTRA LARGE number badge in header:
            badge_txt = f"#{block_num}"
            cdraw.text((22, 14), badge_txt, fill=(255, 255, 255), font=font_large)
            title_txt = block_names_es[block_num - 1]
            cdraw.text((95, 20), title_txt, fill=(255, 255, 255), font=font_medium)

            block_file = os.path.join(block_out_dir, f"block_{block_num}.png")
            card.save(block_file)
            print(f"  Saved block #{block_num} with BIG number: {block_file}")

            block_num += 1

    # Draw dashed separating lines on master grid
    for c in range(1, 3):
        x = int(round(c * dx))
        for y in range(0, H, 20):
            draw.line([(x, y), (x, min(y + 12, H))], fill=(219, 39, 119), width=5)

    y = int(round(dy))
    for x in range(0, W, 20):
        draw.line([(x, y), (min(x + 12, W), y)], fill=(219, 39, 119), width=5)

    # Draw EXTRA LARGE numbered badges on the master grid image
    block_num = 1
    badge_radius = 48  # Large 96px diameter badge
    for r in range(2):
        for c in range(3):
            bx1 = int(round(c * dx)) + 24
            by1 = int(round(r * dy)) + 24
            bx2 = bx1 + badge_radius * 2
            by2 = by1 + badge_radius * 2

            # Badge pill shadow
            draw.ellipse([(bx1 + 3, by1 + 3), (bx2 + 3, by2 + 3)], fill=(15, 23, 42))
            # Main Badge Circle
            draw.ellipse([(bx1, by1), (bx2, by2)], fill=(219, 39, 119), outline=(255, 255, 255), width=4)

            # EXTRA LARGE BOLD NUMBER
            num_str = str(block_num)
            bbox = font_huge.getbbox(num_str)
            nw = bbox[2] - bbox[0]
            nh = bbox[3] - bbox[1]
            nx = bx1 + (badge_radius * 2 - nw) / 2.0 - bbox[0]
            ny = by1 + (badge_radius * 2 - nh) / 2.0 - bbox[1]
            draw.text((nx, ny), num_str, fill=(255, 255, 255), font=font_huge)

            block_num += 1

    grid_img.save(out_grid_path)
    print(f"  Saved master grid with EXTRA LARGE numbers: {out_grid_path}")


def main():
    print("Generating PURE 2D VECTOR Chibi GPU assets (100% mesh-free, big numbers)...")

    raw_2d = os.path.join(KIDS_DIR, "chibi_gpu_2d_full_color.png")
    raw_hero = os.path.join(KIDS_DIR, "chibi_gpu_2d_isometric_hero.png")
    raw_lineart = os.path.join(KIDS_DIR, "chibi_gpu_coloring_lineart.png")
    grid_img = os.path.join(KIDS_DIR, "chibi_gpu_2d_6blocks_grid.png")

    # 1. Pure 2D full color
    render_chibi_vector_image(raw_2d, outline_only=False)
    crop_to_content(raw_2d, margin=24)
    print(f"  Rendered pure 2D vector full color: {raw_2d}")

    # 2. Pure 2D clean line-art outline
    render_chibi_vector_image(raw_lineart, outline_only=True)
    crop_to_content(raw_lineart, margin=24)
    print(f"  Rendered pure 2D vector line-art: {raw_lineart}")

    # 3. Split into 6 blocks with EXTRA LARGE NUMBERS
    split_into_6_blocks_big_numbers(raw_2d, grid_img, KIDS_DIR)
    print("All pure 2D Chibi assets generated successfully!")


if __name__ == "__main__":
    main()
