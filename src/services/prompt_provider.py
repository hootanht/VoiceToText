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

🕒 **CRITICAL TIMESTAMP REQUIREMENTS:**
- Every transcript line MUST include precise start-end timestamps: [mm:ss-mm:ss]
- Every topic discussion MUST specify exact time ranges when it was discussed
- Break down each minute into 20-second segments for detailed analysis
- Identify specific time ranges for different topics (e.g., pricing discussion from 00:10-00:35)
- Calculate total time spent on each topic category across the entire conversation

ویس رو با دقت و جامعیت کامل به متن تبدیل کن و با حداکثر دقت و جزئیات بگو هر دقیقه چه چیزی گفته شده در این گفت‌گو.
تحلیل کامل احساسات و رضایت شامل احساسات کاربر، سطح رضایت، و لحظات ناراحتی یا عصبانیت ارائه بده.

🕒 **الزامات حیاتی تایم‌کد:**
- هر خط رونوشت باید شامل زمان دقیق شروع-پایان باشد: [mm:ss-mm:ss]
- هر بحث موضوعی باید بازه زمانی دقیق مشخص شود
- هر دقیقه را به بخش‌های ۲۰ ثانیه‌ای تقسیم کن
- بازه‌های زمانی دقیق موضوعات مختلف را مشخص کن (مثل بحث قیمت از 00:10-00:35)
- مجموع زمان صرف شده روی هر دسته موضوع را در کل مکالمه محاسبه کن

⚠️ IMPORTANT: تمام بخش‌های زیر الزامی هستند و باید به طور کامل و مفصل پر شوند. هیچ بخشی را خلاصه نکن یا حذف نکن.

لطفاً پاسخ را به این صورت کامل و دقیق ارائه بده:

## ۱. رونوشت کامل مکالمه با تایم‌کد

هر گوینده را به صورت جداگانه در یک خط مجزا بنویس و مشتری و اپراتور را از هم تفکیک کن. برای هر قطعه گفتار، زمان شروع و پایان را مشخص کن:

**[00:05-00:18] مشتری**: [متن گفته شده توسط مشتری از ثانیه ۵ تا ۱۸]
**[00:18-00:35] اپراتور**: [متن گفته شده توسط اپراتور از ثانیه ۱۸ تا ۳۵]
**[00:35-00:52] مشتری**: [متن گفته شده توسط مشتری از ثانیه ۳۵ تا ۵۲]
**[00:52-01:15] اپراتور**: [متن گفته شده توسط اپراتور از ثانیه ۵۲ تا ۱ دقیقه و ۱۵ ثانیه]
...

⏰ **نکات مهم زمان‌بندی:**
- برای هر قطعه گفتار، دقیقاً زمان شروع و پایان را مشخص کن
- در صورت وجود مکث طولانی (بیش از ۳ ثانیه)، آن را جداگانه ذکر کن: **[01:15-01:18] [مکث ۳ ثانیه]**
- اگر دو نفر همزمان صحبت می‌کنند: **[01:20-01:25] مشتری + اپراتور**: [توضیح همزمانی]

حتماً مکث‌ها، تکرارها و جزئیات مکالمه را حفظ کن.

## ۲. تحلیل دقیقه به دقیقه با جزئیات زمانی

**دقیقه ۰-۱ (00:00-01:00):** [شرح کامل و دقیق آنچه در این دقیقه گفته شده، شامل لحن، احساسات، و محتوا]
- **بخش‌های کلیدی**: 
  - **00:00-00:20**: [خلاصه این ۲۰ ثانیه]
  - **00:20-00:40**: [خلاصه این ۲۰ ثانیه] 
  - **00:40-01:00**: [خلاصه این ۲۰ ثانیه]

**دقیقه ۱-۲ (01:00-02:00):** [شرح کامل و دقیق آنچه در این دقیقه گفته شده، شامل لحن، احساسات، و محتوا]
- **بخش‌های کلیدی**:
  - **01:00-01:20**: [خلاصه این ۲۰ ثانیه]
  - **01:20-01:40**: [خلاصه این ۲۰ ثانیه]
  - **01:40-02:00**: [خلاصه این ۲۰ ثانیه]

... و ادامه تا پایان صوت

### 🏷️ طبقه‌بندی با تایم‌کد دقیق

