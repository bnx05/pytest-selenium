#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from selenium import webdriver


browser = webdriver.Firefox()
browser.maximize_window()


# This test will not run since it has been marked 'skip'
@pytest.mark.skip(reason="reset password unavailable from navbar")
def test_assert_reset_password_in_navbar():
    browser.get("https://start.engagespark.com/sign-in/")
    assert browser.find_element_by_css_selector("ul[class*='navbar-right'] a[href='/reset-password/']")


# The tests in this class will not run if the browser instance uses PhantomJS
@pytest.mark.skipif(
    browser == webdriver.PhantomJS, reason="headless browser not suitable for demo")
class TestSignupPage:

    def test_assert_terms_of_service_link_in_form(self):
        browser.get("https://start.engagespark.com/sign-up/")
        time.sleep(10)
        assert browser.find_element_by_link_text("Terms of Service")
