from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


pagina_url = "http://127.0.0.1:8000/"

try:
    
    driver.get(pagina_url)

   
    comprar_button = driver.find_element(By.ID, "id-whatsapp")  

   
    comprar_button.click()

    enviar_mensagem_button = driver.find_element(By.ID, "action-button")
    enviar_mensagem_button.click()

    
    wait = WebDriverWait(driver, 10)
    usar_whatsapp_web_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[3]/div/div/h4[2]/a")))

    
    usar_whatsapp_web_link.click()

    wait = WebDriverWait(driver, 30)
    enviar_mensagem_wpp = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button")))

    enviar_mensagem_wpp.click()
    
    
    input("Pressione Enter para fechar a janela do navegador...")

except Exception as e:
    print("O teste de login falhou:", e)

finally:
    
    driver.quit()
