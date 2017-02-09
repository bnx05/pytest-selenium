#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


'''
Prior to running this module, set the environment variable "URL" first. Set the value to
"https://start.engagespark.com/sign-in/" for the Login test. For the Signup test, set the value to
"https://start.engagespark.com/sign-up/"
'''


class Base:

    @pytest.fixture(autouse=True)
    def browser_setup_and_teardown(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 30)
        yield
        self.browser.close()
        self.browser.quit()

    @pytest.fixture()
    def open_url(self):
        self.browser.get(os.getenv("URL"))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form")))

    def enter_credentials(self, input_field, credential):
        self.browser.find_element_by_name(input_field).click()
        self.browser.find_element_by_name(input_field).send_keys(credential)


class TestSignup(Base):

    @pytest.mark.skipif("sign-up" not in os.getenv("URL"), reason="url provided is incorrect")
    @pytest.mark.usefixtures("open_url")
    @pytest.mark.parametrize("email, password", [
        ("sample_email@blah.org", "password1"),
        ("not_another_email@blah.org", "password2"),
    ])
    def test_signup_without_captcha(self, email, password):
        print("Setting email for sign up")
        self.enter_credentials(input_field="email", credential=email)
        print("Setting password for sign up")
        self.enter_credentials(input_field="password1", credential=password)
        self.browser.find_element_by_css_selector("input[type='checkbox']").click()
        assert not self.browser.find_element_by_css_selector("#signupform button").is_enabled()


class TestLogin(Base):

    @pytest.mark.skipif("sign-in" not in os.getenv("URL"), reason="url provided is incorrect")
    @pytest.mark.usefixtures("open_url")
    @pytest.mark.parametrize("email, password", [
        ("ghost_email_woo@blah.org", "password1"),
        ("my_imaginary_email@blah.org", "password2"),
        pytest.mark.xfail(
            (os.getenv("VALID_EMAIL"), os.getenv("VALID_PASSWORD")))
    ])
    def test_login_with_inexistent_accounts(self, email, password):
        print("Setting email for sign up")
        self.enter_credentials(input_field="login", credential=email)
        print("Setting password for sign up")
        self.enter_credentials(input_field="password", credential=password)
        self.browser.find_element_by_css_selector("#loginform button").click()
        print("Error notification should appear")
        self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "notification-message"), "The e-mail address and/or password you specified are not correct."))
