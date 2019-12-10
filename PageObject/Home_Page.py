class WelcomeScreen:
    def __init__(self):
        self.img_logo = {'xpath': "//div[@class='wrap']//a//img"}
        self.ele_language = {'css': '#english', 'id': 'english'}
        self.ele_custom_care = {'id': 'cCare_city', 'css': '#cCare_city'}
        self.btn_custom_bot = {"xpath": "//div[@class='eye left']"}
        self.lnk_login = {'link': 'Login / Register'}
        self.ele_bus_page = {'xpath': "//div/a/span[contains(text(),'Bus')]"}

    class FilterBusOptions:
        def __init__(self):
            self.txt_source = {'id': 'source', 'css': '#source'}
            self.txt_destination = {'id': 'destination', 'css': '#destination'}
            self.dte_journey_date = {'id': 'datepicker1', 'css': '#datepicker1'}
            self.dte_return_date = {'id': 'datepicker2', 'css': '#datepicker2'}
            self.lnk_search = {'class:': 'btnab icosearch', 'link': 'Search'}

f = WelcomeScreen.FilterBusOptions()
print(f.txt_source['id'])
