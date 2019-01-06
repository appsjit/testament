import pandas
import requests
from bs4 import BeautifulSoup

def scapData():
    strUrl = "https://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/"
    r=requests.get(strUrl)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    ##print(soup.prettify())
    all=soup.find_all("div",{"class":"propertyRow"})
    print(all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ",""))

    l=[] ## Define List
    for item in all:
        d={} ## Defining Dictionary
        print("---------------------------------------------")
        d["Address"] = item.find_all("span",{"class":"propAddressCollapse"})[0].text
        ##print(item.find_all("span",{"class":"propAddressCollapse"})[0].text)
        d["Locality"] = item.find_all("span", {"class": "propAddressCollapse"})[1].text
        ##print(item.find_all("span", {"class": "propAddressCollapse"})[1].text)
        d["Price"] = item.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", "")
        ##print(item.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", ""))

        try:
            ##print(item.find("span",{"class","infoBed"}).find("b").text)
            d["Beds"] = item.find("span",{"class","infoBed"}).find("b").text
        except:
            d["Beds"] = None

        try:
            ##print(item.find("span",{"class","infoValueFullBath"}).find("b").text)
            d["Full Baths" ] = item.find("span",{"class","infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"] = None
            ##print("NotFound")


        for column_group in item.find_all("div",{"class":"columnGroup"}):
            ##print(column_group)
            for feature_group,feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
                if "Lot Size" in feature_group.text:
                    ##print(feature_group.text,feature_name.text)
                    d["Lot Size"] = feature_name.text

        l.append(d)


    print(l)

    df=pandas.DataFrame(l) ## create Dataframe from List
    df.to_csv("RealEstateData.csv")

    print(df)

    print(df.get('Price').sum())



if __name__ == '__main__':
    scapData()


