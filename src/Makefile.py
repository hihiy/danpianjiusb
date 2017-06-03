from distutils.core import setup
import py2exe
setup(zipfile=None, windows=[{"script":"SerialUi.py"}],
		options={"py2exe":{"compressed":2, "bundle_files":1,
                 "includes":["sip", "PyQt4.QtGui", "PyQt4.QtCore", "serial"],
                 "dll_excludes": ["msvcm90.dll", "msvcp90.dll", "msvcr90.dll"]}})
