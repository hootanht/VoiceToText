"""
Analysis Result Model
مدل نتیجه تحلیل
"""

from datetime import datetime
from typing import Optional
from .audio_file import AudioFile


class AnalysisResult:
    """Represents the result of audio analysis"""
    
    audio_file: AudioFile
    analysis_text: str
    success: bool = True
    error_message: Optional[str] = None
    processing_time: Optional[float] = None
    timestamp: Optional[datetime] = None
    output_file_path: Optional[str] = None
    
    def __init__(self, audio_file=None, analysis_text=None, success=True, error_message=None, 
                 processing_time=None, timestamp=None, output_file_path=None,
                 transcription=None, language=None, confidence_score=None, **kwargs):
        """Initialize AnalysisResult with backward compatibility"""
        # Handle both old and new parameter styles
        if transcription is not None and analysis_text is None:
            analysis_text = transcription
        
        # Handle case where first parameter is transcription for compatibility
        if isinstance(audio_file, str) and analysis_text is None:
            # Legacy constructor: AnalysisResult("transcription", "language", confidence, time)
            analysis_text = audio_file
            audio_file = None
            
        self.audio_file = audio_file
        self.analysis_text = analysis_text or ""
        self.success = success
        self.error_message = error_message
        self.processing_time = processing_time
        self.timestamp = timestamp
        self.output_file_path = output_file_path
          # Store compatibility values
        self._language = language or "persian"
        self._confidence_score = confidence_score or 0.95
        
        # Call post_init to handle timestamp
        self.__post_init__()
    
    # Compatibility properties
    @property
    def transcription(self) -> str:
        """Get the transcription (alias for analysis_text)"""
        return self.analysis_text
    
    @property
    def language(self) -> str:
        """Get the detected language (default to persian for compatibility)"""
        return getattr(self, '_language', 'persian')
    
    @property
    def confidence_score(self) -> float:
        """Get confidence score (default to 0.95 for compatibility)"""
        return getattr(self, '_confidence_score', 0.95)
    
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
