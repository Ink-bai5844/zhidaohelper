# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# # 设置 Chrome 驱动路径
# service = Service('chromedriver-win64/chromedriver.exe')  # 确保替换为实际路径
# driver = webdriver.Chrome(service=service)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# 设置 Edge 驱动路径
service = Service('edgedriver_win64/msedgedriver.exe')  # 确保替换为实际路径
driver = webdriver.Edge(service=service)


# 打开网页
driver.get('https://studyvideoh5.zhihuishu.com/stuStudy?recruitAndCourseId=485e5f58415b4859454a58595d455c4251')