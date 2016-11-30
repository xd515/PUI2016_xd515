import os

def getdata():
    filename = '/nycb2010_16d/nycb2010.shp'
    puidata = os.getenv("PUIDATA")
    if not os.path.isfile(puidata + filename):
        os.system("curl -O http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycb2010_16d.zip")
        os.system("mv nycb2010_16d.zip " + puidata)
        os.system("unzip " + puidata + "/nycb2010_16d.zip -d " + puidata)