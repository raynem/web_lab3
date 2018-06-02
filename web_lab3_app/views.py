from django.http import HttpResponse
from django.urls import reverse
import request
from django.shortcuts import render
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom


root = ET.Element('root')
count = 0

def index(request):
    return render(request, "index.html")


def post(request):
    if request.method == 'POST':
        if request.is_ajax():
            if request.POST['file'] in ('','file'):
                data = [{'text': request.POST['field1']}]
                global root, count
                count += 1
                el_name = ET.SubElement(root, 'file')
                x = ET.SubElement(el_name, 'filename')
                xp = ET.SubElement(el_name, 'text')
                x.text = str('file_{}'.format(count))
                xp.text = str(request.POST['field1'])
                tree_out = ET.tostring(root)
                newXML = xml.dom.minidom.parseString(tree_out.decode('UTF-8'))
                pretty_xml = newXML.toprettyxml()

                f = open('web_lab3_app/static/xml/files.xml', "w")
                f.write(pretty_xml)

                return HttpResponse(json.dumps(data))
            else:
                tree = ET.parse('web_lab3_app/static/xml/files.xml')
                r = tree.getroot()
                for file in r.findall('file'):
                    filename = file.find('filename').text
                    if filename == request.POST['file']:
                        file.find('text').text = request.POST['field1']
                tree.write('web_lab3_app/static/xml/files.xml')
                return HttpResponse(json.dumps(''))
    return render(request)



def delete(request):
    if request.method == 'POST':
        if request.is_ajax():
            data = request.POST['mydata']
            tree = ET.parse('web_lab3_app/static/xml/files.xml')
            r = tree.getroot()

            for file in r.findall('file'):
                filename = file.find('filename').text
                if filename == data:
                    r.remove(file)
            tree.write('web_lab3_app/static/xml/files.xml')
            return HttpResponse(json.dumps(''))
    return render(request)


def page1(request):
    return render(request, "html/1.html")


def page2(request):
    return render(request, "html/2.html")


def page3(request):
    return render(request, "html/3.html")
