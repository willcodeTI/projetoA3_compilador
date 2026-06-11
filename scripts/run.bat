@echo off
cd /d "%~dp0\.."
echo Iniciando Language Classifier...
echo.
echo Acesse: http://localhost:8501
echo.
streamlit run app/streamlit_app.py
pause
