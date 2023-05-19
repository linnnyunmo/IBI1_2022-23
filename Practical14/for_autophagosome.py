from xml.dom.minidom import parse
import xml.dom.minidom
import openpyxl
# get the all elements
domtree = xml.dom.minidom.parse("go_obo.xml")
obo = domtree.documentElement
terms = obo.getElementsByTagName('term')
#  Set a dictionary and Calculate the number of child nodes of the child nodes
def childnodes(child_id):
    number=0
    for term in terms:
        go_id=term.getElementsByTagName("id")[0]
        is_a_nodes = term.getElementsByTagName("is_a")

    for is_a_node in is_a_nodes:
        for term in terms:
        is_a_id = is_a_nodes.childNodes[0].data
        if child_id == is_a_id:
            number+=childnodes(go_id.firstchild.nodevalue)
    return number
# Found the nodes related to ‘autophagosome’
    for term in terms:
        defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
        if 'autophagosome' in definition:
            go_id = term.getElementsByTagName('id')[0].childNodes[0].data
            name = term.getElementsByTagName('name')[0].childNodes[0].data
            autophagosomes.append((go_id, name, definition))
            child_nodes = count_child_nodes(go_id)
# create an Excel workbook and worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

# write column headers
worksheet.append(["Go_id", "Name", "Definition", "Childnodes"])
# Add the data to the worksheet
for row in rows:
    sheet.append(row)
# save the excel file
workbook.save("autophagosome.xlsx")
