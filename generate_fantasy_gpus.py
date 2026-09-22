"""
HPC&A Fantasy GPU Keychains Generator
Parametric CAD Generator for 3 Unique Fantasy GPU Keychains:
1. Chibi / Kawaii Character GPU
2. Sci-Fi / Mecha Starship GPU
3. Magic Rune / Crystal Artifact GPU

All models are engineered for 100% support-free FDM 3D printing.
Author: Mechanical & CAD Design Engineer
System: build123d (OpenCASCADE)
"""

import os
import shutil
import numpy as np
import trimesh
from build123d import *

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "output"))
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ==============================================================================
# MODEL 1: CHIBI / KAWAII CHARACTER GPU KEYCHAIN
# ==============================================================================
def build_chibi_gpu(bottom_extra: str | None = None) -> Part:
    """Builds the 3D-printable Chibi Kawaii GPU Character Keychain.

    Args:
        bottom_extra: Optional extra line on the underside (e.g. "FABLAB CASTELLÓ").
    """
    with BuildPart() as chibi:
        # 1. Cute Pillowy Card Body + Integrated Keyring Eyelet
        with BuildSketch() as s:
            Rectangle(50.0, 26.0)
            fillet(s.vertices(), radius=3.2)
            # Corner Eyelet at X = -25.0, Y = 13.0
            with Locations((-25.0, 13.0)):
                Circle(radius=5.2)
                Circle(radius=2.3, mode=Mode.SUBTRACT)
        extrude(amount=4.6)

        # 1B. Underside Inscription (Z = 0) - mirrored about YZ for correct -Z readability
        if bottom_extra is None:
            bottom_lines = [
                (3.5, "CHIBI GPU", 2.4),
                (-3.5, "DESIGNED BY NIMA", 2.2),
            ]
        else:  # FabLab edition: 3 lines
            bottom_lines = [
                (6.0, "CHIBI GPU", 2.4),
                (0.5, "DESIGNED BY NIMA", 2.2),
                (-5.5, bottom_extra, 2.0),
            ]
        with Locations((0, 0, 0)):
            with BuildSketch() as s_bottom:
                for _y, _txt, _fs in bottom_lines:
                    with Locations((0, _y)):
                        Text(_txt, font_size=_fs, font_style=FontStyle.BOLD)
                mirror(about=Plane.YZ, mode=Mode.REPLACE)
            extrude(amount=0.35, mode=Mode.SUBTRACT)

        # 2. Cute Rounded Boots / Feet at bottom (PCIe Tab replacement)
        for bx in [-10.0, 6.0]:
            with Locations((bx, -13.0 - 1.6, 0)):
                with BuildSketch() as s_boot:
                    Rectangle(9.0, 3.2)
                    fillet(s_boot.vertices(), radius=1.4)
                extrude(amount=2.2)
                # Cute rounded toe cap (contained inside boot boundaries)
                with Locations((0, 0, 2.2)):
                    with BuildSketch():
                        Circle(radius=0.9)
                    extrude(amount=0.4)

        # 3. Circular Fan Well
        with Locations((-5.0, -1.8, 4.6)):
            with BuildSketch():
                Circle(radius=8.8)
            extrude(amount=-2.2, mode=Mode.SUBTRACT)

        # 4. Fan Interior (From floor Z = 2.4 mm)
        with Locations((-5.0, -1.8, 2.4)):
            # Chubby Smiling Face Hub (reaches Z = 4.2 mm)
            with BuildSketch():
                Circle(radius=4.6)
            extrude(amount=1.8)

            # 8 Curved petal-like fan blades
            for i in range(8):
                ang = i * (360.0 / 8)
                with Locations(Rotation(0, 0, ang)):
                    with Locations((6.5, 0), Rotation(0, 0, 20)):
                        with BuildSketch() as s_pet:
                            Rectangle(4.0, 1.8)
                            fillet(s_pet.vertices(), radius=0.7)
                        extrude(amount=1.4)

            # Friendly Smiling Face on Hub (at Z = 4.2 mm)
            with Locations((0, 0, 1.8)):
                # Cartoon Eyes with Sparkle Pupils
                for ex in [-1.8, 1.8]:
                    with Locations((ex, 1.0)):
                        with BuildSketch():
                            Circle(radius=0.8)
                        extrude(amount=0.4)
                        with Locations((0.25, 0.25, 0.4)):
                            with BuildSketch():
                                Circle(radius=0.3)
                            extrude(amount=0.2)
                # Open Smiling Mouth
                with Locations((0, -1.0)):
                    with BuildSketch():
                        Circle(radius=1.2)
                        with Locations((0, 0.6)):
                            Rectangle(3.0, 1.2, mode=Mode.SUBTRACT)
                    extrude(amount=0.3)
                # Rosy Cheeks
                for cx in [-3.0, 3.0]:
                    with Locations((cx, -0.1)):
                        with BuildSketch():
                            Circle(radius=0.6)
                        extrude(amount=0.25)

        # 5. Top Curved Banner with "HPC&A" (Z = 4.6 -> 5.5 mm)
        with Locations((0, 10.0, 4.6)):
            with BuildSketch() as s_ban:
                Rectangle(22.0, 4.2)
                fillet(s_ban.vertices(), radius=1.4)
            extrude(amount=0.4)
            with Locations((0, 0, 0.4)):
                with BuildSketch():
                    Text("HPC&A", font_size=3.2, font_style=FontStyle.BOLD)
                extrude(amount=0.5)

        # 6. Right Side Decorative Pill Vents
        with Locations((16.0, -1.8, 4.6)):
            for vy in [-5.0, -1.5, 2.0, 5.5]:
                with Locations((0, vy)):
                    with BuildSketch() as s_v:
                        Rectangle(4.5, 1.6)
                        fillet(s_v.vertices(), radius=0.7)
                    extrude(amount=-1.2, mode=Mode.SUBTRACT)

    return chibi.part


