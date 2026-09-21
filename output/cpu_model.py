"""
CPU Educational Souvenir Model Generator
Science Night Outreach 3D Print Design
Author: Mechanical & CAD Design Engineer
System: build123d (OpenCASCADE parametric CAD)
"""

import math
import os
import numpy as np
import trimesh
from build123d import *

# ==============================================================================
# PARAMETRIC DESIGN CONSTANTS (All dimensions in millimeters)
# ==============================================================================

# 1. PCB Substrate (Package Base)
SUBSTRATE_WIDTH = 50.0          # X dimension (mm)
SUBSTRATE_LENGTH = 50.0         # Y dimension (mm)
SUBSTRATE_THICKNESS = 3.0       # Z dimension (mm) - solid base for durability
CORNER_FILLET_RADIUS = 3.0      # Corner radius on 3 corners
PIN1_CHAMFER_LENGTH = 4.5       # Chamfer on Pin-1 corner (orientation indicator)

# Edge Castellations (Perimeter Gold Finger Notches)
NOTCH_WIDTH = 2.0               # Notch width along perimeter
NOTCH_DEPTH = 1.6               # Notch recess inward
NOTCH_HEIGHT = 3.0              # Notch height (full substrate depth)
NOTCH_OFFSETS = [-14.0, -7.0, 7.0, 14.0]

# Pin 1 Visual/Tactile Marker
PIN1_DOT_RADIUS = 1.2           # Tactile alignment marker
PIN1_DOT_HEIGHT = 0.5           # Raised relief
PIN1_DOT_OFFSET = -20.5         # X, Y position near chamfered corner

# Underside LGA (Land Grid Array) Contacts
LGA_GRID_PITCH = 6.0            # Center-to-center spacing
LGA_PAD_SIZE = 2.4              # Width/length of each recessed pad
LGA_RECESS_DEPTH = 0.35         # Recess into bottom face (approx 2 layers)
LGA_OFFSETS = [-15.0, -9.0, -3.0, 3.0, 9.0, 15.0]

# 2. Integrated Heat Spreader (IHS) & Silicon Die
IHS_SIZE = 28.0                 # Width and length of heat spreader
IHS_HEIGHT = 2.6                # Height above substrate (Z: 3.0 -> 5.6 mm)
IHS_CORNER_RADIUS = 2.5         # Beveled corner radius

DIE_SIZE = 24.0                 # Silicon core plateau width/length
DIE_HEIGHT = 0.8                # Height above IHS (Z: 5.6 -> 6.4 mm)
DIE_CORNER_RADIUS = 1.5         # Core corner radius

# 3. Decoupling Capacitors (SMD Blocks)
CAP_LENGTH = 3.6                # Length of capacitor brick
CAP_WIDTH = 1.8                 # Width of capacitor brick
CAP_HEIGHT = 1.2                # Height of capacitor brick (Z: 3.0 -> 4.2 mm)
CAP_CORNER_RADIUS = 0.4         # Fillet on capacitor edges
CAP_OFFSET_CENTER = 17.0        # Distance from chip center to capacitor banks
CAP_OFFSET_PAIR = 6.5           # Spacing between paired capacitors

# 4. Educational Circuit Bus & Vias
VIA_OUTER_RADIUS = 1.4          # Outer copper pad radius
VIA_INNER_RADIUS = 0.6          # Center drill hole recess
VIA_POSITIONS = [(-19.5, 19.5), (19.5, 19.5), (19.5, -19.5)]
TRACE_THICKNESS = 0.5           # Raised height on substrate (Z: 3.0 -> 3.5 mm)

# 5. Active Cooling Architecture (Heatsink & Turbine)
HUB_RADIUS = 6.0                # Central solid hub core radius (Ø12.0 mm)
HUB_TOTAL_HEIGHT = 6.4          # Hub height from die (Z: 6.4 -> 12.8 mm)

SHROUD_OUTER_RADIUS = 11.5      # Fan shroud outer radius (Ø23.0 mm)
SHROUD_INNER_RADIUS = 9.7       # Fan shroud inner radius (Ø19.4 mm)
SHROUD_HEIGHT = 5.0             # Shroud height (Z: 6.4 -> 11.4 mm)

