from linkedin_messages.Data.targetProfileDetails import targetProfileDetails
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def load_page(driver, url):
    driver.get(url)
    start = time.time()
    initialScroll = 0
    finalScroll = 1000
    while True:
        driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
        initialScroll = finalScroll
        finalScroll += 1000
        time.sleep(2)
        end = time.time()
        if round(end - start) > 20:
            break
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
    return soup



def scrape_details(data):
    print(data)
    driver = webdriver.Chrome() 
    driver.get("https://linkedin.com/uas/login")
    print(driver.title)

    time.sleep(2)

    username = driver.find_element(By.ID, "username")
    username.send_keys(data.username) 
    pword = driver.find_element(By.ID, "password")
    pword.send_keys(data.password)	 
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    profile_url = str(data.profileUrl)
    soup = load_page(driver, profile_url)
    details = soup.find('div', {'class': 'mt2 relative'})
    name_loc = details.find("h1")
    name = name_loc.get_text().strip()
    location_loc = details.find_all("span", {'class': 'text-body-small inline t-black--light break-words'})
    location = location_loc[0].get_text().strip()

    posts_url = str(data.profileUrl)+"/recent-activity/all/"
    soup = load_page(driver, posts_url)
    allActivities = soup.find('div', {'class': 'pv-recent-activity-detail__core-rail'})
    post_loc = allActivities.find('ul')
    posts = []
    h2 = post_loc.find_all("span",{'class':'break-words tvm-parent-container'})
    for i in range(0,5):
        p = h2[i].find("span",{'dir':'ltr'}).get_text().strip()
        posts.append(p)

    user_details = {
        "name": name,
        "location": location,
        "posts": posts
    }

    targetProfileDetails.objects.create(name=name,
                                        location=location,
                                        profile_url=str(data.profileUrl),
                                        posts=posts
    )

    return user_details

