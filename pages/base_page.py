from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 20)

    def open_url(self, url):
        self._driver.get(url)

    def click(self, locator, *, record_pointer_events=False):
        element = self._wait.until(EC.element_to_be_clickable(locator))
        if record_pointer_events:
            self._driver.execute_script(
                """
                const requested = arguments[0];
                window.routePointerTrace?.controller.abort();
                const controller = new AbortController();
                const events = [];
                window.routePointerTrace = {controller, events};

                for (const type of ["pointerdown", "pointerup", "click"]) {
                    document.addEventListener(type, event => {
                        const target = event.target;
                        events.push({
                            event: type,
                            trusted: event.isTrusted,
                            insideRequestedElement: requested.contains(target),
                            tag: target.nodeName,
                            className: target.getAttribute("class"),
                            src: target.getAttribute("src"),
                        });
                    }, {capture: true, once: true, signal: controller.signal});
                }
                """,
                element,
            )
        element.click()

    def hover(self, locator):
        element = self._wait.until(EC.presence_of_element_located(locator))
        self._driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
            element,
        )
        self._wait.until(lambda driver: element if element.is_displayed() else False)
        ActionChains(self._driver).move_to_element(element).perform()

    def get_pointer_events(self):
        return self._driver.execute_script("return window.routePointerTrace?.events ?? [];")

    def fill(self, locator, text):
        field = self._wait.until(EC.element_to_be_clickable(locator))
        field.clear()
        field.send_keys(text)

    def press_tab(self, locator):
        field = self._wait.until(EC.element_to_be_clickable(locator))
        field.send_keys(Keys.TAB)

    def is_visible(self, locator):
        try:
            self._wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def wait_until(self, condition, timeout):
        return WebDriverWait(self._driver, timeout).until(condition)

    def is_invisible(self, locator):
        return self._wait.until(EC.invisibility_of_element_located(locator))

    def get_visible_texts(self, locator):
        self._wait.until(EC.visibility_of_element_located(locator))
        return [element.text for element in self._driver.find_elements(*locator)]

    def count_visible_elements(self, locator):
        return len(
            [
                element
                for element in self._driver.find_elements(*locator)
                if element.is_displayed()
            ]
        )

    def get_visible_text(self, locator):
        return self._wait.until(
            lambda driver: self._get_visible_element_text(driver, locator)
        )

    @staticmethod
    def _get_visible_element_text(driver, locator):
        try:
            element = driver.find_element(*locator)
            return element.text if element.is_displayed() else False
        except (NoSuchElementException, StaleElementReferenceException):
            return False

    def get_current_text(self, locator):
        try:
            return self._driver.find_element(*locator).text
        except (NoSuchElementException, StaleElementReferenceException):
            return None

    def get_current_attribute(self, locator, attribute):
        try:
            return self._driver.find_element(*locator).get_dom_attribute(attribute)
        except (NoSuchElementException, StaleElementReferenceException):
            return None
