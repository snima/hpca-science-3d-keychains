# 🖨️ HPC&A FANTASY & QUANTUM KEYCHAINS — 3D PRINTING WORKSHOP MANUAL
## راهنمای جامع تولید کارگاه پرینت سه‌بعدی برای مجموعه فانتزی و کوانتومی HPC&A

**مجموعه نهایی:** ۶ مدل جاکلیدی (۳ مدل کارت گرافیک فانتزی + ۳ مدل پردازش کوانتومی)
**طراح:** نیما (Designed by Nima)
**توسعه‌یافته برای:** گروه پژوهشی معماری و محاسبات با کارایی بالا (HPC&A Research Group)

---

## 🇮🇷 بخش اول: راهنمای فارسی مخصوص کارگاه پرینت سه‌بعدی

سلام به همکار محترم و اپراتور کارگاه پرینت سه‌بعدی!
این مجموعه شامل **۶ مدل جاکلیدی اختصاصی** (۳ مدل کارت گرافیک فانتزی + ۳ مدل فناوری کوانتومی) است. تمام مدل‌ها با بالاترین دقت مهندسی طراحی شده‌اند تا **بدون دردسر، با کیفیت بی‌نظیر و بدون نیاز به ساپورت** چاپ شوند.

### ۱. تنظیمات حیاتی اسلایسر (Slicer Settings)
* **نیاز به ساپورت (Supports):** **خیر - کاملاً خاموش (Support: NONE / 0%)**. تمام زوایا کمتر از ۴۵ درجه هستند و هیچ بخشی به ساپورت نیاز ندارد.
* **ضخامت لایه (Layer Height):** **$0.20	ext{ mm}$** (هم لایه اول و هم لایه‌های بعدی).
* **تراکم داخلی (Infill):** **۱۵٪ تا ۲۰٪** (الگوی Gyroid یا Grid).
* **تعداد دیواره‌ها (Wall Loops):** **۳ الی ۴ دور دیواره** (برای استحکام سوراخ جاکلیدی در جیب).
* **تعداد لایه‌های کف و سقف:** **۴ لایه کف / ۵ لایه سقف**.
* **نیاز به Brim / Raft:** **خیر**. تمام مدل‌ها در کف ($Z=0$) کاملاً مسطح هستند و چسبندگی عالی به تخت دارند.
* **متریال پیشنهادی:** **PLA یا PETG** (دمای نازل: ۲۰۰-۲۱۰ درجه / دمای بد: ۶۰ درجه).

---

### ۲. فایل‌های آماده برای چاپ تعداد بالا (Batch Print Plates)
برای راحتی کارگاه، فایل‌های چیدمان‌شده آماده روی ابعاد تخت استاندارد ($220 	imes 220	ext{ mm}$) تهیه شده است:

| نام فایل | محتویات صفحه | ابعاد چیدمان | وزن کل فیلامنت | زمان چاپ تخمینی |
| :--- | :--- | :--- | :--- | :--- |
| **`batch_master_suite_x6.stl`** | **پک مستر ۶ عددی (هر ۶ مدل فانتزی و کوانتومی در یک پرینت)** | $204 	imes 110	ext{ mm}$ | $pprox 34	ext{ g}$ | حدود ۲.۸ ساعت |
| **`batch_fantasy_gpus_x6.stl`** | **۶ عدد کارت گرافیک فانتزی (۲ تا چیبی + ۲ تا مکا + ۲ تا رونیک)** | $204 	imes 78	ext{ mm}$ | $pprox 34	ext{ g}$ | حدود ۳ ساعت |
| **`batch_quantum_collection_x6.stl`** | **۶ عدد کوانتومی (۲ تا چیپ QPU + ۲ تا لوستر کرایواستات + ۲ تا بلاخ)** | $174 	imes 130	ext{ mm}$ | $pprox 35	ext{ g}$ | حدود ۳ ساعت |

---

### ۳. معرفی ۶ مدل تکی مجموعه (Single STL Files)

