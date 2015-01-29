'''
pdok wfs:
http://geodata.nationaalgeoregister.nl/bestuurlijkegrenzen/wfs?SERVICE=WFS&VERSION=1.0.0&REQUEST=GetFeature&TYPENAME=bestuurlijkegrenzen:gemeenten&SRSNAME=EPSG:28992&BBOX=0,300000,300000,600000
http://geodata.nationaalgeoregister.nl/bestuurlijkegrenzen/wfs?SERVICE=WFS&VERSION=1.0.0&REQUEST=GetCapabilities
'''

import osgeo
from osgeo import gdal,ogr
import os, sys

def main( gemnaam ):

    curr_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(curr_dir,'data\\')
    out_file = os.path.join(data_dir, gemnaam[0] + '.gpkg')

    #ERROR 4: Unable to open EPSG support file gcs.csv.Try setting the GDAL_DATA environment variable to point to the directory containing EPSG csv files.
    osgeo.gdal.SetConfigOption("GDAL_DATA", 'C:\Gis\OSGeo4W64260\share\gdal')
    
    wfs_driver = ogr.GetDriverByName('WFS')
    wfs_filter = '&FILTER=%3Cogc:Filter%20xmlns:ogc=%22http://www.opengis.net/ogc%22%3E%3Cogc:PropertyIsEqualTo%3E%3Cogc:PropertyName%3Egemeentenaam%3C/ogc:PropertyName%3E%3Cogc:Literal%3E' + gemnaam[0] + '%3C/ogc:Literal%3E%3C/ogc:PropertyIsEqualTo%3E%3C/ogc:Filter%3E'
    wfs_string = 'http://geodata.nationaalgeoregister.nl/bestuurlijkegrenzen/wfs?SERVICE=WFS&VERSION=1.0.0&REQUEST=GetFeature&TYPENAME=bestuurlijkegrenzen:gemeenten&SRSNAME=EPSG:28992' + wfs_filter
    #print wfs_string
    wfs_getfea = wfs_driver.Open(wfs_string)

    wfs_glayer = wfs_getfea.GetLayer()
    
    #need latest gdal 1.11+ for this (geopackage) to work
    out_driver = ogr.GetDriverByName('GPKG')

    if os.path.exists(out_file):
        out_driver.DeleteDataSource(out_file)

    out_datasource = out_driver.CreateDataSource(out_file)
    out_layer = out_datasource.CopyLayer(wfs_glayer, gemnaam[0])

    
if __name__ == '__main__':

    if len( sys.argv ) < 2:
        print "[ FOUT ]: geef een gemeente naam!!"
        sys.exit(1)

    main( sys.argv[1:] )