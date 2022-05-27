from setuptools import setup

APP=["digital_clock.py"]
OPTIONS={"argv_emulation": True, "iconfile": "/icons/digital_clock-logo.png"}


setup(
    app=APP,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)