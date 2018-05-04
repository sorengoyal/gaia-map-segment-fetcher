import unittest
import config
from lambda_function import lambda_handler

class TestLambda(unittest.TestCase):
    event = {
        "Records": [
            {
                "EventVersion": "1.0",
                "EventSubscriptionArn": "arn:aws:sns:EXAMPLE",
                "EventSource": "aws:sns",
                "Sns": {
                    "SignatureVersion": "1",
                    "Timestamp": "2018-05-02T00:00:00.000Z",
                    "Signature": "EXAMPLE",
                    "SigningCertUrl": "EXAMPLE",
                    "MessageId": "95df01b4-ee98-5cb9-9903-4c221d41eb5e",
                    "Message": {
                        "image_type": "visual",
                        "search_request": {
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
                                                "type": "DateRangeFilter",
                                                "field_name": "acquired",
                                                "config": {
                                                    "gte": "2018-02-04T00:00:00.000Z",
                                                    "lte": "2018-05-04T00:00:00.000Z"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    },
                    "MessageAttributes": {
                        "Test": {
                            "Type": "String",
                            "Value": "TestString"
                        },
                        "TestBinary": {
                            "Type": "Binary",
                            "Value": "TestBinary"
                        }
                    },
                    "Type": "Notification",
                    "UnsubscribeUrl": "EXAMPLE",
                    "TopicArn": "arn:aws:sns:EXAMPLE",
                    "Subject": "map-segment-requests"
                }
            }
        ]
    }
    context = {}
    def test_lambda_handler(self):
        lambda_handler(self.event, self.context)
        assert 1 == 1


