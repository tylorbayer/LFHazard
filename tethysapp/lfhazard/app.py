from tethys_sdk.base import TethysAppBase, url_map_maker


class LiquifactionHazardApp(TethysAppBase):
    """
    Tethys app class for Liquifaction Hazard App.
    """

    name = 'Liquifaction Hazard App'
    index = 'lfhazard:home'
    icon = 'lfhazard/images/icon.gif'
    package = 'lfhazard'
    root_url = 'lfhazard'
    color = '#9b59b6'
    description = '"Liquifaction Hazard Lookup"'
    tags = '"Liquifaction", "Geotech"'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='lfhazard',
                           controller='lfhazard.controllers.home'),
        )

        return url_maps