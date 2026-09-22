# 🖨️ HPC&A 3D PRINTING PRODUCTION MANUAL & WORKSHOP GUIDE
## راهنمای جامع تولید و کارگاه پرینت سه‌بعدی برای مجموعه سخت‌افزاری HPC&A

**پروژه:** قطعات یادبود و جاکلیدی‌های رویداد علمی دانشگاهی و هویت آزمایشگاه
**طراح:** نیما (Designed by Nima)
**توسعه‌یافته برای:** گروه پژوهشی معماری و محاسبات با کارایی بالا (HPC&A Research Group)

---

## 🇮🇷 بخش اول: راهنمای فارسی مخصوص کارگاه پرینت سه‌بعدی

سلام به همکار محترم و اپراتور کارگاه پرینت سه‌بعدی!
تمام فایل‌های این مجموعه به صورت کاملاً مهندسی‌شده و با رعایت دقیق اصول پرینت سه‌بعدی FDM طراحی شده‌اند تا **سریع، بی‌دردسر و با بالاترین کیفیت** چاپ شوند.

### ۱. تنظیمات حیاتی اسلایسر (Slicer Settings)
* **نیاز به ساپورت (Supports):** **خیر - کاملاً خاموش (Support: NONE / 0%)**. تمام زوایای شیب‌ها و اورهنگ‌ها کمتر از ۴۵ درجه طراحی شده‌اند و هیچ نیازی به ساپورت‌گذاری ندارند.
* **ضخامت لایه (Layer Height):** **$0.20	ext{ mm}$** (برای اولین لایه و لایه‌های بعدی).
* **تراکم داخلی (Infill):** **۱۵٪ تا ۲۰٪** با الگوی Gyroid یا Grid.
* **تعداد دیواره‌ها (Wall Loops / Perimeters):** **۳ الی ۴ دور دیواره** (برای استحکام حداکثری سوراخ جاکلیدی در جیب).
* **تعداد لایه‌های کف و سقف (Top/Bottom Layers):** **۴ لایه کف / ۵ لایه سقف**.
* **نیاز به Brim / Raft:** **خیر**. تمام مدل‌ها دارای سطح تماس وسیع و کاملاً مسطح در کف ($Z=0$) هستند و بدون چسبندگی اضافه به خوبی روی پلیت می‌چسبند.
* **متریال پیشنهادی:** **PLA یا PETG** (دمای نازل: حدود ۲۰۰-۲۱۰ درجه برای PLA / دمای بد: ۵۵-۶۰ درجه).

---

### ۲. معرفی فایل‌های تکی و فایل‌های چاپ تیراژ بالا (Batch Plates)

| نام فایل | نوع قطعه | ابعاد (میلی‌متر) | وزن تقریبی | زمان چاپ تخمینی |
| :--- | :--- | :--- | :--- | :--- |
| **`batch_gpu_keychains_x6.stl`** | صفحه ۶ تایی جاکلیدی GPU | $214.7 	imes 65.3 	imes 5.4$ | $pprox 35	ext{ g}$ | حدود ۳ ساعت |
| **`batch_qpu_keychains_x6.stl`** | صفحه ۶ تایی پردازنده کوانتومی QPU | $192.7 	imes 82.0 	imes 5.1$ | $pprox 38	ext{ g}$ | حدود ۳.۵ ساعت |
| **`batch_spinning_rotors_x12.stl`** | صفحه ۱۲ تایی پروانه‌های چرخشی فن | $89.6 	imes 65.7 	imes 2.1$ | $pprox 3	ext{ g}$ | حدود ۲۵ دقیقه |
| **`batch_heterogeneous_suite_x6.stl`** | صفحه ترکیبی (۲ تا CPU + ۲ تا GPU + ۲ تا QPU) | $148.7 	imes 143.0 	imes 13.6$ | $pprox 55	ext{ g}$ | حدود ۴.۵ ساعت |
| **`gpu_keychain_hpca.stl`** | جاکلیدی GPU (نسخه یکپارچه صلب) | $64.7 	imes 27.3 	imes 5.4$ | $pprox 5.5	ext{ g}$ | حدود ۳۰ دقیقه |
| **`gpu_spinning_body.stl`** | بدنه جاکلیدی GPU (نسخه فن متحرک) | $64.7 	imes 27.3 	imes 5.4$ | $pprox 5.3	ext{ g}$ | حدود ۲۸ دقیقه |
| **`gpu_spinning_rotor.stl`** | پروانه فن چرخشی تک‌عددی | $arnothing 17.6 	imes 2.1$ | $pprox 0.25	ext{ g}$ | حدود ۲ دقیقه |
| **`qpu_keychain_hpca.stl`** | جاکلیدی چیپ کوانتومی تک‌عددی | $56.7 	imes 36.0 	imes 5.1$ | $pprox 6.4	ext{ g}$ | حدود ۳۵ دقیقه |
| **`cpu_science_souvenir.stl`** | یادبود پردازنده آموزشی تک‌عددی | $45.0 	imes 45.0 	imes 13.6$ | $pprox 18.0	ext{ g}$ | حدود ۱.۵ ساعت |

