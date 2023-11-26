# By Bishesh
import os
import sys
import requests
import bs4
import time
import random
import json
import string
from bs4 import BeautifulSoup
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null')

try:
    import bs4
except ImportError:
    print('\n [×] Module Bs4 Not installed!...\n')
    os.system('pip install bs4')
banner = '''   \033[34m╔╗   ╦  ╔═╗  ╦ ╦  ╔═╗  ╔═╗  ╦ ╦\033[0m 
   \033[34m╠╩╗  ║  ╚═╗  ╠═╣  ║╣   ╚═╗  ╠═╣\033[35m•v1\033\033[0m 
   \033[37m╚═╝  ╩  ╚═╝  ╩ ╩  ╚═╝  ╚═╝  ╩ ╩ \033[0m
         \033[92mDEVELOPED BY:BISHESH\033[0m
\033[34m╚═╦═════════════════════════╦═╝
╔═════╩═════════════════════════╩════╗\033[37m
  [0] Login
  [1] Facebook New ID Generator
  [2] File Cloning 
  [3] Generate Cookies
  [4] Log out\033[0m \033[34m
╚═════════════════════════════════════╝\033[0m '''

# Display the banner
print(banner)

# User input
choice = int(input("Enter your choice: "))
if choice == 0 :
    print("Coming Soon")
  
elif choice == 1 :
    def convert(cok):
        __for = 'datr=' + cok['datr'] + ';' + ('sb=' + cok['sb']) + ';' + ('fr=' + cok['fr']) + ';' + ('c_user=' + cok['c_user']) + ';' + ('xs=' + cok['xs'])
        return __for

    def inbox(session):
        time.sleep(1)
        ses = requests.Session()
        __ = str(time.time()).replace('.', '')[:13]
        data = ses.get(f"https://10minutemail.net/address.api.php?sessionid={session}&_={str(__)}").json()
        if len(data["mail_list"]) != 1:
            address = data["mail_list"][0]["subject"]
            session = address.replace('FB-', '').replace('is your Facebook confirmation code', '')
            return session

    ugen = []
    for xd in range(5000):
        aa = 'Mozilla/5.0 (Linux; U; Android'
        b = random.choice(['5', '6', '7', '8', '9', '10', '11', '12'])
        if b in ['5', '6', '7', '8', '9']:
            z = random.choice(['0', '1'])
            bv = b + '.' + z + '.' + z
        else:
            bv = b
        B = ['GT-', 'SM-']
        c = random.choice(B)
        d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e = random.randrange(1, 999)
        f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h = random.randrange(73, 100)
        i = '0'
        j = random.randrange(4200, 4900)
        k = random.randrange(40, 150)
        l = 'Mobile Safari/537.36'
        application_version = str(random.randint(111, 396)) + '.0.0.' + str(random.randrange(10, 49)) + '.' + str(random.randint(111, 396))
        V = str(random.randrange(11, 99))
        uas = f'{aa} {bv}; {c}{d}{e}{f} Build/{d}{f}{V}{f}; wv) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uas)
