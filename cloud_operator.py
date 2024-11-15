from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class CloudOperator():
    def __init__(self):
        self.driver = None

    def open_web_browser(self, web_address):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(web_address)

    def highlight_important_statement(self):
        important_text = self.driver.find_element(By.XPATH, value='//*[@id="page-width-container"]/div[1]/article/section/div/div[1]/div/div[1]/ul/li[3]')
        actions = ActionChains(self.driver)
        actions.move_to_element(important_text)
        actions.w3c_actions.pointer_action.click()
        actions.w3c_actions.pointer_action.click()
        actions.w3c_actions.pointer_action.click()
        actions.perform()

    def close(self):
        self.driver.close()

