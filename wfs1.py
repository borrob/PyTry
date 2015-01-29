'''
pdok wfs:
http://geodata.nationaalgeoregister.nl/bestuurlijkegrenzen/wfs?SERVICE=WFS&VERSION=1.0.0&REQUEST=GetFeature&TYPENAME=bestuurlijkegrenzen:gemeenten&SRSNAME=EPSG:28992&BBOX=0,300000,300000,600000
http://geodata.nationaalgeoregister.nl/bestuurlijkegrenzen/wfs?SERVICE=WFS&VERSION=1.0.0&REQUEST=GetCapabilities
'''

import osgeo
from osgeo import gdal,ogr

def main():

    #ERROR 4: Unable to open EPSG support file gcs.csv.Try setting the GDAL_DATA environment variable to point to the directory containing EPSG csv files.
    osgeo.gdal.SetConfigOption("GDAL_DATA", 'C:\Gis\OSGeo4W64\share\gdal')

    
    layer_list = []
    driver = ogr.GetDriverByName('WFS')
    wfsurl = driver.Open('http://geodata.nationaalgeoregister.nl/bestuurlijkegrenzen/wfs?SERVICE=WFS&VERSION=1.0.0&REQUEST=GetCapabilities')    

    for i in range(0, wfsurl.GetLayerCount()):
        layer = wfsurl.GetLayerByIndex(i)
        layer_list.append(layer.GetName())
    
    wfsurl.Destroy()
    
    print layer_list
    
if __name__ == '__main__':

    main()