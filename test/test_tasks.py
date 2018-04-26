import json
import time
import unittest
import config
from planet.tasks import *

class TestTasks(unittest.TestCase):
    data = {
        "_links": {
            "_self": "https://api.planet.com/data/v1/item-types/REOrthoTile/items/20180402_190716_1056516_RapidEye-4",
            "_activate": "https://api.planet.com/data/v1/item-types/REOrthoTile/items/20180402_190716_1056516_RapidEye-4/assets/",
            "_type": "https://api.planet.com/data/v1/item-types/REOrthoTile/items/20180402_190716_1056516_RapidEye-4/thumb"
        },
        "location": "https:\/\/api.planet.com\/data\/v1\/item-types\/REOrthoTile\/items\/20180402_190716_1056516_RapidEye-4",
        "asset_type": "analytic",
        "md5_digest": "",
        "geometry": {
            "coordinates": [
                [
                    [
                        -122.44801834858,
                        37.943201162957
                    ],
                    [
                        -122.4496384,
                        37.7254832
                    ],
                    [
                        -122.51471001539,
                        37.725708495275
                    ],
                    [
                        -122.46353852344,
                        37.892588010461
                    ],
                    [
                        -122.44801834858,
                        37.943201162957
                    ]
                ]
            ],
            "type": "Polygon"
        },
        "id": "20180402_190716_1056516_RapidEye-4",
        "properties": {
            "acquired": "2018-04-02T19:07:16Z",
            "anomalous_pixels": 0.9,
            "black_fill": 0.9,
            "catalog_id": "35712133",
            "cloud_cover": 0,
            "columns": 5000,
            "epsg_code": 32610,
            "grid_cell": "1056516",
            "ground_control": True,
            "gsd": 6.5,
            "item_type": "REOrthoTile",
            "origin_x": 523500,
            "origin_y": 4200500,
            "pixel_resolution": 5,
            "provider": "rapideye",
            "published": "2018-04-04T15:49:18Z",
            "rows": 5000,
            "satellite_id": "RapidEye-4",
            "strip_id": "35712123",
            "sun_azimuth": 150.87112,
            "sun_elevation": 54.10796,
            "updated": "2018-04-04T15:49:18Z",
            "usable_data": 0.1,
            "view_angle": -9.82855
        },
        "type": "segment"
    }
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

    def test_writeToS3(self):
        data = "Test data written by a dev"
        bucketname = config.Resources["dev"]["s3"]["bucket"]
        t = time.localtime()
        filename = 'test-%d-%d-%d %d:%d.dat' % (t.tm_year,t.tm_mon,t.tm_mday,t.tm_hour,t.tm_min)
        key = config.Resources["dev"]["s3"]["folder"] + filename
        writeToS3(data, bucketname, key)

    def test_makeEntryIntoRds(self):
        host = config.Resources["dev"]["rds"]["host"]
        port = config.Resources["dev"]["rds"]["port"]
        user = config.Resources["dev"]["rds"]["user"]
        password = config.Resources["dev"]["rds"]["password"]
        db = config.Resources["dev"]["rds"]["db"]
        makeEntryIntoRds(self.data, host, port, user, password, db)

    def test_getMapSegment(self):
        image = getMapSegment(self.search_request, "visual_xml", config.Planet_Api_Key)
        with open("image.jpg", "w") as f:
            f.write(image)

