from typing import Type

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from pydantic import BaseModel, Field, HttpUrl
from superagi.tools.base_tool import BaseTool

from navigate_to_link_toolkit import NavigateToLinkInput


class NavigateToLinkTool(BaseTool):
    name: str = "Navigate to Link"
    args_schema: Type[BaseModel] = NavigateToLinkInput
    description: str = "Uses Selenium to navigate to a given URL and perform actions."

    def _execute(self, url: str):
        options = Options()
        # Uncomment to run Chrome in headless mode
        options.add_argument('--headless')

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        try:
            driver.get(url)
            print(f"Successfully navigated to {url}")
            # Add any specific actions you need to perform on the page here

            time.sleep(30)  # Adjust as needed

        finally:
            driver.quit()

        return f"Finished navigating to {url}."
