'''
pdok wfs:
http://geodata.nationaalgeoregister.nl/bestuurlijkegrenzen/wfs?SERVICE=WFS&VERSION=1.0.0&REQUEST=GetFeature&TYPENAME=bestuurlijkegrenzen:gemeenten&SRSNAME=EPSG:28992&BBOX=0,300000,300000,600000
'''

from osgeo import ogr
import os, sys

def main( gemnaam ):
    print gemnaam
    
    
if __name__ == '__main__':

    if len( sys.argv ) < 2:
        print "[ FOUT ]: geef een gemeente naam!!"
        sys.exit(1)

    main( sys.argv[1:] )