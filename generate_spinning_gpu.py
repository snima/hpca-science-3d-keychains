#!/usr/bin/env python3
"""
HPC&A EDITION GPU KEYCHAIN — SPINNING FAN (SNAP-FIT MODULAR) EDITION
====================================================================
A high-reliability 2-piece modular edition:
  1. Main GPU Body with precision retention spindle pin.
  2. Detached 11-blade aerodynamic impeller rotor with snap bore.

Allows silky-smooth, zero-friction spinning with zero risk of print-in-place fusion.
Enables printing the body and rotor in contrasting colors (e.g. titanium body + gold/black rotor).
Includes "DESIGNED BY NIMA" on the underside.
"""

import os
import sys
import numpy as np
import trimesh
from build123d import *

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "output"))
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Main dimensions
CARD_LENGTH = 56.0
CARD_WIDTH = 25.0
CARD_THICKNESS = 3.4  # Slim edition for fast printing

EYELET_X = -CARD_LENGTH / 2.0 - 3.5  # -31.5 mm
EYELET_Y = 4.0
EYELET_OUTER_R = 5.2
EYELET_HOLE_R = 2.3

PCIE_LENGTH = 28.0
PCIE_PROTRUSION = 2.3
PCIE_THICKNESS = 2.0
PCIE_NOTCH_X = -6.0
PCIE_NOTCH_W = 1.6

FAN_CENTER_X = -13.0
FAN_RADIUS = 9.8
FAN_WELL_DEPTH = 2.2  # Down to Z = 2.4 mm

PIN_RADIUS = 1.80     # Ø3.6 mm pin
PIN_CLEARANCE = 0.25  # 0.25 mm radial gap for free spin

FIN_BAY_CENTER_X = 13.0
FIN_BAY_W = 19.5
FIN_BAY_H = 18.0
FIN_BAY_DEPTH = 1.8