#### الف) ۳ مدل کارت گرافیک فانتزی (Fantasy GPU Keychains):
1. **`gpu_fantasy_chibi.stl`**: کارت گرافیک کارتونی چیبی با صورت خندان و پروانه‌های گلبرگی ($55 	imes 34 	imes 5.5	ext{ mm}$).
2. **`gpu_fantasy_mecha.stl`**: سفینه جنگنده فضایی مکا با توربین جت مافوق‌صوت و اگزوز راکت ($63 	imes 30 	imes 5.6	ext{ mm}$).
3. **`gpu_fantasy_rune.stl`**: تالیسمان جادویی باستان با سیرکل احضار، سپر سلطنتی و کریستال‌های مانا ($65 	imes 28 	imes 5.6	ext{ mm}$).

#### ب) ۳ مدل پردازش کوانتومی (Quantum Keychains):
1. **`qpu_keychain_hpca.stl`**: تراشه ابررسانای کوانتومی با کیوبیت‌های ترانزمون و رزوناتورهای مارپیچی ($57 	imes 36 	imes 5.1	ext{ mm}$).
2. **`quantum_chandelier.stl`**: لوستر کرایواستات برودتی ۱۵ میلی‌کلوین با ۵ طبقه طلایی و قوطی شیلد QPU ($31 	imes 62 	imes 5.4	ext{ mm}$).
3. **`quantum_bloch.stl`**: مدالیون هشت‌ضلعی کره بلاخ با بردار حالت کوانتومی $|\psiangle$ و قطب‌های $|0angle, |1angle$ ($44 	imes 49 	imes 5.1	ext{ mm}$).

---

### ۴. حکاکی پشت و فیت بودن نوشته‌ها
* پشت تمامی ۶ مدل عبارت **`DESIGNED BY NIMA`** در لایه اول ($Z=0$) با عمق $0.35	ext{ mm}$ حکاکی شده است.
* در مدل لوستر، تمامی نوشته‌ها اعم از `HPC&A CRYOSTAT`، `DESIGNED BY NIMA` و `15 mK` در پشت و `HPC&A` و `QPU` در رو با **حاشیه امن بیش از ۵ میلی‌متر** قرار گرفته‌اند و هیچ بیرون‌زدگی ندارند.

### ۵. ترفند دورنگ کردن در پرینتر تک‌نازل (Filament Color Swap)
برای جلوه فوق‌العاده نوشته‌ها و جزئیات روی مدل‌ها:
* لایه‌های $0.00$ تا $4.00	ext{ mm}$ با رنگ پایه بدنه (مشکی، خاکستری تیتانیوم یا آبی تیره) چاپ شوند.
* در ارتفاع **$Z = 4.00	ext{ mm}$ یا $4.60	ext{ mm}$** دستور **Pause at height** داده شود و فیلامنت به **طلایی، نقره‌ای، یا سفید** تغییر کند تا خطوط طبقات، نوشته‌های `HPC&A` و کیوبیت‌ها دو رنگ شوند.

---

## 🇬🇧 Section 2: English Production Sheet for 3D Print Farm

### Quick Slicer Profile:
* **Nozzle:** 0.40 mm
* **Layer Height:** 0.20 mm
* **Supports:** **STRICTLY OFF (0%)** — All models are 100% self-supporting FDM.
* **Infill:** 15–20% (Gyroid / Grid).
* **Perimeters:** 3–4 walls (ensures high tensile strength for keyring eyelets).
* **Top/Bottom Solid Layers:** 4 Bottom / 5 Top.
* **Brim:** None needed (large planar Z=0 contact).
* **Material:** PLA or PETG (Bed: 60°C, Nozzle: 205–215°C).

### Master Production File:
* **`batch_master_suite_x6.stl`**: Contains all 6 unique models (3 Fantasy GPUs + 3 Quantum Keychains) arrayed cleanly within $204 	imes 110	ext{ mm}$, fitting any standard 220x220 mm bed (Ender-3, Prusa MK3/MK4, Bambu Lab X1/P1/A1).

---
**Attribution:** All models feature **`DESIGNED BY NIMA | HPC&A`** debossed on the bottom layer ($Z=0$).
