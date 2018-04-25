import json
import time

import boto3
import botocore

from .api import PlanetApi


def getMapSegment(search_request):
  api = PlanetApi()
  features = api.postSearchRequest(search_request).json()["requests"]
  if (len(features) == 0):
      raise Exception("No Items found for filter:\nResponse:\n" + json.dumps(features, indent=2))
  downloadable_features = [feature for feature in features if len(feature['_permissions']) != 0]
  feature = downloadable_features[-1]
  assets = api.getAllAssetsInfo(feature["_links"]["assets"])
  analytic_asset_activation_link = assets["analytic"]["_links"]["activate"]
  waitUntilActivation(api, analytic_asset_activation_link)
  image = api.downloadAsset(asset, aoi=coordinates)
  return image


def waitUntilActivation(api, asset_link):
  response = api.postActivationRequest(asset_link)
  if (not (response.status_code == 204 or response.status_code == 202)):
      raise Exception("Could not activate asset.\nResponse:\n" + json.dumps(response.json(), indent=2))
  #Status Codes
  #204 - Activation Request Posted
  #202 - Activation Successful
  status = response.status_code
  begin_time = time.time()
  while status == 204:
    time.sleep(1)
    response = api.postActivationRequest(asset_link)
    status = response.status_code
    if time.time() - begin_time > 20:
      raise Exception("Activation of asset taking too long.\n Last Response:\n" + json.dumps(response.json(), indent=2))
  if status != 202:
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

def makeEntryIntoRds():
  pass

def getAllTiffs(filters):
    with open('subarea.json', 'w') as file:
        geojson = {
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": filters[0]['config.json'][0]['config.json']['coordinates']
                }
            }]
        }
        file.write(json.dumps(geojson, indent=2))
    assets = []
    for i in range(0, 4):
        assets.append(planetGetAssets(filters[i])['_links']['assets'])
        result = requests.get(assets[i],
                              auth=HTTPBasicAuth(API_KEY, '')
                              )
        result = result.json()
        response = requests.post(result['analytic']['_links']['activate'],
                                 auth=HTTPBasicAuth(API_KEY, ''))
        if (response.status_code == 202 or response.status_code == 204):
            print('(getAllTiff)Sucess:Asset[' + str(i) + '] has been activated')
        else:
            print('(getAllTiff)Error:Response ' + str(response))
    downloaded = [False, False, False, False]
    tiffs = [0, 0, 0, 0]
    while (not downloaded[0] and not downloaded[1] and not downloaded[2] and not downloaded[3]):
        for i in range(0, 4):
            result = requests.get(assets[i],
                                  auth=HTTPBasicAuth(API_KEY, '')).json()
            if (result['analytic']['status'] == 'active' and not downloaded[i]):
                download_url = result['analytic']['location']
                vsicurl_url = '/vsicurl/' + download_url
                output_file = 'season_analytic_' + str(i) + '_subarea.tif'
                # GDAL Warp crops the image by our AOI, and saves it
                err = gdal.Warp(output_file, vsicurl_url, dstSRS='EPSG:4326', cutlineDSName='subarea.json',
                                cropToCutline=True)
                print("(getAllTiff)Sucess: Downloaded image of subarea:" + output_file)
                downloaded[i] = True
                tiffs[i] = err.ReadAsArray()
            else:
                print('(getAllTiff) Message: Asset[' + str(i) + '] is ' + result['analytic']['status'])
    return tiffs
