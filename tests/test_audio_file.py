"""
Test cases for AudioFile model
"""

import unittest
import sys
import os

# Add the src directory to the path for importing modules
try:
    from src.models.audio_file import AudioFile
except ImportError:
    # Fallback for different import paths
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from src.models.audio_file import AudioFile


class TestAudioFile(unittest.TestCase):
    """Test cases for AudioFile model"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_file_path = "/test/path/audio.mp3"
        self.test_file_name = "audio.mp3"
        self.test_format = "mp3"
        self.test_file_size = 1024000
        
        self.audio_file = AudioFile(
            file_path=self.test_file_path,
            file_name=self.test_file_name,
            format=self.test_format,
            file_size=self.test_file_size
        )
    
    def test_initialization(self):
        """Test AudioFile initialization"""
        self.assertEqual(self.audio_file.file_path, self.test_file_path)
        self.assertEqual(self.audio_file.file_name, self.test_file_name)
        self.assertEqual(self.audio_file.format, self.test_format)
        self.assertEqual(self.audio_file.file_size, self.test_file_size)
    
    def test_attributes_types(self):
        """Test that attributes have correct types"""
        self.assertIsInstance(self.audio_file.file_path, str)
        self.assertIsInstance(self.audio_file.file_name, str)
        self.assertIsInstance(self.audio_file.format, str)
        self.assertIsInstance(self.audio_file.file_size, int)
        self.assertIsInstance(self.audio_file.stem_name, str)
    
    def test_different_formats(self):
        """Test AudioFile with different audio formats"""
        formats = ['wav', 'aiff', 'aac', 'ogg', 'flac']
        
        for fmt in formats:
            audio_file = AudioFile(
                file_path=f"/test/audio.{fmt}",
                file_name=f"audio.{fmt}",
                format=fmt,
                file_size=2048000
            )
            self.assertEqual(audio_file.format, fmt)
            self.assertEqual(audio_file.stem_name, "audio")
    
    def test_python38_compatibility(self):
        """Test Python 3.8 compatibility features with AudioFile"""
        # Test that dataclass works with Python 3.8
        self.assertTrue(hasattr(self.audio_file, '__dataclass_fields__'))
        
        # Test string representation
        str_repr = str(self.audio_file)
        self.assertIn("AudioFile", str_repr)
        self.assertIn("mp3", str_repr)
    
    def test_python38_dataclass_like_behavior(self):
        """Test Python 3.8 dataclass-like behavior"""
        # Test that the object has the expected attributes
        expected_fields = ['file_path', 'file_name', 'file_size', 'duration', 'format']
        
        for field in expected_fields:
            self.assertTrue(hasattr(self.audio_file, field))
    
    def test_python38_pathlib_features(self):
        """Test Python 3.8 pathlib features with AudioFile"""
        from pathlib import Path
        
        # Test pathlib with various audio file extensions
        test_paths = [
            "audio/persian/speech.mp3",
            "audio/english/speech.wav", 
            "audio/mixed/speech.m4a"
        ]
        
        for path_str in test_paths:
            path = Path(path_str)
            audio_file = AudioFile(
                file_path=str(path),
                file_name=path.name,
                format=path.suffix[1:],
                file_size=1024
            )
            
            self.assertEqual(audio_file.format, path.suffix[1:])
            self.assertEqual(audio_file.stem_name, path.stem)
    
    def test_python38_string_methods(self):
        """Test Python 3.8 string methods with file paths"""
        # Test with Persian characters in file path
        persian_path = "صوت/فارسی/test.mp3"
        
        audio_file = AudioFile(
            file_path=persian_path,
            file_name="test.mp3",
            format="mp3",
            file_size=1024
        )
        
        # Test string operations work with Unicode
        self.assertTrue(audio_file.file_path.endswith(".mp3"))
        self.assertEqual(len(audio_file.format), 3)
        
        # Test stem_name property works with Persian paths
        self.assertEqual(audio_file.stem_name, "test")


if __name__ == '__main__':
    unittest.main()
