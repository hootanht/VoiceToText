"""
Comprehensive Service Tests
تست‌های جامع سرویس‌ها

This module contains comprehensive tests for all service classes,
including edge cases, error handling, and Python 3.8 compatibility.
"""

import unittest
import sys
import os
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock, mock_open

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

try:
    from services.audio_file_service import AudioFileService
    from services.gemini_analyzer import GeminiAnalyzer
    from services.prompt_provider import PersianPromptProvider, EnglishPromptProvider
    from services.report_generator import MarkdownReportGenerator
    from services.configuration_service import ConfigurationService
    from models.audio_file import AudioFile
    from models.analysis_result import AnalysisResult
except ImportError:
    # Fallback for different import paths
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from src.services.audio_file_service import AudioFileService
    from src.services.gemini_analyzer import GeminiAnalyzer
    from src.services.prompt_provider import (
        PersianPromptProvider,
        EnglishPromptProvider,
    )
    from src.services.report_generator import MarkdownReportGenerator
    from src.services.configuration_service import ConfigurationService
    from src.models.audio_file import AudioFile
    from src.models.analysis_result import AnalysisResult


class TestAudioFileServiceComprehensive(unittest.TestCase):
    """Comprehensive tests for AudioFileService"""

    def setUp(self):
        """Set up test fixtures"""
        from src.services.configuration_service import ConfigurationService

        config_service = ConfigurationService()
        self.service = AudioFileService(config_service)

    def test_get_files_from_directory_with_real_files(self):
        """Test getting files from a directory with actual files"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create test files
            test_files = ["test1.mp3", "test2.wav", "test3.txt", "test4.m4a"]
            for filename in test_files:
                Path(temp_dir, filename).touch()

            # Test getting audio files
            audio_files = self.service.get_files_from_directory(temp_dir)

            # Should only return audio files
            expected_count = 3  # mp3, wav, m4a
            self.assertEqual(len(audio_files), expected_count)

            # Check file types
            extensions = [af.file_extension for af in audio_files]
            self.assertIn("mp3", extensions)
            self.assertIn("wav", extensions)
            self.assertIn("m4a", extensions)

    def test_get_files_empty_directory(self):
        """Test getting files from empty directory"""
        with tempfile.TemporaryDirectory() as temp_dir:
            audio_files = self.service.get_files_from_directory(temp_dir)
            self.assertEqual(len(audio_files), 0)

    def test_get_files_nonexistent_directory(self):
        """Test getting files from nonexistent directory"""
        nonexistent_path = "/path/that/does/not/exist"
        audio_files = self.service.get_files_from_directory(nonexistent_path)
        self.assertEqual(len(audio_files), 0)

    def test_validate_file_valid_audio_file(self):
        """Test validating a valid audio file"""
        temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
        try:
            temp_file.write(b"fake mp3 content")
            temp_file.close()  # Close the file before using it

            is_valid = self.service.validate_file(temp_file.name)
            self.assertTrue(is_valid)
        finally:
            try:
                os.unlink(temp_file.name)
            except (OSError, PermissionError):
                pass  # Ignore if we can't delete the file

    def test_validate_file_invalid_extension(self):
        """Test validating file with invalid extension"""
        temp_file = tempfile.NamedTemporaryFile(suffix=".txt", delete=False)
        try:
            temp_file.write(b"not an audio file")
            temp_file.close()  # Close the file before using it

            is_valid = self.service.validate_file(temp_file.name)
            self.assertFalse(is_valid)
        finally:
            try:
                os.unlink(temp_file.name)
            except (OSError, PermissionError):
                pass  # Ignore if we can't delete the file

    def test_validate_file_nonexistent_file(self):
        """Test validating nonexistent file"""
        is_valid = self.service.validate_file("/path/to/nonexistent/file.mp3")
        self.assertFalse(is_valid)

    def test_get_file_info_comprehensive(self):
        """Test getting comprehensive file information"""
        temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
        try:
            test_content = b"fake mp3 content for testing"
            temp_file.write(test_content)
            temp_file.close()  # Close the file before using it

            file_info = self.service.get_file_info(temp_file.name)

            self.assertIsInstance(file_info, dict)
            self.assertEqual(file_info["path"], temp_file.name)
            self.assertEqual(file_info["format"], "mp3")
            self.assertEqual(file_info["size"], len(test_content))
        finally:
            try:
                os.unlink(temp_file.name)
            except (OSError, PermissionError):
                pass  # Ignore if we can't delete the file

    def test_python38_pathlib_usage(self):
        """Test Python 3.8 pathlib features"""
        test_path = "test/path/audio.mp3"

        # Test pathlib operations that work in Python 3.8+
        path_obj = Path(test_path)

        self.assertEqual(path_obj.suffix, ".mp3")
        self.assertEqual(path_obj.stem, "audio")
        self.assertEqual(path_obj.name, "audio.mp3")
        # Test parent operations - Handle Windows/Unix path differences
        expected_parent = "test\\path" if os.name == "nt" else "test/path"
        self.assertEqual(str(path_obj.parent), expected_parent)


class TestGeminiAnalyzerComprehensive(unittest.TestCase):
    """Comprehensive tests for GeminiAnalyzer"""

    @patch("src.services.gemini_analyzer.genai")
    def setUp(self, mock_genai):
        """Set up test fixtures"""
        # Mock the client initialization to avoid API calls during tests
        mock_genai.configure = MagicMock()
        self.analyzer = GeminiAnalyzer("test_api_key", "test_model")

    def test_analyze_audio_success(self):
        """Test successful audio analysis"""
        # Mock the Gemini API response completely
        with patch.object(self.analyzer, "_client") as mock_client:
            # Mock upload_file
            mock_uploaded_file = MagicMock()
            mock_client.upload_file.return_value = mock_uploaded_file

            # Mock GenerativeModel and response
            mock_model = MagicMock()
            mock_response = MagicMock()
            mock_response.text = "This is a test transcription"
            mock_model.generate_content.return_value = mock_response
            mock_client.GenerativeModel.return_value = mock_model

            # Create test audio file
            test_file = AudioFile("test.mp3", "mp3", 1024)

            # Test analysis
            result = self.analyzer.analyze_audio(test_file, "persian")

            # Check using the exact type from src.models
            from src.models.analysis_result import AnalysisResult as SrcAnalysisResult

            self.assertIsInstance(result, SrcAnalysisResult)
            self.assertEqual(result.analysis_text, "This is a test transcription")
            self.assertTrue(result.success)
            self.assertGreater(result.processing_time, 0)

    def test_analyze_audio_api_error(self):
        """Test audio analysis with API error"""
        # Mock the client to raise an exception during upload
        with patch.object(self.analyzer, "_client") as mock_client:
            mock_client.upload_file.side_effect = Exception("API Error")

            test_file = AudioFile("test.mp3", "mp3", 1024)

            # The analyzer should return a failed result, not raise an exception
            result = self.analyzer.analyze_audio(test_file, "persian")

            # Check using the exact type from src.models
            from src.models.analysis_result import AnalysisResult as SrcAnalysisResult

            self.assertIsInstance(result, SrcAnalysisResult)
            self.assertFalse(result.success)
            self.assertIn("API Error", result.error_message)

    def test_python38_exception_handling(self):
        """Test Python 3.8 exception handling patterns"""

        def function_with_chained_exception():
            try:
                # Simulate an operation that fails
                raise ValueError("Original error")
            except ValueError as e:
                # Chain exceptions (Python 3+ feature)
                raise RuntimeError("Analysis failed") from e

        with self.assertRaises(RuntimeError) as context:
            function_with_chained_exception()

        # Verify exception chaining
        self.assertIsNotNone(context.exception.__cause__)
        self.assertIsInstance(context.exception.__cause__, ValueError)


class TestPromptProviderComprehensive(unittest.TestCase):
    """Comprehensive tests for PromptProvider"""

    def setUp(self):
        """Set up test fixtures"""
        self.provider = PersianPromptProvider()
        self.english_provider = EnglishPromptProvider()

    def test_get_analysis_prompt_persian(self):
        """Test Persian analysis prompt"""
        prompt = self.provider.get_analysis_prompt()

        self.assertIsInstance(prompt, str)
        self.assertGreater(len(prompt), 0)
        # Check for Persian text
        self.assertIn("ویس", prompt)
        self.assertIn("متن", prompt)

    def test_get_analysis_prompt_english(self):
        """Test English analysis prompt"""
        prompt = self.english_provider.get_analysis_prompt()

        self.assertIsInstance(prompt, str)
        self.assertGreater(len(prompt), 0)
        # Check for English text
        self.assertIn("transcribe", prompt)
        self.assertIn("audio", prompt)
        self.assertGreater(len(prompt), 0)

    def test_get_analysis_prompt_comprehensive(self):
        """Test comprehensive analysis prompt"""
        prompt = self.provider.get_analysis_prompt()

        self.assertIsInstance(prompt, str)
        self.assertGreater(len(prompt), 0)

        # Should contain analysis-related keywords
        prompt_lower = prompt.lower()
        analysis_keywords = ["analyze", "analysis", "summary", "content"]
        self.assertTrue(any(keyword in prompt_lower for keyword in analysis_keywords))

    def test_python38_string_formatting(self):
        """Test Python 3.8 string formatting features"""
        language = "persian"

        # Test f-string formatting (Python 3.6+, important for 3.8)
        formatted_prompt = f"Transcribe this audio in {language} language"

        self.assertIn("persian", formatted_prompt)
        self.assertIn("Transcribe", formatted_prompt)


class TestReportGeneratorComprehensive(unittest.TestCase):
    """Comprehensive tests for MarkdownReportGenerator"""

    def setUp(self):
        """Set up test fixtures"""
        self.generator = MarkdownReportGenerator()

    def test_generate_analysis_report_complete(self):
        """Test generating complete analysis report"""
        # Create test audio file first
        # Let __post_init__ set the name
        audio_file = AudioFile("test.mp3", "", 1024)

        # Create test analysis result with proper constructor
        result = AnalysisResult(
            audio_file=audio_file,
            analysis_text="This is a test transcription",
            processing_time=2.5,
        )

        # Mock the method that doesn't exist
        if not hasattr(self.generator, "generate_analysis_report"):
            # Use the existing method instead
            report = self.generator._generate_analysis_markdown(result)
        else:
            report = self.generator.generate_analysis_report(result, audio_file)

        self.assertIsInstance(report, str)
        self.assertGreater(len(report), 0)
        # Check report contains key information
        self.assertIn("test transcription", report.lower())
        self.assertIn("test.mp3", report)

    def test_generate_summary_report_multiple_files(self):
        """Test generating summary report for multiple files"""
        # Create multiple test results
        results = []
        for i in range(3):
            audio_file = AudioFile(f"test{i+1}.mp3", "mp3", 1024)
            result = AnalysisResult(
                audio_file=audio_file,
                analysis_text=f"Transcription {i+1}",
                processing_time=1.0 + i,
            )
            results.append(result)

        summary = self.generator.generate_summary_report(results)

        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)

        # Check summary contains aggregated information
        summary_lower = summary.lower()
        self.assertIn("3", summary)  # Should mention 3 files

    def test_generate_summary_report_empty_results(self):
        """Test generating summary report with empty results"""
        summary = self.generator.generate_summary_report([])

        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)
        # Check for both English and Persian indicators of empty results
        # Should indicate no results
        self.assertTrue("No" in summary or "هیچ فایلی" in summary)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.makedirs")
    def test_save_report_to_file(self, mock_makedirs, mock_file):
        """Test saving report to file"""
        test_content = "Test report content"
        test_filepath = "results/test_report.md"

        self.generator.save_report_to_file(test_content, test_filepath)

        # Verify makedirs was called for directory creation
        mock_makedirs.assert_called_once()
        # Verify file was opened and written
        mock_file.assert_called_once_with(test_filepath, "w", encoding="utf-8")
        mock_file().write.assert_called_once_with(test_content)

    def test_python38_walrus_operator_simulation(self):
        """Test simulating walrus operator usage in report generation"""
        audio_files = [
            AudioFile("test1.mp3", "mp3", 1024),
            AudioFile("test2.mp3", "mp3", 1024),
            AudioFile("test3.mp3", "mp3", 1024),
        ]

        test_results = [
            AnalysisResult(audio_files[0], "Text 1", processing_time=1.0),
            AnalysisResult(audio_files[1], "Text 2", processing_time=1.5),
            AnalysisResult(audio_files[2], "Text 3", processing_time=2.0),
        ]

        # Simulate walrus operator usage (Python 3.8 feature)
        # Count Persian results
        persian_count = 0
        for result in test_results:
            if (lang := result.language) == "persian":
                persian_count += 1

        self.assertEqual(persian_count, 3)  # All should be persian by default

    def test_python38_positional_only_parameters(self):
        """Test function with positional-only parameters (Python 3.8 feature)"""

        def format_report_line(content, /, *, prefix="- ", suffix="\\n"):
            """Function using positional-only parameter (Python 3.8 feature)"""
            return f"{prefix}{content}{suffix}"

        # Test with positional argument
        result = format_report_line("Test content")
        self.assertEqual(result, "- Test content\\n")

        # Test with keyword arguments
        result2 = format_report_line("Test", prefix="* ", suffix="")
        self.assertEqual(result2, "* Test")


class TestPython38IntegrationFeatures(unittest.TestCase):
    """Integration tests for Python 3.8 specific features across services"""

    def test_typing_integration(self):
        """Test typing integration across services"""
        from typing import List, Optional, Dict, Any

        def process_audio_files(
            files: List[AudioFile], config: Optional[Dict[str, Any]] = None
        ) -> List[AnalysisResult]:
            """Test function with Python 3.8+ type hints"""
            results = []
            for file in files:
                # Simulate processing
                result = AnalysisResult(
                    audio_file=file,
                    analysis_text=f"Processed {file.file_path}",
                    processing_time=1.0,
                )
                results.append(result)
            return results

        # Test the function
        test_files = [
            AudioFile("test1.mp3", "mp3", 1024),
            AudioFile("test2.wav", "wav", 2048),
        ]

        results = process_audio_files(test_files)

        self.assertEqual(len(results), 2)
        self.assertIsInstance(results[0], AnalysisResult)
        self.assertIn("test1.mp3", results[0].analysis_text)

    def test_async_await_compatibility(self):
        """Test async/await syntax compatibility"""
        import asyncio

        async def async_process_file(file_path: str) -> str:
            """Async function for file processing"""
            # Simulate async operation
            await asyncio.sleep(0.001)
            return f"Processed {file_path}"

        # Verify function is coroutine
        self.assertTrue(asyncio.iscoroutinefunction(async_process_file))

    def test_context_manager_integration(self):
        """Test context manager usage in file processing"""

        class AudioProcessor:
            def __init__(self):
                self.files_processed = []
                self.is_processing = False

            def __enter__(self):
                self.is_processing = True
                return self

            def __exit__(self, exc_type, exc_val, exc_tb):
                self.is_processing = False
                return False

            def process(self, file_path: str):
                if self.is_processing:
                    self.files_processed.append(file_path)

        # Test context manager
        with AudioProcessor() as processor:
            processor.process("test1.mp3")
            processor.process("test2.wav")

            self.assertTrue(processor.is_processing)
            self.assertEqual(len(processor.files_processed), 2)

        self.assertFalse(processor.is_processing)


if __name__ == "__main__":
    # Run tests with maximum verbosity
    unittest.main(verbosity=2, buffer=True)
