from selenium import webdriver
import unittest
class TestOrder(unittest.TestCase):
    def test_TC316(self):
        
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        
        el = driver.find_element_by_name('email')
        el.send_keys("tc126@gmail.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()

        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        el = driver.find_element_by_name('add1')
        driver.implicitly_wait(10)
        el.send_keys("2")
        el = driver.find_element_by_name('addtocart1').click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        el = driver.find_element_by_name('add2')
        driver.implicitly_wait(10)
        el.send_keys("2")
        el = driver.find_element_by_name('addtocart2').click()

        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        driver.find_element_by_css_selector("#bs-example-navbar-collapse-1 > ul > li:nth-child(1) > a").click()
        el = driver.find_element_by_css_selector("body > div > div:nth-child(2) > div:nth-child(2) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/checkout")
        el = driver.find_element_by_name("name-order")
        el.send_keys("")
        el = driver.find_element_by_css_selector("#address")
        el.send_keys("")
        el = driver.find_element_by_css_selector("#number-phone")
        el.send_keys("")
        el = driver.find_element_by_css_selector("#checkout-form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/checkout")
        driver.quit()
    def test_TC317(self):
        
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        
        el = driver.find_element_by_name('email')
        el.send_keys("tc126@gmail.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()

        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        el = driver.find_element_by_name('add1')
        driver.implicitly_wait(10)
        el.send_keys("2")
        el = driver.find_element_by_name('addtocart1').click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        el = driver.find_element_by_name('add2')
        driver.implicitly_wait(10)
        el.send_keys("2")
        el = driver.find_element_by_name('addtocart2').click()

        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        driver.find_element_by_css_selector("#bs-example-navbar-collapse-1 > ul > li:nth-child(1) > a").click()
        el = driver.find_element_by_css_selector("body > div > div:nth-child(2) > div:nth-child(2) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/checkout")
        el = driver.find_element_by_name("name-order")
        el.send_keys("")
        el = driver.find_element_by_css_selector("#address")
        el.send_keys("371 Nguyen Kiem")
        el = driver.find_element_by_css_selector("#number-phone")
        el.send_keys("12345678")
        el = driver.find_element_by_css_selector("#checkout-form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/checkout")
        driver.quit()
    def test_TC318(self):
        
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        
        el = driver.find_element_by_name('email')
        el.send_keys("tc126@gmail.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()

        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        el = driver.find_element_by_name('add1')
        driver.implicitly_wait(10)
        el.send_keys("2")
        el = driver.find_element_by_name('addtocart1').click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        el = driver.find_element_by_name('add2')
        driver.implicitly_wait(10)
        el.send_keys("2")
        el = driver.find_element_by_name('addtocart2').click()

        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        driver.find_element_by_css_selector("#bs-example-navbar-collapse-1 > ul > li:nth-child(1) > a").click()
        el = driver.find_element_by_css_selector("body > div > div:nth-child(2) > div:nth-child(2) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/checkout")
        el = driver.find_element_by_name("name-order")
        el.send_keys("Khang Nguyen")
        el = driver.find_element_by_css_selector("#address")
        el.send_keys("")
        el = driver.find_element_by_css_selector("#number-phone")
        el.send_keys("12345678")
        el = driver.find_element_by_css_selector("#checkout-form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/checkout")
        driver.quit()
    def test_TC319(self):
        
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        
        el = driver.find_element_by_name('email')
        el.send_keys("tc126@gmail.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()

        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        el = driver.find_element_by_name('add1')
        driver.implicitly_wait(10)
        el.send_keys("2")
        el = driver.find_element_by_name('addtocart1').click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        el = driver.find_element_by_name('add2')
        driver.implicitly_wait(10)
        el.send_keys("2")
        el = driver.find_element_by_name('addtocart2').click()

        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        driver.find_element_by_css_selector("#bs-example-navbar-collapse-1 > ul > li:nth-child(1) > a").click()
        el = driver.find_element_by_css_selector("body > div > div:nth-child(2) > div:nth-child(2) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/checkout")
        el = driver.find_element_by_name("name-order")
        el.send_keys("Khang Nguyen")
        el = driver.find_element_by_css_selector("#address")
        el.send_keys("371 Nguyen Kiem")
        el = driver.find_element_by_css_selector("#number-phone")
        el.send_keys("")
        el = driver.find_element_by_css_selector("#checkout-form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/checkout")
        driver.quit()
    def test_TC320(self):
        
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        
        el = driver.find_element_by_name('email')
        el.send_keys("tc126@gmail.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()

        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        el = driver.find_element_by_name('add1')
        driver.implicitly_wait(10)
        el.send_keys("2")
        el = driver.find_element_by_name('addtocart1').click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        el = driver.find_element_by_name('add2')
        driver.implicitly_wait(10)
        el.send_keys("2")
        el = driver.find_element_by_name('addtocart2').click()

        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        driver.find_element_by_css_selector("#bs-example-navbar-collapse-1 > ul > li:nth-child(1) > a").click()
        el = driver.find_element_by_css_selector("body > div > div:nth-child(2) > div:nth-child(2) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/checkout")
        el = driver.find_element_by_name("name-order")
        el.send_keys("Khang Nguyen")
        el = driver.find_element_by_css_selector("#address")
        el.send_keys("371 Nguyen Kiem")
        el = driver.find_element_by_css_selector("#number-phone")
        el.send_keys("12345678")
        el = driver.find_element_by_css_selector("#checkout-form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/")
        driver.quit()
if __name__ == '__main__':
 suite = unittest.TestLoader().loadTestsFromTestCase(TestOrder)
 unittest.TextTestRunner(verbosity=2).run(suite)
