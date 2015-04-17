__author__ = 'pma'

from SearchBar import SearchBar


class Page():
    def __init__(self, driver):
        self.Driver = driver
        self._search_bar = None

    @property
    def search_bar(self):
        if self._search_bar is None:
            self._search_bar = \
                SearchBar(self.Driver,
                          self.Driver.find_element(SearchBar.selectors['self'][0],
                                                   SearchBar.selectors['self'][1]))
        return self._search_bar

    def open(self, url):
        self.Driver.get(url)

    @property
    def title(self):
        return self.Driver.title

    @property
    def current_url(self):
        return self.Driver.current_url

    def try_visit_link(self, link_text):
        try:
            self.Driver.find_element_by_link_text(link_text).click()
        except Exception:
            return
