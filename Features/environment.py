from selenium.webdriver import Chrome


def before_all(context):
    path = "C:\\Users\\User\\Desktop\\Chrome WebDriver\\chromedriver_win32\\chromedriver.exe"
    context.driver = Chrome(executable_path=path)


def after_all(context):
    context.driver.close()

