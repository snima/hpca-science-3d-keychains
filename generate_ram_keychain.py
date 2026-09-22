#!/usr/bin/env python3
"""
HPC&A DDR Memory Stick Keychain Generator
=========================================
A DDR-style RAM module keychain: long PCB with end mounting eyelet
(doubles as the keyring hole, like a real DIMM notch hole), 8 memory
chips, gold edge-connector fingers with polarization notch, and an
embossed "HPC&A" top rail.

Same height class as the other keychains (~5.8 mm max) so it nests
level in the full-set batch plate.
100% support-free FDM 3D printing (flat bed at Z=0).
Author: Mechanical & CAD Design Engineer
System: build123d (OpenCASCADE)
"""

import os
import numpy as np
import trimesh
from build123d import *

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "output"))
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==============================================================================
# PARAMETRIC DIMENSIONS (mm)
# ==============================================================================
PCB_L = 60.0                # PCB length (X)
PCB_W = 20.0                # PCB width (Y)
PCB_T = 4.6                 # PCB thickness (Z: 0 -> 4.6)
PCB_R = 2.0                 # Corner fillet

# End mounting eyelet (left end, like a DIMM mounting hole)
EYELET_X = -PCB_L / 2.0 - 3.0   # -33.0
EYELET_OUTER_R = 5.2
EYELET_HOLE_R = 2.3         # Ø4.6 mm through-hole

# Edge-connector finger tab (bottom edge, like the GPU PCIe tab)
TAB_L = 56.0
TAB_PROTRUSION = 2.3
TAB_T = 2.0                 # Z: 0 -> 2.0
TAB_NOTCH_X = -6.0
TAB_NOTCH_W = 1.6

# 8 memory chips (front face)
CHIP_W = 5.0
CHIP_H = 6.5
CHIP_T = 1.2                # Z: 4.6 -> 5.8
CHIP_Y = 1.0
CHIP_XS = [-23.8, -17.0, -10.2, -3.4, 3.4, 10.2, 17.0, 23.8]

# "HPC&A" top rail text (front face)
RAIL_TEXT = "HPC&A"
RAIL_FS = 2.6
RAIL_Y = 7.0
RAIL_RELIEF = 0.5           # Z: 4.6 -> 5.1


def build_ram_keychain(bottom_extra: str | None = None) -> Part:
    """Builds the 3D-printable HPC&A DDR Memory Stick Keychain.

    Args:
        bottom_extra: Optional extra line on the underside (e.g. "PRINTED AT ...").
    """
    with BuildPart() as ram:
        # ------------------------------------------------------------------
        # 1. PCB body + end mounting eyelet
        # ------------------------------------------------------------------
        with BuildSketch() as s_body:
            Rectangle(PCB_L, PCB_W)
            fillet(s_body.vertices(), radius=PCB_R)
            with Locations((EYELET_X, 0)):
                Circle(radius=EYELET_OUTER_R)
                Circle(radius=EYELET_HOLE_R, mode=Mode.SUBTRACT)
        extrude(amount=PCB_T)

        # ------------------------------------------------------------------
        # 1B. Underside inscription (Z = 0) - mirrored for -Z readability
        # ------------------------------------------------------------------
        if bottom_extra is None:
            bottom_lines = [
                (2.5, "DDR MEMORY", 2.4),
                (-2.5, "DESIGNED BY NIMA", 2.2),
            ]
        else:  # FabLab edition: 3 lines
            bottom_lines = [
                (4.5, "DDR MEMORY", 2.4),
                (0.0, "DESIGNED BY NIMA", 2.2),
                (-4.5, bottom_extra, 2.0),
            ]
        with Locations((0, 0, 0)):
            with BuildSketch() as s_bottom:
                for _y, _txt, _fs in bottom_lines:
                    with Locations((0, _y)):
                        Text(_txt, font_size=_fs, font_style=FontStyle.BOLD)
                mirror(about=Plane.YZ, mode=Mode.REPLACE)
            extrude(amount=0.35, mode=Mode.SUBTRACT)

        # ------------------------------------------------------------------
        # 2. Edge-connector finger tab (bottom edge, Z: 0 -> 2.0)
        # ------------------------------------------------------------------
        with BuildSketch() as s_tab:
            with Locations((0, -PCB_W / 2.0 - TAB_PROTRUSION / 2.0)):
                Rectangle(TAB_L, TAB_PROTRUSION)
                with Locations((TAB_NOTCH_X, 0)):
                    Rectangle(TAB_NOTCH_W, 3.0, mode=Mode.SUBTRACT)
        extrude(amount=TAB_T)

        # Debossed gold finger contact lines on the tab
        for px in np.linspace(-26.0, 26.0, 26):
            if abs(px - TAB_NOTCH_X) > 1.8:
                with Locations((px, -PCB_W / 2.0 - TAB_PROTRUSION / 2.0, TAB_T)):
                    with BuildSketch():
                        Rectangle(0.5, 1.7)
                    extrude(amount=-0.35, mode=Mode.SUBTRACT)

        # ------------------------------------------------------------------
        # 3. 8 memory chips (Z: 4.6 -> 5.8)
        # ------------------------------------------------------------------
        for cx in CHIP_XS:
            with Locations((cx, CHIP_Y, PCB_T)):
                with BuildSketch() as s_chip:
                    Rectangle(CHIP_W, CHIP_H)
                    fillet(s_chip.vertices(), radius=0.5)
                extrude(amount=CHIP_T)
                # Chip pin-1 dimple
                with Locations((-CHIP_W / 2.0 + 0.8, CHIP_H / 2.0 - 0.8, CHIP_T)):
                    with BuildSketch():
                        Circle(radius=0.4)
                    extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # ------------------------------------------------------------------
        # 4. "HPC&A" top rail text (Z: 4.6 -> 5.1)
        # ------------------------------------------------------------------
        with Locations((2.0, RAIL_Y, PCB_T)):
            with BuildSketch():
                Text(RAIL_TEXT, font_size=RAIL_FS, font_style=FontStyle.BOLD)
            extrude(amount=RAIL_RELIEF)

    return ram.part


def main():
    print("=================================================================")
    print("Generating HPC&A DDR Memory Stick Keychain...")
    print("=================================================================")

    part = build_ram_keychain()

    stl_path = os.path.join(OUTPUT_DIR, "ram_ddr_hpca.stl")
    step_path = os.path.join(OUTPUT_DIR, "ram_ddr_hpca.step")

    export_stl(part, stl_path, tolerance=0.005, angular_tolerance=0.1)
    export_step(part, step_path)

    mesh = trimesh.load(stl_path)
    bbox = mesh.bounding_box.extents
    vol_cm3 = mesh.volume / 1000.0
    print(f"  Watertight: {mesh.is_watertight}")
    print(f"  Dimensions: {bbox[0]:.2f} x {bbox[1]:.2f} x {bbox[2]:.2f} mm")
    print(f"  Solid Volume: {vol_cm3:.2f} cm3 (~{vol_cm3 * 1.24:.1f} g PLA)")
    print("RAM Stick exported successfully!")


if __name__ == "__main__":
    main()
