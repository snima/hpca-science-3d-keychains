#!/usr/bin/env python3
"""
SERGIO EDITION — THIN KEYCHAINS PRINTED BY SERGIO (0.6 mm NOZZLE)
================================================================
Same slim models, but with an extra underside line "PRINTED BY SERGIO"
in XL lettering with a deeper cut, engineered for a coarse 0.6 mm nozzle:
  - Back text >= 2.4 mm (readable with 0.6 mm extrusion widths)
  - Bottom deboss 0.6 mm deep (visible at 0.3 mm+ layer heights)

Recommended slicer settings for Sergio:
  - Nozzle 0.6 mm, layer height 0.3 mm, 2 walls (1.2 mm), 15% infill
  - Supports OFF, brim OFF

Output goes to a separate folder so the other editions are untouched:
    sergio/
        ├── stl/          (Binary STL for all slicers)
        ├── 3mf/          (Modern 3MF for Bambu Studio, PrusaSlicer, OrcaSlicer)
        ├── step/         (Parametric CAD solids)
        ├── batch_plates/ (Full-set x9 + production x17, no spinning edition)
        └── preview_backs.png
"""

import os
import shutil
import sys
import trimesh
from build123d import export_stl, export_step

from generate_gpu_keychain import build_gpu_keychain_model
from generate_spinning_gpu import build_spinning_gpu_body, build_spinning_rotor
from generate_all_quantum import (
    build_qpu_chip,
    build_quantum_chandelier,
    build_quantum_bloch,
)
from generate_fantasy_gpus import (
    build_chibi_gpu,
    build_mecha_gpu,
    build_rune_gpu,
)
from generate_fantasy_cpu import build_fantasy_cpu
from generate_ram_keychain import build_ram_keychain

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SERGIO_DIR = os.path.join(BASE_DIR, "sergio")
STL_DIR = os.path.join(SERGIO_DIR, "stl")
THREE_MF_DIR = os.path.join(SERGIO_DIR, "3mf")
STEP_DIR = os.path.join(SERGIO_DIR, "step")
BATCH_DIR = os.path.join(SERGIO_DIR, "batch_plates")

for d in [STL_DIR, THREE_MF_DIR, STEP_DIR, BATCH_DIR]:
    os.makedirs(d, exist_ok=True)

BOTTOM_EXTRA = "PRINTED BY SERGIO"

# (file base name, builder callable with coarse XL backs)
MODELS = [
    ("gpu_keychain_hpca", lambda: build_gpu_keychain_model(bottom_extra=BOTTOM_EXTRA, coarse=True)),
    ("gpu_spinning_body", lambda: build_spinning_gpu_body(bottom_extra=BOTTOM_EXTRA, coarse=True)),
    ("gpu_fantasy_chibi", lambda: build_chibi_gpu(bottom_extra=BOTTOM_EXTRA, coarse=True)),
    ("gpu_fantasy_mecha", lambda: build_mecha_gpu(bottom_extra=BOTTOM_EXTRA, coarse=True)),
    ("gpu_fantasy_rune", lambda: build_rune_gpu(bottom_extra=BOTTOM_EXTRA, coarse=True)),
    ("qpu_keychain_hpca", lambda: build_qpu_chip(bottom_extra=BOTTOM_EXTRA, coarse=True)),
    ("quantum_chandelier", lambda: build_quantum_chandelier(bottom_extra=BOTTOM_EXTRA, coarse=True)),
    ("quantum_bloch", lambda: build_quantum_bloch(bottom_extra=BOTTOM_EXTRA, coarse=True)),
    ("cpu_fantasy_chibi", lambda: build_fantasy_cpu(bottom_extra=BOTTOM_EXTRA, coarse=True)),
    ("ram_ddr_hpca", lambda: build_ram_keychain(bottom_extra=BOTTOM_EXTRA, coarse=True)),
]

# Full-set x9 slot grid (3x3 on 220x220)
FULL_SLOTS = [
    (-72.0, 68.0), (0.0, 68.0), (72.0, 68.0),
    (-72.0, 0.0), (0.0, 0.0), (72.0, 0.0),
    (-72.0, -68.0), (0.0, -68.0), (72.0, -68.0),
]
FULL_NAMES = [
    "quantum_chandelier", "quantum_bloch", "cpu_fantasy_chibi",
    "gpu_fantasy_chibi", "gpu_fantasy_mecha", "gpu_fantasy_rune",
    "gpu_keychain_hpca", "qpu_keychain_hpca", "ram_ddr_hpca",
]

# Compact production x17 rows: (gap, [names])
PROD_ROWS = [
    (4.0, ["ram_ddr_hpca", "gpu_keychain_hpca", "gpu_fantasy_rune"]),
    (4.0, ["gpu_fantasy_mecha", "gpu_fantasy_chibi", "qpu_keychain_hpca"]),
    (4.0, ["ram_ddr_hpca", "gpu_keychain_hpca", "gpu_fantasy_rune"]),
    (4.0, ["gpu_fantasy_mecha", "gpu_fantasy_chibi", "qpu_keychain_hpca"]),
    (3.0, ["quantum_chandelier", "quantum_bloch", "cpu_fantasy_chibi",
            "quantum_chandelier", "quantum_bloch"]),
]


