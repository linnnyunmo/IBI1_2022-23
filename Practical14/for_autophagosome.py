from xml.dom.minidom import parse
import xml.dom.minidom
import openpyxl

# get the all elements
domtree = xml.dom.minidom.parse("go_obo.xml")
obo = domtree.documentElement
terms = obo.getElementsByTagName('term')

#  Set a dictionary and Calculate the number of child nodes of the child nodes
def childnodes(child_id):
    number = 0
    for term_child in terms:
        id_element = term_child.getElementsByTagName("id")[0]
        term_id = id_element.firstChild.data
        # Only look at is_a elements for the current term
        if term_id == child_id:
            is_a_elements = term_child.getElementsByTagName("is_a")
            for is_a_element in is_a_elements:
                is_a_id = is_a_element.childNodes[0].data
                # Recursively count child nodes
                number += 1 + childnodes(is_a_id)
    return number

# Find the nodes related to ‘autophagosome’
autophagosome = []
for term in terms:
    if "autophagosome" in term.getElementsByTagName('defstr')[0].firstChild.data:
        go_id = term.getElementsByTagName('id')[0].childNodes[0].data
        name = term.getElementsByTagName('name')[0].childNodes[0].data
        defstr_node = term.getElementsByTagName('defstr')[0].childNodes[0].data
        child_nodes = childnodes(go_id)
        # Append a tuple to the list of autophagosome nodes
        autophagosome.append((go_id, name, defstr_node, child_nodes))

# create an Excel workbook and worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

# write column headers
worksheet.append(["Go_id", "Name", "Definition", "Childnodes"])

# write autophagosome nodes to worksheet
for node in autophagosome:
    worksheet.append(node)

# save the excel file
workbook.save("autophagosome.xlsx")
