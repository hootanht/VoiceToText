# 🎤 Voice to Text Analyzer

An advanced modular AI-powered audio analysis system built with Google Gemini API that converts audio files to text and provides comprehensive analysis reports in Markdown format.

[![Build Status](https://github.com/user/voice-to-text/actions/workflows/ci.yml/badge.svg)](https://github.com/user/voice-to-text/actions/workflows/ci.yml)
[![Tests](https://github.com/user/voice-to-text/actions/workflows/test.yml/badge.svg)](https://github.com/user/voice-to-text/actions/workflows/test.yml)
[![Docker](https://github.com/user/voice-to-text/actions/workflows/deploy.yml/badge.svg)](https://github.com/user/voice-to-text/actions/workflows/deploy.yml)
[![Documentation](https://github.com/user/voice-to-text/actions/workflows/docs.yml/badge.svg)](https://user.github.io/voice-to-text/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## � Table of Contents

- [🎯 Overview](#-overview)
- [✨ Features](#-features)
- [🏗️ Architecture](#-architecture)
- [📋 Prerequisites](#-prerequisites)
- [🚀 Installation](#-installation)
- [🎮 Usage](#-usage)
- [⚙️ Environment Configuration](#-environment-configuration)
- [🐳 Docker Deployment](#-docker-deployment)
- [🔄 CI/CD Pipeline](#-cicd-pipeline)
- [📁 Project Structure](#-project-structure)
- [📖 API Documentation](#-api-documentation)
- [📊 Sample Output](#-sample-output)
- [🔧 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)

---

## 🎯 Overview

### What is Voice to Text Analyzer?

Voice to Text Analyzer is an intelligent audio processing system that:

1. **Reads audio files** from the `assets/voice/` directory
2. **Sends them to Google Gemini AI** for processing
3. **Extracts complete conversation transcripts**
4. **Performs minute-by-minute analysis**
5. **Generates beautiful Markdown reports**
6. **Creates comprehensive summaries** with statistics

### Key Capabilities

- 🎧 **Audio Processing**: Convert conversations to text (optimized for Persian/Farsi)
- 📊 **Content Analysis**: Understand topics, issues, and solutions
- ⏰ **Timeline Analysis**: Minute-by-minute conversation breakdown
- 📝 **Report Generation**: Professional Markdown files with rich formatting
- 📈 **Statistics**: Success rates, processing times, file sizes

### Use Cases

- **Customer Support**: Analyze support call conversations
- **Education**: Review lectures and conference recordings
- **Legal**: Analyze court proceedings and legal consultations
- **Research**: Analyze interviews and focus group discussions
- **Business**: Meeting transcription and analysis

---

## ✨ Features

### 🎯 Core Features
- ✅ **Multiple Format Support**: MP3, WAV, AIFF, AAC, OGG, FLAC
- ✅ **Advanced AI**: Google Gemini 2.0 Flash integration
- ✅ **Persian Language Optimized**: Native Farsi prompt engineering
- ✅ **Markdown Output**: Beautiful, readable reports with tables and formatting
- ✅ **Batch Processing**: Process multiple files simultaneously
- ✅ **Summary Reports**: Aggregate statistics and insights

### 🏗️ Technical Features
- ✅ **Modular Architecture**: Clean separation of concerns
- ✅ **SOLID Principles**: Maintainable and extensible design
- ✅ **Dependency Injection**: Factory pattern implementation
- ✅ **Error Handling**: Comprehensive error management and recovery
- ✅ **Interface-Based Design**: Protocol-oriented programming
- ✅ **Performance Tracking**: Processing time monitoring

### 🎨 User Experience
- ✅ **One-Click Execution**: Simple batch file execution
- ✅ **Progress Tracking**: Real-time processing status
- ✅ **Error Recovery**: Continue processing on individual file failures
- ✅ **Rich Output**: Emoji-enhanced, formatted console output

---

## 🏗️ Architecture

### SOLID Principles Implementation

#### 🔹 Single Responsibility Principle (SRP)
Each class has one specific responsibility:
- `ConfigurationService` → Manages API configuration
- `AudioFileService` → Handles audio file operations
- `GeminiAnalyzer` → AI analysis processing
- `MarkdownReportGenerator` → Report generation
- `PersianPromptProvider` → Persian language prompts

#### 🔹 Open/Closed Principle (OCP)
System is open for extension, closed for modification:
- Add new analyzers without changing existing code
- Support new report formats seamlessly
- Add new languages without core changes

#### 🔹 Liskov Substitution Principle (LSP)
All services are interchangeable through common interfaces:
- All analyzers implement `IAIAnalyzer`
- All report generators follow `IReportGenerator`

#### 🔹 Interface Segregation Principle (ISP)
Small, focused interfaces:
- `IAudioFileService` → Only file operations
- `IAIAnalyzer` → Only AI analysis
- `IReportGenerator` → Only report generation

#### 🔹 Dependency Inversion Principle (DIP)
Classes depend on interfaces, not concrete implementations:
- `ApplicationFactory` injects all dependencies
- High-level modules depend on abstractions

### Design Patterns

#### 🏭 Factory Pattern
```python
app = ApplicationFactory.create_persian_application(api_key)
```

#### 🎯 Strategy Pattern
```python
# Language selection
prompt_provider = PersianPromptProvider()  # or EnglishPromptProvider()
```

#### 📦 Repository Pattern
```python
audio_service.find_audio_files(folder_path)
```

#### 📡 Observer Pattern
```python
# Progress reporting during processing
print(f"📊 Processing file {index}/{total}")
```

---

## 📋 Prerequisites

### Operating System
- ✅ **Windows 10/11** (tested)
- ✅ **macOS** (compatible)
- ✅ **Linux** (compatible)

### Software Requirements
- ✅ **Python 3.8+** (recommended: Python 3.10+)
- ✅ **pip** (Python package manager)
- ✅ **Internet connection** (for Gemini API)

### API Requirements
- ✅ **Google Gemini API Key**
  - Get from: [Google AI Studio](https://aistudio.google.com/)
  - Free tier available with limits

### Audio Files
- ✅ **Supported formats**: MP3, WAV, AIFF, AAC, OGG, FLAC
- ✅ **Quality**: Minimum 16kHz sampling rate
- ✅ **Language**: Optimized for Persian/Farsi (English supported)

---

## 🚀 Installation

### Step 1: Download Project
```bash
# Download or copy the project folder
cd "C:\Users\YourName\Desktop"
# Place the "Voice to text" folder here
```

### Step 2: Install Python
1. Download Python from [python.org](https://python.org)
2. Install with "Add Python to PATH" checked
3. Verify installation:
```bash
python --version
pip --version
```

### Step 3: Install Dependencies
```bash
cd "C:\Users\YourName\Desktop\Voice to text"
pip install -r requirements.txt
```

### Step 4: Get API Key
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Create free account
3. Generate API Key
4. Copy the key

### Step 5: Configure Environment
```bash
# Copy the environment template
cp env.template .env

# Edit .env with your actual API key
# Add: GEMINI_API_KEY=your_actual_api_key_here
```

### Step 6: Set up GitHub Secrets (for CI/CD)
If you're planning to use GitHub Actions:
- See [GITHUB_SECRETS_SETUP.md](GITHUB_SECRETS_SETUP.md) for detailed instructions
- Add `GEMINI_API_KEY` and `GEMINI_MODEL_NAME` secrets to your repository
- This enables automatic testing and integration

### Step 5: Configure Environment Variables (Recommended)

#### Option A: Using Environment Variables (🔒 Secure)
1. **Copy the example environment file:**
   ```bash
   copy .env.example .env
   ```

2. **Edit the `.env` file** with your actual values:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   GEMINI_MODEL_NAME=gemini-2.0-flash
   ```

3. **Install python-dotenv** (if not already installed):
   ```bash
   pip install python-dotenv
   ```

#### Option B: Direct Configuration (Legacy)
Open `main.py` and replace the API key:
```python
API_KEY = "YOUR_GEMINI_API_KEY_HERE"  # Replace with your key
```

> 🛡️ **Security Note**: Using environment variables (Option A) is recommended as it keeps sensitive information out of your source code.

### Step 6: Test Installation
```bash
python main.py
```

---

## 🎮 Usage

### Method 1: Batch File (Simplest)
```bash
# Double-click this file
run_modular.bat
```

### Method 2: Command Line
```bash
cd "C:\Users\YourName\Desktop\Voice to text"
python main.py
```

### Method 3: Custom Configuration
```python
from app_factory import ApplicationFactory

# Persian (default)
app = ApplicationFactory.create_persian_application("YOUR_API_KEY")
results = app.process_audio_files("assets")

# English
app = ApplicationFactory.create_english_application("YOUR_API_KEY")
results = app.process_audio_files("assets")

# Custom
app = ApplicationFactory.create_application(
    api_key="YOUR_API_KEY",
    model_name="gemini-2.0-flash",
    language="persian"
)
```

### Execution Steps

1. **Place Files**: Put audio files in `assets/voice/`
2. **Run**: Choose one of the methods above
3. **Wait**: Processing may take several minutes
4. **View Results**: MD files generated in `results/` folder

---

## ⚙️ Environment Configuration

### 🔐 Secure Configuration with Environment Variables

The application now supports secure configuration through environment variables, keeping sensitive information out of your source code.

#### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|-----------|
| `GEMINI_API_KEY` | Your Google Gemini API key | None | ✅ Yes |
| `GEMINI_MODEL_NAME` | Gemini model to use | `gemini-2.0-flash` | ❌ No |

#### Setup Instructions

1. **Copy the example file:**
   ```bash
   copy .env.example .env
   ```

2. **Edit your `.env` file:**
   ```env
   # Your actual Gemini API key
   GEMINI_API_KEY=AIzaSyD7zLhMbbmZVGMC_Wc96WVi5keyh6_Fbj8
   
   # Optional: Specify a different model
   GEMINI_MODEL_NAME=gemini-2.0-flash
   ```

3. **Install python-dotenv** (if needed):
   ```bash
   pip install python-dotenv
   ```

#### How It Works

The `ConfigurationService` automatically:
- ✅ Checks for environment variables first
- ✅ Falls back to default values if not set
- ✅ Provides a secure way to manage API keys
- ✅ Supports different configurations per environment

```python
# The service automatically uses environment variables
config = ConfigurationService()
api_key = config.get_api_key()  # Gets from GEMINI_API_KEY env var
model = config.get_model_name() # Gets from GEMINI_MODEL_NAME env var or default
```

#### Benefits

- 🔒 **Security**: API keys are not in source code
- 🌍 **Environment-specific**: Different keys for dev/prod
- 🚀 **Easy deployment**: No code changes needed
- 📝 **Version control safe**: .env files are gitignored

---

## 🐳 Docker Deployment

### Quick Start with Docker

The application includes complete Docker support for easy deployment and development.

#### Option 1: Docker Compose (Recommended)

1. **Create your environment file:**
   ```bash
   cp .env.example .env
   # Edit .env with your API key
   ```

2. **Run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

3. **Development mode:**
   ```bash
   docker-compose --profile dev up
   ```

#### Option 2: Docker Build

1. **Build the image:**
   ```bash
   docker build -t voice-to-text .
   ```

2. **Run the container:**
   ```bash
   docker run -it --rm \
     -e GEMINI_API_KEY=your_api_key \
     -v $(pwd)/assets:/app/assets \
     -v $(pwd)/results:/app/results \
     voice-to-text
   ```

#### Production Deployment

The Docker image includes:
- ✅ **Health checks** for monitoring
- ✅ **Volume mounts** for assets and results
- ✅ **Environment configuration** support
- ✅ **Multi-stage builds** for optimization

---

## 🔄 CI/CD Pipeline

### GitHub Actions Workflows

The project includes comprehensive CI/CD automation:

#### 🧪 Continuous Integration (`ci.yml`)

- **Code Quality**: Black, Flake8, isort, MyPy
- **Security Scanning**: Safety, Bandit
- **Multi-Platform Testing**: Ubuntu, Windows, macOS
- **Python Versions**: 3.8, 3.9, 3.10, 3.11
- **Docker Build**: Container testing

```bash
# Triggered on:
- Push to main/develop branches
- Pull requests
- Manual dispatch
```

#### 🔍 Comprehensive Testing (`test.yml`)

- **Unit Tests**: pytest with coverage
- **Integration Tests**: Full application testing
- **Docker Tests**: Container functionality
- **Dependency Security**: Vulnerability scanning

#### 📊 Performance Testing (`performance.yml`)

- **Memory Usage Analysis**: Resource monitoring
- **Performance Benchmarks**: Speed measurements
- **System Resource Monitoring**: CPU, disk, memory
- **Daily Scheduled Runs**: Automated monitoring

#### 🚀 Deployment (`deploy.yml`)

- **Docker Registry**: GitHub Container Registry
- **Security Scanning**: Trivy vulnerability scanner
- **Multi-Environment**: Staging and Production
- **Release Automation**: Tagged releases

#### 📚 Documentation (`docs.yml`)

- **Auto-Generated Docs**: API documentation
- **GitHub Pages**: Hosted documentation
- **Multi-Format**: Markdown, HTML
- **Architecture Diagrams**: Mermaid integration

### Release Process

1. **Create a release tag:**
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

2. **Automated pipeline:**
   - ✅ Build and test
   - ✅ Security scan
   - ✅ Create Docker image
   - ✅ Deploy to staging
   - ✅ Create GitHub release
   - ✅ Update documentation

### Monitoring and Quality

- 📊 **Code Coverage**: Automated reporting
- 🔍 **Security Alerts**: Dependency monitoring
- 📈 **Performance Tracking**: Daily benchmarks
- 🐛 **Error Tracking**: Comprehensive logging
- 📋 **Release Notes**: Auto-generated changelogs

---

## 📁 Project Structure

```
Voice to text/
│
├── 📁 assets/                          # Input files
│   └── 📁 voice/                       # Audio files
│       └── 🎵 1.mp3                    # Sample audio file
│
├── 📁 results/                         # Output files
│   ├── 📄 1_analysis.md               # Individual file analysis
│   └── 📄 summary_report.md           # Summary report
│
├── 📁 src/                            # Source code (modular architecture)
│   ├── 📁 interfaces/                 # Interface definitions
│   │   └── 📄 __init__.py            # System interfaces
│   │
│   ├── 📁 models/                     # Data models
│   │   ├── 📄 __init__.py
│   │   ├── 📄 audio_file.py          # AudioFile model
│   │   └── 📄 analysis_result.py     # AnalysisResult model
│   │
│   ├── 📁 services/                   # Business services
│   │   ├── 📄 __init__.py
│   │   ├── 📄 configuration_service.py    # Configuration management
│   │   ├── 📄 audio_file_service.py       # File operations
│   │   ├── 📄 gemini_analyzer.py          # AI analysis
│   │   ├── 📄 prompt_provider.py          # Prompt provider
│   │   └── 📄 report_generator.py         # Report generation
│   │
│   ├── 📄 __init__.py
│   └── 📄 application.py              # Main orchestrator
│
├── 📄 main.py                         # Application entry point
├── 📄 app_factory.py                  # Dependency injection factory
├── 📄 requirements.txt                # Python dependencies
├── 📄 run_modular.bat                 # Windows execution script
└── 📄 README.md                       # This file
```

---

## 📖 API Documentation

### Core Classes

#### `main.py` - Application Entry Point
```python
# Main application entry point
# Contains API Key configuration and file paths
# Displays architecture information
# Runs the main application
```

#### `app_factory.py` - Dependency Injection Factory
```python
# Creates application instances with Dependency Injection
# Configures all services
# Supports multiple languages
# Implements Factory Pattern
```

### Interfaces (`src/interfaces/`)

#### `__init__.py` - Interface Definitions
```python
# IAudioFileService: File operations interface
# IAIAnalyzer: AI analysis interface
# IReportGenerator: Report generation interface
# IConfigurationService: Configuration interface
# IPromptProvider: Prompt provision interface
```

### Models (`src/models/`)

#### `audio_file.py` - Audio File Model
```python
@dataclass
class AudioFile:
    file_path: str          # File path
    file_name: str          # File name
    stem_name: str          # Name without extension
    format: str             # File format
    file_size: int          # File size in bytes
```

#### `analysis_result.py` - Analysis Result Model
```python
@dataclass  
class AnalysisResult:
    audio_file: AudioFile       # Audio file reference
    analysis_text: str          # Analysis text
    is_successful: bool         # Success status
    processing_time: float      # Processing time in seconds
    timestamp: datetime         # Analysis timestamp
    error_message: str          # Error message if failed
    output_file_path: str       # Output file path
```

### Services (`src/services/`)

#### `configuration_service.py` - Configuration Management
```python
class ConfigurationService:
    # Manages API Key from environment variables
    # Configures Gemini model from GEMINI_MODEL_NAME
    # Provides secure environment-based configuration
    # Validates settings and provides fallback defaults
    # Supports multiple environments (dev/staging/prod)
```

#### `audio_file_service.py` - File Operations
```python
class AudioFileService:
    # Finds audio files
    # Validates supported formats
    # Creates AudioFile models
    # Manages file paths
```

#### `gemini_analyzer.py` - AI Analysis
```python
class GeminiAnalyzer:
    # Sends files to Gemini
    # Receives text analysis
    # Handles API errors
    # Tracks processing time
```

#### `prompt_provider.py` - Prompt Provider
```python
class PersianPromptProvider:
    # Optimized Persian prompts
    # Desired output structure
    # Analysis instructions

class EnglishPromptProvider:
    # English prompts
    # English structure
```

#### `report_generator.py` - Report Generation
```python
class MarkdownReportGenerator:
    # Generates Markdown files
    # Beautiful formatting
    # Information tables
    # Summary reports
```

#### `application.py` - Main Orchestrator
```python
class VoiceToTextApplication:
    # Coordinates between services
    # Manages overall process
    # Reports progress
    # Handles errors
```

---

## 📊 Sample Output

### Individual Analysis File (`1_analysis.md`)
````markdown
# Audio File Analysis: conversation.mp3

## File Information

| Property | Value |
|----------|-------|
| **File Name** | `conversation.mp3` |
| **Format** | MP3 |
| **File Size** | 2.1 MB |
| **Processing Time** | 15.3 seconds |
| **Status** | ✅ Success |

## Analysis Results

### 1. Complete Conversation Transcript
**Person A:** Hello, good day
**Person B:** Hello, how can I help you?
...

### 2. Minute-by-Minute Analysis
**Minute 0-1:** Greetings and introductions
**Minute 1-2:** Customer presents main issue
...

### 3. Summary Report
- **Topic:** Technical issue with application
- **Problem:** Server connection failure
- **Solution:** Network settings reset
- **Status:** ✅ Resolved
````

### Summary Report File (`summary_report.md`)
````markdown
# Processing Summary Report

## Overall Statistics

| Statistic | Count |
|-----------|-------|
| **Total Files** | 5 files |
| **Successful** | 4 ✅ |
| **Failed** | 1 ❌ |
| **Success Rate** | 80% |

## Processed Files

| File | Status | Link |
|------|--------|------|
| `call1.mp3` | ✅ | [View](call1_analysis.md) |
| `call2.mp3` | ✅ | [View](call2_analysis.md) |
...
````

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### ❌ API Key Error
```
Error: Invalid API key
```
**Solution:**
1. Verify API Key in `main.py`
2. Ensure API is enabled in Google AI Studio
3. Check internet connection

#### ❌ Dependency Installation Error
```
ERROR: Could not install packages
```
**Solution:**
```bash
pip install --upgrade pip
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

#### ❌ Audio File Not Found
```
No audio files found
```
**Solution:**
1. Place files in `assets/voice/`
2. Check supported formats
3. Verify folder name (lowercase 'voice')

#### ❌ Memory Error
```
Out of memory error
```
**Solution:**
1. Reduce number of files
2. Lower audio file quality
3. Close unnecessary applications

#### ❌ Connection Error
```
Connection timeout
```
**Solution:**
1. Check internet connection
2. Use VPN if service is blocked
3. Retry after a few minutes

### Debugging and Logs

#### Enable Debug Mode
Modify `main.py`:
```python
# Add detailed logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

#### Check Generated Files
```bash
# List output files
dir results\

# View content
type "results\summary_report.md"
```

### Getting Support

If issues persist:
1. Check GitHub Issues
2. Provide error details
3. Share log files

---

## 🤝 Contributing

### Development Setup

1. **Fork the Repository**
2. **Create Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make Changes**
4. **Run Tests**
   ```bash
   python -m pytest tests/
   ```
5. **Commit Changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
6. **Push and Create PR**

### Code Standards

- Follow **SOLID principles**
- Use **type hints**
- Write **comprehensive tests**
- Document **public APIs**
- Follow **PEP 8** style guide
- Apply **Black code formatting** (see [FORMATTING.md](FORMATTING.md))

### Areas for Contribution

- 🌐 **Multi-language support**
- 🖥️ **GUI development**
- 🐳 **Docker containerization**
- ☁️ **Cloud deployment**
- 📊 **Advanced analytics**
- 🔧 **Performance optimization**

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- **GitHub Issues**: Bug reports and feature requests
- **Email**: hootanhemmati@outlook.com

---

## 🎯 Roadmap

### Version 2.1 (Planned)
- [ ] Multi-language support (English, Arabic)
- [ ] Real-time processing
- [ ] Web API interface
- [ ] Docker support

### Version 3.0 (Future)
- [ ] GUI application
- [ ] Cloud deployment
- [ ] Advanced analytics
- [ ] Batch job scheduler

---

## 🙏 Acknowledgments

- **Google Gemini Team** for providing the AI API
- **Python Community** for excellent libraries
- **Open Source Contributors** worldwide

---

**Built with ❤️ for the Developer Community**
