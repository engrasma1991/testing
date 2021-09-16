from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
#load chrome drive
PATH=r"C:\Users\Umar\Desktop\Web Scrapping\chromedriver.exe"
driver=webdriver.Chrome(PATH)
try:
    driver.get('https://www.d3a.io/')
    click_login_button=driver.find_element_by_xpath('//*[@id="root"]/main/header/div/a')
    click_login_button.click()
    time.sleep(2)
    email_text=driver.find_element_by_name('email')
    email_text.send_keys('test@yopmail.com')
    pass_text=driver.find_element_by_name('password')
    pass_text.send_keys('Qwe123!@#')
    login=driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div/div/div/form/div[3]/button')
    login.submit()
    time.sleep(2)
    project_button=driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/nav/div[2]/div[1]/div[2]/div/div/button')
    project_button.click()
    time.sleep(2)
    new_project=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/header/div[3]/button[2]')
    new_project.click()
    #create new project
    time.sleep(2)
    project_name=driver.find_element_by_name('name')
    project_name.send_keys('My Project')
    project_desc=driver.find_element_by_name('nameTextArea')
    project_desc.send_keys('Tesing')
    #getting value for checking our project listed or not  
    text=project_name.get_attribute('value')
    #add project
    project_add=driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button')
    #prop = project_add.is_enabled()
    #print(prop)
    project_add.click()
    time.sleep(2)
    listed_project = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div')
    listed_project=listed_project.text
    if text in listed_project:
        print('Project listed correctly')
        click_on_project=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div/div[1]/span/span')
        click_on_project.click()
        time.sleep(2)
        add_simulation=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[2]/button')
        add_simulation.click()
        time.sleep(2)
        next_button=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/button')
        next_button.click()
        time.sleep(2)
        project_button=driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/nav/div[2]/div[1]/div[2]/div/div/button')
        project_button.click()
        time.sleep(2)
        listed_simulation=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div/p')
        listed_simulation=listed_simulation.text
        if 'default simulation' in listed_simulation:
            print('Simulation Listed Correctly')
        else:
            print('Simulation NOT Listed Correctly')


    
    else:
        print('Project not Listed Correctly')
    


except:
    print('Error')
