#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver


browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://start.engagespark.com/sign-in/")


@pytest.mark.login_test
@pytest.mark.attribute_test
def test_assert_empty_login_form():
    assert browser.find_element_by_name("login").get_attribute("value") == ""
    assert browser.find_element_by_name("password").get_attribute("value") == ""


@pytest.mark.login_test
@pytest.mark.xfail(reason="button is disabled")
def test_login_empty_fields():
    browser.find_element_by_xpath("//button[contains(text(), 'Login')]").click()


class TestSignupPage:

    @pytest.mark.signup_test
    @pytest.mark.attribute_test
    def test_assert_empty_signup_form(self):
        assert browser.find_element_by_name("login").get_attribute("value") == ""
        assert browser.find_element_by_name("password1").get_attribute("value") == ""

    @pytest.mark.signup_test
    @pytest.mark.xfail(reason="button is disabled")
    def test_signup_empty_fields(self):
        browser.find_element_by_xpath("//button[contains(text(), 'Sign Up')]").click()
