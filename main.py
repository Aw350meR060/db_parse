import xml.dom.minidom as md

from convertion_data import xml_to_ram

#parsing an xml file
tasks = md.parse("tasks.xml")

#converting xml to ram
schema = xml_to_ram(tasks)


