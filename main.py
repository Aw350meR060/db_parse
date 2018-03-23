import xml.dom.minidom as md

from convertion_modules import (xml_to_ram,
                                ram_to_xml,
                                ram_to_dbd)

#parsing an xml file
tasks = md.parse("tasks.xml")

#converting xml to ram
schema = xml_to_ram(tasks)

resXML = ram_to_xml(schema)
with open("result.xdb", "w") as file:
    file.write(resXML.toprettyxml(encoding="utf-8").decode("utf-8"))

ram_to_dbd(schema)