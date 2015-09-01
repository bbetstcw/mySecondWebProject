# Create your views here.
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from mooncakeTestEnvironment.models import Landing_page, Navigation, Navigation_article, Navigation_group, Recent_update, Service, Tutorial_option, Video_link
from django.template import loader, Template, Context
from django.template.loader_tags import BlockNode, TextNode

RELATIVE_PATH = "/static/mooncakeTestEnvironment/"
BLOB_PATH = "http://wacndevelop.blob.core.chinacloudapi.cn/tech-content/"


def landingPage(request, service_id):
    service = get_object_or_404(Service, service_id=service_id)
    landingpage = service.landing_page_set.all()[0]
    tutorial_options = landingpage.tutorial_option_set.all().order_by("order")
    first_option_title = tutorial_options[0].title
    first_option_link = tutorial_options[0].link
    if "edit" in request.GET:
        edit = True
    else:
        edit = False
    return render_to_response('mooncakeTestEnvironment/frame.html', {"service_name":service.service_name,
                                                                     "subtitle":landingpage.subtitle, 
                                                                     "tutorial_message":landingpage.tutorial_message,
                                                                     "update_search_link":landingpage.update_search_link,
                                                                     "navigationJson":landingpage.navigationJson.replace("'", "\\'"),
                                                                     "first_option_title":first_option_title,
                                                                     "first_option_link":first_option_link,
                                                                     "options":tutorial_options,
                                                                     "videoLinks":landingpage.video_link_set.all().order_by("order")[:3],
                                                                     "recentUpdates":landingpage.recent_update_set.all().order_by("order"),
                                                                     "cssLink":RELATIVE_PATH+"style/frame2.css",
                                                                     "jqueryLink":RELATIVE_PATH+"script/jquery-2.1.4.js",
                                                                     "jsLink":RELATIVE_PATH+"script/responsive.js",
                                                                     "imgLink":RELATIVE_PATH+"img/",
                                                                     "edit":edit,
                                                                     "azure":True})

def index(request):
    services = Service.objects.all()
    print(len(services))
    return render_to_response('mooncakeTestEnvironment/index.html', {"services":services})

def xmlpagegenerator(request, service_id):
    service = get_object_or_404(Service, service_id=service_id)
    landingpage = service.landing_page_set.all()[0]
    tutorial_options = landingpage.tutorial_option_set.all().order_by("order")
    first_option_title = tutorial_options[0].title
    first_option_link = tutorial_options[0].link
    template = loader.get_template('mooncakeTestEnvironment/xmlTemplate.xml')
    frame = loader.get_template('mooncakeTestEnvironment/frame.html')
    for node in frame.template.nodelist:
        print(node)
        for child_node in node.nodelist:
            print(type(child_node))
            if type(child_node) == BlockNode:
                if child_node.name == 'header':
                    html_header = child_node
                elif child_node.name == 'content':
                    html_body = child_node
    header = Template("")
    body = Template("")
    header.nodelist = html_header
    body.nodelist = html_body
    html_header = header.render(Context({}))
    html_body = body.render(Context({"service_name":service.service_name,
                                "subtitle":landingpage.subtitle, 
                                "tutorial_message":landingpage.tutorial_message,
                                "update_search_link":landingpage.update_search_link,
                                "navigationJson":landingpage.navigationJson.replace("'", "\\'"),
                                "first_option_title":first_option_title,
                                "first_option_link":first_option_link,
                                "options":tutorial_options,
                                "videoLinks":landingpage.video_link_set.all().order_by("order"),
                                "recentUpdates":landingpage.recent_update_set.all().order_by("order"),
                                "cssLink":BLOB_PATH+"css/landingpageframe.css",
                                "jqueryLink":BLOB_PATH+"js/landingpagejquery-2.1.4.js",
                                "jsLink":BLOB_PATH+"js/landingpageresponsive.js",
                                "imgLink":BLOB_PATH+"media/"}))
    return render_to_response('mooncakeTestEnvironment/xmlPageGenerator.html',{"xmlContent":template.render({"html_header":html_header, "html_body":html_body, "html_title":service.service_name})})

def newRecentUpdate(request, counter):
    return render_to_response('mooncakeTestEnvironment/updateEditTemplate.html', {'counter':counter})

def editTutorialSelectList(request, service_id):
    service = get_object_or_404(Service, service_id=service_id)
    tutorial_options = service.landing_page_set.all()[0].tutorial_option_set.all().order_by("order")
    return render_to_response('mooncakeTestEnvironment/selectListTemplate.html',{"options":tutorial_options})