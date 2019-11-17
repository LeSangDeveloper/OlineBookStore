from selenium import webdriver
import unittest
class TestAdmin(unittest.TestCase):
    def test_TC40(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("tc126@gmail.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/")
        driver.quit()
    def test_TC41(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        driver.quit()
    def test_TC42(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(1) > a").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        driver.quit()
    def test_TC43(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(2) > a").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/update-Product")
        driver.quit()
    def test_TC46(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(1) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        el = driver.find_element_by_name('title')
        el.send_keys("")
        el = driver.find_element_by_name('author')
        el.send_keys("Khang Nguyen")
        el = driver.find_element_by_name('price')
        el.send_keys("20")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("5")
        el = driver.find_element_by_name('description')
        el.send_keys("Best for your Life")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        driver.quit()
    def test_TC47(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(1) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        el = driver.find_element_by_name('title')
        el.send_keys("Your Life")
        el = driver.find_element_by_name('author')
        el.send_keys("")
        el = driver.find_element_by_name('price')
        el.send_keys("20")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("5")
        el = driver.find_element_by_name('description')
        el.send_keys("Best for your Life")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        driver.quit()
    def test_TC48(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(1) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        el = driver.find_element_by_name('title')
        el.send_keys("Your Life")
        el = driver.find_element_by_name('author')
        el.send_keys("Khang Nguyen")
        el = driver.find_element_by_name('price')
        el.send_keys("")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("5")
        el = driver.find_element_by_name('description')
        el.send_keys("Best for your Life")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        driver.quit()
    def test_TC49(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(1) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        el = driver.find_element_by_name('title')
        el.send_keys("Your Life")
        el = driver.find_element_by_name('author')
        el.send_keys("Khang Nguyen")
        el = driver.find_element_by_name('price')
        el.send_keys("20")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("")
        el = driver.find_element_by_name('description')
        el.send_keys("Best for your Life")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        driver.quit()
if __name__ == '__main__':
 suite = unittest.TestLoader().loadTestsFromTestCase(TestAdmin)
 unittest.TextTestRunner(verbosity=2).run(suite)
