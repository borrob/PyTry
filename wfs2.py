'''
pdok wfs:
http://geodata.nationaalgeoregister.nl/bestuurlijkegrenzen/wfs?SERVICE=WFS&VERSION=1.0.0&REQUEST=GetFeature&TYPENAME=bestuurlijkegrenzen:gemeenten&SRSNAME=EPSG:28992&BBOX=0,300000,300000,600000
http://geodata.nationaalgeoregister.nl/bestuurlijkegrenzen/wfs?SERVICE=WFS&VERSION=1.0.0&REQUEST=GetCapabilities
'''

import osgeo
from osgeo import gdal,ogr

def main( ):

    #ERROR 4: Unable to open EPSG support file gcs.csv.Try setting the GDAL_DATA environment variable to point to the directory containing EPSG csv files.
    osgeo.gdal.SetConfigOption("GDAL_DATA", 'C:\Gis\OSGeo4W64\share\gdal')
    #osgeo.gdal.SetConfigOption('OGR_WFS_PAGING_ALLOWED', 'YES')
    #osgeo.gdal.SetConfigOption('OGR_WFS_PAGE_SIZE', '10000')
    
    driver = ogr.GetDriverByName('WFS')
    wfsurl = driver.Open('http://geodata.nationaalgeoregister.nl/bestuurlijkegrenzen/wfs?SERVICE=WFS&VERSION=1.0.0&REQUEST=GetFeature&TYPENAME=bestuurlijkegrenzen:gemeenten&SRSNAME=EPSG:28992&BBOX=0,300000,300000,600000')    

    layer = wfsurl.GetLayer()
    featureCount = layer.GetFeatureCount()
    print featureCount
    
if __name__ == '__main__':
    main( )