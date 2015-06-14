import requests
from bs4 import BeautifulSoup
from pprint import pprint
from histogram import Histogram
import json


class Crawler:

    def __init__(self, url):
        self.url = url
        self.internal_links = []
        self.external_links = []
        self.visited = []

    def start(self):
        links = self.get_links_from_url(self.url)
        self.classify(links)
        self.visited.append(self.url)

        for link in self.internal_links:
            if link not in self.visited:
                print(link)
                self.visited.append(link)
                sub_pages = self.get_links_from_url(link)
                self.classify(sub_pages)

    def get_links_from_url(self, url):
        try:
            r = requests.get(url, timeout=3)
            soup = BeautifulSoup(r.text)

            links = set()
            for link in soup.find_all('a'):
                links.add(link.get('href'))
            return links
        except:
            return 'Invalid input'

    # proverqvame koi linkove sa vunshni za saita i koi vutreshni
    def classify(self, links):
        for link in links:
            if link is None:
                continue
            elif 'start.bg' in link:
                self.internal_links.append(link)
            elif 'link.php?' in link:
                self.external_links.append(link)

        print(self.internal_links)
        print(self.external_links)

    def headers(links):
        server_headers = []

        for link in links:
            try:
                response = requests.head(link, timeout=3, allow_redirects=True)
                server_headers.append(response.headers['server'])
                print(response.headers['server'])
            except:
                print("Not a valid URL!")
        return server_headers

    def server_names_histogram(server_headers):
        searched_names = ["Apache", "Microsoft-IIS", "nginx", "lighttpd"]
        server_histogram = Histogram()

        for server_header in server_headers:
            for searched_name in searched_names:
                if searched_name in server_header:
                    server_histogram.add(searched_name)
        return server_histogram

    def save_results(filename, names):
        with open(filename, 'w') as f:
            json.dump(names, f)

    def load_results(filename):
        with open(filename, "r") as f:
            info = json.loads(f.read())
        return info


def main():
    crawler = Crawler('http://www.start.bg/')
    crawler.start()
    links = (crawler.get_links_from_url('http://www.start.bg/'))
    pprint(crawler.classify(links))
    header = Crawler.headers(links)
    save = Crawler.save_results('data.json', header)

    load = Crawler.load_results('data.json')
    histogram = Crawler.server_names_histogram(load)
    server_histogram = Crawler.save_results(
        'servers_by_groups.json', histogram.dict_histogram)


if __name__ == '__main__':
    main()
