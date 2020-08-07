# a = ["1",1,"2", 2]
# new_dict = {x:1 for x in a}
# print(new_dict)
#
# # create nested dict
#
# a = {"a":[{"b":1}]}
# print(a)

from datetime import date, timedelta,datetime

today = datetime.now()
today += timedelta(days=10, hours=14)
print("Today's date:", today)