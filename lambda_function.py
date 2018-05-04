import json
import config
from planet.tasks import *

Planet_Api_Key = config.Planet_Api_Key
env = "dev"
host = config.Resources[env]["rds"]["host"]
port = config.Resources[env]["rds"]["port"]
user = config.Resources[env]["rds"]["user"]
password = config.Resources[env]["rds"]["password"]
db = config.Resources[env]["rds"]["db"]
bucketname = config.Resources[env]["s3"]["bucket"]
folder = config.Resources[env]["s3"]["folder"]
# A sample event is in planet/samples/event.json
def lambda_handler(event, context):
    print("Received event:\n" + json.dumps(event, indent=2))
    search_request = event["Records"][0]["Sns"]["Message"]["search_request"]
    image_type = event["Records"][0]["Sns"]["Message"]["image_type"]
    segment_info, segment_data = getMapSegment(search_request, image_type, Planet_Api_Key)
    key = '%s/%s.tif' % (folder, segment_info["id"])
    writeToS3(segment_data, bucketname, key)
    makeEntryIntoRds(segment_data, host, port, user, password, db)