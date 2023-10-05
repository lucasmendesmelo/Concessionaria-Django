from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


login_url = "http://127.0.0.1:8000/login/"

try:
    
    driver.get(login_url)

    
    username_field = driver.find_element(By.ID, "username")  
    password_field = driver.find_element(By.ID, "password")  
    login_button = driver.find_element(By.ID, "login-button") 

 
    username_field.send_keys("admin")
    password_field.send_keys("123")

    
    login_button.click()

    
   
    input("Pressione Enter para fechar a janela do navegador...")

except Exception as e:
    print("O teste de login falhou:", e)

finally:
    
    driver.quit()
