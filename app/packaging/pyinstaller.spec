# -*- mode: python ; coding: utf-8 -*-
# T5448/T5449 — receita PyInstaller (onedir) do DAT Engineering Studio.
#
# Uso (na raiz do projeto):
#     pyinstaller app\packaging\pyinstaller.spec
#
# O binário fica em dist\DAT Engineering Studio\main.exe (onedir).
# Para ícone próprio, coloque assets/icon.ico e aperte o valor de ICON.

import sys
from pathlib import Path

ROOT = Path(SPECPATH).resolve().parent.parent  # raiz do projeto
ICON = str(ROOT / "assets" / "icon.ico") if (ROOT / "assets" / "icon.ico").exists() else None

block_cipher = None

a = Analysis(
    [str(ROOT / "main.py")],
    pathex=[str(ROOT)],
    binaries=[],
    datas=[],
    hiddenimports=[
        "PySide6.QtCore",
        "PySide6.QtGui",
        "PySide6.QtWidgets",
        "numpy",
        "scipy",
        "scipy.special",
        "scipy.stats",
        "scipy.stats._qmc",
        "scipy.interpolate",
        "matplotlib",
        "matplotlib.backends.backend_qtagg",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["tkinter", "cv2", "pandas", "IPython"],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="DAT Engineering Studio",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    upx_exclude=[],
    icon=ICON,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="DAT Engineering Studio",
    version="0.1.0",
)

# Metadados do executável (Windows):
#   nome        : DAT Engineering Studio
#   descrição   : editor estocástico de casos CMG .dat
#   versão      : 0.1.0 (sincronize com app/__init__.py)
#   copyright   : diego
#   idioma      : pt-BR
