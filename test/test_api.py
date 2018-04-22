import json
import unittest
from planet.api import PlanetApi

class TestApi(unittest.TestCase):
  config = json.load(open('config.json'))
  search_request = {
    "interval": "day",
    "item_types": ['REOrthoTile'],  # ["PSOrthoTile"],
    "filter": {
      "type": "AndFilter",
      "config": [
        {
          "type": "GeometryFilter",
          "field_name": "geometry",
          "config": {
            "type": "Polygon",
            "coordinates": [
              [
                [-122.46171355247498, 37.80017965728568],
                [-122.45639204978943, 37.80017965728568],
                [-122.45639204978943, 37.803723135087566],
                [-122.46171355247498, 37.803723135087566],
                [-122.46171355247498, 37.80017965728568]

              ]
            ]
          }
        },
        {
          "type": "AndFilter",
          "config": [
            {
              "type": "PermissionFilter",
              "config": ["assets:download"]
            }
          ]
        }
      ]
    }
  }
  assets_link = 'https://api.planet.com/data/v1/item-types/REOrthoTile/items/20180402_190716_1056516_RapidEye-4/assets/'
  analytic_asset_link = 'https://api.planet.com/data/v1/assets/eyJpIjogIjIwMTgwNDAyXzE5MDcxNl8xMDU2NTE2X1JhcGlkRXllLTQiLCAiYyI6ICJSRU9ydGhvVGlsZSIsICJ0IjogImFuYWx5dGljIiwgImN0IjogIml0ZW0tdHlwZSJ9'

  def test_postStatsRequest(self):
    api = PlanetApi(self.config["PLANET_API_KEY"])
    res = api.postStatsRequests(self.search_request)
    #Response was returned successfully
    self.assertEqual(res.status_code, 200)
    #Response had the expected structure
    r = res.json()
    self.assertTrue(r['interval'])
    self.assertTrue((r['buckets']))
    self.assertTrue(r['buckets'][0]['count'])
    self.assertTrue(r['buckets'][0]['start_time'])

  def test_postSearchRequest(self):
    api = PlanetApi(self.config["PLANET_API_KEY"])
    res = api.postSearchRequest(self.search_request)
    # Response was returned successfully
    self.assertEqual(res.status_code, 200)
    # Response had the expected structure
    r = res.json()
    self.assertTrue(r["type"])
    self.assertTrue(r["_links"])
    self.assertTrue(r["_links"]["_self"])
    self.assertTrue(r["_links"]["_next"])
    self.assertTrue(r["_links"]["_first"])
    self.assertTrue(r["features"])
    self.assertTrue(r["features"][0]["properties"])
    self.assertTrue(r["features"][0]["properties"]["catalog_id"])
    self.assertTrue(r["features"][0]["properties"]["usable_data"] is not None)
    self.assertTrue(r["features"][0]["properties"]["pixel_resolution"])
    self.assertTrue(r["features"][0]["properties"]["rows"])
    self.assertTrue(r["features"][0]["properties"]["published"])
    self.assertTrue(r["features"][0]["properties"]["acquired"])
    self.assertTrue(r["features"][0]["properties"]["sun_azimuth"])
    self.assertTrue(r["features"][0]["properties"]["provider"])
    self.assertTrue(r["features"][0]["properties"]["item_type"])
    self.assertTrue(r["features"][0]["properties"]["anomalous_pixels"])
    self.assertTrue(r["features"][0]["properties"]["view_angle"])
    self.assertTrue(r["features"][0]["properties"]["black_fill"] is not None)
    self.assertTrue(r["features"][0]["properties"]["origin_y"])
    self.assertTrue(r["features"][0]["properties"]["gsd"])
    self.assertTrue(r["features"][0]["properties"]["origin_x"])
    self.assertTrue(r["features"][0]["properties"]["columns"])
    self.assertTrue(r["features"][0]["properties"]["epsg_code"])
    self.assertTrue(r["features"][0]["properties"]["strip_id"])
    self.assertTrue(r["features"][0]["properties"]["updated"])
    self.assertTrue(r["features"][0]["properties"]["cloud_cover"] is not None)
    self.assertTrue(r["features"][0]["properties"]["satellite_id"])
    self.assertTrue(r["features"][0]["properties"]["ground_control"])
    self.assertTrue(r["features"][0]["properties"]["grid_cell"])
    self.assertTrue(r["features"][0]["properties"]["sun_elevation"])
    self.assertTrue(r["features"][0]["_permissions"] is not None)
    self.assertTrue(r["features"][0]["_links"])
    self.assertTrue(r["features"][0]["_links"]["_self"])
    self.assertTrue(r["features"][0]["_links"]["assets"])
    self.assertTrue(r["features"][0]["_links"]["thumbnail"])
    self.assertTrue(r["features"][0]["geometry"])
    self.assertTrue(r["features"][0]["geometry"]["type"])
    self.assertTrue(r["features"][0]["geometry"]["coordinates"])
    self.assertTrue(r["features"][0]["geometry"]["coordinates"][0])
    self.assertTrue(r["features"][0]["id"])
    self.assertTrue(r["features"][0]["type"])

  def test_getAllAssets(self):
    api = PlanetApi(self.config["PLANET_API_KEY"])
    res = api.getAllAssets(self.assets_link)
    # Response was returned successfully
    self.assertEqual(res.status_code, 200)
    # Response had the expected structure
    r = res.json()
    self.assertTrue(r["analytic"])
    self.assertTrue(r["analytic"]["_links"])
    self.assertTrue(r["analytic"]["_links"]["_self"])
    self.assertTrue(r["analytic"]["_links"]["activate"])
    self.assertTrue(r["analytic"]["_links"]["type"])
    self.assertTrue(r["analytic"]["_permissions"])
    self.assertTrue(r["analytic"]["_permissions"][0])
    self.assertTrue(r["analytic"]["expires_at"])
    self.assertTrue(r["analytic"]["location"])
    self.assertTrue(r["analytic"]["md5_digest"])
    self.assertTrue(r["analytic"]["status"])
    self.assertTrue(r["analytic"]["type"])
    #The following asset type have same structure as analytic
    self.assertTrue(r["analytic_xml"])
    self.assertTrue(r["visual"])
    self.assertTrue(r["visual_xml"])
    self.assertTrue(["udm"])

  def test_getActivationStatus(self):
    api = PlanetApi(self.config["PLANET_API_KEY"])
    res = api.getAllAssets(self.analytic_asset_link)
    # Response was returned successfully
    self.assertEqual(res.status_code, 200)
    # Response had the expected structure
    r = res.json()
    self.assertTrue(r["_links"])
    self.assertTrue(r["_links"]["_self"])
    self.assertTrue(r["_links"]["activate"])
    self.assertTrue(r["_links"]["type"])
    self.assertTrue(r["_permissions"])
    self.assertTrue(r["_permissions"][0])
    self.assertTrue(r["expires_at"])
    self.assertTrue(r["location"])
    self.assertTrue(r["md5_digest"])
    self.assertTrue(r["type"])
    self.assertTrue(r["status"])
    #Check the Status
    self.assertTrue(r["status"] in ('active',))


if __name__ == '__main__':
    unittest.main()