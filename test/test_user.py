from selenium import webdriver


    # def test_user():
    
    # Create a user
    # self.driver = webdriver.Firefox()
    # self.my_user = login.user.objects.create_user(username=USERNAME, email=None, password=PASSWORD)

    # # User login
    # selenium.get('http://127.0.0.1:8000/login')
    # username.send_keys(my_user.username)
    # password.send_keys(my_user.password)
    # self.driver.find_element_by_css_selector('logBtn').click()

    # # User search
    # selenium.get('http://127.0.0.1:8000/login')
    
    # # User save favorite

    # # User favorite page
    # selenium.get('http://127.0.0.1:8000/favorites')

def setUp():
    self.driver = webdriver.Firefox()

def tearDown():
    self.driver.quit()


def test_user_url():
    setUp()
    self.driver.get(self.get_server_url())
    assert self.driver.current_url == 'http://localhost:8000/'
    tearDown()

def test_user_login():
    setUp()
    # create a user
    my_user = login.user.objects.create_user(username="username", email="username@mail.fr", password="password")
    # open login page
    selenium.get('http://127.0.0.1:8000/login')
    # user login
    username.send_keys(my_user.username)
    password.send_keys(my_user.password)
    self.driver.find_element_by_css_selector('logBtn').click()
    assert self.driver.user == my_user
    tearDown()

def test_user_search():
    # open search page
    selenium.get('http://127.0.0.1:8000/search')
    