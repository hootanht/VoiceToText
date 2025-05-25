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
        
        # Save the summary file
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"گزارش خلاصه ذخیره شد: {summary_file}")
        return summary_file
    
    def generate_summary_report(self, results: List[AnalysisResult]) -> str:
        """Generate summary report content (alias for compatibility)"""
        return self._generate_summary_markdown(results)
    
    def save_report_to_file(self, content: str, filepath: str) -> None:
        """Save report content to file"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _generate_analysis_markdown(self, result: AnalysisResult) -> str:
        """Generate Markdown content for a single analysis result"""
        timestamp = result.timestamp.strftime("%Y-%m-%d %H:%M:%S") if result.timestamp else "نامشخص"
        processing_time = f"{result.processing_time:.2f} ثانیه" if result.processing_time else "نامشخص"
        
        content = f"""# تحلیل فایل صوتی: {result.audio_file.file_name}

        ## اطلاعات فایل

        | ویژگی | مقدار |
        |--------|-------|
        | **نام فایل** | `{result.audio_file.file_name}` |
        | **فرمت** | {result.audio_file.format.upper()} |
        | **حجم فایل** | {self._format_file_size(result.audio_file.file_size)} |
        | **زمان پردازش** | {processing_time} |
        | **تاریخ تحلیل** | {timestamp} |
        | **وضعیت** | {"✅ موفق" if result.is_successful else "❌ ناموفق"} |

        ---

        """
        
        if result.is_successful:
            content += f"""## نتیجه تحلیل

        {result.analysis_text}

        ---

        *این گزارش توسط سیستم تحلیل صدا به متن با استفاده از Gemini AI تولید شده است.*
        """
        else:
            content += f"""## خطا در پردازش

        ```
        {result.error_message}
        ```

        ---

        *پردازش این فایل با خطا مواجه شده است. لطفاً فایل را بررسی کرده و دوباره تلاش کنید.*
        """
        return content
    
    def _generate_summary_markdown(self, results: List[AnalysisResult]) -> str:
        """Generate Markdown content for summary report"""
        successful = [r for r in results if r.is_successful]
        failed = [r for r in results if not r.is_successful]
        total_processing_time = sum(r.processing_time for r in results if r.processing_time)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Handle empty results
        if len(results) == 0:
            content = f"""# گزارش خلاصه پردازش فایل‌های صوتی

**تاریخ تولید گزارش:** {timestamp}

## آمار کلی

| آمار | تعداد |
|------|-------|
| **تعداد کل فایل‌ها** | 0 |
| **فایل‌های موفق** | 0 ✅ |
| **فایل‌های ناموفق** | 0 ❌ |
| **زمان کل پردازش** | 0.00 ثانیه |
| **میانگین زمان پردازش** | 0.00 ثانیه |

## نرخ موفقیت

```
نرخ موفقیت: 0.0%
```

---

هیچ فایلی برای پردازش یافت نشد.

*این گزارش توسط سیستم تحلیل صدا به متن تولید شده است.*
"""
            return content
        
        content = f"""# گزارش خلاصه پردازش فایل‌های صوتی

**تاریخ تولید گزارش:** {timestamp}

## آمار کلی

| آمار | تعداد |
|------|-------|
| **تعداد کل فایل‌ها** | {len(results)} |
| **فایل‌های موفق** | {len(successful)} ✅ |
| **فایل‌های ناموفق** | {len(failed)} ❌ |
| **زمان کل پردازش** | {total_processing_time:.2f} ثانیه |
| **میانگین زمان پردازش** | {total_processing_time/len(results):.2f} ثانیه |

## نرخ موفقیت

```
نرخ موفقیت: {len(successful)/len(results)*100:.1f}%
```

---

"""
        
        if successful:
            content += """## فایل‌های پردازش شده با موفقیت

| فایل | زمان پردازش | فایل خروجی |
|------|-------------|------------|
"""
            for result in successful:
                processing_time = f"{result.processing_time:.2f}s" if result.processing_time else "N/A"
                output_link = f"[{Path(result.output_file_path).name}]({result.output_file_path})" if result.output_file_path else "N/A"
                content += f"| `{result.audio_file.file_name}` | {processing_time} | {output_link} |\n"
            
            content += "\n---\n\n"
        
        if failed:
            content += """## فایل‌های ناموفق

| فایل | خطا |
|------|-----|
"""
            for result in failed:
                error_short = result.error_message[:100] + "..." if len(result.error_message) > 100 else result.error_message
                content += f"| `{result.audio_file.file_name}` | {error_short} |\n"
            
            content += "\n---\n\n"
        
        content += """## راهنمای استفاده از نتایج

1. **فایل‌های تحلیل شده:** بر روی لینک فایل خروجی کلیک کنید تا نتیجه تحلیل را مشاهده کنید
2. **فایل‌های ناموفق:** خطاهای مربوطه را بررسی کرده و مشکل را رفع کنید
3. **گزارش‌ها:** تمام گزارش‌ها در فرمت Markdown هستند و قابل مشاهده در هر ویرایشگر متن

---

*این گزارش توسط سیستم تحلیل صدا به متن تولید شده است.*
"""
        
        return content
    
    def _format_file_size(self, size_bytes: int) -> str:
        """Format file size in human readable format"""
        if size_bytes is None:
            return "نامشخص"
        
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f} KB"
        else:
            return f"{size_bytes / (1024 * 1024):.1f} MB"
