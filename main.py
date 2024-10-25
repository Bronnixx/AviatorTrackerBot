# 15.01.2024
# Author: @erickndeto
# https://www.mozzartbet.rs/ibet-web-client/#/home/game/spribe/aviator tracker for @Highlinkseo


from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from telegram_sender import Sender

TOKEN = "7196154071:AAE3TeUuoDchTpTxgiZaptOR6WQE148icx4" #Your token that you got the BotFather
USERNAME = "erickndeto202@gmail.com" #YOUR-EMAIL
PASSWORD = "Makueniadidas2023" #YOUR-PASSWORD
numberOfConsec = 3 #Number of consecutive
ratio = 2.0 #Trigger ratio. Ex: (Bets below 2.00x.)
url = "https://www.mozzartbet.rs/ibet-web-client/#/home/game/spribe/aviator"

import random

MAX_DATA_POINTS = 25  # Maximum number of multipliers
CRASH_MIN = 1.0  # Minimum multiplier at crash point
CRASH_MAX = 4.0  # Maximum multiplier before crashing

# Function to calculate the average of multipliers
def calculate_average(multipliers):
    return sum(multipliers) / len(multipliers)

# Function to find the maximum multiplier
def find_max_multiplier(multipliers):
    return max(multipliers)

# Function to find the minimum multiplier
def find_min_multiplier(multipliers):
    return min(multipliers)

# Function to simulate the behavior of a multiplier
def generate_multiplier(count):
    base_multiplier = 1.0 + (random.randint(0, 300) / 100.0)
    crash_point = CRASH_MIN + (CRASH_MAX - CRASH_MIN) * (count / MAX_DATA_POINTS)
    return crash_point if random.randint(0, 99) < 20 else base_multiplier  # 20% chance to crash

# Function to predict the next multiplier
def predict_next_multiplier(average):
    return average * (0.90 + (random.randint(0, 10) / 100.0))  # Adjusted for prediction

# Function to place a bet
def place_bet(multiplier, bet_amount):
    print(f"Bet placed: {bet_amount:.2f} on multiplier {multiplier:.2f}")
    payout = bet_amount * multiplier  # Calculate potential payout
    print(f"Potential payout: {payout:.2f}")

# Main program
def main():
    multipliers = []  # List to hold multipliers

    # Input initial multipliers
    print(f"Enter up to {MAX_DATA_POINTS} initial multipliers (enter -1 to stop):")
    while len(multipliers) < MAX_DATA_POINTS:
        input_value = input()
        if input_value == '-1':
            break
        try:
            multipliers.append(float(input_value))  # Store the multiplier
        except ValueError:
            print("Please enter a valid number.")

    # Check if data points are available
    if not multipliers:
        print("No data points entered.")
        return

    # Calculate initial statistics
    average = calculate_average(multipliers)
    max_multiplier = find_max_multiplier(multipliers)
    min_multiplier = find_min_multiplier(multipliers)

    print(f"Initial Average Multiplier: {average:.2f}")
    print(f"Maximum Multiplier: {max_multiplier:.2f}")
    print(f"Minimum Multiplier: {min_multiplier:.2f}")

    # Loop for predicting next multipliers and placing bets
    while True:
        next_input = input("Enter a new multiplier to predict the next (enter -1 to exit): ")
        if next_input == '-1':
            break

        try:
            next_multiplier = float(next_input)
            if len(multipliers) < MAX_DATA_POINTS:
                multipliers.append(next_multiplier)  # Store the new multiplier

            average = calculate_average(multipliers)  # Recalculate the average
            max_multiplier = find_max_multiplier(multipliers)  # Recalculate max
            min_multiplier = find_min_multiplier(multipliers)  # Recalculate min

            # Predict the next multiplier
            next_prediction = predict_next_multiplier(average)
            print(f"Updated Average Multiplier: {average:.2f}")
            print(f"Predicted Next Multiplier (slightly lower): {next_prediction:.2f}")

            # Simulate generating the next multiplier based on game logic
            simulated_multiplier = generate_multiplier(len(multipliers))
            print(f"Simulated Next Multiplier: {simulated_multiplier:.2f}")

            # Place a bet
            bet_amount = float(input("Enter your bet amount: "))
            place_bet(next_prediction, bet_amount)

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "_main_":
    main()
def login():
    while(not checkLogin()):
        try:
            driver.switch_to.default_content()
            log_but = driver.find_element_by_xpath('//*[@id="app-loaded"]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input').click()
            time.sleep(1)
            mail = driver.find_element_by_xpath('//*[@id="app-loaded"]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div/form/input[1]')
            password = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div/form/input[2]')
            mail.send_keys(USERNAME)
            time.sleep(1)
            password.send_keys(PASSWORD)
            log_but = driver.find_element_by_xpath('//*[@id="app-loaded"]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div/form/input[4]').click()
            time.sleep(10)
            login_flag=checkLogin()
        except:
            print("Login attempt failed. I'm trying again.")
    print("Logging successfuly.")    
    
def checkLogin():
    driver.switch_to.default_content()
    username = driver.find_elements_by_class_name("profile-and-gifts-wrapper")
    if len(username) > 0 and username[0].text:
        return True
    else: return False
    
    
def iframe():
    iframe_flag = False
    while(not iframe_flag):
        try:
            iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "seven-plugin")))
            driver.switch_to.frame(iframe)
            button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//div[@class='button-block'])//div/div")))
            button.click()
            iframe_flag = True
        except:
            pass
    


def get_blocks():
    rates = []
    while(len(rates) == 0):
        try:
            blocks = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "(//div[@class='payouts-block'])[1]//app-payout-item/div")))
            for block in blocks:
                if block.text != '':
                    rates.append(float(block.text.replace('x','')))
            if(len(rates) != 0):
                return rates
        except:
            pass
    
    
def checkTrigger(rates, ratio):
    string = "".join(["Y" if rate < ratio else "N" for rate in rates ])
    counter = 0
    for i in string:
        if i == "Y":
            counter+=1
        else: break
    return counter
    
    
def send_msg(rates, numberOfConsec):
    try:
        sender.send_msg(f"!Alert Aviator has {numberOfConsec} blue in a row.")
        sender.send_msg(f"Last {len(rates)} round: " +  ", ".join([f"{rate}x" for rate in rates ]))
    except: 
        print("Message service has a problem. Check your tokens")
    
    
    # <span ng-if="profileInfo.config != 'ug'" class="ng-binding ng-scope">mert</span>
    # //*[@id="app-loaded"]/div[3]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[2]/span

print("Welcome to Aviator Tracker Bot..")
options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
driver = webdriver.Chrome(options=options)
sender = Sender(TOKEN)
driver.get(url)
time.sleep(10)
login()
time.sleep(1)
iframe()
time.sleep(1)
old_rates = []
while True:
    try:
        if checkLogin():
            iframe()
            rates = get_blocks()
            if old_rates != rates:
                print(f"Last {len(rates)} round: " +  ", ".join([f"{rate}x" for rate in rates ]))
                count= checkTrigger(rates,ratio)
                if count >= numberOfConsec:
                    print(f"!Alert Aviator has {count} blue in a row. Message sending via Telegram.")
                    send_msg(rates,count)
            time.sleep(3)
            old_rates = rates
        else:
            driver.refresh()
            time.sleep(3)
            login()
    except:
        pass
    



