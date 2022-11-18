import allure
from allure_commons._allure import attach
from allure_commons.types import Severity, AttachmentType
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from utils.u9 import add_html, add_screenshot, add_logs

@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "Vansansman")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может редактировать задачи в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    follow_repository_link("eroshenkoam/allure-example")
    open_issue_tab()
    check_issue_name("Listeners NamedBy")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def follow_repository_link(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем название Issue {name} в репозитории")
def check_issue_name(name):
    s(by.text(name)).click()

def add_screenshot(browser):
    png = browser.driver.get_screenshots_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_logs(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_sourse
    allure.attach(html, 'page_sourse', AttachmentType.HTML, '.html')