# ==============================================================================
# MODEL 2: SCI-FI / MECHA STARSHIP GPU KEYCHAIN
# ==============================================================================
def build_mecha_gpu(bottom_extra: str | None = None) -> Part:
    """Builds the 3D-printable Sci-Fi Mecha Starship GPU Keychain.

    Args:
        bottom_extra: Optional extra line on the underside (e.g. "FABLAB CASTELLÓ").
    """
    with BuildPart() as mecha:
        # 1. Angular Mecha Starship Hull + Rear Thruster Eyelet
        with BuildSketch() as s_hull:
            pts = [
                (28.0, 0.0),    # Forward sensor nose
                (20.0, 12.5),
                (6.0, 12.5),
                (0.0, 15.0),    # Upper stabilizer winglet tip
                (-6.0, 12.5),
                (-26.0, 12.5),
                (-26.0, -12.5),
                (-6.0, -12.5),
                (0.0, -15.0),   # Lower stabilizer winglet tip
                (6.0, -12.5),
                (20.0, -12.5),
            ]
            Polygon(pts)
            fillet(s_hull.vertices(), radius=1.5)

            # Rear Rocket Thruster Nozzle with Keyring Eyelet at X = -30.5
            with Locations((-30.5, 0.0)):
                Circle(radius=5.2)
                Circle(radius=2.3, mode=Mode.SUBTRACT)
        extrude(amount=4.6)

        # 1B. Underside Inscription (Z = 0) - mirrored about YZ for correct -Z readability
        if bottom_extra is None:
            bottom_lines = [
                (3.5, "MECHA STARSHIP", 2.4),
                (-3.5, "DESIGNED BY NIMA", 2.2),
            ]
        else:  # FabLab edition: 3 lines
            bottom_lines = [
                (6.0, "MECHA STARSHIP", 2.4),
                (0.5, "DESIGNED BY NIMA", 2.2),
                (-5.5, bottom_extra, 2.0),
            ]
        with Locations((0, 0, 0)):
            with BuildSketch() as s_bottom:
                for _y, _txt, _fs in bottom_lines:
                    with Locations((0, _y)):
                        Text(_txt, font_size=_fs, font_style=FontStyle.BOLD)
                mirror(about=Plane.YZ, mode=Mode.REPLACE)
            extrude(amount=0.35, mode=Mode.SUBTRACT)

        # 2. PCIe Energy Conduit Bus Tab along bottom edge
        with BuildSketch() as s_pcie:
            with Locations((-2.0, -12.5 - 1.25)):
                Rectangle(26.0, 2.5)
                with Locations((-6.0, 0)):
                    Rectangle(1.6, 3.0, mode=Mode.SUBTRACT)
        extrude(amount=2.0)

        # 3. Supersonic Jet Turbine Intake (Left bay, center at X = -11.0)
        with Locations((-11.0, 0, 4.6)):
            with BuildSketch():
                Circle(radius=9.5)
            extrude(amount=-2.2, mode=Mode.SUBTRACT)

        # Turbine interior (from Z = 2.4 mm)
        with Locations((-11.0, 0, 2.4)):
            # Central Aerodynamic Bullet Nose Cone
            with BuildSketch():
                Circle(radius=3.2)
            extrude(amount=1.8)
            with Locations((0, 0, 1.8)):
                with BuildSketch():
                    Circle(radius=1.5)
                extrude(amount=0.4)

            # 12 Swept supersonic intake blades
            for i in range(12):
                ang = i * (360.0 / 12)
                with Locations(Rotation(0, 0, ang)):
                    with Locations((6.0, 0), Rotation(0, 0, 30)):
                        with BuildSketch():
                            Rectangle(4.8, 1.1)
                        extrude(amount=1.5)

        # 4. Plasma Radiator Fin Grille (Right bay, center at X = 13.0)
        with Locations((13.0, 0, 4.6)):
            with BuildSketch() as s_rad:
                Rectangle(18.0, 16.0)
                fillet(s_rad.vertices(), radius=1.4)
            extrude(amount=-1.8, mode=Mode.SUBTRACT)

        # Radiator slats (from Z = 2.8 mm)
        for rx in np.linspace(5.5, 20.5, 7):
            with Locations((rx, 0, 2.8)):
                with BuildSketch():
                    Rectangle(1.1, 14.5)
                extrude(amount=1.2)

        # 5. Heavy Armored Nameplate with "HPC&A"
        with Locations((13.0, 0, 2.8)):
            with BuildSketch() as s_plq:
                Rectangle(16.0, 8.0)
                fillet(s_plq.vertices(), radius=1.0)
            extrude(amount=2.2)  # reaches Z = 5.0 mm

            with Locations((0, 0, 2.2)):
                with BuildSketch():
                    Text("HPC&A", font_size=3.6, font_style=FontStyle.BOLD)
                extrude(amount=0.6)  # reaches Z = 5.6 mm

        # 6. Armor Panel Grooves on Hull
        for gy in [8.5, -8.5]:
            with Locations((0, gy, 4.6)):
                with BuildSketch():
                    Rectangle(32.0, 0.6)
                extrude(amount=-0.4, mode=Mode.SUBTRACT)

    return mecha.part


