from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# 设置 Chrome 驱动路径
service = Service('chromedriver-win64/chromedriver.exe')  # 确保替换为实际路径
driver = webdriver.Chrome(service=service)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# # 设置 Edge 驱动路径
# service = Service('edgedriver_win64/msedgedriver.exe')  # 确保替换为实际路径
# driver = webdriver.Edge(service=service)


# 打开网页
driver.get('https://onlineweb.zhihuishu.com/onlinestuh5')

time.sleep(3)

# 定位账号输入框并填写账号
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'lUsername'))
)
username_field.send_keys("15131815512")  # 替换为你的账号

# 定位密码输入框并填写密码
password_field = driver.find_element(By.ID, 'lPassword')
password_field.send_keys("Lhk051212")  # 替换为你的密码

# 模拟点击登录按钮
login_button = driver.find_element(By.CLASS_NAME, 'wall-sub-btn')
login_button.click()

print("登录按钮已点击")

time.sleep(15)

try:

    # 点击关闭按钮（如果存在）
    try:
        close_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.iconfont.iconguanbi'))
        )
        close_icon.click()
        print("已点击关闭按钮")
    except Exception as e:
        print(f"关闭按钮点击时出错: {e}")

    # 等待并找到所有视频列表项
    items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.video .catalogue_title'))
    )

    # 依次点击每个视频
    for item in items:

        # 滚动到该元素，以确保其可见
        driver.execute_script("arguments[0].scrollIntoView();", item)

        item.click()
        print(f"已点击视频: {item.text}")

        time.sleep(2)

        # 检测弹窗是否出现（如果弹窗有 role="dialog"）
        try:
            dialog = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[@role="dialog" and @aria-label="弹题测验"]'))
            )
            print("弹窗已出现")

            # 等待并点击 "关闭" 按钮
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@class="btn" and text()="关闭"]'))
            )
            close_button.click()
            print("已点击 '关闭' 按钮")

        except Exception as popup_exception:
            print(f"未检测到弹窗或弹窗操作失败: {popup_exception}")

        time.sleep(2)

        # 假设 video_area 已经获取
        video_area = driver.find_element(By.CLASS_NAME, 'videoArea')

        # 创建 ActionChains 对象
        actions = ActionChains(driver)

        # 移动鼠标到视频区域
        actions.move_to_element(video_area).perform()

        # 暂停一段时间以保持鼠标在视频区域上
        time.sleep(1)  # 根据需要调整时间

        # 找到视频播放时间和总时长的元素
        current_time_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.nPlayTime .currentTime'))
        )
        duration_time_element = driver.find_element(By.CSS_SELECTOR, 'div.nPlayTime .duration')

        flag = 1

        # 获取当前时间和总时长
        current_time = current_time_element.text
        duration_time = duration_time_element.text

        print(f"当前时间: {current_time} / 总时长: {duration_time}")

        # 如果当前时间和总时长相等，说明视频播放完毕
        if current_time >= duration_time:
            print("视频之前已经播放完毕！")
            flag = 0
        else:
            try:
                # 点击视频区域继续播放
                video_area = driver.find_element(By.CLASS_NAME, 'videoArea')
                video_area.click()
                print("已点击视频区域播放")
            except Exception as e:
                print(f"点击视频区域失败: {e}")

        # 循环检测视频是否播放完毕
        while flag:
            try:
                # 移动鼠标到视频区域
                actions.move_to_element(video_area).perform()

                # 暂停一段时间以保持鼠标在视频区域上
                time.sleep(1)  # 根据需要调整时间

                # 找到视频播放时间和总时长的元素
                current_time_element1 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.nPlayTime .currentTime'))
                )
                duration_time_element1 = driver.find_element(By.CSS_SELECTOR, 'div.nPlayTime .duration')

                # 获取当前时间和总时长
                current_time1 = current_time_element1.text
                duration_time1 = duration_time_element1.text

                print(f"当前时间: {current_time1} / 总时长: {duration_time1}")

                # 如果当前时间和总时长相等，说明视频播放完毕
                if (current_time1 == duration_time1 and current_time1 != ""):
                    print("视频播放完毕！")
                    break

                # 检测弹窗是否出现（如果弹窗有 role="dialog"）
                try:
                    dialog = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//div[@role="dialog" and @aria-label="弹题测验"]'))
                    )
                    print("弹窗已出现")

                    # 等待并点击 "关闭" 按钮
                    close_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//div[@class="btn" and text()="关闭"]'))
                    )
                    close_button.click()
                    print("已点击 '关闭' 按钮")

                    # 点击视频区域继续播放
                    video_area = driver.find_element(By.CLASS_NAME, 'videoArea')
                    video_area.click()
                    print("已点击视频区域继续播放")

                except Exception as popup_exception:
                    print(f"未检测到弹窗或弹窗操作失败: {popup_exception}")

                # 每次循环后暂停几秒，避免过度检测
                time.sleep(3)

            except Exception as e:
                print(f"检测播放状态时出错: {e}")
                break

except Exception as e:
    print(f"出错: {e}")
finally:
    driver.quit()
