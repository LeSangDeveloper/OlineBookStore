from selenium import webdriver
import unittest
import json
FileTest = open("TestSignUp.json", "r")
user = json.load(FileTest)
class TestSignUp(unittest.TestCase):
    def test_TC10(self):
        global i
        i = 0
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
                    
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys(txtName)
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys(txtEmail)
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys(txtPassword)
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        driver.quit()
    def test_TC11(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys(txtName)
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc11@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC12(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
                
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TC12")
        txtEmail = user[i] ["Email"]
        el = driver.find_element_by_name('email')
        el.send_keys(txtEmail)
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC13(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TC13")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc13@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys(txtPassword)
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
        
    def test_TC14(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("1414")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc14@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC15(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TC15!!!")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc15@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC16(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TCTest")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc16@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/")
        print(i)
        driver.quit()
    def test_TC17(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConeseven")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc17")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC18(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConeeight")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc18!#$$@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
        print(i)
        driver.quit()
    def test_TC19(self):
        global i
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signup")
            
        txtName = user[i]["Name"]
        el = driver.find_element_by_name('name')
        el.send_keys("TConenine")
        txtEmail = user[i]["Email"]  
        el = driver.find_element_by_name('email')
        el.send_keys("tc19@gmail.com")
        txtPassword = user[i]["Password"]
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signup').click()
        result = driver.current_url
        i = i + 1
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/")
        print(i)
        driver.quit()
    
if __name__ == '__main__':
 suite = unittest.TestLoader().loadTestsFromTestCase(TestSignUp)
 unittest.TextTestRunner(verbosity=2).run(suite)
