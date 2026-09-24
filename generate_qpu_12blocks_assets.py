#!/usr/bin/env python3
"""
GENERATE PURE 2D VECTOR ASSETS FOR QPU CHIP (100% MESH-FREE)
=============================================================
Generates ultra-clean, flat 2D graphic illustrations directly from CAD geometry:
- ZERO 3D mesh wireframe or black facets
- Rich gold, royal blue, and electric cyan quantum palette
- EXTRA LARGE, high-visibility numbers for students and teens
1. qpu_2d_full_color.png - Pure 2D vector colored QPU illustration
2. qpu_circuit_lineart.png - Clean blueprint circuit schematic
3. qpu_2d_12blocks_grid.png - 2D illustration with 12-block grid & EXTRA LARGE numbers
4. qpu_block_1.png to qpu_block_12.png - Individual cropped puzzle blocks with BIG numbers
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
QPU_DIR = os.path.join(KIDS_DIR, "qpu_advanced_12blocks")
os.makedirs(QPU_DIR, exist_ok=True)

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def draw_pure_2d_qpu(ax, outline_only=False):
    """Draws pure 2D vector geometry of Superconducting QPU Chip (zero mesh)."""
    # 1. Main Ceramic / Gold Package Body (48.0 x 36.0, fillet 3.0 mm)
    pkg_fill = 'white' if outline_only else '#d97706'
    pkg_edge = '#0f172a' if outline_only else '#92400e'
    pkg = patches.FancyBboxPatch((-24.0, -18.0), 48.0, 36.0,
                                boxstyle='round,pad=0,rounding_size=3.0',
                                facecolor=pkg_fill, edgecolor=pkg_edge, linewidth=2.8)
    ax.add_patch(pkg)

    if not outline_only:
        pkg_inner = patches.FancyBboxPatch((-22.5, -16.5), 45.0, 33.0,
                                          boxstyle='round,pad=0,rounding_size=2.2',
                                          facecolor='#f59e0b', edgecolor='#b45309', linewidth=1.5)
        ax.add_patch(pkg_inner)

    # 2. Keyring Eyelet Tab: (-27.5, 6.0), outer r=5.2, inner r=2.3
    eye_fill = 'white' if outline_only else '#f59e0b'
    eye_edge = '#0f172a' if outline_only else '#92400e'
    eyelet_outer = patches.Circle((-27.5, 6.0), 5.2, facecolor=eye_fill, edgecolor=eye_edge, linewidth=2.8)
    eyelet_inner = patches.Circle((-27.5, 6.0), 2.3, facecolor='white', edgecolor=eye_edge, linewidth=2.2)
    ax.add_patch(eyelet_outer)
    ax.add_patch(eyelet_inner)

    # 3. Top Branding Plaque: centered at (2.0, 13.8)
    plaque_fill = 'white' if outline_only else '#090d16'
    plaque_edge = '#0f172a' if outline_only else '#1e293b'
    plaque = patches.FancyBboxPatch((-13.0, 11.8), 30.0, 4.2,
                                   boxstyle='round,pad=0,rounding_size=1.2',
                                   facecolor=plaque_fill, edgecolor=plaque_edge, linewidth=1.6)
    ax.add_patch(plaque)
    txt_col = '#0f172a' if outline_only else '#fef08a'
    ax.text(2.0, 13.8, 'HPC&A QUANTUM', color=txt_col, fontsize=12, fontweight='bold',
            ha='center', va='center', family='sans-serif')

    # 4. Recessed Silicon Die Cavity: 28.0 x 24.0 at (2.0, -1.5)
    die_fill = 'white' if outline_only else '#0a0f1d'
    die_edge = '#0f172a' if outline_only else '#1e293b'
    die = patches.FancyBboxPatch((-12.0, -13.5), 28.0, 24.0,
                                boxstyle='round,pad=0,rounding_size=1.6',
                                facecolor=die_fill, edgecolor=die_edge, linewidth=2.2)
    ax.add_patch(die)

    # 5. Perimeter 28 Gold Wirebond Contact Pads
    pad_fill = 'white' if outline_only else '#fef08a'
    pad_edge = '#0f172a' if outline_only else '#ca8a04'
    wire_edge = '#0f172a' if outline_only else '#fbbf24'

    # Top pads (8):
    for x in np.linspace(-10.0, 14.0, 8):
        pad = patches.Rectangle((x - 0.7, 10.8), 1.4, 1.8, facecolor=pad_fill, edgecolor=pad_edge, linewidth=0.8)
        wire = patches.Polygon([[x, 10.8], [x, 9.8]], closed=False, edgecolor=wire_edge, linewidth=1.0)
        ax.add_patch(pad)
        ax.add_patch(wire)
    # Bottom pads (8):
    for x in np.linspace(-10.0, 14.0, 8):
        pad = patches.Rectangle((x - 0.7, -14.6), 1.4, 1.8, facecolor=pad_fill, edgecolor=pad_edge, linewidth=0.8)
        wire = patches.Polygon([[x, -12.8], [x, -11.8]], closed=False, edgecolor=wire_edge, linewidth=1.0)
        ax.add_patch(pad)
        ax.add_patch(wire)
    # Left pads (6):
    for y in np.linspace(-10.0, 7.0, 6):
        pad = patches.Rectangle((-14.1, y - 0.7), 1.8, 1.4, facecolor=pad_fill, edgecolor=pad_edge, linewidth=0.8)
        wire = patches.Polygon([[-12.3, y], [-11.3, y]], closed=False, edgecolor=wire_edge, linewidth=1.0)
        ax.add_patch(pad)
        ax.add_patch(wire)
    # Right pads (6):
    for y in np.linspace(-10.0, 7.0, 6):
        pad = patches.Rectangle((16.3, y - 0.7), 1.8, 1.4, facecolor=pad_fill, edgecolor=pad_edge, linewidth=0.8)
        wire = patches.Polygon([[16.3, y], [15.3, y]], closed=False, edgecolor=wire_edge, linewidth=1.0)
        ax.add_patch(pad)
        ax.add_patch(wire)

    # 6. Serpentine Coplanar Waveguide (CPW) Resonators
    cpw_color = '#0f172a' if outline_only else '#3b82f6'
    for r_y in [-7.5, -1.5, 4.5]:
        pts = []
        x_start = -9.5
        for s in range(5):
            xs = x_start + s * 4.6
            pts.extend([[xs, r_y - 1.2], [xs + 1.2, r_y + 1.2], [xs + 2.4, r_y - 1.2], [xs + 3.6, r_y + 1.2]])
        pts = np.array(pts)
        ax.plot(pts[:, 0], pts[:, 1], color=cpw_color, linewidth=2.0, solid_capstyle='round')

    # 7. 3x3 Transmon Qubits (Crosses)
    q_fill = 'white' if outline_only else '#06b6d4'
    q_edge = '#0f172a' if outline_only else '#22d3ee'
    dot_fill = 'white' if outline_only else '#fef08a'
    for qx in [-6.5, 2.0, 10.5]:
        for qy in [-7.5, -1.5, 4.5]:
            arm = 1.6
            w = 0.55
            h_cross = patches.Rectangle((qx - arm, qy - w/2), 2*arm, w, facecolor=q_fill, edgecolor=q_edge, linewidth=0.9)
            v_cross = patches.Rectangle((qx - w/2, qy - arm), w, 2*arm, facecolor=q_fill, edgecolor=q_edge, linewidth=0.9)
            ax.add_patch(h_cross)
            ax.add_patch(v_cross)
            jj = patches.Circle((qx, qy), 0.38, facecolor=dot_fill, edgecolor=q_edge, linewidth=0.6)
            ax.add_patch(jj)


def render_qpu_vector_image(output_path: str, outline_only: bool = False):
    """Renders pure 2D vector graphic of QPU chip at high resolution."""
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300, facecolor='white')
    ax.set_facecolor('white')

    draw_pure_2d_qpu(ax, outline_only=outline_only)

    ax.set_xlim(-34.5, 25.5)
    ax.set_ylim(-19.5, 19.5)
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


def split_into_12_blocks_big_numbers(full_img_path: str, out_grid_path: str, block_out_dir: str):
    """
    Splits the QPU illustration into 12 blocks with EXTRA LARGE, HIGH-VISIBILITY NUMBERS.
    """
    img = Image.open(full_img_path).convert('RGB')
    W, H = img.size

    dx = W / 4.0
    dy = H / 3.0

    grid_img = img.copy()
    draw = ImageDraw.Draw(grid_img)

    font_huge = ImageFont.truetype(FONT_PATH, size=48)
    font_large = ImageFont.truetype(FONT_PATH, size=28)
    font_medium = ImageFont.truetype(FONT_PATH, size=18)

    block_names_es = [
        "1. ANILLA & WIREBOND NW",
        "2. LOGO HPC&A & PADS N1",
        "3. LOGO QUANTUM & PADS N2",
        "4. ALMOHADILLAS NE",
        "5. BUS I/O & CÚBIT Q0",
        "6. RESONADOR CPW R0",
        "7. CÚBIT CENTRAL Q1",
        "8. ACOPLAMIENTO ESTE",
        "9. RETORNO TIERRA & Q2",
        "10. RESONADOR CPW R2",
        "11. LÍNEA FLUX Z & PADS S1",
        "12. ALMOHADILLAS SE",
    ]

    block_num = 1
    for r in range(3):
        for c in range(4):
            x1 = int(round(c * dx))
            x2 = int(round((c + 1) * dx)) if c < 3 else W
            y1 = int(round(r * dy))
            y2 = int(round((r + 1) * dy)) if r < 2 else H

            piece = img.crop((x1, y1, x2, y2))

            pw, ph = piece.size
            header_h = 58
            card = Image.new("RGB", (pw + 24, ph + header_h + 16), color=(255, 255, 255))
            card.paste(piece, (12, header_h + 8))
            cdraw = ImageDraw.Draw(card)

            # Outer border
            cdraw.rectangle([(4, 4), (pw + 19, ph + header_h + 11)], outline=(2, 132, 199), width=3)
            # Header Badge
            cdraw.rectangle([(8, 8), (pw + 15, header_h)], fill=(2, 132, 199))

            # EXTRA LARGE number badge in header:
            badge_txt = f"#{block_num}"
            cdraw.text((16, 12), badge_txt, fill=(255, 255, 255), font=font_large)
            title_txt = block_names_es[block_num - 1]
            cdraw.text((78, 18), title_txt, fill=(255, 255, 255), font=font_medium)

            block_file = os.path.join(block_out_dir, f"qpu_block_{block_num}.png")
            card.save(block_file)
            print(f"  Saved QPU block #{block_num} with BIG number: {block_file}")

            block_num += 1

    # Draw vertical dashed lines on master grid
    for c in range(1, 4):
        x = int(round(c * dx))
        for y in range(0, H, 18):
            draw.line([(x, y), (x, min(y + 10, H))], fill=(2, 132, 199), width=4)

    # Draw horizontal dashed lines
    for r in range(1, 3):
        y = int(round(r * dy))
        for x in range(0, W, 18):
            draw.line([(x, y), (min(x + 10, W), y)], fill=(2, 132, 199), width=4)

    # Draw EXTRA LARGE numbered badges on the master grid image
    block_num = 1
    badge_radius = 40  # 80px diameter badge
    for r in range(3):
        for c in range(4):
            bx1 = int(round(c * dx)) + 20
            by1 = int(round(r * dy)) + 20
            bx2 = bx1 + badge_radius * 2
            by2 = by1 + badge_radius * 2

            # Badge shadow
            draw.ellipse([(bx1 + 3, by1 + 3), (bx2 + 3, by2 + 3)], fill=(9, 13, 22))
            # Main Badge Circle
            draw.ellipse([(bx1, by1), (bx2, by2)], fill=(2, 132, 199), outline=(255, 255, 255), width=3)

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
    print(f"  Saved master QPU grid with EXTRA LARGE numbers: {out_grid_path}")


def main():
    print("Generating PURE 2D VECTOR QPU assets (100% mesh-free, big numbers)...")

    raw_2d = os.path.join(QPU_DIR, "qpu_2d_full_color.png")
    raw_lineart = os.path.join(QPU_DIR, "qpu_circuit_lineart.png")
    grid_img = os.path.join(QPU_DIR, "qpu_2d_12blocks_grid.png")

    # 1. Pure 2D full color
    render_qpu_vector_image(raw_2d, outline_only=False)
    crop_to_content(raw_2d, margin=24)
    print(f"  Rendered pure 2D vector full color QPU: {raw_2d}")

    # 2. Pure 2D clean blueprint line-art outline
    render_qpu_vector_image(raw_lineart, outline_only=True)
    crop_to_content(raw_lineart, margin=24)
    print(f"  Rendered pure 2D vector line-art QPU: {raw_lineart}")

    # 3. Split into 12 blocks with EXTRA LARGE NUMBERS
    split_into_12_blocks_big_numbers(raw_2d, grid_img, QPU_DIR)
    print("All pure 2D QPU assets generated successfully!")


if __name__ == "__main__":
    main()
