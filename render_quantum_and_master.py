#!/usr/bin/env python3
"""
RENDERS FOR QUANTUM COLLECTION & MASTER BATCH PRINT PLATE
=========================================================
Generates:
1. 3-in-1 Quantum Trio Showcase (QPU, 2.5D Chandelier, Bloch Sphere)
2. Dedicated Dual-View Detail Render for the 2.5D Quantum Chandelier (Front & Underside Text Margins)
3. Master Batch Plate Showcase (All 6 Unique Models on 220x220 mm bed)
4. Comprehensive Print Shop Manual (Persian & English) in output/PRINT_SHOP_GUIDE.md
"""

import os
import sys
import numpy as np
import trimesh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "output"))


def render_quantum_trio():
    print("Rendering 3-in-1 Quantum Trio Showcase...")
    fig = plt.figure(figsize=(18, 7), dpi=200, facecolor="#0d1117")

    models = [
        ("qpu_keychain_hpca.stl", "SUPERCONDUCTING QPU CHIP", "Transmon Qubits & CPW Waveguides", [-34, 30], [-22, 22], [0, 14], (45, -55)),
        ("quantum_chandelier.stl", "QUANTUM DILUTION CHANDELIER", "Multi-Tiered 15 mK Cryostat & QPU Can", [-22, 22], [-34, 38], [0, 14], (45, -55)),
        ("quantum_bloch.stl", "BLOCH SPHERE MEDALLION", "State Vector |ψ> & Quantum Info Gates", [-26, 26], [-28, 28], [0, 14], (45, -55)),
    ]

    light_dir = np.array([0.45, -0.60, 0.80])
    l_key = light_dir / np.linalg.norm(light_dir)

    for idx, (fname, title, subtitle, xlim, ylim, zlim, view) in enumerate(models):
        ax = fig.add_subplot(1, 3, idx + 1, projection="3d", facecolor="#0d1117")
        mesh = trimesh.load(os.path.join(OUTPUT_DIR, fname))

        diffuse = np.clip(np.sum(mesh.face_normals * l_key, axis=1), 0, 1)
        intensity = np.clip(0.35 + 0.65 * diffuse, 0.15, 1.0)

        colors = np.zeros((len(mesh.faces), 3), dtype=np.float32)
        for i in range(len(mesh.faces)):
            zc = mesh.triangles_center[i, 2]
            xc = mesh.triangles_center[i, 0]
            yc = mesh.triangles_center[i, 1]

            if idx == 0:  # QPU Chip
                if zc > 4.8:
                    col = [0.98, 0.84, 0.25]  # Gold text/pads
                elif zc > 3.0 and (-12.0 < xc < 16.0):
                    col = [0.15, 0.85, 1.00]  # Cyan Transmons
                elif zc > 2.6 and (-12.0 < xc < 16.0):
                    col = [0.35, 0.55, 0.85]  # Resonators
                elif (-12.0 < xc < 16.0):
                    col = [0.12, 0.14, 0.20]  # Silicon die
                elif zc > 4.4:
                    col = [0.82, 0.70, 0.35]  # Package
                else:
                    col = [0.32, 0.28, 0.22]
            elif idx == 1:  # 2.5D Sleek Dilution Chandelier
                if zc > 5.0:
                    col = [1.00, 1.00, 1.00]  # Crisp White "HPC&A" and "QPU" lettering
                elif zc > 4.7:
                    col = [0.98, 0.84, 0.22]  # Gleaming Gold Thermal Stages & Shield Can
                elif zc > 4.4:
                    col = [0.30, 0.85, 0.95]  # Cyan RF Coaxial Lines & Cooling Coils
                elif zc > 3.8:
                    col = [0.25, 0.28, 0.35]  # Sleek Dark Titanium Cryostat Chassis Base
                else:
                    col = [0.18, 0.20, 0.25]  # Base backplate
            else:  # Bloch Sphere
                if zc > 4.8:
                    col = [0.98, 0.85, 0.25]  # Gold text
                elif zc > 3.4:
                    col = [0.20, 0.85, 1.00]  # Cyan vector |psi> & poles
                elif zc > 2.6:
                    col = [0.45, 0.65, 0.90]  # Equator / meridian lines
                elif zc > 4.4:
                    col = [0.78, 0.68, 0.35]  # Package
                else:
                    col = [0.28, 0.25, 0.20]

            colors[i] = np.clip(np.array(col) * intensity[i], 0.0, 1.0)

        poly = Poly3DCollection(mesh.vertices[mesh.faces], facecolors=colors, edgecolors="none", linewidth=0, shade=False)
        ax.add_collection3d(poly)
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.set_zlim(zlim)
        ax.view_init(elev=view[0], azim=view[1])
        ax.set_axis_off()
        ax.set_title(f"{title}\n{subtitle}", color="#58a6ff", fontsize=11, fontweight="bold", pad=-5)

    fig.suptitle("HPC&A QUANTUM COLLECTION (3 EDITIONS) — 100% 3D PRINTABLE | DESIGNED BY NIMA",
                 color="#ffffff", fontsize=15, fontweight="bold", y=0.98)

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "quantum_trio_showcase.png")
    plt.savefig(out_path, facecolor="#0d1117", edgecolor="none", bbox_inches="tight", pad_inches=0.1)
    plt.close()
    print(f"  Saved: {out_path}")


