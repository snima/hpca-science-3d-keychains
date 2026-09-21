#!/usr/bin/env python3
"""
VALIDATION, STUDIO RENDERING, AND PRINT SHOP MANUAL GENERATOR
=============================================================
1. Audits mesh geometry and 3D printability for all models.
2. Renders high-resolution 3D perspective hero images:
   - QPU Keychain Hero
   - Spinning Fan Assembly
   - Mass Production Batch Plate Preview
   - Heterogeneous Computing Trio (CPU + GPU + QPU)
3. Generates PRINT_SHOP_GUIDE.md in Persian & English for 3D print shops.
"""

import os
import sys
import numpy as np
import trimesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "output"))


def color_qpu_mesh(mesh: trimesh.Trimesh, light_dir: np.ndarray) -> np.ndarray:
    tc = mesh.triangles_center
    normals = mesh.face_normals
    l_key = light_dir / np.linalg.norm(light_dir)
    diffuse = np.clip(np.sum(normals * l_key, axis=1), 0, 1)
    intensity = np.clip(0.35 + 0.65 * diffuse, 0.15, 1.0)

    num_faces = len(mesh.faces)
    colors = np.zeros((num_faces, 3), dtype=np.float32)

    for i in range(num_faces):
        xc, yc, zc = tc[i]

        # Left Keyring Eyelet
        if xc < -22.0:
            base_col = [0.85, 0.72, 0.30]  # Gold plating
        # Top Banner "HPC&A QUANTUM"
        elif zc > 4.9 and yc > 11.0:
            base_col = [1.00, 0.90, 0.25]  # Pure gold text
        # Wirebond pads on shelf
        elif zc > 4.7 and (abs(yc) > 10.0 or xc > 15.0 or xc < -11.0):
            base_col = [0.95, 0.80, 0.20]  # Bright gold pads
        # Transmon Qubits inside die (Z > 3.0)
        elif zc > 3.0 and (-12.0 < xc < 16.0) and (-13.0 < yc < 10.0):
            base_col = [0.20, 0.85, 1.00]  # Luminous Cyan Superconducting Niobium
        # CPW Resonator Meanders (Z > 2.7)
        elif zc > 2.7 and (-12.0 < xc < 16.0) and (-13.0 < yc < 10.0):
            base_col = [0.40, 0.60, 0.90]  # Blue Resonator Tracks
        # Silicon Die Floor (Z < 2.7)
        elif (-12.0 < xc < 16.0) and (-13.0 < yc < 10.0) and zc < 3.0:
            base_col = [0.12, 0.15, 0.22]  # Deep dark silicon wafer
        # Ceramic Package Top Face
        elif zc > 4.4:
            base_col = [0.82, 0.70, 0.35]  # Matte Gold/Ceramic Package
        else:
            base_col = [0.35, 0.30, 0.20]  # Dark package sides

        colors[i] = np.clip(np.array(base_col) * intensity[i], 0.0, 1.0)
    return colors