**دقیقه ۰-۱:** 
- **تگ:** [💰 pricing / ⚡ features / 🎯 need / ⚠️ service problems / ➡️ next steps / 🤖 LLM suggestion: ___]
- **زمان‌های دقیق موضوع**: 
  - **💰 قیمت**: [00:05-00:25] - [توضیح کوتاه موضوع قیمت]
  - **⚡ قابلیت**: [00:35-00:58] - [توضیح کوتاه موضوع قابلیت]
- **توضیح کلی دقیقه:** [دلیل انتخاب این دسته]

**دقیقه ۱-۲:**
- **تگ:** [💰 pricing / ⚡ features / 🎯 need / ⚠️ service problems / ➡️ next steps / 🤖 LLM suggestion: ___]
- **زمان‌های دقیق موضوع**:
  - **[نوع موضوع]**: [01:10-01:45] - [توضیح کوتاه]
  - **[نوع موضوع]**: [01:45-01:58] - [توضیح کوتاه]
- **توضیح کلی دقیقه:** [دلیل انتخاب این دسته]

... و ادامه برای تمام دقایق

### 📊 خلاصه زمان‌بندی موضوعات

**💰 قیمت (Pricing):**
- **مجموع زمان صحبت**: [X دقیقه و Y ثانیه]
- **بازه‌های زمانی**: [00:05-00:25], [02:30-03:15], [05:40-06:10]
- **خلاصه نکات**: [خلاصه تمام نکات مطرح شده درباره قیمت]

**⚡ قابلیت‌ها (Features):**
- **مجموع زمان صحبت**: [X دقیقه و Y ثانیه]
- **بازه‌های زمانی**: [00:35-01:20], [03:45-04:30]
- **خلاصه نکات**: [خلاصه تمام نکات مطرح شده درباره قابلیت‌ها]

**🎯 نیاز مشتری (Customer Need):**
- **مجموع زمان صحبت**: [X دقیقه و Y ثانیه]
- **بازه‌های زمانی**: [01:20-02:10], [04:30-05:00]
- **خلاصه نکات**: [خلاصه تمام نیازهای مطرح شده]

**⚠️ مشکلات سرویس (Service Problems):**
- **مجموع زمان صحبت**: [X دقیقه و Y ثانیه]
- **بازه‌های زمانی**: [02:10-02:30], [06:10-07:00]
- **خلاصه نکات**: [خلاصه تمام مشکلات مطرح شده]

**➡️ مراحل بعدی (Next Steps):**
- **مجموع زمان صحبت**: [X دقیقه و Y ثانیه]
- **بازه‌های زمانی**: [07:00-07:45]
- **خلاصه نکات**: [خلاصه تمام مراحل بعدی]

## ۳. گزارش کلی

- **موضوع اصلی مکالمه:** [شرح کامل و دقیق موضوع با تمام جزئیات]
- **مشکل یا مسئله مطرح شده:** [شرح دقیق مشکل با ذکر علل و زمینه‌ها]
- **راه‌حل‌های ارائه شده:** [شرح کامل راه‌حل‌ها با جزئیات اجرایی]
- **وضعیت نهایی:** [حل شده/حل نشده/در حال بررسی + توضیح کامل]
- **نکات مهم:** [تمام نکات قابل توجه با اولویت‌بندی]
- **نقاط قوت مکالمه:** [آنچه خوب پیش رفته]
- **نقاط ضعف مکالمه:** [آنچه نیاز به بهبود دارد]

## ۳.۱. خلاصه طبقه‌بندی موضوعات با تایم‌کد

- **💰 قیمت (Pricing):** 
  - **مجموع زمان**: [X دقیقه Y ثانیه] 
  - **بازه‌های زمانی**: [00:05-00:25], [02:30-03:15], [05:40-06:10]
  - **خلاصه نکات**: [خلاصه تمام نکات مطرح شده درباره قیمت]
  
- **⚡ قابلیت‌ها (Features):** 
  - **مجموع زمان**: [X دقیقه Y ثانیه]
  - **بازه‌های زمانی**: [00:35-01:20], [03:45-04:30] 
  - **خلاصه نکات**: [خلاصه تمام نکات مطرح شده درباره قابلیت‌ها]
  
- **🎯 نیاز مشتری (Customer Need):** 
  - **مجموع زمان**: [X دقیقه Y ثانیه]
  - **بازه‌های زمانی**: [01:20-02:10], [04:30-05:00]
  - **خلاصه نکات**: [خلاصه تمام نیازهای مطرح شده]
  
