from selenium import webdriver
import unittest
class TestAdminUP(unittest.TestCase):
    def test_TC457(self):
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
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        driver.quit()
    def test_TC458(self):
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
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/postupdateProduct")
        driver.quit()
    def test_TC459(self):
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
        el = driver.find_element_by_name('title')
        el.send_keys(" ")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/updateProduct/1")
        driver.quit()
if __name__ == '__main__':
 suite = unittest.TestLoader().loadTestsFromTestCase(TestAdminUP)
 unittest.TextTestRunner(verbosity=2).run(suite)