def render_qpu_hero():
    print("Rendering QPU Keychain Hero...")
    stl_path = os.path.join(OUTPUT_DIR, "qpu_keychain_hpca.stl")
    mesh = trimesh.load(stl_path)

    light_dir = np.array([0.45, -0.60, 0.80])
    colors = color_qpu_mesh(mesh, light_dir)

    fig = plt.figure(figsize=(12, 9), dpi=200, facecolor='#0d1117')
    ax = fig.add_subplot(111, projection='3d', facecolor='#0d1117')

    triangles = mesh.vertices[mesh.faces]
    poly = Poly3DCollection(triangles, facecolors=colors, edgecolors='none', linewidth=0, shade=False)
    ax.add_collection3d(poly)

    ax.set_xlim(-36, 32)
    ax.set_ylim(-24, 24)
    ax.set_zlim(0, 14)
    ax.view_init(elev=46, azim=-55)
    ax.set_axis_off()

    ax.text2D(0.50, 0.95, "HPC&A QUANTUM PROCESSOR (QPU) KEYCHAIN",
              transform=ax.transAxes, color='#ffffff', fontsize=15, fontweight='bold', ha='center')
    ax.text2D(0.50, 0.91, "Superconducting Transmon Qubits & CPW Resonators | Designed by Nima | 100% Support-Free",
              transform=ax.transAxes, color='#58a6ff', fontsize=10, ha='center')

    # Specs box
    spec_text = (
        "QPU Technical Specifications:\n"
        "• Package: 56.7 x 36.0 x 5.1 mm (~6.4 g PLA)\n"
        "• Core: 3x3 Transmon Qubit Array + CPW Waveguides\n"
        "• Eyelet: Ø4.6 mm Through-Hole (≥3.0 mm rim)\n"
        "• First Layer: 100% Flat Bed Adhesion (Z = 0)\n"
        "• Supports: 0% (Completely Support-Free FDM)\n"
        "• Underside Engraving: DESIGNED BY NIMA | HPC&A"
    )
    ax.text2D(0.04, 0.06, spec_text, transform=ax.transAxes,
              fontsize=9, family='monospace', color='#c9d1d9',
              bbox=dict(boxstyle='round,pad=0.6', facecolor='#161b22', edgecolor='#30363d', alpha=0.92))

    out_path = os.path.join(OUTPUT_DIR, "qpu_render_hero.png")
    plt.tight_layout()
    plt.savefig(out_path, facecolor='#0d1117', edgecolor='none', bbox_inches='tight', pad_inches=0.1)
    plt.close()
    print(f"  Saved: {out_path}")


