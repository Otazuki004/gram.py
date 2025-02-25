from setuptools import setup, find_packages

setup( 
  name="Nexgram.py",
  version="0.0.7",
  packages=find_packages(),
  install_requires=[
    "aiofiles>=24.1.0",
    "pycryptodome>=3.20.0",
  ],
  author="Otazuki",
  author_email="otazuki004@gmail.com",
  description="just a try to beat pyrogram :)",
  long_description=open("README.md").read(),
  long_description_content_type="text/markdown",
  url="https://github.com/Otazuki004/Nexgram.py",
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)