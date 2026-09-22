#!/usr/bin/env python3
"""
HPC&A QUANTUM COLLECTION — 3 DISTINCT 3D-PRINTABLE EDITIONS
============================================================
1. Model 1: HPC&A Superconducting QPU Chip (qpu_keychain_hpca.stl)
2. Model 2: 3D Conical Quantum Dilution Chandelier (quantum_chandelier.stl)
3. Model 3: Quantum Bloch Sphere & Info Medallion (quantum_bloch.stl)

All models feature:
  - 100% support-free FDM 3D printing (flat bed adhesion at Z=0).
  - Reinforced Ø4.6 mm keyring through-hole.
  - "DESIGNED BY NIMA | HPC&A" debossed on the underside.
"""

import os
import sys
import numpy as np
import trimesh
from build123d import *

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "output"))
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ==============================================================================
# MODEL 1: SUPERCONDUCTING QPU CHIP KEYCHAIN
# ==============================================================================
def build_qpu_chip() -> Part:
    with BuildPart() as qpu:
        # Package Body + Left Eyelet
        with BuildSketch() as s_pkg:
            Rectangle(48.0, 36.0)
            fillet(s_pkg.vertices(), radius=3.0)
            with Locations((-27.5, 6.0)):
                Circle(radius=5.2)
                Circle(radius=2.3, mode=Mode.SUBTRACT)
        extrude(amount=4.6)

        # Underside (Z = 0) - mirrored about YZ for correct -Z (bottom) readability
        with Locations((0, 0, 0)):
            with BuildSketch() as s_bottom:
                with Locations((0, 4.2)):
                    Text("HPC&A QUANTUM LAB", font_size=2.8, font_style=FontStyle.BOLD)
                with Locations((0, -4.2)):
                    Text("DESIGNED BY NIMA", font_size=2.5, font_style=FontStyle.BOLD)
                mirror(about=Plane.YZ, mode=Mode.REPLACE)
            extrude(amount=0.35, mode=Mode.SUBTRACT)

        # Recessed Silicon Die Cavity
        with Locations((2.0, -1.5, 4.6)):
            with BuildSketch() as s_die:
                Rectangle(28.0, 24.0)
                fillet(s_die.vertices(), radius=1.6)
            extrude(amount=-2.0, mode=Mode.SUBTRACT)

        # Top Banner
        with Locations((2.0, 13.8, 4.6)):
            with BuildSketch():
                Text("HPC&A QUANTUM", font_size=2.8, font_style=FontStyle.BOLD)
            extrude(amount=0.5)

        # Wirebond Contact Pads
        for px in np.linspace(-9.5, 13.5, 8):
            for py in [11.5, -14.5]:
                with Locations((px, py, 4.6)):
                    with BuildSketch():
                        Rectangle(1.4, 1.8)
                    extrude(amount=0.3)

        for py in np.linspace(-11.5, 8.5, 6):
            for px in [-13.5, 17.5]:
                with Locations((px, py, 4.6)):
                    with BuildSketch():
                        Rectangle(1.8, 1.4)
                    extrude(amount=0.3)

        # 3x3 Transmon Qubits
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

        # CPW Resonator Meanders
        for qy in qy_list:
            for mx in [-1.5, 5.5]:
                with Locations((mx, qy, 2.6)):
                    with BuildSketch():
                        Rectangle(2.6, 0.45)
                    extrude(amount=0.5)

        for qx in qx_list:
            for my in [-5.0, 2.0]:
                with Locations((qx, my, 2.6)):
                    with BuildSketch():
                        Rectangle(0.45, 2.6)
                    extrude(amount=0.5)

        # Corner Fiducials
        for fx in [-9.5, 13.5]:
            for fy in [-11.0, 8.0]:
                with Locations((fx, fy, 2.6)):
                    with BuildSketch():
                        Rectangle(1.4, 0.35)
                        Rectangle(0.35, 1.4)
                    extrude(amount=0.4)

    return qpu.part


