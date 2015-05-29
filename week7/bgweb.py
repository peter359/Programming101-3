import requests
import bs4


class Histogram:
    def __init__(self):
        self.histogram = {}

    def __len__(self):
        return sum([1 for key in self.histogram])

    def __getitem__(self, index):
        return self.histogram[index]

    def add(self, key):
        if key in self.histogram:
            self.histogram[key] += 1
        else:
            self.histogram[key] = 1

    def count(self, key):
        if key in self.histogram:
            return self.histogram[key]

    def items(self):
        return [(key, self.histogram[key]) for key in self.histogram]

    def get_dict(self):
        return {key: self.histogram[key] for key in self.histogram}


def main():
    h = Histogram()
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    r = requests.get("http://register.start.bg/", headers=headers)
    b = bs4.BeautifulSoup(r.text)
    links = [l.get('href') for l in b.find_all('a') if l.get('href') is not None]
    links = [l for l in links if "link.php" in l]
    for l in links[30:40]:
        p = requests.head("http://register.start.bg/" + l, headers=headers, allow_redirects=True, timeout=10.000)
        if 'server' in p.headers:
            h.add(p.headers['server'])
    print(h)

if __name__ == '__main__':
    main()
