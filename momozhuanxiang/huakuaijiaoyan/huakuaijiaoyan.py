#滑动 模块验证


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class seleniumLogin()
    def __init__(self, timeout=20):
        self.timeout = timeout
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, self.timeout)

    def login(self):
        # ....其他代码....

        # 获取滑动滑块
        slide = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'div#nc_1__scale_text > span.nc-lang-cnt'))
        )
        # 获取滑块滑动距离
        distance = slide.size['width']
        # 生成滑动轨迹
        tracks = self.get_tracks(self, distance):
        # 获取滑块点击按钮
        slide_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'span#nc_1_n1z'))
        )
        # 滑动滑块进行验证
        self.move_to_gap(slide_button, tracks)