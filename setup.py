# python package setup file


from setuptools import setup, find_packages

VERSION = '0.1.0'
setup(
    name='PathSelector',
    version=VERSION,
    description='PathSelector is a simple path selection module for python.',
    author='Mustafa Ozan Çetin',
    author_email='',
    url='',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'path', 'selector', 'file', 'directory'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
# end of file