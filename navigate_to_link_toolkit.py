from typing import Type

from pydantic import BaseModel, Field, HttpUrl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from superagi.tools.base_tool import BaseTool


class NavigateToLinkInput(BaseModel):
    url: HttpUrl = Field(..., description="The URL to navigate to using Selenium.")


class NavigateToLinkTool(BaseTool):
    name: str = "Navigate to Link"
    args_schema: Type[BaseModel] = NavigateToLinkInput
    description: str = "Uses Selenium to navigate to a given URL."

    def _execute(self, url: str):
        options = Options()
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        try:
            driver.get(url)
            print(f"Navigated to {url}")
            time.sleep(10)
        finally:
            driver.quit()

        return f"Finished navigating to {url}."
