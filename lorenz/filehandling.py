"""
This file can contain functionalities for saving/loading data

"""
import h5py


def save_data(file, name):
    """
    Saves the data as a hdf5 file into the path name/name.hdf5

    INPUT::

     file: to save
     name: name of the file

    OUPUT::

    """
    f = h5py.File(name + '/{}.hdf5'.format(name), 'w')
    f.create_dataset('RND', data=file)
    f.close()


def load_data(name):
    """
    Utility function to load an .hdf5 file

    """

    f = h5py.File('{}.hdf5'.format(name), 'r')
    B = f['RND'][...]
    return B