boy = ['Hari Kc', 'Basanta Sharma', 'Abhinav Maharjan', 'Aditya Bhandari', 'Alok Gautam', 'Aman Gurung', 'Amit Basnet', 'Aniket Thapa', 'Anmol Joshi', 'Anshu Regmi', 'Arjun Adhikari', 'Ashish Chhetri', 'Ayush Shahi', 'Bhupendra Rai', 'Bibek Oli', 'Bimal Lama', 'Binay Tamang', 'Biren Khadka', 'Bishal Pant', 'Bishesh Bhusal', 'Buddha Rana', 'Chandra Bhattarai', 'Chetan Aryal', 'Dhiraj Rijal', 'Dipesh Lama', 'Gaurav Yadav', 'Gopal Bohara', 'Govind Budhathoki', 'Hari Karki', 'Himanshu Sapkota', 'Indra Neupane', 'Ishan Pandey', 'Jeevan Kunwar', 'Jivan Basnyat', 'Kailash Koirala', 'Keshav Chapagain', 'Kiran Poudel', 'Krishna Lamsal', 'Kshitiz Bista', 'Kumar Dangol', 'Kushal Kafle', 'Lokesh Kandel', 'Manish Subedi', 'Milan Limbu', 'Mohan Bohora', 'Nabin Budha', 'Nischal Magar', 'Niraj Sunar', 'Niroj Lama', 'Nischit Pariyar', 'Pawan Adhikari', 'Prabin Bista', 'Pranav Shrestha', 'Prasanna Aryal', 'Pratik Rai', 'Prem Giri', 'Raj Khatiwada', 'Rajan Joshi', 'Rajeev Kunwar', 'Rakesh Panta', 'Ravi Sharma', 'Rohit Bhattarai', 'Rupesh Raut', 'Sabin Chaudhary', 'Sagar Bista', 'Sahil Thakuri', 'Sameer Baniya', 'Samrat Dhakal', 'Sandeep Aryal', 'Santosh Magar', 'Saurav Shrestha', 'Shashi Rawat', 'Shiva Basnyat', 'Shubham Pokhrel', 'Siddharth Nepal', 'Srijan Poudel', 'Subash Kandel', 'Sudeep Gautam', 'Sujan Khatri', 'Sumit Acharya', 'Sunil Gurung', 'Suraj Bhandari', 'Sushant Lama', 'Ujjwal Thapa', 'Uttam Chaudhary', 'Varun Singh', 'Vikas Bohora', 'Vishal Limbu', 'Yadav Ghimire', 'Yuvraj Rijal', 'Zenith Lama', 'Aadesh Bista', 'Adarsh Subedi', 'Akash Shah', 'Amar Dangol', 'Amrit Ghale', 'Anand Khadka', 'Anish Bhattarai', 'Arnav Oli', 'Ayush Tamrakar', 'Bhuwan Pokharel', 'Binod Magar', 'Bishal Lama', 'Chiran Thakuri', 'Darshan Kafle', 'Deepak Adhikari', 'Devendra Thapa', 'Dipak Aryal', 'Divas Shrestha', 'Gagan Bajracharya', 'Ganesh Regmi', 'Gaurav Shah', 'Gokul Lama', 'Hari Krishna', 'Hemant Bhandari', 'Himal Neupane', 'Ishaan Rajbhandari', 'Jai Rawal', 'Jitendra Rana', 'Kabir Khadka', 'Kavi Gurung', 'Kiran Bista', 'Kishan Pariyar', 'Kshitij Pandey', 'Lokendra Gurung', 'Mahesh Aryal', 'Manav Rijal', 'Manoj Poudel', 'Mihir Shrestha', 'Mukesh Thapa', 'Nabin Thakuri', 'Nandan Bohora', 'Nihal Joshi', 'Nikhil Baniya', 'Nirvan Lama', 'Omkar Tamang', 'Paritosh Chhetri', 'Parvesh Bista', 'Pradip Khatiwada', 'Pranjal Magar', 'Prashant Bhandari', 'Pravin Shrestha', 'Pritam Khatri', 'Rahul Oli', 'Rajendra Dhungana', 'Rajesh Adhikari', 'Rakesh Poudel', 'Raman Lama', 'Ravi Thapa', 'Rishab Bist', 'Ritesh Panta', 'Roshan Basnet', 'Sachin Pandey', 'Sagar Limbu', 'Sahadev Bohara', 'Sameep Chaudhary', 'Samir Sharma', 'Sanam Thapa', 'Sandesh Oli', 'Santanu Bhattarai', 'Saroj Rai', 'Satish Bhandari', 'Shakti Gurung', 'Sharan Thapa', 'Sharad Oli', 'Shashank Magar', 'Shishir Aryal', 'Siddhant Joshi', 'Snehal Bista', 'Suman Bohara', 'Sunil Chhetri', 'Suraj Thakur', 'Sushil Aryal', 'Tashi Lama', 'Tilak Adhikari', 'Utsav Pokhrel', 'Vansh Karki', 'Vidit Bhattarai', 'Vishnu Budha', 'Vivek Tamang', 'Yash Poudel', 'Yuvan Shrestha', 'Aakash Koirala', 'Abishek Bhusal', 'Adarsh Gautam', 'Aditya Magar', 'Akshay Lama', 'Aman Chhetri', 'Amrit Khatiwada', 'Aniket Tamang', 'Anirudh Joshi', 'Anup Bist', 'Arjun Oli', 'Ashutosh Khatri', 'Avinash Gurung', 'Ayush Thakur', 'Babin Bhandari', 'Basant Sharma']