def build_spinning_gpu_body(bottom_extra: str | None = None, coarse: bool = False) -> Part:
    """Builds the GPU body with the spindle axle pin for the snap-fit fan.

    Args:
        bottom_extra: Optional extra line on the underside (e.g. "FABLAB CASTELLÓ").
        coarse: XL underside text with deeper cut for coarse nozzles (>= 0.6 mm).
    """
    with BuildPart() as body:
        # 1. Main Shroud & Keyring Eyelet
        with BuildSketch() as s_shroud:
            Rectangle(CARD_LENGTH, CARD_WIDTH)
            fillet(s_shroud.vertices(), radius=2.2)
            with Locations((EYELET_X, EYELET_Y)):
                Circle(radius=EYELET_OUTER_R)
                Circle(radius=EYELET_HOLE_R, mode=Mode.SUBTRACT)
        extrude(amount=CARD_THICKNESS)

        # 2. Underside Attribution Inscription (Debossed at Z = 0)
        # Mirrored about YZ so it reads correctly from below (-Z view).
        if coarse:  # Sergio / 0.6 mm nozzle: XL text, deeper cut
            bottom_lines = [
                (6.0, "HPC&A EDITION", 3.0),
                (0.0, "DESIGNED BY NIMA", 2.8),
                (-6.0, bottom_extra, 2.6),
            ]
            _cut = 0.6
        elif bottom_extra is None:
            bottom_lines = [
                (3.5, "HPC&A EDITION", 2.6),
                (-3.5, "DESIGNED BY NIMA", 2.4),
            ]
            _cut = 0.35
        else:  # FabLab edition: 3 lines
            bottom_lines = [
                (6.0, "HPC&A EDITION", 2.4),
                (0.5, "DESIGNED BY NIMA", 2.2),
                (-5.5, bottom_extra, 2.0),
            ]
            _cut = 0.35
        with Locations((0, 0, 0)):
            with BuildSketch() as s_bottom:
                for _y, _txt, _fs in bottom_lines:
                    with Locations((0, _y)):
                        Text(_txt, font_size=_fs, font_style=FontStyle.BOLD)
                mirror(about=Plane.YZ, mode=Mode.REPLACE)
            extrude(amount=_cut, mode=Mode.SUBTRACT)

        # 3. PCIe Connector Tab
        with BuildSketch() as s_pcie:
            with Locations((-2.0, -CARD_WIDTH / 2.0 - PCIE_PROTRUSION / 2.0)):
                Rectangle(PCIE_LENGTH, PCIE_PROTRUSION)
                with Locations((PCIE_NOTCH_X, 0)):
                    Rectangle(PCIE_NOTCH_W, 3.0, mode=Mode.SUBTRACT)
        extrude(amount=PCIE_THICKNESS)

        # PCIe Gold Fingers
        for px in np.linspace(-14.5, 10.5, 16):
            if abs(px - PCIE_NOTCH_X) > 1.8:
                with Locations((px, -CARD_WIDTH / 2.0 - PCIE_PROTRUSION / 2.0, PCIE_THICKNESS)):
                    with BuildSketch():
                        Rectangle(0.5, 1.7)
                    extrude(amount=-0.35, mode=Mode.SUBTRACT)

        # 4. Display Ports on I/O Bracket
        for dy in [-2.0, 1.0, 4.0]:
            with Locations((-CARD_LENGTH / 2.0 - 1.0, dy, CARD_THICKNESS)):
                with BuildSketch():
                    Rectangle(1.2, 2.0)
                extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # 5. Cooling Bays
        # Left: Open Fan Bay
        with Locations((FAN_CENTER_X, 0, CARD_THICKNESS)):
            with BuildSketch():
                Circle(radius=FAN_RADIUS)
            extrude(amount=-FAN_WELL_DEPTH, mode=Mode.SUBTRACT)

        # Right: Heatsink Well
        with Locations((FIN_BAY_CENTER_X, 0, CARD_THICKNESS)):
            with BuildSketch() as s_fin_well:
                Rectangle(FIN_BAY_W, FIN_BAY_H)
                fillet(s_fin_well.vertices(), radius=1.6)
            extrude(amount=-FIN_BAY_DEPTH, mode=Mode.SUBTRACT)

        # 6. Central Spindle Axle Pin (from Z = 2.4 to 4.5 mm)
        pin_floor_z = CARD_THICKNESS - FAN_WELL_DEPTH  # 2.4 mm
        with Locations((FAN_CENTER_X, 0, pin_floor_z)):
            # Pin shaft
            with BuildSketch():
                Circle(radius=PIN_RADIUS)
            extrude(amount=1.8)
            # Retention snap-fit mushroom lip (Z = 4.2 to 4.5 mm)
            with Locations((0, 0, 1.8)):
                with BuildSketch():
                    Circle(radius=PIN_RADIUS + 0.18)
                extrude(amount=0.3)
                # Chamfered lead-in cone on top
                with Locations((0, 0, 0.3)):
                    with BuildSketch():
                        Circle(radius=PIN_RADIUS - 0.2)
                    extrude(amount=0.2)
            # Center compliance slit
            with Locations((0, 0, 1.3)):
                with BuildSketch():
                    Rectangle(0.5, PIN_RADIUS * 2.2)
                extrude(amount=1.1, mode=Mode.SUBTRACT)

        # 7. Right Bay: Heatsink Fins (from Z = 2.8 mm)
        fin_floor_z = CARD_THICKNESS - FIN_BAY_DEPTH
        for fx in np.linspace(FIN_BAY_CENTER_X - 8.0, FIN_BAY_CENTER_X + 8.0, 9):
            with Locations((fx, 0, fin_floor_z)):
                with BuildSketch():
                    Rectangle(0.85, 16.5)
                extrude(amount=1.4)

        # 8. Elevated Plaque with "HPC&A"
        with Locations((FIN_BAY_CENTER_X, 0, fin_floor_z)):
            with BuildSketch() as s_plaque:
                Rectangle(16.5, 8.2)
                fillet(s_plaque.vertices(), radius=1.2)
            extrude(amount=2.0)

            with Locations((0, 0, 2.0)):
                with BuildSketch():
                    Text("HPC&A", font_size=3.8, font_style=FontStyle.BOLD)
                extrude(amount=0.6)

        # 9. Top Spine Text "HPC&A EDITION"
        with Locations((0, CARD_WIDTH / 2.0 - 1.4, CARD_THICKNESS)):
            with BuildSketch():
                Text("HPC&A EDITION", font_size=2.2, font_style=FontStyle.BOLD)
            extrude(amount=0.5)

    return body.part


