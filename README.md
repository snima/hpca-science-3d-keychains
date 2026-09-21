# 🚀 HPC&A 3D Science & Fantasy Keychains Suite
### 3D-Printable Science Souvenirs & Mechanical Art for HPC & Quantum Computing
**Designed by Nima** | Commissioned for the **HPC&A Research Group** (High Performance Computing & Architecture)

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Code: MIT](https://img.shields.io/badge/Code_License-MIT-green.svg)](LICENSE)
[![FDM Support-Free](https://img.shields.io/badge/FDM_Supports-0%25_(Strictly_Free)-success.svg)](#-fdm-print-farm-specifications)
[![Bed Size](https://img.shields.io/badge/Bed_Compatibility-220x220_mm-blue.svg)](#-mass-production-batch-plates)

---

![Master Batch Plate 6-Pack](output/master_batch_plate_showcase.png)

A collection of **6 unique, ultra-detailed 3D-printable keychains** blending high-performance computing, quantum information hardware, and mechanical fantasy aesthetics. Every model is engineered from first principles in Python CAD ([Build123d](https://github.com/gumyr/build123d)), 100% watertight, with strictly **0% supports required** on any standard FDM 3D printer.

Every keychain features **`DESIGNED BY NIMA`** debossed on the bottom layer ($Z=0$), ensuring clear attribution while resting flat on the print bed.

---

## 🌟 The 6 Editions

### ⚛️ Part 1: Quantum Computing Hardware Editions
![Quantum Trio Showcase](output/quantum_trio_showcase.png)

1. **Superconducting QPU Chip (`qpu_keychain_hpca.stl` / `.step`)**
   - Transmon qubit crosses, serpentine coplanar waveguide (CPW) readout resonators, wirebond gold contact pads, and silicon substrate cavity.
   - Dimensions: $56.7 \times 36.0 \times 5.1\text{ mm}$ | Volume: $6.9\text{ cm}^3$ (~$6.4\text{ g}$ PLA).

2. **Multi-Tiered Dilution Chandelier (`quantum_chandelier.stl` / `.step`)**
   - Sleek 2.5D tiered silhouette of an ultra-low temperature $15\text{ mK}$ dilution refrigerator cryostat.
   - 5 gold thermal stages, vertical RF coaxial lines, side heat-exchanger coils, and bottom gold-plated QPU shielding can.
   - All text inscriptions fit with **$>5.0\text{ mm}$ safety clearances** from every edge.
   - Dimensions: $31.2 \times 61.7 \times 5.4\text{ mm}$ | Volume: $5.4\text{ cm}^3$ (~$5.0\text{ g}$ PLA).

3. **Bloch Sphere Quantum Info Medallion (`quantum_bloch.stl` / `.step`)**
   - Octagonal coin frame with a 3D spherical dome representing the single-qubit state space.
   - Features equator, prime meridian, $Z$-axis spindle, state vector $|\psi\rangle$ arrow, and basis state labels $|0\rangle$ & $|1\rangle$.
   - Dimensions: $43.7 \times 49.0 \times 5.1\text{ mm}$ | Volume: $5.3\text{ cm}^3$ (~$5.0\text{ g}$ PLA).

---

### 🎮 Part 2: Fantasy GPU Editions
![Fantasy GPU Trio Showcase](output/gpu_fantasy_trio_showcase.png)

1. **Chibi Anime GPU (`gpu_fantasy_chibi.stl` / `.step`)**
   - Kawaii cartoon graphics card with smiling anime eyes, rosy blush cheeks, petal fan blades, and curved boots.
   - Dimensions: $55.0 \times 34.0 \times 5.5\text{ mm}$ | Volume: $5.8\text{ cm}^3$ (~$5.4\text{ g}$ PLA).

2. **Sci-Fi Mecha Starfighter GPU (`gpu_fantasy_mecha.stl` / `.step`)**
   - Supersonic jet fighter aesthetic with swept-back aerofoil wings, central supersonic jet turbine, and dual thrusters.
   - Dimensions: $63.0 \times 30.0 \times 5.6\text{ mm}$ | Volume: $4.8\text{ cm}^3$ (~$4.5\text{ g}$ PLA).

3. **Cyber-Runic Arcane GPU (`gpu_fantasy_rune.stl` / `.step`)**
   - Mystical alchemical talisman blending circuit traces with an 8-spoke summoning circle, royal shield crest, and mana crystals.
   - Dimensions: $65.0 \times 28.0 \times 5.6\text{ mm}$ | Volume: $5.8\text{ cm}^3$ (~$5.4\text{ g}$ PLA).

---

## 🖨️ Mass Production Batch Plates (Pre-Arranged STL)

Ready-to-slice batch plates pre-arranged for maximum print farm throughput on standard $220 \times 220\text{ mm}$ beds:

| STL File | Contents | Array Footprint | Total Filament | Print Time @ 0.20 mm |
| :--- | :--- | :--- | :--- | :--- |
| **`output/batch_master_suite_x6.stl`** | **All 6 Unique Models in 1 Job** | $203.9 \times 110.0 \times 5.6\text{ mm}$ | $\approx 34\text{ g}$ | **~2.8 hours** |
| **`output/batch_fantasy_gpus_x6.stl`** | 6x Fantasy GPUs (2x Chibi, 2x Mecha, 2x Rune) | $203.9 \times 78.4 \times 5.6\text{ mm}$ | $\approx 34\text{ g}$ | **~3.0 hours** |
| **`output/batch_quantum_collection_x6.stl`** | 6x Quantum Models (2x QPU, 2x Chandelier, 2x Bloch) | $174.2 \times 129.7 \times 5.4\text{ mm}$ | $\approx 35\text{ g}$ | **~3.0 hours** |

---

## ⚙️ Slicer & Printing Guidelines

* **Supports:** **STRICTLY OFF (0%)** — All overhangs $\le 45^\circ$, all text debossed/embossed with print-safe angles.
* **Layer Height:** $0.20\text{ mm}$ (First layer $0.20\text{ mm}$).
* **Infill:** 15% – 20% (Gyroid or Grid).
* **Walls / Perimeters:** 3 to 4 loops (guarantees solid $\varnothing 4.6\text{ mm}$ keyring hole strength).
* **Material:** PLA, PLA+, or PETG (Nozzle: 205–215°C, Bed: 60°C).
* **Brim / Raft:** None needed (solid planar bed contact).
* **Dual-Color Trick (Single Nozzle):** Set **Pause at Height** at $Z = 4.0\text{ mm}$ or $4.6\text{ mm}$ to switch from dark base filament to gold/white for vibrant two-tone lettering and details.

For detailed workshop instructions in Persian and English, see [`output/PRINT_SHOP_GUIDE.md`](output/PRINT_SHOP_GUIDE.md).

---

## 🛠️ Reproducing & Generating CAD Models

Prerequisites: Python 3.10+ and a virtual environment.

```bash
# Clone the repository
git clone git@github.com:snima/hpca-science-3d-keychains.git
cd hpca-science-3d-keychains

# Create virtual environment and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install build123d trimesh matplotlib numpy

# Generate all 3D models (STL + STEP)
python generate_fantasy_gpus.py
python generate_all_quantum.py

# Generate batch production plates
python generate_batch_plates.py

# Render high-resolution showcases
python render_quantum_and_master.py
```

---

## 📄 License & Attribution

This project is licensed under a dual-licensing model:
* **3D Designs, STL/STEP Models, Batch Plates & Documentation:** Licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](LICENSE).
  - ✅ **Free to share, download, 3D-print, and modify** for personal, educational, research, and non-commercial purposes.
  - ⚠️ **Attribution Required:** Must credit **Nima** and the **HPC&A Research Group**.
  - ⛔ **Non-Commercial:** No commercial selling of prints or files without explicit prior written authorization.
  - 🔄 **ShareAlike:** Derivative works must be published under the same CC BY-NC-SA 4.0 terms.
* **Software & Python Generation Scripts:** Licensed under the [MIT License](LICENSE).

---

## 🇮🇷 راهنمای فارسی مختصر

مجموعه جاکلیدی‌های سه‌بعدی علمی و فانتزی **HPC&A**:
* **طراح:** نیما (Designed by Nima)
* شامل ۶ طرح اختصاصی: ۳ طرح فانتزی کارت گرافیک (چیبی، مکا، رونیک) + ۳ طرح پردازش کوانتومی (چیپ کیوبیت QPU، لوستر برودتی کرایواستات، کره بلاخ).
* ۱۰۰٪ قابل چاپ با پرینترهای FDM بدون نیاز به ساپورت (Support: 0%).
* صفحه آماده چاپ مستر (`output/batch_master_suite_x6.stl`) با چیدمان هر ۶ مدل به صورت یکجا، با مصرف فقط ۳۴ گرم فیلامنت و زمان پرینت کمتر از ۳ ساعت.
* مجوز نشر: **CC BY-NC-SA 4.0** (آزاد برای استفاده شخصی، علمی و چاپ دانشگاهی، با حفظ نام طراح نیما و عدم استفاده تجاری بدون اجازه).
