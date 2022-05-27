import setuptools
from digital_clock import __version__ as version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="digital-clock-Nukecraft5419",
    version=version,
    url="https://github.com/Nukecraft5419/Digital-Clock",
    license="MIT",
    author="Nukecraft5419",
    author_email="nukecraft5419@proton.me",
    description="A customisable and lightweight digital watch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["digital_clock"],
    python_requires=">=3.6",
    classifiers=[
         "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Operating System :: POSIX :: Linux",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
