#!/usr/bin/env python3
"""
Python 3.8 Compatibility Test Runner
راه‌انداز تست سازگاری پایتون ۳.۸

This script runs comprehensive Python 3.8 compatibility tests and provides
detailed reporting on feature availability and compatibility status.
"""

import importlib
import json
import os
import sys
import unittest
from pathlib import Path
from typing import Any, Dict, List, Optional

# Ensure we can import our test modules
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


class Python38CompatibilityRunner:
    """Comprehensive Python 3.8 compatibility test runner"""

    def __init__(self):
        self.results = {
            "python_version": {
                "major": sys.version_info.major,
                "minor": sys.version_info.minor,
                "micro": sys.version_info.micro,
                "full": sys.version,
            },
            "feature_compatibility": {},
            "test_results": {},
            "import_tests": {},
            "overall_score": 0,
        }

    def check_python38_features(self) -> Dict[str, bool]:
        """Check availability of Python 3.8 specific features"""
        features = {}

        # Test walrus operator (:=)
        try:
            exec("if (x := 1): pass")
            features["walrus_operator"] = True
        except SyntaxError:
            features["walrus_operator"] = False

        # Test positional-only parameters (/)
        try:
            exec("def f(a, /): pass")
            features["positional_only"] = True
        except SyntaxError:
            features["positional_only"] = False

        # Test f-string debugging (=)
        try:
            test_var = 42
            exec("f'{test_var=}'")
            features["f_string_debug"] = True
        except SyntaxError:
            features["f_string_debug"] = False

        # Test typing.Literal
        try:
            from typing import Literal

            features["typing_literal"] = True
        except ImportError:
            try:
                from typing_extensions import Literal

                features["typing_literal"] = True
            except ImportError:
                features["typing_literal"] = False

        # Test typing.Final
        try:
            from typing import Final

            features["typing_final"] = True
        except ImportError:
            features["typing_final"] = False

        # Test typing.TypedDict
        try:
            from typing import TypedDict

            features["typed_dict"] = True
        except ImportError:
            try:
                from typing_extensions import TypedDict

                features["typed_dict"] = True
            except ImportError:
                features["typed_dict"] = False

        # Test math.prod (Python 3.8+)
        try:
            import math

            math.prod([1, 2, 3])
            features["math_prod"] = True
        except AttributeError:
            features["math_prod"] = False

        # Test math.isqrt (Python 3.8+)
        try:
            import math

            math.isqrt(16)
            features["math_isqrt"] = True
        except AttributeError:
            features["math_isqrt"] = False

        # Test importlib.metadata (Python 3.8+)
        try:
            import importlib.metadata

            features["importlib_metadata"] = True
        except ImportError:
            try:
                import importlib_metadata

                features["importlib_metadata"] = True
            except ImportError:
                features["importlib_metadata"] = False

        return features

    def test_application_imports(self) -> Dict[str, bool]:
        """Test that our application modules can be imported"""
        import_results = {}

        modules_to_test = [
            "services.configuration_service",
            "services.audio_file_service",
            "services.gemini_analyzer",
            "services.report_generator",
            "services.prompt_provider",
            "models.audio_file",
            "models.analysis_result",
        ]

        for module_name in modules_to_test:
            try:
                importlib.import_module(module_name)
                import_results[module_name] = True
            except ImportError as e:
                import_results[module_name] = False
                print(f"❌ Failed to import {module_name}: {e}")

        return import_results

    def run_test_suite(self, test_module_name: str) -> Dict[str, Any]:
        """Run a specific test suite and return results"""
        try:
            # Import the test module
            test_module = importlib.import_module(test_module_name)

            # Create test suite
            loader = unittest.TestLoader()
            suite = loader.loadTestsFromModule(test_module)

            # Run tests
            runner = unittest.TextTestRunner(
                verbosity=0, stream=open(os.devnull, "w"))
            result = runner.run(suite)

            return {
                "tests_run": result.testsRun,
                "failures": len(result.failures),
                "errors": len(result.errors),
                "skipped": len(result.skipped) if hasattr(result, "skipped") else 0,
                "success_rate": (
                    result.testsRun - len(result.failures) - len(result.errors)
                )
                / max(result.testsRun, 1)
                * 100,
            }

        except Exception as e:
            return {
                "tests_run": 0,
                "failures": 1,
                "errors": 1,
                "skipped": 0,
                "success_rate": 0,
                "error": str(e),
            }

    def calculate_compatibility_score(self) -> float:
        """Calculate overall Python 3.8 compatibility score"""
        feature_score = 0
        total_features = 0

        for feature, available in self.results["feature_compatibility"].items():
            total_features += 1
            if available:
                feature_score += 1

        import_score = 0
        total_imports = 0

        for module, success in self.results["import_tests"].items():
            total_imports += 1
            if success:
                import_score += 1

        test_score = 0
        total_test_suites = 0

        for suite, results in self.results["test_results"].items():
            if "success_rate" in results:
                total_test_suites += 1
                test_score += results["success_rate"]

        # Calculate weighted average
        feature_weight = 0.4
        import_weight = 0.3
        test_weight = 0.3

        final_score = 0
        if total_features > 0:
            final_score += (feature_score / total_features) * \
                100 * feature_weight

        if total_imports > 0:
            final_score += (import_score / total_imports) * 100 * import_weight

        if total_test_suites > 0:
            final_score += (test_score / total_test_suites) * test_weight

        return final_score

    def run_all_tests(self):
        """Run all Python 3.8 compatibility tests"""
        print("🔍 Starting Python 3.8 Compatibility Analysis...")
        print(f"🐍 Python Version: {sys.version}")
        print("=" * 60)

        # Check Python 3.8 features
        print("📋 Checking Python 3.8 Feature Availability...")
        self.results["feature_compatibility"] = self.check_python38_features()

        for feature, available in self.results["feature_compatibility"].items():
            status = "✅" if available else "❌"
            print(
                f"  {status} {feature}: {'Available' if available else 'Not Available'}"
            )

        print()

        # Test application imports
        print("📦 Testing Application Module Imports...")
        self.results["import_tests"] = self.test_application_imports()

        for module, success in self.results["import_tests"].items():
            status = "✅" if success else "❌"
            print(f"  {status} {module}")

        print()

        # Run test suites
        test_suites = [
            "test_python38_features",
            "test_configuration_service",
            "test_audio_file",
            "test_analysis_result",
        ]

        print("🧪 Running Test Suites...")
        for suite in test_suites:
            print(f"  Running {suite}...")
            self.results["test_results"][suite] = self.run_test_suite(suite)

            results = self.results["test_results"][suite]
            if "error" in results:
                print(f"    ❌ Failed to run: {results['error']}")
            else:
                print(
                    f"    📊 Tests: {results['tests_run']}, "
                    f"Failures: {results['failures']}, "
                    f"Errors: {results['errors']}, "
                    f"Success: {results['success_rate']:.1f}%"
                )

        print()

        # Calculate overall score
        self.results["overall_score"] = self.calculate_compatibility_score()

        # Print summary
        self.print_summary()

        # Save results
        self.save_results()

    def print_summary(self):
        """Print comprehensive compatibility summary"""
        print("📈 PYTHON 3.8 COMPATIBILITY SUMMARY")
        print("=" * 60)

        score = self.results["overall_score"]
        if score >= 90:
            grade = "A+ (Excellent)"
            emoji = "🌟"
        elif score >= 80:
            grade = "A (Very Good)"
            emoji = "✨"
        elif score >= 70:
            grade = "B (Good)"
            emoji = "👍"
        elif score >= 60:
            grade = "C (Fair)"
            emoji = "⚠️"
        else:
            grade = "D (Needs Improvement)"
            emoji = "🔧"

        print(f"{emoji} Overall Compatibility Score: {score:.1f}% ({grade})")
        print()

        # Feature summary
        feature_stats = self.results["feature_compatibility"]
        available_features = sum(1 for v in feature_stats.values() if v)
        total_features = len(feature_stats)

        print(
            f"🎯 Python 3.8 Features: {available_features}/{total_features} available"
        )

        # Import summary
        import_stats = self.results["import_tests"]
        successful_imports = sum(1 for v in import_stats.values() if v)
        total_imports = len(import_stats)

        print(
            f"📦 Module Imports: {successful_imports}/{total_imports} successful")

        # Test summary
        test_stats = self.results["test_results"]
        total_tests = sum(r.get("tests_run", 0) for r in test_stats.values())
        total_failures = sum(
            r.get("failures", 0) + r.get("errors", 0) for r in test_stats.values()
        )

        print(
            f"🧪 Test Results: {total_tests - total_failures}/{total_tests} passed")

        print()

        # Recommendations
        print("💡 RECOMMENDATIONS:")

        if score >= 90:
            print("  ✅ Excellent Python 3.8 compatibility!")
            print("  ✅ All major features are working correctly.")
            print("  ✅ Ready for production deployment.")
        elif score >= 80:
            print("  👍 Very good compatibility with minor issues.")
            print("  🔧 Consider addressing any import failures.")
            print("  ✅ Suitable for most production environments.")
        elif score >= 70:
            print("  ⚠️  Good compatibility but some improvements needed.")
            print("  🔧 Review failed tests and imports.")
            print("  📚 Consider updating dependencies for better compatibility.")
        else:
            print("  🚨 Significant compatibility issues detected.")
            print("  🔧 Major fixes required before deployment.")
            print("  📚 Review Python 3.8 migration guide.")
            print("  🧪 Fix failing tests and import issues.")

        print()

    def save_results(self):
        """Save detailed results to JSON file"""
        output_file = Path("python38_compatibility_report.json")

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(self.results, f, indent=2, ensure_ascii=False)

            print(f"📄 Detailed report saved to: {output_file}")
        except Exception as e:
            print(f"❌ Failed to save report: {e}")


def main():
    """Main entry point for compatibility testing"""
    runner = Python38CompatibilityRunner()
    runner.run_all_tests()

    # Return appropriate exit code
    score = runner.results["overall_score"]
    if score >= 80:
        return 0  # Success
    elif score >= 60:
        return 1  # Warning
    else:
        return 2  # Error


if __name__ == "__main__":
    sys.exit(main())
