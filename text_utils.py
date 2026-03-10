# text_utils.py
from playwright.async_api import Page
from locators import LocatorTypes, LocatorTemplates


class TestUtils:
    """Утилиты для работы с тестами ProBonus"""
    
    def __init__(self, page: Page, locators, locator_templates):
        self.page = page
        self.loc = locators
        self.templates = locator_templates
    
    def get_element(self, locator_data):
        """Получить элемент по данным локатора"""
        if not locator_data:
            return None
            
        if LocatorTypes.LOCATOR in locator_data:
            element = self.page.locator(locator_data[LocatorTypes.LOCATOR])
            if "has_text" in locator_data:
                element = element.filter(has_text=locator_data["has_text"])
            if "nth" in locator_data:
                element = element.nth(locator_data["nth"])
            return element
        elif LocatorTypes.ROLE in locator_data:
            role = locator_data[LocatorTypes.ROLE]
            # Фильтруем только допустимые параметры для get_by_role
            valid_role_params = {"name", "checked", "disabled", "selected", "expanded", "level"}
            kwargs = {k: v for k, v in locator_data.items() if k in valid_role_params and k != LocatorTypes.ROLE}
            return self.page.get_by_role(role, **kwargs)
        elif LocatorTypes.TEXT in locator_data:
            # Для get_by_text используем только text и exact
            text = locator_data[LocatorTypes.TEXT]
            exact = locator_data.get("exact", False)
            return self.page.get_by_text(text, exact=exact)
        elif LocatorTypes.LABEL in locator_data:
            label = locator_data[LocatorTypes.LABEL]
            exact = locator_data.get("exact", False)
            return self.page.get_by_label(label, exact=exact)
        elif LocatorTypes.ID in locator_data:
            return self.page.locator(f"#{locator_data[LocatorTypes.ID]}")
        return None
    
    async def click(self, locator_data):
        """Кликнуть по элементу"""
        element = self.get_element(locator_data)
        if element:
            await element.click()
        else:
            print(f"Элемент не найден для клика: {locator_data}")
    
    async def fill(self, locator_data, text):
        """Заполнить поле"""
        element = self.get_element(locator_data)
        if element:
            await element.fill(text)
        else:
            print(f"Элемент не найден для заполнения: {locator_data}")
    
    async def expect_visible(self, locator_data):
        """Проверить видимость элемента"""
        from playwright.async_api import expect
        element = self.get_element(locator_data)
        if element:
            await expect(element).to_be_visible()
        else:
            print(f"Элемент не найден для проверки видимости: {locator_data}")
    
    async def expect_not_visible(self, locator_data):
        """Проверить что элемент не виден"""
        from playwright.async_api import expect
        element = self.get_element(locator_data)
        if element:
            await expect(element).not_to_be_visible()
        else:
            print(f"Элемент не найден для проверки невидимости: {locator_data}")
    
    async def expect_text(self, locator_data, text):
        """Проверить текст элемента"""
        from playwright.async_api import expect
        element = self.get_element(locator_data)
        if element:
            await expect(element).to_have_text(text)
        else:
            print(f"Элемент не найден для проверки текста: {locator_data}")
    
    async def login(self, username="user", password="123"):
        """Выполнить вход в систему"""
        await self.fill(self.loc.LOGIN_FIELD, username)
        await self.fill(self.loc.PASSWORD_FIELD, password)
        await self.click(self.loc.LOGIN_BUTTON)
    
    async def navigate_to(self, link_locator):
        """Перейти по ссылке"""
        await self.click(link_locator)