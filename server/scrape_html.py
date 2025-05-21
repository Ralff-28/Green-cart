from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set Chrome options to avoid detection
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without GUI
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent bot detection
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# Initialize Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Load URL
url = "https://www.flipkart.com/subham-woven-embellished-banarasi-silk-blend-saree/p/itma15660287068c"
print(f"🔹 Fetching HTML from: {url}")

driver.get(url)
time.sleep(5)  # Wait for JavaScript to load content

# Get full page source
html_content = driver.page_source

# Save to a file
with open("scraped_data.txt", "w", encoding="utf-8") as file:
    file.write(html_content)

print("✅ HTML saved with Selenium")

driver.quit()
