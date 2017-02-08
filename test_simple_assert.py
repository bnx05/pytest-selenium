#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver


browser = webdriver.Firefox()


def test_open_engagespark_homepage():
    browser.get("https://www.engagespark.com/")
    assert "Home" in browser.title


# @pytest.mark.xfail(strict=True)
def test_login_link_available_in_homepage():
    browser.get("https://www.engagespark.com/")
    assert browser.find_element_by_link_text("login")


# @pytest.mark.xfail(reason="needs wait")
def test_open_login_page_from_homepage():
    browser.get("https://www.engagespark.com/")
    browser.find_element_by_link_text("login").click()
    assert "Sign In" in browser.title
    assert browser.find_element_by_id("loginform")
