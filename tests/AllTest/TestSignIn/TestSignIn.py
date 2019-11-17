from selenium import webdriver
import unittest
import json
FileTest = open("TestSignIn.json", "r")
user = json.load(FileTest)
class TestSignIn(unittest.TestCase):
    def test_TC20(self):
        global i
        i = 0
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys(txtEmail)
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys(txtPassword)
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC21(self):
        global i
        i = 0
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys(txtEmail)
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC22(self):
        global i
        i = 0
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc22@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys(txtPassword)
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC23(self):
        global i
        i = 0
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc23")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC24(self):
        global i
        i = 0
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc24!!!@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC25(self):
        global i
        i = 0
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc25@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC26(self):
        global i
        i = 0
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc26@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/")
        driver.quit()
    def test_TC27(self):
        global i
        i = 0
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc27@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        i = i + 1
        driver.quit()
    def test_TC28(self):
        global i
        i = 0
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc28@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("SASASASA")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC29(self):
        global i
        i = 0
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc29@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("12345678")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()

if __name__ == '__main__':
 suite = unittest.TestLoader().loadTestsFromTestCase(TestSignIn)
 unittest.TextTestRunner(verbosity=2).run(suite)
