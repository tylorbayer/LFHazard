from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .model import SessionMaker, StreamGage
from tethys_sdk.gizmos import MapView, MVLayer, MVView
from tethys_sdk.gizmos import TextInput
from tethys_sdk.gizmos import SelectInput
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
    print returnPeriod
    print "*************"

    #******************************************************************************
    # This part is just to test the map
    # Transform into GeoJSON format
    features = []
    # Sets up the points from the csv file
    path = '/home/student/tethysdev/tethysapp-lfhazard/tethysapp/lfhazard/public/csv/Test.csv'
    # path = '/static/tethysapp-lfhazard/tethysapp/lfhazard/public/csv/Test.csv'
    liqu_data = []

    # This opens the csv file, extracts the data and puts it in a array.
    with open(path, 'rb') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            temp = []
            longitude = row[0]
            temp.append(longitude)
            latitude = row[1]
            temp.append(latitude)
            value = row[2]
            temp.append(value)
            liqu_data.append(temp)
    for r in liqu_data[1:]: # the [1:] skips the first row
        temp_long = float(r[0])
        temp_lat = float(r[1])
        temp_coor = [temp_lat,temp_long]
        temp_point = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': temp_coor
            }
        }
        features.append(temp_point)


    #$$$$$$$$$$$$$$$$$$$$$$$$ This gets the LS data out $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # gets the data from the LS-475.csv file
    path_LS475 = '/home/student/tethysdev/tethysapp-lfhazard/tethysapp/lfhazard/public/csv/LS-475.csv'
    liqu_data_LS475 = []
    with open(path_LS475, 'rb') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            temp = []
            longitude = row[0]
            temp.append(longitude)
            latitude = row[1]
            temp.append(latitude)
            DHREF = row[2]
            temp.append(DHREF)
            liqu_data_LS475.append(temp)
    # gets the dat from the LS-1033.csv file
    path_LS1033 = '/home/student/tethysdev/tethysapp-lfhazard/tethysapp/lfhazard/public/csv/LS-1033.csv'
    liqu_data_LS1033 = []
    with open(path_LS1033, 'rb') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            temp = []
            longitude = row[0]
            temp.append(longitude)
            latitude = row[1]
            temp.append(latitude)
            DHREF = row[2]
            temp.append(DHREF)
            liqu_data_LS1033.append(temp)
    # gets the dat from the LS-2475.csv file
    path_LS2475 = '/home/student/tethysdev/tethysapp-lfhazard/tethysapp/lfhazard/public/csv/LS-2475.csv'
    liqu_data_LS2475 = []
    with open(path_LS2475, 'rb') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            temp = []
            longitude = row[0]
            temp.append(longitude)
            latitude = row[1]
            temp.append(latitude)
            DHREF = row[2]
            temp.append(DHREF)
            liqu_data_LS2475.append(temp)

    #$$$$$$$$$$$$$$$$$$$$$$$$ This gets the SSD data out $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # gets the dat from the SSD-475.csv file
    path_SSD475 = '/home/student/tethysdev/tethysapp-lfhazard/tethysapp/lfhazard/public/csv/SSD-475.csv'
    liqu_data_SSD475 = []
    with open(path_SSD475, 'rb') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            temp = []
            longitude = row[0]
            temp.append(longitude)
            latitude = row[1]
            temp.append(latitude)
            Cetin_percent = row[2]
            temp.append(Cetin_percent)
            IandY_percent = row[3]
            temp.append(IandY_percent)
            PB_Seismic_Slope_Disp_RandS = row[4]
            temp.append(PB_Seismic_Slope_Disp_RandS)
            PB_Seismic_Slope_Disp_RandT = row[5]
            temp.append(PB_Seismic_Slope_Disp_RandT)
            liqu_data_SSD475.append(temp)
    # gets the dat from the SSD-1033.csv file
    path_SSD1033 = '/home/student/tethysdev/tethysapp-lfhazard/tethysapp/lfhazard/public/csv/SSD-1033.csv'
    liqu_data_SSD1033 = []
    with open(path_SSD1033, 'rb') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            temp = []
            longitude = row[0]
            temp.append(longitude)
            latitude = row[1]
            temp.append(latitude)
            Cetin_percent = row[2]
            temp.append(Cetin_percent)
            IandY_percent = row[3]
            temp.append(IandY_percent)
            PB_Seismic_Slope_Disp_RandS = row[4]
            temp.append(PB_Seismic_Slope_Disp_RandS)
            PB_Seismic_Slope_Disp_RandT = row[5]
            temp.append(PB_Seismic_Slope_Disp_RandT)
            liqu_data_SSD1033.append(temp)
    # gets the dat from the SSD-2475.csv file
    path_SSD2475 = '/home/student/tethysdev/tethysapp-lfhazard/tethysapp/lfhazard/public/csv/SSD-2475.csv'
    liqu_data_SSD2475 = []
    with open(path_SSD2475, 'rb') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            temp = []
            longitude = row[0]
            temp.append(longitude)
            latitude = row[1]
            temp.append(latitude)
            Cetin_percent = row[2]
            temp.append(Cetin_percent)
            IandY_percent = row[3]
            temp.append(IandY_percent)
            PB_Seismic_Slope_Disp_RandS = row[4]
            temp.append(PB_Seismic_Slope_Disp_RandS)
            PB_Seismic_Slope_Disp_RandT = row[5]
            temp.append(PB_Seismic_Slope_Disp_RandT)
            liqu_data_SSD2475.append(temp)

    #$$$$$$$$$$$$$$$$$$$$$$$$ This gets the LT data out $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # gets the dat from the LT-475.csv file
    path_LT475 = '/home/student/tethysdev/tethysapp-lfhazard/tethysapp/lfhazard/public/csv/LT-475.csv'
    liqu_data_LT475 = []
    with open(path_LT475, 'rb') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            temp = []
            longitude = row[0]
            temp.append(longitude)
            latitude = row[1]
            temp.append(latitude)
            PB_Nreq_Cetin = row[2]
            temp.append(PB_Nreq_Cetin)
            PB_CSRp = row[3]
            temp.append(PB_CSRp)
            liqu_data_LT475.append(temp)
    # gets the dat from the LT-1033.csv file
    path_LT1033 = '/home/student/tethysdev/tethysapp-lfhazard/tethysapp/lfhazard/public/csv/LT-1033.csv'
    liqu_data_LT1033 = []
    with open(path_LT1033, 'rb') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            temp = []
            longitude = row[0]
            temp.append(longitude)
            latitude = row[1]
            temp.append(latitude)
            PB_Nreq_Cetin = row[2]
            temp.append(PB_Nreq_Cetin)
            PB_CSRp = row[3]
            temp.append(PB_CSRp)
            liqu_data_LT1033.append(temp)
    # gets the dat from the LT-2475.csv file
    path_LT2475 = '/home/student/tethysdev/tethysapp-lfhazard/tethysapp/lfhazard/public/csv/LT-2475.csv'
    liqu_data_LT2475 = []
    with open(path_LT2475, 'rb') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            temp = []
            longitude = row[0]
            temp.append(longitude)
            latitude = row[1]
            temp.append(latitude)
            PB_Nreq_Cetin = row[2]
            temp.append(PB_Nreq_Cetin)
            PB_CSRp = row[3]
            temp.append(PB_CSRp)
            liqu_data_LT2475.append(temp)

    # This makes the points
    for r in liqu_data_SSD475[1:]:
        temp_long = float(r[0])
        temp_lat = float(r[1])
        temp_coor = [temp_long,temp_lat]
        temp_point = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': temp_coor
            }
        }

        # features.append(temp_point)

    #******************************************************************************

    # this part helps with zooming to the lat and long entered into

    if str(lon)!='' and str(lat)!='':
        temp_lon = float(lon)
        temp_lat = float(lat)
        zoom_pt = [temp_lon,temp_lat]
    else:
        zoom_pt = [-111.70, 40.24]


    #================================================================

    geojson_objects = {
      'type': 'FeatureCollection',
      'crs': {
        'type': 'name',
        'properties': {
          'name': 'EPSG:4326'
        }
      },
      'features': features
    }

    # Define layer for Map View
    geojson_layer = MVLayer(source='GeoJSON',
                            options=geojson_objects,
                            legend_title='Test points',
                            legend_extent=[-111.74, 40.22, -111.67, 40.25])

    # Define initial view for Map View
    view_options = MVView(
        projection='EPSG:4326',
        center=zoom_pt,
        zoom=4,
        maxZoom=18,
        minZoom=2
    )

    # Configure the map
    map_options = MapView(height='500px',
                          width='100%',
                          layers=[geojson_layer],
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
def echo_name(request):
    """
    Controller that will echo the name provided by the user via a form.
    """
    # Default value for name
    state = ''
    lat = ''
    lon = ''
    modelYear = ''
    returnPeriod = ''

    # Define Gizmo Options
    select_state = SelectInput(display_text='State:',
                            name='select_state',
                            multiple=False,
                            options=[('Utah', 'Utah'), ('Alaska', 'Alaska')],
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

    # Create template context dictionary
    context = {'state': state,
               'lat': lat,
               'lon': lon,
               'modelYear': modelYear,
               'returnPeriod': returnPeriod,
               'select_state': select_state,
               'text_input_lat': text_input_lat,
               'text_input_lon': text_input_lon,
               'select_modelYear': select_modelYear,
               'select_returnPeriod': select_returnPeriod}

    #This creates the

    return render(request, 'lfhazard/echo_name.html', context)