# ==============================================================================
# MODEL 2: 2.5D SLEEK TIERED QUANTUM DILUTION CHANDELIER
# ==============================================================================
def build_quantum_chandelier() -> Part:
    """Builds the sleek 2.5D tiered dilution refrigerator chandelier keychain."""
    with BuildPart() as chand:
        # 1. Base Plate: Smooth tapered trapezoidal silhouette
        # Y spans from -28 to +25 mm (53 mm tall body).
        # Top width = 32 mm, Bottom width = 13 mm.
        pts = [
            (-16.0, 25.0),
            (16.0, 25.0),
            (6.5, -28.0),
            (-6.5, -28.0),
        ]
        with BuildSketch() as s_base:
            with BuildLine():
                l1 = Line(pts[0], pts[1])
                l2 = Line(pts[1], pts[2])
                l3 = Line(pts[2], pts[3])
                l4 = Line(pts[3], pts[0])
            make_face()
            fillet(s_base.vertices(), radius=2.0)

            # Integrated Keyring Hanging Eyelet at Y = 28.5 mm
            with Locations((0, 28.5)):
                Circle(radius=5.2)
                Circle(radius=2.3, mode=Mode.SUBTRACT)  # Ø4.6 mm standard hole
        extrude(amount=4.0)

        # 2. Underside Debossed Inscription (Z = 0, depth = 0.35 mm)
        # Base plate widths: at Y=18 -> 29.5 mm, at Y=11 -> 27.0 mm, at Y=-20 -> 15.8 mm.
        # Texts have >5 mm clearance from all outer contours!
        # Mirrored about YZ for correct -Z (bottom) readability.
        with Locations((0, 0, 0)):
            with BuildSketch() as s_bottom:
                with Locations((0, 18.0)):
                    Text("HPC&A CRYOSTAT", font_size=1.8, font_style=FontStyle.BOLD)
                with Locations((0, 11.0)):
                    Text("DESIGNED BY NIMA", font_size=1.8, font_style=FontStyle.BOLD)
                with Locations((0, -20.0)):
                    Text("15 mK", font_size=1.8, font_style=FontStyle.BOLD)
                mirror(about=Plane.YZ, mode=Mode.REPLACE)
            extrude(amount=0.35, mode=Mode.SUBTRACT)

        # 3. Front Details (Base Z = 4.0 mm)
        stages = [
            (23.5, 30.0, 3.0),   # 300 K / 50 K stage plate
            (14.0, 26.0, 2.5),   # 4 K stage plate
            (4.0, 22.0, 2.2),    # Still stage (800 mK)
            (-5.0, 18.0, 2.0),   # 100 mK cold plate
            (-13.0, 14.0, 1.8),  # 15 mK mixing chamber plate
        ]

        with Locations((0, 0, 4.0)):
            # Raised Stage Plates (+0.8 mm -> Z = 4.8 mm)
            for y_pos, w, h in stages:
                with Locations((0, y_pos)):
                    with BuildSketch() as s_stage:
                        Rectangle(w, h)
                        fillet(s_stage.vertices(), radius=0.6)
                    extrude(amount=0.8)

            # Central Vertical RF Coaxial Struts / Waveguides (+0.5 mm -> Z = 4.5 mm)
            for x_offset in [-6.0, -2.0, 2.0, 6.0]:
                with Locations((x_offset, 0)):
                    with BuildSketch():
                        Rectangle(0.9, 44.0)
                    extrude(amount=0.5)

            # Helical Heat Exchanger Coils on sides (+0.6 mm -> Z = 4.6 mm)
            for side in [-1, 1]:
                for y_coil in [19.0, 9.5, 0.0, -9.0]:
                    x_c = side * (10.0 - (20.0 - y_coil) * 0.15)
                    with Locations((x_c, y_coil)):
                        with BuildSketch():
                            Circle(radius=1.8)
                            Circle(radius=1.0, mode=Mode.SUBTRACT)
                        extrude(amount=0.6)

            # Bottom Cylindrical Gold QPU Shielding Can (+1.0 mm -> Z = 5.0 mm)
            with Locations((0, -21.0)):
                with BuildSketch() as s_can:
                    Rectangle(10.0, 12.0)
                    fillet(s_can.vertices(), radius=1.2)
                extrude(amount=1.0)

            # Front Text on Top Flange (+0.4 mm on top of stage -> Z = 5.2 mm)
            # Text width = 7.6 mm, Flange width = 30.0 mm -> 11.2 mm margin on each side!
            with Locations((0, 23.5, 0.8)):
                with BuildSketch():
                    Text("HPC&A", font_size=2.2, font_style=FontStyle.BOLD)
                extrude(amount=0.4)

            # Front Text on Bottom QPU Can (+0.4 mm on top of can -> Z = 5.4 mm)
            # Text width = 3.74 mm, Can width = 10.0 mm -> 3.13 mm margin on each side!
            with Locations((0, -21.0, 1.0)):
                with BuildSketch():
                    Text("QPU", font_size=1.8, font_style=FontStyle.BOLD)
                extrude(amount=0.4)

    return chand.part


