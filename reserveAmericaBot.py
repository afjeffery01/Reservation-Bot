import mmap
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

start = input("Have You Logged In Yet? Yes Or No. ")
start = start.upper()
if start == "YES":
    usrLookUp = input("Enter The Username You Created: ")
    f = open("pswd.txt","r")
    lines = f.read()
    findUsr = lines.find(usrLookUp)
    print(findUsr)
elif start == "NO":
    email = input("Please Enter Your Email For Reserve America: ")
    pswd = input("Please Enter Your Password For Reserve America: ")
    save = input("Would You Like To Save This Information? Yes or No: ")
    save = save.upper()
    if save == "YES":
        userId = input("Please Make A Username: ")
        text_file = open("pswd.txt", 'a')
        saveText = userId + " " + email + " " + pswd + "\n" 
        text_file.write(saveText)
        text_file.close()
    elif save == "NO":
        print()
    else:
        print("Please Say Yes or No: ")
else:
    print("Please Say Yes or No.")
cottageInput = input("What Cottage Number Would You Like To Rent? ")
if cottageInput == "40":
    siteId = "246321"
elif cottageInput == "41":
    siteId = "246277"
elif cottageInput == "42":
    siteId = "260617"

arvdate = input("Please Input Arrival Date: MM/DD/YY: ")
lenOfStay = input("Please Input Length of Stay: ")

url = "https://www.reserveamerica.com/campsiteDetails.do?siteId="+ siteId +"&contractCode=NY&parkId=175&arvdate="+ arvdate +"&lengthOfStay=" + lenOfStay

driver = webdriver.Chrome()
driver.get(url)
button = driver.find_element_by_class_name("btn_book_dates")
button.click()
if driver.current_url == url:
    while driver.current_url == url:
        time.sleep(60)
        button.click
elif driver.current_url != url:
    findEmail = driver.find_element_by_id("AemailGroup_1733152645")
    findPswd = driver.find_element_by_id("ApasswrdGroup_704558654")
    findEmail.send_keys(email)
    findPswd.send_keys(pswd)
    enter = driver.find_element_by_name("submitForm")
    enter.click()
