from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
# navigate to url
driver.get("https://automationexercise.com/")
#verify homepage
try:

    text_element = driver.find_element(By.XPATH, "//*[@id='slider-carousel']/div/div[1]/div[1]/h1/span")
    assert text_element.is_displayed(), "Home page text is displayed"

    # If the above checks pass, you can consider the home page as visible successfully.
    print("Home page is visible successfully!")

except Exception as e:

    print(f"Home page verification failed: {str(e)}")

driver.get("https://automationexercise.com/product_details/1")
driver.find_element(By.XPATH, "/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='cartModal']/div/div/div[3]/button").click()
time.sleep(5)
driver.get("https://automationexercise.com/view_cart")
driver.implicitly_wait(15)
#verify view cart
try:
    current_url = driver.current_url
except Exception as e:
    print(f"Error while getting the current url: {str(e)}")

expected_url = "https://automationexercise.com/view_cart"
try:
    if current_url == expected_url:
        print(f"Page url matches the expected url:{current_url}")
    else:
        print(f"Page URL ({current_url}) does not match the expected URL ({expected_url})")
except Exception as e:
    print(f"Error while verifying the URL: {str(e)}")

#fill up from
driver.find_element(By.XPATH, "//*[@id='do_action']/div[1]/div/div/a").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='checkoutModal']/div/div/div[2]/p[2]/a/u").click()
time.sleep(5)
first_name = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[2]")
time.sleep(5)
first_name.send_keys("farzana lubna890")
time.sleep(5)
email = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[3]")
time.sleep(5)
email.send_keys("farzanalubna890@yopmail.com")
time.sleep(5)
button = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/button")
button.click()
time.sleep(5)
mrs_radio_button = driver.find_element(By.XPATH, "//*[@id='id_gender2']")
time.sleep(5)
mrs_radio_button.click()
if mrs_radio_button.is_selected():
    print("Female radio button is selected.")
else:
    print("Female radio button is not selected.")
time.sleep(5)
password = driver.find_element(By.XPATH, "//*[@id='password']")
time.sleep(5)
password.send_keys("12345678")
time.sleep(5)
day_dropdown = Select(driver.find_element(By.XPATH, "//*[@id='days']"))
time.sleep(5)
day_dropdown.select_by_value("17")  # Replace "2" with the day you want to select
time.sleep(5)

month_dropdown = Select(driver.find_element(By.XPATH, "//*[@id='months']"))
time.sleep(5)
month_dropdown.select_by_visible_text("March")  # Replace with the month you want to select
time.sleep(5)

year_dropdown = Select(driver.find_element(By.XPATH, "//*[@id='years']"))
time.sleep(5)
year_dropdown.select_by_index(1)  # Replace with the index of the year option you want to select
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='newsletter']").click()
time.sleep(5)

name = driver.find_element(By.XPATH, "//*[@id='first_name']")
time.sleep(5)
name.send_keys("farzana")
time.sleep(5)

last_name = driver.find_element(By.XPATH, "//*[@id='last_name']")
time.sleep(5)
last_name.send_keys("lubna890")
time.sleep(5)

company = driver.find_element(By.XPATH, "//*[@id='company']")
time.sleep(5)
company.send_keys("asha ltd")
time.sleep(5)

address1 = driver.find_element(By.XPATH, "//*[@id='address1']")
time.sleep(5)
address1.send_keys("asha ltd, po-1234, street-gulshan 1")
time.sleep(5)

country = Select(driver.find_element(By.XPATH, "//*[@id='country']"))
time.sleep(5)
country.select_by_visible_text("Canada")
time.sleep(5)

state = driver.find_element(By.XPATH, "//*[@id='state']")
time.sleep(5)
state.send_keys("Alberta")
time.sleep(5)

city = driver.find_element(By.XPATH, "//*[@id='city']")
time.sleep(5)
city.send_keys("Toronto")
time.sleep(5)

zipcode = driver.find_element(By.XPATH, "//*[@id='zipcode']")
time.sleep(5)
zipcode.send_keys("12009")
time.sleep(5)

mobile_number = driver.find_element(By.XPATH, "//*[@id='mobile_number']")
time.sleep(5)
mobile_number.send_keys("+1416-555-0106")
time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div/form/button").click()
time.sleep(5)

# verify account created


try:
    current_url = driver.current_url
except Exception as e:
    print(f"Error while getting the current url: {str(e)}")

expected_url = "https://automationexercise.com/account_created"
try:
    if current_url == expected_url:
        print(f"Page url matches the expected url:{current_url}")
        continue_button = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div/a")
        time.sleep(5)
        continue_button.click()
        time.sleep(5)

    else:
        print(f"Page URL ({current_url}) does not match the expected URL ({expected_url})")
except Exception as e:
    print(f"Error while verifying the URL: {str(e)}")
