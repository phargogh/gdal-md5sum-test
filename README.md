gdal-md5sum-test
================

Record GDAL info and MD5sum data to a logfile.

Python package dependencies:
----------------------------
+ numpy
+ scipy
+ gdal

Environment Setup and Running on Linux and Mac
--------------------------------
``$ .\setup_env.sh``

``$ source env/bin/activate``

``$ python run.py``


Environment Setup and Running on Windows
----------------------------------------
``C:\Python27\Scripts\virtualenv env --system-site-packages``

``env\Scripts\pip.exe install hg+https://bitbucket.org/richpsharp/pygeoprocessing``

``env\Scripts\python.exe run.py``

When setting up pygeoprocessing, if Python complains about ``vcvarsall.bat``, run this line:

``copy C:\Python27\Lib\distutils\disutils.cfg env\Lib\distutils\distutils.cfg``

