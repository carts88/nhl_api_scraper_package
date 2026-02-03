from setuptools import setup, find_packages

setup(
    name="NHL-Stats-and-Record-Scraper",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",

    ],
    entry_points={
        "console_scripts": [
            "nhl-scraper=nhl_scraper:main"
        ]
    }
)