import setuptools
from digital_clock import __version__ as version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="digital-clock-Nukecraft5419",
    version=version,
    author="Nukecraft5419",
    author_email="author@example.com",
    description="A customisable and lightweight digital watch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nukecraft5419/Digital-Clock",
    project_urls={
        "Bug Tracker": "https://github.com/Nukecraft5419/Digital-Clock/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)