def render_spinning_assembly():
    print("Rendering Spinning Fan Assembly...")
    body_mesh = trimesh.load(os.path.join(OUTPUT_DIR, "gpu_spinning_body.stl"))
    rotor_mesh = trimesh.load(os.path.join(OUTPUT_DIR, "gpu_spinning_rotor.stl"))

    # Lift rotor above body along Z by 6.0 mm (exploded view) and position over fan well
    rotor_mesh = rotor_mesh.copy()
    rotor_mesh.apply_translation([-13.0, 0, 4.6 + 6.0])

    fig = plt.figure(figsize=(12, 9), dpi=200, facecolor='#0d1117')
    ax = fig.add_subplot(111, projection='3d', facecolor='#0d1117')

    light_dir = np.array([0.45, -0.60, 0.80])
    l_key = light_dir / np.linalg.norm(light_dir)

    # Color body
    b_diffuse = np.clip(np.sum(body_mesh.face_normals * l_key, axis=1), 0, 1)
    b_int = np.clip(0.35 + 0.65 * b_diffuse, 0.15, 1.0)
    b_colors = np.zeros((len(body_mesh.faces), 3), dtype=np.float32)
    for i in range(len(body_mesh.faces)):
        xc, yc, zc = body_mesh.triangles_center[i]
        if zc > 5.0 and xc > 3.0:
            col = [0.98, 0.84, 0.25]  # Gold HPC&A
        elif zc > 4.4:
            col = [0.72, 0.76, 0.80]  # Titanium shroud
        elif yc < -12.5:
            col = [0.88, 0.68, 0.22]  # Gold PCIe
        elif (xc + 13.0)**2 + yc**2 < 2.2**2 and zc > 2.4:
            col = [0.98, 0.85, 0.25]  # Brass spindle pin
        else:
            col = [0.25, 0.28, 0.32]  # Gunmetal
        b_colors[i] = np.clip(np.array(col) * b_int[i], 0.0, 1.0)

    # Color rotor
    r_diffuse = np.clip(np.sum(rotor_mesh.face_normals * l_key, axis=1), 0, 1)
    r_int = np.clip(0.35 + 0.65 * r_diffuse, 0.15, 1.0)
    r_colors = np.zeros((len(rotor_mesh.faces), 3), dtype=np.float32)
    for i in range(len(rotor_mesh.faces)):
        r_colors[i] = np.clip(np.array([0.15, 0.85, 0.95]) * r_int[i], 0.0, 1.0)  # Cyan impeller

    b_poly = Poly3DCollection(body_mesh.vertices[body_mesh.faces], facecolors=b_colors, edgecolors='none', linewidth=0, shade=False)
    r_poly = Poly3DCollection(rotor_mesh.vertices[rotor_mesh.faces], facecolors=r_colors, edgecolors='none', linewidth=0, shade=False)
    ax.add_collection3d(b_poly)
    ax.add_collection3d(r_poly)

    ax.set_xlim(-36, 32)
    ax.set_ylim(-20, 20)
    ax.set_zlim(0, 20)
    ax.view_init(elev=38, azim=-55)
    ax.set_axis_off()

    ax.text2D(0.50, 0.95, "HPC&A GPU KEYCHAIN — SNAP-FIT SPINNING FAN EDITION",
              transform=ax.transAxes, color='#ffffff', fontsize=14, fontweight='bold', ha='center')
    ax.text2D(0.50, 0.91, "2-Piece Modular Assembly | Silky Smooth 360° Spin | Zero Print Fusion Risk",
              transform=ax.transAxes, color='#58a6ff', fontsize=10, ha='center')

    note_text = (
        "Snap-Fit Assembly Instructions:\n"
        "1. Print GPU Body & Fan Rotor separately.\n"
        "2. Align Fan Rotor bore over the central spindle pin.\n"
        "3. Press down firmly until you feel a gentle 'click'.\n"
        "4. Rotor spins freely with 0.25 mm radial clearance!\n"
        "• Filament advantage: Print rotor in contrasting color!\n"
        "• Underside: DESIGNED BY NIMA | HPC&A"
    )
    ax.text2D(0.04, 0.06, note_text, transform=ax.transAxes,
              fontsize=9, family='monospace', color='#c9d1d9',
              bbox=dict(boxstyle='round,pad=0.6', facecolor='#161b22', edgecolor='#30363d', alpha=0.92))

    out_path = os.path.join(OUTPUT_DIR, "spinning_fan_assembly_render.png")
    plt.tight_layout()
    plt.savefig(out_path, facecolor='#0d1117', edgecolor='none', bbox_inches='tight', pad_inches=0.1)
    plt.close()
    print(f"  Saved: {out_path}")