FIN_COUNT = 12                  # 12 aerodynamic radial heatsink fins
FIN_THICKNESS = 1.6             # Solid fin thickness (exceeds 1.5mm min)
FIN_RADIAL_SPAN = 4.2           # Radial fin length (r=6.0 to r=10.2 mm)
FIN_HEIGHT = 5.8                # Fin height (Z: 6.4 -> 12.2 mm)

# 6. Hub Bezel & "CPU" Crest
BEZEL_OUTER_RADIUS = 6.0        # Outer bezel rim radius
BEZEL_INNER_RADIUS = 5.2        # Inner bezel rim radius
BEZEL_HEIGHT = 0.4              # Bezel relief height (Z: 12.8 -> 13.2 mm)

TEXT_LABEL = "CPU"              # Bold central embossed badge
TEXT_FONT_SIZE = 4.4            # Bold typography scale
TEXT_RELIEF_HEIGHT = 0.8        # Relief height (4 layers at 0.2mm, Z: 12.8 -> 13.6 mm)


def build_cpu_model() -> Part:
    """Procedurally generates the CPU Educational Souvenir 3D model."""
    with BuildPart() as cpu:
        # ======================================================================
        # 1. BASE SUBSTRATE (PCB PACKAGE)
        # ======================================================================
        with BuildSketch() as s_base:
            Rectangle(SUBSTRATE_WIDTH, SUBSTRATE_LENGTH)
            v_all = s_base.vertices().sort_by(lambda v: (v.X, v.Y))
            
            # Fillet 3 safe corners for tactile comfort
            v_fillet = v_all.filter_by(lambda v: not (v.X < 0 and v.Y < 0))
            fillet(v_fillet, radius=CORNER_FILLET_RADIUS)
            
            # Chamfer Pin-1 corner (orientation indicator)
            v_chamf = v_all.filter_by(lambda v: v.X < 0 and v.Y < 0)
            chamfer(v_chamf, length=PIN1_CHAMFER_LENGTH)
        extrude(amount=SUBSTRATE_THICKNESS)

        # 1b. Edge Castellations (Perimeter gold finger contact notches)
        for offset in NOTCH_OFFSETS:
            with Locations((offset, SUBSTRATE_LENGTH / 2.0, SUBSTRATE_THICKNESS / 2.0),
                           (offset, -SUBSTRATE_LENGTH / 2.0, SUBSTRATE_THICKNESS / 2.0)):
                Box(NOTCH_WIDTH, NOTCH_DEPTH, NOTCH_HEIGHT, mode=Mode.SUBTRACT)
            with Locations((SUBSTRATE_WIDTH / 2.0, offset, SUBSTRATE_THICKNESS / 2.0),
                           (-SUBSTRATE_WIDTH / 2.0, offset, SUBSTRATE_THICKNESS / 2.0)):
                Box(NOTCH_DEPTH, NOTCH_WIDTH, NOTCH_HEIGHT, mode=Mode.SUBTRACT)

        # 1c. Pin-1 Alignment Marker Dot
        with Locations((PIN1_DOT_OFFSET, PIN1_DOT_OFFSET, SUBSTRATE_THICKNESS)):
            with BuildSketch():
                Circle(radius=PIN1_DOT_RADIUS)
            extrude(amount=PIN1_DOT_HEIGHT)

        # 1d. Underside Land Grid Array (LGA) Pad Recesses
        # Recessed 0.35 mm into the flat bottom; maintains >82% direct bed contact
        for px in LGA_OFFSETS:
            for py in LGA_OFFSETS:
                if abs(px) <= 3.0 and abs(py) <= 3.0:
                    continue  # Central keep-out cavity (socket design convention)
                with Locations((px, py, LGA_RECESS_DEPTH / 2.0)):
                    Box(LGA_PAD_SIZE, LGA_PAD_SIZE, LGA_RECESS_DEPTH, mode=Mode.SUBTRACT)

        # ======================================================================
        # 2. INTEGRATED HEAT SPREADER (IHS) & SILICON DIE
        # ======================================================================
        # 2a. Heat Spreader (Z: 3.0 -> 5.6 mm)
        with Locations((0, 0, SUBSTRATE_THICKNESS)):
            with BuildSketch() as s_ihs:
                Rectangle(IHS_SIZE, IHS_SIZE)
                fillet(s_ihs.vertices(), radius=IHS_CORNER_RADIUS)
            extrude(amount=IHS_HEIGHT)

        # 2b. Stepped Silicon Core Plateau (Z: 5.6 -> 6.4 mm)
        with Locations((0, 0, SUBSTRATE_THICKNESS + IHS_HEIGHT)):
            with BuildSketch() as s_die:
                Rectangle(DIE_SIZE, DIE_SIZE)
                fillet(s_die.vertices(), radius=DIE_CORNER_RADIUS)
            extrude(amount=DIE_HEIGHT)

        # ======================================================================
        # 3. SURFACE-MOUNT DECOUPLING CAPACITORS
        # ======================================================================
        cap_positions = [
            (-CAP_OFFSET_PAIR, CAP_OFFSET_CENTER, 0),
            (CAP_OFFSET_PAIR, CAP_OFFSET_CENTER, 0),
            (-CAP_OFFSET_PAIR, -CAP_OFFSET_CENTER, 0),
            (CAP_OFFSET_PAIR, -CAP_OFFSET_CENTER, 0),
            (-CAP_OFFSET_CENTER, -CAP_OFFSET_PAIR, 90),
            (-CAP_OFFSET_CENTER, CAP_OFFSET_PAIR, 90),
            (CAP_OFFSET_CENTER, -CAP_OFFSET_PAIR, 90),
            (CAP_OFFSET_CENTER, CAP_OFFSET_PAIR, 90),
        ]
        for cx, cy, crot in cap_positions:
            with Locations((cx, cy, SUBSTRATE_THICKNESS)):
                with BuildSketch() as s_cap:
                    with Locations(Rotation(0, 0, crot)):
                        Rectangle(CAP_LENGTH, CAP_WIDTH)
                        fillet(s_cap.vertices(), radius=CAP_CORNER_RADIUS)
                extrude(amount=CAP_HEIGHT)

        # ======================================================================
        # 4. EDUCATIONAL CIRCUIT BUS TRACES & BINARY TRACK
        # ======================================================================
        with Locations((0, 0, SUBSTRATE_THICKNESS)):
            with BuildSketch() as s_tr:
                # Corner test pads / vias
                for vx, vy in VIA_POSITIONS:
                    with Locations((vx, vy)):
                        Circle(radius=VIA_OUTER_RADIUS)
                        Circle(radius=VIA_INNER_RADIUS, mode=Mode.SUBTRACT)
                
                # 45-degree bus tracks radiating to corners
                for angle in [45, 135, -45]:
                    with Locations(Rotation(0, 0, angle)):
                        with Locations((19.5, 0)):
                            Rectangle(6.5, 1.2)
                        with Locations((17.0, 2.5)):
                            Rectangle(4.5, 1.0)
                        with Locations((17.0, -2.5)):
                            Rectangle(4.5, 1.0)

                # 8-bit binary data track along north margin:
                # ASCII 'C' = 01000011 (binary educational element)
                binary_bits = [0, 1, 0, 0, 0, 0, 1, 1]
                for i, bit in enumerate(binary_bits):
                    bx = -14.0 + i * 4.0
                    by = 21.8
                    if bit == 1:
                        with Locations((bx, by)):
                            Circle(radius=1.0)
                    else:
                        with Locations((bx, by)):
                            Circle(radius=0.4)
            extrude(amount=TRACE_THICKNESS)

        # ======================================================================
        # 5. COOLING ARCHITECTURE (HEATSINK & TURBINE FAN)
        # ======================================================================
        z_cooler_base = SUBSTRATE_THICKNESS + IHS_HEIGHT + DIE_HEIGHT  # 6.4 mm

        # 5a. Central solid hub core column (Z: 6.4 -> 12.8 mm)
        with Locations((0, 0, z_cooler_base)):
            with BuildSketch():
                Circle(radius=HUB_RADIUS)
            extrude(amount=HUB_TOTAL_HEIGHT)

            # 5b. Outer heatsink shroud ring (Z: 6.4 -> 11.4 mm)
            with BuildSketch() as s_ring:
                Circle(radius=SHROUD_OUTER_RADIUS)
                Circle(radius=SHROUD_INNER_RADIUS, mode=Mode.SUBTRACT)
            extrude(amount=SHROUD_HEIGHT)

            # 5c. 12 Aerodynamic radial heatsink fins / turbine vanes (Z: 6.4 -> 12.2 mm)
            fin_center_radius = (HUB_RADIUS + SHROUD_INNER_RADIUS) / 2.0  # 7.85 mm
            for fin_idx in range(FIN_COUNT):
                fin_angle = fin_idx * (360.0 / FIN_COUNT)
                with BuildSketch() as s_fin:
                    with Locations(Rotation(0, 0, fin_angle)):
                        with Locations((fin_center_radius, 0)):
                            Rectangle(FIN_RADIAL_SPAN, FIN_THICKNESS)
                extrude(amount=FIN_HEIGHT)

        # ======================================================================
        # 6. HUB BEZEL & EMBOSSED "CPU" CREST
        # ======================================================================
        z_crest_base = z_cooler_base + HUB_TOTAL_HEIGHT  # 12.8 mm

        # 6a. Circular bezel framing the crest (Z: 12.8 -> 13.2 mm)
        with Locations((0, 0, z_crest_base)):
            with BuildSketch() as s_bezel:
                Circle(radius=BEZEL_OUTER_RADIUS)
                Circle(radius=BEZEL_INNER_RADIUS, mode=Mode.SUBTRACT)
            extrude(amount=BEZEL_HEIGHT)

        # 6b. Raised bold "CPU" text badge (Z: 12.8 -> 13.6 mm, relief: 0.8 mm)
        with Locations((0, 0, z_crest_base)):
            with BuildSketch() as s_txt:
                Text(TEXT_LABEL, font_size=TEXT_FONT_SIZE, font_style=FontStyle.BOLD)
            extrude(amount=TEXT_RELIEF_HEIGHT)

    return cpu.part


