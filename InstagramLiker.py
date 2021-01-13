from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os



username = '_durachello_'
password = 'DSAqwe321'
tags = "dogphoto"
hashtags = tags.split("#")
urlTag = 'https://www.instagram.com/explore/tags/'

def Sleep(time: int, showStat: bool = False, now: int = 0, _all: int = 0) -> None:
    for i in range(time):
        if showStat == False:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("{} secs left of {}".format(i + 1, time))
            sleep(1)
        if showStat == True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("{} secs left of {}".format(i + 1, time))
            print("#{} of #{}".format(now, _all))
            sleep(1)

driver = webdriver.Firefox()
driver.get("http://www.instagram.com")

Sleep(10)

driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(username)
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(password)

print("Username entered")
print("Password entered")

driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()
Sleep(5)

for hashtag in hashtags:
    HowManyToLike = 100
    HowManyLiked = 0
    driver.get(urlTag + hashtag + "/")
    Sleep(5)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]").click()
    Sleep(3)
    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]").click()
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a").click()
    HowManyLiked += 1
    Sleep(3, True, HowManyLiked, HowManyToLike)
    for i in range(HowManyToLike - 1):
        try:
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]").click()
            driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]").click()
            HowManyLiked += 1
            Sleep(3, True, HowManyLiked, HowManyToLike)
        except Exception:
            driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]").click()
            Sleep(3, True, HowManyLiked, HowManyToLike)
        
