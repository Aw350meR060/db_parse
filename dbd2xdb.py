from convertion_modules import (dbd_to_ram,
                                ram_to_xml)

def parse():
    dbd_path = "result_files/result.db"
    xdb_path = "result_files/result.xdb"

    #converting dbd to ram
    schema1 = dbd_to_ram(dbd_path)

    #converting ram to xml
    resXML = ram_to_xml(schema1)
    with open(xdb_path, "w") as file:
        file.write(resXML.toprettyxml(encoding="utf-8").decode("utf-8"))

