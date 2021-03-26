# humour for mama - # https://www.youtube.com/watch?v=r0R63TKpcnY


from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option('excludeSwitches', ['enable-logging'])

#option.add_argument("--headless")
#option.add_argument("disable-gpu")

browser = webdriver.Chrome(executable_path='E:\projects\python\mama\chromedriver.exe', options=option)

browser.get("https://forms.gle/kR7MH5heecSUefHZ7")

radiobuttons = browser.find_element_by_xpath('//*[@id="i5"]/div[3]/div')
submitbutton = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')

radiobuttons.click()

submitbutton.click()
# <div class="appsMaterialWizToggleRadiogroupOffRadio exportOuterCircle"><div class=" exportInnerCircle"></div></div>

# <span jsslot="" class="appsMaterialWizButtonPaperbuttonContent exportButtonContent"><span class="appsMaterialWizButtonPaperbuttonLabel quantumWizButtonPaperbuttonLabel exportLabel">Submit</span></span>