- **⚠️ مشکلات سرویس (Service Problems):** 
  - **مجموع زمان**: [X دقیقه Y ثانیه]
  - **بازه‌های زمانی**: [02:10-02:30], [06:10-07:00]
  - **خلاصه نکات**: [خلاصه تمام مشکلات مطرح شده]
  
- **➡️ مراحل بعدی (Next Steps):** 
  - **مجموع زمان**: [X دقیقه Y ثانیه]
  - **بازه‌های زمانی**: [07:00-07:45]
  - **خلاصه نکات**: [خلاصه تمام مراحل بعدی]
  
- **🤖 موضوعات پیشنهادی LLM:** 
  - **[نام موضوع جدید]**: 
    - **مجموع زمان**: [X دقیقه Y ثانیه]
    - **بازه‌های زمانی**: [mm:ss-mm:ss]
    - **خلاصه**: [توضیح موضوع و دلیل پیشنهاد]

**آمار کلی طبقه‌بندی:**
- موضوع غالب مکالمه: [موضوعی که بیشترین زمان را شامل شده]
- تنوع موضوعات: [آیا مکالمه متمرکز بوده یا پراکنده]
- موضوعات حل نشده: [موضوعاتی که نیاز به پیگیری دارند]

## ۴. تحلیل احساسات و رضایت

### 🎭 احساسات کلی:
- **گوینده اول:** [احساس اصلی] ⭐⭐⭐⭐⭐ (شدت) - [لحن: رسمی/دوستانه/عصبی/آرام]
- **گوینده دوم:** [احساس اصلی] ⭐⭐⭐⭐⭐ (شدت) - [لحن: رسمی/دوستانه/عصبی/آرام]
- **تغییرات احساسی:** [شرح تغییرات در طول مکالمه]

### � رضایت:
- **رضایت از مکالمه:** ⭐⭐⭐⭐⭐ - [دلیل]
- **رضایت از نتیجه:** ⭐⭐⭐⭐⭐ - [دلیل]

### 😠 لحظات منفی:
- **ناراحتی:** [بله/خیر] - [زمان + دلیل]
- **عصبانیت:** [بله/خیر] - [زمان + دلیل]
- **سطح استرس:** ⭐⭐⭐⭐⭐ - [توضیح]
- **زمان دقیق لحظات منفی:** [mm:ss-mm:ss - شرح اتفاق، مثال: 02:15-02:30 - مشتری عصبانی شد بخاطر تأخیر]
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

## ۷. آمار و اطلاعات کلیدی

- **تعداد کلمات:** [عدد دقیق] | **کلمات در دقیقه:** [محاسبه]
- **مدت زمان:** [دقیقه:ثانیه] | **زمان خالص گفتار:** [بدون مکث‌ها]
- **تعداد گویندگان:** [عدد] - **گوینده غالب:** [کدام یکی + درصد زمان]
- **زبان:** [فارسی ___% / انگلیسی ___% / سایر ___%]
- **سرعت گفتار:** [آهسته/متوسط/سریع] - **لهجه:** [تشخیص منطقه]
- **کیفیت ضبط:** ⭐⭐⭐⭐⭐ - **نویز:** [کم/متوسط/زیاد]
- **تعداد مکث‌ها:** [عدد] | **مدت کل مکث:** [ثانیه]
- **تکرارها:** [عدد] | **بیشترین کلمه تکراری:** [کلمه: ___ بار]

## ۸. توصیه‌های عملیاتی

### 🗄️ نگهداری:
- **اولویت:** [پایین/متوسط/بالا] - **دلیل:** [توضیح]
- **طبقه‌بندی:** [دسته اصلی] > [زیرشاخه] 
- **برچسب‌ها:** [5 کلمه کلیدی مهم]
- **مدت نگهداری:** [___ ماه] - **سطح دسترسی:** [عمومی/محدود/محرمانه]

### 🔄 پردازش بعدی:
- **جستجو:** [بله/خیر] - **بررسی دستی:** [بله/خیر + اولویت]
- **تحلیل بیشتر:** [احساسات/کلمات کلیدی/الگو] 
- **آموزش AI:** [بله/خیر] - **نحوه استفاده:** [توضیح]

### 🎯 بهبود:
1. **نکته اول:** [پیشنهاد عملی]
2. **نکته دوم:** [پیشنهاد عملی]
3. **نکته سوم:** [پیشنهاد عملی]

