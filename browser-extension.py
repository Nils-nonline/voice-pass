from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import json
# create action chain object
from urllib.parse import urlparse


options = webdriver.FirefoxOptions()
#options.add_argument('-headless')
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "")
options.set_preference("browser.download.dir", "/dev/null")
options.set_preference('permissions.default.stylesheet', 2)
options.set_preference('permissions.default.image', 2)
options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
options.set_preference("media.autoplay.default", 0)
options.add_argument('--blink-settings=imagesEnabled=false')

# Create FirefoxDriver with the modified options
driver = webdriver.Firefox(options=options)
action = ActionChains(driver)

#driver.get(url)
html = """
<h1> Locked </h1>
Use your voice to unlock.
"""

while True:
	f = open('urls.json',)
	locked = json.load(f)["locked"]
	f.close()
	url = driver.current_url
	domain = urlparse(url).netloc
	if domain in locked:
		try:
			driver.get("file:///Users/Michel/Documents/voice-pass-main/index.html#"+url)
		except:
			pass

driver.close()
