from drivers import ChromeDriver


""" BadZap começa aqui! """
class BadZap:
    def __init__(self):
        self.driver = ChromeDriver().webdriver()
        self.base_url = 'https://web.whatsapp.com/'
        self.buttoms = dict()
        self.inputs = dict()
        self.lists = dict()


    def wait_element(self, element):
        pass

    def gera_xpath(self):
        pass

    def get_contacts(self, contact='all'):
        return []

    def search_groups(self, group='all'):
        return []

    def get_chats(self, status='all'):
        return []

    def get_archived_chats(self, status='all'):
        return []

    def send_message(self, chat=''):
        return True