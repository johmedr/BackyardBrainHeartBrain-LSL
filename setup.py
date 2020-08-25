import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="byb2lsl", # Replace with your own username
    version="0.0.2",
    author="Johan Medrano",
    author_email="johan.medrano@umontpellier.fr",
    description="A driver to connect the Heart&Brain kit from Backyard Brain to the LabStreamingLayer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yop0/BackyardBrainHeartBrain-LSL",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
       'pylsl',
       'pyserial'
    ],
    python_requires='>=2.7',
)