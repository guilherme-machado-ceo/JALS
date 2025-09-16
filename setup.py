from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="jals",
    version="0.1.0",
    author="Guilherme Machado",
    author_email="guilherme.ceo@hubstry.com",
    description="Journey Amplified Language Systems - Framework para amplificação sistêmica da linguagem",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guilherme-machado-ceo/JALS",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=20.8b1",
            "flake8>=3.8.0",
            "jupyter>=1.0.0",
        ],
    },
)