# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json

SERVICE_TRANSLATION = {"activeDirectory":"Active Directory", "automation":"自动化", "backup":"备份", "cdn":"CDN", "cloudServices":"云服务", "eventHubs":"事件中心",
                       "hdinsight":"HDInsight", "mediaService":"媒体服务", "mobileService":"移动服务", "notificationHubs":"通知中心", "redisCache":"Redis 缓存",
                       "scheduler":"计划程序", "serviceBus":"服务总线", "siteRecovery":"站点恢复", "sqlDatabase":"SQL 数据库", "storage":"存储", "trafficManager":"流量管理器",
                       "virtualMachine":"虚拟机", "virtualNetwork":"虚拟网络", "websites":"网站", "applicationGateway":"应用程序网关","batch":"批处理",
                       "azureMySql":"MySQL Database on Azure","multiFactorAuthentication":"多重身份验证"}

JSON_PATH = "./mooncakeTestEnvironment/static/mooncakeTestEnvironment/json/"

def addDataToTable(apps, schema_editor):
    Landing_page = apps.get_model("mooncakeTestEnvironment", "Landing_page")
    Service = apps.get_model("mooncakeTestEnvironment", "Service")

    for service_id,service_name in SERVICE_TRANSLATION.items():
        service = Service.objects.get(service_id=service_id, service_name=service_name)
        landingpage = service.landing_page_set.all()[0]
        navigation = json.loads(landingpage.navigationJson)
        for group in navigation["navigation"]:
            for article in group["articles"]:
                if "/home/features/" in article["link"]:
                    group["articles"].remove(article)
        navigaionJson = json.dumps(navigation)
        landingpage.navigationJson = navigaionJson
        landingpage.save()
        

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
        ('mooncakeTestEnvironment', '0007_add_1_page'),
    ]

    operations = [
        migrations.RunPython(addDataToTable),
    ]


