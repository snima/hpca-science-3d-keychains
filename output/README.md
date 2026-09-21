# CPU Educational Souvenir Token — 3D Printing & Fabrication Guide
**Event:** University Science Night Outreach  
**Design:** Microprocessor / CPU Physical Educational Souvenir  
**Author:** Mechanical & CAD Design Engineer  
**CAD System:** Parametric OpenCASCADE / `build123d`

---

## 1. Overview & Educational Intent

This physical educational token was created for university science outreach events to teach children and families what a modern microprocessor looks like inside and how computers compute.

Rather than looking like an abstract flat metal square, the model exposes the **physical hierarchy** of modern semiconductor packaging:

```
┌────────────────────────────────────────────────────────┐
│   [ACTIVE COOLING] Turbine Fan Shroud & "CPU" Crest    │ (Z: 12.8 – 13.6 mm)
├────────────────────────────────────────────────────────┤
│   [HEAT DISSIPATION] 12 Radial Aluminum Cooling Fins   │ (Z: 6.4 – 12.2 mm)
├────────────────────────────────────────────────────────┤
│   [COMPUTING CORE] Stepped Silicon Die Plateau         │ (Z: 5.6 – 6.4 mm)
├────────────────────────────────────────────────────────┤
│   [THERMAL SPREADER] Nickel-Plated Copper IHS          │ (Z: 3.0 – 5.6 mm)
├────────────────────────────────────────────────────────┤
│   [POWER DELIVERY] 8 Decoupling Ceramic Capacitors     │ (Z: 3.0 – 4.2 mm)
├────────────────────────────────────────────────────────┤
│   [DATA HIGHWAY] 45° Bus Traces & 8-Bit Binary Track   │ (Z: 3.0 – 3.5 mm)
├────────────────────────────────────────────────────────┤
│   [PACKAGE SUBSTRATE] PCB with Pin-1 Notch & Contacts  │ (Z: 0.0 – 3.0 mm)
├────────────────────────────────────────────────────────┤
│   [MOTHERBOARD INTERFACE] Recessed LGA Pad Grid Base   │ (Z: 0.0 mm / Bed)
└────────────────────────────────────────────────────────┘
```

### Educational Concepts for Science Presenters & Children
1. **The Brain (Silicon Die)**: The central raised core represents the silicon chip where billions of microscopic transistors execute instructions and calculate results.
2. **Thermal Management (Heatsink & Turbine Cooler)**: Computation requires moving electrical charges, which generates heat through Joule heating ($P = I^2 R$). Without heatsink fins and cooling airflow, high-performance processors would overheat in seconds!
3. **Data Highways (Traces & Castellated Edges)**: The 45° angled metallic tracks represent the microscopic copper traces that carry binary signals (data buses) between the core and the outside world.
4. **Binary Language**: Along the northern margin, a physical 8-bit track spells ASCII character **'C'** (`01000011` in binary: small dots = 0, large raised pads = 1), demonstrating how all digital words and images are composed of 1s and 0s.
5. **Clean Power (Decoupling Capacitors)**: The 8 small rectangular blocks surrounding the core represent ceramic bypass capacitors that filter voltage noise and store quick bursts of power.
6. **Orientation Notch (Pin 1)**: Three corners are rounded for child safety, while the bottom-left corner features a distinct 45° chamfer with a tactile dot. Presenters can challenge children to locate "Pin 1" and explain why processors can only be inserted in one specific direction.
7. **Land Grid Array (LGA)**: Flipping the token over reveals a flat grid of contact pads instead of old-fashioned bendable pins, showing how modern computers achieve reliable electrical contact without fragile parts.

---

## 2. Model Specifications

| Parameter | Specification | Manufacturing Rationale |
|---|---|---|
| **Footprint Dimensions** | 50.00 mm × 50.00 mm | Ideal hand-held token size for children; fits comfortable in palms and pockets. |
| **Total Height** | 13.60 mm | Substantial 3D relief within the 10–15 mm design window. |
| **Substrate Thickness** | 3.00 mm | Heavy-duty base plate; prevents flexing or layer delamination when dropped. |
| **Minimum Wall Thickness** | 1.60 mm (Fins / Shroud) | Exactly 4 perimeters with a 0.4 mm nozzle; high impact resistance. |
| **Minimum Feature Relief** | 0.50 mm (Traces & Vias) | Distinctly resolved by standard 0.20 mm layer height slicers. |
| **Corner Safety** | R = 3.0 mm (3 corners), 4.5 mm chamfer | Eliminates sharp points; completely safe for young children. |
| **Underside Safety** | Flat base with 0.35 mm recessed LGA pads | Zero sharp needle pins; safe tactile experience. |
| **Solid Enclosed Volume** | 11.68 cm³ (11,676 mm³) | Lightweight and compact. |
| **Part Mass (PLA @ 15% infill)** | ~10.4 – 14.5 grams | Extremely economical for high-volume outreach giveaways. |

---

## 3. Recommended 3D Printing & Slicer Settings

