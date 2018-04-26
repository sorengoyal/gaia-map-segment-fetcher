import json
import config
from planet.tasks import *

Planet_Api_Key = config.Planet_Api_Key
host = config.Resources["prod"]["rds"]["host"]
port = config.Resources["prod"]["rds"]["port"]
user = config.Resources["prod"]["rds"]["user"]
password = config.Resources["prod"]["rds"]["password"]
db = config.Resources["prod"]["rds"]["db"]
bucketname = config.Resources["prod"]["s3"]["bucket"]
folder = config.Resources["dev"]["s3"]["folder"]
# A sample event is in planet/samples/event.json
def lambda_handler(event, context):
    filter = event["filter"]
    print("Received event:\n" + json.dumps(event, indent=2))
    segment_info, segment_data = getMapSegment(filter, Planet_Api_Key)
    key = '%s/%s.tif' % (folder, segment_info["id"])
    writeToS3(segment_data, bucketname, key)
    makeEntryIntoRds(segment_data, host, port, user, password, db)