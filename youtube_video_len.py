# Chnage url to your playlist url in line no 9.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime as dt
import time

driver = webdriver.Chrome()
# Enter your playlist URL here
url = "https://www.youtube.com/playlist?list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go"
driver.get(url)

html_elm = driver.find_element_by_tag_name('html')
no_of_videos = driver.find_element_by_css_selector(
    "#stats > yt-formatted-string:nth-child(1) > span:nth-child(1)").text.strip()
no_of_videos = int(no_of_videos)

# no of down arrow presses
for i in range(no_of_videos*2):
    html_elm.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.05)
    if i % 100 == 0:
        time.sleep(1)

contents = driver.find_element_by_css_selector(
    "#contents").find_elements_by_id("content")
total_time = dt.timedelta()

for c in contents:
    time_elm = c.find_element_by_tag_name("span").text
    h = '0'
    if len(time_elm.split(':')) == 3:
        h, m, s = time_elm.split(':')
    elif len(time_elm.split(':')) == 2:
        m, s = time_elm.split(':')
    print(time_elm)
    time = dt.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    total_time += time

print('\nNumber of avaiable videos: ' + str(len(contents)))
print('\nPlaylist time: ' + str(total_time))

driver.quit()
