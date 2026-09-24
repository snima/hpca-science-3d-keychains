#!/usr/bin/env python3
"""
GPU CON ESPADA KEYCHAIN GENERATOR (HPC&A FANTASY SUITE)
======================================================
Generates the 3D-printable GPU with Sword Keychain (GPU con Espada):
- Realistic GPU graphics card silhouette with PCIe gold fingers and heatsink fans
- Heroic energy sword integrated across the shroud with crossguard and energy blade
- Top-corner keyring eyelet for 100% support-free FDM 3D printing
Author: Mechanical & CAD Design Engineer / Antigravity
"""

import os
import trimesh
from build123d import *

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "output"))
os.makedirs(OUTPUT_DIR, exist_ok=True)
READY_STL = os.path.abspath(os.path.join(os.path.dirname(__file__), "ready_to_print", "stl"))
os.makedirs(READY_STL, exist_ok=True)

BODY_T = 3.4  # Base GPU card thickness


def build_gpu_sword(bottom_extra: str | None = None, coarse: bool = False) -> Part:
    """Builds the 3D-printable GPU con Espada Keychain."""
    with BuildPart() as gpu_sword:
        # 1. GPU Card Base Chassis + Corner Eyelet
        with BuildSketch() as s_body:
            Rectangle(58.0, 32.0)
            fillet(s_body.vertices(), radius=3.0)
            # Corner Eyelet at top-left: X = -28.0, Y = 16.0
            with Locations((-28.0, 16.0)):
                Circle(radius=5.2)
                Circle(radius=2.3, mode=Mode.SUBTRACT)
        extrude(amount=BODY_T)

        # 1B. Underside Inscription (Z = 0, depth = 0.35 mm)
        bottom_lines = [
            (5.0, "GPU CON ESPADA", 2.4),
            (-1.0, "DESIGNED BY NIMA", 2.2),
            (-7.0, "HPC&A FABLAB", 2.0),
        ]
        with Locations((0, 0, 0)):
            with BuildSketch() as s_bottom:
                for _y, _txt, _fs in bottom_lines:
                    with Locations((0, _y)):
                        Text(_txt, font_size=_fs, font_style=FontStyle.BOLD)
                mirror(about=Plane.YZ, mode=Mode.REPLACE)
            extrude(amount=0.35, mode=Mode.SUBTRACT)

        # 2. Bottom PCIe Connector Tab
        with BuildSketch() as s_pcie:
            with Locations((-3.0, -16.0 - 1.25)):
                Rectangle(28.0, 2.5)
                with Locations((-6.0, 0)):
                    Rectangle(1.6, 3.0, mode=Mode.SUBTRACT)
        extrude(amount=2.0)

        # 3. Left Bay: GPU Heatsink Fan Well (Center at X = -14.0, Y = 0)
        with Locations((-14.0, 0, BODY_T)):
            with BuildSketch():
                Circle(radius=10.5)
            extrude(amount=-1.8, mode=Mode.SUBTRACT)

        with Locations((-14.0, 0, 1.6)):
            # Central Hub
            with BuildSketch():
                Circle(radius=3.5)
            extrude(amount=1.6)
            # Fan Blades (8 curved blades)
            for i in range(8):
                ang = i * (360.0 / 8.0)
                with Locations(Rotation(0, 0, ang)):
                    with Locations((6.0, 0)):
                        with BuildSketch():
                            Rectangle(4.5, 1.2)
                        extrude(amount=1.2)

        # 4. Right Bay & Diagonal: HEROIC ENERGY SWORD (Center X = 12.0)
        # Vertical / slightly angled heroic cyber sword slicing across right half of GPU
        # Blade tip at Y = 13.0, Pommel at Y = -13.0
        sword_x = 13.0
        
        # Raised Sword Base Plate (+0.6 mm -> Z = 4.0 mm)
        with Locations((sword_x, 0, BODY_T)):
            # Diamond-shaped Energy Blade
            with Locations((0, 4.0)):
                with BuildSketch() as s_blade:
                    pts = [(0, 10.0), (3.8, 4.0), (4.2, -6.0), (-4.2, -6.0), (-3.8, 4.0)]
                    Polygon(pts)
                    fillet(s_blade.vertices().filter_by(Axis.Y), radius=0.8)
                extrude(amount=0.8)

            # Winged Crossguard at Y = -3.0 (+1.2 mm -> Z = 4.6 mm)
            with Locations((0, -3.0)):
                with BuildSketch() as s_guard:
                    pts = [(0, 1.0), (9.0, 2.0), (10.0, -1.0), (4.0, -2.5), (-4.0, -2.5), (-10.0, -1.0), (-9.0, 2.0)]
                    Polygon(pts)
                    fillet(s_guard.vertices(), radius=0.6)
                extrude(amount=1.2)

            # Central Guard Energy Gem (+1.6 mm -> Z = 5.0 mm)
            with Locations((0, -3.0)):
                with BuildSketch():
                    RegularPolygon(radius=2.2, side_count=4)
                extrude(amount=1.6)

            # Sword Grip at Y = -7.5 (+0.6 mm -> Z = 4.0 mm)
            with Locations((0, -7.0)):
                with BuildSketch() as s_grip:
                    Rectangle(2.4, 6.0)
                    fillet(s_grip.vertices(), radius=0.4)
                extrude(amount=0.6)

            # Sword Pommel at Y = -11.0 (+1.0 mm -> Z = 4.4 mm)
            with Locations((0, -11.0)):
                with BuildSketch():
                    Circle(radius=2.2)
                extrude(amount=1.0)

            # Central Blade Fuller Channel with "HPC&A" Rune (+1.2 mm -> Z = 4.6 mm)
            with Locations((0, 3.5, 0.8)):
                with BuildSketch():
                    Text("HPC&A", font_size=1.8, font_style=FontStyle.BOLD, rotation=90)
                extrude(amount=0.4)

        # 5. Top Left Banner: "GPU" Badge (+0.5 mm -> Z = 3.9 mm)
        with Locations((-14.0, 11.5, BODY_T)):
            with BuildSketch():
                Text("GPU", font_size=2.8, font_style=FontStyle.BOLD)
            extrude(amount=0.5)

        # 6. Lateral Ventilation Slots on Upper Edge
        for vx in [-3.0, 1.0, 5.0]:
            with Locations((vx, 12.0, BODY_T)):
                with BuildSketch() as s_vent:
                    Rectangle(2.2, 4.0)
                    fillet(s_vent.vertices(), radius=0.6)
                extrude(amount=-1.5, mode=Mode.SUBTRACT)

    return gpu_sword.part


def main():
    print("Generating GPU con Espada 3D CAD model...")
    model = build_gpu_sword()

    out_stl = os.path.join(OUTPUT_DIR, "gpu_fantasy_sword.stl")
    ready_stl = os.path.join(READY_STL, "gpu_fantasy_sword.stl")
    out_step = os.path.join(OUTPUT_DIR, "gpu_fantasy_sword.step")

    export_stl(model, out_stl, tolerance=0.005, angular_tolerance=0.1)
    export_stl(model, ready_stl, tolerance=0.005, angular_tolerance=0.1)
    export_step(model, out_step)

    m = trimesh.load(out_stl)
    print(f"  Exported STL: {out_stl}")
    print(f"  Watertight: {m.is_watertight}")
    print(f"  Volume: {m.volume:.1f} mm³")
    print(f"  Bounds: X=[{m.bounds[0][0]:.1f}, {m.bounds[1][0]:.1f}], Y=[{m.bounds[0][1]:.1f}, {m.bounds[1][1]:.1f}], Z=[{m.bounds[0][2]:.1f}, {m.bounds[1][2]:.1f}]")


if __name__ == "__main__":
    main()
