from setuptools import setup, find_packages



setup(
    name="nhl_stats_and_record_scraper",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "logging"
    ],
)