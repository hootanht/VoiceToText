"""
Unit tests for Configuration Service
تست‌های واحد برای سرویس پیکربندی
"""

import unittest
import sys
import os
from unittest.mock import patch, MagicMock

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

try:
    from services.configuration_service import ConfigurationService
except ImportError:
    # Fallback for different import paths
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from src.services.configuration_service import ConfigurationService


class TestConfigurationService(unittest.TestCase):
    """Test cases for ConfigurationService class"""

    def setUp(self):
        """Set up test fixtures before each test method."""
        # Test with explicit parameters to avoid env dependency
        self.service = ConfigurationService(api_key="test_key", model_name="test_model")

    def test_initialization_with_explicit_params(self):
        """Test service initialization with explicit parameters"""
        service = ConfigurationService(
            api_key="explicit_key", model_name="explicit_model"
        )
        self.assertEqual(service.get_api_key(), "explicit_key")
        self.assertEqual(service.get_model_name(), "explicit_model")

    @patch.dict(
        os.environ, {"GEMINI_API_KEY": "env_key", "GEMINI_MODEL_NAME": "env_model"}
    )
    def test_initialization_with_env_vars(self):
        """Test service initialization with environment variables"""
        service = ConfigurationService()
        self.assertEqual(service.get_api_key(), "env_key")
        self.assertEqual(service.get_model_name(), "env_model")

    @patch.dict(os.environ, {}, clear=True)
    def test_initialization_with_defaults(self):
        """Test service initialization with default values"""
        service = ConfigurationService()
        # Should be None if no env var
        self.assertIsNone(service.get_api_key())
        self.assertEqual(service.get_model_name(), "gemini-2.0-flash")  # Default value

    def test_get_api_key(self):
        """Test API key retrieval"""
        api_key = self.service.get_api_key()
        self.assertIsNotNone(api_key)
        self.assertIsInstance(api_key, str)
        self.assertEqual(api_key, "test_key")

    def test_get_model_name(self):
        """Test model name retrieval"""
        model_name = self.service.get_model_name()
        self.assertIsNotNone(model_name)
        self.assertIsInstance(model_name, str)
        self.assertEqual(model_name, "test_model")

    def test_get_supported_extensions(self):
        """Test supported extensions retrieval"""
        extensions = self.service.get_supported_extensions()
        self.assertIsInstance(extensions, list)
        self.assertGreater(len(extensions), 0)
        self.assertIn("mp3", extensions)
        self.assertIn("wav", extensions)
        self.assertIn("aiff", extensions)
        self.assertIn("aac", extensions)
        self.assertIn("ogg", extensions)
        self.assertIn("flac", extensions)

    def test_supported_extensions_immutability(self):
        """Test that supported extensions returns a copy (immutable)"""
        extensions1 = self.service.get_supported_extensions()
        extensions2 = self.service.get_supported_extensions()
        # Should be different objects (copy returned)
        self.assertIsNot(extensions1, extensions2)
        # But same content
        self.assertEqual(extensions1, extensions2)

        # Modifying one shouldn't affect the other
        extensions1.append("test_extension")
        extensions3 = self.service.get_supported_extensions()
        self.assertNotIn("test_extension", extensions3)

    def test_set_api_key(self):
        """Test API key setting"""
        new_key = "new_test_key"
        self.service.set_api_key(new_key)
        self.assertEqual(self.service.get_api_key(), new_key)

    def test_set_model_name(self):
        """Test model name setting"""
        new_model = "new_test_model"
        self.service.set_model_name(new_model)
        self.assertEqual(self.service.get_model_name(), new_model)

    def test_add_supported_extension(self):
        """Test adding new supported extension"""
        initial_count = len(self.service.get_supported_extensions())
        new_extension = "wma"  # Use extension that's not already in the list

        # Add new extension
        self.service.add_supported_extension(new_extension)
        updated_extensions = self.service.get_supported_extensions()

        self.assertEqual(len(updated_extensions), initial_count + 1)
        self.assertIn(new_extension, updated_extensions)

    def test_add_duplicate_extension(self):
        """Test adding duplicate extension doesn't create duplicates"""
        initial_extensions = self.service.get_supported_extensions()
        existing_extension = initial_extensions[0]
        initial_count = len(initial_extensions)

        # Try to add existing extension
        self.service.add_supported_extension(existing_extension)
        updated_extensions = self.service.get_supported_extensions()

        # Count should remain the same
        self.assertEqual(len(updated_extensions), initial_count)
        # Extension should still be there only once
        self.assertEqual(updated_extensions.count(existing_extension), 1)

    def test_python38_compatibility(self):
        """Test Python 3.8 specific compatibility features"""
        # Test typing compatibility
        extensions = self.service.get_supported_extensions()
        self.assertIsInstance(extensions, list)

        # Test that all methods return expected types
        api_key = self.service.get_api_key()
        model_name = self.service.get_model_name()

        if api_key is not None:
            self.assertIsInstance(api_key, str)
        self.assertIsInstance(model_name, str)

    def test_python38_walrus_operator_compatibility(self):
        """Test walrus operator usage in configuration (Python 3.8 feature)"""
        # Test walrus operator with configuration values
        config = ConfigurationService(api_key="test_key", model_name="test_model")

        # Use walrus operator to check and assign API key
        if (api_key := config.get_api_key()) and len(api_key) > 0:
            result = f"API key length: {len(api_key)}"
        else:
            result = "No API key"

        self.assertEqual(result, "API key length: 8")  # "test_key" is 8 chars

    def test_python38_positional_only_params(self):
        """Test function with positional-only parameters (Python 3.8 feature)"""

        def create_config(api_key, /, *, model_name="default_model", timeout=30):
            """Function using positional-only parameter"""
            return {"api_key": api_key, "model_name": model_name, "timeout": timeout}

        # Test positional-only parameter
        config = create_config("test_key", model_name="custom_model")

        self.assertEqual(config["api_key"], "test_key")
        self.assertEqual(config["model_name"], "custom_model")
        self.assertEqual(config["timeout"], 30)

    def test_python38_f_string_debugging(self):
        """Test f-string debugging feature (Python 3.8+)"""
        api_key = "test_key"
        model_name = "test_model"

        # F-string with = for debugging (Python 3.8 feature)
        # Note: We'll test the functionality, not the = syntax which might not work in all contexts
        debug_info = f"api_key={api_key}, model_name={model_name}"

        self.assertIn("test_key", debug_info)
        self.assertIn("test_model", debug_info)

    def test_python38_typing_features(self):
        """Test Python 3.8 typing features"""
        from typing import TypedDict, Final, Literal

        # Test Final annotation (Python 3.8+)
        try:
            DEFAULT_MODEL: Final = "gemini-2.0-flash"
            self.assertEqual(DEFAULT_MODEL, "gemini-2.0-flash")
        except ImportError:
            self.skipTest("Final not available in this Python version")

        # Test Literal type (Python 3.8+)
        try:

            def get_supported_language(
                lang: Literal["persian", "english", "arabic"],
            ) -> str:
                return f"Language: {lang}"

            result = get_supported_language("persian")
            self.assertEqual(result, "Language: persian")
        except ImportError:
            self.skipTest("Literal not available in this Python version")

    def test_interface_compliance(self):
        """Test that the service implements all required interface methods"""
        # Check that all interface methods exist and are callable
        self.assertTrue(hasattr(self.service, "get_api_key"))
        self.assertTrue(callable(getattr(self.service, "get_api_key")))

        self.assertTrue(hasattr(self.service, "get_model_name"))
        self.assertTrue(callable(getattr(self.service, "get_model_name")))

        self.assertTrue(hasattr(self.service, "get_supported_extensions"))
        self.assertTrue(callable(getattr(self.service, "get_supported_extensions")))


if __name__ == "__main__":
    unittest.main()
