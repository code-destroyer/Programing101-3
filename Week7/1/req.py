import requests
from bs4 import BeautifulSoup
import json
from histogram import Histogram


class Links:

    def get_links():
        links = []

        response = requests.get("http://register.start.bg/")
        soup = BeautifulSoup(response.text)

        for link in soup.find_all('a'):
            if link.get('href') is not None and "link.php" in link.get('href'):
                    links.append("http://register.start.bg/" + link.get('href'))
        return links

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


link = Links.get_links()
header = Links.headers(link)
save = Links.save_results('data.json', header)

load = Links.load_results('data.json')
histogram = Links.server_names_histogram(load)
server_histogram = Links.save_results('servers_by_groups.json', histogram.dict_histogram)
