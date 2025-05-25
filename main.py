"""
Voice to Text Analyzer - Main Application
تحلیلگر صدا به متن - برنامه اصلی

This is a modular and SOLID principles-based voice to text analyzer
using Google's Gemini AI for Persian and English audio analysis.
"""

import os

from dotenv import load_dotenv

from app_factory import ApplicationFactory

# Load environment variables from .env file
load_dotenv()


def main():
    """Main application entry point"""

    # Configuration from environment variables
    API_KEY = os.getenv("GEMINI_API_KEY")
    ASSETS_FOLDER = "assets"
    LANGUAGE = "persian"  # or "english"

    if not API_KEY:
        print("❌ خطا: متغیر محیطی GEMINI_API_KEY تنظیم نشده است")
        print("❌ Error: GEMINI_API_KEY environment variable is not set")
        print("💡 لطفاً فایل .env را ایجاد کرده و کلید API خود را تنظیم کنید")
        print("💡 Please create a .env file and set your API key")
        return

    print("🎤 برنامه تحلیل صدا به متن با Gemini AI")
    print("📋 نسخه مدولار و پیروی از اصول SOLID")
    print("=" * 50)

    try:
        # Create application using dependency injection
        print("🔧 در حال راه‌اندازی سرویس‌ها...")
        app = ApplicationFactory.create_application(api_key=API_KEY, language=LANGUAGE)

        # Validate configuration
        print("🔍 بررسی پیکربندی...")
        if not app.validate_configuration():
            print("❌ پیکربندی نامعتبر است. لطفاً تنظیمات را بررسی کنید.")
            return

        print("✅ پیکربندی معتبر است")

        # Process audio files
        print(f"\n🎯 شروع پردازش فایل‌ها از پوشه: {ASSETS_FOLDER}")
        results = app.process_audio_files(ASSETS_FOLDER)

        # Display final summary
        app.print_final_summary(results)

        print(f"\n🎉 پردازش با موفقیت تکمیل شد!")
        print(f"📁 فایل‌های خروجی در فرمت Markdown در پوشه 'results' ذخیره شدند")

    except KeyboardInterrupt:
        print(f"\n⚠️  پردازش توسط کاربر متوقف شد")
    except Exception as e:
        print(f"\n❌ خطای غیرمنتظره: {str(e)}")
        print(f"💡 لطفاً اتصال اینترنت و API key را بررسی کنید")


def run_with_custom_config():
    """Run with custom configuration - example usage"""

    print("🔧 اجرا با پیکربندی سفارشی...")

    # Create application with custom settings
    app = ApplicationFactory.create_application(
        api_key="YOUR_CUSTOM_API_KEY", model_name="gemini-2.0-flash", language="english"
    )

    # Process files
    results = app.process_audio_files("assets", "custom_results")
    app.print_final_summary(results)


def show_application_info():
    """Show information about the application architecture"""

    print(
        """
🏗️  معماری برنامه (SOLID Principles):

📦 Single Responsibility Principle (SRP):
   • ConfigurationService: مدیریت تنظیمات
   • AudioFileService: عملیات فایل صوتی  
   • GeminiAnalyzer: تحلیل با هوش مصنوعی
   • MarkdownReportGenerator: تولید گزارش
   • PersianPromptProvider: ارائه پرامت فارسی

🔓 Open/Closed Principle (OCP):
   • امکان اضافه کردن تحلیلگرهای جدید
   • پشتیبانی از فرمت‌های گزارش مختلف
   • قابلیت توسعه پرامت‌ها

🔄 Liskov Substitution Principle (LSP):
   • تمام سرویس‌ها قابل جایگزینی
   • پیاده‌سازی Interface های مشترک

🎯 Interface Segregation Principle (ISP):
   • Interface های کوچک و متمرکز
   • جداسازی مسئولیت‌ها

⬇️  Dependency Inversion Principle (DIP):
   • وابستگی به Interface ها
   • Dependency Injection با Factory Pattern

📁 ساختار مدولار:
   src/
   ├── interfaces/     # تعریف رابط‌ها
   ├── models/         # مدل‌های داده
   ├── services/       # سرویس‌های کاربردی
   └── application.py  # هماهنگ‌کننده اصلی

🎨 Design Patterns:
   • Factory Pattern: ساخت اپلیکیشن
   • Strategy Pattern: انتخاب زبان و پرامت
   • Repository Pattern: مدیریت فایل‌ها
    """
    )


if __name__ == "__main__":
    # Show application info
    show_application_info()

    # Run main application
    main()

    print(f"\n" + "=" * 50)
    print(f"💡 برای اجرا با تنظیمات سفارشی از run_with_custom_config() استفاده کنید")
    print(f"🔗 GitHub: https://github.com/your-repo/voice-to-text-analyzer")
    print(f"📧 Support: your-email@example.com")
