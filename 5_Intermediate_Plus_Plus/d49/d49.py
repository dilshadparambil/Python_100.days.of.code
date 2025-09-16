#Automated gym workout booking 

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions
from datetime import timedelta,datetime

def get_book_date(week_day,today_date):
    today=today_date
    days_until_booking = (week_day - today.weekday() + 7) % 7
    booking_date = today + timedelta(days=days_until_booking)
    return booking_date

def login():
    login_bt=wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_bt.click()

    email=wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    email.clear()
    email.send_keys(ACCOUNT_EMAIL)

    password=driver.find_element(By.NAME,value='password')
    password.clear()
    password.send_keys(ACCOUNT_PASSWORD)

    submit=driver.find_element(By.ID,value='submit-button')
    submit.click()

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

def book(day_num,what_time):
    global already_counter, waitlists_joined, bookings_done

    site_date = driver.find_element(By.CLASS_NAME, value='Schedule_scheduleTitle__zfZxg').text.split()[-1].replace(')','')
    date_object = datetime.strptime(site_date, "%d/%m/%Y").date()
    chosen_date = get_book_date(day_num,date_object)  #tueday=1,thursday=3

    book_date= chosen_date.strftime("%Y-%m-%d")
    book_month = chosen_date.strftime("%B")[:3]
    book_day = chosen_date.day
    book_day_name = chosen_date.strftime("%A")

    book_item=driver.find_element(By.CSS_SELECTOR,value=f"button[id$='{book_date}-{what_time}']")
    book_item_name=driver.find_element(By.CSS_SELECTOR,value=f"h3[id$='{book_date}-{what_time}']").text
    book_item_time=driver.find_element(By.CSS_SELECTOR,value=f"p[id$='{book_date}-{what_time}']").text.strip('Time: ')
    print_msg=f'on {book_day_name[:3]}, {book_month} {book_day}, {book_item_time}'

    if book_item.text=='Booked':
        print(f"Already booked: {book_item_name} {print_msg}")
        verification.append(f"{book_item_name} {print_msg}")
        already_counter+=1
        return
    elif book_item.text=='Waitlisted':
        print(f"Already on waitlist: {book_item_name} (Waitlist) {print_msg}")
        verification.append(f"{book_item_name} (Waitlist) {print_msg}")
        already_counter+=1
        return
    elif book_item.text in ['Book Class', 'Join Waitlist']:
        book_item.click()
        # Determine expected status
        expected_status = 'Booked' if book_item.text == 'Book Class' else 'Waitlisted'
        # Re-locate the button after click (avoid stale element reference)
        button_selector = f"button[id$='{book_date}-{what_time}']"
        WebDriverWait(driver, 5).until(
            lambda d: d.find_element(By.CSS_SELECTOR, button_selector).text == expected_status
        )
        # Get fresh element for text confirmation
        updated_item = driver.find_element(By.CSS_SELECTOR, button_selector)
        if updated_item.text == 'Booked':
            print(f"✓ Successfully booked: {book_item_name} {print_msg}")
            verification.append(f"{book_item_name} {print_msg}")
            bookings_done += 1
        else:
            print(f"✓ Joined waitlist for: {book_item_name} (Waitlist) {print_msg}")
            verification.append(f"{book_item_name} (Waitlist) {print_msg}")
            waitlists_joined += 1


def verify_booking():
    booking_page = driver.find_element(By.ID, value='my-bookings-link')
    booking_page.click()
    wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))
    print("\n")
    print(f"--------------Total Tuesday & Thursday 6pm classes : {bookings_done + waitlists_joined + already_counter}--------------")
    bookings = driver.find_elements(By.CSS_SELECTOR, value=f"div[class^='MyBookings_bookingDetails']")
    print("\n")
    print("--- VERIFYING ON MY BOOKINGS PAGE ---")
    for element in bookings:
        class_name = element.text.split('\n')[0]
        text = element.text.replace('\nWhen:', ' on').split('\n')[0]
        if text in verification:
            print(f"✓ Verified: {class_name}")

    print("\n\n")
    print("--- VERIFICATION RESULT ---")
    print(f'Expected: {len(verification)} bookings')
    print(f"Found:{len(bookings)} bookings")
    if len(verification) == len(bookings):
        print('✅ SUCCESS: All bookings verified!')
    else:
        print(f'❌ MISMATCH: Missing {len(verification) - len(bookings)} bookings')

from selenium.common import exceptions

def retry(func, description, max_attempts=7):
    for attempt in range(max_attempts):
        print(f"Trying {description}. Attempt: {attempt + 1}")
        try:
            return func()
        except exceptions.TimeoutException:
            if attempt == max_attempts - 1:
                raise  # Re-raise if all attempts fail
            time.sleep(1)


ACCOUNT_EMAIL = "dilshadkareemparambil@gmail.com"
ACCOUNT_PASSWORD = 'dilshad123'
GYM_URL = "https://appbrewery.github.io/gym/"

login_no=0
booking_no=[0,0]
verify_no=0

already_counter=0
waitlists_joined=0
bookings_done=0
verification=[]

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
usr_dir = os.path.join(os.getcwd(), "chrome_profile")
options.add_argument(f"--user-data-dir={usr_dir}")
driver=webdriver.Chrome(options=options)
driver.get(GYM_URL)
wait = WebDriverWait(driver, 2)

retry(login, 'Login')
retry(lambda: book(1, '1800'), 'Booking')
retry(lambda: book(3, '1800'), 'Booking')

time.sleep(5)
verify_booking()

# driver.quit()
