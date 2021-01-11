"extract number of gallons from account and store in a file"
from datetime import datetime
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
warnings.filterwarnings("ignore")

def login():
    "login to website"

    username = 'username'
    password = 'pwd'
    urlLogin = 'https://myaccount.xyz.com/'
    urlTank = 'https://myaccount.xyz.com/mytankmonitor'

    try:
        driver = webdriver.Chrome()
        driver.get(urlLogin)
        element = driver.find_element(By.ID, 'email_check')
        element.send_keys(username)
        element = driver.find_element(By.ID, 'password_check')
        element.send_keys(password)
        element = driver.find_element(By.ID, 'cmdLogin')
        element.click()
    except TypeError:
        print("None argument from webdriver")
        driver = None

    return driver

def get_gallons(driver):
    "go to web page (if driver is available) with gallons and grab number if gallons"
    if driver:
        driver.get(urlTank)
        element = driver.find_element_by_id("tank-intank-gauge")
        gallons = float(element.text.split(': ')[1])
    else:
        gallons = 0.0

    return gallons

def add_to_file(gallons, path):
    "write gallons to file"
    now = datetime.now()
    new_string = now.strftime('%m%d%Y, %H%M, ') + str(gallons) + '\n'
    with open(path, "a") as myfile:
        myfile.write(new_string)

def rerun_bool(path):
    try:
        with open(path) as f:
            for line in f:
                pass
            last_line = line
        today = datetime.now().strftime('%m%d%Y')
        last_line_date = last_line.split(',')[0]
        if today!=last_line_date:
            rerun=True
        else:
            rerun=False
    except:
        rerun=False
    
    return rerun    

def main():
    "main function to call functions in sequence"
    writePath = '/Users/local/oil_recording.txt'
    rerun = rerun_bool(writePath)
    if rerun:
        driver = login()
        gallons = get_gallons(driver)
        add_to_file(gallons, path)


main()
