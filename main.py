import xml.dom.minidom as md

from convertion_modules import (xml_to_ram,
                                ram_to_xml,
                                ram_to_dbd,
                                dbd_to_ram)

#parsing an xml file
tasks = md.parse("prjadm.xdb")

#converting xml to ram
schema = xml_to_ram(tasks)

#converting ram to dbd
ram_to_dbd(schema)

#converting dbd to ram
schema1 = dbd_to_ram("result.db")

#converting ram to xml
resXML = ram_to_xml(schema1)
with open("result.xdb", "w") as file:
    file.write(resXML.toprettyxml(encoding="utf-8").decode("utf-8"))