This model is engineered from the ground up for **FDM (Fused Deposition Modeling)** 3D printing in a single piece with **ZERO support material**.

### Primary Settings
* **Print Orientation**: Upright (flat base directly on print bed, heatsink/crest facing upward).
* **Layer Height**: `0.20 mm` (Standard) or `0.16 mm` (Fine detail).
* **First Layer Height**: `0.20 mm`.
* **Nozzle Diameter**: `0.40 mm` (Standard brass or hardened steel).
* **Perimeters / Wall Loops**: `3` (giving 1.2 mm solid outer shells).
* **Top Shell Layers**: `4` (minimum 0.8 mm solid top surface).
* **Bottom Shell Layers**: `3` (minimum 0.6 mm solid bottom surface).
* **Infill Density**: `15%` to `20%`.
* **Infill Pattern**: `Gyroid` or `Grid` (Gyroid provides equal strength in all directions).
* **Supports**: **NONE / DISABLED** (`Generate Support = False`). All overhangs are $\le 45^\circ$.
* **Brim / Raft**: **NONE / DISABLED**. The 2,284 mm² contact surface (>91% of footprint) guarantees rock-solid bed adhesion.

### Material & Temperature Recommendations
* **Filament**: Standard PLA (Polylactic Acid) — non-toxic, odorless, biodegradable, and rigid.
* **Nozzle Temperature**: 205°C – 215°C.
* **Bed Temperature**: 55°C – 60°C (Textured PEI, Satin sheet, or smooth glass).
* **Cooling Fan**: 100% after layer 2 (ensures crisp heatsink fin bridging and sharp text).

### Production Time & Material Estimates
* **Modern High-Speed Printers** (Bambu Lab X1C / P1S / A1, Prusa MK4, Voron 2.4 @ 150–250 mm/s):
  * **Print Time per Unit**: ~22 – 26 minutes.
  * **Material per Unit**: ~11 grams of PLA.
  * **Full Build Plate (16 units on 256×256 mm bed)**: ~6.5 hours (175 grams).
* **Standard FDM Printers** (Prusa MK3S+, Creality Ender 3 / CR-10 @ 50 mm/s):
  * **Print Time per Unit**: ~48 – 55 minutes.
  * **Full Build Plate (9 units on 220×220 mm bed)**: ~7.5 hours.
* **Cost per Unit**: Approximately **$0.25 to $0.35 USD** (based on a standard $20–$25/kg PLA spool), allowing a university department to produce **70–80 souvenirs per spool**.

---

## 4. Optional Multi-Color Printing (Dual-Color / AMS / Manual Swap)

While the model looks outstanding printed in a single solid color (e.g., Metallic Silver, Galaxy Black, or Silk Emerald Green), it is designed with stepped layer heights to allow **effortless color swaps even on single-extruder printers**:

| Layer Height (Z) | Recommended Color | Component Represented |
|---|---|---|
| **0.00 – 3.00 mm** (Layers 1 – 15) | Emerald Green / Matte Navy | PCB Substrate Package |
| **3.00 – 5.60 mm** (Layers 16 – 28) | Metallic Gold or Copper | Bus Traces, Capacitors, & Base |
| **5.60 – 6.40 mm** (Layers 29 – 32) | Dark Silicon Blue / Gloss Black | Exposed Silicon Die Plateau |
| **6.40 – 12.80 mm** (Layers 33 – 64) | Silk Silver / Aluminum Grey | Heatsink Fin Array & Shroud |
| **12.80 – 13.60 mm** (Layers 65 – 68) | Bright Gold or White | Raised "CPU" Crest & Bezel |

On printers without multi-material units (AMS/MMU), a single filament pause can be placed at **Z = 12.8 mm** to give the "CPU" lettering a contrasting highlight in under 1 minute!

---

## 5. File Manifest

Every file is organized within the `output/` directory:

```
output/
├── cpu_science_souvenir.stl     # Watertight, high-density binary STL for 3D slicers
├── cpu_science_souvenir.step    # Standardized ISO 10303 STEP B-Rep CAD model
├── cpu_model.py                 # Fully parametric Python source script (build123d)
├── cpu_render_isometric.png     # High-resolution 3D hero isometric render
├── cpu_render_multiview.png     # 4-panel educational visual showcase
├── cpu_technical_drawing.png    # Dimensioned engineering drawing (Top, Front, Iso)
├── cpu_technical_drawing.svg    # Vector CAD drawing for print / publication
├── validation_report.txt        # Automated geometric and manufacturing validation log
└── README.md                    # This documentation and outreach guide
```

---

## 6. Verification Summary

* **Watertight / Manifold**: Verified 100% closed surface with zero non-manifold edges.
* **Self-Intersections**: 0 detected.
* **Disconnected Shells**: 0 detected (single continuous solid body).
* **Overhang Angles**: 0 unsupported steep overhangs ($> 45^\circ$ from vertical).
* **Safety**: Child-safe filleted corners, recessed LGA pads, no detachable small parts.
