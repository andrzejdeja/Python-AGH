from xml.dom import minidom

doc = minidom.parse("plant_catalog.xml")

for e in doc.getElementsByTagName("PRICE"):
    price = float(e.firstChild.nodeValue.strip("$"))
    print(price)
    if price > 1.0:
        data = "$" + str(price - 0.5)
        print(data)
        e.firstChild.nodeValue = data
        
with open("plant_catalog2.xml", "wb") as out:
    out.write(doc.toxml("utf-8"))
