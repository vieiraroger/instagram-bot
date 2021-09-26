from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Stalker():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.get('https://www.instagram.com/')
    
    def teste(self):
        try:
            img = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[4]/article/div/div/div[1]/div[1]/a')
            print("deu")
        except: 
            print("num deu")


    def get_photos_link(self, times=3):
        for i in range(times):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        hrefs = self.driver.find_elements_by_tag_name('a')
        #photos_hrefs
        print(hrefs)
        photos_link = []
        for i in range(len(hrefs)):
            href = hrefs[i].get_attribute('href')
            if(href.startswith('https://www.instagram.com/p/')):
                photos_link.append(href)

        return photos_link

    def like_all_photos(self, name):
        self.driver.get('https://www.instagram.com/' + name + '/')
        time.sleep(3)
        
        photos_link = self.get_photos_link()

        for photo_link in photos_link:
            self.driver.get(photo_link)
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()


    def trolar_jackson(self, arroba):
        self.driver.get('https://www.instagram.com/explore/tags/instasorteios/')
        time.sleep(3)
        
        photos_link = self.get_photos_link(5)
        print(len(photos_link))
        for photo_link in photos_link:
            self.driver.get(photo_link)
            time.sleep(3)
            comment = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
            time.sleep(1)
            comment.click()
            comment = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
            comment.clear()

            comment.send_keys(arroba)

            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]').click()
            time.sleep(3)


st = Stalker()
time.sleep(10)
# st.like_all_photos('nomedeusuario')
#st.trolar_jackson("@nomedeusuario")