from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import requests
from datetime import datetime, timedelta

# Replace these with your actual login credentials
username = '***'
password = '***'

# URL of the login page
url = 'https://bulut.e-kres.com.tr/Veli/VeliGirisSayfasi#tab-1'

# Path to your ChromeDriver (if not in PATH)
driver = webdriver.Chrome()  # Make sure the ChromeDriver is in your PATH or provide the path to the ChromeDriver

image_dir = 'images'
os.makedirs(image_dir, exist_ok=True)

def fotoIndir(new_date):
    # Wait for the page to load after the date change
    time.sleep(5)  # Adjust this as needed

    # Find the "Fotoğraflar" tab and click on it
    foto_tab = driver.find_element(By.ID, 'Li_VeliFotograflar')
    foto_tab.click()

    # Wait for the page to load after clicking on the tab
    time.sleep(5)  # Adjust this as needed
    
    # Find the image gallery
    image_gallery = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "image-gallery-1"))
    )

    # Find all images within the container
    images = image_gallery.find_elements(By.CLASS_NAME, 'gallery-items')

    # Extract and download the images
    for idx, img in enumerate(images):
        img_url = img.get_attribute('src')
        if img_url:
            # Download the image using requests
            response = requests.get(img_url)
            if response.status_code == 200:
                # Save the image to 'images' directory with a specific filename
                img_name = f'{int(new_date.replace(".", ""))}_{idx}.jpg'
                img_path = os.path.join(image_dir, img_name)
                with open(img_path, 'wb') as f:
                    f.write(response.content)
                    print(f'Downloaded {img_name} to {image_dir}')

try:
    # Open the URL
    driver.get(url)

    # Wait for the login form to be present
    login_form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-form"))
    )

    # Find the username and password input fields
    username_input = driver.find_element(By.NAME, 'UserName')
    password_input = driver.find_element(By.NAME, 'Password')

    # Enter the username and password with a delay
    time.sleep(2)  # Delay to mimic human behavior
    username_input.send_keys(username)

    time.sleep(2)  # Delay to mimic human behavior
    password_input.send_keys(password)

    # Submit the login form
    login_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    time.sleep(2)  # Delay to mimic human behavior
    login_button.click()

    # Wait for the next page to load
    time.sleep(5)  # Adjust this as needed to wait for the next page

    # Change the date using the date picker
    date_picker = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'VeliGirisTarihhh'))
    )

    dates = ['26.06.2024', '27.06.2024', '28.06.2024']
    
    for new_date in dates:
        # Change the date using the date picker
        date_picker = driver.find_element(By.ID, 'VeliGirisTarihhh')
        date_picker.clear()
        date_picker.send_keys(new_date)
        date_picker.send_keys(Keys.RETURN)  

        # Download images and videos
        fotoIndir(new_date)

finally:
    # Close the driver
    driver.quit()