import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyDSP",
    version="0.1.0",
    author="Tobias Hienzsch",
    author_email="post@tobias-hienzsch.de",
    description="Python audio dsp utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tobanteAudio/pyDSP",
    project_urls={
        "Bug Tracker": "https://github.com/tobanteAudio/pyDSP/issues",
    },
    python_requires=">=3.7",
)
