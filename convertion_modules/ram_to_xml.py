import functools
from convertion_modules import minidom_fixed as dom
from ram_data import Schema, Domain, Table, Constraint, Field, Index, Item

def ram_to_xml(schema):
    if schema == None:
        raise ValueError("Schema is empty")
    xml = dom.Document()

    node = xml.createElement("dbd_schema")
    if schema.fulltext_engine != None:
        node.setAttribute("fulltext_engine", schema.fulltext_engine)
    if schema.version != None:
        node.setAttribute("version", schema.version)
    if schema.name != None:
        node.setAttribute("name", schema.name)
    if schema.description != None:
        node.setAttribute("description", schema.description)
    node.appendChild(xml.createElement("custom"))

    domains = xml.createElement("domains")
    createDomain = functools.partial(_createDomainNode, xml)
    for domain in map(createDomain, schema.domains):
        domains.appendChild(domain)
    node.appendChild(domains)

    tables = xml.createElement("tables")
    createTable = functools.partial(_createTableNode, xml)
    for table in map(createTable, schema.tables):
        tables.appendChild(table)
    node.appendChild(tables)

    xml.appendChild(node)
    return xml


def _createDomainNode(xml, domain, node = None):
    if node is None:
        node = xml.createElement("domain")

    if domain.name != None:
        node.setAttribute("name", domain.name)
    if domain.description != None:
        node.setAttribute("description", domain.description)
    if domain.type != None:
        node.setAttribute("type", domain.type)
    if domain.align != None:
        node.setAttribute("align", domain.align)
    if domain.width != None:
        node.setAttribute("width", domain.width)
    if domain.precision != None:
        node.setAttribute("precision", domain.precision)

    props = []
    if domain.show_null:
       props.append("show_null")
    if domain.summable:
       props.append("summable")
    if domain.case_sensitive:
       props.append("case_sensitive")
    if domain.show_lead_nulls:
       props.append("show_lead_nulls")
    if domain.thousands_separator:
       props.append("thousands_separator")
    if props != []:
        node.setAttribute("props", ", ".join(props))

    if domain.char_length != None:
        node.setAttribute("char_length", domain.char_length)
    if domain.length != None:
        node.setAttribute("length", domain.length)
    if domain.scale != None:
        node.setAttribute("scale", domain.scale)

    return node


def _createTableNode(xml, table, node=None):
    if node is None:
        node = xml.createElement("table")

    if table.name != None:
        node.setAttribute("name", table.name)
    if table.description != None:
        node.setAttribute("description", table.description)

    props = []
    if table.add:
       props.append("add")
    if table.edit:
       props.append("edit")
    if table.delete:
       props.append("delete")
    if props != []:
        node.setAttribute("props", ", ".join(props))

    if table.ht_table_flags != None:
        node.setAttribute("ht_table_flags", table.ht_table_flags)
    if table.access_level != None:
        node.setAttribute("access_level", table.access_level)

    createField = functools.partial(_createFieldNode, xml)
    for field in map(createField, table.fields):
        node.appendChild(field)

    createConstraint = functools.partial(_createConstraintNode, xml)
    for constraint in map(createConstraint, table.constraints):
        node.appendChild(constraint)

    createIndex = functools.partial(_createIndexNode, xml)
    for index in map(createIndex, table.indices):
        node.appendChild(index)

    return node


def _createFieldNode(xml, field, node=None):
    if node is None:
        node = xml.createElement("field")

    if field.name != None:
        node.setAttribute("name", field.name)
    if field.rname != None:
        node.setAttribute("rname", field.rname)
    if field.domain != None:
        node.setAttribute("domain", field.domain)
    if field.description != None:
        node.setAttribute("description", field.description)

    props = []
    if field.input:
        props.append("input")
    if field.edit:
        props.append("edit")
    if field.show_in_grid:
        props.append("show_in_grid")
    if field.show_in_details:
        props.append("show_in_details")
    if field.is_mean:
        props.append("is_mean")
    if field.autocalculated:
        props.append("autocalculated")
    if field.required:
        props.append("required")
    if props != []:
        node.setAttribute("props", ", ".join(props))

    return node


def _createConstraintNode(xml, constraint):
    node = xml.createElement("constraint")

    if constraint.name != None:
        node.setAttribute("name", constraint.name)
    if constraint.kind != None:
        node.setAttribute("kind", constraint.kind)
    if constraint.items != None:
        if len(constraint.items) == 1:
            node.setAttribute("items", constraint.items[0])
        else:
            pass
    if constraint.reference_type != None:
        node.setAttribute("reference_type", constraint.reference_type)
    if constraint.reference != None:
        node.setAttribute("reference", constraint.reference)
    if constraint.expression != None:
        node.setAttribute("", constraint.expression)

    props = []
    if constraint.has_value_edit:
        props.append("has_value_edit")
    if constraint.cascading_delete:
        props.append("cascading_delete")
    if constraint.full_cascading_delete:
        props.append("full_cascading_delete")
    if props != []:
        node.setAttribute("props", ", ".join(props))

    return node


def _createIndexNode(xml, index):
    if index.fields != []:
        node = xml.createElement("index")
        if len(index.fields) == 1:
            node.setAttribute("field",index.fields[0].name)
        else:
            createItem = functools(_createItem, xml)
            for item in map(createItem, index.fields):
                node.appendChild(item)

        if index.name != None:
            node.setAttribute("name", index.name)

        props = [];
        if index.fulltext:
            props.append("fulltext")
        if index.uniqueness:
            props.append("uniqueness")
        if index.is_clustered:
            props.append("clustered")
        if props != []:
            node.setAttribute("props", ", ".join(props))

        return node
    else:
        raise ValueError("Index has no fields")


def _createItem(xml, item):
    node = xml.createElement("item")
    node.setAttribute("name", item.name)
    node.setAttribute("position", str(item.position))
    if item.desc:
        node.setAttribute("desc")

    return node