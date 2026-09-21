# HPC&A Keychains Suite: 3D Printing Workshop Manual
**Author:** Nima | **Designation:** HPC&A Research Group  
**Scope:** 6 Production Models (3 Fantasy GPU Editions + 3 Quantum Hardware Editions)

---

## 1. Slicer Configuration & Production Parameters
* **Support Material:** **STRICTLY DISABLED (0% Supports)**  
  All 6 models are engineered with self-supporting geometry (overhang angles <= 45 degrees) and 100% flat bed adhesion at Z=0.
* **Layer Height:** 0.20 mm (First layer: 0.20 mm).
* **Infill Density:** 15% to 20% (Gyroid, Grid, or Adaptive Cubic).
* **Perimeter Walls:** 3 to 4 loops (ensures high tensile strength for the keyring through-holes).
* **Top/Bottom Shells:** 4 bottom solid layers, 5 top solid layers.
* **Bed Adhesion (Brim/Raft):** None required. The continuous planar base ensures secure adhesion to textured PEI, smooth PEI, or glass.
* **Recommended Filament:** PLA, PLA+, or PETG (Nozzle: 205-215 deg C, Bed: 60 deg C).

---

## 2. Mass Production Batch Print Plates
Pre-nested print layouts optimized for standard 220x220 mm build plates (Ender-3, Prusa MK3/MK4, Bambu Lab X1/P1/A1, Elegoo Neptune):

| File Name | Plate Contents | Array Footprint | Filament Weight | Print Time @ 0.20 mm |
| :--- | :--- | :--- | :--- | :--- |
| `batch_master_suite_x6.stl` | Complete 6-Pack (All 6 unique models) | 203.9 x 110.0 x 5.6 mm | ~34 g | ~2.8 hours |
| `batch_fantasy_gpus_x6.stl` | 6x Fantasy GPUs (2x Chibi, 2x Mecha, 2x Rune) | 203.9 x 78.4 x 5.6 mm | ~34 g | ~3.0 hours |
| `batch_quantum_collection_x6.stl` | 6x Quantum Models (2x QPU, 2x Chandelier, 2x Bloch) | 174.2 x 129.7 x 5.4 mm | ~35 g | ~3.0 hours |

---

## 3. Individual Models Summary

### A. Fantasy GPU Editions
1. `gpu_fantasy_chibi.stl`: Chibi cartoon GPU with anime face, blush cheeks, and petal fan (55.0 x 34.0 x 5.5 mm).
2. `gpu_fantasy_mecha.stl`: Sci-fi mecha fighter GPU with supersonic jet turbine and thrusters (63.0 x 30.0 x 5.6 mm).
3. `gpu_fantasy_rune.stl`: Cyber-runic arcane talisman with summoning circle and crest (65.0 x 28.0 x 5.6 mm).

### B. Quantum Computing Editions
1. `qpu_keychain_hpca.stl`: Superconducting QPU chip with Transmon qubits and CPW readout lines (56.7 x 36.0 x 5.1 mm).
2. `quantum_chandelier.stl`: Multi-tiered 15 mK dilution refrigerator cryostat with QPU can (31.2 x 61.7 x 5.4 mm).
3. `quantum_bloch.stl`: Octagonal Bloch sphere medallion with state vector |psi> and |0>, |1> poles (43.7 x 49.0 x 5.1 mm).

---

## 4. Underside Attribution & Clearances
* Every model features **DESIGNED BY NIMA** debossed on the bottom layer (Z=0, depth 0.35 mm).
* All inscriptions on both front and back surfaces maintain >= 5.0 mm clearance from exterior contours with zero boundary protrusion.

---

## 5. Dual-Color Filament Swap (Single Extruder)
For high-contrast lettering and circuit highlights on single-extruder printers:
1. Print layers 0.00 mm to 4.00 mm using primary dark filament (black, titanium gray, or dark navy).
2. Insert a **Pause at height** command in your slicer at **Z = 4.00 mm** (or **Z = 4.60 mm** for GPU models).
3. Switch to contrasting filament (gold, silver, or white) for the top details and text embossing.
