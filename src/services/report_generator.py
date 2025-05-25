"""
Markdown Report Generator
تولیدکننده گزارش مارک‌داون
"""

import os
from datetime import datetime
from pathlib import Path
from typing import List

from src.interfaces import IReportGenerator
from src.models import AnalysisResult


class MarkdownReportGenerator(IReportGenerator):
    """Generates Markdown reports following Single Responsibility Principle"""

    def save_analysis_result(self, result: AnalysisResult, output_folder: str) -> str:
        """Save analysis result to a Markdown file"""
        # Ensure output directory exists
        os.makedirs(output_folder, exist_ok=True)

        # Create output filename
        base_name = result.audio_file.stem_name
        output_file = os.path.join(output_folder, f"{base_name}_analysis.md")

        # Generate Markdown content
        markdown_content = self._generate_analysis_markdown(result)

        # Save the file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(markdown_content)

        result.output_file_path = output_file
        print(f"نتیجه ذخیره شد در: {output_file}")
        return output_file

    def create_summary_report(
        self, results: List[AnalysisResult], output_folder: str
    ) -> str:
        """Create a summary report of all results in Markdown format"""
        summary_file = os.path.join(output_folder, "summary_report.md")

        # Generate summary content
        markdown_content = self._generate_summary_markdown(results)

        # Add English note for empty results
        if not results:
            markdown_content = markdown_content.replace(
                "هیچ فایلی برای پردازش یافت نشد.",
                "No files found for processing. / هیچ فایلی برای پردازش یافت نشد.",
            )

        # Save the summary file
        with open(summary_file, "w", encoding="utf-8") as f:
            f.write(markdown_content)

        print(f"گزارش خلاصه ذخیره شد: {summary_file}")
        return summary_file

    def generate_summary_report(self, results: List[AnalysisResult]) -> str:
        """Generate a summary report in Markdown format"""
        markdown_content = self._generate_summary_markdown(results)
        return markdown_content

    def save_report_to_file(self, content: str, filepath: str) -> None:
        """Save report content to a file"""
        # Ensure output directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # Save the file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"گزارش ذخیره شد در: {filepath}")

    def _generate_summary_markdown(self, results: List[AnalysisResult]) -> str:
        """Generate summary markdown content"""
        # Calculate statistics
        total_files = len(results)
        successful_files = len([r for r in results if r.success])
        failed_files = total_files - successful_files
        total_time = sum(r.processing_time for r in results) if results else 0
        avg_time = total_time / total_files if total_files > 0 else 0
        success_rate = (successful_files / total_files *
                        100) if total_files > 0 else 0

        # Generate markdown
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if not results:
            markdown = f"""# 📊 گزارش خلاصه پردازش فایل‌های صوتی

## 🔍 وضعیت کلی
**تاریخ تولید گزارش:** {now}

### ⚠️ هیچ فایلی برای پردازش یافت نشد

**دلایل احتمالی:**
- فولدر `assets/voice/` خالی است  
- فرمت فایل‌ها پشتیبانی نمی‌شود
- مشکل در دسترسی به فایل‌ها

**اقدامات پیشنهادی:**
1. بررسی وجود فایل‌های صوتی در فولدر `assets/voice/`
2. اطمینان از فرمت‌های پشتیبانی شده (MP3, WAV, etc.)
3. بررسی مجوزهای دسترسی به فایل‌ها

---

*🤖 این گزارش به‌طور خودکار توسط سیستم هوش مصنوعی تولید شده است.*
*📅 تاریخ تولید: {now}*"""
        else:
            # Calculate additional metrics for non-empty results
            total_words = sum(len(r.analysis_text.split())
                              if r.analysis_text else 0 for r in results)
            avg_words = total_words / successful_files if successful_files > 0 else 0
            total_size = sum(r.audio_file.file_size for r in results)
            avg_size = total_size / total_files if total_files > 0 else 0

            # Performance categories
            fast_files = len(
                [r for r in results if r.processing_time and r.processing_time < 10])
            medium_files = len(
                [r for r in results if r.processing_time and 10 <= r.processing_time < 30])
            slow_files = len(
                [r for r in results if r.processing_time and r.processing_time >= 30])

            # Generate status indicators
            if success_rate >= 90:
                status_emoji = "🟢"
                status_text = "عالی"
            elif success_rate >= 70:
                status_emoji = "🟡"
                status_text = "خوب"
            else:
                status_emoji = "🔴"
                status_text = "نیاز به بررسی"

            markdown = f"""# 📊 گزارش خلاصه پردازش فایل‌های صوتی

## 🔍 وضعیت کلی
**تاریخ تولید گزارش:** {now}

### {status_emoji} وضعیت سیستم: {status_text}

---

## 📈 آمار کلی

| 📋 شاخص | 📊 مقدار | 📝 توضیحات |
|----------|-----------|-------------|
| **تعداد کل فایل‌ها** | {total_files} | تعداد فایل‌های پردازش شده |
| **فایل‌های موفق** | {successful_files} ✅ | پردازش با موفقیت |
| **فایل‌های ناموفق** | {failed_files} ❌ | نیاز به بررسی |
| **نرخ موفقیت** | {success_rate:.1f}% | درصد موفقیت کلی |
| **زمان کل پردازش** | {total_time:.2f} ثانیه | مدت زمان کل |
| **میانگین زمان** | {avg_time:.2f} ثانیه | میانگین هر فایل |

---

## 📊 تحلیل محتوا

### 📝 آمار متن
| شاخص | مقدار |
|-------|-------|
| **تعداد کل کلمات** | {total_words:,} کلمه |
| **میانگین کلمات** | {avg_words:.0f} کلمه/فایل |
| **حجم کل فایل‌ها** | {total_size/1024/1024:.2f} MB |
| **میانگین حجم** | {avg_size/1024:.1f} KB/فایل |

### ⚡ عملکرد پردازش
| سرعت | تعداد فایل | درصد |
|-------|-------------|------|
| **🟢 سریع** (< 10 ثانیه) | {fast_files} | {(fast_files/total_files*100) if total_files > 0 else 0:.1f}% |
| **🟡 متوسط** (10-30 ثانیه) | {medium_files} | {(medium_files/total_files*100) if total_files > 0 else 0:.1f}% |
| **🔴 آهسته** (> 30 ثانیه) | {slow_files} | {(slow_files/total_files*100) if total_files > 0 else 0:.1f}% |

---

## 📋 فهرست فایل‌های پردازش شده

| # | نام فایل | وضعیت | زمان | حجم | لینک گزارش |
|---|---------|--------|------|------|-------------|"""

            # Add file details
            for i, result in enumerate(results, 1):
                status_icon = "✅" if result.success else "❌"
                file_size = f"{result.audio_file.file_size/1024:.1f} KB"
                processing_time = f"{result.processing_time:.1f}s" if result.processing_time else "N/A"
                report_link = f"[نمایش]({result.audio_file.file_name.replace('.mp3', '_analysis.md')})" if hasattr(
                    result.audio_file, 'file_name') else "N/A"

                markdown += f"\n| {i} | `{result.audio_file.file_name}` | {status_icon} | {processing_time} | {file_size} | {report_link} |"

            markdown += f"""

---

## 🎯 خلاصه وضعیت

### ✅ نکات مثبت
- {"پردازش موفقیت‌آمیز اکثر فایل‌ها" if success_rate > 70 else "سیستم فعال و در حال کار"}
- {"سرعت مناسب پردازش" if avg_time < 20 else "سیستم در حال پردازش"}
- {"کیفیت قابل قبول نتایج" if successful_files > 0 else "آماده برای پردازش"}

### ⚠️ نکات قابل توجه
- {"بررسی فایل‌های ناموفق" if failed_files > 0 else "همه فایل‌ها موفق"}
- {"بهینه‌سازی سرعت پردازش" if avg_time > 30 else "سرعت مناسب"}
- {"نظارت بر کیفیت نتایج" if success_rate < 90 else "کیفیت عالی"}

### 📊 ارزیابی کلی
| معیار | امتیاز | وضعیت |
|-------|--------|--------|
| **کیفیت پردازش** | {"⭐⭐⭐⭐⭐" if success_rate >= 90 else "⭐⭐⭐⭐" if success_rate >= 70 else "⭐⭐⭐"} | {status_text} |
| **سرعت عملیات** | {"⭐⭐⭐⭐⭐" if avg_time < 10 else "⭐⭐⭐⭐" if avg_time < 20 else "⭐⭐⭐"} | {"عالی" if avg_time < 10 else "خوب" if avg_time < 20 else "قابل قبول"} |
| **نرخ موفقیت** | {"⭐⭐⭐⭐⭐" if success_rate >= 95 else "⭐⭐⭐⭐" if success_rate >= 80 else "⭐⭐⭐"} | {"ممتاز" if success_rate >= 95 else "عالی" if success_rate >= 80 else "خوب"} |

---

## 🔧 توصیه‌های عملیاتی

### 💡 بهبود عملکرد
- {"✅ سیستم بهینه عمل می‌کند" if success_rate >= 90 and avg_time < 20 else "⚠️ امکان بهینه‌سازی وجود دارد"}
- {"✅ ظرفیت پردازش مناسب" if total_files < 100 else "⚠️ در نظر گیری تقسیم‌بندی فایل‌ها"}
- {"✅ کیفیت نتایج قابل اعتماد" if success_rate > 80 else "⚠️ بررسی تنظیمات سیستم"}

### 📁 مدیریت فایل‌ها
- **آرشیو موفق:** {successful_files} فایل آماده نگهداری
- **بررسی مجدد:** {failed_files} فایل نیاز به توجه
- **ظرفیت آرشیو:** {total_size/1024/1024:.2f} MB فضای اشغال شده

---

*🤖 این گزارش به‌طور خودکار توسط سیستم هوش مصنوعی تحلیل صدا تولید شده است.*
*📅 آخرین بروزرسانی: {now}*
*🔄 گزارش بعدی: در صورت پردازش فایل‌های جدید*"""
        return markdown

    def _generate_analysis_markdown(self, result: AnalysisResult) -> str:
        """Generate analysis markdown content using AI-provided analysis"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        success_mark = "✅" if result.success else "❌"

        if result.success:
            # Use the complete AI analysis directly
            ai_analysis = result.analysis_text
        else:
            error_msg = getattr(result, "error_message", "خطای نامشخص")
            ai_analysis = f"خطا در تحلیل فایل:\n{error_msg}"

        markdown = f"""# 📊 گزارش تحلیل فایل صوتی

## 🔍 اطلاعات فایل
| مشخصه | مقدار |
|--------|--------|
| **نام فایل** | `{result.audio_file.file_name}` |
| **مسیر** | `{result.audio_file.file_path}` |
| **حجم** | {result.audio_file.file_size/1024:.1f} KB |
| **فرمت** | {result.audio_file.format.upper()} |
| **تاریخ تحلیل** | {now} |

---

## ⚡ وضعیت پردازش
- **وضعیت:** {success_mark} `{"موفقیت‌آمیز" if result.success else "ناموفق"}`
- **زمان پردازش:** `{result.processing_time:.2f} ثانیه`

---

## 🤖 تحلیل هوش مصنوعی

{ai_analysis}

---

*📅 تاریخ تولید گزارش: {now}*
*🤖 تحلیل شده توسط: Google Gemini AI*"""
        return markdown
