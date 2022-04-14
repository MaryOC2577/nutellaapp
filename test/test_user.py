from selenium import webdriver

def test_user():
    
    # Create a user
    self.driver = webdriver.Firefox()
    self.my_user = login.user.objects.create_user(username=USERNAME, email=None, password=PASSWORD)

    # User login
    selenium.get('http://127.0.0.1:8000/login')
    username.send_keys(my_user.username)
    password.send_keys(my_user.password)
    self.driver.find_element_by_css_selector('logBtn').click()

    # User search
    selenium.get('http://127.0.0.1:8000/login')
    
    # User save favorite

    # User favorite page
    selenium.get('http://127.0.0.1:8000/favorites')
