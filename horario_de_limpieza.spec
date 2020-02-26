# -*- mode: python -*-

block_cipher = None


a = Analysis(['horario_de_limpieza.py'],
             pathex=['C:\\Users\\Artur\\Documents\\ARTUR\\PROGRAMMING\\Python\\Python_files\\Horarios_de_limpieza_en_casa'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
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
          name='horario_de_limpieza',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='broom.ico')
