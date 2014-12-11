import pygeoprocessing

def main():
    src_ds = 'landuse_cur_200m.tif'
    dest_ds = 'gaussian.tif'

    nodata = pygeoprocessing.get_nodata_from_uri(src_ds)

    pygeoprocessing.gaussian_filter_dataset_uri(
        src_ds, 4, dest_ds, nodata)

if __name__ == '__main__':
    main()
