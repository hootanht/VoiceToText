"""
Python 3.8 Compatibility Tests
تست‌های سازگاری با پایتون ۳.۸

This module tests features that are specific to Python 3.8 compatibility,
including type hints, walrus operator usage, positional-only parameters,
and other language features.
"""

import unittest
import sys
import os
from unittest.mock import patch, MagicMock

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from services.configuration_service import ConfigurationService
    from services.audio_file_service import AudioFileService
    from models.audio_file import AudioFile
    from models.analysis_result import AnalysisResult
except ImportError:
    # Fallback for different import paths
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from src.services.configuration_service import ConfigurationService
    from src.services.audio_file_service import AudioFileService
    from src.models.audio_file import AudioFile
    from src.models.analysis_result import AnalysisResult


class TestPython38Compatibility(unittest.TestCase):
    """Test cases for Python 3.8 compatibility features"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.config_service = ConfigurationService(api_key="test_key", model_name="test_model")
        self.file_service = AudioFileService(self.config_service)
    
    def test_type_hints_work(self):
        """Test that type hints are properly handled in Python 3.8+"""
        from typing import List, Optional, Dict, Any
        
        # Test that we can import and use modern type hints
        def test_function(items: List[str], config: Optional[Dict[str, Any]] = None) -> bool:
            return len(items) > 0 and (config is None or isinstance(config, dict))
        
        result = test_function(["test"], {"key": "value"})
        self.assertTrue(result)
        
        result2 = test_function([], None)
        self.assertFalse(result2)
    
    def test_f_string_support(self):
        """Test f-string formatting (Python 3.6+ feature, but important for 3.8)"""
        name = "test"
        version = "3.8"
        
        formatted = f"Testing {name} with Python {version}"
        expected = "Testing test with Python 3.8"
        
        self.assertEqual(formatted, expected)
    
    def test_dict_merge_operator_fallback(self):
        """Test dict merge functionality (3.9+ has |= operator, test fallback for 3.8)"""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        
        # Python 3.8 compatible dict merge
        merged = {**dict1, **dict2}
        expected = {"a": 1, "b": 2, "c": 3, "d": 4}
        
        self.assertEqual(merged, expected)
    
    def test_positional_only_parameters_simulation(self):
        """Test simulation of positional-only parameters (3.8 feature)"""
        
        def process_file(file_path, /, *, encoding="utf-8", errors="strict"):
            """
            Function using positional-only parameters (/) 
            This is a Python 3.8 feature
            """
            return {
                "path": file_path,
                "encoding": encoding,
                "errors": errors
            }
        
        # Should work with positional argument
        result = process_file("test.txt", encoding="utf-8")
        self.assertEqual(result["path"], "test.txt")
        self.assertEqual(result["encoding"], "utf-8")
        
        # Should work with keyword-only arguments
        result2 = process_file("test2.txt", errors="ignore")
        self.assertEqual(result2["path"], "test2.txt")
        self.assertEqual(result2["errors"], "ignore")
    
    def test_walrus_operator_usage(self):
        """Test walrus operator := (Python 3.8 feature)"""
        
        # Test walrus operator in list comprehension
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        # Using walrus operator to avoid calling len() multiple times
        if (n := len(data)) > 5:
            result = f"Data has {n} items"
        else:
            result = "Data is small"
        
        self.assertEqual(result, "Data has 10 items")
          # Test walrus operator in while loop simulation
        test_values = ["", "test", "", "another", ""]
        results = []
        
        for val in test_values:
            if cleaned := val.strip():
                results.append(cleaned)
        
        self.assertEqual(results, ["test", "another"])
    
    def test_dataclass_compatibility(self):
        """Test that our models work with dataclass-like patterns"""
        # Test AudioFile model
        audio_file = AudioFile("test.mp3", "mp3", 1024)
        
        self.assertEqual(audio_file.file_path, "test.mp3")
        self.assertEqual(audio_file.file_extension, "mp3")
        self.assertEqual(audio_file.file_size, 1024)
        
        # Test AnalysisResult model
        result = AnalysisResult(
            audio_file=audio_file,
            analysis_text="test transcription",
            processing_time=1.5
        )
        
        self.assertEqual(result.transcription, "test transcription")
        self.assertEqual(result.language, "persian")
        self.assertAlmostEqual(result.confidence_score, 0.95)
        self.assertAlmostEqual(result.processing_time, 1.5)
    
    def test_pathlib_compatibility(self):
        """Test pathlib usage (important for cross-platform file handling)"""
        from pathlib import Path
        
        # Test pathlib operations
        test_path = Path("assets") / "voice" / "test.mp3"
        
        self.assertEqual(test_path.suffix, ".mp3")
        self.assertEqual(test_path.stem, "test")
        self.assertEqual(test_path.name, "test.mp3")
    
    def test_async_compatibility_check(self):
        """Test that async/await syntax is available (Python 3.5+, but verify for 3.8)"""
        import asyncio
        
        async def async_function():
            await asyncio.sleep(0.001)  # Very short sleep
            return "async works"
        
        # Test async function can be defined and would work
        # (We don't actually run it in unittest, just verify syntax works)
        self.assertTrue(asyncio.iscoroutinefunction(async_function))
    
    def test_exception_chaining(self):
        """Test exception chaining with 'raise ... from ...' (Python 3+ feature)"""
        
        def function_that_raises():
            try:
                1 / 0
            except ZeroDivisionError as e:
                raise ValueError("Cannot process zero division") from e
        
        with self.assertRaises(ValueError) as context:
            function_that_raises()
        
        # Verify exception chaining
        self.assertIsNotNone(context.exception.__cause__)
        self.assertIsInstance(context.exception.__cause__, ZeroDivisionError)
    
    def test_context_manager_compatibility(self):
        """Test context manager usage"""
        
        class TestContextManager:
            def __init__(self):
                self.entered = False
                self.exited = False
            
            def __enter__(self):
                self.entered = True
                return self
            
            def __exit__(self, exc_type, exc_val, exc_tb):
                self.exited = True
                return False
        
        # Test context manager
        with TestContextManager() as cm:
            self.assertTrue(cm.entered)
            self.assertFalse(cm.exited)
        
        self.assertTrue(cm.exited)
    
    def test_generator_expressions(self):
        """Test generator expressions and yield"""
        
        def fibonacci_generator(n):
            a, b = 0, 1
            for _ in range(n):
                yield a
                a, b = b, a + b
        
        # Test generator
        fib_gen = fibonacci_generator(5)
        fib_list = list(fib_gen)
        
        self.assertEqual(fib_list, [0, 1, 1, 2, 3])
    
    def test_unicode_and_string_handling(self):
        """Test unicode and string handling for Persian text"""
        
        # Test Persian text handling
        persian_text = "سلام دنیا"
        english_text = "Hello World"
        
        # Test string operations
        self.assertTrue(persian_text.strip())
        self.assertEqual(len(persian_text), 9)  # 9 characters including space
        
        # Test encoding/decoding
        encoded = persian_text.encode('utf-8')
        decoded = encoded.decode('utf-8')
        
        self.assertEqual(persian_text, decoded)
    
    @patch.dict(os.environ, {'TEST_VAR': 'test_value'})
    def test_environment_variable_handling(self):
        """Test environment variable handling"""
        
        # Test os.environ usage
        test_value = os.environ.get('TEST_VAR')
        self.assertEqual(test_value, 'test_value')
        
        # Test default values
        missing_value = os.environ.get('MISSING_VAR', 'default')
        self.assertEqual(missing_value, 'default')


class TestPython38SpecificFeatures(unittest.TestCase):
    """Test specific Python 3.8 features that might affect our application"""
    
    def test_python_version_check(self):
        """Verify we're testing with appropriate Python version"""
        major, minor = sys.version_info[:2]
        
        # Should be Python 3.8 or higher
        self.assertGreaterEqual(major, 3)
        if major == 3:
            self.assertGreaterEqual(minor, 8)
    
    def test_importlib_metadata_availability(self):
        """Test importlib.metadata availability (Python 3.8+)"""
        try:
            import importlib.metadata as metadata
            # Try to get version of a standard library package
            # This should work in Python 3.8+
            self.assertTrue(hasattr(metadata, 'version'))
        except ImportError:
            # Fall back to importlib_metadata for older versions
            try:
                import importlib_metadata as metadata
                self.assertTrue(hasattr(metadata, 'version'))
            except ImportError:
                self.skipTest("Neither importlib.metadata nor importlib_metadata available")
    
    def test_math_functions_38(self):
        """Test math functions available in Python 3.8"""
        import math
        
        # Test math.isqrt (added in Python 3.8)
        if hasattr(math, 'isqrt'):
            self.assertEqual(math.isqrt(16), 4)
            self.assertEqual(math.isqrt(15), 3)
        
        # Test math.prod (added in Python 3.8)
        if hasattr(math, 'prod'):
            self.assertEqual(math.prod([1, 2, 3, 4]), 24)
            self.assertEqual(math.prod([]), 1)
    
    def test_typing_extensions_compatibility(self):
        """Test typing extensions that might be needed"""
        from typing import Union, Optional, List, Dict
        
        # Test Union types
        def process_input(value: Union[str, int]) -> str:
            return str(value)
        
        result1 = process_input("test")
        result2 = process_input(42)
        
        self.assertEqual(result1, "test")
        self.assertEqual(result2, "42")
        
        # Test Optional
        def get_config(key: str) -> Optional[str]:
            configs = {"key1": "value1"}
            return configs.get(key)
        
        self.assertEqual(get_config("key1"), "value1")
        self.assertIsNone(get_config("missing"))


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