### ⚙️ نکات فنی:
- **بهبود تجهیزات:** [پیشنهاد مشخص]
- **ملاحظات حقوقی:** [نکته مهم]
- **امنیت:** [توصیه کلیدی]

🚨 مهم: تمام بخش‌ها الزامی هستند. هر بخش حداقل 2-3 خط توضیح داشته باشد. اعداد دقیق باشند و امتیازات توجیه داشته باشند. اگر اطلاعاتی نداری، بنویس "اطلاعات کافی نیست" اما تخمین معقول بده.
"""


class EnglishPromptProvider(IPromptProvider):
    """Provides English prompts for audio analysis"""

    def get_analysis_prompt(self) -> str:
        """Get the English analysis prompt"""
        return """
Please analyze and transcribe this audio carefully and comprehensively. Transform the voice to text with maximum accuracy and detail, telling me what was said in each minute of this conversation with precise timing and context.
Provide a complete emotional and satisfaction analysis including user feelings, satisfaction levels, and any moments of frustration or anger.

🕒 **CRITICAL TIMESTAMP REQUIREMENTS:**
- Every transcript line MUST include precise start-end timestamps: [mm:ss-mm:ss]
- Every topic discussion MUST specify exact time ranges when it was discussed
- Break down each minute into 20-second segments for detailed analysis
- Identify specific time ranges for different topics (e.g., pricing discussion from 00:10-00:35)
- Calculate total time spent on each topic category across the entire conversation

⚠️ IMPORTANT: All sections below are mandatory and must be filled completely and in detail. Do not summarize or omit any sections.

Please format your response completely and accurately as follows:

## 1. Complete Conversation Transcript with Timestamps

Separate each speaker on a new line and distinguish between customer and operator. For each speech segment, specify the start and end time:

**[00:05-00:18] Customer**: [Text spoken by the customer from second 5 to 18]
**[00:18-00:35] Operator**: [Text spoken by the operator from second 18 to 35]
**[00:35-00:52] Customer**: [Text spoken by the customer from second 35 to 52]
**[00:52-01:15] Operator**: [Text spoken by the operator from second 52 to 1 minute 15 seconds]
...

⏰ **Important Timing Notes:**
- For each speech segment, specify exactly the start and end time
- If there are long pauses (more than 3 seconds), mention them separately: **[01:15-01:18] [3-second pause]**
- If two people speak simultaneously: **[01:20-01:25] Customer + Operator**: [description of overlap]

Make sure to preserve all pauses, repetitions, and conversational details.

## 2. Minute-by-Minute Analysis with Detailed Timing

**Minute 0-1 (00:00-01:00):** [Complete and detailed description of what was said in this minute, including tone, emotions, and content]
- **Key Segments**: 
  - **00:00-00:20**: [Summary of these 20 seconds]
  - **00:20-00:40**: [Summary of these 20 seconds] 
  - **00:40-01:00**: [Summary of these 20 seconds]

**Minute 1-2 (01:00-02:00):** [Complete and detailed description of what was said in this minute, including tone, emotions, and content]
- **Key Segments**:
  - **01:00-01:20**: [Summary of these 20 seconds]
  - **01:20-01:40**: [Summary of these 20 seconds]
  - **01:40-02:00**: [Summary of these 20 seconds]

... continue until end of audio

## 2.1. Minute-by-Minute Categorization with Precise Timestamps

For each minute of the conversation, categorize and tag the content. Use the following categories:
- 💰 pricing/قیمت
- ⚡ features/قابلیت‌ها  
- 🎯 need/نیاز مشتری
- ⚠️ service problems/مشکلات سرویس
- ➡️ next steps/مراحل بعدی

If the content of any minute doesn't fit into any of the above categories, suggest an appropriate category and clearly indicate that this is an LLM suggestion.

**Minute 0-1:** 
- **Tag:** [💰 pricing / ⚡ features / 🎯 need / ⚠️ service problems / ➡️ next steps / 🤖 LLM suggestion: suggested category]
- **Precise Topic Timings**: 
  - **💰 Pricing**: [00:05-00:25] - [Brief description of pricing topic]
  - **⚡ Features**: [00:35-00:58] - [Brief description of features topic]
- **Overall Minute Description:** [Reason for choosing this category]

