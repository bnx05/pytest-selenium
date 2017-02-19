#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Prior to running this module, set the environment variable "URL" first.
# Set the value to "https://start.engagespark.com/sign-in/" for the Login test.
# For the Signup test, set the value to https://start.engagespark.com/sign-up/".


class Base:

    # This fixture contains the set up and tear down code for each test.
    @pytest.fixture(autouse=True)
    def browser_setup_and_teardown(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 30)
        yield
        self.browser.close()
        self.browser.quit()

    # This fixture opens the URL set in the environment variable and waits
    # until a form is visible before proceeding.
    @pytest.fixture()
    def open_url(self):
        self.browser.get(os.getenv("URL"))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form")))

    def enter_credentials(self, input_field, credential):
        self.browser.find_element_by_name(input_field).click()
        self.browser.find_element_by_name(input_field).send_keys(credential)


class TestSignup(Base):

    # When this test runs, it will use the 'browser_setup_and_teardown' fixture first, followed by
    # the 'open_url' fixture before running the test itself.
    @pytest.mark.usefixtures("open_url")
    def test_signup_without_captcha(self):
        print("Setting email for sign up")
        self.enter_credentials(input_field="email", credential="sample_email@blah.org")
        print("Setting password for sign up")
        self.enter_credentials(input_field="password1", credential="password1")
        self.browser.find_element_by_css_selector("input[type='checkbox']").click()
        assert not self.browser.find_element_by_css_selector("#signupform button").is_enabled()


class TestLogin(Base):

    # When this test runs, it will use the 'browser_setup_and_teardown' fixture first, followed by
    # the 'open_url' fixture before running the test itself.
    @pytest.mark.usefixtures("open_url")
    def test_login_with_inexistent_accounts(self):
        print("Setting email for sign up")
        self.enter_credentials(input_field="login", credential="another_imaginary_email@blah.org")
        print("Setting password for sign up")
        self.enter_credentials(input_field="password", credential="password2")
        self.browser.find_element_by_css_selector("#loginform button").click()
        print("Error notification should appear")
        self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "notification-message"), "The e-mail address and/or password you specified are not correct."))
