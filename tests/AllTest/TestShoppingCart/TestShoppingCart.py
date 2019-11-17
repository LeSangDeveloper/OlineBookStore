from selenium import webdriver
import unittest
class TestShoppingCart(unittest.TestCase):
    def test_TC30(self):
        
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        el = driver.find_element_by_name('add1')
        driver.implicitly_wait(10)
        el.send_keys("")
        el = driver.find_element_by_name('addtocart1').click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/")
        driver.quit()
    def test_TC31(self):
        
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        el = driver.find_element_by_name('add1')
        driver.implicitly_wait(10)
        el.send_keys("2")
        el = driver.find_element_by_name('addtocart1').click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC32(self):
        
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        el = driver.find_element_by_name('add1')
        driver.implicitly_wait(10)
        el.send_keys("a")
        el = driver.find_element_by_name('addtocart1').click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/")
        driver.quit()
    def test_TC33(self):
        
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        el = driver.find_element_by_css_selector("#bs-example-navbar-collapse-1 > ul > li:nth-child(1) > a > span").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC34(self):
        
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        el = driver.find_element_by_name('add1')
        driver.implicitly_wait(10)
        el.send_keys("2")
        el = driver.find_element_by_name('addtocart1').click()
        el = driver.find_element_by_css_selector("#bs-example-navbar-collapse-1 > ul > li:nth-child(1) > a > span").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC35(self):
        
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
        el.send_keys("")
        el = driver.find_element_by_name('addtocart1').click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/")
        driver.quit()
    def test_TC36(self):
        
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
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/add-to-cart/1")
        driver.quit()
    def test_TC37(self):
        
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
        el.send_keys("a")
        el = driver.find_element_by_name('addtocart1').click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/")
        driver.quit()
    def test_TC38(self):
        
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        
        el = driver.find_element_by_name('email')
        el.send_keys("tc126@gmail.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()

        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/")
        el = driver.find_element_by_css_selector("#bs-example-navbar-collapse-1 > ul > li:nth-child(1) > a > span").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/shoppingCart")
        driver.quit()
    def test_TC39(self):
        
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
        driver.implicitly_wait(10)
        c1 = driver.find_element_by_css_selector("body > div > div:nth-child(1) > div:nth-child(1) > div > div > h3").text
        el = driver.find_element_by_css_selector("#bs-example-navbar-collapse-1 > ul > li:nth-child(1) > a > span").click()
        b1 = driver.find_element_by_css_selector("body > div > div:nth-child(1) > div > ul > li > span.badge").text
        b2 = "2"
        c2 = driver.find_element_by_css_selector("body > div > div:nth-child(1) > div > ul > li:nth-child(1) > strong").text
        t1 = (b1 == b2)
        t2 = c2 in c1
        self.assertTrue(t1 and t2)
        driver.quit()
if __name__ == '__main__':
 suite = unittest.TestLoader().loadTestsFromTestCase(TestShoppingCart)
 unittest.TextTestRunner(verbosity=2).run(suite)
