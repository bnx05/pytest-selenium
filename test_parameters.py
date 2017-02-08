#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from selenium import webdriver


browser = webdriver.Firefox()
email_addresses = ["invalid_email", "another_invalid_email@", "not_another_invalid_email@blah"]
passwords = ["weak_password", "generic_password", "shitty_password"]


@pytest.mark.parametrize("email", email_addresses)
@pytest.mark.parametrize("password", passwords)
def test_assert_login_button_enabled(email, password):
    browser.get("https://start.engagespark.com/sign-in/")
    time.sleep(3)
    browser.find_element_by_name("login").click()
    browser.find_element_by_name("login").send_keys(email)
    browser.find_element_by_name("password").click()
    browser.find_element_by_name("password").send_keys(password)


@pytest.mark.parametrize("field_name, maxlength", [
    ("login", "75"),
    ("password", "128"),
])
def test_assert_field_maxlength(field_name, maxlength):
    browser.get("https://start.engagespark.com/sign-in/")
    time.sleep(3)
    browser.find_element_by_name(field_name).get_attribute("maxlength") == maxlength


@pytest.mark.parametrize("email", [
    "123@abc.org",
    pytest.mark.xfail("blah"),
])
def test_assert_valid_email_entry(email):
    browser.get("https://start.engagespark.com/sign-in/")
    time.sleep(3)
    browser.find_element_by_name("login").click()
    browser.find_element_by_name("login").send_keys(email)
    assert "@" in browser.find_element_by_name("login").get_attribute("value")