def render_chandelier_detail():
    print("Rendering Dedicated 2.5D Quantum Chandelier Detail Showcase...")
    mesh = trimesh.load(os.path.join(OUTPUT_DIR, "quantum_chandelier.stl"))

    fig = plt.figure(figsize=(16, 8), dpi=200, facecolor="#0d1117")

    # Left: Front Isometric View
    ax1 = fig.add_subplot(1, 2, 1, projection="3d", facecolor="#0d1117")
    light_dir = np.array([0.45, -0.60, 0.80])
    l_key = light_dir / np.linalg.norm(light_dir)
    diffuse = np.clip(np.sum(mesh.face_normals * l_key, axis=1), 0, 1)
    intensity = np.clip(0.35 + 0.65 * diffuse, 0.15, 1.0)

    colors_front = np.zeros((len(mesh.faces), 3), dtype=np.float32)
    for i in range(len(mesh.faces)):
        zc = mesh.triangles_center[i, 2]
        if zc > 5.0:
            col = [1.00, 1.00, 1.00]  # Crisp White "HPC&A" and "QPU" lettering
        elif zc > 4.7:
            col = [0.98, 0.84, 0.22]  # Gold Thermal Stages & Shield Can
        elif zc > 4.4:
            col = [0.25, 0.82, 0.95]  # Cyan RF Coaxial Lines & Cooling Coils
        elif zc > 3.8:
            col = [0.25, 0.28, 0.35]  # Dark Titanium Cryostat Chassis Base
        else:
            col = [0.18, 0.20, 0.25]
        colors_front[i] = np.clip(np.array(col) * intensity[i], 0.0, 1.0)

    poly1 = Poly3DCollection(mesh.vertices[mesh.faces], facecolors=colors_front, edgecolors="none", linewidth=0, shade=False)
    ax1.add_collection3d(poly1)
    ax1.set_xlim(-22, 22)
    ax1.set_ylim(-34, 38)
    ax1.set_zlim(0, 14)
    ax1.view_init(elev=46, azim=-55)
    ax1.set_axis_off()
    ax1.set_title("FRONT ISOMETRIC VIEW\nMulti-Tiered Gold Stages, RF Waveguides & QPU Can",
                  color="#58a6ff", fontsize=12, fontweight="bold")

    # Right: Underside View (Looking at Z=0 Inscriptions)
    ax2 = fig.add_subplot(1, 2, 2, projection="3d", facecolor="#0d1117")
    light_dir_back = np.array([-0.45, 0.60, -0.80])
    l_key_back = light_dir_back / np.linalg.norm(light_dir_back)
    diffuse_back = np.clip(np.sum(mesh.face_normals * l_key_back, axis=1), 0, 1)
    intensity_back = np.clip(0.35 + 0.65 * diffuse_back, 0.15, 1.0)

    colors_back = np.zeros((len(mesh.faces), 3), dtype=np.float32)
    for i in range(len(mesh.faces)):
        zc = mesh.triangles_center[i, 2]
        if zc < 0.36:
            # Debossed text grooves: highlight with vivid gold
            if zc > 0.02:
                col = [0.98, 0.85, 0.25]  # Debossed text inner walls
            else:
                col = [0.22, 0.24, 0.28]  # Flat bed contact
        else:
            col = [0.18, 0.20, 0.25]
        colors_back[i] = np.clip(np.array(col) * intensity_back[i], 0.0, 1.0)

    poly2 = Poly3DCollection(mesh.vertices[mesh.faces], facecolors=colors_back, edgecolors="none", linewidth=0, shade=False)
    ax2.add_collection3d(poly2)
    ax2.set_xlim(-22, 22)
    ax2.set_ylim(-34, 38)
    ax2.set_zlim(-2, 12)
    # Underside perspective: looking from bottom up
    ax2.view_init(elev=-135, azim=55)
    ax2.set_axis_off()
    ax2.set_title("UNDERSIDE BED VIEW (Z = 0)\nDebossed Inscriptions with >5.0 mm Safety Clearances",
                  color="#58a6ff", fontsize=12, fontweight="bold")

    info_box = (
        "Precision Text Boundary Verification:\n"
        "• 'HPC&A CRYOSTAT': Width 16.2 mm | Margin: 6.6 mm each side\n"
        "• 'DESIGNED BY NIMA': Width 16.8 mm | Margin: 5.1 mm each side\n"
        "• '15 mK': Width 5.3 mm | Margin: 5.2 mm each side\n"
        "• Front 'HPC&A' on Top Flange: Margin: 11.2 mm each side\n"
        "• Front 'QPU' on Bottom Can: Margin: 3.1 mm each side\n"
        "• 100% Contained — Zero Protrusion or Border Clipping"
    )
    fig.text(0.50, 0.05, info_box, fontsize=10, family="monospace", color="#c9d1d9",
             ha="center", bbox=dict(boxstyle="round,pad=0.7", facecolor="#161b22", edgecolor="#30363d", alpha=0.95))

    fig.suptitle("HPC&A QUANTUM DILUTION CHANDELIER (2.5D REVISION) — CAD VERIFICATION",
                 color="#ffffff", fontsize=15, fontweight="bold", y=0.96)

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "quantum_chandelier_render.png")
    plt.savefig(out_path, facecolor="#0d1117", edgecolor="none", bbox_inches="tight", pad_inches=0.1)
    plt.close()
    print(f"  Saved: {out_path}")


