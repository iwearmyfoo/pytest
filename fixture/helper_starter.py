from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class HelperManager:

    def __init__(self, app):
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.app = app
        wd = self.app.wd
