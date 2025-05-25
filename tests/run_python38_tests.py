"""
Python 3.8 Compatibility Test Runner
اجرا کننده تست سازگاری پایتون ۳.۸

This script runs all tests and specifically checks for Python 3.8 compatibility features.
It also provides detailed reporting on which Python 3.8 features are working.
"""

import importlib
import os
import sys
import unittest
from pathlib import Path


def check_python_version():
    """Check if we're running on Python 3.8 or higher"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"⚠️  Warning: Running on Python {version.major}.{version.minor}")
        print("   Some tests may not work as expected. Python 3.8+ recommended.")
        return False
    print(f"✅ Running on Python {version.major}.{version.minor}.{version.micro}")
    return True


def check_python38_features():
    """Check availability of Python 3.8 specific features"""
    print("\\n🔍 Checking Python 3.8 Features:")

    features = {}

    # Test walrus operator
    try:
        exec("if (x := 5) > 0: pass")
        features["walrus_operator"] = True
        print("  ✅ Walrus operator (:=) - Available")
    except SyntaxError:
        features["walrus_operator"] = False
        print("  ❌ Walrus operator (:=) - Not available")

    # Test positional-only parameters
    try:
        exec("def test_func(a, /, b): pass")
        features["positional_only"] = True
        print("  ✅ Positional-only parameters (/) - Available")
    except SyntaxError:
        features["positional_only"] = False
        print("  ❌ Positional-only parameters (/) - Not available")

    # Test f-string = debugging
    try:
        test_var = 42
        result = eval("f'{test_var=}'")
        features["f_string_debug"] = True
        print("  ✅ F-string debugging (=) - Available")
    except SyntaxError:
        features["f_string_debug"] = False
        print("  ❌ F-string debugging (=) - Not available")

    # Test typing.Final
    try:
        from typing import Final

        features["typing_final"] = True
        print("  ✅ typing.Final - Available")
    except ImportError:
        features["typing_final"] = False
        print("  ❌ typing.Final - Not available")

    # Test typing.Literal
    try:
        from typing import Literal

        features["typing_literal"] = True
        print("  ✅ typing.Literal - Available")
    except ImportError:
        features["typing_literal"] = False
        print("  ❌ typing.Literal - Not available")

    # Test typing.TypedDict
    try:
        from typing import TypedDict

        features["typed_dict"] = True
        print("  ✅ typing.TypedDict - Available")
    except ImportError:
        features["typed_dict"] = False
        print("  ❌ typing.TypedDict - Not available")

    # Test math.prod (Python 3.8+)
    try:
        import math

        if hasattr(math, "prod"):
            features["math_prod"] = True
            print("  ✅ math.prod - Available")
        else:
            features["math_prod"] = False
            print("  ❌ math.prod - Not available")
    except ImportError:
        features["math_prod"] = False
        print("  ❌ math.prod - Not available")

    # Test math.isqrt (Python 3.8+)
    try:
        import math

        if hasattr(math, "isqrt"):
            features["math_isqrt"] = True
            print("  ✅ math.isqrt - Available")
        else:
            features["math_isqrt"] = False
            print("  ❌ math.isqrt - Not available")
    except ImportError:
        features["math_isqrt"] = False
        print("  ❌ math.isqrt - Not available")

    return features


def discover_and_run_tests():
    """Discover and run all tests"""
    print("\\n🧪 Discovering and running tests...")

    # Add current directory and src to path
    current_dir = Path(__file__).parent
    src_dir = current_dir.parent / "src"

    sys.path.insert(0, str(current_dir))
    sys.path.insert(0, str(src_dir))

    # Discover tests
    loader = unittest.TestLoader()
    start_dir = str(current_dir)
    suite = loader.discover(start_dir, pattern="test_*.py")

    # Run tests
    runner = unittest.TextTestRunner(verbosity=2, buffer=True)
    result = runner.run(suite)

    return result


def run_specific_python38_tests():
    """Run specific Python 3.8 compatibility tests"""
    print("\\n🐍 Running Python 3.8 specific compatibility tests...")

    # Add paths
    current_dir = Path(__file__).parent
    src_dir = current_dir.parent / "src"

    sys.path.insert(0, str(current_dir))
    sys.path.insert(0, str(src_dir))

    # Import and run Python 3.8 specific tests
    try:
        from test_python38_compatibility import (
            TestPython38Compatibility,
            TestPython38SpecificFeatures,
        )

        loader = unittest.TestLoader()
        suite = unittest.TestSuite()

        # Add Python 3.8 compatibility tests
        suite.addTest(loader.loadTestsFromTestCase(TestPython38Compatibility))
        suite.addTest(loader.loadTestsFromTestCase(TestPython38SpecificFeatures))

        runner = unittest.TextTestRunner(verbosity=2, buffer=True)
        result = runner.run(suite)

        return result

    except ImportError as e:
        print(f"❌ Could not import Python 3.8 compatibility tests: {e}")
        return None


def check_package_compatibility():
    """Check compatibility of required packages"""
    print("\\n📦 Checking package compatibility:")

    packages = {
        "google.generativeai": "Google Generative AI",
        "pathlib": "Path library",
        "typing": "Type hints",
        "unittest.mock": "Mock testing",
        "tempfile": "Temporary files",
        "os": "Operating system interface",
    }

    compatible_packages = {}

    for package, description in packages.items():
        try:
            importlib.import_module(package)
            compatible_packages[package] = True
            print(f"  ✅ {description} ({package}) - Available")
        except ImportError:
            compatible_packages[package] = False
            print(f"  ❌ {description} ({package}) - Not available")

    return compatible_packages


def generate_compatibility_report(features, packages, test_result, py38_result):
    """Generate a comprehensive compatibility report"""
    print("\\n📊 Python 3.8 Compatibility Report")
    print("=" * 50)

    # Python version
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")

    # Features summary
    total_features = len(features)
    available_features = sum(features.values())
    feature_percentage = (available_features / total_features) * 100

    print(
        f"\\nPython 3.8 Features: {available_features}/{total_features} ({feature_percentage:.1f}%)"
    )

    # Package summary
    total_packages = len(packages)
    available_packages = sum(packages.values())
    package_percentage = (available_packages / total_packages) * 100

    print(
        f"Required Packages: {available_packages}/{total_packages} ({package_percentage:.1f}%)"
    )

    # Test results
    if test_result:
        print(f"\\nGeneral Tests:")
        print(f"  Total: {test_result.testsRun}")
        print(
            f"  Passed: {test_result.testsRun - len(test_result.failures) - len(test_result.errors)}"
        )
        print(f"  Failed: {len(test_result.failures)}")
        print(f"  Errors: {len(test_result.errors)}")

    if py38_result:
        print(f"\\nPython 3.8 Compatibility Tests:")
        print(f"  Total: {py38_result.testsRun}")
        print(
            f"  Passed: {py38_result.testsRun - len(py38_result.failures) - len(py38_result.errors)}"
        )
        print(f"  Failed: {len(py38_result.failures)}")
        print(f"  Errors: {len(py38_result.errors)}")

    # Overall compatibility
    overall_score = (feature_percentage + package_percentage) / 2
    print(f"\\nOverall Compatibility Score: {overall_score:.1f}%")

    if overall_score >= 90:
        print("🎉 Excellent Python 3.8 compatibility!")
    elif overall_score >= 75:
        print("✅ Good Python 3.8 compatibility")
    elif overall_score >= 50:
        print("⚠️  Moderate Python 3.8 compatibility")
    else:
        print("❌ Poor Python 3.8 compatibility")

    # Recommendations
    print("\\n💡 Recommendations:")
    if feature_percentage < 100:
        print("  - Consider upgrading to Python 3.8+ for full feature support")
    if package_percentage < 100:
        print("  - Install missing packages: pip install -r requirements.txt")
    if test_result and (test_result.failures or test_result.errors):
        print("  - Fix failing tests before deploying")

    return overall_score


def main():
    """Main test runner function"""
    print("🚀 Python 3.8 Compatibility Test Suite")
    print("=" * 50)

    # Check Python version
    version_ok = check_python_version()

    # Check Python 3.8 features
    features = check_python38_features()

    # Check package compatibility
    packages = check_package_compatibility()

    # Run general tests
    test_result = discover_and_run_tests()

    # Run Python 3.8 specific tests
    py38_result = run_specific_python38_tests()

    # Generate report
    compatibility_score = generate_compatibility_report(
        features, packages, test_result, py38_result
    )

    # Exit with appropriate code
    if compatibility_score >= 75 and test_result and test_result.wasSuccessful():
        if py38_result is None or py38_result.wasSuccessful():
            print("\\n🎉 All tests passed! Application is Python 3.8 compatible.")
            sys.exit(0)

    print("\\n⚠️  Some issues were found. Check the report above.")
    sys.exit(1)


if __name__ == "__main__":
    main()