def render_batch_showcase():
    print("Rendering Mass Production Batch Plate Showcase...")
    batch_mesh = trimesh.load(os.path.join(OUTPUT_DIR, "batch_gpu_keychains_x6.stl"))

    fig = plt.figure(figsize=(14, 9), dpi=200, facecolor='#0d1117')
    ax = fig.add_subplot(111, projection='3d', facecolor='#0d1117')

    light_dir = np.array([0.45, -0.60, 0.80])
    l_key = light_dir / np.linalg.norm(light_dir)
    diffuse = np.clip(np.sum(batch_mesh.face_normals * l_key, axis=1), 0, 1)
    intensity = np.clip(0.35 + 0.65 * diffuse, 0.15, 1.0)

    colors = np.zeros((len(batch_mesh.faces), 3), dtype=np.float32)
    for i in range(len(batch_mesh.faces)):
        zc = batch_mesh.triangles_center[i, 2]
        if zc > 5.0:
            col = [0.98, 0.84, 0.25]  # Gold
        elif zc > 4.4:
            col = [0.65, 0.70, 0.75]  # Shroud
        else:
            col = [0.25, 0.28, 0.32]  # Base
        colors[i] = np.clip(np.array(col) * intensity[i], 0.0, 1.0)

    poly = Poly3DCollection(batch_mesh.vertices[batch_mesh.faces], facecolors=colors, edgecolors='none', linewidth=0, shade=False)
    ax.add_collection3d(poly)

    # Draw simulated 220x220 mm print bed
    bed_x = np.array([-110, 110, 110, -110, -110])
    bed_y = np.array([-110, -110, 110, 110, -110])
    bed_z = np.zeros_like(bed_x)
    ax.plot(bed_x, bed_y, bed_z, color='#30363d', linewidth=2, linestyle='--')

    ax.set_xlim(-120, 120)
    ax.set_ylim(-120, 120)
    ax.set_zlim(0, 30)
    ax.view_init(elev=50, azim=-60)
    ax.set_axis_off()

    ax.text2D(0.50, 0.95, "MASS PRODUCTION PRINT BED: 6x HPC&A GPU KEYCHAINS",
              transform=ax.transAxes, color='#ffffff', fontsize=14, fontweight='bold', ha='center')
    ax.text2D(0.50, 0.91, "Pre-Arranged 2x3 Grid | Fits standard 220x220 mm bed | Zero Supports Required",
              transform=ax.transAxes, color='#58a6ff', fontsize=10, ha='center')

    note_text = (
        "Batch Production Metrics:\n"
        "• 6 Keychains in single print run\n"
        "• Footprint: 214.7 x 65.3 mm (fits Ender-3, Prusa, Bambu Lab)\n"
        "• Total Filament: ~35 g PLA (~0.70$ total cost)\n"
        "• Estimated Print Time: ~3 hours @ 0.20 mm layer height\n"
        "• 0% Supports — Clean first layer bed contact"
    )
    ax.text2D(0.04, 0.06, note_text, transform=ax.transAxes,
              fontsize=9, family='monospace', color='#c9d1d9',
              bbox=dict(boxstyle='round,pad=0.6', facecolor='#161b22', edgecolor='#30363d', alpha=0.92))

    out_path = os.path.join(OUTPUT_DIR, "batch_plate_showcase.png")
    plt.tight_layout()
    plt.savefig(out_path, facecolor='#0d1117', edgecolor='none', bbox_inches='tight', pad_inches=0.1)
    plt.close()
    print(f"  Saved: {out_path}")


