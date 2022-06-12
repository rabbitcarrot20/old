import setuptools
 
with open("README.md", "r",encoding = 'UTF8') as fh:
    long_description = fh.read()

project_urls_ = {
    'Link 1' : 'https://github.com/rabbitcarrot20
    'Link 2' : 'https://github.com/gadarangeo
}
    
setuptools.setup(
    name="korean_holiday_calendar",
    version="0.0.2",
    author="rabbitcarrot20, gadarangeo",
    author_email="butterfly36082@gmail.com, yuuhy1020@gmail.com",
    description="korean holiday calendar based on holidays package by dr-prodigy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rabbitcarrot20/korean_holiday_calendar",
    project_urls = project_urls_
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)