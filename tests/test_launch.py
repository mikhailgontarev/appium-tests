
from app_images.app_elements import app_ui_elements


def test_begin(driver):
    driver.wait_img_element(app_ui_elements.persons.ernie).click()
    field = driver.wait_img_element(app_ui_elements.main_screen.empty_field)
    field.click()
    wheat = driver.wait_img_element(app_ui_elements.main_screen.wheat)
    wheat.drag_to(field.position)
    assert driver.wait_img_element(app_ui_elements.main_screen.sown_field, timeout=5), 'Wheat has not planted'
