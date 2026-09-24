#!/usr/bin/env python3
"""
GPU CON ESPADA 2D VECTOR ASSET GENERATOR (HPC&A FANTASY)
=======================================================
Pure 2D vector graphic generation (zero 3D mesh wireframe artifacts).
Generates:
1. High-resolution master illustration of the GPU with Sword Keychain.
2. 6-Block puzzle grids:
   - With Numbers (smart positions: top at top, bottom at bottom)
   - Without Numbers (pure artwork with dashed cutting lines only)
   - Rotated 90° versions to fill A4 page vertically
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
SWORD_GPU_DIR = os.path.join(KIDS_DIR, "gpu_sword_challenge")
os.makedirs(SWORD_GPU_DIR, exist_ok=True)

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def draw_gpu_sword_vector(output_png: str):
    """Draws a pure 2D vector illustration of the GPU with Sword."""
    fig, ax = plt.subplots(figsize=(15, 9.5), dpi=160)
    fig.patch.set_facecolor('#090d16')
    ax.set_facecolor('#090d16')

    # Coordinates: X: -36 to 36, Y: -24 to 24
    ax.set_xlim(-36, 36)
    ax.set_ylim(-24, 24)
    ax.set_aspect('equal')
    ax.axis('off')

    # Background subtle cyber grid
    for gx in np.linspace(-34, 34, 35):
        ax.plot([gx, gx], [-22, 22], color='#1e293b', lw=0.6, alpha=0.5, zorder=1)
    for gy in np.linspace(-22, 22, 23):
        ax.plot([-34, 34], [gy, gy], color='#1e293b', lw=0.6, alpha=0.5, zorder=1)

    # 1. MAIN GPU CHASSIS (Titanium Blue / Deep Slate)
    gpu_body = patches.FancyBboxPatch((-28.0, -14.0), 56.0, 28.0,
                                     boxstyle="round,pad=1.2",
                                     facecolor='#0f172a', edgecolor='#38bdf8', lw=2.4, zorder=2)
    ax.add_patch(gpu_body)

    # Shroud Accent Bevels
    shroud_top = patches.FancyBboxPatch((-26.5, 9.0), 53.0, 3.5, boxstyle="round,pad=0.4",
                                       facecolor='#1e293b', edgecolor='#64748b', lw=1.0, zorder=3)
    ax.add_patch(shroud_top)

    # 2. KEYRING HANGING EYELET AT TOP-LEFT (X = -27.5, Y = 13.5)
    eyelet_outer = patches.Circle((-27.5, 13.5), radius=5.2, facecolor='#f59e0b', edgecolor='#fde68a', lw=2.0, zorder=5)
    ax.add_patch(eyelet_outer)
    eyelet_inner = patches.Circle((-27.5, 13.5), radius=2.3, facecolor='#090d16', edgecolor='#b45309', lw=1.5, zorder=6)
    ax.add_patch(eyelet_inner)

    # 3. BOTTOM PCIe GOLD FINGERS
    pcie_tab = patches.Rectangle((-18.0, -17.5), 32.0, 3.2, facecolor='#b45309', edgecolor='#f59e0b', lw=1.5, zorder=4)
    ax.add_patch(pcie_tab)
    # Individual Gold Pins
    for px in np.linspace(-16.5, 12.5, 18):
        if abs(px - (-3.0)) > 1.5:  # PCIe Key Notch
            ax.plot([px, px], [-17.2, -14.5], color='#fde68a', lw=1.4, zorder=5)

    # 4. LEFT BAY: HIGH-TECH TURBINE HEATSINK FAN (Center X = -14.0, Y = -0.5)
    fan_well = patches.Circle((-14.0, -0.5), radius=10.5, facecolor='#020617', edgecolor='#0284c7', lw=2.2, zorder=4)
    ax.add_patch(fan_well)
    # Fan Hub
    fan_hub = patches.Circle((-14.0, -0.5), radius=3.8, facecolor='#0284c7', edgecolor='#38bdf8', lw=1.8, zorder=7)
    ax.add_patch(fan_hub)
    # 8 Curved Fan Blades (Cyan glow)
    for i in range(8):
        ang = np.radians(i * (360.0 / 8.0) + 15)
        bx1 = -14.0 + 3.8 * np.cos(ang)
        by1 = -0.5 + 3.8 * np.sin(ang)
        bx2 = -14.0 + 9.8 * np.cos(ang + 0.3)
        by2 = -0.5 + 9.8 * np.sin(ang + 0.3)
        ax.plot([bx1, bx2], [by1, by2], color='#06b6d4', lw=2.8, solid_capstyle='round', zorder=5)
        ax.plot([bx1, bx2], [by1, by2], color='#e0f2fe', lw=1.0, zorder=6)

    # Center Hub Logo
    ax.text(-14.0, -0.5, "GPU", color='#ffffff', fontsize=7.5, fontweight='bold',
            ha='center', va='center', zorder=8)

    # 5. RIGHT BAY: HEROIC CYBER ENERGY SWORD (Center X = 13.0)
    # Aura around sword
    sword_aura = patches.Polygon([
        (13.0, 14.5), (20.0, 3.0), (18.0, -12.0),
        (8.0, -12.0), (6.0, 3.0)
    ], closed=True, facecolor='#0284c7', alpha=0.25, zorder=3)
    ax.add_patch(sword_aura)

    # Energy Blade (Vertical, Point at Top Y = 13.5, Base at Y = -1.5)
    blade_outer = [
        (13.0, 13.5),   # Tip
        (16.8, 6.0),    # Upper edge
        (16.5, -1.5),   # Blade base right
        (9.5, -1.5),    # Blade base left
        (9.2, 6.0),     # Upper edge left
    ]
    blade_poly = patches.Polygon(blade_outer, closed=True, facecolor='#06b6d4', edgecolor='#e0f2fe', lw=2.0, zorder=7)
    ax.add_patch(blade_poly)

    # Blade Core Beam (Electric white)
    ax.plot([13.0, 13.0], [-1.0, 12.0], color='#ffffff', lw=2.0, zorder=8)

    # Blade Fuller with "HPC&A" Runes
    for i, ch in enumerate(["H", "P", "C", "&", "A"]):
        ax.text(13.0, 9.2 - i * 2.2, ch, color='#0f172a', fontsize=6.0, fontweight='bold',
                ha='center', va='center', zorder=9)

    # Winged Crossguard (Gold / Amber at Y = -2.5)
    guard_pts = [
        (13.0, -1.0),
        (21.5, 0.0),
        (22.0, -3.2),
        (16.5, -4.5),
        (9.5, -4.5),
        (4.0, -3.2),
        (4.5, 0.0),
    ]
    guard_poly = patches.Polygon(guard_pts, closed=True, facecolor='#d97706', edgecolor='#fde68a', lw=2.0, zorder=10)
    ax.add_patch(guard_poly)

    # Central Power Diamond on Guard
    guard_core = patches.RegularPolygon((13.0, -2.8), numVertices=4, radius=2.6,
                                       facecolor='#38bdf8', edgecolor='#ffffff', lw=1.2, zorder=11)
    ax.add_patch(guard_core)

    # Cyber Sword Grip (Y = -4.5 to -9.5)
    grip = patches.FancyBboxPatch((11.8, -9.5), 2.4, 5.0, boxstyle="round,pad=0.2",
                                  facecolor='#1e293b', edgecolor='#64748b', lw=1.2, zorder=8)
    ax.add_patch(grip)
    for gy in [-5.5, -7.0, -8.5]:
        ax.plot([11.8, 14.2], [gy, gy], color='#38bdf8', lw=1.0, zorder=9)

    # Pommel with Gold Gem (Y = -11.0)
    pommel = patches.Circle((13.0, -10.8), radius=2.2, facecolor='#f59e0b', edgecolor='#fef3c7', lw=1.5, zorder=10)
    ax.add_patch(pommel)

    # 6. TOP BREADBOARD / EMBLEM "HPC&A FANTASY GPU"
    ax.text(-2.0, 11.2, "⚔️ HPC&A GPU CON ESPADA ⚔️", color='#38bdf8', fontsize=8.5, fontweight='bold',
            ha='center', va='center', zorder=12)

    # Top Edge Cooling Fins
    for fx in np.linspace(-10.0, 3.0, 6):
        vent = patches.FancyBboxPatch((fx - 0.8, 6.5), 1.6, 3.2, boxstyle="round,pad=0.2",
                                     facecolor='#020617', edgecolor='#0284c7', lw=1.0, zorder=4)
        ax.add_patch(vent)

    plt.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
    fig.savefig(output_png, facecolor=fig.get_facecolor(), edgecolor='none', dpi=160)
    plt.close(fig)
    print(f"Generated Vector GPU con Espada: {output_png}")


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


def split_gpu_sword_into_6_blocks(full_img_path: str, out_grid_path: str, out_grid_no_num_path: str):
    """
    Splits into 6 blocks (3 columns x 2 rows):
    - With numbers version:
      * Row 0: numbers at TOP
      * Row 1: numbers at BOTTOM (پایین شکل)
      * Middle cut line unobstructed
    - Without numbers version:
      * Pure artwork with only dashed scissor cut lines!
    """
    img = Image.open(full_img_path).convert('RGB')
    W, H = img.size

    dx = W / 3.0
    dy = H / 2.0

    font_huge = ImageFont.truetype(FONT_PATH, size=52)
    font_scis = ImageFont.truetype(FONT_PATH, size=24)

    # --- VERSION 1: WITHOUT NUMBERS (Puzle Visual Puro) ---
    no_num_img = img.copy()
    draw_no_num = ImageDraw.Draw(no_num_img)

    # Vertical cut lines (2 lines)
    for c in range(1, 3):
        x = int(round(c * dx))
        for y in range(0, H, 20):
            draw_no_num.line([(x, y), (x, min(y + 11, H))], fill=(6, 182, 212), width=4)

    # Horizontal cut line through the middle
    y_mid = int(round(dy))
    for x in range(0, W, 20):
        draw_no_num.line([(x, y_mid), (min(x + 11, W), y_mid)], fill=(6, 182, 212), width=4)

    # Scissors markings along middle line
    draw_no_num.text((int(dx * 0.4), y_mid - 28), '✂ - - - - - - - -', fill=(6, 182, 212), font=font_scis)
    draw_no_num.text((int(dx * 1.4), y_mid - 28), '✂ - - - - - - - -', fill=(6, 182, 212), font=font_scis)
    draw_no_num.text((int(dx * 2.4), y_mid - 28), '✂ - - - - - - - -', fill=(6, 182, 212), font=font_scis)

    no_num_img.save(out_grid_no_num_path)
    print(f"  Saved No-Numbers Grid: {out_grid_no_num_path}")

    # --- VERSION 2: WITH NUMBERS (Modo Guiado) ---
    grid_img = no_num_img.copy()
    draw = ImageDraw.Draw(grid_img)

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
        # Cyan Badge
        draw.ellipse([(bx1, by1), (bx2, by2)], fill=(6, 182, 212), outline=(255, 255, 255), width=4)

        # Number
        num_str = str(i)
        bbox = font_huge.getbbox(num_str)
        nw = bbox[2] - bbox[0]
        nh = bbox[3] - bbox[1]
        nx = cx - nw / 2.0 - bbox[0]
        ny = cy - nh / 2.0 - bbox[1]
        draw.text((nx, ny), num_str, fill=(255, 255, 255), font=font_huge)

    grid_img.save(out_grid_path)
    print(f"  Saved With-Numbers Grid: {out_grid_path}")


def main():
    print("Generating GPU con Espada 2D Vector Illustration & 6-Block Grids...")
    master_png = os.path.join(KIDS_DIR, "gpu_sword_2d_master.png")
    grid_num_png = os.path.join(KIDS_DIR, "gpu_sword_2d_6blocks_grid.png")
    grid_no_num_png = os.path.join(KIDS_DIR, "gpu_sword_2d_6blocks_grid_no_num.png")

    draw_gpu_sword_vector(master_png)
    crop_image_tight(master_png, margin=20)
    split_gpu_sword_into_6_blocks(master_png, grid_num_png, grid_no_num_png)

    # Generate Rotated 90° versions for A4 full vertical coverage!
    im_num = Image.open(grid_num_png)
    im_num_rot = im_num.rotate(90, expand=True)
    rot_num_path = os.path.join(KIDS_DIR, "gpu_sword_2d_6blocks_grid_rot90.png")
    im_num_rot.save(rot_num_path)
    print(f"  Saved Rotated 90° With-Numbers: {rot_num_path}")

    im_no_num = Image.open(grid_no_num_png)
    im_no_num_rot = im_no_num.rotate(90, expand=True)
    rot_no_num_path = os.path.join(KIDS_DIR, "gpu_sword_2d_6blocks_grid_rot90_no_num.png")
    im_no_num_rot.save(rot_no_num_path)
    print(f"  Saved Rotated 90° No-Numbers: {rot_no_num_path}")

    print("GPU con Espada 2D assets generated successfully!")


if __name__ == "__main__":
    main()
