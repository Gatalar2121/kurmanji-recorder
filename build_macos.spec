# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['kurmanji_recorder_clean.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('kurmanji_dataset', 'kurmanji_dataset'),
    ],
    hiddenimports=[
        'customtkinter',
        'PIL._tkinter_finder',
        'sounddevice',
        'soundfile',
        'numpy',
        'librosa',
        'scipy',
        'docx',
        'PyPDF2',
        'requests',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='KurmanjiRecorder',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='KurmanjiRecorder',
)

app = BUNDLE(
    coll,
    name='KurmanjiRecorder.app',
    icon=None,  # Add .icns file path here if you have an icon
    bundle_identifier='com.kurmanji.recorder',
)
