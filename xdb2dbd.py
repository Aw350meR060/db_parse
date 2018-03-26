import xml.dom.minidom as md

from convertion_modules import (xml_to_ram,
                                ram_to_dbd)
def parse(xdb, dbd):
    #parsing an xml file
    tasks = md.parse(xdb)

    #converting xml to ram
    schema = xml_to_ram(tasks)

    #converting ram to dbd
    ram_to_dbd(schema, dbd)