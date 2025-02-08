from setuptools import setup, find_packages

setup(
    name="pdf-info-retrieval",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
        "PyPDF2",
    ],
    entry_points={
        "console_scripts": [
            # Add command line scripts here
        ],
    },
    author="shweta",
    author_email="your.email@example.com",
    description="A project for retrieving information from PDF files",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pdf-info-retrieval",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)