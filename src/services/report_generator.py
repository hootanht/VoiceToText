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
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        result.output_file_path = output_file
        print(f"نتیجه ذخیره شد در: {output_file}")
        return output_file
    
    def create_summary_report(self, results: List[AnalysisResult], output_folder: str) -> str:
        """Create a summary report of all results in Markdown format"""
        summary_file = os.path.join(output_folder, "summary_report.md")
        
        # Generate summary content
        markdown_content = self._generate_summary_markdown(results)
        
        # Add English note for empty results
        if not results:
            markdown_content = markdown_content.replace(
                "هیچ فایلی برای پردازش یافت نشد.",
                "No files found for processing. / هیچ فایلی برای پردازش یافت نشد."
            )
        
        # Save the summary file
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"گزارش خلاصه ذخیره شد: {summary_file}")
        return summary_file
    
    def generate_summary_report(self, results: List[AnalysisResult]) -> str:
        """Generate a summary report in Markdown format"""
        markdown_content = self._generate_summary_markdown(results)
        return markdown_content
    
    def _generate_summary_markdown(self, results: List[AnalysisResult]) -> str:
        """Generate summary markdown content"""
        # Calculate statistics
        total_files = len(results)
        successful_files = len([r for r in results if r.success])
        failed_files = total_files - successful_files
        total_time = sum(r.processing_time for r in results) if results else 0
        avg_time = total_time / total_files if total_files > 0 else 0
        success_rate = (successful_files / total_files * 100) if total_files > 0 else 0
        
        # Generate markdown
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        markdown = f"""# گزارش خلاصه پردازش فایل‌های صوتی

**تاریخ تولید گزارش:** {now}

## آمار کلی

| آمار | تعداد |
|------|-------|
| **تعداد کل فایل‌ها** | {total_files} |
| **فایل‌های موفق** | {successful_files} ✅ |
| **فایل‌های ناموفق** | {failed_files} ❌ |
| **زمان کل پردازش** | {total_time:.2f} ثانیه |
| **میانگین زمان پردازش** | {avg_time:.2f} ثانیه |

## نرخ موفقیت

```
نرخ موفقیت: {success_rate:.1f}%
```

---

{"هیچ فایلی برای پردازش یافت نشد." if not results else ""}

*این گزارش توسط سیستم تحلیل صدا به متن تولید شده است.*
"""
        return markdown
    
    def _generate_analysis_markdown(self, result: AnalysisResult) -> str:
        """Generate analysis markdown content"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        success_mark = "✅" if result.success else "❌"
        
        markdown = f"""# گزارش تحلیل فایل صوتی {result.audio_file.file_name}

**تاریخ تحلیل:** {now}

## اطلاعات فایل
- **نام فایل:** {result.audio_file.file_name}
- **مسیر فایل:** {result.audio_file.file_path}
- **حجم فایل:** {result.audio_file.file_size/1024:.1f} KB
- **فرمت فایل:** {result.audio_file.format}

## نتیجه تحلیل {success_mark}
- **وضعیت:** {"موفق" if result.success else "ناموفق"}
- **زمان پردازش:** {result.processing_time:.2f} ثانیه

## متن استخراج شده
{"```\n" + result.analysis_text + "\n```" if result.success else "```\nخطا در تحلیل فایل:\n" + result.error + "\n```"}

---

*این گزارش توسط سیستم تحلیل صدا به متن تولید شده است.*
"""
        return markdown
