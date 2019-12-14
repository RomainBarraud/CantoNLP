def initialize_browser():

    my_options = webdriver.ChromeOptions()
    driver_path = "C:/Data/chromedriver.exe"
    my_options.add_argument("--disable-extensions")
    my_options.add_argument("--profile-directory=Default")
    my_options.add_argument("--incognito")
    my_options.add_argument("--disable-plugins-discovery")
    my_options.add_argument("--start-maximized")
    my_options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(executable_path = driver_path, chrome_options = my_options)

    return browser

