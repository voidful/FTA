from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='fta',
    version='0.0.14',
    description='',
    url='https://github.com/voidful/FTA',
    author='Voidful',
    author_email='voidful.stack@gmail.com',
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    setup_requires=['setuptools-git'],
    classifiers=[
        'Development Status :: 4 - Beta',
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python"
    ],
    license_files="Apache",
    keywords='finance',
    packages=find_packages(),
    install_requires=required,
    zip_safe=False,
)
