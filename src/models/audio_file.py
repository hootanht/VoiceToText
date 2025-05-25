"""
Audio File Model
مدل فایل صوتی
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class AudioFile:
    """Represents an audio file with its metadata"""
    
    file_path: str
    file_name: str
    file_size: Optional[int] = None
    duration: Optional[float] = None
    format: Optional[str] = None
    
    @property
    def file_extension(self) -> str:
        """Get the file extension (for compatibility)"""
        return self.format.lstrip('.') if self.format else ''
    
    def __post_init__(self):
        """Initialize additional properties after object creation"""
        if not self.file_name:
            self.file_name = Path(self.file_path).name
        
        if not self.format:
            self.format = Path(self.file_path).suffix.lower()
    
    @property
    def stem_name(self) -> str:
        """Get the file name without extension"""
        return Path(self.file_path).stem
    
    @property
    def exists(self) -> bool:
        """Check if the file exists"""
        return Path(self.file_path).exists()
    
    def __str__(self) -> str:
        return f"AudioFile(name={self.file_name}, format={self.format})"
