from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd



PATH = "" #location of the chrome webdriver for selenium
URL = "https://www.jobbank.gc.ca/youth"
What = "programmer"
Where = "Québec"
driver = webdriver.Chrome(PATH)

def getIn(url, what, where): #searching for the job
    driver.get(URL)
    driver.set_window_size(1920, 1080) #full screen ish because there's some weird bugs if small window
    search_title = driver.find_element_by_xpath('//*[@id="searchString"]')
    search_title.clear()
    search_title.send_keys(what)
    search_location = driver.find_element_by_xpath('//*[@id="locationstring"]')
    search_location.clear()
    search_location.send_keys(where)
    search_button = driver.find_element_by_xpath('//*[@id="searchSubmit"]')
    search_button.click()
    driver.implicitly_wait(10)
    
    return

def getURL():
    for i in range(20): #prob less than 20 pages right?
        try:
            next_page = driver.find_element_by_xpath('//*[@id="moreresultbutton"]')
            next_page.click()
            time.sleep(0.5) 
        except:
            break

    Jobs = driver.find_elements_by_class_name("resultJobItem")
    for job in Jobs:
        links.append(job.get_attribute("href"))
    return 

def getINFO(url):
    driver.get(url)
    Button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "applynowbutton"))
    )
    Button.click()

    #mail has a waiting time
    time.sleep(1)
    Title = driver.find_element_by_xpath('/html/body/main/section[1]/div[2]/div[1]/div[1]/h2/span')
    Company = driver.find_element_by_xpath('/html/body/main/section[1]/div[2]/div[1]/div[1]/p/span[3]/span[2]/span/strong')
    Mail = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/main/section[1]/div[2]/div[1]/div[1]/div/div[1]/p[1]"))
    )
    Language = driver.find_element_by_xpath('/html/body/main/section[1]/div[2]/div[1]/div[1]/ul/li[3]')
    print(Mail.text)
    job_info = {'title':Title.text, 'company':Company.text, 'email':Mail.text, 'language': Language.text[10:]}

    listINFO.append(job_info)


#MAIN
#getIn(URL, What, Where) because doing only french, so links is already done
driver.get('https://www.guichetemplois.gc.ca/jobsearch/rechercheemplois?flg=F&fcid=5005&fcid=19836&fcid=22587&fcid=22611&fcid=22612&fcid=22613&fcid=22614&fcid=22616&fcid=22617&fcid=22618&fcid=22619&fn=2174&term=programmer&sort=M&fprov=QC&fsrc=21#results-list-content')
time.sleep(1)
driver.set_window_size(1920, 1080)

links = []
listINFO= []
getURL()

for i in links:
    getINFO(i)
print(listINFO)
df = pd.DataFrame(listINFO)
print(df.head())
df.to_csv('New.csv', encoding='latin1')

