"""
Unit tests for Analysis Result model
تست‌های واحد برای مدل نتیجه تحلیل
"""

import unittest
import sys
import os
from datetime import datetime
from pathlib import Path

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

try:
    from models.analysis_result import AnalysisResult
    from models.audio_file import AudioFile
except ImportError:
    # Fallback for different import paths
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from src.models.analysis_result import AnalysisResult
    from src.models.audio_file import AudioFile


class TestAnalysisResult(unittest.TestCase):
    """Test cases for AnalysisResult model"""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_audio_file = AudioFile(
            file_path=Path("/test/audio.mp3"),
            file_name="audio.mp3",
            format="mp3",
            file_size=1024000,
        )

        self.test_analysis_text = "This is a test analysis of the audio content"
        self.test_processing_time = 5.5
        self.test_timestamp = datetime.now()
        self.test_output_file_path = "/test/output.txt"

        self.analysis_result = AnalysisResult(
            audio_file=self.test_audio_file,
            analysis_text=self.test_analysis_text,
            success=True,
            processing_time=self.test_processing_time,
            timestamp=self.test_timestamp,
            output_file_path=self.test_output_file_path,
        )

    def test_initialization(self):
        """Test AnalysisResult initialization"""
        self.assertEqual(self.analysis_result.audio_file, self.test_audio_file)
        self.assertEqual(self.analysis_result.analysis_text, self.test_analysis_text)
        self.assertTrue(self.analysis_result.success)
        self.assertIsNone(self.analysis_result.error_message)
        self.assertEqual(
            self.analysis_result.processing_time, self.test_processing_time
        )
        self.assertEqual(self.analysis_result.timestamp, self.test_timestamp)
        self.assertEqual(
            self.analysis_result.output_file_path, self.test_output_file_path
        )

    def test_default_values(self):
        """Test AnalysisResult initialization with default values"""
        minimal_result = AnalysisResult(
            audio_file=self.test_audio_file, analysis_text=self.test_analysis_text
        )

        self.assertTrue(minimal_result.success)
        self.assertIsNone(minimal_result.error_message)
        self.assertIsNone(minimal_result.processing_time)
        self.assertIsNotNone(
            minimal_result.timestamp
        )  # Auto-generated in __post_init__
        self.assertIsNone(minimal_result.output_file_path)

    def test_attributes_types(self):
        """Test that all attributes have correct types"""
        self.assertIsInstance(self.analysis_result.audio_file, AudioFile)
        self.assertIsInstance(self.analysis_result.analysis_text, str)
        self.assertIsInstance(self.analysis_result.success, bool)
        self.assertIsInstance(
            self.analysis_result.processing_time, (int, float, type(None))
        )
        self.assertIsInstance(self.analysis_result.timestamp, (datetime, type(None)))
        self.assertIsInstance(self.analysis_result.output_file_path, (str, type(None)))

    def test_is_successful_property(self):
        """Test the is_successful property"""
        # Test successful case
        self.assertTrue(self.analysis_result.is_successful)

        # Test failed case with success=False
        failed_result = AnalysisResult(
            audio_file=self.test_audio_file, analysis_text="", success=False
        )
        self.assertFalse(failed_result.is_successful)

        # Test failed case with error message
        error_result = AnalysisResult(
            audio_file=self.test_audio_file,
            analysis_text="",
            error_message="Processing failed",
        )
        self.assertFalse(error_result.is_successful)

    def test_file_name_property(self):
        """Test the file_name property"""
        self.assertEqual(self.analysis_result.file_name, "audio.mp3")
        self.assertEqual(self.analysis_result.file_name, self.test_audio_file.file_name)

    def test_audio_file_relationship(self):
        """Test the relationship with AudioFile"""
        # The audio file should be accessible
        self.assertEqual(self.analysis_result.audio_file.file_name, "audio.mp3")
        self.assertEqual(self.analysis_result.audio_file.format, "mp3")
        self.assertEqual(self.analysis_result.audio_file.file_size, 1024000)

    def test_str_representation(self):
        """Test string representation"""
        str_repr = str(self.analysis_result)
        self.assertIn("AnalysisResult", str_repr)
        self.assertIn("audio.mp3", str_repr)
        self.assertIn("موفق", str_repr)  # Persian for "successful"

        # Test failed case
        failed_result = AnalysisResult(
            audio_file=self.test_audio_file, analysis_text="", success=False
        )
        failed_str = str(failed_result)
        self.assertIn("ناموفق", failed_str)  # Persian for "failed"

    def test_with_different_processing_times(self):
        """Test with different processing time types"""
        # Test with integer
        result_int = AnalysisResult(
            audio_file=self.test_audio_file, analysis_text="test", processing_time=10
        )
        self.assertIsInstance(result_int.processing_time, int)
        self.assertEqual(result_int.processing_time, 10)

        # Test with float
        result_float = AnalysisResult(
            audio_file=self.test_audio_file, analysis_text="test", processing_time=10.5
        )
        self.assertIsInstance(result_float.processing_time, float)
        self.assertEqual(result_float.processing_time, 10.5)

        # Test with None
        result_none = AnalysisResult(
            audio_file=self.test_audio_file, analysis_text="test"
        )
        self.assertIsNone(result_none.processing_time)

    def test_error_handling(self):
        """Test error handling scenarios"""
        error_result = AnalysisResult(
            audio_file=self.test_audio_file,
            analysis_text="",
            success=False,
            error_message="File processing failed",
        )

        self.assertFalse(error_result.success)
        self.assertEqual(error_result.error_message, "File processing failed")
        self.assertFalse(error_result.is_successful)

    def test_timestamp_auto_generation(self):
        """Test that timestamp is auto-generated if not provided"""
        before_creation = datetime.now()
        result = AnalysisResult(audio_file=self.test_audio_file, analysis_text="test")
        after_creation = datetime.now()

        self.assertIsNotNone(result.timestamp)
        self.assertGreaterEqual(result.timestamp, before_creation)
        self.assertLessEqual(result.timestamp, after_creation)

    def test_python38_compatibility(self):
        """Test Python 3.8 compatibility features"""
        # Test that the model works with Python 3.8 features
        self.assertIsNotNone(self.analysis_result)

        # Test that all attributes are accessible
        attributes = [
            "audio_file",
            "analysis_text",
            "success",
            "error_message",
            "processing_time",
            "timestamp",
            "output_file_path",
        ]
        for attr in attributes:
            self.assertTrue(hasattr(self.analysis_result, attr))

    def test_python38_walrus_operator_with_analysis(self):
        """Test walrus operator with analysis results (Python 3.8 feature)"""
        # Test with successful result
        if (analysis := self.analysis_result.analysis_text) and len(analysis) > 0:
            is_valid = True
        else:
            is_valid = False

        self.assertTrue(is_valid)
        self.assertEqual(analysis, self.test_analysis_text)

        # Test with timestamp
        if (timestamp := self.analysis_result.timestamp) is not None:
            has_timestamp = True
        else:
            has_timestamp = False

        self.assertTrue(has_timestamp)
        self.assertEqual(timestamp, self.test_timestamp)

    def test_python38_exception_chaining(self):
        """Test exception chaining with analysis results"""

        def validate_analysis_result(result):
            try:
                if not result.analysis_text:
                    raise ValueError("Empty analysis text")
                if result.processing_time is not None and result.processing_time < 0:
                    raise ValueError("Invalid processing time")
                return True
            except ValueError as e:
                raise RuntimeError("Analysis validation failed") from e

        # Test with invalid result (empty analysis)
        invalid_result = AnalysisResult(
            audio_file=self.test_audio_file, analysis_text=""
        )

        with self.assertRaises(RuntimeError) as context:
            validate_analysis_result(invalid_result)

        # Verify exception chaining
        self.assertIsNotNone(context.exception.__cause__)
        self.assertIsInstance(context.exception.__cause__, ValueError)
        self.assertIn("Empty analysis text", str(context.exception.__cause__))

    def test_python38_typing_with_metadata(self):
        """Test Python 3.8 typing features with metadata"""
        from typing import Dict, Any, Optional

        def create_analysis_with_metadata(
            audio_file: AudioFile,
            analysis_text: str,
            metadata: Optional[Dict[str, Any]] = None,
        ) -> AnalysisResult:
            """Function with type hints for metadata handling"""
            result = AnalysisResult(
                audio_file=audio_file,
                analysis_text=analysis_text,
                success=True,
                processing_time=1.5,
            )

            # Store metadata as a custom attribute (not part of the dataclass)
            if metadata:
                for key, value in metadata.items():
                    setattr(result, f"meta_{key}", value)

            return result

        # Test function
        metadata = {"source": "test", "version": "1.0", "confidence": 0.95}
        result = create_analysis_with_metadata(
            self.test_audio_file, "Test analysis", metadata
        )

        self.assertEqual(result.analysis_text, "Test analysis")
        self.assertTrue(result.success)
        self.assertEqual(result.processing_time, 1.5)

        # Check metadata attributes
        self.assertEqual(getattr(result, "meta_source"), "test")
        self.assertEqual(getattr(result, "meta_version"), "1.0")
        self.assertEqual(getattr(result, "meta_confidence"), 0.95)


if __name__ == "__main__":
    unittest.main()
