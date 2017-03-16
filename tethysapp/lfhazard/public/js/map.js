$( document ).ready(function() {
  var map = TETHYS_MAP_VIEW.getMap();

  var format = 'image/png';
  var state = document.getElementById("state").value();
  alert(state);

  var LS = new ol.layer.Tile({
          visible: false,
          source: new ol.source.TileWMS({
            url: 'http://127.0.0.1:8181/geoserver/lfhazard/wms',
            params: {'FORMAT': format, 
                     'VERSION': '1.1.1',
                     tiled: true,
                  LAYERS: 'lfhazard:Kriging_LS-475_Utah2008',
                  STYLES: '',
            }
          })
        });

  var LT_Nreq = new ol.layer.Tile({
          visible: false,
          source: new ol.source.TileWMS({
            url: 'http://127.0.0.1:8181/geoserver/lfhazard/wms',
            params: {'FORMAT': format, 
                     'VERSION': '1.1.1',
                     tiled: true,
                  LAYERS: 'lfhazard:Kriging_LT-475_Utah_PB_Nreq_Cetin2008',
                  STYLES: '',
            }
          })
        });

  var LT_CSR = new ol.layer.Tile({
          visible: false,
          source: new ol.source.TileWMS({
            url: 'http://127.0.0.1:8181/geoserver/lfhazard/wms',
            params: {'FORMAT': format, 
                     'VERSION': '1.1.1',
                     tiled: true,
                  LAYERS: 'lfhazard:Kriging_LT-475_Utah_PB_CSR_2008',
                  STYLES: '',
            }
          })
        });

  var SSD_Cetin = new ol.layer.Tile({
          visible: false,
          source: new ol.source.TileWMS({
            url: 'http://127.0.0.1:8181/geoserver/lfhazard/wms',
            params: {'FORMAT': format, 
                     'VERSION': '1.1.1',
                     tiled: true,
                  LAYERS: 'lfhazard:Kriging_SSD-475_Utah_Cetin_percent2008',
                  STYLES: '',
            }
          })
        });

  var SSD_IY = new ol.layer.Tile({
          visible: false,
          source: new ol.source.TileWMS({
            url: 'http://127.0.0.1:8181/geoserver/lfhazard/wms',
            params: {'FORMAT': format, 
                     'VERSION': '1.1.1',
                     tiled: true,
                  LAYERS: 'lfhazard:Kriging_SSD-475_Utah_IandY_percent2008',
                  STYLES: '',
            }
          })
        });

  var SSD_RandS = new ol.layer.Tile({
          visible: false,
          source: new ol.source.TileWMS({
            url: 'http://127.0.0.1:8181/geoserver/lfhazard/wms',
            params: {'FORMAT': format, 
                     'VERSION': '1.1.1',
                     tiled: true,
                  LAYERS: 'lfhazard:Kriging_SSD-475_Utah_PB_Seismic_Slope_Disp_RandS2008',
                  STYLES: '',
            }
          })
        });

  var SSD_BandT = new ol.layer.Tile({
          visible: false,
          source: new ol.source.TileWMS({
            url: 'http://127.0.0.1:8181/geoserver/lfhazard/wms',
            params: {'FORMAT': format, 
                     'VERSION': '1.1.1',
                     tiled: true,
                  LAYERS: 'Kriging_SSD-475_Utah_PB_Seismic_Slope_Disp_BandT2008',
                  STYLES: '',
            }
          })
        });


  map.on('singleclick', function(evt) {
          var view = map.getView();
          var viewResolution = view.getResolution();

          var source_LS = LS.getSource();
          var source_LT_Nreq = LT_Nreq.getSource();
          var source_LT_CSR = LT_CSR.getSource();
          var source_SSD_Cetin = SSD_Cetin.getSource();
          var source_SSD_IY = SSD_IY.getSource();
          var source_SSD_RandS = SSD_RandS.getSource();
          var source_SSD_BandT = SSD_BandT.getSource();

          var url_LS = source_LS.getGetFeatureInfoUrl(
            evt.coordinate, viewResolution, view.getProjection(),
            {'INFO_FORMAT': 'application/json', 'FEATURE_COUNT': 50});
          var url_LT_Nreq = source_LT_Nreq.getGetFeatureInfoUrl(
            evt.coordinate, viewResolution, view.getProjection(),
            {'INFO_FORMAT': 'application/json', 'FEATURE_COUNT': 50});
          var url_LT_CSR = source_LT_CSR.getGetFeatureInfoUrl(
            evt.coordinate, viewResolution, view.getProjection(),
            {'INFO_FORMAT': 'application/json', 'FEATURE_COUNT': 50});
          var url_SSD_Cetin = source_SSD_Cetin.getGetFeatureInfoUrl(
            evt.coordinate, viewResolution, view.getProjection(),
            {'INFO_FORMAT': 'application/json', 'FEATURE_COUNT': 50});
          var url_SSD_IY = source_SSD_IY.getGetFeatureInfoUrl(
            evt.coordinate, viewResolution, view.getProjection(),
            {'INFO_FORMAT': 'application/json', 'FEATURE_COUNT': 50});
          var url_SSD_RandS = source_SSD_RandS.getGetFeatureInfoUrl(
            evt.coordinate, viewResolution, view.getProjection(),
            {'INFO_FORMAT': 'application/json', 'FEATURE_COUNT': 50});
          var url_SSD_BandT = source_SSD_BandT.getGetFeatureInfoUrl(
            evt.coordinate, viewResolution, view.getProjection(),
            {'INFO_FORMAT': 'application/json', 'FEATURE_COUNT': 50});

          var coor_dict = {};
          $.getJSON(url_LS, function(data) {coor_dict["LS"]=data.features[0].properties.GRAY_INDEX});
          $.getJSON(url_LT_Nreq, function(data) {alert(data.features[0].properties.GRAY_INDEX)});
          $.getJSON(url_LT_CSR, function(data) {alert(data.features[0].properties.GRAY_INDEX)});
          $.getJSON(url_SSD_Cetin, function(data) {alert(data.features[0].properties.GRAY_INDEX)});
          $.getJSON(url_SSD_IY, function(data) {alert(data.features[0].properties.GRAY_INDEX)});
          $.getJSON(url_SSD_RandS, function(data) {alert(data.features[0].properties.GRAY_INDEX)});
          $.getJSON(url_SSD_BandT, function(data) {alert(data.features[0].properties.GRAY_INDEX)});

          console.log(url_LS);
  });
});