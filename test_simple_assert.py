#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver


browser = webdriver.Firefox()


def test_assert_title_of_homepage():
    browser.get("https://www.engagespark.com/")
    assert browser.title == "Home - Send and Receive Automated Call and SMS Text Campaigns."


@pytest.mark.xfail()
def test_assert_presence_of_login_link():
    browser.get("https://www.engagespark.com/")
    assert browser.find_element_by_link_text("login")


@pytest.mark.xfail(reason="needs wait")
def test_assert_login_page():
    browser.get("https://www.engagespark.com/")
    browser.find_element_by_link_text("login").click()
    assert browser.title == "engageSPARK - Sign In"
    assert browser.find_element_by_id("loginform")
