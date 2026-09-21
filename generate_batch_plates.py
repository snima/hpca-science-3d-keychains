#!/usr/bin/env python3
"""
MASS PRODUCTION BATCH PRINT PLATES — FANTASY & QUANTUM EDITIONS
==============================================================
Generates pre-arranged, nested print plates for 3D printing service bureaus
and print farms. Optimized for standard 220x220 mm build plates.

Batch Plates:
  1. batch_fantasy_gpus_x6.stl: 6x Fantasy GPU Keychains (2x Chibi + 2x Mecha + 2x Rune).
  2. batch_quantum_collection_x6.stl: 6x Quantum Keychains (2x QPU + 2x Chandelier + 2x Bloch).
  3. batch_master_suite_x6.stl: 6-Pack of all 6 unique models (1 of each).
"""

import os
import sys
import numpy as np
import trimesh

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "output"))


def prepare_mesh(mesh: trimesh.Trimesh) -> trimesh.Trimesh:
    """Zeroes Z to bed (Z=0) and centers in XY."""
    m = mesh.copy()
    min_z = m.bounds[0, 2]
    m.apply_translation([0, 0, -min_z])
    c_xy = (m.bounds[0, :2] + m.bounds[1, :2]) / 2.0
    m.apply_translation([-c_xy[0], -c_xy[1], 0])
    return m


def main():
    print("=================================================================")
    print("Generating Mass Production Batch Plates (Fantasy + Quantum)...")
    print("=================================================================")

    # Load the 3 Fantasy meshes
    m_chibi = prepare_mesh(trimesh.load(os.path.join(OUTPUT_DIR, "gpu_fantasy_chibi.stl")))
    m_mecha = prepare_mesh(trimesh.load(os.path.join(OUTPUT_DIR, "gpu_fantasy_mecha.stl")))
    m_rune  = prepare_mesh(trimesh.load(os.path.join(OUTPUT_DIR, "gpu_fantasy_rune.stl")))

    # Load the 3 Quantum meshes
    m_qpu   = prepare_mesh(trimesh.load(os.path.join(OUTPUT_DIR, "qpu_keychain_hpca.stl")))
    m_chand = prepare_mesh(trimesh.load(os.path.join(OUTPUT_DIR, "quantum_chandelier.stl")))
    m_bloch = prepare_mesh(trimesh.load(os.path.join(OUTPUT_DIR, "quantum_bloch.stl")))

    # --------------------------------------------------------------------------
    # 1. BATCH PLATE: 6x Fantasy GPUs (2x Chibi, 2x Mecha, 2x Rune)
    # --------------------------------------------------------------------------
    fantasy_parts = []
    # Row 1 (Y = +20 mm)
    for x_pos, m in [(-72.0, m_chibi), (0.0, m_mecha), (72.0, m_rune)]:
        c = m.copy()
        c.apply_translation([x_pos, 22.0, 0])
        fantasy_parts.append(c)
    # Row 2 (Y = -20 mm)
    for x_pos, m in [(-72.0, m_chibi), (0.0, m_mecha), (72.0, m_rune)]:
        c = m.copy()
        c.apply_translation([x_pos, -22.0, 0])
        fantasy_parts.append(c)

    plate_fantasy = trimesh.util.concatenate(fantasy_parts)
    out_f = os.path.join(OUTPUT_DIR, "batch_fantasy_gpus_x6.stl")
    plate_fantasy.export(out_f)
    print(f"Exported: {out_f}")
    print(f"  Footprint: {plate_fantasy.bounding_box.extents[0]:.1f} x {plate_fantasy.bounding_box.extents[1]:.1f} x {plate_fantasy.bounding_box.extents[2]:.1f} mm")

    # --------------------------------------------------------------------------
    # 2. BATCH PLATE: 6x Quantum Keychains (2x QPU, 2x Chandelier, 2x Bloch)
    # --------------------------------------------------------------------------
    quantum_parts = []
    # Row 1 (Y = +32 mm)
    for x_pos, m in [(-64.0, m_qpu), (0.0, m_chand), (60.0, m_bloch)]:
        c = m.copy()
        c.apply_translation([x_pos, 34.0, 0])
        quantum_parts.append(c)
    # Row 2 (Y = -32 mm)
    for x_pos, m in [(-64.0, m_qpu), (0.0, m_chand), (60.0, m_bloch)]:
        c = m.copy()
        c.apply_translation([x_pos, -34.0, 0])
        quantum_parts.append(c)

    plate_quantum = trimesh.util.concatenate(quantum_parts)
    out_q = os.path.join(OUTPUT_DIR, "batch_quantum_collection_x6.stl")
    plate_quantum.export(out_q)
    print(f"Exported: {out_q}")
    print(f"  Footprint: {plate_quantum.bounding_box.extents[0]:.1f} x {plate_quantum.bounding_box.extents[1]:.1f} x {plate_quantum.bounding_box.extents[2]:.1f} mm")

    # --------------------------------------------------------------------------
    # 3. MASTER SUITE 6-PACK: All 6 Unique Models in 1 Print Run
    # --------------------------------------------------------------------------
    master_parts = []
    # Row 1 (Top): 3 Fantasy GPUs
    for x_pos, m in [(-72.0, m_chibi), (0.0, m_mecha), (72.0, m_rune)]:
        c = m.copy()
        c.apply_translation([x_pos, 30.0, 0])
        master_parts.append(c)
    # Row 2 (Bottom): 3 Quantum Keychains
    for x_pos, m in [(-68.0, m_qpu), (0.0, m_chand), (62.0, m_bloch)]:
        c = m.copy()
        c.apply_translation([x_pos, -32.0, 0])
        master_parts.append(c)

    plate_master = trimesh.util.concatenate(master_parts)
    out_m = os.path.join(OUTPUT_DIR, "batch_master_suite_x6.stl")
    plate_master.export(out_m)
    print(f"Exported: {out_m}")
    print(f"  Footprint: {plate_master.bounding_box.extents[0]:.1f} x {plate_master.bounding_box.extents[1]:.1f} x {plate_master.bounding_box.extents[2]:.1f} mm")

    print("\nAll Mass Production Batch Plates exported successfully!")


if __name__ == "__main__":
    main()
