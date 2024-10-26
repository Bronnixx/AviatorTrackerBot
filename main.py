# 15.01.2024
# Author: @erickndeto
# https://www.mozzartbet.rs/ibet-web-client/#/home/game/spribe/aviator tracker for @Highlinkseo


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver with webdriver_manager
options = Options()
options.add_argument("--headless")  # Optional: Runs Chrome without a GUI (remove if you want to see the browser)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Function to fetch multipliers from the Aviator game on SportPesa
def fetch_multipliers():
    # Direct URL to Aviator on SportPesa
    aviator_url = "https://aviator-next.spribegaming.com/?user=819968792907&token=ba402771-c08e-4e5d-b48e-acaa9a182c72&lang=en&currency=KES&operator=sportpesake"
    
    # Step 1: Open the Aviator game page
    driver.get(aviator_url)
    time.sleep(5)  # Wait for the page to load fully

    # Step 2: Fetch multipliers from the game (update the CSS selector if needed)
    try:
        multipliers = driver.find_elements(By.CSS_SELECTOR, "app-bubble-multiplier .bubble-multiplier")
        print("Multipliers:")
        for multiplier in multipliers:
            print(multiplier.text)  # Print each multiplier found on the page
    except Exception as e:
        print("Error fetching multipliers:", e)

    # Close the browser
    driver.quit()

# Run the function to fetch multipliers
if _name_ == "_main_":
    fetch_multipliers()
