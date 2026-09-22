#!/usr/bin/env python3
"""
HPC&A Fantasy CPU Keychain Generator — HETERO / REALISTIC EDITION
=================================================================
A fantasy processor package that reads like a real CPU: square substrate
with Pin-1 chamfer, stubby socket pin teeth, SMD capacitor blocks, a
nickel-style heat spreader (IHS) with laser-etched branding, and an
exposed silicon die with a realistic heterogeneous floorplan — 2 big
P-cores (strong), a 4-way E-core cluster (weak, shared cache style),
L3 cache strips and engraved interconnect streets.

Engineered for 100% support-free FDM 3D printing (flat bed at Z=0).
Author: Mechanical & CAD Design Engineer
System: build123d (OpenCASCADE)
"""

import os
import trimesh
from build123d import *

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "output"))
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==============================================================================
# PARAMETRIC DIMENSIONS (mm)
# ==============================================================================
BODY = 44.0                 # Square substrate edge
BODY_T = 3.4                # Substrate thickness (Z: 0 -> 3.4) - slim edition
CORNER_R = 3.0              # Fillet on 3 corners
PIN1_CHAMFER = 4.5          # Chamfer on Pin-1 corner (-X, -Y)

EYELET_XY = -BODY / 2.0     # Corner eyelet center (top-left corner)
EYELET_OUTER_R = 5.2
EYELET_HOLE_R = 2.3         # Ø4.6 mm through-hole

# Stubby socket pin teeth on left/right edges
TEETH_PROTRUSION = 2.0      # Outward extent beyond body edge
TEETH_W = 3.0               # Tooth width along edge
TEETH_T = 2.2               # Tooth thickness (Z: 0 -> 2.2)
TEETH_YS = [-12.0, -6.0, 0.0, 6.0, 12.0]

# Pin-1 marker dot (top face)
PIN1_R = 1.2
PIN1_H = 0.5
PIN1_XY = -17.0

# SMD capacitor blocks around the IHS (like a real package)
CAP_L = 3.6
CAP_W = 1.8
CAP_H = 1.2                 # Z: body-top -> +1.2
CAP_R = 0.4
# (x, y, rotation_deg): top row, left column, right column
CAPS = [
    (-8.0, 19.5, 0), (8.0, 19.5, 0),
    (-19.5, 8.0, 90), (-19.5, -8.0, 90),
    (19.5, 8.0, 90), (19.5, -8.0, 90),
]

# Nickel-style heat spreader (IHS)
IHS = 34.0                  # IHS edge
IHS_H = 1.0                 # Z: body-top -> +1.0
IHS_R = 2.0

# Laser-etched branding on the IHS top ring (debossed)
ETCH_DEPTH = 0.35
ETCH_BRAND = "HPC&A"
ETCH_BRAND_FS = 2.4
ETCH_BRAND_Y = 11.5
ETCH_SUB = "HETERO"
ETCH_SUB_FS = 2.0
ETCH_SUB_Y = 8.5

# Exposed silicon die (delidded look), shifted down for the etched text
DIE_W = 24.0
DIE_H = 16.0
DIE_CY = -2.0               # Die center Y
DIE_T = 0.7                 # Z: 5.6 -> 6.3
DIE_R = 1.0

# Floorplan blocks (raised 0.5 above die, 1.0 streets between)
BLOCK_H = 0.5               # Z: 6.3 -> 6.8
LABEL_H = 0.3               # Embossed labels (Z: 6.8 -> 7.1)
# 2 big P-cores (die-local coords, die center = 0,0)
P_BLOCKS = [                # (cx, cy, w, h, label)
    (-7.5, 0.0, 6.4, 10.0, "P0"),
    (0.0, 0.0, 6.4, 10.0, "P1"),
]
P_LABEL_FS = 2.0
# 4-way E-core cluster (die-local): 2 cols x 2 rows sharing one island
E_BLOCKS = [                # (cx, cy)
    (5.7, 2.65), (9.55, 2.65),
    (5.7, -2.65), (9.55, -2.65),
]
E_W = 2.9
E_H = 4.7
E_LABEL_FS = 1.6
# L3 cache strips (die-local, full width bars)
L3_BARS = [6.8, -6.8]       # center Y
L3_W = 22.0
L3_H = 1.2

