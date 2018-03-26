from convertion_modules import (dbd_to_ram,
                                ram_to_xml)

def parse(dbd,xdb):
    #converting dbd to ram
    schema1 = dbd_to_ram(dbd)

    #converting ram to xml
    resXML = ram_to_xml(schema1)
    with open(xdb, "w") as file:
        file.write(resXML.toprettyxml(encoding="utf-8").decode("utf-8"))

