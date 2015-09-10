# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json

SERVICE_TRANSLATION = {"azureMySql":"MySQL Database on Azure"}

JSON_PATH = "./mooncakeTestEnvironment/static/mooncakeTestEnvironment/json/"

def addDataToTable(apps, schema_editor):
    Landing_page = apps.get_model("mooncakeTestEnvironment", "Landing_page")
    Recent_update = apps.get_model("mooncakeTestEnvironment", "Recent_update")
    Service = apps.get_model("mooncakeTestEnvironment", "Service")
    Tutorial_option = apps.get_model("mooncakeTestEnvironment", "Tutorial_option")
    Video_link = apps.get_model("mooncakeTestEnvironment", "Video_link")
    Navigation = apps.get_model("mooncakeTestEnvironment", "Navigation")
    Navigation_group = apps.get_model("mooncakeTestEnvironment", "Navigation_group")
    Navigation_article = apps.get_model("mooncakeTestEnvironment", "Navigation_article")

    for service_id,service_name in SERVICE_TRANSLATION.items():
        service = Service(service_id=service_id, service_name=service_name)
        service.save()
        navigationJson = readFileToString(JSON_PATH+"navigationJson/"+service_id+".json")
        navigationWhole = json.loads(navigationJson)
        navigation = Navigation(service=service, html_id=navigationWhole["id"])
        navigation.save()
        order = 1
        for groupWhole in navigationWhole["navigation"]:
            group = Navigation_group(navigation=navigation, group=groupWhole["group"], html_id=groupWhole["id"], order=order)
            order+=1
            group.save()
            order2 = 1
            for articleWhole in groupWhole["articles"]:
                article = Navigation_article(navigation_group=group, title=articleWhole["title"], link=articleWhole["link"], html_id=articleWhole["id"], order=order2)
                order2+=1
                article.save()
            
        content = json.loads(readFileToString(JSON_PATH+"contentJson/"+service_id+".json"))
        landing_page = Landing_page(service=service, navigationJson=navigationJson, subtitle=content["subtitle"], tutorial_message=content["tutorial_message"], update_search_link=content["update_search_links"])
        landing_page.save()
        options = json.loads(readFileToString(JSON_PATH+"tutorialOptionsJson/"+service_id+".json"))
        order=1
        for option in options:
            tutorial_option = Tutorial_option(landing_page=landing_page, order=order, title=option["title"], link=option["link"])
            order+=1
            tutorial_option.save()
        videos = json.loads(readFileToString(JSON_PATH+"videoLinkJson/"+service_id+".json"))
        order=1
        for video in videos:
            video_link = Video_link(landing_page=landing_page, order=order, video_url=video["VideoUrl"], title=video["Title"], publish_time=video["PublishTime"], duration=video["Duration"], description=video["Description"])
            order+=1
            video_link.save()
        updates = json.loads(readFileToString(JSON_PATH+"recentUpdateJson/"+service_id+".json"))
        order=1
        for update in updates:
            recent_update = Recent_update(landing_page=landing_page, order=order, title=update["update_title"], date=update["update_date"], description=update["update_description"], detail=update["update_detail"])
            order+=1
            recent_update.save()

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
        ('mooncakeTestEnvironment', '0005_add_2_pages'),
    ]

    operations = [
        migrations.RunPython(addDataToTable),
    ]


