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

## Dual-Color Lettering (Single-Extruder Filament Swap)
To achieve contrasting high-visibility lettering and details without a multi-material system:
1. Slice the model using a dark primary color (black, slate gray, or navy).
2. Insert a **Pause at height** (`M600`) command in your slicer at **Z = 4.00 mm** (or **Z = 4.60 mm** depending on the model).
3. Swap filament to a contrasting color (gold, white, or silver) for the top embossed features, lettering, and chips.

---

## Production Batch Specs
| File | Contents | Footprint | Filament Weight | Print Time (0.20 mm) |
| :--- | :--- | :--- | :--- | :--- |
| `batch_master_suite_x6.stl` | Complete 6-Pack (All 6 unique models) | 203.9 x 110.0 x 5.6 mm | ~34 g | ~2.8 hours |
| `batch_fantasy_gpus_x6.stl` | 6x Fantasy GPUs (2x Chibi, 2x Mecha, 2x Rune) | 203.9 x 78.4 x 5.6 mm | ~34 g | ~3.0 hours |
| `batch_quantum_collection_x6.stl` | 6x Quantum Keychains (2x QPU, 2x Chandelier, 2x Bloch) | 174.2 x 129.7 x 5.4 mm | ~35 g | ~3.0 hours |

---
**Attribution:** All models feature **DESIGNED BY NIMA | HPC&A** debossed on the bottom layer (Z=0).
