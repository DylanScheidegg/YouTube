from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_binary
import os
import time

keyboard = Controller()
browser = webdriver.Chrome()

userName = 'Gmail in this format'
passWord = 'Password this format'
videoLink = 'Video Link this format'

comments = ['Comments in', 'this format']


def open_video(video):
    browser.get(video)


def like_video():
    likeClick = browser.find_element_by_xpath("//*[@id='top-level-buttons']/ytd-toggle-button-renderer[1]/a")
    likeClick.click()


def comment_section(comment):
    commentClick = browser.find_element_by_id('placeholder-area')
    ActionChains(browser).move_to_element(commentClick).perform()
    commentClick.click()
    keyboard.type(comment)
    time.sleep(2)
    submit = browser.find_element_by_xpath("//*[@id='submit-button']")
    submit.click()
    time.sleep(5)


def __login_google__(email, password):
    browser.get(
        'https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    time.sleep(3)
    emailElem = browser.find_element_by_class_name("Xb9hP")
    emailElem.click()
    keyboard.type(email)
    time.sleep(3)
    nextClick = browser.find_element_by_class_name("CwaK9")
    nextClick.click()
    time.sleep(5)
    passWordElem = browser.find_element_by_class_name("Xb9hP")
    passWordElem.click()
    keyboard.type(password)
    time.sleep(3)
    signInElem = browser.find_element_by_class_name("CwaK9")
    signInElem.click()
    time.sleep(5)
    keyboard.press(Key.esc)
    time.sleep(5)
    open_video(videoLink)
    time.sleep(2)
    like_video()
    time.sleep(5)
    keyboard.press(Key.end)
    time.sleep(5)
    keyboard.press(Key.end)
    time.sleep(1)
    keyboard.press(Key.page_up)
    for x in comments:
        comment_section(x)


__login_google__(userName, passWord)
browser.close()
