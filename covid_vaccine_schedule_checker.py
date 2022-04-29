from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from plyer import notification
import time
from datetime import datetime
import sys
from twilio.rest import Client

account_sid = ""
auth_token = ""
from_no = ''

client = Client(account_sid, auth_token)


def prGreen(skk): print("\033[92m {}\033[00m".format(skk))


# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)


# if len(sys.argv) != 2:
#     msg = 'Error: Please Provide a 6 digit Pin Code'
#     print("\033[91m {}\033[00m".format(msg))
#     exit()

# print(sys.argv)
# pincode = sys.argv[1]

pincode = input("Enter your pincode\n>> ")
to_no = input("Enter your mobile no with country code: \n>>")

print("loading...")

driver = webdriver.Firefox()

print("Don't close the browser...")
print("You will get a notification when slots become available...")

while True:
    try:
        driver.get(
            "https://www.cowin.gov.in/home")
        search = driver.find_element_by_id("mat-input-0")
        # pincode = input('\n\n Enter Pin Code\n>')
        # pincode = "845101"
        search.send_keys(pincode)
        search.send_keys(Keys.RETURN)

        slot_boxes = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "slots-box"))
        )

        for slot_box in slot_boxes:
            vaccine = slot_box.text.strip().split('\n')
            if len(vaccine) < 3:
                continue
            vac_count, vac_name, vac_age = vaccine[0], vaccine[1], int(
                vaccine[2][-3:-1])

            if vac_count.isnumeric() and vac_age == 18:
                # if vac_count.isnumeric():
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                message = f"Location {pincode} || Time {current_time} || {vac_count} {vac_name} for Age: {vac_age}+\n"

                with open("log.txt", 'a') as mfile:
                    mfile.write(message)
                prGreen(message)

                notification.notify(
                    title=f"Vaccine Available",
                    message=message,
                    app_icon="vac_icon.ico",
                    timeout=500
                )
                message = client.messages.create(
                    body=message,
                    from_=from_no,
                    to=to_no
                )

                call = client.calls.create(
                    url='http://demo.twilio.com/docs/voice.xml',
                    to=to_no,
                    from_=from_no
                )

                print("Program Terminated...")
                exit()

    finally:
        # time interval(in seconds) of two consecutive check
        time_interval = 30
        time.sleep(time_interval)

driver.quit()