girl = ['Aaradhya Shrestha', 'Aashika Maharjan', 'Aditi Bhandari', 'Aishwarya Gautam', 'Akriti Gurung', 'Alina Basnet', 'Ananya Thapa', 'Anisha Joshi', 'Ankita Regmi', 'Anushka Adhikari', 'Arya Chhetri', 'Ashima Shahi', 'Asmita Rai', 'Ayisha Oli', 'Bhawana Lama', 'Binita Tamang', 'Bishika Khadka', 'Charu Bista', 'Deeksha Pant', 'Diksha Bhusal', 'Eva Rana', 'Gargee Karki', 'Ishani Chapagain', 'Jiya Poudel', 'Kajal Limbu', 'Karishma Bohora', 'Krisha Budhathoki', 'Laxmi Karki', 'Mamata Sapkota', 'Maya Neupane', 'Neha Pandey', 'Nisha Kunwar', 'Pari Lama', 'Pooja Subedi', 'Prisha Limbu', 'Radha Magar', 'Ritika Sunar', 'Sakshi Lama', 'Samriddhi Chaudhary', 'Sara Sharma', 'Shalu Thakur', 'Shikha Baniya', 'Shreya Dhakal', 'Simran Aryal', 'Sneha Thapa', 'Suman Gautam', 'Sunita Khatri', 'Sweta Acharya', 'Trisha Gurung', 'Urmila Thapa', 'Vidhi Singh', 'Yamini Bohora', 'Zara Limbu', 'Aanya Bista', 'Aarohi Subedi', 'Abha Shah', 'Adhya Dangol', 'Akansha Ghale', 'Alka Khatiwada', 'Amara Bhattarai', 'Amisha Oli', 'Ananya Tamang', 'Anita Joshi', 'Aria Oli', 'Ashika Khatri', 'Ava Gurung', 'Avisha Shah', 'Aylin Thakur', 'Bibisha Bhandari', 'Charvi Thapa', 'Daksha Aryal', 'Divya Shrestha', 'Eesha Bista', 'Grishma Magar', 'Ira Bohora', 'Ishita Adhikari', 'Jasmine Koirala', 'Jiya Rai', 'Kaira Poudel', 'Kritika Limbu', 'Lavanya Bohora', 'Mansi Aryal', 'Mira Rijal', 'Nandini Poudel', 'Neha Thakuri', 'Nisha Rai', 'Ojaswi Lama', 'Pihu Sharma', 'Prakriti Oli', 'Rashmi Thapa', 'Ritisha Basnyat', 'Sadhana Sharma', 'Salina Chaudhary', 'Sanya Magar', 'Shaina Oli', 'Shreeya Bhattarai', 'Siya Limbu', 'Suhani Bohora', 'Tanvi Shah', 'Trisha Lama', 'Udita Thapa', 'Vaishali Chhetri', 'Varsha Sharma', 'Yukta Limbu', 'Zoya Baniya', 'Anvi Koirala', 'Aarvi Bhusal', 'Adrika Gautam', 'Aisha Magar', 'Akriti Chhetri', 'Amisha Shah', 'Anaya Gurung', 'Anika Regmi', 'Anusha Shahi', 'Aria Rai', 'Avni Oli', 'Diya Thapa', 'Eva Basnet', 'Ishana Chaudhary', 'Jiya Kafle', 'Kashvi Panta', 'Kiara Shrestha', 'Liza Karki', 'Mahika Aryal', 'Myra Bista', 'Nandita Thakuri', 'Neha Adhikari', 'Pari Poudel', 'Pranjal Sharma', 'Reeva Thapa', 'Rhea Oli', 'Riya Lama', 'Samaira Bohora', 'Samridhi Pariyar', 'Shruti Dhakal', 'Simi Aryal', 'Sneha Magar', 'Suhana Limbu', 'Tara Thapa', 'Trisha Bhandari', 'Vanya Gurung', 'Vidisha Limbu', 'Yamika Bhattarai', 'Zara Sharma', 'Aanya Koirala', 'Aditi Bhusal', 'Aishani Gautam', 'Akshita Magar', 'Anvi Chhetri', 'Aradhya Shah', 'Arya Magar', 'Ashmi Lama', 'Ayushi Tamang', 'Bhavika Poudel', 'Divisha Shrestha', 'Eshika Bhattarai', 'Ishika Khatri', 'Ishwari Bohora', 'Kritisha Joshi', 'Nishika Baniya', 'Pranvi Oli', 'Ridhi Panta', 'Roma Thapa', 'Sadhika Magar', 'Sanvi Bhandari', 'Sara Kafle', 'Siya Aryal', 'Sneha Lama', 'Suhani Thakur', 'Swara Shrestha', 'Tanishka Chaudhary', 'Trishna Bhattarai', 'Vaishnavi Limbu', 'Vanya Sharma', 'Yukti Bista', 'Ziva Thakuri']

