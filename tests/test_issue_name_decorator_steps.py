import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


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