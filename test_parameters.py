#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from selenium import webdriver


sample_email_address = "demo@engagespark.com"
sample_password = "Password123"
email_addresses = ["invalid_email", "another_invalid_email@", "not_another_invalid_email@blah"]
passwords = ["weak_password", "generic_password", "bleep_password"]


browser = webdriver.Firefox()
browser.maximize_window()


# this test checks the maxlength attribute of the login and password fields
@pytest.mark.parametrize("field_name, maxlength", [
    ("login", "75"),
    ("password", "128"),
])
def test_assert_field_maxlength(field_name, maxlength):
    browser.get("https://start.engagespark.com/sign-in/")
    time.sleep(5)
    browser.find_element_by_name(field_name).get_attribute("maxlength") == maxlength


# this test asserts the string length of values entered in the login and
# password fields
@pytest.mark.parametrize("field_name, sample_string, string_length", [
    ("login", sample_email_address, 20),
    ("password", sample_password, 11),
])
def test_assert_email_and_password_length(field_name, sample_string, string_length):
    browser.get("https://start.engagespark.com/sign-in/")
    time.sleep(5)
    browser.find_element_by_name(field_name).click()
    browser.find_element_by_name(field_name).send_keys(sample_string)
    assert len(browser.find_element_by_name(field_name).get_attribute("value")) == string_length


# this test checks if the login button is enabled after entering different
# combinations of invalid values in the email and password fields
@pytest.mark.parametrize("email", email_addresses)
@pytest.mark.parametrize("password", passwords)
def test_assert_login_button_enabled(email, password):
    browser.get("https://start.engagespark.com/sign-in/")
    time.sleep(5)
    browser.find_element_by_name("login").click()
    browser.find_element_by_name("login").send_keys(email)
    browser.find_element_by_name("password").click()
    browser.find_element_by_name("password").send_keys(password)
    assert browser.find_element_by_xpath("//button[contains(text(), 'Login')]").is_enabled()


# this test checks if the values entered into the email field contain '@'
@pytest.mark.parametrize("email", [
    "123@abc.org",
    "info@engagespark.com",
    "blah",
])
def test_assert_valid_email_entry(email):
    browser.get("https://start.engagespark.com/sign-in/")
    time.sleep(5)
    browser.find_element_by_name("login").click()
    browser.find_element_by_name("login").send_keys(email)
    assert "@" in browser.find_element_by_name("login").get_attribute("value")