---

### ۳. نحوه مونتاژ نسخه فن چرخشی (Snap-Fit Assembly)
برای نسخه چرخشی:
1. بدنه (`gpu_spinning_body.stl`) و پروانه (`gpu_spinning_rotor.stl`) جداگانه چاپ می‌شوند. (پیشنهاد جذاب: پروانه را با یک رنگ متضاد، مثلاً بدنه خاکستری و پروانه آبی یا قرمز چاپ کنید!).
2. سوراخ وسط پروانه را روی پین برآمده وسط بدنه قرار دهید.
3. با نوک انگشت یک فشار عمودی کوچک وارد کنید تا صدای ضعیف «کلیک» شنیده شود و پروانه جا بیفتد.
4. پروانه اکنون بدون لق زدن و با تلرانس مهندسی $0.25	ext{ mm}$ به صورت ۳۶۰ درجه و آزادانه می‌چرخد!

---

### ۴. ترفند تغییر رنگ لایه‌ای در پرینتر تک‌نازل (Optional Filament Color Swap)
اگر می‌خواهید نوشته‌ها و برجستگی‌ها دورنگ و بسیار شیک شوند (بدون نیاز به سیستم چندرنگ چندکاناله):
* **در جاکلیدی GPU و QPU:**
  * لایه‌های $0.00$ تا $4.60	ext{ mm}$: رنگ اصلی بدنه (مشکی، طوسی تیتانیوم، یا سرمه‌ای).
  * در ارتفاع $Z = 4.60	ext{ mm}$ دستور **Pause at height** در اسلایسر بگذارید و فیلامنت را به **طلایی، نقره‌ای، یا سفید** تغییر دهید تا نوشته‌های `HPC&A` و کیوبیت‌های کوانتومی با کنتراست فوق‌العاده چاپ شوند!

---

## 🇬🇧 Section 2: English Technical Production Sheet

### Recommended Slicer Settings:
* **Nozzle Size:** $0.4	ext{ mm}$ standard.
* **Layer Height:** $0.20	ext{ mm}$ (First Layer: $0.20	ext{ mm}$).
* **Supports:** **STRICTLY OFF (0% supports required)**. All overhang angles $\le 45^\circ$.
* **Infill:** $15	ext{ - }20\%$ (Gyroid / Grid).
* **Wall Perimeters:** $3	ext{ - }4$ perimeters for high tensile strength on the keyring eyelet.
* **Top/Bottom Solid Layers:** 4 Bottom / 5 Top.
* **Bed Adhesion:** Skirt only (Brim/Raft NOT needed; flat $Z=0$ planar contact).
* **Material:** PLA / PETG / PLA+ ($205	ext{ - }215^\circ	ext{C}$ nozzle, $55	ext{ - }60^\circ	ext{C}$ bed).

### Mass Production Batch Files:
1. `batch_gpu_keychains_x6.stl`: 6x GPU keychains arrayed on $214.7 	imes 65.3	ext{ mm}$ footprint.
2. `batch_qpu_keychains_x6.stl`: 6x Quantum QPU keychains on $192.7 	imes 82.0	ext{ mm}$ footprint.
3. `batch_spinning_rotors_x12.stl`: 12x Snap-Fit fan impellers on $89.6 	imes 65.7	ext{ mm}$ footprint.
4. `batch_heterogeneous_suite_x6.stl`: 2x CPU + 2x GPU + 2x QPU combo pack on $148.7 	imes 143.0	ext{ mm}$ footprint.

### Snap-Fit Assembly:
Press the center bore of `gpu_spinning_rotor.stl` down onto the axle pin of `gpu_spinning_body.stl` until it clicks past the retention lip. The $0.25	ext{ mm}$ radial running gap allows free, low-friction $360^\circ$ rotation.

---
**Attribution:** All models feature **`DESIGNED BY NIMA | HPC&A`** debossed on the bottom layer ($Z=0$).
