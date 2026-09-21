# HPC&A Edition GPU Keychain — 3D Printing & Fabrication Guide

A pocket-sized, geeky, dual-axial graphics card keychain designed specifically for the **HPC&A (High Performance Computing & Architecture)** research group. Inspired by modern high-end GPU industrial design (flow-through architecture, heatsink fins, radial fan blades, and PCIe connector fingers), engineered from the ground up as a **unified monolithic graphics card** with zero support requirements.

---

## 📸 Renderings & Technical Drawings

* **Technical Drawing**: [`gpu_keychain_technical_drawing.png`](./gpu_keychain_technical_drawing.png) | [`gpu_keychain_technical_drawing.svg`](./gpu_keychain_technical_drawing.svg)
* **Hero Isometric View**: [`gpu_keychain_render_hero.png`](./gpu_keychain_render_hero.png)
* **Multiview Studio Presentation**: [`gpu_keychain_render_multiview.png`](./gpu_keychain_render_multiview.png)
* **CAD Source Script**: [`gpu_keychain_model.py`](./gpu_keychain_model.py)
* **Printable Meshes**: [`gpu_keychain_hpca.stl`](./gpu_keychain_hpca.stl) (STL) & [`gpu_keychain_hpca.step`](./gpu_keychain_hpca.step) (STEP AP214)

---

## 📐 Physical Specifications (Unified Monolithic Revision)

| Parameter | Value | Engineering Rationale |
| :--- | :--- | :--- |
| **Form Factor** | **Unified Single Body** | No secondary underlayer, shelf, or baseplate pedestal. The model is 100% the graphics card itself! |
| **Total Bounding Dimensions** | **64.7 mm × 27.3 mm × 5.4 mm** | Ultra-slim, pocket-friendly; fits comfortably on any keyring. |
| **Card Body Dimensions** | **56.0 mm × 25.0 mm × 4.6 mm** | Authentic miniature scale of modern dual-slot graphics cards. |
| **Keyring Eyelet Hole** | **Ø4.6 mm** | Fits all standard split-rings (25 mm / 30 mm) and carabiners. |
| **Eyelet Outer Wall Thickness** | **2.9 mm solid perimeter** | Eliminates tear-out risk under heavy pocket tensile stress. |
| **PCIe Interface Tab** | **28.0 mm length, 2.3 mm protrusion** | Features polarization keyway notch and 16 debossed gold finger contact lines. |
| **Corner Fillet Radii** | **$R = 2.2\text{ mm}$** | Smooth ergonomics; zero sharp edges to snag on fabric or scratch keys. |
| **Solid Volume** | **$6.13\text{ cm}^3$** | Compact, durable, and very fast to print. |
| **Part Weight** | **~5.3 grams** (at 20% infill in PLA) | Ultra-lightweight for daily keychain carry. |
| **Watertight Solid** | **Yes** (1 shell, 0 non-manifold edges, Euler number = 0) | Flawless slicer slicing across Cura, PrusaSlicer, Bambu Studio, OrcaSlicer. |
| **Overhangs Requiring Supports** | **0** (Zero supports needed) | Every face builds straight up from the bed or within standard draft angles. |

---

## 🏷️ Custom Branding & Lab Identity

* **Card Spine (Top Edge)**:
  * Embossed: `HPC&A EDITION`
  * Text Relief: $0.6\text{ mm}$ raised
  * Font Height: $2.2\text{ mm}$
* **Front Shroud Badge**:
  * Embossed: `HPC&A`
  * Plaque Surface: $Z = 4.8\text{ mm}$
  * Text Relief: $0.6\text{ mm}$ (tops out at $Z = 5.4\text{ mm}$)
  * Font Height: $3.8\text{ mm}$
* **Zero Trademarks**:
  * 100% clean custom IP — no "GeForce", "RTX", or proprietary vendor logos. Perfectly compliant for university events, gifts, and academic dissemination.

---

## 🖨️ Recommended 3D Slicer Settings

### Basic Print Settings
* **Print Orientation**: Flat on backplate (Z = 0 mm directly touching the build plate).
* **Layer Height**: `0.16 mm` (recommended for razor-sharp text and fine fan blades) or `0.20 mm` (fast print).
* **Initial Layer Height**: `0.20 mm`.
* **Walls / Perimeters**: `3` (ensures the keyring hole is printed purely out of concentric solid perimeters for maximum tensile hoop strength).
* **Top / Bottom Solid Layers**: `4` top layers, `4` bottom layers.
* **Infill**: `15% - 20%` (Gyroid or Grid pattern).
* **Supports**: **DISABLED (0% Supports)** — the entire model is strictly support-free.
* **Brim**: Not required if using a heated PEI bed (clean 56×25 mm flat backplate provides abundant adhesion).

### Print Duration & Material
* **Print Time**: ~25–30 minutes per piece (standard speeds: 60–100 mm/s) / ~15 minutes on high-speed CoreXY printers (Bambu / Voron / Prusa MK4).
* **Filament Consumption**: ~5.3 g (approx. 180 keychains per 1 kg spool of filament!).
* **Material**: PLA, PLA+, PETG, or Matte PLA. (Matte PLA or silk silver/gold gives an incredible finish).

---

## 🎨 Multi-Color Printing & Filament Pause (Single-Extruder Friendly)

You don't need a multi-material system (like Bambu AMS or Prusa MMU) to get stunning dual-color or tri-color results!

### Single-Pause Dual-Color Accent (Pause at $Z = 4.8\text{ mm}$)
1. **$Z = 0.0\text{ mm} \rightarrow 4.8\text{ mm}$**: Print in **Black**, **Gunmetal Grey**, or **Silver** (Card body, heatsink fins, fan blades, outer shroud).
2. **At $Z = 4.8\text{ mm}$**: Insert a pause command (`M600` or slicer pause) and load **Gold**, **Yellow**, or **White** filament.
3. **$Z = 4.8\text{ mm} \rightarrow 5.4\text{ mm}$**: Resumes printing the raised `HPC&A` badge and `HPC&A EDITION` spine text in contrasting bright color!

---

## 🛠️ Post-Processing & Assembly

1. **Remove from Bed**: Allow the build plate to cool to room temperature; the keychain pops off effortlessly.
2. **Keyring Attachment**: Slide a standard $25\text{ mm}$ split key ring or a mini carabiner through the Ø4.6 mm eyelet.
3. **Optional Detail Polish**: A touch of metallic gold paint pen on the raised `HPC&A` text and the PCIe gold finger lines provides an instant premium touch!
