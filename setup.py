from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as fh:
    long_description = fh.read()


setup(
    name="nhl_stats_and_record_scraper",
    version="0.5.0",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "requests",
        "logging",
        "sys"
    ],
)