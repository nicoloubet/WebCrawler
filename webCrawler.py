#shift-ctrl-b(run script)
#Next Tue time stamp = 1572332400
from selenium import webdriver
import time

#Opens up the Chrome browser and navigates to the web page.
chromeDriverPath = r"C:\Users\nicol\Downloads\chromedriver_win32\chromedriver.exe"
browser = webdriver.Chrome(chromeDriverPath)
browser.get("https://fantasy.espn.com/football/fantasycast?leagueId=44970803")

#Going to check for timestamp every 60 seconds until timestamp is met in loop
while time.time()<=1572107400:
    time.sleep(60)

#Add player from watchlist page
browser.find_element_by_css_selector("#espn-analytics > div > div.jsx-3010562182.shell-container > div.page-container.cf > div.layout.is-full > div > div > div > div.jsx-2968158442.container.page-contents.generic--container > div.jsx-1618617030.players-table__sortable.tc > section > table > tbody > tr > td > div > div > div.Table2__shadow-scroller > table > tbody > tr > td > div > table > tbody > tr > td:nth-child(3) > div > div > div > button.btn.btn--custom.add-action-btn.clr-positive.mh2.btn--sm").click()

#Sleeps for one seconcd closes the browser then..
#Exiting python session
time.sleep(1)
browser.close()
quit()
