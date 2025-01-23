from setuptools import setup, find_packages

setup(
    name="gpt_trainer_api",
    version="0.2.3",
    description="Python client for interacting with the GPT Trainer API.",
    long_description=open("README.md", "r").read() + "\n\n" + open("CHANGELOG.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Tahir Siddique",
    author_email="tahirsiddiquework@gmail.com",
    url="https://github.com/Tahir-Siddique/gpt-trainer-api",
    packages=find_packages(),
    install_requires=[
        "requests>=2.32.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    project_urls={
        "Source": "https://github.com/Tahir-Siddique/gpt-trainer-api",
        "Tracker": "https://github.com/Tahir-Siddique/gpt-trainer-api/issues",
    },
)