# ==============================================================================
# MODEL 3: MAGIC RUNE / CRYSTAL ARTIFACT GPU KEYCHAIN
# ==============================================================================
def build_rune_gpu(bottom_extra: str | None = None) -> Part:
    """Builds the 3D-printable Magic Rune / Crystal Artifact GPU Keychain.

    Args:
        bottom_extra: Optional extra line on the underside (e.g. "FABLAB CASTELLÓ").
    """
    with BuildPart() as rune:
        # 1. Antique Dwarven Armor Frame (Z = 0 to 4.6 mm) + Keyring Eyelet
        with BuildSketch() as s_body:
            Rectangle(56.0, 26.0)
            fillet(s_body.vertices(), radius=2.5)
            # Left Bracket Eyelet at X = -31.5, Y = 3.5
            with Locations((-31.5, 3.5)):
                Circle(radius=5.2)
                Circle(radius=2.3, mode=Mode.SUBTRACT)
        extrude(amount=4.6)

        # 1B. Underside Inscription (Z = 0) - mirrored about YZ for correct -Z readability
        if bottom_extra is None:
            bottom_lines = [
                (3.5, "MAGIC RUNE GPU", 2.4),
                (-3.5, "DESIGNED BY NIMA", 2.2),
            ]
        else:  # FabLab edition: 3 lines
            bottom_lines = [
                (6.0, "MAGIC RUNE GPU", 2.4),
                (0.5, "DESIGNED BY NIMA", 2.2),
                (-5.5, bottom_extra, 2.0),
            ]
        with Locations((0, 0, 0)):
            with BuildSketch() as s_bottom:
                for _y, _txt, _fs in bottom_lines:
                    with Locations((0, _y)):
                        Text(_txt, font_size=_fs, font_style=FontStyle.BOLD)
                mirror(about=Plane.YZ, mode=Mode.REPLACE)
            extrude(amount=0.35, mode=Mode.SUBTRACT)

        # 2. Bottom Runic Golden Teeth (PCIe Tab at bottom)
        with BuildSketch() as s_pcie:
            with Locations((-2.0, -13.0 - 1.25)):
                Rectangle(28.0, 2.5)
                with Locations((-6.0, 0)):
                    Rectangle(1.6, 3.0, mode=Mode.SUBTRACT)
        extrude(amount=2.0)

        # Individual runic teeth notches on PCIe tab
        for tx in np.linspace(-14.0, 10.0, 12):
            if abs(tx - (-6.0)) > 1.8:
                with Locations((tx, -13.0 - 1.25, 2.0)):
                    with BuildSketch():
                        Rectangle(0.6, 1.8)
                    extrude(amount=-0.35, mode=Mode.SUBTRACT)

        # 3. Corner Rivet Bosses (Dwarven armor aesthetics)
        for cx in [-25.0, 25.0]:
            for cy in [-10.5, 10.5]:
                with Locations((cx, cy, 4.6)):
                    with BuildSketch():
                        Circle(radius=1.1)
                    extrude(amount=0.4)
                    with Locations((0, 0, 0.4)):
                        with BuildSketch():
                            Circle(radius=0.6)
                        extrude(amount=0.2)

        # 4. Left Bay: The Arcane Magic Circle (center at X = -16.0, radius 8.6 -> right edge at -7.4)
        with Locations((-16.0, 0, 4.6)):
            with BuildSketch():
                Circle(radius=8.6)
            extrude(amount=-2.2, mode=Mode.SUBTRACT)

        with Locations((-16.0, 0, 2.4)):
            # Outer ring
            with BuildSketch():
                Circle(radius=8.2)
                Circle(radius=7.2, mode=Mode.SUBTRACT)
            extrude(amount=1.5)
            # Inner ring
            with BuildSketch():
                Circle(radius=4.2)
                Circle(radius=3.3, mode=Mode.SUBTRACT)
            extrude(amount=1.5)
            # Central Orb
            with BuildSketch():
                Circle(radius=2.0)
            extrude(amount=1.8)
            with Locations((0, 0, 1.8)):
                with BuildSketch():
                    Circle(radius=1.1)
                extrude(amount=0.3)

            # 8-Pointed Star Rays
            for i in range(8):
                ang = i * (360.0 / 8)
                with Locations(Rotation(0, 0, ang)):
                    with Locations((5.6, 0)):
                        with BuildSketch():
                            Rectangle(3.2, 0.8)
                        extrude(amount=1.4)

        # 5. Right Bay: Mana Crystal Cluster (center at X = 16.0, width 15.5 -> left edge at 8.25)
        with Locations((16.0, 0, 4.6)):
            with BuildSketch() as s_cwell:
                Rectangle(15.5, 17.0)
                fillet(s_cwell.vertices(), radius=1.6)
            extrude(amount=-2.0, mode=Mode.SUBTRACT)

        crystals = [
            (2.5, 0.0, 2.6, 1.6, 0.9),    # Tallest Alpha Crystal
            (-2.5, 4.2, 2.0, 1.3, 0.7),   # Upper crystal
            (-2.5, -4.2, 2.0, 1.3, 0.7),  # Lower crystal
            (2.0, 4.8, 1.7, 1.1, 0.6),    # Top-right crystal
            (2.0, -4.8, 1.7, 1.1, 0.6),   # Bottom-right crystal
            (-4.2, 0.0, 1.8, 1.2, 0.6),   # Inner-left crystal
            (4.5, 0.0, 1.5, 1.0, 0.5),    # Outer-right crystal
        ]
        for dx, dy, br, ph, th in crystals:
            with Locations((16.0 + dx, dy, 2.6)):
                with BuildSketch():
                    RegularPolygon(radius=br, side_count=6)
                extrude(amount=ph)
                with Locations((0, 0, ph)):
                    with BuildSketch():
                        RegularPolygon(radius=br * 0.55, side_count=6)
                    extrude(amount=th)

        # 6. Central Heraldic Crest: Shield with "HPC&A" (from X = -5.2 to +5.2 -> zero overlap)
        with Locations((0, 0, 4.6)):
            with BuildSketch() as s_shield:
                pts = [(-5.2, 6.0), (5.2, 6.0), (5.2, -1.0), (0.0, -6.5), (-5.2, -1.0)]
                Polygon(pts)
                fillet(s_shield.vertices(), radius=1.0)
            extrude(amount=0.5)

            with Locations((0, 0.2, 0.5)):
                with BuildSketch():
                    Text("HPC&A", font_size=2.8, font_style=FontStyle.BOLD)
                extrude(amount=0.5)

        # 7. Ancient Mana Inscription Glyphs on Frame
        for rx in [-22.0, 22.0]:
            for ry in [8.0, -8.0]:
                with Locations((rx, ry, 4.6)):
                    with BuildSketch():
                        Rectangle(1.4, 1.4)
                    extrude(amount=-0.35, mode=Mode.SUBTRACT)

    return rune.part


# ==============================================================================
# MAIN EXPORT ROUTINE
# ==============================================================================
def main():
    print("=================================================================")
    print("Generating All 3 Fantasy GPU Keychain Models...")
    print("=================================================================")

    models = [
        ("gpu_fantasy_chibi", build_chibi_gpu),
        ("gpu_fantasy_mecha", build_mecha_gpu),
        ("gpu_fantasy_rune", build_rune_gpu),
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
        print(f"  Dimensions: {bbox[0]:.2f} x {bbox[1]:.2f} x {bbox[2]:.2f} mm")
        print(f"  Solid Volume: {vol_cm3:.2f} cm3 (~{vol_cm3 * 1.24 * 0.75:.1f} g at 15% infill)")

    print("\nAll 3 Fantasy GPU Models exported successfully!")


if __name__ == "__main__":
    main()