def build_spinning_rotor() -> Part:
    """Builds the detachable 11-blade fan impeller rotor for snap-fit mounting."""
    with BuildPart() as rotor:
        # Central Hub (thickness 1.8 mm)
        hub_r = 3.6
        bore_r = PIN_RADIUS + PIN_CLEARANCE  # 1.80 + 0.25 = 2.05 mm (Ø4.1 mm bore)
        
        with BuildSketch():
            Circle(radius=hub_r)
            Circle(radius=bore_r, mode=Mode.SUBTRACT)
        extrude(amount=1.8)

        # Center grip cap dome on top of hub
        with Locations((0, 0, 1.8)):
            with BuildSketch():
                Circle(radius=hub_r)
                Circle(radius=bore_r, mode=Mode.SUBTRACT)
            extrude(amount=0.3)

        # 11 Aerodynamic Swept Impeller Blades
        blade_len = 5.6
        blade_w = 1.3
        for i in range(11):
            ang = i * (360.0 / 11)
            with Locations(Rotation(0, 0, ang)):
                with Locations((hub_r + blade_len / 2.0 - 0.3, 0), Rotation(0, 0, 28)):
                    with BuildSketch() as s_blade:
                        Rectangle(blade_len, blade_w)
                        fillet(s_blade.vertices(), radius=0.3)
                    extrude(amount=1.5)

    return rotor.part


def main():
    print("=================================================================")
    print("Generating HPC&A GPU Keychain — Spinning Fan Edition...")
    print("=================================================================")

    # 1. Build and export GPU Body
    body_part = build_spinning_gpu_body()
    body_stl = os.path.join(OUTPUT_DIR, "gpu_spinning_body.stl")
    body_step = os.path.join(OUTPUT_DIR, "gpu_spinning_body.step")

    print(f"Exporting GPU Body STL: {body_stl}...")
    export_stl(body_part, body_stl, tolerance=0.005, angular_tolerance=0.1)
    print(f"Exporting GPU Body STEP: {body_step}...")
    export_step(body_part, body_step)

    # 2. Build and export Fan Rotor
    rotor_part = build_spinning_rotor()
    rotor_stl = os.path.join(OUTPUT_DIR, "gpu_spinning_rotor.stl")
    rotor_step = os.path.join(OUTPUT_DIR, "gpu_spinning_rotor.step")

    print(f"Exporting Fan Rotor STL: {rotor_stl}...")
    export_stl(rotor_part, rotor_stl, tolerance=0.005, angular_tolerance=0.1)
    print(f"Exporting Fan Rotor STEP: {rotor_step}...")
    export_step(rotor_part, rotor_step)

    # Verify meshes
    m_body = trimesh.load(body_stl)
    m_rotor = trimesh.load(rotor_stl)

    print("\n--- Verification Summary ---")
    print(f"GPU Body: Watertight = {m_body.is_watertight}, Euler = {m_body.euler_number}, Bounds = {m_body.bounding_box.extents}")
    print(f"Fan Rotor: Watertight = {m_rotor.is_watertight}, Euler = {m_rotor.euler_number}, Bounds = {m_rotor.bounding_box.extents}")
    print(f"Fan Rotor Solid Volume: {m_rotor.volume / 1000.0:.2f} cm3 (~{m_rotor.volume / 1000.0 * 1.24:.2f} g PLA)")


if __name__ == "__main__":
    main()
