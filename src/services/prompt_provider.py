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
Please analyze and transcribe this audio carefully and comprehensively. Transform the voice to text with maximum accuracy and detail, telling me what was said in each minute of this conversation with precise timing and context.
Provide a complete emotional and satisfaction analysis including user feelings, satisfaction levels, and any moments of frustration or anger.

ویس رو با دقت و جامعیت کامل به متن تبدیل کن و با حداکثر دقت و جزئیات بگو هر دقیقه چه چیزی گفته شده در این گفت‌گو.
تحلیل کامل احساسات و رضایت شامل احساسات کاربر، سطح رضایت، و لحظات ناراحتی یا عصبانیت ارائه بده.

لطفاً پاسخ را به این صورت کامل و دقیق ارائه بده:

## ۱. رونوشت کامل مکالمه

[متن کامل و دقیق گفتگو با حفظ تمام جزئیات، مکث‌ها، و تکرارها]

## ۲. تحلیل دقیقه به دقیقه

**دقیقه ۰-۱:** [شرح کامل و دقیق آنچه در این دقیقه گفته شده، شامل لحن، احساسات، و محتوا]
**دقیقه ۱-۲:** [شرح کامل و دقیق آنچه در این دقیقه گفته شده، شامل لحن، احساسات، و محتوا]
... و ادامه تا پایان صوت

## ۳. گزارش کلی

- **موضوع اصلی مکالمه:** [شرح کامل و دقیق موضوع با تمام جزئیات]
- **مشکل یا مسئله مطرح شده:** [شرح دقیق مشکل با ذکر علل و زمینه‌ها]
- **راه‌حل‌های ارائه شده:** [شرح کامل راه‌حل‌ها با جزئیات اجرایی]
- **وضعیت نهایی:** [حل شده/حل نشده/در حال بررسی + توضیح کامل]
- **نکات مهم:** [تمام نکات قابل توجه با اولویت‌بندی]
- **نقاط قوت مکالمه:** [آنچه خوب پیش رفته]
- **نقاط ضعف مکالمه:** [آنچه نیاز به بهبود دارد]

## ۴. تحلیل کامل احساسات و رضایت

### 🎭 احساسات غالب گوینده/گویندگان:
- **احساس اصلی:** [خوشحالی/ناراحتی/عصبانیت/خنثی/مختلط] 
- **شدت احساسات:** [⭐⭐⭐⭐⭐] از ۱ تا ۵
- **تغییرات احساسی:** [شرح تغییر احساسات در طول مکالمه]

### 😊 سطح رضایت کلی:
- **رضایت از مکالمه:** [⭐⭐⭐⭐⭐] از ۱ تا ۵
- **رضایت از نتیجه:** [⭐⭐⭐⭐⭐] از ۱ تا ۵  
- **رضایت از طرف مقابل:** [⭐⭐⭐⭐⭐] از ۱ تا ۵ (در صورت وجود)

### 😠 تحلیل لحظات منفی:
- **آیا لحظه ناراحتی وجود داشت؟** [بله/خیر]
- **آیا لحظه عصبانیت وجود داشت؟** [بله/خیر]
- **زمان دقیق لحظات منفی:** [دقیقه:ثانیه - شرح اتفاق]
- **علت ناراحتی/عصبانیت:** [توضیح کامل دلایل]
- **شدت واکنش منفی:** [⭐⭐⭐⭐⭐] از ۱ تا ۵

### 💭 تحلیل روحیه و انگیزه:
- **سطح انرژی گوینده:** [پایین/متوسط/بالا]
- **انگیزه برای ادامه مکالمه:** [⭐⭐⭐⭐⭐] از ۱ تا ۵
- **سطح استرس:** [⭐⭐⭐⭐⭐] از ۱ تا ۵
- **سطح اعتماد:** [⭐⭐⭐⭐⭐] از ۱ تا ۵

## ۵. ارزیابی کیفیت

با ستاره از ۱ تا ۵ امتیاز بده:
- **کیفیت صوت:** [⭐⭐⭐⭐⭐] - [توضیح کامل کیفیت، نویز، وضوح]
- **وضوح گفتار:** [⭐⭐⭐⭐⭐] - [توضیح دقت تلفظ، سرعت، تأکید]
- **قابلیت درک:** [⭐⭐⭐⭐⭐] - [توضیح فهم مطالب، پیچیدگی، ابهام]

