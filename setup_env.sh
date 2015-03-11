
ENVDIR=env

virtualenv --system-site-packages env

source $ENVDIR/bin/activate

pip install hg+https://bitbucket.org/richpsharp/pygeoprocessing
