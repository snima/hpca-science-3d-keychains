# HPC&A Fantasy GPU Keychains — 3D Printing & Fabrication Guide

A creative collection of three distinct **Fantasy Editions** of the HPC&A GPU Keychain, specially designed for university outreach, tech gifts, and 3D printing enthusiasts. Each model is engineered from the ground up to follow rigorous **DFAM (Design for Additive Manufacturing)** principles: 100% support-free, flat bed adhesion, manifold topology, and pocket-durable keyring eyelets.

---

## 📸 Collection Visuals & Comparison

* **3-in-1 Trio Showcase**: [`gpu_fantasy_trio_showcase.png`](./gpu_fantasy_trio_showcase.png)
* **Chibi Kawaii GPU Hero Render**: [`gpu_fantasy_chibi_render.png`](./gpu_fantasy_chibi_render.png)
* **Sci-Fi Mecha Starship GPU Hero Render**: [`gpu_fantasy_mecha_render.png`](./gpu_fantasy_mecha_render.png)
* **Magic Rune Artifact GPU Hero Render**: [`gpu_fantasy_rune_render.png`](./gpu_fantasy_rune_render.png)
* **Parametric CAD Source Script**: [`../generate_fantasy_gpus.py`](../generate_fantasy_gpus.py)

---

## 1. The Three Editions

### Model A: Chibi Kawaii GPU Keychain (`gpu_fantasy_chibi`)
* **Aesthetic**: Playful, adorable cartoon character toy.
* **Key Features**:
  * Smiling cartoon face on the central fan hub (recessed eyes, pupils with sparkle reflections, smiling open mouth, rosy cheeks).
  * 8 curved petal-shaped turbine blades.
  * Cute rounded boots/feet along the bottom (reimagined PCIe connector).
  * Pillowy filleted corners ($R = 3.2\text{ mm}$) for maximum pocket ergonomics.
  * Curved top name banner with bold embossed **`HPC&A`**.
* **Files**: [`gpu_fantasy_chibi.stl`](./gpu_fantasy_chibi.stl) | [`gpu_fantasy_chibi.step`](./gpu_fantasy_chibi.step)
* **Dimensions**: $55.20 \times 34.40 \times 5.50\text{ mm}$
* **Weight**: $\approx 5.5\text{ g}$ in PLA

### Model B: Sci-Fi / Mecha Starship GPU Keychain (`gpu_fantasy_mecha`)
* **Aesthetic**: Futuristic high-tech aerospace fighter / hyperdrive warp core.
* **Key Features**:
  * Angular stealth mecha armor plating with forward cockpit/sensor nose cone and stabilizer winglets.
  * Supersonic jet intake turbine with 12 swept blades and center bullet cone.
  * Plasma heat radiation fin grille.
  * Heavy-duty industrial armored nameplate with bold **`HPC&A`**.
  * Rear rocket thruster nozzle housing the reinforced Ø4.6 mm keyring hole.
* **Files**: [`gpu_fantasy_mecha.stl`](./gpu_fantasy_mecha.stl) | [`gpu_fantasy_mecha.step`](./gpu_fantasy_mecha.step)
* **Dimensions**: $63.42 \times 29.88 \times 5.60\text{ mm}$
* **Weight**: $\approx 5.2\text{ g}$ in PLA

### Model C: Magic Rune / Crystal Artifact GPU Keychain (`gpu_fantasy_rune`)
* **Aesthetic**: Ancient dwarven techno-sorcery talisman fusing magic and silicon.
* **Key Features**:
  * Heatsink fins reimagined as 7 faceted hexagonal crystal gemstones (all drafted at $\le 45^\circ$ for 100% self-supporting FDM printability).
  * Arcane mystic vortex sigil / portal in place of the cooling fan.
  * Ancient runic inscriptions engraved into the frame borders.
  * Central knightly heraldic shield crest with bold **`HPC&A`**.
  * Ornate antique filigree bracket integrating the Ø4.6 mm keyring hole.
* **Files**: [`gpu_fantasy_rune.stl`](./gpu_fantasy_rune.stl) | [`gpu_fantasy_rune.step`](./gpu_fantasy_rune.step)
* **Dimensions**: $64.70 \times 28.40 \times 5.60\text{ mm}$
* **Weight**: $\approx 5.9\text{ g}$ in PLA

---

## 🖨️ Recommended 3D Slicer Settings (Universal for all 3 models)

* **Print Orientation**: Flat on backplate ($Z = 0\text{ mm}$ directly on build plate).
* **Layer Height**: `0.16 mm` (recommended for fine details and sharp text) or `0.20 mm` (fast print).
* **Walls / Perimeters**: `3` (ensures the eyelet hole is 100% solid concentric rings).
* **Infill**: `15% - 20%` (Gyroid pattern).
* **Supports**: **DISABLED (0% Supports)** — every feature is strictly self-supporting.
* **Brim**: Not required (large planar bed contact area $>1,390\text{ mm}^2$ guarantees zero warping on heated PEI).
* **Print Time**: $\approx 15\text{ minutes}$ (high-speed CoreXY) / $\approx 28\text{ minutes}$ (standard $50\text{ mm/s}$).

---

## 🎨 Dual-Color Filament Swap (Single Extruder)

To get stunning multi-color results on standard single-nozzle printers:
* **Chibi GPU**:
  * $Z = 0.0 \rightarrow 4.6\text{ mm}$: Mint Green or Pastel Blue (Body & Shoes)
  * Pause at $Z = 4.6\text{ mm}$: Switch to White or Pastel Pink (Top banner, face details, and `HPC&A` text)
* **Mecha Starship GPU**:
  * $Z = 0.0 \rightarrow 5.0\text{ mm}$: Gunmetal Grey or Matte Black (Armor hull)
  * Pause at $Z = 5.0\text{ mm}$: Switch to Gold or Electric Cyan (Raised `HPC&A` armor plate)
* **Magic Rune GPU**:
  * $Z = 0.0 \rightarrow 5.0\text{ mm}$: Antique Bronze or Copper (Talisman chassis & crystals)
  * Pause at $Z = 5.0\text{ mm}$: Switch to Bright Gold (Raised heraldic shield & `HPC&A` crest)
