"""
Analysis Result Model
مدل نتیجه تحلیل
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from .audio_file import AudioFile


@dataclass
class AnalysisResult:
    """Represents the result of audio analysis"""
    
    audio_file: AudioFile
    analysis_text: str
    success: bool = True
    error_message: Optional[str] = None
    processing_time: Optional[float] = None
    timestamp: Optional[datetime] = None
    output_file_path: Optional[str] = None
    
    def __post_init__(self):
        """Initialize timestamp if not provided"""
        if self.timestamp is None:
            self.timestamp = datetime.now()
    
    @property
    def is_successful(self) -> bool:
        """Check if the analysis was successful"""
        return self.success and self.error_message is None
    
    @property
    def file_name(self) -> str:
        """Get the audio file name"""
        return self.audio_file.file_name
    
    def __str__(self) -> str:
        status = "موفق" if self.is_successful else "ناموفق"
        return f"AnalysisResult(file={self.file_name}, status={status})"
