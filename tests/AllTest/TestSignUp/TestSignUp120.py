from selenium import webdriver
import unittest
import json
FileTest = open("TestSignUp120.json", "r")
user = json.load(FileTest)
class TestSignUp(unittest.TestCase):
    def test_TC120(self):
        global i
        i = 0
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConetwozero")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc120@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("!!!123##$")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC121(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConetwoone")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc121@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("!!@#$sa")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC122(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConetwotwo")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc122@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("sa!12345")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC123(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConetwothree")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc123@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!@#$!!")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC124(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConetwofour")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc124@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("SA!12345")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC125(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConetwofive")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc125@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Saa12345")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC126(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConetwosix")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc126@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/")
        print(i)
        driver.quit()
    def test_TC127(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConetwoseven")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc127@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys(" Sa!!12345")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC128(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConetwoeight")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc128@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!!12345 ")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC129(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConetwonine")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc129@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!! 12345")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
if __name__ == '__main__':
 suite = unittest.TestLoader().loadTestsFromTestCase(TestSignUp)
 unittest.TextTestRunner(verbosity=2).run(suite)
