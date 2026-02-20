import pytest
from utils.login_helper import todo_login
from Pages.lead_page import LeadPage

@pytest.mark.smoke
def test_lead_page(driver):
    todo_login(driver)
    assert "home" in driver.current_url
    lead = LeadPage(driver)
    lead.lead_page_inputs()

