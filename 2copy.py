#working but api is not able to fetch proxy 
import requests
import random

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4505.0 Safari/537.36',
]

def get_free_proxies():
    url = 'https://public.freeproxyapi.com/api/Proxy/Large?country=US'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        proxies = [f"{proxy['ip']}:{proxy['port']}" for proxy in data]
        return proxies
    else:
        print(f"Failed to fetch proxies. Status code: {response.status_code}")
        return []

def increase_link_click(url, num_clicks):
    proxies = get_free_proxies()

    if not proxies:
        print("No proxies available. Unable to proceed.")
        return

    for _ in range(num_clicks):
        headers = {
            'User-Agent': random.choice(USER_AGENTS)
        }

        try:
            proxy = random.choice(proxies)

            proxy_dict = {
                'http': f'http://{proxy}',
                'https': f'http://{proxy}'
            }

            response = requests.get(url, headers=headers, proxies=proxy_dict)
            if response.status_code == 200:
                print('Link clicked successfully.')
            else:
                print(f'Failed to click the link. Status code: {response.status_code}')
        except Exception as e:
            print(f'Error: {str(e)}')


link = 'https://modernageinventions.blogspot.com/2022/07/laser-light.html'  # Replace with the target URL
click_count = 10  # Replace with the desired number of clicks

increase_link_click(link, click_count)