# ==============================================================================
# MODEL 3: BLOCH SPHERE & QUANTUM INFO MEDALLION
# ==============================================================================
def build_quantum_bloch() -> Part:
    with BuildPart() as bloch:
        # 1. Octagonal Medallion + Top Hanging Eyelet
        with BuildSketch() as s_body:
            RegularPolygon(radius=22.0, side_count=8)
            fillet(s_body.vertices(), radius=2.0)
            with Locations((0, 22.0)):
                Circle(radius=5.2)
                Circle(radius=2.3, mode=Mode.SUBTRACT)
        extrude(amount=4.6)

        # 2. Underside Inscription (Z = 0) - mirrored about YZ for correct -Z readability
        with Locations((0, 0, 0)):
            with BuildSketch() as s_bottom:
                with Locations((0, 4.0)):
                    Text("BLOCH SPHERE", font_size=2.6, font_style=FontStyle.BOLD)
                with Locations((0, -4.0)):
                    Text("DESIGNED BY NIMA", font_size=2.3, font_style=FontStyle.BOLD)
                mirror(about=Plane.YZ, mode=Mode.REPLACE)
            extrude(amount=0.35, mode=Mode.SUBTRACT)

        # 3. Recessed Central Well (Z = 4.6 to 2.6 mm)
        with Locations((0, -1.0, 4.6)):
            with BuildSketch():
                Circle(radius=16.0)
            extrude(amount=-2.0, mode=Mode.SUBTRACT)

        # 4. 3D Bloch Sphere Dome & State Vectors (from Z = 2.6 mm)
        with Locations((0, -1.0, 2.6)):
            # Base Sphere Dome
            with BuildSketch():
                Circle(radius=11.5)
            extrude(amount=1.0)

            # Equator Ellipse
            with Locations((0, 0, 1.0)):
                with BuildSketch():
                    Ellipse(11.0, 3.8)
                    Ellipse(9.8, 2.6, mode=Mode.SUBTRACT)
                extrude(amount=0.6)

            # Meridian Ellipse
            with Locations((0, 0, 1.0)):
                with BuildSketch():
                    Ellipse(3.8, 11.0)
                    Ellipse(2.6, 9.8, mode=Mode.SUBTRACT)
                extrude(amount=0.6)

            # Z-Axis Spindle
            with Locations((0, 0, 1.0)):
                with BuildSketch():
                    Rectangle(0.8, 23.0)
                extrude(amount=0.7)

            # State Vector |psi> arrow at 40 degrees
            with Locations(Rotation(0, 0, 40)):
                with Locations((4.0, 0, 1.0)):
                    with BuildSketch():
                        Rectangle(8.0, 1.1)
                    extrude(amount=0.9)
                    with Locations((4.5, 0)):
                        with BuildSketch():
                            Triangle(a=2.2, b=2.2, C=60)
                        extrude(amount=0.9)

            # North Pole State |0>
            with Locations((0, 12.8, 1.0)):
                with BuildSketch():
                    Text("|0>", font_size=2.5, font_style=FontStyle.BOLD)
                extrude(amount=0.7)

            # South Pole State |1>
            with Locations((0, -13.0, 1.0)):
                with BuildSketch():
                    Text("|1>", font_size=2.5, font_style=FontStyle.BOLD)
                extrude(amount=0.7)

            # State Vector Label |psi>
            with Locations((6.5, 6.5, 1.0)):
                with BuildSketch():
                    Text("|ψ>", font_size=2.5, font_style=FontStyle.BOLD)
                extrude(amount=0.8)

        # 5. Top Crest "HPC&A QUANTUM"
        with Locations((0, 16.0, 4.6)):
            with BuildSketch():
                Text("HPC&A QUANTUM", font_size=2.4, font_style=FontStyle.BOLD)
            extrude(amount=0.5)

    return bloch.part


def main():
    print("=================================================================")
    print("Generating All 3 HPC&A Quantum Editions...")
    print("=================================================================")

    models = [
        ("qpu_keychain_hpca", build_qpu_chip),
        ("quantum_chandelier", build_quantum_chandelier),
        ("quantum_bloch", build_quantum_bloch),
    ]

    for name, builder in models:
        print(f"\nBuilding {name}...")
        part = builder()

        stl_path = os.path.join(OUTPUT_DIR, f"{name}.stl")
        step_path = os.path.join(OUTPUT_DIR, f"{name}.step")

        print(f"  Exporting STL: {stl_path}...")
        export_stl(part, stl_path, tolerance=0.005, angular_tolerance=0.1)

        print(f"  Exporting STEP: {step_path}...")
        export_step(part, step_path)

        mesh = trimesh.load(stl_path)
        bbox = mesh.bounding_box.extents
        vol_cm3 = mesh.volume / 1000.0

        print(f"  Watertight: {mesh.is_watertight}")
        print(f"  Euler Characteristic: {mesh.euler_number}")
        print(f"  Dimensions: {bbox[0]:.2f} x {bbox[1]:.2f} x {bbox[2]:.2f} mm")
        print(f"  Solid Volume: {vol_cm3:.2f} cm3 (~{vol_cm3 * 1.24 * 0.75:.1f} g PLA)")

    print("\nAll 3 Quantum Models exported successfully!")


if __name__ == "__main__":
    main()
