import xml.etree.ElementTree as et

data= '''
<person>
    <girls>
        <girl x="1">
        <name>Shreya</name>
        <phone type="intl">
            +1234567890
            </phone>
        </girl>
        <girl x="2">
            <name>Rutuja</name>
            <phone type="intl"> +1234567890</phone>
        </girl>
    </girls>
</person>'''

tree= et.fromstring(data)
branch= tree.findall('girls/girl')

for i in branch:
    print("Name:", i.find('name').text)
    print("Attribute: ", i.get('x'))
