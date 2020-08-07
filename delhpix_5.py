""" This is sample test scenario to test departure trains """
from json.decoder import JSONDecodeError
import math

import requests


class Request:
    """ This class is responsible for calling rest API's using request module """

    def __init__(self, url: str):
        """ This __init__ function is setting the URL """
        self.url = url

    def get_request(self, params: dict, extend_url: str):
        """
        This method is used to send a get request to the request module
        :param params: its a dictionary with needed parameters
        :param extend_url: Actual page to load
        :return: Response or False
        """
        url = self.url + extend_url
        response = requests.get(url=url, params=params)
        if response.ok:
            try:
                return response.json()
            except JSONDecodeError:
                return response.text
        else:
            return False


class BartAPI(Request):
    """
    This class is specific for calling Bart API's
    Currently this supports only etd function of rest API
    Any other API can be build over it with minimal effort
    """

    def __init__(self,
                 url: str = "https://api.bart.gov/",
                 key: str = "MW9S-E7SL-26DU-VV8V",
                 json: str = "y",
                 cmd: str = "etd"):
        """
        Constructor of the class
        :param url: URL on which REST api will be sent
        :param key: Key to validate request
        :param json: Whether we need json response or not
        :param cmd: etd
        """
        self.params = dict(
            key=key,
            json=json,
            cmd=cmd)
        Request.__init__(self, url)

    def get_train_estimates(self, orig: str):
        """
        Method to get train estimates
        :param orig: Origin station
        :return: Response in JSON format
        """
        self.params["orig"] = orig
        extend_url = "api/etd.aspx?"

        return self.get_request(params=self.params, extend_url=extend_url)


class TestCase(BartAPI):
    """ This is actual test case class where I am sorting the destination stations based on timings """

    def __init__(self,
                 url: str = "https://api.bart.gov/",
                 key: str = "MW9S-E7SL-26DU-VV8V",
                 json: str = "y",
                 cmd: str = "etd"):
        """
        Constructor for class
        :param url: URL
        :param key: Key to validate request
        :param json: Whether response is needed in JSON or not.
        :param cmd: etd
        """
        # Calling BartAPI constructor
        BartAPI.__init__(self, url, key, json, cmd)

    @staticmethod
    def _create_dict(staion_json: dict):
        station_dict: dict = {}
        for destination_details in staion_json:
            station_dict[destination_details["destination"]] = []
            for time in destination_details["estimate"]:
                station_dict[destination_details["destination"]].append(time["minutes"])
        return station_dict

    def _sort_station_time(self, station_json: dict):
        """
        This is the main method to get the sorted list
        This uses algorithm where I am matching with first index of each dict key then
        pop that particular element from key value
        :param: station_json: Station details in json format
        :return: It returns station_list in the form of city_minutes which is sorted
        """

        # Creating a dict of all the departure station with station name as key and timing list as values
        station_dict = self._create_dict(station_json)
        # This is a function to sort the dictionary based on 0th index and return a list
        def _sort_dict(a):

            dict_keys = list(a)
            new_lis = []
            count = 0
            while True:
                # Breaking while loop if there are no keys left or sorted count reached to 10
                if len(dict_keys) == 0 or count == 10:
                    break
                # Setting min_value to infinity
                min_value = math.inf
                # For loop for iterating over dict keys
                for key in dict_keys:
                    if a[key][0] == "Leaving":
                        a[key][0] = 0
                    if int(a[key][0]) < min_value:
                        min_value, temp = int(a[key][0]), key
                # Removing element that code is going to append in list
                a[temp].pop(0)
                if len(a[temp]) == 0:
                    # Removing the dict key if it has no values left
                    dict_keys.remove(temp)
                new_lis.append(f"{temp}_{min_value}")
                count += 1
            return new_lis
        # Returning the actual sorted list of stations merged with minutes with seperator _
        #
        # Sample list returned is
        # ['SF Airport_10', 'Warm Springs_12', 'Richmond_13', 'Antioch_14', 'SF Airport_35',
        # 'Warm Springs_36', 'Richmond_37', 'Antioch_38', 'SFO/Millbrae_58', 'Warm Springs_60']
        return _sort_dict(station_dict)

    @staticmethod
    def _print_header(station_name: str, time: str):
        """ Method to print origin station name and current time """
        print("----------------------------------")
        print(station_name, time)
        print("----------------------------------")

    @staticmethod
    def _print_stations(station_list: list):
        """
        Method to print all the stations list sorted with timing of their departure trains
        :param: station_list: List with station names and station timing
        """
        for i in station_list:
            time = i.split("_")[1]
            if int(time) == 0:
                time = "Leaving"
            print('%19.20s  |  %1.20s' % (i.split("_")[0], time))

    def get_departure_details(self, orig: str):
        """
        Main method which user will be exposed to user
        :param: orig: Origin station
        """
        response = self.get_train_estimates(orig=orig)
        if "missing or invalid" not in response:
            time = response["root"]["time"]
            station_name = response["root"]["station"][0]["name"]
            self._print_header(station_name, time)
            print(response["root"])
            if "messages" in response["root"] and\
                    "warning" in response["root"]["message"] and\
                    "No data matched your criteria" in response["root"]["message"]["warning"]:
                print("No Trains available")
            else:
                try:
                    station_dict = response["root"]["station"][0]["etd"]
                    sorted_station_list = self._sort_station_time(station_dict)
                    self._print_stations(sorted_station_list)
                except KeyError:
                    print("Expected keys are missing")
                    raise KeyError
        elif "missing or invalid" in response:
            print("Please enter valid origin station value")
        else:
            print("Unable to process request", response.text)


obj = TestCase()
obj.get_departure_details(orig="mont")
