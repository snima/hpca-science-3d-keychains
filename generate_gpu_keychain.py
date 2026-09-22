"""
HPC&A Edition GPU Keychain Generator
3D-Printable High-Performance Graphics Card Miniature Keychain
Author: Mechanical & CAD Design Engineer
System: build123d (OpenCASCADE parametric CAD)

Unified monolithic graphics card body:
- No secondary underlayer / baseplate pedestal
- Pure graphics card form factor with integrated I/O bracket and PCIe port
- 100% support-free FDM 3D printing
- Custom HPC&A research group branding (Zero proprietary trademarks)
"""

import os
import shutil
import numpy as np
import trimesh
from build123d import *

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "output"))
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==============================================================================
# PARAMETRIC DIMENSIONS (All values in millimeters)
# ==============================================================================
# Main Card Body
CARD_LENGTH = 56.0           # Main card body length (X)
CARD_WIDTH = 25.0            # Main card body width (Y)
CARD_THICKNESS = 4.6         # Shroud body height (Z)

# Keyring Eyelet on I/O Bracket
EYELET_X = -CARD_LENGTH / 2.0 - 3.5  # -31.5 mm
EYELET_Y = 4.0                       # Keyring eyelet Y offset
EYELET_OUTER_R = 5.2                 # Outer radius (Ø10.4 mm)
EYELET_HOLE_R = 2.3                  # Inner hole radius (Ø4.6 mm, 2.9 mm solid rim)

# PCIe Interface Tab
PCIE_LENGTH = 28.0           # Gold finger strip length
PCIE_PROTRUSION = 2.3        # Protruding width below card edge
PCIE_THICKNESS = 2.0         # PCB tab thickness (Z)
PCIE_NOTCH_X = -6.0          # Keying notch position
PCIE_NOTCH_W = 1.6           # Notch width

# Cooling Chambers (Front face at Z = CARD_THICKNESS)
FAN_CENTER_X = -13.0         # Left bay: Fan center
FAN_RADIUS = 9.8             # Fan well radius (Ø19.6 mm)
FAN_WELL_DEPTH = 2.0         # Cut down to Z = 2.6 mm
FAN_HUB_R = 3.5              # Impeller hub radius (Ø7.0 mm)
FAN_BLADE_COUNT = 11         # 11 aerodynamic swept blades

FIN_BAY_CENTER_X = 13.0      # Right bay: Heatsink & Badge center
FIN_BAY_W = 19.5             # Fin bay cutout width
FIN_BAY_H = 18.0             # Fin bay cutout height
FIN_BAY_DEPTH = 1.8          # Cut down to Z = 2.8 mm

# Badge & Branding
BADGE_W = 16.5               # "HPC&A" Plaque width
BADGE_H = 8.2                # "HPC&A" Plaque height
BADGE_TOP_Z = 4.8            # Plaque top Z
TEXT_SERIES = "HPC&A"        # Main series badge
TEXT_SPINE = "HPC&A EDITION" # Spine branding (No proprietary trademarks)
TEXT_RELIEF = 0.6            # Embossed text relief


