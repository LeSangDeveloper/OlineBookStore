from selenium import webdriver
import unittest
class TestShoppingCart310(unittest.TestCase):
    def test_TC310(self):
        
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
        driver.find_element_by_css_selector("#bs-example-navbar-collapse-1 > ul > li:nth-child(1) > a").click()
        el = driver.find_element_by_css_selector("body > div > div:nth-child(1) > div > ul > li:nth-child(1) > div > a:nth-child(2)").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/removeOne/1")
        driver.quit()
    def test_TC311(self):
        
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
        driver.find_element_by_css_selector("#bs-example-navbar-collapse-1 > ul > li:nth-child(1) > a").click()
        el = driver.find_element_by_css_selector("body > div > div:nth-child(1) > div > ul > li:nth-child(1) > div > a:nth-child(1)").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/removeAll/1")
        driver.quit()
    def test_TC312(self):
        
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
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/shoppingCart")
        el = driver.find_element_by_css_selector("body > div > div:nth-child(1) > div > ul > li:nth-child(2) > div > a:nth-child(2)").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/removeOne/2")
        driver.quit()
    def test_TC313(self):
        
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
        el = driver.find_element_by_css_selector("body > div > div:nth-child(1) > div > ul > li:nth-child(2) > div > a:nth-child(1)").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/removeAll/2")
        driver.quit()
    def test_TC314(self):
        
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
        driver.find_element_by_css_selector("#bs-example-navbar-collapse-1 > ul > li:nth-child(1) > a").click()
        n = int(driver.find_element_by_css_selector("body > div > div:nth-child(1) > div > ul > li > span.badge").text)
        while (n > 0):
            driver.find_element_by_css_selector("body > div > div:nth-child(1) > div > ul > li > div > a:nth-child(2)").click()
            n = n - 1
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/removeOne/1")
        driver.quit()
    def test_TC315(self):
        
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
        n = int(driver.find_element_by_css_selector("body > div > div:nth-child(1) > div > ul > li:nth-child(2) > span.badge").text)
        while (n > 0):
            driver.find_element_by_css_selector("body > div > div:nth-child(1) > div > ul > li:nth-child(2) > div > a:nth-child(2)").click()
            n = n - 1
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/removeOne/2")
        driver.quit()
if __name__ == '__main__':
 suite = unittest.TestLoader().loadTestsFromTestCase(TestShoppingCart310)
 unittest.TextTestRunner(verbosity=2).run(suite)
