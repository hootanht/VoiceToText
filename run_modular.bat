@echo off
echo ====================================
echo Voice to Text Analyzer v2.0
echo Modular Architecture with SOLID Principles
echo ====================================
echo.

echo [1/3] Installing required packages...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo ERROR: Failed to install packages
    echo Trying with trusted hosts...
    pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
)

echo.
echo [2/3] Running voice to text analyzer...
python main.py

echo.
echo [3/3] Process completed!
echo Check the 'results' folder for Markdown output files.
echo.
echo Press any key to exit...
pause