ok = []
cp = []
def menu():
    os.system('clear')
    print(banner)
    print('Start to generate new accounts?')
    print(42 * '═')
    sel = input('(Type "y" to proceed & Type "n" to get back) ')

    if sel in ['y', 'yes', 'Yes', 'Y']:
        create().start()
    elif sel in ['n', 'No', 'no', 'N']:
        print('Exit')
        os.system('clear')
        print(banner)
    else:
        print('Invalid choice, so getting back to the menu')
        time.sleep(3)
        menu()


class create:

    def __init__(self):
        self.loop = 0
        self.gender = []

    def start(self):
        os.system('clear')
        print (banner)
        print ('[1] Boys Accounts')
        print ('[2] Girls Accounts')
        print (38*'═')
        gen = input('Choose: ')
        print (38*'═')
        if gen in ['1', '01']:
            self.gender.append('boy')
        elif gen in ['2', '02']:
            self.gender.append('girl')
        else:
            self.gender.append('boy')
        print ('Example: 1000, 2000, 5000, 10000')
        print (38*'═')
        lim = int(input('Choose Quantity: '))
        os.system('clear')
        print (banner)
        agent = random.choice(ugen)
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en;q=0.9,si-LK;q=0.8,si;q=0.7,en-US;q=0.6',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="118"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Chromium";v="118.0.5993.118","Google Chrome";v="118.0.5993.118"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 
            'Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)',
          'viewport-width': '1365',}
        headers1 = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en;q=0.9,si-LK;q=0.8,si;q=0.7,en-US;q=0.6',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Chromium";v="118"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Chromium";v="118.0.5993.118","Google Chrome";v="118.0.5993.118"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        }
        print(' [•] Use aeroplane mode if no result. ')
        print (38*'═')
        OO = '\033[0;37m'
        for x in range(lim):
            self.loop += 1
            sys.stdout.write(f'\r {OO}[BISHESH-CREATING] {OO}{self.loop}/{str(lim)} | ALIVE: {len(ok)} | CHECKPOINT: {len(cp)}{OO} '),
            sys.stdout.flush()
            if 'boy' in self.gender:
                name = random.choice(boy).split(' ')
                sex = '2'
            elif 'girl' in self.gender:
                name = random.choice(girl).split(' ')
                sex = '1'
            try:
                ses = requests.Session()
                buildses = user = "".join(random.SystemRandom().choice("qwertyuiopasdfghjklzxcvbnm0987654321") for i in range(26))
                create = ses.get(f"https://10minutemail.net/address.api.php?new=1&sessionid={buildses}&_={int(datetime.now().timestamp() * 1000)}").json()
                mail = {"mail": create["permalink"]["mail"], "session": create["session_id"]}
                email = mail['mail']
                session = mail['session']
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
            passw = name[0]+name[1]+str(123)
            try:
                self.ses = requests.Session()
                a = self.ses.get('https://m.facebook.com/reg?_fb_noscript', headers=headers)
                loger = re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1)
                ref = BeautifulSoup(a.text, 'html.parser').find('form', {'action': True, "id":"mobile-reg-form", "method":"post"})
                bl = ['lsd', 'jazoest', 'cpp', 'reg_instance', 'submission_request']
                bz = ['reg_impression_id', 'ns']
                self.data = {}
                for v in ref('input'):
                    if v.get('name') in bl:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({'helper': ''})
                for v in ref('input'):
                    if v.get('name') in bz:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({
                    "zero_header_af_client": "",
                    "app_id": "103",
                    "logger_id": re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1),
                    "field_names[0]": "firstname",
                    "firstname": name[0],
                    "lastname": name[1],
                    "field_names[1]": "birthday_wrapper",
                    "birthday_day": str(random.randint(1,28)),
                    "birthday_month": str(random.randint(1,12)),
                    "birthday_year": str(random.randint(1992,2004)),
                    "age_step_input": "",
                    "did_use_age": "",
                    "field_names[2]": "reg_email__",
                    "reg_email__": email,
                    "field_names[3]": "sex",
                    "sex": sex,
                    "preferred_pronoun": "",
                    "custom_gender": "",
                    "field_names[]": "reg_passwd__",
                    "reg_passwd__": passw,
                    "submit": "Sign Up",
                    "name_suggest_elig": "false",
                    "was_shown_name_suggestions": "false",
                    "did_use_suggested_name": "false",
                    "use_custom_gender": "",
                    "guid": "",
                    "pre_form_step": "",
                })
                gett = self.ses.post('https://m.facebook.com'+ref['action'], headers=headers1, data=self.data)
                getts = self.ses.get('https://m.facebook.com/login/save-device/?login_source=account_creation&logger_id='+loger+'&app_id=103', headers=headers1)
                data1 = {}
                data2 = {}
                data3 = {}
                cok = self.ses.cookies.get_dict()
                if 'checkpoint' in getts.url:
                    cp.append(email+passw)
                    print ('\r\033[1;96m [CHECKPOINT] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                dbl = ['fb_dtsg', 'jazoest', 'flow', 'next', 'nux_source']
                for x in BeautifulSoup(getts.text, 'html.parser').find_all('form', {'method': 'post'}):
                    if '/login/device-based/update-nonce/' in str(x):
                        for v in x('input'):
                            if v.get('name') in dbl:
                                try:
                                    data1.update({v.get('name'):v.get('value')})
                                except:
                                    pass
                        data1.update({'submit': 'OK'})
                        po = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data1)
                        for x in BeautifulSoup(po.text, 'html.parser').find_all('form', {'method': 'post'}):
                            if 'confirmation_event_location=cliff' in str(x):
                                for v in x('input'):
                                    if v.get('name') in dbl:
                                        try:
                                            data2.update({v.get('name'):v.get('value')})
                                        except:
                                            pass
                                code = inbox(session)
                                data2.update({'c': code, 'submit': 'Confirm'})
                                rex = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data2)
                                if 'checkpoint' in rex.url:
                                    cok = self.ses.cookies.get_dict()
                                    cp.append(email+passw)
                                    print ('\r\033[1;96m [CHECKPOINT] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                                else:
                                    coki = (";").join([ "%s=%s" % (key, value) for key, value in self.ses.cookies.get_dict().items() ])
                                    cok = self.ses.cookies.get_dict()
                                    print ('\r\033[1;34m [BISHESH-ALIVE] '+cok['c_user']+' | '+passw+' | '+coki+'\033[0;97m     ')
                                    ok.append(email+passw)
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
        print ('process has been completed')
        print (38*'═')
        print ('\033[1;94mTotal ids > ALIVE/' +str(len(ok)) + ' CHECKPOINT/' + str(len(cp)))
        print (38*'═')
        input('back')
        menu()
menu()
