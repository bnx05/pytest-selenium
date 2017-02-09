# pytest + selenium: demo tests

## Setup instructions (this assumes that you already have Python and pip installed)

- If you clone this repo, you can do `pip install -r requirements.txt` to install both pytest and
selenium at once. Otherwise, you can install them one by one:

### pytest

- Install [pytest](http://doc.pytest.org/en/latest/getting-started.html) via pip or easy_install:
```
pip install -U pytest or easy_install -U pytest
```
- After installation, you can check the installed version by running:
```
pytest --version
```

### selenium webdriver

- Install [selenium](http://selenium-python.readthedocs.io/installation.html) via pip:
```
pip install -U selenium
```

### geckodriver

- Download tar file from [geckodriver](https://github.com/mozilla/geckodriver/releases)
- Go to download location and extract the file:
```
tar -xvzf geckodriver
```
- Make geckodriver executable:
```
chmod +x geckodriver
```
- Add geckodriver executable to your `PATH`, or you can move the executable to the location/s
specified in your `PATH` variable.

## How to run the tests

- To run all tests at once, simply run this command inside the test directory:
```
pytest or python -m pytest
```
This will open multiple Firefox browsers, since each module is calling a separate Firefox instance.
- To run a specific test module, simply do
```
pytest <module name> e.g. pytest test_markers.py
```
- It is recommended to run the tests with verbosity by adding `-v` invocation during the test run.
- If there are `print` statements you wish to see when the tests run, add `-s` to disable stdout
capturing.
