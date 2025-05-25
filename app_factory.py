"""
Dependency Injection Factory
کارخانه تزریق وابستگی
"""

from src.application import VoiceToTextApplication
from src.services.configuration_service import ConfigurationService
from src.services.prompt_provider import PersianPromptProvider
from src.services.audio_file_service import AudioFileService
from src.services.gemini_analyzer import GeminiAnalyzer
from src.services.report_generator import MarkdownReportGenerator


class ApplicationFactory:
    """Factory class for creating the application with proper dependency injection"""
    
    @staticmethod
    def create_application(
        api_key: str = None,
        model_name: str = None,
        language: str = "persian"
    ) -> VoiceToTextApplication:
        """
        Create a fully configured VoiceToTextApplication instance
        
        Args:
            api_key: Gemini API key (optional, will use default if not provided)
            model_name: Gemini model name (optional, will use default if not provided)
            language: Language for prompts ("persian" or "english")
        
        Returns:
            VoiceToTextApplication: Configured application instance
        """
        
        # Create configuration service
        config_service = ConfigurationService(api_key=api_key, model_name=model_name)
          # Create prompt provider based on language
        if language.lower() == "english":
            from src.services.prompt_provider import EnglishPromptProvider
            prompt_provider = EnglishPromptProvider()
        else:
            prompt_provider = PersianPromptProvider()
        
        # Create services with dependency injection
        audio_service = AudioFileService(config_service)
        ai_analyzer = GeminiAnalyzer(config_service, prompt_provider)
        report_generator = MarkdownReportGenerator()
        
        # Create and return the application
        return VoiceToTextApplication(
            audio_service=audio_service,
            ai_analyzer=ai_analyzer,
            report_generator=report_generator,
            config_service=config_service
        )
    
    @staticmethod
    def create_persian_application(api_key: str = None) -> VoiceToTextApplication:
        """Create application with Persian language support"""
        return ApplicationFactory.create_application(
            api_key=api_key, 
            language="persian"
        )
    
    @staticmethod
    def create_english_application(api_key: str = None) -> VoiceToTextApplication:
        """Create application with English language support"""
        return ApplicationFactory.create_application(
            api_key=api_key, 
            language="english"
        )
