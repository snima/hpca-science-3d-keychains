# 3D Printing Production Guide: HPC&A Keychains Suite
**Author:** Nima | **Organization:** HPC&A Research Group  
**License:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

---

## Directory Structure
* `stl/`: Universal stereolithography files for all slicing software (PrusaSlicer, Bambu Studio, Cura, OrcaSlicer, Simplify3D).
* `3mf/`: Modern 3D Manufacturing Format files with native unit, geometry, and slicer metadata.
* `step/`: Standard AP214 boundary-representation CAD solids for parametric engineering and machining.
* `obj/`: Wavefront OBJ polygon meshes for 3D visualization, CGI, and rendering.
* `batch_plates/`: Pre-nested multi-model print layouts for high-throughput batch production on standard 220x220 mm beds.

---

## Recommended Slicer Parameters
* **Support Material:** **STRICTLY DISABLED (Support: 0%)**  
  All 6 models are engineered with self-supporting geometry (overhang angles <= 45 degrees) and 100% flat bed adhesion at Z=0.
* **Layer Height:** 0.20 mm (First layer: 0.20 mm).
* **Infill:** 15% to 20% (Gyroid, Grid, or Adaptive Cubic recommended).
* **Perimeters / Wall Loops:** 3 to 4 loops (ensures maximum tensile durability for keyring attachment holes).
* **Top / Bottom Solid Shells:** 4 bottom layers, 5 top layers.
* **Bed Adhesion (Brim/Raft):** None required. Flat Z=0 contact area provides excellent adhesion on textured PEI, smooth PEI, or glass.
* **Recommended Filaments:** PLA, PLA+, or PETG.
  * Nozzle Temperature: 205 - 215 deg C (PLA) / 230 - 245 deg C (PETG)
  * Bed Temperature: 55 - 60 deg C (PLA) / 70 - 80 deg C (PETG)

---

## Dual-Color Printing & Exact Filament Swap Heights (Slim Edition)
To achieve high-contrast lettering, circuit traces, and shiny accent details without requiring an expensive multi-material system (AMS/MMU), use a standard single-extruder filament pause (`M600`):

1. **Base Color (Color 1):** Slice the bottom portion with a dark filament (Black, Slate Gray, or Deep Navy).
2. **Pause Command:** Insert a **Pause at Height** (`M600`) at the exact height/layer specified in the table below.
3. **Accent Color (Color 2):** Swap filament to your highlight color (Gleaming Gold, Silk White, or Silver) to print the top embossed letters, circuit traces, and logos.

### Exact Filament Swap Reference Table

| Model Name | Total Z Height | Base Body Top | Exact Pause Height (`M600`) | Slicer Layer (@ 0.20 mm) | Slicer Layer (@ 0.16 mm) | What Prints in Accent Color |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`gpu_fantasy_chibi`** | 4.30 mm | 3.40 mm | **$Z = 3.40	ext{ mm}$** | **Layer 18** | Layer 22 | Top banner plinth, "HPC&A" letters, facial smile, blush cheeks |
| **`gpu_fantasy_mecha`** | 4.40 mm | 3.40 mm | **$Z = 3.40	ext{ mm}$** *(or 3.80 mm)* | **Layer 18** *(or 20)* | Layer 22 *(or 24)* | Jet turbine bullet nose, armored nameplate & "HPC&A" text |
| **`gpu_fantasy_rune`** | 4.40 mm | 3.40 mm | **$Z = 3.40	ext{ mm}$** *(or 3.80 mm)* | **Layer 18** *(or 20)* | Layer 22 *(or 24)* | Central heraldic shield, "HPC&A" letters, tall mana crystals |
| **`qpu_keychain_hpca`** | 3.90 mm | 3.40 mm | **$Z = 3.40	ext{ mm}$** | **Layer 18** | Layer 22 | "HPC&A QUANTUM" text, gold wirebond pads & transmon crosses |
| **`quantum_chandelier`** | 4.40 mm | 3.00 mm | **$Z = 3.00	ext{ mm}$** *(or 3.80 mm)* | **Layer 16** *(or 20)* | Layer 19 *(or 24)* | All 5 golden dilution cryostat stages, RF coax lines & text |
| **`quantum_bloch`** | 3.90 mm | 3.40 mm | **$Z = 3.40	ext{ mm}$** | **Layer 18** | Layer 22 | State vector arrow, basis states \|0⟩, \|1⟩, \|ψ⟩ & text |
| **`ram_ddr_hpca`** | 4.60 mm | 3.40 mm | **$Z = 3.40	ext{ mm}$** | **Layer 18** | Layer 22 | Aluminum heatsink spreader, IC memory chips & "HPC&A" rail |
| **`cpu_fantasy_chibi`** | 5.90 mm | 3.40 mm | **$Z = 3.40	ext{ mm}$** *(or 4.20 mm)* | **Layer 18** *(or 22)* | Layer 22 *(or 27)* | IHS nickel heat spreader, P-cores, E-cluster & L3 cache die |
| **`gpu_spinning_body`** | 4.20 mm | 3.40 mm | **$Z = 3.40	ext{ mm}$** | **Layer 18** | Layer 22 | Elevated plaque & "HPC&A" / "HPC&A EDITION" lettering |

### Universal Master Batch Plate Rule
* When printing the **`batch_master_suite_x6`**, **`batch_fantasy_gpus_x6`**, or **`batch_quantum_collection_x6`**:
  * Set a **single universal pause (`M600`) at $Z = 3.40	ext{ mm}$ (Layer 18 @ 0.20 mm)**.
  * At $Z = 3.40	ext{ mm}$, all standard cards have completed their base layers. Swapping to Gold/White filament at this exact height produces a razor-sharp, two-tone color contrast across the entire plate in a single pause!
  * *(Note: For the Dilution Chandelier on the master plate, its first 0.40 mm of lower stage silhouette is printed in the dark base color, and its upper 1.00 mm of stages and lettering print in Gold, creating an aesthetically pleasing multi-tiered depth).*

### How to Configure in Common Slicers
* **Bambu Studio / OrcaSlicer:** Slice the plate. In the right vertical layer preview bar, scroll down to **Layer 18 ($Z = 3.40	ext{ mm}$)**, right-click the orange slider handle, and select **Pause** (or **Change Filament**).
* **PrusaSlicer:** Slice the plate. On the right vertical layer slider, move to **$3.40	ext{ mm}$**, right-click the small `+` icon, and select **Add color change (M600)**.
* **UltiMaker Cura:** Menu **Extensions** > **Post Processing** > **Modify G-Code** > **Add a script** > **Pause at height** > set **Pause Height** to `3.40 mm`.

---

## Production Batch Specs
| File | Contents | Footprint | Filament Weight | Print Time (0.20 mm) |
| :--- | :--- | :--- | :--- | :--- |
| `batch_master_suite_x6.stl` | Complete 6-Pack (All 6 unique models) | 203.9 x 110.0 x 4.4 mm | ~24 g | ~2.0 hours |
| `batch_fantasy_gpus_x6.stl` | 6x Fantasy GPUs (2x Chibi, 2x Mecha, 2x Rune) | 203.9 x 78.4 x 4.4 mm | ~24 g | ~2.2 hours |
| `batch_quantum_collection_x6.stl` | 6x Quantum Keychains (2x QPU, 2x Chandelier, 2x Bloch) | 174.2 x 129.7 x 4.4 mm | ~23 g | ~2.2 hours |

---
**Attribution:** All models feature **DESIGNED BY NIMA | HPC&A** debossed on the bottom layer (Z=0).
