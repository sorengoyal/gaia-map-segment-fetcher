import json
from planet.tasks import getMapSegment


# A sample event is in planet/samples/event.json
def lambda_handler(event, context):
    filter = event["filter"]
    print("Received event:\n" + json.dumps(event, indent=2))
    getMapSegment(filter)
    #raise Exception('Something went wrong')
