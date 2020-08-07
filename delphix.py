# import json, requests, pprint
#
# url = 'http://maps.googleapis.com/maps/api/directions/json?'
#
# params = dict(
#     origin='Chicago,IL',
#     destination='Los+Angeles,CA',
#     waypoints='Joplin,MO|Oklahoma+City,OK',
#     sensor='false'
# )
#
#
# data = requests.get(url=url, params=params)
# binary = data.content
# output = json.loads(binary)
#
# # test to see if the request was valid
# #print output['status']
#
# # output all of the results
# #pprint.pprint(output)
#
# # step-by-step directions
# for route in output['routes']:
#         for leg in route['legs']:
#             for step in leg['steps']:
#                 print step['html_instructions']

import math
import requests


class Request:

    def __init__(self,
                 orig: str,
                 url: str = "https://api.bart.gov/api/etd.aspx?",
                 key: str = "MW9S-E7SL-26DU-VV8V",
                 json: str = "y",
                 cmd: str = "etd"):
        self.params = dict(
                        orig=orig,
                        key=key,
                        json=json,
                        cmd=cmd)
        self.url = url
        res = requests.get(url=self.url, params=self.params)
        res.encoding = "utf-8"
        self.res = res.json()
        print(self.res)

    def get_time(self):
        return self.res["root"]["date"]

    def get_station(self):
        return self.res["root"]["station"]


    def create_dict(self):
        ret = self.get_station()
        station_dict = {}
        for destination_details in ret[0]["etd"]:
            station_dict[destination_details["destination"]] = []
            for time in destination_details["estimate"]:
                station_dict[destination_details["destination"]].append(time["minutes"])

        return station_dict

    def sort_dict(self):
        new_dict = self.create_dict()
        dict_keys = list(new_dict)
        while True:
            # Breaking while loop if there are no keys left
            if len(dict_keys) == 0:
                break
            # Setting min_value to infinity
            min_value = math.inf
            # For loop for iterating over dict keys
            for key in dict_keys:
                new_dict[key][0] = 0 if new_dict[key][0] == "Leaving" else "Useless expression"
                if int(new_dict[key][0]) < min_value:
                    min_value, temp = int(new_dict[key][0]), key
            new_dict[temp].pop(0)
            dict_keys.remove(temp) if len(new_dict[temp]) == 0 else "Useless expression"
            print(temp, min_value )

obj = Request(orig="mont")
print(obj.get_station())
print(obj.sort_dict())
