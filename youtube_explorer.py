from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 5)
actions = ActionChains(driver)

def show_youtube():
    print(f'In show_youtube()')
    driver.get("https://www.youtube.com/")
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[text()="I Agree"]'))).click()
    except:
        pass

def search():
    print(f'In search()')
    search_bar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'input[id = search]')))
    actions.move_to_element(search_bar).click().perform()
    search_bar.clear()
    search_bar.send_keys("USA National Anthem")
    sleep(2) # Espero dos segundos, si no espero un poco el comportamiento es extraño
    search_bar.send_keys(Keys.ENTER)

def watch_third_video():
    print(f'In watch_third_video()')
    section_renderer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'ytd-item-section-renderer[class="style-scope ytd-section-list-renderer"]')))

    video = section_renderer.find_elements(By.CSS_SELECTOR, f'ytd-video-renderer[class = "style-scope ytd-item-section-renderer"]')[2]
    video.find_element(By.CSS_SELECTOR, f'yt-formatted-string[class="style-scope ytd-video-renderer"]')
    sleep(2) # Espero porque a pesar de que los elementos están visibles, el siguiente click impide visualizarlos

    video.click()
    title = video.text.split("\n")[1]
    print(f'\nImprimiendo título por pantalla: {title}\n')

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'div[id="columns"]')))
    for i in range(10):
        try:
            driver.find_element(By.XPATH, f'//*[text()="Show more"]').click()
        except:
            pass
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.DOWN)

    sleep(3)
    for i in range(3):
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
        sleep(2)
    
def see_explore_section():
    driver.back()
    driver.back()
    driver.find_element(By.XPATH, f'//*[text()="Explore"]').click()
    sleep(10)
    

show_youtube()
while True:
    # He optado por colocar estas dos en bucle porque en algunas ocasiones no consigue introducir el título del vídeo en la barra de búsqueda
    # independientemente de que haga click en ella.
    try:
        search()
        watch_third_video()
        break
    except:
        continue

see_explore_section()
driver.quit()