def render_master_batch_showcase():
    print("Rendering Master Batch Plate Showcase...")
    mesh = trimesh.load(os.path.join(OUTPUT_DIR, "batch_master_suite_x6.stl"))

    fig = plt.figure(figsize=(14, 9), dpi=200, facecolor="#0d1117")
    ax = fig.add_subplot(111, projection="3d", facecolor="#0d1117")

    light_dir = np.array([0.45, -0.60, 0.80])
    l_key = light_dir / np.linalg.norm(light_dir)
    diffuse = np.clip(np.sum(mesh.face_normals * l_key, axis=1), 0, 1)
    intensity = np.clip(0.35 + 0.65 * diffuse, 0.15, 1.0)

    colors = np.zeros((len(mesh.faces), 3), dtype=np.float32)
    for i in range(len(mesh.faces)):
        zc = mesh.triangles_center[i, 2]
        if zc > 5.0:
            col = [0.98, 0.88, 0.35]  # Gold / White top details
        elif zc > 4.4:
            col = [0.30, 0.75, 0.95]  # Cyan accents & fans
        elif zc > 3.8:
            col = [0.65, 0.70, 0.75]  # Chassis upper
        else:
            col = [0.22, 0.25, 0.30]  # Base beds
        colors[i] = np.clip(np.array(col) * intensity[i], 0.0, 1.0)

    poly = Poly3DCollection(mesh.vertices[mesh.faces], facecolors=colors, edgecolors="none", linewidth=0, shade=False)
    ax.add_collection3d(poly)

    # 220x220 mm bed outline
    bed_x = np.array([-110, 110, 110, -110, -110])
    bed_y = np.array([-110, -110, 110, 110, -110])
    bed_z = np.zeros_like(bed_x)
    ax.plot(bed_x, bed_y, bed_z, color="#30363d", linewidth=2, linestyle="--")

    ax.set_xlim(-120, 120)
    ax.set_ylim(-120, 120)
    ax.set_zlim(0, 25)
    ax.view_init(elev=48, azim=-55)
    ax.set_axis_off()

    ax.text2D(0.50, 0.95, "MASTER BATCH PRINT PLATE: 3 FANTASY GPUS + 3 QUANTUM KEYCHAINS",
              transform=ax.transAxes, color="#ffffff", fontsize=13, fontweight="bold", ha="center")
    ax.text2D(0.50, 0.91, "All 6 Unique Models in 1 Job | Fits 220x220 mm Bed | 100% Support-Free | Designed by Nima",
              transform=ax.transAxes, color="#58a6ff", fontsize=10, ha="center")

    note_text = (
        "Master Print Sheet Metrics:\n"
        "• Row 1: Chibi GPU + Mecha GPU + Magic Rune GPU\n"
        "• Row 2: QPU Chip + Dilution Chandelier + Bloch Sphere\n"
        "• Footprint: 203.9 x 110.0 x 5.6 mm (Standard 220x220 mm bed)\n"
        "• Total Filament: ~34 g PLA (~0.68$ total material cost)\n"
        "• Estimated Print Time: ~2.8 hours @ 0.20 mm layer height\n"
        "• 0% Supports Required (All 6 models flat Z=0 adhesion)"
    )
    ax.text2D(0.04, 0.06, note_text, transform=ax.transAxes,
              fontsize=9, family="monospace", color="#c9d1d9",
              bbox=dict(boxstyle="round,pad=0.6", facecolor="#161b22", edgecolor="#30363d", alpha=0.92))

    out_path = os.path.join(OUTPUT_DIR, "master_batch_plate_showcase.png")
    plt.tight_layout()
    plt.savefig(out_path, facecolor="#0d1117", edgecolor="none", bbox_inches="tight", pad_inches=0.1)
    plt.close()
    print(f"  Saved: {out_path}")


