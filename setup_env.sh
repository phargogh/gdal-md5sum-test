
ENVDIR=env

virtualenv --system-site-packages env

source $ENVDIR/bin/activate

pip install git+git://github.com/natcap/pygeoprocessing.git
