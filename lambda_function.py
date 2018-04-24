import json
from planet.tasks import getMapSegment
'''
event = {
"traceid": "",
"filter": {
  "type": "AndFilter",
  "config.json": [
    {
      "type":"GeometryFilter",
      "field_name":"geometry",
      "config.json":{
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
    },
    {
      "type":"AndFilter",
      "config.json":[{
        "type": "RangeFilter",
        "field_name": "cloud_cover",
        "config.json": {
          "gte": 0,
          "lte": 0.2
        }
      }]
    },
    {
      "type":"RangeFilter",
      "field_name":"sun_elevation",
      "config.json":{
        "gte":0,
        "lte":90
      }
    },
    {
      "type":"AndFilter",
      "config.json":[
        {
          "type":"DateRangeFilter",
          "field_name":"acquired",
          "config.json":{
            "gte":"2018-01-14T21:58:20.902Z",
            "lte":"2018-04-14T20:58:20.902Z"
          }
        }
      ]
    }
  ]
}
'''


def lambda_handler(event, context):
  filter = event["filter"]
  print("Received event:\n" + json.dumps(event, indent=2))
  getMapSegment(filter)
  #raise Exception('Something went wrong')
