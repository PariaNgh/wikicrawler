import numpy as np
import copy
import multiprocessing
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from postgres import insert_func

def crawl(parent_urls, visited_urls):
    queue = copy.deepcopy(parent_urls)
    for parent_url in parent_urls:
        parsed_url = urlparse(parent_url)
        base_url = parsed_url.scheme + "://" + parsed_url.netloc
        response = requests.get(parent_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        if parent_url in visited_urls:
            continue
        visited_urls.append(parent_url)

        for link in soup.find_all('a'):
            href = link.get('href')
            if href is not None:
                if not href.startswith('https:'):
                    if not href.endswith('.org/') or href.endswith('.com/'):
                        child_url = base_url + href
                        queue.append(child_url)
                        print(parent_url, child_url)
                    else:
                        child_url = 'https:' + href
                        queue.append(child_url)
                        print(parent_url, child_url)

                else:
                    child_url = href
                    queue.append(child_url)
                insert_func(parent_url, child_url)

        queue.pop(0)
    if len(visited_urls) < 2000:
        return crawl(queue, visited_urls)




