"""
Prompt Provider Service
سرویس ارائه‌دهنده پرامت
"""

from src.interfaces import IPromptProvider


class PromptProvider(IPromptProvider):
    """Default Prompt Provider (alias for PersianPromptProvider)"""

    def get_analysis_prompt(self) -> str:
        """Get the analysis prompt"""
        return PersianPromptProvider().get_analysis_prompt()


class PersianPromptProvider(IPromptProvider):
    """Provides Persian prompts for audio analysis"""

    def get_analysis_prompt(self) -> str:
        """Get the Persian analysis prompt"""
        return """
Please analyze and transcribe this audio carefully. Transform the voice to text and tell me what was said in each minute of this conversation.
At the end, provide a summary of what happened, what the problem was, and whether it was resolved.

ویس رو با دقت به متن تبدیل کن و بگو هر دقیقه چه چیزی گفته شده در این گفت گوی دو طرفه.
در آخر هم یک گزارش کلی بهم بده که چه اتفاقی افتاده و مشکل چی بوده و آیا حل شده یا نه.

لطفاً پاسخ را به این صورت ارائه بده:

## ۱. رونوشت کامل مکالمه

[متن کامل گفتگو]

## ۲. تحلیل دقیقه به دقیقه

**دقیقه ۰-۱:** [خلاصه آنچه در این دقیقه گفته شده]
**دقیقه ۱-۲:** [خلاصه آنچه در این دقیقه گفته شده]
... و ادامه

## ۳. گزارش کلی

- **موضوع اصلی مکالمه:** [شرح موضوع]
- **مشکل یا مسئله مطرح شده:** [شرح مشکل]
- **راه‌حل‌های ارائه شده:** [شرح راه‌حل‌ها]
- **وضعیت نهایی:** [حل شده/حل نشده/در حال بررسی]
- **نکات مهم:** [سایر نکات قابل توجه]

توجه: لطفاً پاسخ را در فرمت Markdown ارائه بده.
"""


class EnglishPromptProvider(IPromptProvider):
    """Provides English prompts for audio analysis"""

    def get_analysis_prompt(self) -> str:
        """Get the English analysis prompt"""
        return """
Please carefully transcribe this audio to text and provide a minute-by-minute breakdown of what was said in this conversation.
At the end, provide a general summary of what happened, what the problem was, and whether it was resolved.

Please format your response as follows:

## 1. Complete Conversation Transcript

[Full conversation text]

## 2. Minute-by-Minute Analysis

**Minute 0-1:** [Summary of what was said in this minute]
**Minute 1-2:** [Summary of what was said in this minute]
... and so on

## 3. General Summary

- **Main Topic:** [Description of the topic]
- **Problem or Issue Raised:** [Description of the problem]
- **Solutions Provided:** [Description of solutions]
- **Final Status:** [Resolved/Unresolved/Under Review]
- **Important Notes:** [Other notable points]

Note: Please provide the response in Markdown format.
"""
