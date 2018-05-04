import json
import time
import pymysql
import boto3
import botocore
from .api import PlanetApi


def getMapSegment(search_request, asset_type, api_key):
    api = PlanetApi(api_key)
    features = api.postSearchRequest(search_request).json()["features"]
    if (len(features) == 0):
        raise Exception("No Items found for filter:\nResponse:\n" + json.dumps(features, indent=2))
    downloadable_features = [feature for feature in features if len(feature['_permissions']) != 0]
    feature = downloadable_features[-1]
    assets_info = api.getAllAssetsInfo(feature["_links"]["assets"]).json()
    asset_activation_link = assets_info[asset_type]["_links"]["activate"]
    waitUntilActivation(api, asset_activation_link)
    assets_info = api.getAllAssetsInfo(feature["_links"]["assets"]).json() #Update the assets link
    image = api.downloadAsset(assets_info[asset_type]["location"])
    return {"feature": feature, "asset_type": asset_type}, image.content


def waitUntilActivation(api, asset_activation_link):
    response = api.postActivationRequest(asset_activation_link)
    if (not (response.status_code == 204 or response.status_code == 202)):
        raise Exception("Could not activate asset.\nResponse:\n" + json.dumps(response.json(), indent=2))
    #Status Codes
    #202 - Activation Request Posted
    #204 - Activation Successful
    status = response.status_code
    begin_time = time.time()
    while status == 202:
        time.sleep(1)
        response = api.postActivationRequest(asset_activation_link)
        status = response.status_code
        print("Response Code: %d, Link: %s" %(status, asset_activation_link))
        if time.time() - begin_time > 200:
            raise Exception("Activation of asset taking too long.\n Last Response:\n" + json.dumps(response.json(), indent=2))
    if status != 204:
        raise Exception("Error in Activating Request\n Response:\n" + json.dumps(response.json(), indent=2))


def writeToS3(data, bucketname, key):
    s3 = boto3.resource('s3')
    try:
        s3.meta.client.head_bucket(Bucket=bucketname)
    except botocore.exceptions.ClientError as e:
        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            print("Could not find the bucket: " + bucketname)
            raise e
    try:
        s3.Object(bucketname, key).put(Body=data)
    except Exception as e:
        raise e


def makeEntryIntoRds(data, host, port, user, password, db):
    conn = pymysql.connect(host, user=user, passwd=password, port=port, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute('Insert into %s.RawTileData (JSON) Values (\'%s\')' % (db,json.dumps(data)))
        conn.commit()
