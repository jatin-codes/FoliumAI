from bs4 import BeautifulSoup
import urllib.request as urllib2

'''
Common Name: Japanese maple 
Type: Tree
Family: Sapindaceae
Native Range: Korea, Japan
Zone: 5 to 8
Height: 10.00 to 25.00 feet
Spread: 10.00 to 25.00 feet
Bloom Time: April
Bloom Description: Reddish-purple
Sun: Full sun to part shade
Water: Medium
Maintenance: Low
Flower: Insignificant
Leaf: Good Fall
Tolerate: Rabbit, Black Walnut

'''
def get_data(kempercode):
    keys =["name","type", "family", "native", "zone", "hight", "spread", "bloom", "color", "sun", "water", "maintain", "culture", "note", "problem", "garden"]
    fields = []
    quote_page = 'http://www.missouribotanicalgarden.org/PlantFinder/PlantFinderDetails.aspx?kempercode='+kempercode
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_CommonNameRow'})
    if(name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_TypeRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_FamilyRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_NativeRangeRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_ZoneRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_HeightRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_SpreadRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_BloomTimeRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_ColorTextRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_SunRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_WaterRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_MaintenanceRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_CultureRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_NoteworthyRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_ProblemsRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_GardenUseRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Not available")
    for i in range(len(keys)):
        print(str(keys[i])+": "+str(fields[i]))
if __name__ == "__main__":
    get_data("b975")