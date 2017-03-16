from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .model import SessionMaker, StreamGage
from tethys_sdk.gizmos import MapView, MVLayer, MVView
from tethys_sdk.gizmos import TextInput
from tethys_sdk.gizmos import SelectInput

from pyproj import Proj, transform
import csv

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'lfhazard/home.html', context)


@login_required()
def map(request):
    """
    Controller for map page.
    """

    # Default value for name
    state = ''
    lat = ''
    lon = ''
    modelYear = ''
    returnPeriod = ''
    features = []

    # Define Gizmo Options
    select_state = SelectInput(display_text='State:',
                            name='select_state',
                            multiple=False,
                            options=[('Utah', 'Utah'), ('Alaska', 'Alaska'), ('Idaho', 'Idaho'), ('Montana', 'Montana'), ('Oregon', 'Oregon'), ('South Carolina', 'South Carolina'), ('Connecticut', 'Connecticut'),],
                            initial=['Utah', 'Utah'])

    text_input_lat = TextInput(display_text='Latitude',
                                   name='lat-input')

    text_input_lon = TextInput(display_text='Longitude',
                                   name='lon-input')

    select_modelYear = SelectInput(display_text='Model Year:',
                            name='select_modelYear',
                            multiple=False,
                            options=[('2008', 2008), ('2014', 2014)],
                            initial=['2008', 2008])

    select_returnPeriod = SelectInput(display_text='Return Period:',
                            name='select_returnPeriod',
                            multiple=False,
                            options=[('475', 475), ('1033', 1033), ('2475', 2475)],
                            initial=['475', 475])

    # Check form data
    if request.POST and 'lat-input' and 'lon-input' in request.POST:
       lat = request.POST['lat-input']
       lon = request.POST['lon-input']


    if request.POST and 'select_state' and 'select_modelYear' and 'select_returnPeriod' in request.POST:
       state = request.POST['select_state']
       modelYear = request.POST['select_modelYear']
       returnPeriod = request.POST['select_returnPeriod']

    print "*************"
    print lat + " " + lon
    print "*************"


    # this part helps with zooming to the lat and long entered into

    if str(lon)!='' and str(lat)!='':
        temp_lon = float(lon)
        temp_lat = float(lat)
        zoom_pt = [temp_lon,temp_lat]
        inProj = Proj(init='epsg:4326')
        outProj = Proj(init='epsg:3857')
        zoom_pt = transform(inProj, outProj, zoom_pt[0], zoom_pt[1])
    else:
        zoom_pt = [-111.70, 40.24]
        inProj = Proj(init='epsg:4326')
        outProj = Proj(init='epsg:3857')
        zoom_pt = transform(inProj, outProj, zoom_pt[0], zoom_pt[1])


    #================================================================

    geojson_objects = {
      'type': 'FeatureCollection',
      'crs': {
        'type': 'name',
        'properties': {
          'name': 'EPSG:3857'
        }
      },
      'features': features
    }

    # Define layer for Map View
    # geojson_layer = MVLayer(source='GeoJSON',
    #                         options=geojson_objects,
    #                         legend_title='Test points',
    #                         legend_extent=[-111.74, 40.22, -111.67, 40.25])

    # Define initial view for Map View
    view_options = MVView(
        projection='EPSG:3857',
        center=zoom_pt,
        zoom=10,
        maxZoom=18,
        minZoom=2
    )

    # Configure the map
    map_options = MapView(height='500px',
                          width='100%',
                          view=view_options,
                          basemap='OpenStreetMap',
                          legend=True)
    #================================================================
    # Pass variables to the template via the context dictionary
    context = {'map_options': map_options,
               'state': state,
               'lat': lat,
               'lon': lon,
               'modelYear': modelYear,
               'returnPeriod': returnPeriod,
               'select_state': select_state,
               'text_input_lat': text_input_lat,
               'text_input_lon': text_input_lon,
               'select_modelYear': select_modelYear,
               'select_returnPeriod': select_returnPeriod}

    return render(request, 'lfhazard/map.html', context)


@login_required
def documentation(request):

    # Create template context dictionary
    context = {}

    return render(request, 'lfhazard/documentation.html', context)