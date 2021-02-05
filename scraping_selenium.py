from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.chrome import service

#Opera browser
#webdriver_service = service.Service('C:\Program Files (x86)\operadriver.exe')
#webdriver_service.start()
#driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)


#Chrome browser
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


name_city = []
email = []


def get_profiles(driver, n_page=2):
    """Get web site and find all profiles"""

    for i in range(1, 26):   #search by cities
        page = 1
        while page != n_page:  # number of pages
            try:
                URL = f'https://upsihologa.com.ua/baza-city-{i}-page-{page}.htm'
                driver.get(URL)
                time.sleep(3)
                
                search_profiles = driver.find_elements_by_class_name("roundedtablenew2")
                get_content(driver, search_profiles)
                page += 1
            except:
                pass


def get_content(driver, search_profiles):
    for profiles in search_profiles:
        time.sleep(1)

        #geting name
        name_city.append(profiles.find_element_by_class_name("righttitlename").text)
        driver.implicitly_wait(10)
        
        #clicking a button and getting an email
        profiles.find_element_by_name("submit").click()
        time.sleep(1)
        contact = profiles.find_element_by_class_name("shownemail")
        time.sleep(1)
        email.append(contact.find_element_by_tag_name("div").text)


def write_down(name_city, email):
    """writing down content to csv file using pandas library"""

    psychologists = pd.DataFrame(
        {
            "name_city": name_city,
            "email": email
        })
    
    psychologists.to_csv("Psychologists.csv")


if __name__ == '__main__':
    get_profiles(driver, 3)
    write_down(name_city, email)
