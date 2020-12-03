import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def make_directory():
    """Modificar descargas con path completo"""
    main_folder = 'files2'

    os.makedirs(f'../{main_folder}/PML/MDA')
    os.makedirs(f'../{main_folder}/PML/MTR')
    os.makedirs(f'../{main_folder}/PND/MDA')
    os.makedirs(f'../{main_folder}/PND/MTR')
    os.makedirs(f'../{main_folder}/generation/real')
    os.makedirs(f'../{main_folder}/generation/forecast')
    os.makedirs(f'../{main_folder}/consumption/real')
    os.makedirs(f'../{main_folder}/consumption/forecast')


def wait_download(directorio,file_number, download_folder):
    """Iterates while a file is being downloaded in order to download just one file at a time. To do this a file.part is searched in the download_folder directory, when it disappears, the download has finished. Does not return anything."""

    while directorio == os.listdir(download_folder):
        # Waiting for the download to begin
        pass

    time.sleep(1)
    print(f'File {file_number}.', end = '')

    wait = True
    # Looking for a .part file in download_folder directory
    while wait:
        wait = False
        for file in os.listdir(download_folder):
            if ".part" in file:
                time.sleep(0.5)
                wait = True
                print('.', end = '')
                sys.stdout.flush()
    print('Done')


def open_browser(download_folder):
    """Function description..."""

    profile = webdriver.FirefoxProfile()

    # Do not use default download folder
    profile.set_preference("browser.download.folderList", 2)

    # Use selected download folder
    profile.set_preference("browser.download.dir", download_folder)

    # Do not show download popup for selected mime-type files
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream, application/zip")

    print('Opening Browser.')
    driver = webdriver.Firefox(firefox_profile=profile)

    return driver

def download_by_xpath(driver, folder_path, xpath):
    """"""
    # Find element
    download_button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))

    # Get before-download directory content
    directory = os.listdir(folder_path)

    # Click button and begin download
    download_button.click()

    return directory

def postgres_password(file_path = 'psql_password.txt'):

    with open(file_path, 'r') as file:
        password = file.readline()

    return password


def textbox_fill(driver, xpath, date_string, attribute):

    textbox = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    textbox.send_keys(date_string)
    textbox.send_keys(Keys.TAB)
    time.sleep(0.1)

    return textbox.get_attribute(attribute)


def get_folder(folder_frame, subfolder_1, subfolder_2 = None):
    """This function returns folder,files wher folder is the folder to look for files in the selected system and data, files is a list with the name of all the files available"""

    folder = f'{folder_frame}\\{subfolder_1}'

    if subfolder_2:
        folder = f'{folder_frame}\\{subfolder_1}\\{subfolder_2}'

    files = os.listdir(folder)

    return folder,files

if __name__ == '__main__':
    # make_directory()
    # print(postgres_password())
    pass