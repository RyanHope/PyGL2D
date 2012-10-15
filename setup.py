from setuptools import setup
from pygl2d import __version__ as version
import os.path

descr_file = os.path.join(os.path.dirname(__file__), 'README')

setup(
    name='PyGL2D',
    version=version,

    packages=['pygl2d'],

    description='A 2D Graphics Library for PyGame and PyOpenGL.',
    long_description=open(descr_file).read(),
    author='Ryan Hope',
    author_email='rmh3093@gmail.com',
    url='https://github.com/RyanHope/PyGL2D',
    classifiers=[
				'License :: OSI Approved :: GNU General Public License (GPL)',
				'Framework :: Twisted',
				'Programming Language :: Python :: 2',
				'Topic :: Software Development :: Libraries :: pygame',
				'Topic :: Multimedia :: Graphics :: 3D Rendering',
    ],
	license='GPL-3',
	install_requires=[
					'pygame',
                    'PyOpenGL',
					'PyOpenGL_accelerate'
	]
 )
