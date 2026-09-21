#!/usr/bin/env python3
"""
HPC&A QUANTUM PROCESSING UNIT (QPU) KEYCHAIN — CAD GENERATOR
============================================================
Parametric 3D model of a modern superconducting quantum processor package
designed for 3D printing (100% support-free FDM, flat bed adhesion at Z=0).

Architecture & Components:
  1. High-Density Ceramic/Gold-Plated Package Body (48.0 x 36.0 x 4.6 mm).
  2. Reinforced Keyring Eyelet on I/O tab (Ø4.6 mm through-hole, ≥3.0 mm solid rim).
  3. Recessed Silicon Die Cavity (Z = 2.6 to 4.6 mm).
  4. 3x3 Superconducting Transmon Qubit Array (cross transmons with Josephson junctions).
  5. Coplanar Waveguide (CPW) Serpentine Resonators connecting qubits and readout lines.
  6. Perimeter Wire-Bonding Contact Pads (28 gold pads).
  7. Top Plaque: "HPC&A QUANTUM" bold branding.
  8. Underside (Z = 0): Debossed "HPC&A QUANTUM LAB" and "DESIGNED BY NIMA".

Engineered for the HPC&A (High Performance Computing & Architecture) Research Group.
"""

import os
import sys
import numpy as np
import trimesh
from build123d import *

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "output"))
os.makedirs(OUTPUT_DIR, exist_ok=True)


def build_qpu_keychain() -> Part:
    """Builds the 3D-printable HPC&A Quantum Processor (QPU) Keychain."""
    with BuildPart() as qpu:
        # ======================================================================
        # 1. MAIN CERAMIC / GOLD-PLATED PACKAGE BODY + KEYRING EYELET
        # ======================================================================
        with BuildSketch() as s_pkg:
            Rectangle(48.0, 36.0)
            fillet(s_pkg.vertices(), radius=3.0)
            # Sturdy Keyring Eyelet Tab on left side at X = -27.5, Y = 6.0
            with Locations((-27.5, 6.0)):
                Circle(radius=5.2)
                Circle(radius=2.3, mode=Mode.SUBTRACT)  # Ø4.6 mm through-hole
        extrude(amount=4.6)

        # ======================================================================
        # 2. UNDERSIDE ATTRIBUTION INSCRIPTION (Debossed at Z = 0)
        # ======================================================================
        with Locations((0, 0, 0)):
            with BuildSketch():
                with Locations((0, 4.2)):
                    Text("HPC&A QUANTUM LAB", font_size=2.8, font_style=FontStyle.BOLD)
                with Locations((0, -4.2)):
                    Text("DESIGNED BY NIMA", font_size=2.5, font_style=FontStyle.BOLD)
            extrude(amount=0.35, mode=Mode.SUBTRACT)

        # ======================================================================
        # 3. TOP RECESSED SILICON DIE CAVITY (Z = 4.6 down to 2.6 mm)
        # ======================================================================
        with Locations((2.0, -1.5, 4.6)):
            with BuildSketch() as s_die:
                Rectangle(28.0, 24.0)
                fillet(s_die.vertices(), radius=1.6)
            extrude(amount=-2.0, mode=Mode.SUBTRACT)

        # ======================================================================
        # 4. TOP BRANDING BANNER (Z = 4.6 to 5.1 mm)
        # ======================================================================
        with Locations((2.0, 13.8, 4.6)):
            with BuildSketch():
                Text("HPC&A QUANTUM", font_size=2.8, font_style=FontStyle.BOLD)
            extrude(amount=0.5)

        # ======================================================================
        # 5. PERIMETER WIREBOND CONTACT PADS (Gold wirebonding shelf)
        # ======================================================================
        # Top and bottom row wirebond pads
        for px in np.linspace(-9.5, 13.5, 8):
            for py in [11.5, -14.5]:
                with Locations((px, py, 4.6)):
                    with BuildSketch():
                        Rectangle(1.4, 1.8)
                    extrude(amount=0.3)

        # Left and right column wirebond pads
        for py in np.linspace(-11.5, 8.5, 6):
            for px in [-13.5, 17.5]:
                with Locations((px, py, 4.6)):
                    with BuildSketch():
                        Rectangle(1.8, 1.4)
                    extrude(amount=0.3)

        # ======================================================================
        # 6. SUPERCONDUCTING TRANSMON QUBIT ARRAY (Inside die cavity, Z = 2.6 to 3.4 mm)
        # ======================================================================
        qx_list = [-5.0, 2.0, 9.0]
        qy_list = [-8.5, -1.5, 5.5]
        for qx in qx_list:
            for qy in qy_list:
                with Locations((qx, qy, 2.6)):
                    with BuildSketch():
                        Rectangle(3.4, 0.9)
                        Rectangle(0.9, 3.4)
                        Circle(radius=0.9)
                    extrude(amount=0.8)

        # ======================================================================
        # 7. COPLANAR WAVEGUIDE (CPW) SERPENTINE RESONATOR LINES
        # ======================================================================
        # Horizontal inter-qubit coupling lines
        for qy in qy_list:
            for mx in [-1.5, 5.5]:
                with Locations((mx, qy, 2.6)):
                    with BuildSketch():
                        Rectangle(2.6, 0.45)
                    extrude(amount=0.5)

        # Vertical inter-qubit coupling lines
        for qx in qx_list:
            for my in [-5.0, 2.0]:
                with Locations((qx, my, 2.6)):
                    with BuildSketch():
                        Rectangle(0.45, 2.6)
                    extrude(amount=0.5)

        # Silicon alignment fiducials at 4 corners of the chip
        for fx in [-9.5, 13.5]:
            for fy in [-11.0, 8.0]:
                with Locations((fx, fy, 2.6)):
                    with BuildSketch():
                        Rectangle(1.4, 0.35)
                        Rectangle(0.35, 1.4)
                    extrude(amount=0.4)

    return qpu.part


def main():
    print("=================================================================")
    print("Generating HPC&A Quantum Processor (QPU) Keychain...")
    print("=================================================================")

    part = build_qpu_keychain()

    stl_path = os.path.join(OUTPUT_DIR, "qpu_keychain_hpca.stl")
    step_path = os.path.join(OUTPUT_DIR, "qpu_keychain_hpca.step")

    print(f"Exporting STL: {stl_path}...")
    export_stl(part, stl_path, tolerance=0.005, angular_tolerance=0.1)

    print(f"Exporting STEP: {step_path}...")
    export_step(part, step_path)

    mesh = trimesh.load(stl_path)
    bbox = mesh.bounding_box.extents
    vol_cm3 = mesh.volume / 1000.0

    print(f"  Mesh Watertight: {mesh.is_watertight}")
    print(f"  Euler Characteristic: {mesh.euler_number}")
    print(f"  Dimensions: {bbox[0]:.2f} x {bbox[1]:.2f} x {bbox[2]:.2f} mm")
    print(f"  Solid Volume: {vol_cm3:.2f} cm3 (~{vol_cm3 * 1.24 * 0.75:.1f} g PLA)")
    print("QPU Keychain exported successfully!")


if __name__ == "__main__":
    main()
