from selenium import webdriver
import unittest
import json
FileTest = open("TestSignUp110.json", "r")
user = json.load(FileTest)
class TestSignUp(unittest.TestCase):
    def test_TC110(self):
        global i
        i = 0
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConeonezero")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc19@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC111(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConeoneone")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc111@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        i = i + 1
        print(i)
        driver.quit()
    def test_TC112(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConeonetwo")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc112@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("SASASASA")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC113(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConeonethree")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc113@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("12345678")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC114(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConeonefour")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc114@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("sasasasa")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC115(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConeonefive")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc115@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("!!@#$!!@")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC116(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConeonesix")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc116@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("SAS12345")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC117(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConeoneseven")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc117@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sasasasa")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC118(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConeoneeight")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc118@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("SA!!!@@#")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC119(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConeonenine")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc119@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("saaaa123")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
if __name__ == '__main__':
 suite = unittest.TestLoader().loadTestsFromTestCase(TestSignUp)
 unittest.TextTestRunner(verbosity=2).run(suite)
