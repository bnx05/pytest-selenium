#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from selenium import webdriver


browser = webdriver.Firefox()
browser.maximize_window()


def test_assert_title_of_homepage():
    browser.get("https://www.engagespark.com/")
    assert browser.title == "Home - Send and Receive Automated Call and SMS Text Campaigns."


def test_assert_presence_of_login_button():
    browser.get("https://www.engagespark.com/")
    assert browser.find_element_by_link_text("login")


def test_assert_availability_of_login_page():
    browser.get("https://www.engagespark.com/")
    browser.find_element_by_link_text("login").click()
    time.sleep(10)
    assert browser.title == "engageSPARK - Sign In"
    assert browser.find_element_by_id("loginform")
