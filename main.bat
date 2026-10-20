@echo off
setlocal
title DAT Engineering Studio
cd /d "%~dp0"

if not exist "main.py" goto NO_PROJECT

:MENU
cls
echo ==================================================
echo              DAT ENGINEERING STUDIO
echo ==================================================
echo.
echo   [1] Executar GUI (python main.py)
echo   [2] Executar todos os testes (pytest)
echo   [3] Executar testes de GUI (pytest-qt)
echo   [4] Instalar dependencias (pip install -r requirements.txt)
echo   [5] Mostrar versao do Python e pip
echo   [6] Abrir pasta do projeto no Explorer
echo   [7] Executar exemplo completo (sampling + export)
echo   [0] Sair
echo.
echo ==================================================
set /p opt="Escolha uma opcao: "

if "%opt%"=="1" goto RUN_GUI
if "%opt%"=="2" goto RUN_TESTS
if "%opt%"=="3" goto RUN_GUI_TESTS
if "%opt%"=="4" goto INSTALL_DEPS
if "%opt%"=="5" goto SHOW_VERSIONS
if "%opt%"=="6" goto OPEN_FOLDER
if "%opt%"=="7" goto RUN_EXAMPLE
if "%opt%"=="0" goto EXIT

echo.
echo Opcao invalida: "%opt%"
timeout /t 2 >nul
goto MENU

:RUN_GUI
echo.
echo --- Iniciando GUI ---
python "main.py"
if errorlevel 1 echo [ERRO] A GUI terminou com codigo de erro.
pause
goto MENU

:RUN_TESTS
echo.
echo --- pytest tests ---
python -m pytest tests -q --tb=short
if errorlevel 1 echo [ERRO]Algum teste falhou.
pause
goto MENU

:RUN_GUI_TESTS
echo.
echo --- Testes de GUI (offscreen) ---
set QT_QPA_PLATFORM=offscreen
python -m pytest tests/test_gui_startup.py tests/test_ui_qt.py -q --tb=short
set QT_QPA_PLATFORM=
if errorlevel 1 echo [ERRO]Algum teste de GUI falhou.
pause
goto MENU

:INSTALL_DEPS
echo.
echo --- Instalando dependencias ---
python -m pip install -r requirements.txt
if errorlevel 1 echo [ERRO] Falha ao instalar dependencias.
pause
goto MENU

:SHOW_VERSIONS
echo.
python --version
python -m pip --version
echo.
pause
goto MENU

:OPEN_FOLDER
start "" "%~dp0"
goto MENU

:RUN_EXAMPLE
echo.
echo --- Exemplo: sampling + export (examples) ---
python -c "import runpy,sys; sys.argv=['example']; runpy.run_path(r'%~dp0examples\run_example.py')"
if errorlevel 1 echo [ERRO] O exemplo falhou.
pause
goto MENU

:EXIT
endlocal
exit /b 0

:NO_PROJECT
echo [ERRO] main.py nao encontrado. Execute este .bat na pasta do projeto.
pause
endlocal
exit /b 1
