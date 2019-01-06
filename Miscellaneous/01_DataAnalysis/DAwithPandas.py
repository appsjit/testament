import pandas
import ssl
import certifi
import geopy.geocoders

from geopy.geocoders import ArcGIS

def dataAna():
    print('Start with Data Analysis')
    df1  = pandas.read_csv("supermarkets.csv")

    ctx = ssl.create_default_context(cafile=certifi.where())
    geopy.geocoders.options.default_ssl_context = ctx
    nom=ArcGIS()

    print(nom.geocode("242 Fairmeadow Way Milpitas CA"))

    df1["FullAddr"] = df1["Address"] + " " +df1["City"] +" "+ df1["State"]+" " + df1["Country"]
    df1["LatLong"] = df1["FullAddr"].apply(nom.geocode)
    df1["Latitude"] = df1["LatLong"].apply(lambda x: x.latitude if x != None else None)
    ##print(dir(df1))

    # To iterate over Data Frame
    # for idx,rws in df1.iterrows():
    #     n = nom.geocode(rws['FullAddr'])
    #     print((n.latitude))

    # To return sum of one column
    ##tot =  df1['Employees'].sum()
    ##tot = sum(df1['Employees'])

    return df1


if __name__ == '__main__':
    print(dataAna())