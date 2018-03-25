
# Database parses

A collection of various database parsers for a student project by Evgeny Sorokin.

## Project Structure

```
xml_db_parse
  │   generate_db.py - empty postgresql database generator
  │   dbd2xml.py - loads a database from sqlite and writes its contents to a xdb file
  │   xml2dbd.py - parses data from a xml/xdb-file and creates a sqlite database
  │
  ├───convertion_modules
  │       dbd_struct.py         - script for creating the database structure
  │       dbd_to_ram.py         - converts a sqlite database into ram-data
  │       minidom_fixed.py      - an xdb-converting util
  │       ram_to_dbd.py         - converts ram-data into a sqlite database
  │       ram_to_xml.py         - converts ram-data into a xdb-file
  │       xml_to_ram.py         - converts a xml/xdb-file into ram-data
  │
  ├───ram_data
  │       *.py   - python classes, containing database structure in ram-data
  │
  ├───result_files
  │       result.db             - result db-file
  │       result.xdb            - result xdb-file
  │
  └────source_files
          prjadm.xdb            - source xdb-file
          tasks.xml             - source xml-file
```