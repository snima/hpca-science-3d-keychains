#!/usr/bin/env python3
"""
PREPARE PRINT-READY PACKAGE & MULTI-FORMAT EXPORT
=================================================
Generates a structured, production-ready release folder:
  ready_to_print/
    ├── stl/          (Binary STL for all slicers)
    ├── 3mf/          (Modern 3MF for Bambu Studio, PrusaSlicer, OrcaSlicer)
    ├── step/         (Parametric boundary-representation CAD solids)
    ├── obj/          (Wavefront OBJ meshes for 3D CGI and rendering)
    ├── batch_plates/ (Pre-arranged plates for mass production)
    ├── PRINTING_GUIDE.md
    └── hpc_a_keychains_print_ready.zip
"""

import os
import shutil
import zipfile
import trimesh

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
READY_DIR = os.path.join(BASE_DIR, "ready_to_print")

# Subdirectories
STL_DIR = os.path.join(READY_DIR, "stl")
THREE_MF_DIR = os.path.join(READY_DIR, "3mf")
STEP_DIR = os.path.join(READY_DIR, "step")
OBJ_DIR = os.path.join(READY_DIR, "obj")
BATCH_DIR = os.path.join(READY_DIR, "batch_plates")

for d in [STL_DIR, THREE_MF_DIR, STEP_DIR, OBJ_DIR, BATCH_DIR]:
    os.makedirs(d, exist_ok=True)

# The 6 Final Models
models = [
    ("gpu_fantasy_chibi", "Chibi Anime GPU Keychain"),
    ("gpu_fantasy_mecha", "Mecha Starfighter GPU Keychain"),
    ("gpu_fantasy_rune", "Cyber-Runic Arcane GPU Keychain"),
    ("qpu_keychain_hpca", "Superconducting QPU Chip Keychain"),
    ("quantum_chandelier", "Dilution Refrigerator Chandelier Keychain"),
    ("quantum_bloch", "Bloch Sphere Quantum Info Medallion"),
]

# The 3 Batch Plates
batch_plates = [
    ("batch_master_suite_x6", "Master 6-Pack (All 6 Models in 1 Print)"),
    ("batch_fantasy_gpus_x6", "Fantasy 6-Pack (2x Chibi, 2x Mecha, 2x Rune)"),
    ("batch_quantum_collection_x6", "Quantum 6-Pack (2x QPU, 2x Chandelier, 2x Bloch)"),
]

print("Processing individual models...")
for base_name, desc in models:
    src_stl = os.path.join(OUTPUT_DIR, f"{base_name}.stl")
    src_step = os.path.join(OUTPUT_DIR, f"{base_name}.step")

    # 1. Copy STL
    dst_stl = os.path.join(STL_DIR, f"{base_name}.stl")
    shutil.copy2(src_stl, dst_stl)

    # 2. Copy STEP
    if os.path.exists(src_step):
        dst_step = os.path.join(STEP_DIR, f"{base_name}.step")
        shutil.copy2(src_step, dst_step)

    # 3. Load mesh for 3MF and OBJ conversions
    mesh = trimesh.load(src_stl)

    # Export 3MF
    dst_3mf = os.path.join(THREE_MF_DIR, f"{base_name}.3mf")
    mesh.export(dst_3mf)

    # Export OBJ
    dst_obj = os.path.join(OBJ_DIR, f"{base_name}.obj")
    mesh.export(dst_obj)

    print(f"  Processed: {base_name} (STL, STEP, 3MF, OBJ)")

print("\nProcessing batch plates...")
for base_name, desc in batch_plates:
    src_stl = os.path.join(OUTPUT_DIR, f"{base_name}.stl")

    # Copy STL to batch_plates folder
    dst_stl = os.path.join(BATCH_DIR, f"{base_name}.stl")
    shutil.copy2(src_stl, dst_stl)

    # Export 3MF to batch_plates folder
    mesh = trimesh.load(src_stl)
    dst_3mf = os.path.join(BATCH_DIR, f"{base_name}.3mf")
    mesh.export(dst_3mf)

    print(f"  Processed Batch: {base_name} (STL, 3MF)")

# Create PRINTING_GUIDE.md inside ready_to_print/
guide_text = """# 3D Printing Production Guide: HPC&A Keychains Suite
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
"""

with open(os.path.join(READY_DIR, "PRINTING_GUIDE.md"), "w", encoding="utf-8") as f:
    f.write(guide_text)

# Create convenient ZIP archive of ready_to_print directory
zip_path = os.path.join(READY_DIR, "hpc_a_keychains_print_ready.zip")
print(f"\nCreating ZIP archive: {zip_path}...")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(READY_DIR):
        for file in files:
            if file.endswith(".zip"):
                continue
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, READY_DIR)
            zipf.write(full_path, arcname=rel_path)

print("ZIP archive created successfully!")
print(f"Archive size: {os.path.getsize(zip_path) / (1024 * 1024):.2f} MB")