# "P+E CORES" nameplate on substrate bottom margin (top face)
PLATE_W = 20.0
PLATE_H = 3.5
PLATE_Y = -19.75
PLATE_T = 0.4               # Z: body-top -> +0.4
PLATE_TEXT = "P+E CORES"
PLATE_FS = 2.6
PLATE_RELIEF = 0.5          # Z: 5.0 -> 5.5


def build_fantasy_cpu(bottom_extra: str | None = None, coarse: bool = False) -> Part:
    """Builds the 3D-printable Hetero Fantasy CPU Keychain (weak + strong cores).

    Args:
        bottom_extra: Optional extra line on the underside (e.g. "PRINTED AT ...").
    """
    with BuildPart() as cpu:
        # ------------------------------------------------------------------
        # 1. Square substrate + Pin-1 chamfer + corner keyring eyelet
        # ------------------------------------------------------------------
        with BuildSketch() as s_base:
            Rectangle(BODY, BODY)
            v_all = s_base.vertices().sort_by(lambda v: (v.X, v.Y))
            # Fillet 3 safe corners
            v_fillet = v_all.filter_by(lambda v: not (v.X < 0 and v.Y < 0))
            fillet(v_fillet, radius=CORNER_R)
            # Chamfer Pin-1 corner (orientation indicator)
            v_chamf = v_all.filter_by(lambda v: v.X < 0 and v.Y < 0)
            chamfer(v_chamf, length=PIN1_CHAMFER)
            # Corner eyelet merged into top-left corner
            with Locations((EYELET_XY, -EYELET_XY)):
                Circle(radius=EYELET_OUTER_R)
                Circle(radius=EYELET_HOLE_R, mode=Mode.SUBTRACT)
        extrude(amount=BODY_T)

        # ------------------------------------------------------------------
        # 1B. Underside inscription (Z = 0) - mirrored for -Z readability
        # ------------------------------------------------------------------
        if coarse:  # Sergio / 0.6 mm nozzle: XL text, deeper cut
            bottom_lines = [
                (7.0, "HETERO CPU", 3.2),
                (0.0, "DESIGNED BY NIMA", 3.0),
                (-7.0, bottom_extra, 2.8),
            ]
            _cut = 0.6
        elif bottom_extra is None:
            bottom_lines = [
                (3.5, "HETERO CPU", 2.4),
                (-3.5, "DESIGNED BY NIMA", 2.2),
            ]
            _cut = 0.35
        else:  # FabLab edition: 3 lines
            bottom_lines = [
                (6.0, "HETERO CPU", 2.4),
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

        # ------------------------------------------------------------------
        # 2. Stubby socket pin teeth on left/right edges (Z: 0 -> 2.2)
        # ------------------------------------------------------------------
        for ty in TEETH_YS:
            for sx in [-1, 1]:
                with Locations((sx * (BODY / 2.0 + TEETH_PROTRUSION / 2.0), ty, 0)):
                    with BuildSketch() as s_tooth:
                        Rectangle(TEETH_PROTRUSION, TEETH_W)
                        fillet(s_tooth.vertices(), radius=0.5)
                    extrude(amount=TEETH_T)

        # ------------------------------------------------------------------
        # 3. Pin-1 marker dot (on body top)
        # ------------------------------------------------------------------
        with Locations((PIN1_XY, PIN1_XY, BODY_T)):
            with BuildSketch():
                Circle(radius=PIN1_R)
            extrude(amount=PIN1_H)

        # ------------------------------------------------------------------
        # 4. SMD capacitor blocks around the IHS (on body top)
        # ------------------------------------------------------------------
        for cx, cy, crot in CAPS:
            with Locations((cx, cy, BODY_T)):
                with BuildSketch() as s_cap:
                    with Locations(Rotation(0, 0, crot)):
                        Rectangle(CAP_L, CAP_W)
                        fillet(s_cap.vertices(), radius=CAP_R)
                extrude(amount=CAP_H)

        # ------------------------------------------------------------------
        # 5. "P+E CORES" nameplate on bottom margin (on body top)
        # ------------------------------------------------------------------
        with Locations((0, PLATE_Y, BODY_T)):
            with BuildSketch() as s_plate:
                Rectangle(PLATE_W, PLATE_H)
                fillet(s_plate.vertices(), radius=1.0)
            extrude(amount=PLATE_T)
            with Locations((0, 0, PLATE_T)):
                with BuildSketch():
                    Text(PLATE_TEXT, font_size=PLATE_FS, font_style=FontStyle.BOLD)
                extrude(amount=PLATE_RELIEF)

        # ------------------------------------------------------------------
        # 6. Heat spreader / IHS (on body top)
        # ------------------------------------------------------------------
        with Locations((0, 0, BODY_T)):
            with BuildSketch() as s_ihs:
                Rectangle(IHS, IHS)
                fillet(s_ihs.vertices(), radius=IHS_R)
            extrude(amount=IHS_H)

        # ------------------------------------------------------------------
        # 6B. Laser-etched branding on the IHS top ring (debossed)
        # ------------------------------------------------------------------
        with Locations((0, ETCH_BRAND_Y, BODY_T + IHS_H)):
            with BuildSketch():
                Text(ETCH_BRAND, font_size=ETCH_BRAND_FS, font_style=FontStyle.BOLD)
            extrude(amount=-ETCH_DEPTH, mode=Mode.SUBTRACT)
        with Locations((0, ETCH_SUB_Y, BODY_T + IHS_H)):
            with BuildSketch():
                Text(ETCH_SUB, font_size=ETCH_SUB_FS, font_style=FontStyle.BOLD)
            extrude(amount=-ETCH_DEPTH, mode=Mode.SUBTRACT)

        # ------------------------------------------------------------------
        # 7. Exposed silicon die with heterogeneous floorplan (Z: 5.6 -> 6.3)
        # ------------------------------------------------------------------
        with Locations((0, DIE_CY, BODY_T + IHS_H)):
            with BuildSketch() as s_die:
                Rectangle(DIE_W, DIE_H)
                fillet(s_die.vertices(), radius=DIE_R)
            extrude(amount=DIE_T)

        z_blk = BODY_T + IHS_H + DIE_T  # 6.3: block base plane
        # 7a. 2 big P-cores with labels
        for cx, cy, w, h, label in P_BLOCKS:
            with Locations((cx, DIE_CY + cy, z_blk)):
                with BuildSketch():
                    Rectangle(w, h)
                extrude(amount=BLOCK_H)
                with Locations((0, 0, BLOCK_H)):
                    with BuildSketch():
                        Text(label, font_size=P_LABEL_FS, font_style=FontStyle.BOLD)
                    extrude(amount=LABEL_H)
        # 7b. 4-way E-core cluster with labels
        for cx, cy in E_BLOCKS:
            with Locations((cx, DIE_CY + cy, z_blk)):
                with BuildSketch():
                    Rectangle(E_W, E_H)
                extrude(amount=BLOCK_H)
                with Locations((0, 0, BLOCK_H)):
                    with BuildSketch():
                        Text("E", font_size=E_LABEL_FS, font_style=FontStyle.BOLD)
                    extrude(amount=LABEL_H)
        # 7c. L3 cache strips (full-width bars, no labels)
        for ly in L3_BARS:
            with Locations((0, DIE_CY + ly, z_blk)):
                with BuildSketch():
                    Rectangle(L3_W, L3_H)
                extrude(amount=BLOCK_H)

    return cpu.part


def main():
    print("=================================================================")
    print("Generating Hetero Fantasy CPU Keychain (realistic P+E floorplan)...")
    print("=================================================================")

    part = build_fantasy_cpu()

    stl_path = os.path.join(OUTPUT_DIR, "cpu_fantasy_chibi.stl")
    step_path = os.path.join(OUTPUT_DIR, "cpu_fantasy_chibi.step")

    export_stl(part, stl_path, tolerance=0.005, angular_tolerance=0.1)
    export_step(part, step_path)

    mesh = trimesh.load(stl_path)
    bbox = mesh.bounding_box.extents
    vol_cm3 = mesh.volume / 1000.0
    print(f"  Watertight: {mesh.is_watertight}")
    print(f"  Dimensions: {bbox[0]:.2f} x {bbox[1]:.2f} x {bbox[2]:.2f} mm")
    print(f"  Solid Volume: {vol_cm3:.2f} cm3 (~{vol_cm3 * 1.24:.1f} g PLA)")
    print("Fantasy CPU exported successfully!")


if __name__ == "__main__":
    main()
