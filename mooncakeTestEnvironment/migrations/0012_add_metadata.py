# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json

JSON_PATH = "./mooncakeTestEnvironment/static/mooncakeTestEnvironment/json/"

def addDataToTable(apps, schema_editor):
    Meta_data = apps.get_model("mooncakeTestEnvironment", "Meta_data")
    Service = apps.get_model("mooncakeTestEnvironment", "Service")

    services = Service.objects.all()
    for service in services:
        metaJson = readFileToString(JSON_PATH+"metaJson/"+service.service_id+".json")
        meta = json.loads(metaJson)
        metaData = Meta_data(service=service, metat_keywords=meta["metat_keywords"], meta_description=meta["meta_description"])
        metaData.save()
        

def readFileToString(fileName):
    file = open(fileName, "r")
    lines = file.readlines()
    file.close()
    result = ""
    for line in lines:
        result += line
    return result

class Migration(migrations.Migration):

    dependencies = [
        ('mooncakeTestEnvironment', '0011_auto_20150917_1144'),
    ]

    operations = [
        migrations.RunPython(addDataToTable),
    ]