def main():
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "output"))
    os.makedirs(output_dir, exist_ok=True)

    print("=================================================================")
    print("Generating CPU Educational Souvenir Parametric CAD Model...")
    print("=================================================================")
    
    part = build_cpu_model()
    
    # Paths for export
    stl_path = os.path.join(output_dir, "cpu_science_souvenir.stl")
    step_path = os.path.join(output_dir, "cpu_science_souvenir.step")
    source_script_path = os.path.join(output_dir, "cpu_model.py")
    
    # 1. Export STL (high fidelity for 3D printing)
    print("Exporting STL mesh (tolerance=0.005, angular_tolerance=0.1)...")
    export_stl(part, stl_path, tolerance=0.005, angular_tolerance=0.1)
    print(f"STL exported: {stl_path} ({os.path.getsize(stl_path):,} bytes)")

    # 2. Export STEP (B-Rep CAD interchange)
    print("Exporting STEP CAD model...")
    export_step(part, step_path)
    print(f"STEP exported: {step_path} ({os.path.getsize(step_path):,} bytes)")

    # 3. Copy clean standalone Python CAD script into output directory
    with open(__file__, "r") as src_f:
        with open(source_script_path, "w") as dst_f:
            dst_f.write(src_f.read())
    print(f"Native CAD source exported: {source_script_path}")

    # 4. Immediate Validation Checks
    print("\nRunning Automated Geometric Validation...")
    mesh = trimesh.load(stl_path)
    
    print(f"Watertight (Manifold): {mesh.is_watertight}")
    print(f"Total Vertices: {len(mesh.vertices):,}")
    print(f"Total Faces: {len(mesh.faces):,}")
    print(f"Exact Solid Volume: {part.volume:,.2f} mm^3 ({part.volume / 1000.0:.2f} cm^3)")
    print(f"Mesh Bounding Box Extents (X, Y, Z): {mesh.extents[0]:.2f} x {mesh.extents[1]:.2f} x {mesh.extents[2]:.2f} mm")
    
    # Assertions
    assert mesh.is_watertight, "ERROR: STL is not watertight / manifold!"
    assert 49.5 <= mesh.extents[0] <= 50.5, f"ERROR: Width out of spec: {mesh.extents[0]}"
    assert 49.5 <= mesh.extents[1] <= 50.5, f"ERROR: Length out of spec: {mesh.extents[1]}"
    assert 13.0 <= mesh.extents[2] <= 14.5, f"ERROR: Height out of spec: {mesh.extents[2]}"
    
    print("\n✓ CAD Model Generation and Geometric Validation Completed Successfully!")


if __name__ == "__main__":
    main()
