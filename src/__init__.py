"""
Voice to Text Analyzer Package
پکیج تحلیلگر صدا به متن
"""

from .application import VoiceToTextApplication
from .models import AnalysisResult, AudioFile
from .services import (
    AudioFileService,
    ConfigurationService,
    EnglishPromptProvider,
    GeminiAnalyzer,
    MarkdownReportGenerator,
    PersianPromptProvider,
)

__version__ = "2.0.0"
__author__ = "Voice to Text Analyzer"
__description__ = "A modular voice to text analyzer using Gemini AI"

__all__ = [
    "VoiceToTextApplication",
    "AudioFile",
    "AnalysisResult",
    "ConfigurationService",
    "PersianPromptProvider",
    "EnglishPromptProvider",
    "AudioFileService",
    "GeminiAnalyzer",
    "MarkdownReportGenerator",
]
