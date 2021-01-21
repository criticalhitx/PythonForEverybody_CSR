import xml.etree.ElementTree as ET

data = """<person>
    <name>Chuck</name>
    <phone type="intl">+11234124124</phone>
    <email hide="yes"/>
    </person>"""
tree = ET.fromstring(data)
print(type(tree))
print('Name:',tree.find('name').text) #text to see the xml text
print('Attr:',tree.find('email').get('hide')) #Get email attribute