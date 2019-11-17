from selenium import webdriver
import unittest
class TestAdminUP490(unittest.TestCase):
    def test_TC490(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(2) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/update-Product")
        driver.find_element_by_css_selector("body > div.container > div.row > div > div > div > div:nth-child(4) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        el = driver.find_element_by_name('price')
        el.send_keys("20.5")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/postupdateProduct")
        driver.quit()
    def test_TC491(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(2) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/update-Product")
        driver.find_element_by_css_selector("body > div.container > div.row > div > div > div > div:nth-child(4) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        el = driver.find_element_by_name('price')
        el.send_keys("20..5")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        driver.quit()
    def test_TC492(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(2) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/update-Product")
        driver.find_element_by_css_selector("body > div.container > div.row > div > div > div > div:nth-child(4) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        el = driver.find_element_by_name('price')
        el.send_keys("20.5.")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        driver.quit()
    def test_TC493(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(2) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/update-Product")
        driver.find_element_by_css_selector("body > div.container > div.row > div > div > div > div:nth-child(4) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        el = driver.find_element_by_name('price')
        el.send_keys(".20.5")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        driver.quit()
    def test_TC494(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(2) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/update-Product")
        driver.find_element_by_css_selector("body > div.container > div.row > div > div > div > div:nth-child(4) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        el = driver.find_element_by_name('in-stock')
        el.send_keys(" ")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        driver.quit()
    def test_TC495(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(2) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/update-Product")
        driver.find_element_by_css_selector("body > div.container > div.row > div > div > div > div:nth-child(4) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("!!!")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        driver.quit()
    def test_TC496(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(2) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/update-Product")
        driver.find_element_by_css_selector("body > div.container > div.row > div > div > div > div:nth-child(4) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("KHANG")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        driver.quit()
    def test_TC497(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(2) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/update-Product")
        driver.find_element_by_css_selector("body > div.container > div.row > div > div > div > div:nth-child(4) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("khang")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        driver.quit()
    def test_TC498(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(2) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/update-Product")
        driver.find_element_by_css_selector("body > div.container > div.row > div > div > div > div:nth-child(4) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("5")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/postupdateProduct")
        driver.quit()
    def test_TC499(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(2) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/update-Product")
        driver.find_element_by_css_selector("body > div.container > div.row > div > div > div > div:nth-child(4) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("5khang")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        driver.quit()
    def test_TC500(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(2) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/update-Product")
        driver.find_element_by_css_selector("body > div.container > div.row > div > div > div > div:nth-child(4) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("5!!!")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        driver.quit()
    def test_TC501(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(2) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/update-Product")
        driver.find_element_by_css_selector("body > div.container > div.row > div > div > div > div:nth-child(4) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("5 ")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        driver.quit()
if __name__ == '__main__':
 suite = unittest.TestLoader().loadTestsFromTestCase(TestAdminUP490)
 unittest.TextTestRunner(verbosity=2).run(suite)
