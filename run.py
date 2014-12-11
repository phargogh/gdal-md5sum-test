import hashlib
import os
import platform
import sys

from osgeo import gdal
import numpy
import scipy
import pygeoprocessing

GDAL_DTYPES = {}
for _gdal_label in dir(sys.modules['osgeo.gdal']):
    if _gdal_label.startswith('GDT_'):
        GDAL_DTYPES[getattr(gdal, _gdal_label)] = _gdal_label

def md5sum(file_uri):
    """Get the MD5 hash for a single file.  The file is read in a
        memory-efficient fashion.

        Args:
            uri (string): a string uri to the file to be tested.

        Returns:
            An md5sum of the input file"""

    block_size = 2**20
    file_handler = open(file_uri, 'rb')  # open in binary to ensure compatibility
    md5 = hashlib.md5()
    while True:
        data = file_handler.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()

def main():
    base_raster = 'landuse_cur_200m.tif'
    base_nodata = pygeoprocessing.get_nodata_from_uri(base_raster)
    base_pixel_size = pygeoprocessing.get_cell_size_from_uri(base_raster)
    system = platform.platform()
    logfile_uri = 'md5_check_%s.log' % system

    logfile = open(logfile_uri, 'w')

    _write = lambda x: logfile.write(x + '\n')

    _write('System: %s' % system)
    _write('Python %s' % platform.python_version())
    _write('GDAL version: %s' % gdal.__version__)
    _write('numpy version: %s' % numpy.__version__)
    _write('scipy version: %s' % scipy.__version__)
    _write('base MD5sum: %s' % md5sum(base_raster))

    for gdal_type, gdal_type_label in GDAL_DTYPES.iteritems():
        if gdal_type_label in ['GDT_Unknown', 'GDT_TypeCount']:
            continue

        print gdal_type_label

        # convert the raster (via vectorize_datasets) to a new dtype
        new_uri = '%s.tif' % gdal_type_label
        pygeoprocessing.vectorize_datasets([base_raster], lambda x: x,
            new_uri, gdal_type, base_nodata, base_pixel_size, 'intersection')

        _write("%-15s: %s" % (gdal_type_label, md5sum(new_uri)))



    # write the 




if __name__ == '__main__':
    main()
