"""
Gemini AI Analyzer Service
سرویس تحلیلگر هوش مصنوعی جمینی
"""

import time

import google.generativeai as genai

from src.interfaces import IAIAnalyzer, IConfigurationService, IPromptProvider
from src.models import AnalysisResult, AudioFile


class GeminiAnalyzer(IAIAnalyzer):
    """Analyzes audio files using Google's Gemini AI following Dependency Inversion Principle"""

    def __init__(self, config_service, prompt_provider=None):
        # Handle backward compatibility - if first arg is string, it's api_key
        if isinstance(config_service, str):
            # Legacy constructor: GeminiAnalyzer(api_key, model_name)
            from src.services.configuration_service import ConfigurationService
            from src.services.prompt_provider import PromptProvider

            self._config_service = ConfigurationService(
                api_key=config_service, model_name=prompt_provider
            )
            self._prompt_provider = PromptProvider()
        else:
            # New constructor: GeminiAnalyzer(config_service, prompt_provider)
            self._config_service = config_service
            self._prompt_provider = prompt_provider

        self._client = None
        self._initialize_client()

    def _initialize_client(self) -> None:
        """Initialize the Gemini client"""
        try:
            api_key = self._config_service.get_api_key()
            genai.configure(api_key=api_key)
            self._client = genai
        except Exception as e:
            raise ConnectionError(f"Failed to initialize Gemini client: {str(e)}")

    def analyze_audio(
        self, audio_file: AudioFile, language: str = None
    ) -> AnalysisResult:
        """Analyze an audio file and return the result

        Args:
            audio_file (AudioFile): The audio file to analyze
            language (str, optional): The language of the audio. Defaults to None.
        """
        start_time = time.time()

        try:
            if not self._client:
                raise RuntimeError("Gemini client not initialized")

            print(f"در حال پردازش فایل: {audio_file.file_name}")

            # Upload the audio file
            uploaded_file = self._upload_file(audio_file)

            # Generate content with the prompt
            analysis_text = self._generate_analysis(uploaded_file)

            processing_time = time.time() - start_time

            return AnalysisResult(
                audio_file=audio_file,
                analysis_text=analysis_text,
                success=True,
                processing_time=processing_time,
            )

        except Exception as e:
            processing_time = time.time() - start_time
            error_message = f"خطا در پردازش فایل {audio_file.file_name}: {str(e)}"

            return AnalysisResult(
                audio_file=audio_file,
                analysis_text="",
                success=False,
                error_message=error_message,
                processing_time=processing_time,
            )

    def _upload_file(self, audio_file: AudioFile):
        """Upload audio file to Gemini"""
        try:
            return self._client.upload_file(audio_file.file_path)
        except Exception as e:
            raise RuntimeError(
                f"Failed to upload file {audio_file.file_name}: {str(e)}"
            )

    def _generate_analysis(self, uploaded_file) -> str:
        """Generate analysis using Gemini"""
        try:
            model_name = self._config_service.get_model_name()
            prompt = self._prompt_provider.get_analysis_prompt()

            model = self._client.GenerativeModel(model_name)
            response = model.generate_content([prompt, uploaded_file])

            return response.text
        except Exception as e:
            raise RuntimeError(f"Failed to generate analysis: {str(e)}")

    def test_connection(self) -> bool:
        """Test the connection to Gemini API"""
        try:
            if not self._client:
                return False

            # Try a simple request to test the connection
            model_name = self._config_service.get_model_name()
            model = self._client.GenerativeModel(model_name)
            response = model.generate_content("Test connection")
            return response is not None
        except:
            return False