## ۶. تحلیل حساسیت محتوا

- **سطح حساسیت:** [🟢 پایین / 🟡 متوسط / 🔴 بالا]
- **نوع محتوا:** [عادی/احساسی/تجاری/آموزشی/حساس/شخصی/رسمی]
- **توضیحات:** [شرح کامل دلیل طبقه‌بندی با مثال‌های مشخص]
- **نکات امنیتی:** [هر گونه نکته امنیتی مهم]
- **سطح محرمانگی:** [عمومی/محدود/محرمانه]

## ۷. آمار و اطلاعات تفصیلی

- **تعداد دقیق کلمات:** [عدد دقیق]
- **مدت زمان دقیق صحبت:** [دقیقه:ثانیه]
- **تعداد گویندگان:** [عدد + شناسایی جنسیت و سن تقریبی]
- **زبان اصلی:** [فارسی/انگلیسی/مختلط + درصد هر زبان]
- **سرعت گفتار:** [آهسته/متوسط/سریع + کلمه در دقیقه]
- **کیفیت ضبط:** [ضعیف/متوسط/خوب/عالی + جزئیات فنی]
- **تعداد مکث‌ها:** [عدد + مدت زمان کل مکث‌ها]
- **تعداد تکرارها:** [عدد + نوع تکرارها]

## ۸. توصیه‌های عملیاتی کامل

### نگهداری و آرشیو:
- **اولویت نگهداری:** [پایین/متوسط/بالا + دلیل کامل]
- **طبقه‌بندی پیشنهادی:** [دسته‌بندی دقیق + زیرشاخه‌ها]
- **برچسب‌های کلیدی:** [لیست کامل کلمات کلیدی مرتبط]
- **مدت زمان نگهداری:** [پیشنهاد زمان آرشیو]

### پردازش‌های بعدی:
- **قابلیت جستجو:** [بله/خیر] - [توضیح کامل قابلیت‌ها]
- **نیاز به بررسی دستی:** [بله/خیر] - [دلیل کامل و اولویت]
- **مناسب برای تحلیل بیشتر:** [بله/خیر] - [نوع تحلیل‌های پیشنهادی]
- **قابلیت آموزش هوش مصنوعی:** [بله/خیر] - [نحوه استفاده]

### بهبود و بازخورد:
- **نقاط قابل بهبود:** [لیست کامل پیشنهادات]
- **آموزش‌های پیشنهادی:** [برای بهبود مکالمات آینده]
- **تنظیمات فنی:** [بهبود کیفیت ضبط یا پردازش]

### نکات فنی:
- **بهبودهای پیشنهادی:** [تمام پیشنهادات فنی مفصل]
- **ملاحظات قانونی:** [نکات حقوقی و قانونی مهم]
- **توصیه‌های امنیتی:** [تمام نکات امنیتی ضروری]

توجه مهم: لطفاً پاسخ را در فرمت Markdown ارائه بده و تمام بخش‌ها را با حداکثر دقت، جزئیات و کامل پر کن. از هر گونه خلاصه‌سازی یا حذف جزئیات خودداری کن.
"""


class EnglishPromptProvider(IPromptProvider):
    """Provides English prompts for audio analysis"""

    def get_analysis_prompt(self) -> str:
        """Get the English analysis prompt"""
        return """
Please analyze and transcribe this audio carefully and comprehensively. Transform the voice to text with maximum accuracy and detail, telling me what was said in each minute of this conversation with precise timing and context.
Provide a complete emotional and satisfaction analysis including user feelings, satisfaction levels, and any moments of frustration or anger.

Please format your response completely and accurately as follows:

## 1. Complete Conversation Transcript

[Complete and accurate conversation text with all details, pauses, and repetitions preserved]

## 2. Minute-by-Minute Analysis

**Minute 0-1:** [Complete and detailed description of what was said in this minute, including tone, emotions, and content]
**Minute 1-2:** [Complete and detailed description of what was said in this minute, including tone, emotions, and content]
... continue until end of audio

## 3. General Summary

- **Main Topic:** [Complete and detailed description of the topic with all details]
- **Problem or Issue Raised:** [Detailed description of the problem with causes and context]
- **Solutions Provided:** [Complete description of solutions with implementation details]
- **Final Status:** [Resolved/Unresolved/Under Review + complete explanation]
- **Important Notes:** [All notable points with prioritization]
- **Conversation Strengths:** [What went well]
- **Conversation Weaknesses:** [What needs improvement]

