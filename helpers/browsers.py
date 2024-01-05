from selenium.webdriver import Chrome, Firefox


def browsers(b_option):
    browser_dict = {
        'Chrome': Chrome,
        'Firefox': Firefox
    }
    return browser_dict[b_option]

