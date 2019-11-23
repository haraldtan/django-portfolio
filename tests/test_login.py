import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create your tests here.
def test_login():
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
    submit = driver.find_element_by_name("submit")

    submit.click()

    time.sleep(0.5)

    assert driver.find_element_by_name("logout-button")

def test_login_wrong_pass():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/projects")

    login = driver.find_element_by_name("login-button")
    login.click()

    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")

    username.clear()
    password.clear()

    username.send_keys("Harald")
    password.send_keys("MicWord1")
    submit = driver.find_element_by_name("submit")

    submit.click()

    time.sleep(0.5)
    assert driver.find_element_by_xpath("//*[contains(text(), 'Please enter a correct username and password. Note that both fields may be case-sensitive.')]")

def test_login_other_user():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/projects")

    login = driver.find_element_by_name("login-button")
    login.click()

    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")

    username.clear()
    password.clear()

    username.send_keys("otheruser")
    password.send_keys("MicWord1")
    submit = driver.find_element_by_name("submit")

    submit.click()

    time.sleep(0.5)

    assert driver.find_element_by_name("logout-button")

def test_check_redirect():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/projects")

    login = driver.find_element_by_name("login-button")
    login.click()

    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")

    username.clear()
    password.clear()

    username.send_keys("otheruser")
    password.send_keys("MicWord1")
    submit = driver.find_element_by_name("submit")

    submit.click()

    time.sleep(0.5)

    assert driver.current_url == "http://127.0.0.1:8000/projects/"

def test_check_login_admin():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")

    username.clear()
    password.clear()

    username.send_keys("Harald")
    password.send_keys("x+y=z200")
    password.send_keys(Keys.RETURN)
    time.sleep(0.5)
    assert driver.current_url == "http://127.0.0.1:8000/admin/"

def test_check_login_admin_wrong_pass():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")

    username.clear()
    password.clear()

    username.send_keys("Harald")
    password.send_keys("MicWord1")
    password.send_keys(Keys.RETURN)
    time.sleep(0.5)
    assert driver.find_element_by_xpath("//*[contains(text(), 'Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive.')]")

def test_check_login_admin_non_admin():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")

    username.clear()
    password.clear()

    username.send_keys("otheruser")
    password.send_keys("MicWord1")
    password.send_keys(Keys.RETURN)
    time.sleep(0.5)
    assert driver.find_element_by_xpath("//*[contains(text(), 'Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive.')]")