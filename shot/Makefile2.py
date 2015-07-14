from distutils.core import setup
import py2exe

DATA=[('imageformats',['D:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qjpeg4.dll',
    'D:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qgif4.dll',
    'D:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qico4.dll',
    'D:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qmng4.dll',
    'D:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qsvg4.dll',
    'D:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qtiff4.dll'
    ])]
setup(windows=[{"script":"Main.py"}], 
    data_files = DATA,
    zipfile='lib.zip',
    options={"py2exe":{
        "includes":["sip", "PyQt4.QtNetwork", "PyQt4.QtWebKit", "PyQt4.QtSvg" ],
        # "includes":["sip"],
        # "excludes"["PyQt4"],
        "bundle_files":3,
        "compressed":False,
        "dll_excludes":["msvcm90.dll",
                        "msvcp90.dll", 
                        "msvcr90.dll"],
        "xref":False}}, 
    )