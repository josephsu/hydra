from setuptools import setup
from setuptools.extension import Extension
from Cython.Distutils import build_ext
from os.path import join

import os

ext_modules=[ 
        Extension("_hydra", 
            extra_compile_args=['-std=gnu99', '-O2'],
            sources = [
                "src/_hydra.pyx",
                'src/mmap_writer.c',
                'src/MurmurHash2A.c'],
            include_dirs = [join(os.getcwd(), 'src')],  # path to .h file(s)
            library_dirs = [join(os.getcwd(), 'src')],  # path to .a or .so file(s)
            ),
]

setup(
  name = 'Hydra',
  version=1.0,
  cmdclass = {'build_ext': build_ext},
  zip_safe=False,
  package_dir = {'': 'src'},
  py_modules = ['hydra'],
  ext_modules = ext_modules,
)
