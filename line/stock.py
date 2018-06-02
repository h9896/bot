from bs4 import BeautifulSoup
import requests

class stocks(object):
    def __init__(self, stock_id):
        self.stock_id = stock_id
    def search(self):
        url = "https://tw.stock.yahoo.com/q/q?s={0}".format(self.stock_id)
        resp = requests.get(url)
        con = resp.text
        soup = BeautifulSoup(con)
        body = soup.find_all('table', {'border': '2'})
        if  not body:
            return [], []
        for i in body:
            col = i.find_all('th')
            col_str = []
            for j in col:
                if j.string:
                    col_str.append(j.string)
            val = i.find_all('td')
            val_str = []
            for j in val:
                if j.string:
                    if '\n' in j.string:
                        j.string = j.string.split('\n')[0]
                    val_str.append(j.string)
        return col_str, val_str
if __name__ == '__main__':
   p = stocks("8924").search()
   print(p)
