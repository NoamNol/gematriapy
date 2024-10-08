import setuptools
import gematriapy

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gematriapy",
    version=gematriapy.__version__,
    author="Noam Nol",
    author_email="noamnol19@gmail.com",
    description=gematriapy.__doc__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NoamNol/gematriapy",
    packages=['gematriapy'],
    package_data={
        'gematriapy': ['py.typed'],
    },
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Development Status :: 4 - Beta',
    ],
    keywords="hebrew gematria gematriapy",
    python_requires='>=3.7',
)
