from django.http import HttpResponse
import json
from itertools import chain
from collections import defaultdict

from elders.MongoDBManagerAlarm import MongoDBManager as MongoDBManagerAlarm
from elders.MongoDBManager import MongoDBManager


def all_users(request):
    def get():
        dbAlarmData = MongoDBManagerAlarm().get_users_from_collection({})
        responseData = []
        for user in dbAlarmData:
            del user["_id"]
            if user["name"] == "HwaGok-dong":
                user["name"] = "김옥순"
            elif user["name"] == "NoWon-Gu":
                user["name"] = "손영섭"
            elif user["name"] == "GangDong-Gu":
                user["name"] = "김주필"
            elif user["name"] == "JungNang-Gu":
                user["name"] = "권오갑"
            elif user["name"] == "DoBong-Gu":
                user["name"] = "김주필"

            for x in MongoDBManager().get_users_from_collection({"name": user["name"]}):
                user["gender"] = x["gender"]
                user["age"] = x["age"]
                user["address"] = x["address"]
                user["phonenumber"] = x["phone number"]
                user["medicalrecords"] = x["medical records"]
                user["protector'sname"] = x["protector's name"]
                user["protector'sphonenumber"] = x["protector's phone number"]
                user["manager"] = x["manager"]

            responseData.append(user)

        print(type(responseData))

        return HttpResponse(json.dumps(responseData), status=200)

    if request.method == "GET":
        return get()
    else:
        return HttpResponse(status=405)
