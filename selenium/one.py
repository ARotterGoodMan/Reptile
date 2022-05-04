from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
from CrackVerificationCode.CrackVerificationCode import CrackVerificationCode
import time

CrackVerificationCode = CrackVerificationCode('sxy12363', 'Shao264419', '932825')

web = Chrome()


def crack_verification(crack_verification_code):
    web.get("https://www.chaojiying.com/user/login/")
    web.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input").send_keys("sxy12363")
    web.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input").send_keys("Shao264419")
    code = web.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div[1]/form/div/img").screenshot_as_png
    code_str = crack_verification_code.post_pic(code, 1902)['pic_str']
    web.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input").send_keys(code_str)
    time.sleep(1)
    web.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()


if __name__ == '__main__':
    crack_verification(CrackVerificationCode)
