from distutils.core import setup
from setuptools import find_packages
import os
import sys

this = os.path.dirname(__file__)

packages = find_packages()
assert packages

# read version from the package file.
with (open(os.path.join(this, "hummingbird/__init__.py"), "r")) as f:
    line = [_ for _ in [_.strip("\r\n ") for _ in f.readlines()] if _.startswith("__version__")]
    if len(line) > 0:
        version_str = line[0].split("=")[1].strip('" ')

README = os.path.join(os.getcwd(), "README.md")
with open(README) as f:
    long_description = f.read()
    start_pos = long_description.find("## Introduction")
    if start_pos >= 0:
        long_description = long_description[start_pos:]

install_requires = ["numpy>=1.15", "onnxconverter-common>=1.6.0", "scikit-learn==0.22.1"]
if sys.platform == "darwin" or sys.platform == "linux":
    install_requires.append("torch>=1.4.0")
else:
    if sys.version_info[:2] == (3, 8):
        install_requires.append("torch @ https://download.pytorch.org/whl/cpu/torch-1.5.0%2Bcpu-cp38-cp38-win_amd64.whl")
    elif sys.version_info[:2] == (3, 7):
        install_requires.append("torch @ https://download.pytorch.org/whl/cpu/torch-1.5.0%2Bcpu-cp37-cp37m-win_amd64.whl")
    elif sys.version_info[:2] == (3, 6):
        install_requires.append("torch @ https://download.pytorch.org/whl/cpu/torch-1.5.0%2Bcpu-cp36-cp36m-win_amd64.whl")
    elif sys.version_info[:2] == (3, 5):
        install_requires.append("torch @ https://download.pytorch.org/whl/cpu/torch-1.5.0%2Bcpu-cp35-cp35m-win_amd64.whl")
    else:
        raise Exception("Python version < 3.5 not supported.")
setup(
    name="hummingbird-ml",
    version=version_str,
    description="Convert trained traditional machine learning models into tensor computations",
    license="MIT License",
    author="Microsoft Corporation",
    author_email="hummingbird-dev@microsoft.com",
    url="https://github.com/microsoft/hummingbird",
    packages=packages,
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        "tests": ["flake8", "pytest", "coverage", "pre-commit"],
        "docs": ["pdoc"],
        "onnx": ["onnxruntime>=1.0.0", "onnxmltools>=1.6.0"],
        "extra": [
            # The need each for these depends on which libraries you plan to convert from
            "xgboost==0.90",
            "lightgbm>=2.2",
        ],
    },
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.5",
)
