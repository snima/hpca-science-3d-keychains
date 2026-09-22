#!/usr/bin/env python3
"""
FABLAB CASTELLO EDITION — KEYCHAINS PRINTED AT FABLAB CASTELLO
==============================================================
Generates the same keychain models but with an extra underside line
"FABLAB CASTELLO" below "DESIGNED BY NIMA", for the batch printed by
Sergio at FabLab Castello (home / community printing).

Output goes to a separate folder so the standard edition is untouched:
    fablab_castello/
        ├── stl/    (Binary STL for all slicers)
        ├── 3mf/    (Modern 3MF for Bambu Studio, PrusaSlicer, OrcaSlicer)
        └── step/   (Parametric CAD solids)

All underside inscriptions are mirrored about YZ so they read correctly
from below (-Z), with home-print-safe sizes (>= 1.8 mm).
"""

import os
import shutil
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
FABLAB_DIR = os.path.join(BASE_DIR, "fablab_castello")
STL_DIR = os.path.join(FABLAB_DIR, "stl")
THREE_MF_DIR = os.path.join(FABLAB_DIR, "3mf")
STEP_DIR = os.path.join(FABLAB_DIR, "step")
BATCH_DIR = os.path.join(FABLAB_DIR, "batch_plates")

for d in [STL_DIR, THREE_MF_DIR, STEP_DIR, BATCH_DIR]:
    os.makedirs(d, exist_ok=True)

BOTTOM_EXTRA = "PRINTED AT FABLAB CASTELLÓ"
# The chandelier back is a narrow trapezoid: no room for the long line there.
CHANDELIER_EXTRA = "PRINT: FABLAB CASTELLÓ"

# (file base name, builder callable, needs bottom_extra?)
MODELS = [
    ("gpu_keychain_hpca", lambda: build_gpu_keychain_model(bottom_extra=BOTTOM_EXTRA)),
    ("gpu_spinning_body", lambda: build_spinning_gpu_body(bottom_extra=BOTTOM_EXTRA)),
    ("gpu_fantasy_chibi", lambda: build_chibi_gpu(bottom_extra=BOTTOM_EXTRA)),
    ("gpu_fantasy_mecha", lambda: build_mecha_gpu(bottom_extra=BOTTOM_EXTRA)),
    ("gpu_fantasy_rune", lambda: build_rune_gpu(bottom_extra=BOTTOM_EXTRA)),
    ("qpu_keychain_hpca", lambda: build_qpu_chip(bottom_extra=BOTTOM_EXTRA)),
    ("quantum_chandelier", lambda: build_quantum_chandelier(bottom_extra=CHANDELIER_EXTRA)),
    ("quantum_bloch", lambda: build_quantum_bloch(bottom_extra=BOTTOM_EXTRA)),
    ("cpu_fantasy_chibi", lambda: build_fantasy_cpu(bottom_extra=BOTTOM_EXTRA)),
    ("ram_ddr_hpca", lambda: build_ram_keychain(bottom_extra=BOTTOM_EXTRA)),
]


