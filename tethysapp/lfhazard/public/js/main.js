
var map_gizmo;
var overlay;
/**
       * Elements that make up the popup.
       */
      var container = document.getElementById('popup');
      var content = document.getElementById('popup-content');
      var closer = document.getElementById('popup-closer');

$( document ).ready(function() {
console.log( "ready!" );
    map_gizmo = TETHYS_MAP_VIEW.getMap();
     overlay = new ol.Overlay(/** @type {olx.OverlayOptions} */ ({
        element: container,
        autoPan: true,
        autoPanAnimation: {
          duration: 250
        }
      }));
    map_gizmo.overlays= [overlay]
    map_gizmo.on('singleclick', function(evt) {
//        alert("123");
        var coordinate = evt.coordinate;

        var hdms = ol.coordinate.toStringHDMS(ol.proj.transform(
            coordinate, 'EPSG:3857', 'EPSG:4326'));
        console.log(coordinate);
        content.innerHTML = '<p>You clicked here:</p><code>' + hdms +
            '</code>';

        overlay.setPosition(coordinate);
      });
    closer.onclick = function() {
        overlay.setPosition(undefined);
        closer.blur();
        return false;
      };
});




      /**
       * Create an overlay to anchor the popup to the map.
       */



      /**
       * Add a click handler to hide the popup.
       * @return {boolean} Don't follow the href.
       */



//      /**
//       * Create the map.
//       */
//      var map = new ol.Map({
//        layers: [
//          new ol.layer.Tile({
//            source: new ol.source.TileJSON({
//              url: 'https://api.tiles.mapbox.com/v3/mapbox.natural-earth-hypso-bathy.json?secure',
//              crossOrigin: 'anonymous'
//            })
//          })
//        ],
//        overlays: [overlay],
//        target: 'map',
//        view: new ol.View({
//          center: [0, 0],
//          zoom: 2
//        })
//      });


      /**
       * Add a click handler to the map to render the popup.
       */
