#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver


browser = webdriver.Firefox()
browser.maximize_window()


# This test will run when 'login_test' is called when invoking -m,
# e.g. 'pytest test_custom_markers.py -m "login_test"'.
# This test will run when 'empty_form_test' is called when invoking -m,
# e.g. 'pytest test_custom_markers.py -m "empty_form_test"'.
@pytest.mark.login_test
@pytest.mark.empty_form_test
def test_assert_empty_login_form():
    browser.get("https://start.engagespark.com/sign-in/")
    assert browser.find_element_by_name("login").get_attribute("value") == ""
    assert browser.find_element_by_name("password").get_attribute("value") == ""


# This test will run when 'login_test' is called when invoking -m,
# e.g. 'pytest test_custom_markers.py -m "login_test"'.
# This test will run when 'empty_form_test' is called when invoking -m,
# e.g. 'pytest test_custom_markers.py -m "empty_form_test"'.
@pytest.mark.login_test
@pytest.mark.input_attribute_test
def test_assert_login_input_field_type():
    browser.get("https://start.engagespark.com/sign-in/")
    assert browser.find_element_by_name("login").get_attribute("type") == "email"
    assert browser.find_element_by_name("password").get_attribute("type") == "password"


# The tests in this class will run when 'signup_test' is called when invoking -m,
# e.g. 'pytest test_custom_markers.py -m "signup_test"'.
@pytest.mark.signup_test
class TestSignupPage:

    # This test will run when 'empty_form_test' is called when invoking -m,
    # e.g. 'pytest test_custom_markers.py -m "empty_form_test"'.
    @pytest.mark.empty_form_test
    def test_assert_empty_signup_form(self):
        browser.get("https://start.engagespark.com/sign-up/")
        assert browser.find_element_by_name("email").get_attribute("value") == ""
        assert browser.find_element_by_name("password1").get_attribute("value") == ""

    # This test will run when 'input_attribute_test' is called when invoking -m,
    # e.g. 'pytest test_custom_markers.py -m "input_attribute_test"'.
    @pytest.mark.input_attribute_test
    def test_assert_signup_input_field_type(self):
        browser.get("https://start.engagespark.com/sign-up/")
        assert browser.find_element_by_name("email").get_attribute("type") == "email"
        assert browser.find_element_by_name("password1").get_attribute("type") == "password"
