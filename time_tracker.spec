# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['time_tracker.py'],
             pathex=['/home/bacancy/Downloads/TRACKER_UBUNTU_V2.1-20210930T103319Z-001/TRACKER_UBUNTU_V2.1'],
             binaries=[],
             datas=[('/home/bacancy/Documents/time_tracker_ubuntu_31_AUG/env/lib/python3.8/site-packages/eel/eel.js', 'eel'), ('web', 'web')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='time_tracker',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
