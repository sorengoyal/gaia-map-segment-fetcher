import json
import unittest
from planet.api import PlanetApi
import config

class TestApi(unittest.TestCase):
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
    assets = {
        "analytic": {
          "_links": {
            "_self": "https://api.planet.com/data/v1/assets/eyJpIjogIjIwMTgwNDAyXzE5MDcxNl8xMDU2NTE2X1JhcGlkRXllLTQiLCAiYyI6ICJSRU9ydGhvVGlsZSIsICJ0IjogImFuYWx5dGljIiwgImN0IjogIml0ZW0tdHlwZSJ9",
            "activate": "https://api.planet.com/data/v1/assets/eyJpIjogIjIwMTgwNDAyXzE5MDcxNl8xMDU2NTE2X1JhcGlkRXllLTQiLCAiYyI6ICJSRU9ydGhvVGlsZSIsICJ0IjogImFuYWx5dGljIiwgImN0IjogIml0ZW0tdHlwZSJ9/activate",
            "type": "https://api.planet.com/data/v1/asset-types/analytic"
          },
          "_permissions": [
            "download"
          ],
          "expires_at": "2018-04-22T23:39:24.297779",
          "location": "https://api.planet.com/data/v1/download?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzVSt0eTY2YWZlNWtBNWtvYnBMVG5EUG5MS3UzaWtkeC80UTUxdXJWQnc1RGFHS29hdDlOcUtWdnpvei9oY1BubkliUkhRdFJFbUF3ZzZDMmtFTUpmZz09IiwiaXRlbV90eXBlX2lkIjoiUkVPcnRob1RpbGUiLCJ0b2tlbl90eXBlIjoidHlwZWQtaXRlbSIsImV4cCI6MTUyNDQ0MDM2NCwiaXRlbV9pZCI6IjIwMTgwNDAyXzE5MDcxNl8xMDU2NTE2X1JhcGlkRXllLTQiLCJhc3NldF90eXBlIjoiYW5hbHl0aWMifQ.8tYUJRLs8pfxwxuZjcBIKhnnhYwIeXvwoANEdaY7kDQtP1APKCIf9lNb3RwKRzNpn1XF8POvm2r-fZINkdUpuQ",
          "md5_digest": "f4ef058a97b8dbcf373d1ece39bb01c2",
          "status": "active",
          "type": "analytic"
        },
        "analytic_xml": {
          "_links": {
            "_self": "https://api.planet.com/data/v1/assets/eyJpIjogIjIwMTgwNDAyXzE5MDcxNl8xMDU2NTE2X1JhcGlkRXllLTQiLCAiYyI6ICJSRU9ydGhvVGlsZSIsICJ0IjogImFuYWx5dGljX3htbCIsICJjdCI6ICJpdGVtLXR5cGUifQ",
            "activate": "https://api.planet.com/data/v1/assets/eyJpIjogIjIwMTgwNDAyXzE5MDcxNl8xMDU2NTE2X1JhcGlkRXllLTQiLCAiYyI6ICJSRU9ydGhvVGlsZSIsICJ0IjogImFuYWx5dGljX3htbCIsICJjdCI6ICJpdGVtLXR5cGUifQ/activate",
            "type": "https://api.planet.com/data/v1/asset-types/analytic_xml"
          },
          "_permissions": [
            "download"
          ],
          "expires_at": "2018-04-22T23:39:24.300622",
          "location": "https://api.planet.com/data/v1/download?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJPZUJESDNmM1RMODRyYWZqbzZ3ZTBVVyt2MUh5SUVUakxWdXlGQ0JWdEtYQ0N5MUtzTWhGTGFQMHM1WUt0Q0MvSVI1Nk9GRDNwZTZEZFUra2Rnc0R5dz09IiwiaXRlbV90eXBlX2lkIjoiUkVPcnRob1RpbGUiLCJ0b2tlbl90eXBlIjoidHlwZWQtaXRlbSIsImV4cCI6MTUyNDQ0MDM2NCwiaXRlbV9pZCI6IjIwMTgwNDAyXzE5MDcxNl8xMDU2NTE2X1JhcGlkRXllLTQiLCJhc3NldF90eXBlIjoiYW5hbHl0aWNfeG1sIn0.h20yaRo7R4g63ySBVPWhhjPfwkOKbsmcCWmOYHStM0a0KSERPaSylZH5B7i99t5MlCArO7cPwy4Y6WWKRlsaRw",
          "md5_digest": "d34818b95d0001d3f3e8ea7ba39bfadf",
          "status": "active",
          "type": "analytic_xml"
        },
        "udm": {
          "_links": {
            "_self": "https://api.planet.com/data/v1/assets/eyJpIjogIjIwMTgwNDAyXzE5MDcxNl8xMDU2NTE2X1JhcGlkRXllLTQiLCAiYyI6ICJSRU9ydGhvVGlsZSIsICJ0IjogInVkbSIsICJjdCI6ICJpdGVtLXR5cGUifQ",
            "activate": "https://api.planet.com/data/v1/assets/eyJpIjogIjIwMTgwNDAyXzE5MDcxNl8xMDU2NTE2X1JhcGlkRXllLTQiLCAiYyI6ICJSRU9ydGhvVGlsZSIsICJ0IjogInVkbSIsICJjdCI6ICJpdGVtLXR5cGUifQ/activate",
            "type": "https://api.planet.com/data/v1/asset-types/udm"
          },
          "_permissions": [
            "download"
          ],
          "expires_at": "2018-04-22T23:39:24.302792",
          "location": "https://api.planet.com/data/v1/download?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtZGlGTC9PUlk1S2ZYdjZrbUR3b1VtME1rdVRCVks4djUvYXVhcXMxYjdtU0lMd3FSaC9kZlhjcW5IK2ZvR29EWENzcGk1T1Q2c2ZMTmJBQ3R4Q3hGZz09IiwiaXRlbV90eXBlX2lkIjoiUkVPcnRob1RpbGUiLCJ0b2tlbl90eXBlIjoidHlwZWQtaXRlbSIsImV4cCI6MTUyNDQ0MDM2NCwiaXRlbV9pZCI6IjIwMTgwNDAyXzE5MDcxNl8xMDU2NTE2X1JhcGlkRXllLTQiLCJhc3NldF90eXBlIjoidWRtIn0.2eLh_dBpmugHnshiscu4IkFCZw4SfKYkcqlfrORIVVFEgiTYr2MSQ0clT6yl8SoSFoxYi5ARAxlSC8ew1F3UMQ",
          "md5_digest": "fae12057d8f96017f39fc155d8c7110a",
          "status": "active",
          "type": "udm"
        },
        "visual": {
          "_links": {
            "_self": "https://api.planet.com/data/v1/assets/eyJpIjogIjIwMTgwNDAyXzE5MDcxNl8xMDU2NTE2X1JhcGlkRXllLTQiLCAiYyI6ICJSRU9ydGhvVGlsZSIsICJ0IjogInZpc3VhbCIsICJjdCI6ICJpdGVtLXR5cGUifQ",
            "activate": "https://api.planet.com/data/v1/assets/eyJpIjogIjIwMTgwNDAyXzE5MDcxNl8xMDU2NTE2X1JhcGlkRXllLTQiLCAiYyI6ICJSRU9ydGhvVGlsZSIsICJ0IjogInZpc3VhbCIsICJjdCI6ICJpdGVtLXR5cGUifQ/activate",
            "type": "https://api.planet.com/data/v1/asset-types/visual"
          },
          "_permissions": [
            "download"
          ],
          "expires_at": "2018-04-22T23:39:24.299552",
          "location": "https://api.planet.com/data/v1/download?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2bHFpZ2JReDI1MEpaL0M3dWQxOC90d1RsTWNKVDdyWTNSaUZqV2MvdFdvQUVtOEFLcnFZMzhZVFpQUmhDTkw2U3ZRNkliMXVqS0FoNkZjMlJORXpPUT09IiwiaXRlbV90eXBlX2lkIjoiUkVPcnRob1RpbGUiLCJ0b2tlbl90eXBlIjoidHlwZWQtaXRlbSIsImV4cCI6MTUyNDQ0MDM2NCwiaXRlbV9pZCI6IjIwMTgwNDAyXzE5MDcxNl8xMDU2NTE2X1JhcGlkRXllLTQiLCJhc3NldF90eXBlIjoidmlzdWFsIn0.GtNkrAxM30uQvLhv4OsrfxQSEh32nVEQ8FrPeq706QyGweqlTPIdZlTUnWCu7vFj9wxpHKfjDV8Z_uVbpjunag",
          "md5_digest": "da6ad4fa7f61639edf606a9c7ea31ec8",
          "status": "active",
          "type": "visual"
        },
        "visual_xml": {
          "_links": {
            "_self": "https://api.planet.com/data/v1/assets/eyJpIjogIjIwMTgwNDAyXzE5MDcxNl8xMDU2NTE2X1JhcGlkRXllLTQiLCAiYyI6ICJSRU9ydGhvVGlsZSIsICJ0IjogInZpc3VhbF94bWwiLCAiY3QiOiAiaXRlbS10eXBlIn0",
            "activate": "https://api.planet.com/data/v1/assets/eyJpIjogIjIwMTgwNDAyXzE5MDcxNl8xMDU2NTE2X1JhcGlkRXllLTQiLCAiYyI6ICJSRU9ydGhvVGlsZSIsICJ0IjogInZpc3VhbF94bWwiLCAiY3QiOiAiaXRlbS10eXBlIn0/activate",
            "type": "https://api.planet.com/data/v1/asset-types/visual_xml"
          },
          "_permissions": [
            "download"
          ],
          "expires_at": "2018-04-22T23:39:24.301691",
          "location": "https://api.planet.com/data/v1/download?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJRNmlyMENObmhLd0t0NHpYN0xpNXhJRnN3eHFTdzBnUzNUYk5CejJCcEVRTU9lQnViNnZKNDhnOThrd0I5cTFrMlJDSkVLdnBKRm4xMWpkalgzTnVMdz09IiwiaXRlbV90eXBlX2lkIjoiUkVPcnRob1RpbGUiLCJ0b2tlbl90eXBlIjoidHlwZWQtaXRlbSIsImV4cCI6MTUyNDQ0MDM2NCwiaXRlbV9pZCI6IjIwMTgwNDAyXzE5MDcxNl8xMDU2NTE2X1JhcGlkRXllLTQiLCJhc3NldF90eXBlIjoidmlzdWFsX3htbCJ9.0ipR1gfOnH2yGJpWx7_1HiQaF0y895rYECUoFjBVlTV1HFFlokrGU9OZMX-757f0er9u7cqvFbRV2pNAkhcJDQ",
          "md5_digest": "d71635bfeac7a9fd4da765dc5606491c",
          "status": "active",
          "type": "visual_xml"
        }
      }
    assets_link = 'https://api.planet.com/data/v1/item-types/REOrthoTile/items/20180402_190716_1056516_RapidEye-4/assets/'
    analytic_asset_link = 'https://api.planet.com/data/v1/assets/eyJpIjogIjIwMTgwNDAyXzE5MDcxNl8xMDU2NTE2X1JhcGlkRXllLTQiLCAiYyI6ICJSRU9ydGhvVGlsZSIsICJ0IjogImFuYWx5dGljIiwgImN0IjogIml0ZW0tdHlwZSJ9'

    def test_postStatsRequest(self):
        """Verify the structure of the Response of a quick search requests"""
        api = PlanetApi(config.Planet_Api_Key)
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
        api = PlanetApi(config.Planet_Api_Key)
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

    def test_getAllAssetsInfo(self):
        api = PlanetApi(config.Planet_Api_Key)
        res = api.getAllAssetsInfo(self.assets_link)
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

    def test_postActivationRequest(self):
        api = PlanetApi(config.Planet_Api_Key)
        res = api.postActivationRequest(self.assets["analytic"]["_links"]["activate"])
        # Response was returned successfully
        self.assertTrue(res.status_code == 202 or res.status_code == 204)

    def test_getActivationStatus(self):
        api = PlanetApi(config.Planet_Api_Key)
        res = api.getAllAssetsInfo(self.analytic_asset_link)
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

    def test_downloadAsset(self):
        api = PlanetApi(config.Planet_Api_Key)
        asset_info = api.getAllAssetsInfo(self.assets_link)
        asset_info_json = asset_info.json()
        res = api.downloadAsset(asset_info_json["visual_xml"]["location"])
        #As long as downloadAsset() does not geenrate any erros we are good

    def suite(self):
        return unittest.makeSuite(TestApi, 'test')

if __name__ == '__main__':
    unittest.main()