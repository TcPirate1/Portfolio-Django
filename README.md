# Portfolio website
Welcome to my website repository.

This is created with Django as a way to practice the framework but also as a replacement for the previous templated HTML/CSS site I used to use.

## Setting up the repository locally
- Clone the repo to whichever directory you desire. Make note of which OS its on
- [Create a Python virtual environment](#Creating-the-Python-virtual-environment)
- [Activate the virtual environment](#Activating-Python-virtual-environment) and install the dependencies with `
py -m pip install -r requirements.txt` on Windows and `python -m pip install -r requirements.txt` on Unix/Mac
- Use `py manage.py runserver` for Windows and `python3 manage.py runserver` for Unix/Mac, to start the site on a Django development server.

## Creating the Python virtual environment
`py -m venv <file name>` - Windows

`python3 -m venv <file name>` - Unix/Mac

## Activating Python virtual environment
`<file name>\Scripts\activate` - Windows

`source <file name>/bin/activate` - Unix/Mac