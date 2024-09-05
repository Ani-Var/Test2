class Component:
    def __init__(self, page, locator, name):
        self.page = page
        self.locator = locator
        self.name = name

    def get_locator(self, **kwargs):
        return self.page.locator(self.locator, **kwargs)

    def should_be_visible(self):
        assert self.get_locator().is_visible(), f"{self.name} не виден"