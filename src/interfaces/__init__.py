"""
Interfaces for the Voice to Text Analyzer
رابط‌های کاربری برای تحلیلگر صدا به متن
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from src.models.audio_file import AudioFile
from src.models.analysis_result import AnalysisResult


class IAudioFileService(ABC):
    """Interface for audio file operations"""

    @abstractmethod
    def find_audio_files(self, folder_path: str) -> List[AudioFile]:
        """Find all audio files in the specified folder"""
        pass


class IAIAnalyzer(ABC):
    """Interface for AI analysis operations"""

    @abstractmethod
    def analyze_audio(self, audio_file: AudioFile) -> AnalysisResult:
        """Analyze an audio file and return the result"""
        pass


class IReportGenerator(ABC):
    """Interface for report generation"""

    @abstractmethod
    def save_analysis_result(self, result: AnalysisResult, output_folder: str) -> str:
        """Save analysis result to a file"""
        pass

    @abstractmethod
    def create_summary_report(
        self, results: List[AnalysisResult], output_folder: str
    ) -> str:
        """Create a summary report of all results"""
        pass


class IPromptProvider(ABC):
    """Interface for prompt provision"""

    @abstractmethod
    def get_analysis_prompt(self) -> str:
        """Get the prompt for audio analysis"""
        pass


class IConfigurationService(ABC):
    """Interface for configuration management"""

    @abstractmethod
    def get_api_key(self) -> str:
        """Get the API key"""
        pass

    @abstractmethod
    def get_model_name(self) -> str:
        """Get the model name"""
        pass

    @abstractmethod
    def get_supported_extensions(self) -> List[str]:
        """Get supported file extensions"""
        pass
