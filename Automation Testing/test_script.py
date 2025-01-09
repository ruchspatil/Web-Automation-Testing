from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
 
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  

driver.get("https://expensetracker-site.netlify.app/")

driver.maximize_window()

try:
    get_started_button = driver.find_element(By.XPATH, "//button[text()='Get Started']")
    get_started_button.click()
    time.sleep(2)  
   
    expense_name = driver.find_element(By.NAME, "expenseName") 
    amount = driver.find_element(By.NAME, "amount")  
    
    expense_name.send_keys("Lunch")
    amount.send_keys("15.50")
    
  
    add_expense_button = driver.find_element(By.XPATH, "//button[text()='Add Expense']")
    add_expense_button.click()
    time.sleep(2)  

   
    expense_list = driver.find_element(By.XPATH, "//div[@class='expense-list']")  
    expense_items = expense_list.find_elements(By.TAG_NAME, "li") 
    
    assert len(expense_items) > 0, "No expenses found"
    print("Expense added successfully.")

    first_expense = expense_items[0]
    edit_button = first_expense.find_element(By.XPATH, ".//button[text()='Edit']") 
    edit_button.click()
    time.sleep(2)
    
    amount_field = driver.find_element(By.NAME, "amount") 
    amount_field.clear()  
    amount_field.send_keys("20.00")  
    save_button = driver.find_element(By.XPATH, "//button[text()='Save']") 
    save_button.click()
    time.sleep(2)
    
  
    updated_amount = first_expense.find_element(By.XPATH, ".//span[@class='amount']") 
    assert updated_amount.text == "20.00", f"Amount not updated. Found: {updated_amount.text}"


    delete_button = first_expense.find_element(By.XPATH, ".//button[text()='Delete']") 
    delete_button.click()
    time.sleep(2)
    
    
    expense_items_after_deletion = driver.find_elements(By.XPATH, "//div[@class='expense-list']//li") 
    assert len(expense_items_after_deletion) == len(expense_items) - 1, "Expense not deleted"

    print("Test completed successfully.")

finally:
    driver.quit()
