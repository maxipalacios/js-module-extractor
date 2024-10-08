from setuptools import setup, find_packages

setup(
    name='module_generator',
    version='0.1.0',
    description='JavaScript module generator from a text file.',
    author='Maximiliano Palacios',
    url='https://github.com/maxipalacios/module_generator',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'jsbeautifier',
    ],
    entry_points={
        'console_scripts': [
            'module_generator=module_generator:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
