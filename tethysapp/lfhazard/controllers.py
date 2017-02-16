from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'lfhazard/home.html', context)
def map(request):
    """
    Controller for the map
    """
    map_options = MapView(height='500px',
                          width='100%',
                          layers=[geojson_layer],
                          view=view_options,
                          basemap='OpenStreetMap',
                          legend=True)
    # Pass variables to the template via the context dictionary
    context = {'map_options': map_options}
    #herl
    #sdfg
    return render(request, 'lfhazard/map.html', context)