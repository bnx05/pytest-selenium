# pytest + selenium: demo tests

## Setup instructions (this assumes that you already have Python and pip installed)

- If you clone this repo, you can do `pip install -r requirements.txt` to install both pytest and
selenium at once. Otherwise, you can install them one by one. Note that you will still need to install geckodriver, since Selenium 3 does not support default Firefox:


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

#### Unix

- Download tar file from [geckodriver](https://github.com/mozilla/geckodriver/releases)
- Go to download location and extract the file:
```
tar -xvzf geckodriver
```
- Make geckodriver executable:
```
chmod +x geckodriver
```
- Add geckodriver executable to your `PATH`. The default `PATH` is set in the `/etc/environment`
file. Add the location there if it is not already set, e.g.
```
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:<geckodriver location>"
```
- Alternatively, you can move the executable to the location/s specified in your `PATH` variable

#### Windows

- Download and extract zip file from [geckodriver](https://github.com/mozilla/geckodriver/releases)
- Get the executable file's location and add it to your Environment Variables. Instructions on
setting the path can be found [here](http://www.computerhope.com/issues/ch000549.htm)

## How to run the tests

- To run all tests inside the test directory, simply run this command:
```
pytest
or python -m pytest
```
This will open multiple Firefox browsers, since each module is calling a separate Firefox instance.
- To run a test module, simply do
```
pytest <module name>
e.g. pytest test_markers.py
```
- To run a specific test, do
```
pytest <module name> <class name> <test name>
e.g. pytest test_markers.py::TestSignupPage::test_assert_empty_signup_form
```
- It is recommended to run the tests with verbosity by invoking `-v` during the test run.
- If there are `print` statements you wish to see on the console when the tests run, add `-s` to disable stdout
capturing.
