"""
Voice to Text Application
اپلیکیشن تبدیل صدا به متن
"""

import os
from typing import List, Optional
from src.interfaces import IAudioFileService, IAIAnalyzer, IReportGenerator, IConfigurationService
from src.models import AudioFile, AnalysisResult


class VoiceToTextApplication:
    """Main application class following Dependency Inversion Principle"""
    
    def __init__(
        self,
        audio_service: IAudioFileService,
        ai_analyzer: IAIAnalyzer,
        report_generator: IReportGenerator,
        config_service: IConfigurationService
    ):
        self._audio_service = audio_service
        self._ai_analyzer = ai_analyzer
        self._report_generator = report_generator
        self._config_service = config_service
    
    def process_audio_files(
        self, 
        assets_folder: str, 
        output_folder: str = "results"
    ) -> List[AnalysisResult]:
        """Process all audio files in the assets folder"""
        
        voice_folder = os.path.join(assets_folder, "voice")
        
        if not os.path.exists(voice_folder):
            print(f"❌ پوشه صدا پیدا نشد: {voice_folder}")
            return []
        
        # Find audio files
        audio_files = self._audio_service.find_audio_files(voice_folder)
        
        if not audio_files:
            print("❌ هیچ فایل صوتی در پوشه پیدا نشد!")
            return []
        
        print(f"🔍 تعداد {len(audio_files)} فایل صوتی پیدا شد:")
        for audio_file in audio_files:
            print(f"  📄 {audio_file.file_name}")
        
        print(f"\n🚀 شروع پردازش فایل‌ها...")
        
        # Process each file
        results = []
        for i, audio_file in enumerate(audio_files, 1):
            print(f"\n📊 پردازش فایل {i}/{len(audio_files)}")
            
            try:
                # Analyze the audio file
                result = self._ai_analyzer.analyze_audio(audio_file)
                
                if result.is_successful:
                    # Save the result
                    self._report_generator.save_analysis_result(result, output_folder)
                    print(f"✅ {audio_file.file_name} با موفقیت پردازش شد")
                else:
                    print(f"❌ خطا در پردازش {audio_file.file_name}")
                    print(f"   {result.error_message}")
                
                results.append(result)
                
            except Exception as e:
                error_result = AnalysisResult(
                    audio_file=audio_file,
                    analysis_text="",
                    success=False,
                    error_message=f"خطای غیرمنتظره: {str(e)}"
                )
                results.append(error_result)
                print(f"❌ خطای غیرمنتظره در پردازش {audio_file.file_name}: {str(e)}")
        
        # Create summary report
        if results:
            self._report_generator.create_summary_report(results, output_folder)
        
        return results
    
    def get_processing_summary(self, results: List[AnalysisResult]) -> dict:
        """Get a summary of processing results"""
        successful = [r for r in results if r.is_successful]
        failed = [r for r in results if not r.is_successful]
        
        total_time = sum(r.processing_time for r in results if r.processing_time)
        avg_time = total_time / len(results) if results else 0
        
        return {
            'total_files': len(results),
            'successful': len(successful),
            'failed': len(failed),
            'success_rate': len(successful) / len(results) * 100 if results else 0,
            'total_processing_time': total_time,
            'average_processing_time': avg_time
        }
    
    def print_final_summary(self, results: List[AnalysisResult]) -> None:
        """Print a final summary of the processing"""
        if not results:
            print("\n📋 هیچ فایلی برای پردازش پیدا نشد.")
            return
        
        summary = self.get_processing_summary(results)
        
        print(f"\n📋 خلاصه نهایی:")
        print(f"   📁 تعداد کل فایل‌ها: {summary['total_files']}")
        print(f"   ✅ فایل‌های موفق: {summary['successful']}")
        print(f"   ❌ فایل‌های ناموفق: {summary['failed']}")
        print(f"   📊 نرخ موفقیت: {summary['success_rate']:.1f}%")
        print(f"   ⏱️  زمان کل پردازش: {summary['total_processing_time']:.2f} ثانیه")
        print(f"   📈 میانگین زمان پردازش: {summary['average_processing_time']:.2f} ثانیه")
        print(f"\n📂 نتایج در پوشه 'results' ذخیره شدند (فرمت Markdown)")
    
    def validate_configuration(self) -> bool:
        """Validate the application configuration"""
        try:
            api_key = self._config_service.get_api_key()
            if not api_key or api_key == "YOUR_API_KEY_HERE":
                print("❌ API Key معتبر تنظیم نشده است")
                return False
            
            model_name = self._config_service.get_model_name()
            if not model_name:
                print("❌ نام مدل تنظیم نشده است")
                return False
            
            return True
            
        except Exception as e:
            print(f"❌ خطا در اعتبارسنجی پیکربندی: {str(e)}")
            return False
