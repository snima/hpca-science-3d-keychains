#!/usr/bin/env python3
"""
HPC&A CYBER SWORD KEYCHAIN GENERATOR
====================================
Parametric CAD Generator for the 3D-Printable Science Cyber Sword Keychain.
Engineered for 100% support-free FDM 3D printing with integrated keyring pommel.
Author: Mechanical & CAD Design Engineer / Antigravity
"""

import os
import trimesh
from build123d import *

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "output"))
os.makedirs(OUTPUT_DIR, exist_ok=True)
READY_STL = os.path.abspath(os.path.join(os.path.dirname(__file__), "ready_to_print", "stl"))
os.makedirs(READY_STL, exist_ok=True)

BODY_T = 3.4  # Main blade and handle thickness
GUARD_T = 4.4 # Crossguard thickness


def build_sword_keychain(bottom_extra: str | None = None, coarse: bool = False) -> Part:
    """Builds the 3D-printable Cyber Sword Keychain.
    
    Y-axis oriented:
    - Pommel Eyelet at Y = -29.0 mm
    - Handle / Grip from Y = -24.0 to -11.0 mm
    - Crossguard from Y = -11.0 to -4.0 mm (Width: 26 mm)
    - Tapered Energy Blade from Y = -4.0 to +32.0 mm (Tip at Y = 32.0 mm)
    """
    with BuildPart() as sword:
        pts_right = [
            (0.0, 32.0),       # Tip
            (5.5, 20.0),       # Upper blade taper
            (6.5, 4.0),        # Mid blade
            (6.0, -4.5),       # Blade base
            (13.0, -6.5),      # Guard upper wing
            (13.0, -9.5),      # Guard outer edge
            (9.0, -11.5),      # Guard lower angle
            (3.8, -11.5),      # Guard to grip notch
            (3.5, -23.0),      # Grip bottom
            (5.5, -25.0),      # Pommel flare
            (5.2, -29.0),      # Pommel eyelet right
            (0.0, -34.2),      # Pommel bottom
        ]
        
        # Build symmetric outline
        pts_left = [(-x, y) for x, y in reversed(pts_right[1:-1])]
        all_pts = pts_right + pts_left

        with BuildSketch() as s_base:
            with BuildLine():
                for i in range(len(all_pts)):
                    p1 = all_pts[i]
                    p2 = all_pts[(i + 1) % len(all_pts)]
                    Line(p1, p2)
            make_face()
            fillet(s_base.vertices().filter_by(Axis.Y), radius=1.0)
            
            # Keyring hole at Pommel (Ø4.6 mm standard hole)
            with Locations((0, -29.0)):
                Circle(radius=2.3, mode=Mode.SUBTRACT)

        extrude(amount=BODY_T)

        # 2. Underside Debossed Inscription (Z = 0, depth = 0.35 mm)
        bottom_lines = [
            (10.0, "HPC&A SWORD", 2.0),
            (2.0, "DESIGNED BY NIMA", 1.8),
            (-17.0, "FABLAB", 1.8),
        ]
        with Locations((0, 0, 0)):
            with BuildSketch() as s_bottom:
                for _y, _txt, _fs in bottom_lines:
                    with Locations((0, _y)):
                        Text(_txt, font_size=_fs, font_style=FontStyle.BOLD)
                mirror(about=Plane.YZ, mode=Mode.REPLACE)
            extrude(amount=0.35, mode=Mode.SUBTRACT)

        # 3. Raised Crossguard Plate & Power Core (Z = BODY_T)
        with Locations((0, 0, BODY_T)):
            # Guard wing reinforcement (+0.8 mm -> Z = 4.2 mm)
            with BuildSketch() as s_guard:
                with BuildLine():
                    Line((-11.5, -7.0), (11.5, -7.0))
                    Line((11.5, -7.0), (12.0, -9.5))
                    Line((12.0, -9.5), (8.0, -11.5))
                    Line((8.0, -11.5), (-8.0, -11.5))
                    Line((-8.0, -11.5), (-12.0, -9.5))
                    Line((-12.0, -9.5), (-11.5, -7.0))
                make_face()
            extrude(amount=0.8)

            # Central Energy Diamond / Core (+1.2 mm -> Z = 4.6 mm)
            with Locations((0, -9.0)):
                with BuildSketch():
                    RegularPolygon(radius=3.5, side_count=4)
                extrude(amount=1.2)

            # Grip Texture Ribs (+0.4 mm -> Z = 3.8 mm)
            for y_rib in [-15.0, -17.5, -20.0]:
                with Locations((0, y_rib)):
                    with BuildSketch() as s_rib:
                        Rectangle(6.0, 1.2)
                        fillet(s_rib.vertices(), radius=0.4)
                    extrude(amount=0.4)

            # Blade Central Fuller & Rune Channel (+0.6 mm -> Z = 4.0 mm)
            with Locations((0, 12.0)):
                with BuildSketch() as s_fuller:
                    Rectangle(2.8, 30.0)
                    fillet(s_fuller.vertices(), radius=0.8)
                extrude(amount=0.6)

            # Embossed "HPC&A" Runes on the Blade (+1.0 mm -> Z = 4.4 mm)
            with Locations((0, 12.0, 0.6)):
                with BuildSketch():
                    Text("HPC&A", font_size=2.4, font_style=FontStyle.BOLD, rotation=90)
                extrude(amount=0.4)

    return sword.part


def main():
    print("Generating HPC&A Cyber Sword 3D CAD model...")
    sword = build_sword_keychain()

    out_stl = os.path.join(OUTPUT_DIR, "sword_keychain_hpca.stl")
    ready_stl = os.path.join(READY_STL, "sword_keychain_hpca.stl")
    out_step = os.path.join(OUTPUT_DIR, "sword_keychain_hpca.step")

    export_stl(sword, out_stl, tolerance=0.005, angular_tolerance=0.1)
    export_stl(sword, ready_stl, tolerance=0.005, angular_tolerance=0.1)
    export_step(sword, out_step)

    # Validate with trimesh
    m = trimesh.load(out_stl)
    print(f"  Exported STL: {out_stl}")
    print(f"  Watertight: {m.is_watertight}")
    print(f"  Volume: {m.volume:.1f} mm³")
    print(f"  Bounds: X=[{m.bounds[0][0]:.1f}, {m.bounds[1][0]:.1f}], Y=[{m.bounds[0][1]:.1f}, {m.bounds[1][1]:.1f}], Z=[{m.bounds[0][2]:.1f}, {m.bounds[1][2]:.1f}]")


if __name__ == "__main__":
    main()
