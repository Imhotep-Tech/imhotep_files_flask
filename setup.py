from setuptools import setup, find_packages

setup(
    name='imhotep_files_flask',  # Name of your library
    version='0.1',  # Version number
    packages=find_packages(),  # Automatically find package directories
    install_requires=[
        'Flask',
        'Werkzeug',
    ],
    description='A Flask library for secure file uploads and deletions',
    long_description=open('README.md').read(),  # Read long description from README
    long_description_content_type='text/markdown',
    author='Karim Bassem',
    author_email='imhoteptech@outlook.com',
    url='https://github.com/Imhotep-Tech/imhotep_files_flask',  # URL of your project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version
    entry_points={
      "console_scripts": [
          "imhotep-files-flask = imhotep_files_flask:hello",
      ],
  },
)
