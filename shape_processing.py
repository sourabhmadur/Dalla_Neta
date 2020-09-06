from shapely.geometry import Point
from shapely.geometry.multipolygon import MultiPolygon
import geopandas as gpd

class Constituency:
	
	def __init__(self, name, code, polygon):
		self.election
		self.name=name
		self.code=code
		self.polygon=polygon


class Election:

	def __init__(self, name, file_name, year=2009 ,description="", state_name=""):
		self.name=name
		self.year=year
		self.constituencies=construct_constituencies_list(file_name, state_name)

	def construct_constituencies_list(file_name, state_name):



geo_df = gpd.read_file('maps-master/assembly-constituencies/India_AC.shp')
geo_df_mh_assembly = geo_df[geo_df['ST_NAME']=="MAHARASHTRA"]

p1 = Point(73.0219966, 19.0311954)
# p1 = Point(19.205135, 72.972277)
for index, row in geo_df_mh_assembly.iterrows():
    if row["AC_NAME"] == "Belapur":
        print(row['geometry'].centroid)
        print(type(row['geometry']))
        print(row['geometry'].contains(p1))
    if p1.within(row['geometry']):
        print(row['AC_NAME'])
        break