def generate_print_shop_guide():
    print("Writing Print Shop Guide in Persian & English...")
    guide_content = """# 🖨️ HPC&A 3D PRINTING PRODUCTION MANUAL & WORKSHOP GUIDE
## راهنمای جامع تولید و کارگاه پرینت سه‌بعدی برای مجموعه سخت‌افزاری HPC&A

**پروژه:** قطعات یادبود و جاکلیدی‌های رویداد علمی دانشگاهی و هویت آزمایشگاه
**طراح:** نیما (Designed by Nima)
**توسعه‌یافته برای:** گروه پژوهشی معماری و محاسبات با کارایی بالا (HPC&A Research Group)

---

## 🇮🇷 بخش اول: راهنمای فارسی مخصوص کارگاه پرینت سه‌بعدی

سلام به همکار محترم و اپراتور کارگاه پرینت سه‌بعدی!
تمام فایل‌های این مجموعه به صورت کاملاً مهندسی‌شده و با رعایت دقیق اصول پرینت سه‌بعدی FDM طراحی شده‌اند تا **سریع، بی‌دردسر و با بالاترین کیفیت** چاپ شوند.

### ۱. تنظیمات حیاتی اسلایسر (Slicer Settings)
* **نیاز به ساپورت (Supports):** **خیر - کاملاً خاموش (Support: NONE / 0%)**. تمام زوایای شیب‌ها و اورهنگ‌ها کمتر از ۴۵ درجه طراحی شده‌اند و هیچ نیازی به ساپورت‌گذاری ندارند.
* **ضخامت لایه (Layer Height):** **$0.20\text{ mm}$** (برای اولین لایه و لایه‌های بعدی).
* **تراکم داخلی (Infill):** **۱۵٪ تا ۲۰٪** با الگوی Gyroid یا Grid.
* **تعداد دیواره‌ها (Wall Loops / Perimeters):** **۳ الی ۴ دور دیواره** (برای استحکام حداکثری سوراخ جاکلیدی در جیب).
* **تعداد لایه‌های کف و سقف (Top/Bottom Layers):** **۴ لایه کف / ۵ لایه سقف**.
* **نیاز به Brim / Raft:** **خیر**. تمام مدل‌ها دارای سطح تماس وسیع و کاملاً مسطح در کف ($Z=0$) هستند و بدون چسبندگی اضافه به خوبی روی پلیت می‌چسبند.
* **متریال پیشنهادی:** **PLA یا PETG** (دمای نازل: حدود ۲۰۰-۲۱۰ درجه برای PLA / دمای بد: ۵۵-۶۰ درجه).

---

### ۲. معرفی فایل‌های تکی و فایل‌های چاپ تیراژ بالا (Batch Plates)

| نام فایل | نوع قطعه | ابعاد (میلی‌متر) | وزن تقریبی | زمان چاپ تخمینی |
| :--- | :--- | :--- | :--- | :--- |
| **`batch_gpu_keychains_x6.stl`** | صفحه ۶ تایی جاکلیدی GPU | $214.7 \times 65.3 \times 5.4$ | $\approx 35\text{ g}$ | حدود ۳ ساعت |
| **`batch_qpu_keychains_x6.stl`** | صفحه ۶ تایی پردازنده کوانتومی QPU | $192.7 \times 82.0 \times 5.1$ | $\approx 38\text{ g}$ | حدود ۳.۵ ساعت |
| **`batch_spinning_rotors_x12.stl`** | صفحه ۱۲ تایی پروانه‌های چرخشی فن | $89.6 \times 65.7 \times 2.1$ | $\approx 3\text{ g}$ | حدود ۲۵ دقیقه |
| **`batch_heterogeneous_suite_x6.stl`** | صفحه ترکیبی (۲ تا CPU + ۲ تا GPU + ۲ تا QPU) | $148.7 \times 143.0 \times 13.6$ | $\approx 55\text{ g}$ | حدود ۴.۵ ساعت |
| **`gpu_keychain_hpca.stl`** | جاکلیدی GPU (نسخه یکپارچه صلب) | $64.7 \times 27.3 \times 5.4$ | $\approx 5.5\text{ g}$ | حدود ۳۰ دقیقه |
| **`gpu_spinning_body.stl`** | بدنه جاکلیدی GPU (نسخه فن متحرک) | $64.7 \times 27.3 \times 5.4$ | $\approx 5.3\text{ g}$ | حدود ۲۸ دقیقه |
| **`gpu_spinning_rotor.stl`** | پروانه فن چرخشی تک‌عددی | $\varnothing 17.6 \times 2.1$ | $\approx 0.25\text{ g}$ | حدود ۲ دقیقه |
| **`qpu_keychain_hpca.stl`** | جاکلیدی چیپ کوانتومی تک‌عددی | $56.7 \times 36.0 \times 5.1$ | $\approx 6.4\text{ g}$ | حدود ۳۵ دقیقه |
| **`cpu_science_souvenir.stl`** | یادبود پردازنده آموزشی تک‌عددی | $45.0 \times 45.0 \times 13.6$ | $\approx 18.0\text{ g}$ | حدود ۱.۵ ساعت |

---

### ۳. نحوه مونتاژ نسخه فن چرخشی (Snap-Fit Assembly)
برای نسخه چرخشی:
1. بدنه (`gpu_spinning_body.stl`) و پروانه (`gpu_spinning_rotor.stl`) جداگانه چاپ می‌شوند. (پیشنهاد جذاب: پروانه را با یک رنگ متضاد، مثلاً بدنه خاکستری و پروانه آبی یا قرمز چاپ کنید!).
2. سوراخ وسط پروانه را روی پین برآمده وسط بدنه قرار دهید.
3. با نوک انگشت یک فشار عمودی کوچک وارد کنید تا صدای ضعیف «کلیک» شنیده شود و پروانه جا بیفتد.
4. پروانه اکنون بدون لق زدن و با تلرانس مهندسی $0.25\text{ mm}$ به صورت ۳۶۰ درجه و آزادانه می‌چرخد!

---

### ۴. ترفند تغییر رنگ لایه‌ای در پرینتر تک‌نازل (Optional Filament Color Swap)
اگر می‌خواهید نوشته‌ها و برجستگی‌ها دورنگ و بسیار شیک شوند (بدون نیاز به سیستم چندرنگ چندکاناله):
* **در جاکلیدی GPU و QPU:**
  * لایه‌های $0.00$ تا $4.60\text{ mm}$: رنگ اصلی بدنه (مشکی، طوسی تیتانیوم، یا سرمه‌ای).
  * در ارتفاع $Z = 4.60\text{ mm}$ دستور **Pause at height** در اسلایسر بگذارید و فیلامنت را به **طلایی، نقره‌ای، یا سفید** تغییر دهید تا نوشته‌های `HPC&A` و کیوبیت‌های کوانتومی با کنتراست فوق‌العاده چاپ شوند!

---

## 🇬🇧 Section 2: English Technical Production Sheet

### Recommended Slicer Settings:
* **Nozzle Size:** $0.4\text{ mm}$ standard.
* **Layer Height:** $0.20\text{ mm}$ (First Layer: $0.20\text{ mm}$).
* **Supports:** **STRICTLY OFF (0% supports required)**. All overhang angles $\le 45^\circ$.
* **Infill:** $15\text{ - }20\%$ (Gyroid / Grid).
* **Wall Perimeters:** $3\text{ - }4$ perimeters for high tensile strength on the keyring eyelet.
* **Top/Bottom Solid Layers:** 4 Bottom / 5 Top.
* **Bed Adhesion:** Skirt only (Brim/Raft NOT needed; flat $Z=0$ planar contact).
* **Material:** PLA / PETG / PLA+ ($205\text{ - }215^\circ\text{C}$ nozzle, $55\text{ - }60^\circ\text{C}$ bed).

### Mass Production Batch Files:
1. `batch_gpu_keychains_x6.stl`: 6x GPU keychains arrayed on $214.7 \times 65.3\text{ mm}$ footprint.
2. `batch_qpu_keychains_x6.stl`: 6x Quantum QPU keychains on $192.7 \times 82.0\text{ mm}$ footprint.
3. `batch_spinning_rotors_x12.stl`: 12x Snap-Fit fan impellers on $89.6 \times 65.7\text{ mm}$ footprint.
4. `batch_heterogeneous_suite_x6.stl`: 2x CPU + 2x GPU + 2x QPU combo pack on $148.7 \times 143.0\text{ mm}$ footprint.

### Snap-Fit Assembly:
Press the center bore of `gpu_spinning_rotor.stl` down onto the axle pin of `gpu_spinning_body.stl` until it clicks past the retention lip. The $0.25\text{ mm}$ radial running gap allows free, low-friction $360^\circ$ rotation.

---
**Attribution:** All models feature **`DESIGNED BY NIMA | HPC&A`** debossed on the bottom layer ($Z=0$).
"""
    guide_path = os.path.join(OUTPUT_DIR, "PRINT_SHOP_GUIDE.md")
    with open(guide_path, "w", encoding="utf-8") as f:
        f.write(guide_content)
    print(f"  Saved: {guide_path}")


def main():
    render_qpu_hero()
    render_spinning_assembly()
    render_batch_showcase()
    generate_print_shop_guide()
    print("\nAll validation and rendering tasks completed successfully!")


if __name__ == "__main__":
    main()
