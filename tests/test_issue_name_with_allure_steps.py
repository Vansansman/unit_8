import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "Vansansman")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может открывать задачи в репозитории")
@allure.link("https://github.com", name="Testing")
def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем название Issue 'Listeners NamedBy' в репозитории"):
        s(by.text("Listeners NamedBy")).should(be.visible)