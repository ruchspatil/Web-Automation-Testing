from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver 
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Adjust path to your chromedriver

# Open the website
driver.get("https://expensetracker-site.netlify.app/")

driver.maximize_window()

try:
    # Step 1: Click the "Get Started" button
    get_started_button = driver.find_element(By.XPATH, "//button[text()='Get Started']")
    get_started_button.click()
    time.sleep(2)  # Wait for the form to appear
    
    # Step 2: Fill out the expense form
    # Example: Let's assume the form has fields for "Expense Name", "Amount", "Category", and "Date".
    expense_name = driver.find_element(By.NAME, "expenseName")  # Adjust if the name of the field is different
    amount = driver.find_element(By.NAME, "amount")  # Adjust if the name of the field is different
    
    expense_name.send_keys("Lunch")
    amount.send_keys("15.50")
    
    # Step 3: Click the "Add Expense" button
    add_expense_button = driver.find_element(By.XPATH, "//button[text()='Add Expense']")
    add_expense_button.click()
    time.sleep(2)  # Wait for the expense to be added

    # Step 4: Verify that the expense appears on the screen
    expense_list = driver.find_element(By.XPATH, "//div[@class='expense-list']")  
    expense_items = expense_list.find_elements(By.TAG_NAME, "li") 
    
    assert len(expense_items) > 0, "No expenses found"
    print("Expense added successfully.")

    # Step 5: Edit or delete an expense 
    first_expense = expense_items[0]
    edit_button = first_expense.find_element(By.XPATH, ".//button[text()='Edit']") 
    edit_button.click()
    time.sleep(2)
    
    # Example of editing the expense (changing the amount)
    amount_field = driver.find_element(By.NAME, "amount") 
    amount_field.clear()  
    amount_field.send_keys("20.00")  
    save_button = driver.find_element(By.XPATH, "//button[text()='Save']") 
    save_button.click()
    time.sleep(2)
    
    # Verify that the expense amount has been updated
    updated_amount = first_expense.find_element(By.XPATH, ".//span[@class='amount']") 
    assert updated_amount.text == "20.00", f"Amount not updated. Found: {updated_amount.text}"

    # Step 6: Delete the expense
    delete_button = first_expense.find_element(By.XPATH, ".//button[text()='Delete']")  # Adjust as per your actual DOM
    delete_button.click()
    time.sleep(2)
    
    # Verify the expense is deleted
    expense_items_after_deletion = driver.find_elements(By.XPATH, "//div[@class='expense-list']//li") 
    assert len(expense_items_after_deletion) == len(expense_items) - 1, "Expense not deleted"

    print("Test completed successfully.")

finally:
    driver.quit()
