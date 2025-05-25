"""
Configuration Service
سرویس پیکربندی
"""

import os
from typing import List
from dotenv import load_dotenv
from ..interfaces import IConfigurationService

# Load environment variables from .env file
load_dotenv()


class ConfigurationService(IConfigurationService):
    """Manages application configuration following Single Responsibility Principle"""
    def __init__(self, api_key: str = None, model_name: str = None):
        self._api_key = api_key or os.getenv('GEMINI_API_KEY')
        self._model_name = model_name or os.getenv('GEMINI_MODEL_NAME', 'gemini-2.0-flash')
        self._supported_extensions = ['mp3', 'wav', 'aiff', 'aac', 'ogg', 'flac']
    
    def get_api_key(self) -> str:
        """Get the Gemini API key"""
        # Return the configured API key (which already checks environment variables)
        return self._api_key
    
    def get_model_name(self) -> str:
        """Get the Gemini model name"""
        return self._model_name
    
    def get_supported_extensions(self) -> List[str]:
        """Get list of supported audio file extensions"""
        return self._supported_extensions.copy()
    
    def set_api_key(self, api_key: str) -> None:
        """Set a new API key"""
        self._api_key = api_key
    
    def set_model_name(self, model_name: str) -> None:
        """Set a new model name"""
        self._model_name = model_name
    
    def add_supported_extension(self, extension: str) -> None:
        """Add a new supported extension"""
        if extension not in self._supported_extensions:
            self._supported_extensions.append(extension)
