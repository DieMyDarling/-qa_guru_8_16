import pytest
from selene import browser

from pages.main_page import main_page


@pytest.fixture(params=[(1920, 1080, 'desktop'), (375, 667, 'mobile')])
def browser_setup(request):
    if request.param[2] == 'desktop':
        browser.config.window_width = request.param[0]
        browser.config.window_height = request.param[1]
        return request.param[2]

    if request.param[2] == 'mobile':
        browser.config.window_width = request.param[0]
        browser.config.window_height = request.param[1]
        return request.param[2]


def test_github_desktop(browser_setup):
    if browser_setup == 'mobile':
        pytest.skip('Not for mobile browsers')
    main_page.open()
    main_page.login_in_desktop()
    main_page.check_header()


def test_github_mobile(browser_setup):
    if browser_setup == 'desktop':
        pytest.skip('Not for desktop browsers')
    main_page.open()
    main_page.login_in_mobile()
    main_page.check_header()
