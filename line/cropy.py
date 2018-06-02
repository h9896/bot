import requests

class price(object):
    def __init__(self, s1, s2 = "USD"):
        self.s1 = s1
        self.s2 = s2
    def last_price(self):
        url="https://cex.io/api/last_price/{0}/{1}".format(self.s1,self.s2)
        resp = requests.get(url)
        if resp.ok:
            #json_data = json.loads(resp.text)
            json_data = resp.text.split(",")[0].split(":")[1].replace('"',"")
            return json_data
        else:
            return "Error"

if __name__ == '__main__':
    lis = ["BTC", "ETH", "ZEC", "XRP"]
    while True:
        crypto = input("Crypto Currency: ").upper()
        if crypto not in lis:
            print("Sorry this crypto currency is not in service!")
            print("Please type again!")
        else:
            p = price(crypto).last_price()
            print("{0}/USD: {1}".format(crypto, p))