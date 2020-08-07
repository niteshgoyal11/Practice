import requests
from json.decoder import JSONDecodeError
import math


class Request:

    def __init__(self, url: str):
        self.url = url

    def get_request(self, params: dict, extend_url: str):
        url = self.url + extend_url
        response = requests.get(url=url, params=params)
        if response.ok:
            try:
                return response.json()
            except JSONDecodeError:
                print("Getting Json Decodedr error")
                return False


class BartAPI(Request):

    def __init__(self,
                 url: str = "https://api.bart.gov/",
                 key: str = "MW9S-E7SL-26DU-VV8V",
                 json: str = "y",
                 cmd: str = "etd"):
        self.params = dict(
            key=key,
            json=json,
            cmd=cmd)
        Request.__init__(self, url)

    def get_train_estimates(self,
                            orig: str,
                            extend_url: str = "api/etd.aspx?"):
        self.params["orig"] = orig
        return self.get_request(params=self.params, extend_url=extend_url)


class TestCase(BartAPI):

    def __init__(self,
                 orig: str,
                 url: str = "https://api.bart.gov/",
                 key: str = "MW9S-E7SL-26DU-VV8V",
                 json: str = "y",
                 cmd: str = "etd"):
        BartAPI.__init__(self, url, key,json,cmd)
        self.response = self.get_train_estimates(orig=orig)
        if self.response:
            self.date = self.response["root"]["date"]
            self.station_name = self.response["root"]["station"][0]["name"]

    def print_header(self):
        if self.response:
            print("------------------------------")
            print(self.station_name, self.date)
            print("------------------------------")

    def _create_dict(self):
        ret = self.response["root"]["station"][0]["etd"]
        station_dict = {}
        for destination_details in ret:
            station_dict[destination_details["destination"]] = []
            for time in destination_details["estimate"]:
                station_dict[destination_details["destination"]].append(time["minutes"])
        return station_dict

    def sort_dict(self):
        new_dict = self._create_dict()
        dict_keys = list(new_dict)
        while True:
            # Breaking while loop if there are no keys left
            if len(dict_keys) == 0:
                break
            # Setting min_value to infinity
            min_value = math.inf
            # For loop for iterating over dict keys
            for key in dict_keys:
                if new_dict[key][0] == "Leaving":
                    new_dict[key][0] = 0
                if int(new_dict[key][0]) < min_value:
                    min_value, temp = int(new_dict[key][0]), key
            new_dict[temp].pop(0)
            dict_keys.remove(temp) if len(new_dict[temp]) == 0 else "Useless expression"
            print(temp, min_value )


obj = TestCase(orig="mont")
print(obj.print_header())
obj.sort_dict()