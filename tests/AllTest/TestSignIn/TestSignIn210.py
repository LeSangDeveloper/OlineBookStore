from selenium import webdriver
import unittest
import json
FileTest = open("TestSignIn210.json", "r")
user = json.load(FileTest)
class TestSignIn(unittest.TestCase):
    def test_TC210(self):
        global i
        i = 0
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc210@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("sasasasa")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC211(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc211@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("!!@@##$$")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC212(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc212@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("SASA12345")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC213(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc213@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("SASAsasa")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC214(self):
        global i
        i = 0
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc214@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("SASA!!@@")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC215(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc215@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("sasa12345")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC216(self):
        global i
        i = 0
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc216@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("!!@@12345")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC217(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc217@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("!!@@sasa")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC218(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc218@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("sasa!!@@")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
    def test_TC219(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
                    
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc219@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sasa!!@@")
        el = driver.find_element_by_name('signin').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signin")
        driver.quit()
if __name__ == '__main__':
 suite = unittest.TestLoader().loadTestsFromTestCase(TestSignIn)
 unittest.TextTestRunner(verbosity=2).run(suite)
