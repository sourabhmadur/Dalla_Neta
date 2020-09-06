from flask import Flask,render_template, flash, redirect,request
from forms import LoginForm
import geopandas as gpd
from shapely.geometry import Point
app = Flask(__name__)

geo_df = gpd.read_file('../maps-master/assembly-constituencies/India_AC.shp')
geo_df_assembly = geo_df[['AC_NO','AC_NAME','ST_NAME','geometry']]
geo_df_mh_assembly = geo_df_assembly[geo_df_assembly['ST_NAME']=="MAHARASHTRA"]

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    lat = request.form['lat']
    lon= request.form['lon']
    processed_text = get_constituency_from_coordinates(float(lat), float(lon))
    return processed_text

def get_constituency_from_coordinates(lat,lon):
    # p1 = Point(73.0219966, 19.0311954)
    p1 = Point(lat, lon)
# p1 = Point(19.205135, 72.972277)
    for index, row in geo_df_mh_assembly.iterrows():
        if p1.within(row['geometry']):
            return '<a href=https://myneta.info/mh2009/index.php?action=show_candidates&constituency_id={}>myneta</a>'.format(str(row['AC_NO']))

if __name__ == '__main__':
    app.run()