#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from selenium import webdriver


browser = webdriver.Firefox()
browser.maximize_window()


# This test will run but will be marked as 'xfail' if it fails; however, it will
# be marked as 'xpass' if it passes.
@pytest.mark.xfail(reason="button is disabled")
def test_assert_login_with_empty_fields():
    browser.get("https://start.engagespark.com/sign-in/")
    browser.find_element_by_xpath("//button[contains(text(), 'Login')]").click()


class TestSignupPage:

    # This test will run but will be marked as 'xfail' if it fails; however, it
    # will be marked as 'xpass' if it passes.
    @pytest.mark.xfail(strict=True, reason="button is disabled")
    def test_signup_with_empty_fields(self):
        browser.get("https://start.engagespark.com/sign-up/")
        browser.find_element_by_xpath("//button[contains(text(), 'Sign Up')]").click()