def build_gpu_keychain_model() -> Part:
    """Builds the unified 3D-printable HPC&A Edition GPU Keychain solid body."""
    with BuildPart() as gpu:
        # ======================================================================
        # 1. UNIFIED CARD BODY & INTEGRATED I/O BRACKET KEYRING EYELET
        # ======================================================================
        with BuildSketch() as s_body:
            # Main card body rounded rectangle
            Rectangle(CARD_LENGTH, CARD_WIDTH)
            fillet(s_body.vertices(), radius=2.2)
            
            # Left I/O bracket tab with reinforced keyring eyelet
            with Locations((EYELET_X, EYELET_Y)):
                Circle(radius=EYELET_OUTER_R)
                Circle(radius=EYELET_HOLE_R, mode=Mode.SUBTRACT)
        extrude(amount=CARD_THICKNESS)

        # ======================================================================
        # 1B. UNDERSIDE ATTRIBUTION INSCRIPTION (Debossed at Z = 0)
        # Mirrored about YZ so it reads correctly from below (-Z view).
        # ======================================================================
        with Locations((0, 0, 0)):
            with BuildSketch() as s_bottom:
                with Locations((0, 3.5)):
                    Text("HPC&A EDITION", font_size=2.6, font_style=FontStyle.BOLD)
                with Locations((0, -3.5)):
                    Text("DESIGNED BY NIMA", font_size=2.4, font_style=FontStyle.BOLD)
                mirror(about=Plane.YZ, mode=Mode.REPLACE)
            extrude(amount=0.35, mode=Mode.SUBTRACT)

        # ======================================================================
        # 2. PCIe CONNECTOR TAB (Protrudes directly from card bottom edge)
        # ======================================================================
        with BuildSketch() as s_pcie:
            with Locations((-2.0, -CARD_WIDTH / 2.0 - PCIE_PROTRUSION / 2.0)):
                Rectangle(PCIE_LENGTH, PCIE_PROTRUSION)
                # Polarization keying notch
                with Locations((PCIE_NOTCH_X, 0)):
                    Rectangle(PCIE_NOTCH_W, 3.0, mode=Mode.SUBTRACT)
        extrude(amount=PCIE_THICKNESS)

        # Debossed gold finger contact lines on PCIe tab (0.35 mm depth)
        for px in np.linspace(-14.5, 10.5, 16):
            if abs(px - PCIE_NOTCH_X) > 1.8:
                with Locations((px, -CARD_WIDTH / 2.0 - PCIE_PROTRUSION / 2.0, PCIE_THICKNESS)):
                    with BuildSketch():
                        Rectangle(0.5, 1.7)
                    extrude(amount=-0.35, mode=Mode.SUBTRACT)

        # ======================================================================
        # 3. I/O BRACKET DISPLAY PORTS (DisplayPort & HDMI slots debossed)
        # ======================================================================
        for dy in [-2.0, 1.0, 4.0]:
            with Locations((-CARD_LENGTH / 2.0 - 1.0, dy, CARD_THICKNESS)):
                with BuildSketch():
                    Rectangle(1.2, 2.0)
                extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # ======================================================================
        # 4. COOLING BAYS CARVED INTO SHROUD FACE
        # ======================================================================
        # Left Bay: Axial cooling fan well
        with Locations((FAN_CENTER_X, 0, CARD_THICKNESS)):
            with BuildSketch():
                Circle(radius=FAN_RADIUS)
            extrude(amount=-FAN_WELL_DEPTH, mode=Mode.SUBTRACT)

        # Right Bay: Heatsink pass-through fin well
        with Locations((FIN_BAY_CENTER_X, 0, CARD_THICKNESS)):
            with BuildSketch() as s_fin_well:
                Rectangle(FIN_BAY_W, FIN_BAY_H)
                fillet(s_fin_well.vertices(), radius=1.6)
            extrude(amount=-FIN_BAY_DEPTH, mode=Mode.SUBTRACT)

        # ======================================================================
        # 5. FAN INTERIOR DETAILS (Built from well floor at Z = 2.6 mm)
        # ======================================================================
        fan_floor_z = CARD_THICKNESS - FAN_WELL_DEPTH  # 2.6 mm
        with Locations((FAN_CENTER_X, 0, fan_floor_z)):
            # Impeller central hub (reaches Z = 4.2 mm)
            with BuildSketch():
                Circle(radius=FAN_HUB_R)
            extrude(amount=1.6)
            
            # Hub center metallic dome
            with Locations((0, 0, 1.6)):
                with BuildSketch():
                    Circle(radius=1.6)
                extrude(amount=0.3)

            # 11 Aerodynamic swept turbine blades (reaches Z = 4.0 mm)
            for b_idx in range(FAN_BLADE_COUNT):
                b_ang = b_idx * (360.0 / FAN_BLADE_COUNT)
                with Locations(Rotation(0, 0, b_ang)):
                    with Locations((6.2, 0), Rotation(0, 0, 25)):
                        with BuildSketch():
                            Rectangle(4.6, 1.2)
                        extrude(amount=1.4)

        # ======================================================================
        # 6. HEATSINK FINS & "HPC&A" PLAQUE (Built from well floor at Z = 2.8 mm)
        # ======================================================================
        fin_floor_z = CARD_THICKNESS - FIN_BAY_DEPTH  # 2.8 mm
        
        # 9 Vertical heatsink fin channels
        for fx in np.linspace(4.5, 21.5, 9):
            with Locations((fx, 0, fin_floor_z)):
                with BuildSketch():
                    Rectangle(1.0, 16.8)
                extrude(amount=1.3)

        # Elevated "HPC&A" Plaque (reaches Z = 4.8 mm)
        plaque_height = BADGE_TOP_Z - fin_floor_z  # 2.0 mm
        with Locations((FIN_BAY_CENTER_X, 0, fin_floor_z)):
            with BuildSketch() as s_badge:
                Rectangle(BADGE_W, BADGE_H)
                fillet(s_badge.vertices(), radius=1.2)
            extrude(amount=plaque_height)

            # Raised Bold "HPC&A" Text (reaches Z = 5.4 mm)
            with Locations((0, 0, plaque_height)):
                with BuildSketch():
                    Text(TEXT_SERIES, font_size=3.8, font_style=FontStyle.BOLD)
                extrude(amount=TEXT_RELIEF)

        # ======================================================================
        # 7. TOP SPINE: "HPC&A EDITION" EMBOSSED BRANDING
        # ======================================================================
        with Locations((0, 10.4, CARD_THICKNESS)):
            with BuildSketch():
                Text(TEXT_SPINE, font_size=2.2, font_style=FontStyle.BOLD)
            extrude(amount=TEXT_RELIEF)

    return gpu.part


def main():
    print("=================================================================")
    print("Generating Unified HPC&A Edition GPU Keychain CAD Model...")
    print("=================================================================")

    part = build_gpu_keychain_model()

    stl_path = os.path.join(OUTPUT_DIR, "gpu_keychain_hpca.stl")
    step_path = os.path.join(OUTPUT_DIR, "gpu_keychain_hpca.step")
    source_path = os.path.join(OUTPUT_DIR, "gpu_keychain_model.py")

    # Export STL
    print("Exporting STL mesh (tolerance=0.005, angular_tolerance=0.1)...")
    export_stl(part, stl_path, tolerance=0.005, angular_tolerance=0.1)

    # Export STEP
    print("Exporting STEP CAD model...")
    export_step(part, step_path)

    # Self-copy source to output
    shutil.copy(__file__, source_path)
    print(f"Source saved to: {source_path}")

    # Geometry verification
    mesh = trimesh.load(stl_path)
    print(f"STL File: {stl_path} ({os.path.getsize(stl_path) / 1024:.1f} KB)")
    print(f"STEP File: {step_path} ({os.path.getsize(step_path) / 1024:.1f} KB)")
    print(f"Mesh Watertight: {mesh.is_watertight}")
    print(f"Triangle Count: {len(mesh.faces):,}")
    print(f"Vertex Count: {len(mesh.vertices):,}")
    bbox = mesh.bounding_box.extents
    print(f"Bounding Envelope: {bbox[0]:.2f} x {bbox[1]:.2f} x {bbox[2]:.2f} mm")
    print(f"Volume: {mesh.volume / 1000.0:.2f} cm3")


if __name__ == "__main__":
    main()
