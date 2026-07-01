from components.base_component import BaseComponent
from playwright.sync_api import Page
import re

from components.navigation.sidebar_list_item_component import SideBarListItemComponent


class SideBarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_list_item = SideBarListItemComponent(page, identifier='dashboard')
        self.courses_list_item = SideBarListItemComponent(page, identifier='courses')
        self.logout_list_item = SideBarListItemComponent(page, identifier='logout')

    def check_visible(self):
        self.dashboard_list_item.check_visible(title='Dashboard')
        self.courses_list_item.check_visible(title='Courses')
        self.logout_list_item.check_visible(title='Logout')

    def click_dashboard(self):
        self.dashboard_list_item.navigate(expected_url=re.compile(r".*/#/dashboard"))

    def click_courses(self):
        self.courses_list_item.navigate(expected_url=re.compile(r".*/#/courses"))

    def click_logout(self):
        self.logout_list_item.navigate(expected_url=re.compile(r".*/#/auth/login"))

