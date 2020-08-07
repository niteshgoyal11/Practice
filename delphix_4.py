""" This is sample test scenario to test departure trains """
from json.decoder import JSONDecodeError

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
    def _create_list(staion_json: dict):
        station_list = []
        for destination_details in staion_json:
            city_name = destination_details["destination"]
            for time in destination_details["estimate"]:
                if time['minutes'] == "Leaving":
                    time['minutes'] = 0
                station_list.append(f"{city_name}_{time['minutes']}")
        return station_list

    def _sort_station_time(self, station_json: dict):
        """
        This is the main method to get the sorted list
        This uses merge sort algorithm to get the time complexity O(nlogn)
        This also uses nested function _mergeSort which is the main function for
        merge sort operation
        :param: station_json: Station details in json format
        :return: It returns station_list in the form of city_minutes which is sorted
        """

        # Creating a list of all the departure station with timing in format as stationName_minutes
        station_list = self._create_list(station_json)

        def _merge_sort(a):
            if len(a) > 1:
                mid = len(a) // 2
                L = a[:mid]
                R = a[mid:]
                _merge_sort(L)
                _merge_sort(R)

                i = j = k = 0
                while i < len(L) and j < len(R):
                    if int(L[i].split("_")[1]) == int(R[j].split("_")[1]):
                        if L[i].split("_")[0] < R[j].split("_")[0]:
                            a[k] = L[i]
                            i += 1
                        else:
                            a[k] = L[j]
                            j += 1
                    elif int(L[i].split("_")[1]) < int(R[j].split("_")[1]):
                        a[k] = L[i]
                        i += 1
                    else:
                        a[k] = R[j]
                        j += 1
                    k += 1
                while i < len(L):
                    a[k] = L[i]
                    i += 1
                    k += 1

                while j < len(R):
                    a[k] = R[j]
                    j += 1
                    k += 1

        _merge_sort(station_list)
        # Returning the actual sorted list of stations merged with minutes with seperator _
        #
        # Sample list returned is
        # ['SF Airport_1', 'Antioch_3', 'Dublin/Pleasanton_5', 'Daly City_20', 'SF Airport_23', 'Antioch_24',
        # 'Dublin/Pleasanton_27', 'Daly City_44', 'SFO/Millbrae_47', 'Antioch_48', 'Dublin/Pleasanton_51']
        return station_list

    @staticmethod
    def _print_header(station_name: str, time: str):
        """ Method to print origin station name and current time """
        print("----------------------------------")
        print(station_name, time)
        print("----------------------------------")

    @staticmethod
    def _print_stations(station_list: list):
        """ Method to print all the stations list sorted with timing of their departure trains"""
        # This count variable restricts the destination station print to 10
        count = 0
        for i in station_list:
            time = i.split("_")[1]
            if int(time) == 0:
                time = "Leaving"
            print('%19.20s  |  %1.20s' % (i.split("_")[0], time))
            count += 1
            if count == 10:
                break

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
            if "message" in response["root"]:
                print("No Trains available")
            else:
                station_dict = response["root"]["station"][0]["etd"]
                sorted_station_list = self._sort_station_time(station_dict)
                self._print_stations(sorted_station_list)
        elif "missing or invalid" in response:
            print("Please enter valid origin station value")
        else:
            print("Unable to process request", response.text)


obj = TestCase()
obj.get_departure_details(orig="mont")