def centered(mesh: trimesh.Trimesh) -> trimesh.Trimesh:
    """Zero Z to bed and center in XY."""
    m = mesh.copy()
    m.apply_translation([0, 0, -m.bounds[0, 2]])
    c_xy = (m.bounds[0, :2] + m.bounds[1, :2]) / 2.0
    m.apply_translation([-c_xy[0], -c_xy[1], 0])
    return m


def main(plates_only: bool = False):
    print("=================================================================")
    print("Generating Sergio Edition (XL backs for 0.6 mm nozzle)...")
    print("=================================================================")

    if not plates_only:
        for name, builder in MODELS:
            print(f"\nBuilding {name}...")
            part = builder()

            stl_path = os.path.join(STL_DIR, f"{name}.stl")
            step_path = os.path.join(STEP_DIR, f"{name}.step")
            mf_path = os.path.join(THREE_MF_DIR, f"{name}.3mf")

            export_stl(part, stl_path, tolerance=0.005, angular_tolerance=0.1)
            export_step(part, step_path)

            mesh = trimesh.load(stl_path)
            mesh.export(mf_path)

            bbox = mesh.bounding_box.extents
            print(f"  Watertight: {mesh.is_watertight}")
            print(f"  Dimensions: {bbox[0]:.2f} x {bbox[1]:.2f} x {bbox[2]:.2f} mm")

        # The snap-fit rotor has no inscription; copy the standard one unchanged.
        rotor_src = os.path.join(BASE_DIR, "output", "gpu_spinning_rotor.stl")
        if os.path.exists(rotor_src):
            shutil.copy2(rotor_src, os.path.join(STL_DIR, "gpu_spinning_rotor.stl"))
            trimesh.load(rotor_src).export(
                os.path.join(THREE_MF_DIR, "gpu_spinning_rotor.3mf")
            )
            print("\nCopied unchanged gpu_spinning_rotor (no inscription).")

    # Full-set batch plate x9
    print("\nBuilding full-set batch plate x9...")
    full_parts = []
    for (x_pos, y_pos), base in zip(FULL_SLOTS, FULL_NAMES):
        m = centered(trimesh.load(os.path.join(STL_DIR, f"{base}.stl")))
        m.apply_translation([x_pos, y_pos, 0])
        full_parts.append(m)
    plate = trimesh.util.concatenate(full_parts)
    plate.export(os.path.join(BATCH_DIR, "batch_full_set_x9.stl"))
    plate.export(os.path.join(BATCH_DIR, "batch_full_set_x9.3mf"))
    ext = plate.bounding_box.extents
    print(f"  Footprint: {ext[0]:.1f} x {ext[1]:.1f} x {ext[2]:.1f} mm")

    # Compact production plate x17
    print("\nBuilding production batch plate x17...")
    fab = {b: centered(trimesh.load(os.path.join(STL_DIR, f"{b}.stl")))
           for b in ["ram_ddr_hpca", "gpu_keychain_hpca", "gpu_fantasy_rune",
                     "gpu_fantasy_mecha", "gpu_fantasy_chibi", "qpu_keychain_hpca",
                     "quantum_chandelier", "quantum_bloch", "cpu_fantasy_chibi"]}
    row_heights = [max(fab[b].bounding_box.extents[1] for b in row) for _, row in PROD_ROWS]
    row_gap = 4.0
    total_h = sum(row_heights) + row_gap * (len(PROD_ROWS) - 1)
    prod_parts = []
    y_cur = -total_h / 2.0
    for (gap, row), rh in zip(PROD_ROWS, row_heights):
        widths = [fab[b].bounding_box.extents[0] for b in row]
        total_w = sum(widths) + gap * (len(row) - 1)
        x_cur = -total_w / 2.0
        y_c = y_cur + rh / 2.0
        for b, w in zip(row, widths):
            c = fab[b].copy()
            c.apply_translation([x_cur + w / 2.0, y_c, 0])
            prod_parts.append(c)
            x_cur += w + gap
        y_cur += rh + row_gap
    plate_p = trimesh.util.concatenate(prod_parts)
    plate_p.export(os.path.join(BATCH_DIR, "batch_production_x17.stl"))
    plate_p.export(os.path.join(BATCH_DIR, "batch_production_x17.3mf"))
    extp = plate_p.bounding_box.extents
    print(f"  Footprint: {extp[0]:.1f} x {extp[1]:.1f} x {extp[2]:.1f} mm")

    print("\nSergio Edition exported successfully!")
    print(f"Folder: {SERGIO_DIR}")


if __name__ == "__main__":
    main(plates_only="--plates-only" in sys.argv)
