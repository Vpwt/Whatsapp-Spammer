from selenium import webdriver
from selenium.webdriver.common.keys import Keys



receiver = input(str("Enter the name of the contact or group name which you want to FLOOD >>")) 
rounds = input("Enter the number of times you want to send >>")
rounds = int(rounds) 
msg = input(str("Type the message you want to send >>"))


driver=webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.implicitly_wait(30)
searchReceiver=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
searchReceiver.send_keys(receiver,Keys.RETURN)
sendElement=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")


for i in range(rounds):
    sendElement.send_keys(msg,Keys.RETURN)