**Minute 1-2:**
- **Tag:** [💰 pricing / ⚡ features / 🎯 need / ⚠️ service problems / ➡️ next steps / 🤖 LLM suggestion: suggested category]
- **Precise Topic Timings**:
  - **[Topic Type]**: [01:10-01:45] - [Brief description]
  - **[Topic Type]**: [01:45-01:58] - [Brief description]
- **Overall Minute Description:** [Reason for choosing this category]

... continue for all minutes

### 📊 Topic Timing Summary

**💰 Pricing:**
- **Total discussion time**: [X minutes Y seconds]
- **Time ranges**: [00:05-00:25], [02:30-03:15], [05:40-06:10]
- **Summary of points**: [Summary of all pricing points discussed]

**⚡ Features:**
- **Total discussion time**: [X minutes Y seconds]
- **Time ranges**: [00:35-01:20], [03:45-04:30]
- **Summary of points**: [Summary of all feature points discussed]

**🎯 Customer Need:**
- **Total discussion time**: [X minutes Y seconds]
- **Time ranges**: [01:20-02:10], [04:30-05:00]
- **Summary of points**: [Summary of all needs discussed]

**⚠️ Service Problems:**
- **Total discussion time**: [X minutes Y seconds]
- **Time ranges**: [02:10-02:30], [06:10-07:00]
- **Summary of points**: [Summary of all problems discussed]

**➡️ Next Steps:**
- **Total discussion time**: [X minutes Y seconds]
- **Time ranges**: [07:00-07:45]
- **Summary of points**: [Summary of all next steps discussed]

## 3. General Summary

- **Main Topic:** [Complete and detailed description of the topic with all details]
- **Problem or Issue Raised:** [Detailed description of the problem with causes and context]
- **Solutions Provided:** [Complete description of solutions with implementation details]
- **Final Status:** [Resolved/Unresolved/Under Review + complete explanation]
- **Important Notes:** [All notable points with prioritization]
- **Conversation Strengths:** [What went well]
- **Conversation Weaknesses:** [What needs improvement]

## 3.1. Topic Categorization Summary with Timestamps

- **💰 Pricing:** 
  - **Total Time**: [X minutes Y seconds] 
  - **Time Ranges**: [00:05-00:25], [02:30-03:15], [05:40-06:10]
  - **Summary of Points**: [Summary of all pricing points discussed]
  
- **⚡ Features:** 
  - **Total Time**: [X minutes Y seconds]
  - **Time Ranges**: [00:35-01:20], [03:45-04:30] 
  - **Summary of Points**: [Summary of all feature points discussed]
  
- **🎯 Customer Need:** 
  - **Total Time**: [X minutes Y seconds]
  - **Time Ranges**: [01:20-02:10], [04:30-05:00]
  - **Summary of Points**: [Summary of all needs discussed]
  
- **⚠️ Service Problems:** 
  - **Total Time**: [X minutes Y seconds]
  - **Time Ranges**: [02:10-02:30], [06:10-07:00]
  - **Summary of Points**: [Summary of all problems discussed]
  
- **➡️ Next Steps:** 
  - **Total Time**: [X minutes Y seconds]
  - **Time Ranges**: [07:00-07:45]
  - **Summary of Points**: [Summary of all next steps discussed]
  
- **🤖 LLM Suggested Topics:** 
  - **[New Topic Name]**: 
    - **Total Time**: [X minutes Y seconds]
    - **Time Ranges**: [mm:ss-mm:ss]
    - **Summary**: [Topic description and reason for suggestion]

**Overall Categorization Statistics:**
- Dominant conversation topic: [Topic that consumed the most time]
- Topic diversity: [Whether conversation was focused or scattered]
- Unresolved topics: [Topics that need follow-up]

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
- **Exact timing of negative moments:** [mm:ss-mm:ss - description of incident, example: 02:15-02:30 - customer became angry due to delay]
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

Important Note: 
🚨 MANDATORY: Please provide the response in Markdown format and complete all sections with maximum accuracy, detail, and completeness. 
⛔ FORBIDDEN: Avoid any summarization or omission of details.
📝 MANDATORY: Each section must have at least 3-5 lines of explanation.
🔢 MANDATORY: All numbers and statistics must be accurate.
⭐ MANDATORY: All star ratings must have complete justification.
📊 MANDATORY: All calculations (percentages, averages) must be performed.
🎯 MANDATORY: All suggestions must be practical and actionable.

If information is not available to complete a section, explicitly write "Insufficient information available" but try to provide reasonable estimates based on available content.
"""
