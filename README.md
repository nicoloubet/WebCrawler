# WebCrawler
## Tools
- Selenium
- ChromeDriver
## Motivation
The main reason i created this was because the wavier wire for my fantasy league opens up at 2am every Tuesday morning.
I personally do not find it fun to set an alarm or stay up until 2am to select a player.
## How it works/What it is doing
 In a nut shell all Selenium is doing is opening the browswer and selecting the player i specify. 
 1. Open browser
 2. Manually sign in
 3. Manually navigate too watch list where i already have the player i wish to select
 4. Searches for timestamp i specify every 60 seconds 
 5. Selects the add button by unique CSS Selector (which adds him to my roster)
 6. Closes browser/Exiting python session
