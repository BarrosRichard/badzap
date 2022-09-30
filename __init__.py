from drivers import ChromeDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


""" BadZap começa aqui! """
class BadZap:
    def __init__(self):
        self.driver = ChromeDriver().webdriver(options=['--log-level=3', ['excludeSwitches', ['enable-logging']]])
        self.wait = 30
        self.base_url = 'https://web.whatsapp.com/'

    def waitReturn(self, searchElement, analisar=False, clicavel=False, exibirErro=True):
        if analisar == True:
            print(f'Buscando elemento: {searchElement}')
        try:
            if clicavel == False:
                element = WebDriverWait(self.driver, self.wait).until(
                    EC.presence_of_element_located(searchElement))
            else:
                element = WebDriverWait(self.driver, self.wait).until(
                    EC.element_to_be_clickable(searchElement))

            if analisar == True:
                self.anl_elemento(element)
            return element
        except:
            if exibirErro == True:
                print(
                    f'Erro ao localizar elemento: {searchElement} Timeout de: {self.wait} segundos', True)
            return None

    def gera_xpath(self, elemento):
        components = []
        child = elemento if elemento.name else elemento.parent
        for parent in child.parents:
            siblings = parent.find_all(child.name, recursive=False)
            # try:
            components.append(
                    child.name if 1 == len(siblings) else '%s[%d]' % (
                        child.name,
                        next(i for i, s in enumerate(siblings, 1) if s is child)
                    )
            )
            # except:
            #     pass
            child = parent
        components.reverse()
        return '/%s' % '/'.join(components)

    def get_contacts(self, contact='all'):
        return []

    def search_groups(self, group='all'):
        return []

    def get_chats(self, status='all'):
        chats = BeautifulSoup(self.waitReturn((By.XPATH, 'html')).get_attribute('innerHTML'), 'lxml').find('div', {'data-testid': 'chat-list'}).find_all('span')

        for chat in chats:
            if status in chat.text and status != 'all':
                return self.gera_xpath(chat)

        return chats

    def get_archived_chats(self, status='all'):
        return []

    def send_message(self, chat=''):
        self.driver.find_element(By.XPATH, self.gera_xpath(BeautifulSoup(self.waitReturn((By.XPATH, 'html')).get_attribute(
            'innerHTML'), 'lxml').find('div', {'data-testid': 'conversation-compose-box-input'}))).send_keys(chat, Keys.ENTER)
        return True


'''     TESTESTESTESTESTESTESTESTESTESTES   '''
# zapzap = BadZap()

# driver = zapzap.driver
# driver.get(zapzap.base_url)
# time.sleep(10)
# driver.find_element(By.XPATH, zapzap.get_chats('lambreta')).click()
# time.sleep(2)
# zapzap.send_message('opaaaa')
