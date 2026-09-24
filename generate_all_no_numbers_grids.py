#!/usr/bin/env python3
"""
Generate No-Numbers (Sin Números) Grid Images for all 4 models:
1. Chibi GPU (6 blocks, Rotated 90°)
2. GPU con Espada (6 blocks, Rotated 90°)
3. QPU Chip (12 blocks, Rotated 90°)
4. Quantum Chandelier (12 blocks, Portrait)
"""
import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
KIDS_DIR = os.path.join(BASE_DIR, "kids_reward_challenge")
QPU_DIR = os.path.join(KIDS_DIR, "qpu_advanced_12blocks")
CHAND_DIR = os.path.join(KIDS_DIR, "chandelier_advanced_12blocks")

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font_scis = ImageFont.truetype(FONT_PATH, size=24)
font_scis_small = ImageFont.truetype(FONT_PATH, size=20)

# 1. Chibi GPU No-Numbers (6 blocks)
chibi_master = Image.open(os.path.join(KIDS_DIR, "chibi_gpu_2d_full_color.png")).convert('RGB')
W, H = chibi_master.size
dx = W / 3.0
dy = H / 2.0
chibi_no_num = chibi_master.copy()
draw = ImageDraw.Draw(chibi_no_num)

# Vertical cuts
for c in range(1, 3):
    x = int(round(c * dx))
    for y in range(0, H, 20):
        draw.line([(x, y), (x, min(y + 11, H))], fill=(219, 39, 119), width=4)

# Horizontal cut
y_mid = int(round(dy))
for x in range(0, W, 20):
    draw.line([(x, y_mid), (min(x + 11, W), y_mid)], fill=(219, 39, 119), width=4)
draw.text((int(dx * 0.4), y_mid - 28), '✂ - - - - - - - -', fill=(219, 39, 119), font=font_scis)
draw.text((int(dx * 1.4), y_mid - 28), '✂ - - - - - - - -', fill=(219, 39, 119), font=font_scis)
draw.text((int(dx * 2.4), y_mid - 28), '✂ - - - - - - - -', fill=(219, 39, 119), font=font_scis)

chibi_no_num_path = os.path.join(KIDS_DIR, "chibi_gpu_2d_6blocks_grid_no_num.png")
chibi_no_num.save(chibi_no_num_path)
chibi_rot_no_num = chibi_no_num.rotate(90, expand=True)
chibi_rot_no_num_path = os.path.join(KIDS_DIR, "chibi_gpu_2d_6blocks_grid_rot90_no_num.png")
chibi_rot_no_num.save(chibi_rot_no_num_path)
print("Saved Chibi No-Numbers grids")


# 2. QPU Chip No-Numbers (12 blocks)
qpu_master = Image.open(os.path.join(QPU_DIR, "qpu_2d_full_color.png")).convert('RGB')
W, H = qpu_master.size
dx = W / 4.0
dy = H / 3.0
qpu_no_num = qpu_master.copy()
draw = ImageDraw.Draw(qpu_no_num)

# Vertical cuts
for c in range(1, 4):
    x = int(round(c * dx))
    for y in range(0, H, 18):
        draw.line([(x, y), (x, min(y + 10, H))], fill=(2, 132, 199), width=4)

# Horizontal cuts
for r in range(1, 3):
    y = int(round(r * dy))
    for x in range(0, W, 18):
        draw.line([(x, y), (min(x + 10, W), y)], fill=(2, 132, 199), width=4)
    draw.text((int(dx * 0.4), y - 24), '✂ - - - -', fill=(2, 132, 199), font=font_scis_small)
    draw.text((int(dx * 1.4), y - 24), '✂ - - - -', fill=(2, 132, 199), font=font_scis_small)
    draw.text((int(dx * 2.4), y - 24), '✂ - - - -', fill=(2, 132, 199), font=font_scis_small)
    draw.text((int(dx * 3.4), y - 24), '✂ - - - -', fill=(2, 132, 199), font=font_scis_small)

qpu_no_num_path = os.path.join(QPU_DIR, "qpu_2d_12blocks_grid_no_num.png")
qpu_no_num.save(qpu_no_num_path)
qpu_rot_no_num = qpu_no_num.rotate(90, expand=True)
qpu_rot_no_num_path = os.path.join(QPU_DIR, "qpu_2d_12blocks_grid_rot90_no_num.png")
qpu_rot_no_num.save(qpu_rot_no_num_path)
print("Saved QPU No-Numbers grids")


# 3. Quantum Chandelier No-Numbers (12 blocks)
chand_master = Image.open(os.path.join(CHAND_DIR, "chandelier_2d_master.png")).convert('RGB')
W, H = chand_master.size
dx = W / 3.0
dy = H / 4.0
chand_no_num = chand_master.copy()
draw = ImageDraw.Draw(chand_no_num)

# Vertical cuts
for c in range(1, 3):
    x = int(round(c * dx))
    for y in range(0, H, 20):
        draw.line([(x, y), (x, min(y + 11, H))], fill=(245, 158, 11), width=4)

# Horizontal cuts
for r in range(1, 4):
    y = int(round(r * dy))
    for x in range(0, W, 20):
        draw.line([(x, y), (min(x + 11, W), y)], fill=(245, 158, 11), width=4)
    draw.text((int(dx * 0.4), y - 24), '✂ - - - -', fill=(245, 158, 11), font=font_scis_small)
    draw.text((int(dx * 1.4), y - 24), '✂ - - - -', fill=(245, 158, 11), font=font_scis_small)
    draw.text((int(dx * 2.4), y - 24), '✂ - - - -', fill=(245, 158, 11), font=font_scis_small)

chand_no_num_path = os.path.join(CHAND_DIR, "chandelier_2d_12blocks_grid_no_num.png")
chand_no_num.save(chand_no_num_path)
print("Saved Chandelier No-Numbers grid")

print("All No-Numbers grids generated successfully!")
