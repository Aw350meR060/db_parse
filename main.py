import xdb2dbd,dbd2xdb,generate_db
from convertion_modules import dbd_to_ram
import xml.dom.minidom as md


xdb_s = "source_files/prjadm.xdb"
dbd_r = "result_files/result.db"
xdb_r = "result_files/result.xdb"
pg_name = "db_metadata"

xdb2dbd.parse(xdb_s,dbd_r)

dbd2xdb.parse(dbd_r,xdb_r)

schema = dbd_to_ram(dbd_r)
generate_db.generate_db(schema,pg_name)