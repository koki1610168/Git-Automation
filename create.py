from selenium import webdriver
import sys
import os

from config import email, password

FOLDER_NAME = str(sys.argv[1])
FOLDER_KIND = str(sys.argv[2])

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.github.com/login")


def login(email, password, foldername, folderkind):

    os.makedirs("/Users/hachimannoboruju/developments/" + FOLDER_KIND + "/" + FOLDER_NAME)

    #type email address in login field
    driver.find_element_by_id("login_field").send_keys(email)

    #type password
    driver.find_element_by_id("password").send_keys(password)

    #push "Sign in" button at the bottom of the login page
    driver.find_element_by_xpath("//*[@id='login']/form/div[4]/input[9]").submit()

    #go to github.com/new to create a new repository
    driver.get("https://github.com/new")

    #put in the repository name in the repo page
    driver.find_element_by_xpath("//*[@id='repository_name']").send_keys(foldername)

    #push "Create Repository" button at the bottom of the repo page
    driver.find_element_by_xpath("//*[@id='new_repository']/div[3]/button").submit()


login(email, password, FOLDER_NAME, FOLDER_KIND)