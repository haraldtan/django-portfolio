import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_access_projects():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/projects")
    home = driver.find_element_by_name("home")
    home.click()
    assert driver.current_url == "http://127.0.0.1:8000/projects/"

def test_access_projects_wrong():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/project")
    time.sleep(0.5)
    assert driver.find_element_by_xpath("//*[contains(text(), '404')]")

def test_access_blog():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/projects")
    blog = driver.find_element_by_name("blog")
    blog.click()
    assert driver.current_url == "http://127.0.0.1:8000/blog/"

def test_access_blog_wrong():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/blogs")
    time.sleep(0.5)
    assert driver.find_element_by_xpath("//*[contains(text(), '404')]")

def test_access_blog_post():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/projects")
    blog = driver.find_element_by_name("blog")
    blog.click()
    post = driver.find_element_by_xpath("//a[@href='/blog/1/']")
    post.click()
    assert driver.current_url == "http://127.0.0.1:8000/blog/1/"

def test_access_blog_post_wrong():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/blog/2")
    time.sleep(0.5)
    assert driver.find_element_by_xpath("//*[contains(text(), 'DoesNotExist')]")

def test_access_login():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/projects")
    login = driver.find_element_by_name("login-button")
    login.click()
    assert driver.current_url == "http://127.0.0.1:8000/accounts/login/"

def test_access_login_wrong():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/login")
    time.sleep(0.5)
    assert driver.find_element_by_xpath("//*[contains(text(), '404')]")

def test_access_admin():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/admin")
    assert driver.current_url == "http://127.0.0.1:8000/admin/login/?next=/admin/"

def test_access_admin_wrong():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/admins")
    time.sleep(0.5)
    assert driver.find_element_by_xpath("//*[contains(text(), '404')]")