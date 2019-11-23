import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create your tests here.
def test_comment_no_login():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/blog/1")
    assert driver.find_element_by_xpath("//*[contains(text(), 'Login to post comments')]")

def test_comment_blank_comment():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/projects")

    login = driver.find_element_by_name("login-button")
    login.click()

    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")

    username.clear()
    password.clear()

    username.send_keys("Harald")
    password.send_keys("x+y=z200")
    password.send_keys(Keys.RETURN)

    time.sleep(0.5)
    driver.get("http://127.0.0.1:8000/blog/1")
    body = driver.find_element_by_name("body")
    submit = driver.find_element_by_name("submit")
    submit.click()
    message = body.get_attribute("validationMessage")
    assert message == "Please fill out this field."

def test_comment_login():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/projects")

    login = driver.find_element_by_name("login-button")
    login.click()

    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")

    username.clear()
    password.clear()

    username.send_keys("Harald")
    password.send_keys("x+y=z200")
    password.send_keys(Keys.RETURN)

    time.sleep(0.5)
    driver.get("http://127.0.0.1:8000/blog/1")
    
    comment_body = driver.find_element_by_name("body")
    comment_body.send_keys("This is a Selenium test comment")
    submit = driver.find_element_by_name("submit")

    submit.click()
    driver.refresh
    assert driver.find_element_by_xpath("//*[contains(text(), 'This is a Selenium test comment')]")