from selene.api import *


class MainPage:
    def open(self):
        browser.open('https://github.com/')
        return self

    def login_in_desktop(self):
        browser.element('a[href="/login"]').click()
        return self

    def login_in_mobile(self):
        browser.element('.Button--link').click()
        browser.element('a[href="/login"]').click()
        return self

    def check_header(self):
        browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
        return self


main_page = MainPage()