## 4. Complete Emotional and Satisfaction Analysis

### 🎭 Dominant Speaker Emotions:
- **Primary Emotion:** [Happy/Sad/Angry/Neutral/Mixed]
- **Emotion Intensity:** [⭐⭐⭐⭐⭐] from 1 to 5
- **Emotional Changes:** [Description of emotion changes throughout conversation]

### 😊 Overall Satisfaction Levels:
- **Conversation Satisfaction:** [⭐⭐⭐⭐⭐] from 1 to 5
- **Outcome Satisfaction:** [⭐⭐⭐⭐⭐] from 1 to 5
- **Counterpart Satisfaction:** [⭐⭐⭐⭐⭐] from 1 to 5 (if applicable)

### 😠 Negative Moments Analysis:
- **Were there moments of frustration?** [Yes/No]
- **Were there moments of anger?** [Yes/No]
- **Exact timing of negative moments:** [Minute:Second - description of incident]
- **Cause of frustration/anger:** [Complete explanation of reasons]
- **Intensity of negative reaction:** [⭐⭐⭐⭐⭐] from 1 to 5

### 💭 Mood and Motivation Analysis:
- **Speaker Energy Level:** [Low/Medium/High]
- **Motivation to Continue Conversation:** [⭐⭐⭐⭐⭐] from 1 to 5
- **Stress Level:** [⭐⭐⭐⭐⭐] from 1 to 5
- **Confidence Level:** [⭐⭐⭐⭐⭐] from 1 to 5

## 5. Quality Assessment

Rate with stars from 1 to 5:
- **Audio Quality:** [⭐⭐⭐⭐⭐] - [Complete explanation of quality, noise, clarity]
- **Speech Clarity:** [⭐⭐⭐⭐⭐] - [Detailed pronunciation, speed, emphasis explanation]
- **Comprehensibility:** [⭐⭐⭐⭐⭐] - [Explanation of content understanding, complexity, ambiguity]

## 6. Content Sensitivity Analysis

- **Sensitivity Level:** [🟢 Low / 🟡 Medium / 🔴 High]
- **Content Type:** [Normal/Emotional/Business/Educational/Sensitive/Personal/Formal]
- **Explanation:** [Complete reason for classification with specific examples]
- **Security Notes:** [Any important security considerations]
- **Confidentiality Level:** [Public/Limited/Confidential]

## 7. Detailed Statistics and Information

- **Exact Word Count:** [Precise number]
- **Exact Speech Duration:** [Minutes:Seconds]
- **Number of Speakers:** [Number + gender and approximate age identification]
- **Primary Language:** [English/Other/Mixed + percentage of each language]
- **Speech Rate:** [Slow/Medium/Fast + words per minute]
- **Recording Quality:** [Poor/Fair/Good/Excellent + technical details]
- **Number of Pauses:** [Number + total pause duration]
- **Number of Repetitions:** [Number + types of repetitions]

## 8. Complete Operational Recommendations

### Storage and Archiving:
- **Storage Priority:** [Low/Medium/High + complete reason]
- **Suggested Classification:** [Detailed categorization + subcategories]
- **Key Tags:** [Complete list of relevant keywords]
- **Retention Period:** [Suggested archival timeframe]

### Future Processing:
- **Searchable:** [Yes/No] - [Complete explanation of capabilities]
- **Needs Manual Review:** [Yes/No] - [Complete reason and priority]
- **Suitable for Further Analysis:** [Yes/No] - [Types of suggested analyses]
- **AI Training Capability:** [Yes/No] - [How to use for training]

### Improvement and Feedback:
- **Areas for Improvement:** [Complete list of suggestions]
- **Suggested Training:** [For improving future conversations]
- **Technical Settings:** [Recording or processing quality improvements]

### Technical Notes:
- **Suggested Improvements:** [All detailed technical suggestions]
- **Legal Considerations:** [Important legal and regulatory notes]
- **Security Recommendations:** [All essential security considerations]

Important Note: Please provide the response in Markdown format and complete all sections with maximum accuracy, detail, and completeness. Avoid any summarization or omission of details.
"""