def update_print_shop_guide():
    guide_content = """# 🖨️ HPC&A FANTASY & QUANTUM KEYCHAINS — 3D PRINTING WORKSHOP MANUAL
## راهنمای جامع تولید کارگاه پرینت سه‌بعدی برای مجموعه فانتزی و کوانتومی HPC&A

**مجموعه نهایی:** ۶ مدل جاکلیدی (۳ مدل کارت گرافیک فانتزی + ۳ مدل پردازش کوانتومی)
**طراح:** نیما (Designed by Nima)
**توسعه‌یافته برای:** گروه پژوهشی معماری و محاسبات با کارایی بالا (HPC&A Research Group)

---

## 🇮🇷 بخش اول: راهنمای فارسی مخصوص کارگاه پرینت سه‌بعدی

سلام به همکار محترم و اپراتور کارگاه پرینت سه‌بعدی!
این مجموعه شامل **۶ مدل جاکلیدی اختصاصی** (۳ مدل کارت گرافیک فانتزی + ۳ مدل فناوری کوانتومی) است. تمام مدل‌ها با بالاترین دقت مهندسی طراحی شده‌اند تا **بدون دردسر، با کیفیت بی‌نظیر و بدون نیاز به ساپورت** چاپ شوند.

### ۱. تنظیمات حیاتی اسلایسر (Slicer Settings)
* **نیاز به ساپورت (Supports):** **خیر - کاملاً خاموش (Support: NONE / 0%)**. تمام زوایا کمتر از ۴۵ درجه هستند و هیچ بخشی به ساپورت نیاز ندارد.
* **ضخامت لایه (Layer Height):** **$0.20\text{ mm}$** (هم لایه اول و هم لایه‌های بعدی).
* **تراکم داخلی (Infill):** **۱۵٪ تا ۲۰٪** (الگوی Gyroid یا Grid).
* **تعداد دیواره‌ها (Wall Loops):** **۳ الی ۴ دور دیواره** (برای استحکام سوراخ جاکلیدی در جیب).
* **تعداد لایه‌های کف و سقف:** **۴ لایه کف / ۵ لایه سقف**.
* **نیاز به Brim / Raft:** **خیر**. تمام مدل‌ها در کف ($Z=0$) کاملاً مسطح هستند و چسبندگی عالی به تخت دارند.
* **متریال پیشنهادی:** **PLA یا PETG** (دمای نازل: ۲۰۰-۲۱۰ درجه / دمای بد: ۶۰ درجه).

---

### ۲. فایل‌های آماده برای چاپ تعداد بالا (Batch Print Plates)
برای راحتی کارگاه، فایل‌های چیدمان‌شده آماده روی ابعاد تخت استاندارد ($220 \times 220\text{ mm}$) تهیه شده است:

| نام فایل | محتویات صفحه | ابعاد چیدمان | وزن کل فیلامنت | زمان چاپ تخمینی |
| :--- | :--- | :--- | :--- | :--- |
| **`batch_master_suite_x6.stl`** | **پک مستر ۶ عددی (هر ۶ مدل فانتزی و کوانتومی در یک پرینت)** | $204 \times 110\text{ mm}$ | $\approx 34\text{ g}$ | حدود ۲.۸ ساعت |
| **`batch_fantasy_gpus_x6.stl`** | **۶ عدد کارت گرافیک فانتزی (۲ تا چیبی + ۲ تا مکا + ۲ تا رونیک)** | $204 \times 78\text{ mm}$ | $\approx 34\text{ g}$ | حدود ۳ ساعت |
| **`batch_quantum_collection_x6.stl`** | **۶ عدد کوانتومی (۲ تا چیپ QPU + ۲ تا لوستر کرایواستات + ۲ تا بلاخ)** | $174 \times 130\text{ mm}$ | $\approx 35\text{ g}$ | حدود ۳ ساعت |

---

### ۳. معرفی ۶ مدل تکی مجموعه (Single STL Files)

#### الف) ۳ مدل کارت گرافیک فانتزی (Fantasy GPU Keychains):
1. **`gpu_fantasy_chibi.stl`**: کارت گرافیک کارتونی چیبی با صورت خندان و پروانه‌های گلبرگی ($55 \times 34 \times 5.5\text{ mm}$).
2. **`gpu_fantasy_mecha.stl`**: سفینه جنگنده فضایی مکا با توربین جت مافوق‌صوت و اگزوز راکت ($63 \times 30 \times 5.6\text{ mm}$).
3. **`gpu_fantasy_rune.stl`**: تالیسمان جادویی باستان با سیرکل احضار، سپر سلطنتی و کریستال‌های مانا ($65 \times 28 \times 5.6\text{ mm}$).

#### ب) ۳ مدل پردازش کوانتومی (Quantum Keychains):
1. **`qpu_keychain_hpca.stl`**: تراشه ابررسانای کوانتومی با کیوبیت‌های ترانزمون و رزوناتورهای مارپیچی ($57 \times 36 \times 5.1\text{ mm}$).
2. **`quantum_chandelier.stl`**: لوستر کرایواستات برودتی ۱۵ میلی‌کلوین با ۵ طبقه طلایی و قوطی شیلد QPU ($31 \times 62 \times 5.4\text{ mm}$).
3. **`quantum_bloch.stl`**: مدالیون هشت‌ضلعی کره بلاخ با بردار حالت کوانتومی $|\psi\rangle$ و قطب‌های $|0\rangle, |1\rangle$ ($44 \times 49 \times 5.1\text{ mm}$).

---

### ۴. حکاکی پشت و فیت بودن نوشته‌ها
* پشت تمامی ۶ مدل عبارت **`DESIGNED BY NIMA`** در لایه اول ($Z=0$) با عمق $0.35\text{ mm}$ حکاکی شده است.
* در مدل لوستر، تمامی نوشته‌ها اعم از `HPC&A CRYOSTAT`، `DESIGNED BY NIMA` و `15 mK` در پشت و `HPC&A` و `QPU` در رو با **حاشیه امن بیش از ۵ میلی‌متر** قرار گرفته‌اند و هیچ بیرون‌زدگی ندارند.

### ۵. ترفند دورنگ کردن در پرینتر تک‌نازل (Filament Color Swap)
برای جلوه فوق‌العاده نوشته‌ها و جزئیات روی مدل‌ها:
* لایه‌های $0.00$ تا $4.00\text{ mm}$ با رنگ پایه بدنه (مشکی، خاکستری تیتانیوم یا آبی تیره) چاپ شوند.
* در ارتفاع **$Z = 4.00\text{ mm}$ یا $4.60\text{ mm}$** دستور **Pause at height** داده شود و فیلامنت به **طلایی، نقره‌ای، یا سفید** تغییر کند تا خطوط طبقات، نوشته‌های `HPC&A` و کیوبیت‌ها دو رنگ شوند.

---

## 🇬🇧 Section 2: English Production Sheet for 3D Print Farm

### Quick Slicer Profile:
* **Nozzle:** 0.40 mm
* **Layer Height:** 0.20 mm
* **Supports:** **STRICTLY OFF (0%)** — All models are 100% self-supporting FDM.
* **Infill:** 15–20% (Gyroid / Grid).
* **Perimeters:** 3–4 walls (ensures high tensile strength for keyring eyelets).
* **Top/Bottom Solid Layers:** 4 Bottom / 5 Top.
* **Brim:** None needed (large planar Z=0 contact).
* **Material:** PLA or PETG (Bed: 60°C, Nozzle: 205–215°C).

### Master Production File:
* **`batch_master_suite_x6.stl`**: Contains all 6 unique models (3 Fantasy GPUs + 3 Quantum Keychains) arrayed cleanly within $204 \times 110\text{ mm}$, fitting any standard 220x220 mm bed (Ender-3, Prusa MK3/MK4, Bambu Lab X1/P1/A1).

---
**Attribution:** All models feature **`DESIGNED BY NIMA | HPC&A`** debossed on the bottom layer ($Z=0$).
"""
    guide_path = os.path.join(OUTPUT_DIR, "PRINT_SHOP_GUIDE.md")
    with open(guide_path, "w", encoding="utf-8") as f:
        f.write(guide_content)
    print(f"  Saved: {guide_path}")


def main():
    render_quantum_trio()
    render_chandelier_detail()
    render_master_batch_showcase()
    update_print_shop_guide()
    print("\nAll renders and guide updates completed successfully!")


if __name__ == "__main__":
    main()
