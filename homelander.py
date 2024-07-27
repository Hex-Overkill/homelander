#!/usr/bin/python3
# coding: utf-8
# HOMELANDER v1.0
# By CYBERHUB - youtube/cyberhubacademy
import socket
import requests
from bs4 import BeautifulSoup
import socket
import dns.resolver
# ANSI escape codes for colors
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    BACK_BLACK = "\033[40m"
    BACK_RED = "\033[41m"
    BACK_GREEN = "\033[42m"
    BACK_YELLOW = "\033[43m"
    BACK_BLUE = "\033[44m"
    BACK_MAGENTA = "\033[45m"
    BACK_CYAN = "\033[46m"
    BACK_WHITE = "\033[47m"

def print_colored_text():
    
    print(f"{Colors.GREEN}This is green text{Colors.RESET}")
    print(f"{Colors.BLUE}This is blue text{Colors.RESET}")
    print(f"{Colors.YELLOW}This is yellow text{Colors.RESET}")
    print(f"{Colors.MAGENTA}This is magenta text{Colors.RESET}")
    print(f"{Colors.CYAN}This is cyan text{Colors.RESET}")
    print(f"{Colors.WHITE}This is white text{Colors.RESET}")
    
    print(f"{Colors.BACK_RED}{Colors.BLACK}This is text with a red background and black text{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.GREEN}This is bold green text{Colors.RESET}")
    print(f"{Colors.UNDERLINE}{Colors.BLUE}This is underlined blue text{Colors.RESET}")

print(f"{Colors.RED}{Colors.RESET}")
print(f"{Colors.RED}_   _  ___  __  __ _____ _        _    _   _ ____  _____ ____   {Colors.RESET}")
print(f"{Colors.RED}| | | |/ _ \|  \/  | ____| |      / \  | \ | |  _ \| ____|  _ \  {Colors.RESET}")
print(f"{Colors.RED}| |_| | | | | |\/| |  _| | |     / _ \ |  \| | | | |  _| | |_) | {Colors.RESET}")
print(f"{Colors.RED}|  _  | |_| | |  | | |___| |___ / ___ \| |\  | |_| | |___|  _ <{Colors.RESET}")
print(f"{Colors.RED}|_| |_|\___/|_|  |_|_____|_____/_/   \_\_| \_|____/|_____|_| \_\ {Colors.RESET}")
print('')
print(f"{Colors.YELLOW}MADE BY TEAM CYBERHUB SL - PROFESSOR & HEX_OVERKIILL{Colors.RESET}")

print('')
website = input(f"{Colors.BOLD}{Colors.GREEN}KINDLY INPUT THE DOMAIN :\n{Colors.RESET}")
def get_website_info(url):
    try:
        
        response = requests.get(url)
        if response.status_code == 200:
            print(f"URL: {url}")
            print(f"Status: {response.status_code}")
            print('')
            
            print("SERVER HEADERS")
            print('--------------')
            print('')
            for header, value in response.headers.items():
                print(f"{header}: {value}")
            print('')
            
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string if soup.title else 'No title found'
            print('')
            print('TITLE')
            print('------')
            print('')
            print( title)
            print('')
            print('IPV4 ADDRESS')
            print('------------')
           
            domain = url.split("//")[-1].split("/")[0]
            ip = socket.gethostbyname(domain)
            print(f"IP Address: {ip}")
            print('')
           
           
            dns_info = dns.resolver.resolve(domain, 'MX')
            print("DNS INFORMATION:")
            print('---------------')
            for data in dns_info:
                print(f"Mail Exchange Host: {data.exchange}")
             

        else:
            print(f"Failed to retrieve URL: {url}, Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    website_url = ('https://' + website)
    get_website_info(website_url)
    

def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        return response
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None


def extract_website_info(url):
    response = get_page_content(url)
    if response is None:
        return

   
    headers = response.headers

    
    soup = BeautifulSoup(response.text, 'html.parser')

    
    title = soup.title.string if soup.title else 'No title found'

    
    meta_description_tag = soup.find('meta', attrs={'name': 'description'})
    meta_description = meta_description_tag['content'] if meta_description_tag else 'No meta description found'

    
    links = [a.get('href') for a in soup.find_all('a', href=True)]

   
    print('')
    print('LINKS')
    print('-----')
    print(f"Meta Description: {meta_description}")
    print(f"Links found: {len(links)}")
    for link in links:

        print(f"  {link}")
        


if __name__ == "__main__":
    websiteurl = website_url  
    extract_website_info(websiteurl)
    print('')
    print('OPEN PORTS')
    print('----------')
def port_scanner(target_host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
          
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           
            sock.settimeout(1)
          
            result = sock.connect_ex((target_host, port))
            if result == 0:
                
                service = socket.getservbyport(port)
                print(f"Port {port} ({service}): Open")
            # Close the socket
            sock.close()
        except socket.error:
            pass  


if __name__ == "__main__":
    target = (website)
    start = int(1)
    end = int(6535)
    port_scanner(target, start, end)