time.sleep(5)
driver.get("https://automationexercise.com/")
try:
    # Replace the XPATH with the actual XPath or locator for the anchor element
    anchor_element = driver.find_element(By.XPATH, "//b[contains(text(),'farzana lubna890')]")
    time.sleep(5)
    # Verify if the anchor element contains the expected text
    expected_text = " Logged in as farzana lubna890 "  # Replace with the expected text
    if expected_text in anchor_element.text:
        print(f"Text '{expected_text}' found at the top. Verification successful!")
    else:
        print(f"Text '{expected_text}' not found at the top. Verification failed.")
except Exception as e:
    print(f"Verification failed: {str(e)}")

time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[3]/a").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='do_action']/div[1]/div/div/a").click()
time.sleep(5)

#verify order details
try:

    company_name_element = driver.find_element(By.XPATH, "//*[@id='address_delivery']/li[3]")
    time.sleep(5)
    address_element = driver.find_element(By.XPATH, "//*[@id='address_delivery']/li[4]")
    time.sleep(5)
    city_state_element = driver.find_element(By.XPATH, "//*[@id='address_delivery']/li[6]")
    time.sleep(5)
    country_name_element = driver.find_element(By.XPATH, "//*[@id='address_delivery']/li[7]")
    time.sleep(5)

    # Verify the address details
    expected_company_name = "asha ltd"
    expected_address_element = "asha ltd, po-1234, street-gulshan 1"
    expected_city_state_element = "Toronto Alberta 12009"
    expected_country_name_element = "Canada"
    time.sleep(5)
    if (expected_company_name in company_name_element.text and
            expected_address_element in address_element.text and
            expected_city_state_element in city_state_element.text and
            expected_country_name_element in country_name_element.text):
        print("Address details are as expected.")

    else:
        print("Address details verification failed.")
except Exception as e:
    print(f"Verification failed: {str(e)}")


#verify review order

# Step 3: Find the element displaying the total amount
try:
    # Replace the XPATH with the actual XPath or locator for the total amount element
    total_amount_element = driver.find_element(By.XPATH, "//*[@id='cart_info']/table/tbody/tr[2]/td[4]/p")

    # Get the total amount value
    total_amount = total_amount_element.text

    # Verify the total amount
    expected_total = "Rs. 500"  # Replace with the expected total amount
    if expected_total == total_amount:
        print(f"Total amount is correct: {total_amount}")
    else:
        print(f"Total amount verification failed. Expected: {expected_total}, Actual: {total_amount}")
except Exception as e:
    print(f"Verification failed: {str(e)}")

#add description
time.sleep(5)
description = driver.find_element(By.XPATH,"//*[@id='ordermsg']/textarea")
time.sleep(5)
description.send_keys("Order initiated. details is ok. send product safely")
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='cart_items']/div/div[7]/a").click()
time.sleep(5)
#payment details
name_element=driver.find_element(By.XPATH,"//*[@id='payment-form']/div[1]/div/input")
time.sleep(5)
name_element.send_keys("farzana lubna890")
time.sleep(5)
card_element = driver.find_element(By.XPATH,"//*[@id='payment-form']/div[2]/div/input")
time.sleep(5)
card_element.send_keys("678900")
time.sleep(5)
cvc_element = driver.find_element(By.XPATH, "//*[@id='payment-form']/div[3]/div[1]/input")
time.sleep(5)
cvc_element.send_keys("100")
time.sleep(5)
# expire_month = driver.find_element(By.XPATH, "//*[@id='payment-form']/div[3]/div[2]/input")
# time.sleep(5)
# expire_month.send_keys("03")
# time.sleep(6)

# Explicitly wait for the first field
expire_month = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='payment-form']/div[3]/div[2]/input"))
)
expire_month.clear()
expire_month.send_keys("03")

# Explicitly wait for the second field
expire_year = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='payment-form']/div[3]/div[3]/input"))
)
expire_year.clear()
expire_year.send_keys("2024")

# expire_year = driver.find_element(By.XPATH, "//*[@id='payment-form']/div[3]/div[3]/input")
# time.sleep(5)
# expire_month.send_keys("2024")
time.sleep(5)
place_order_btn = driver.find_element(By.XPATH, "//*[@id='submit']")
time.sleep(5)
place_order_btn.click()
time.sleep(5)

#verify success payment

try:
    # Replace the XPATH with the actual XPath or locator for the success message element
    success_message_element = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/p")

    # Verify the success message
    expected_message = 'Congratulations! Your order has been confirmed!'  # Replace with the expected message
    actual_message = success_message_element.text

    if expected_message == actual_message:
        print(f"Success message is as expected: '{expected_message}'")
    else:
        print(f"Success message verification failed. Expected: '{expected_message}', Actual: '{actual_message}'")
except Exception as e:
    print(f"Verification failed: {str(e)}")


driver.quit()
