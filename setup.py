from setuptools import setup, find_packages

setup(
    name='js-module-extractor',
    version='0.1.0',
    description='CLI tool to extract and beautify JavaScript modules from a text file.',
    author='Maximiliano Palacios',
    url='https://github.com/maxipalacios/js-module-extractor',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'jsbeautifier',
    ],
    entry_points={
        'console_scripts': [
            'js-module-extractor=main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
