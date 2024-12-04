# Selenium Toolkit

**Selenium Toolkit** is a Python-based utility designed to simplify web navigation and automation tasks. Built for the SuperAGI Toolkit, this library provides straightforward tools for navigating to web links and handling common browser automation requirements using Selenium.

## Features

- **Link Navigation**: Effortlessly navigate to specified URLs using Selenium WebDriver.
- **Extensibility**: Designed to integrate with the SuperAGI framework, allowing for seamless integration into broader automation workflows.
- **Ease of Use**: Simple and intuitive Python modules to handle common web automation tasks.
- **Customizable**: Easily adaptable for specific project needs by extending the provided modules.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/[your-username]/SeleniumToolkit.git
   cd SeleniumToolkit
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the correct WebDriver for your browser (e.g., ChromeDriver for Google Chrome) and place it in your system's PATH.

## Usage

### Example: Navigating to a URL

```python
from selenium_toolkit import navigate_to_link_toolkit

# Example function to navigate to a website
navigate_to_link_toolkit.navigate_to_url("https://example.com")
```

### Module Overview

1. `selenium_toolkit.py`: Contains core functions and utilities for browser automation.
2. `navigate_to_link_toolkit.py`: Simplifies URL navigation with easy-to-use methods.
3. `requirements.txt`: Lists all Python dependencies for seamless setup.

## Requirements

- Python 3.7+
- Selenium library
- Compatible WebDriver (e.g., ChromeDriver, GeckoDriver)

