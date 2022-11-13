import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Vansansman")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованному пользователю доступны задачи в репозитории")
@allure.link("https://github.com", name="Testing")
def test_github_selene():
    browser.open("https://github.com")

    s(".header-search-input").click()
    s(".header-search-input").send_keys("eroshenkoam/allure-example")
    s(".header-search-input").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.text("Listeners NamedBy")).should(be.visible)