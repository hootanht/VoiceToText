"""
Audio File Service
سرویس فایل صوتی
"""

import glob
import os
from pathlib import Path
from typing import List, Union

from src.interfaces import IAudioFileService, IConfigurationService
from src.models import AudioFile


class AudioFileService(IAudioFileService):
    """Handles audio file operations following Single Responsibility Principle"""

    def __init__(self, config_service: IConfigurationService):
        self._config_service = config_service

    def find_audio_files(self, folder_path: str) -> List[AudioFile]:
        """Find all audio files in the specified folder and subfolders"""
        if not os.path.exists(folder_path):
            return []

        audio_files = []
        supported_extensions = self._config_service.get_supported_extensions()

        for extension in supported_extensions:
            pattern = os.path.join(folder_path, "**", f"*.{extension}")
            file_paths = glob.glob(pattern, recursive=True)

            for file_path in file_paths:
                audio_file = self._create_audio_file(file_path)
                if audio_file.exists:
                    audio_files.append(audio_file)

        return audio_files

    def _create_audio_file(self, file_path: str) -> AudioFile:
        """Create an AudioFile object with metadata"""
        file_path = os.path.abspath(file_path)
        file_name = Path(file_path).name

        # Get file size
        file_size = None
        try:
            file_size = os.path.getsize(file_path)
        except OSError:
            pass

        # Get file format
        file_format = Path(file_path).suffix.lower().lstrip(".")

        return AudioFile(
            file_path=file_path,
            file_name=file_name,
            file_size=file_size,
            format=file_format,
        )

    def validate_audio_file(self, audio_file: AudioFile) -> bool:
        """Validate if the audio file is supported and accessible"""
        if not audio_file.exists:
            return False

        supported_extensions = self._config_service.get_supported_extensions()
        return audio_file.format in supported_extensions

    def get_files_from_directory(self, directory_path: str) -> List[AudioFile]:
        """Get audio files from a directory (alias for find_audio_files)"""
        return self.find_audio_files(directory_path)

    def validate_file(self, file_path: str) -> bool:
        """Validate a file by its path"""
        try:
            audio_file = self._create_audio_file(file_path)
            return self.validate_audio_file(audio_file)
        except Exception:
            return False

    def get_file_info(self, file_path_or_audio: Union[str, AudioFile]) -> dict:
        """Get detailed information about an audio file"""
        if isinstance(file_path_or_audio, str):
            audio_file = self._create_audio_file(file_path_or_audio)
        else:
            audio_file = file_path_or_audio

        return {
            "path": audio_file.file_path,
            "name": audio_file.file_name,
            "size": audio_file.file_size,
            "format": audio_file.format,
            "exists": audio_file.exists,
            "size_mb": (
                round(audio_file.file_size / (1024 * 1024), 2)
                if audio_file.file_size
                else None
            ),
        }
