import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gematriapy",
    version="0.1.0",
    author="Noam Nol",
    author_email="noamnol19@gmail.com",
    description="Convert numbers to Hebrew letters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NoamNol/gematriapy",
    packages=['gematriapy'],
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
