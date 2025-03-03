from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time
from plyer import notification

# Function to check if the Google Form is active
def is_form_active(inner_url):
    driver.get(inner_url)
    time.sleep(2)  # Wait for the redirection to complete
    current_url = driver.current_url
    return "/viewform" in current_url

# Function to send local notification
def send_notification():
    notification.notify(
        title='Google Form Notification',
        message='The Google Form is now active!',
        app_name='Form Checker',
        timeout=10  # Notification will stay for 10 seconds
    )

# Main script execution
input_url = input("Enter Form URL: ")  # ask for the URL


# Create a Service object and set path
service = Service(r"C:\Selenium_Drivers\geckodriver.exe")   # paste your driver path

driver = webdriver.Firefox(service=service)  # Initialize Firefox driver using the Service


try:
    while True:
        if is_form_active(input_url):
            send_notification()
            print("Notification sent. The form is active. Stopping the script.")
            break
        else:
            print("Form is still closed. Checking again in 15 seconds...")
            time.sleep(15)
finally:
    driver.quit()
