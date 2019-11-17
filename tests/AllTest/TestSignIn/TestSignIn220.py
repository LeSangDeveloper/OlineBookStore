from selenium import webdriver
import unittest
import json
FileTest = open("TestSignIn220.json", "r")
user = json.load(FileTest)
class TestSignIn(unittest.TestCase):
    def test_TC220(self):
        global i
        i = 0
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc220@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("SA!12345")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC221(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc221@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sasa12345")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC222(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc222@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/")
        driver.quit()
    def test_TC223(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc223@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys(" Sa!12345")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC224(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc224@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345 ")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC225(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc225@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa! 12345")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
if __name__ == '__main__':
 suite = unittest.TestLoader().loadTestsFromTestCase(TestSignIn)
 unittest.TextTestRunner(verbosity=2).run(suite)
