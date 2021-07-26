"""
This file can contain functionalities for saving/loading data
"""
import h5py

def save_data(file, case): # hdf5 file saving

    f = h5py.File(case + "/" + case + '.hdf5', 'w')
    f.create_dataset('RND', data=file)
    f.close()
