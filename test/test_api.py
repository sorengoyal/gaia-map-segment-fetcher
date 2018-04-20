import unittest
from planet.api import PlanetApi

class TestApi(unittest.TestCase):
  search_request = {
    "interval": "day",
    "item_types": ['REOrthoTile'],  # ["PSOrthoTile"],
    "filter": {
      "type": "AndFilter",
      "config": [{
        "type":"GeometryFilter",
        "field_name":"geometry",
        "config":{
          "type":"Polygon",
          "coordinates":[
            [
              [ -5.788282155990601, 19.168407103123812],
              [-5.785256624221801, 19.168407103123812],
              [-5.785256624221801, 19.1703325524945],
              [-5.788282155990601, 19.1703325524945],
              [-5.788282155990601,19.168407103123812]
            ]
          ]
        }
      }]
    }
  }

  def test_postStatsRequest(self):
    api = PlanetApi('3d42933f4c284a3b8dd2c5200e97da00')
    res = api.postStatsRequests(self.search_request)
    #Response was returned successfully
    self.assertEqual(res.status_code, 200)
    #Response had the expected structure
    r = res.json()
    self.assertTrue(r['interval'])
    self.assertTrue((r['buckets']))
    self.assertTrue(r['buckets'][0]['count'])
    self.assertTrue(r['buckets'][0]['start_time'])

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()