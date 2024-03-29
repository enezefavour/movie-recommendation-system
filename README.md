# Movie Recommendation System

## Requirements

Python 3.3+

## Project Setup

Make sure you are at the root of `server/` directory.

> `cd server`

### Create a virtual environment for this project with python venv

> `python3 -m venv venv`

For Windows:

> `python -m venv venv`

### Activate the virtual environment

For Linux/MacOS, run:

> `source venv/bin/activate`

For Windows Powershell, run:

> `venv/Scripts/Activate.ps1`

For Windows CMD, run:

> `venv/Scripts/activate.bat`

### Install Packages

Run:

> `pip install -r requirements.txt`

_Please update the requirements.txt file when you add a new package_

Run `pip freeze` and copy the content of the output to the `requirements.txt` file

### Download Datasets

Run the download script to download the datasets zip file.

Run:

> `python data/download.py`

Or

> `python data/download.py small`

_Downloads the small datasets file, ml-latest-small.zip (1MB)_

> `python data/download.py large`

_Downloads the large datasets file ml-latest.zip (256MB)_