def main(plates_only: bool = False):
    print("=================================================================")
    print("Generating FabLab Castello Edition (extra 'PRINTED AT ...' line)...")
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

    # The snap-fit rotor has no inscription; copy the standard one unchanged
    # so the spinning edition is complete in this folder too.
    rotor_src = os.path.join(BASE_DIR, "output", "gpu_spinning_rotor.stl")
    if os.path.exists(rotor_src):
        shutil.copy2(rotor_src, os.path.join(STL_DIR, "gpu_spinning_rotor.stl"))
        trimesh.load(rotor_src).export(
            os.path.join(THREE_MF_DIR, "gpu_spinning_rotor.3mf")
        )
        print("\nCopied unchanged gpu_spinning_rotor (no inscription).")

    # Full-set batch plate: all 9 keychains in 1 print (no spinning edition).
    # The educational CPU has no inscription; it is taken from output/ unchanged.
    print("\nBuilding full-set batch plate...")
    full_names = [
        "quantum_chandelier", "quantum_bloch", "cpu_fantasy_chibi",
        "gpu_fantasy_chibi", "gpu_fantasy_mecha", "gpu_fantasy_rune",
        "gpu_keychain_hpca", "qpu_keychain_hpca", "ram_ddr_hpca",
    ]
    full_slots_xy = [
        (-72.0, 68.0), (0.0, 68.0), (72.0, 68.0),
        (-72.0, 0.0), (0.0, 0.0), (72.0, 0.0),
        (-72.0, -68.0), (0.0, -68.0), (72.0, -68.0),
    ]
    full_parts = []
    for (x_pos, y_pos), base in zip(full_slots_xy, full_names):
        src = os.path.join(STL_DIR, f"{base}.stl")
        if not os.path.exists(src):  # models without inscription live in output/
            src = os.path.join(BASE_DIR, "output", f"{base}.stl")
        m = trimesh.load(src).copy()
        m.apply_translation([0, 0, -m.bounds[0, 2]])
        c_xy = (m.bounds[0, :2] + m.bounds[1, :2]) / 2.0
        m.apply_translation([-c_xy[0], -c_xy[1], 0])
        m.apply_translation([x_pos, y_pos, 0])
        full_parts.append(m)
    plate = trimesh.util.concatenate(full_parts)
    plate_stl = os.path.join(BATCH_DIR, "batch_full_set_x9.stl")
    plate_3mf = os.path.join(BATCH_DIR, "batch_full_set_x9.3mf")
    plate.export(plate_stl)
    plate.export(plate_3mf)
    ext = plate.bounding_box.extents
    print(f"  Exported: {plate_stl}")
    print(f"  Footprint: {ext[0]:.1f} x {ext[1]:.1f} x {ext[2]:.1f} mm")

    # Compact production plate x17 (same nested rows as the standard edition).
    print("\nBuilding production batch plate x17...")
    fab = {}
    for base in ["ram_ddr_hpca", "gpu_keychain_hpca", "gpu_fantasy_rune",
                 "gpu_fantasy_mecha", "gpu_fantasy_chibi", "qpu_keychain_hpca",
                 "quantum_chandelier", "quantum_bloch", "cpu_fantasy_chibi"]:
        m = trimesh.load(os.path.join(STL_DIR, f"{base}.stl")).copy()
        m.apply_translation([0, 0, -m.bounds[0, 2]])
        c_xy = (m.bounds[0, :2] + m.bounds[1, :2]) / 2.0
        m.apply_translation([-c_xy[0], -c_xy[1], 0])
        fab[base] = m
    prod_rows = [
        (4.0, ["ram_ddr_hpca", "gpu_keychain_hpca", "gpu_fantasy_rune"]),
        (4.0, ["gpu_fantasy_mecha", "gpu_fantasy_chibi", "qpu_keychain_hpca"]),
        (4.0, ["ram_ddr_hpca", "gpu_keychain_hpca", "gpu_fantasy_rune"]),
        (4.0, ["gpu_fantasy_mecha", "gpu_fantasy_chibi", "qpu_keychain_hpca"]),
        (3.0, ["quantum_chandelier", "quantum_bloch", "cpu_fantasy_chibi",
               "quantum_chandelier", "quantum_bloch"]),
    ]
    row_heights = [
        max(fab[b].bounding_box.extents[1] for b in row) for _, row in prod_rows
    ]
    row_gap = 4.0
    total_h = sum(row_heights) + row_gap * (len(prod_rows) - 1)
    prod_parts = []
    y_cur = -total_h / 2.0
    for (gap, row), rh in zip(prod_rows, row_heights):
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
    plate_p_stl = os.path.join(BATCH_DIR, "batch_production_x17.stl")
    plate_p_3mf = os.path.join(BATCH_DIR, "batch_production_x17.3mf")
    plate_p.export(plate_p_stl)
    plate_p.export(plate_p_3mf)
    extp = plate_p.bounding_box.extents
    print(f"  Exported: {plate_p_stl}")
    print(f"  Footprint: {extp[0]:.1f} x {extp[1]:.1f} x {extp[2]:.1f} mm")

    print("\nFabLab Castello Edition exported successfully!")
    print(f"Folder: {FABLAB_DIR}")


if __name__ == "__main__":
    import sys
    main(plates_only="--plates-only" in sys.argv)
