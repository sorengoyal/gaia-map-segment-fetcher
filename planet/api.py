import requests
import json
from . import api_config

class PlanetApi:
  def __init__(self, api_key):
    self.API_KEY = api_key
    self.session = requests.session()
    self.session.auth = (api_key, '')
    self.endpoint = api_config
    self.endpoint = api_config.endpoints
  def __del__(self):
    self.session.close()
  '''
  search_request = {
      "interval": "day",
      "item_types": ['REOrthoTile'], #["PSOrthoTile"],
      "filter": filter #see filter.json
  }
  '''
  def postSearchRequest(self, search_request):
      res = self.session.post(self.endpoint["quick_search"], json=search_request)
      return res #.json()['features']
  ''' 
      search_request = {
          "interval": "day",
          "item_types": ['REOrthoTile'], #["PSOrthoTile"],
          "filter": filter #see filter.json
      }
  '''
  def postStatsRequests(self, search_request):
      res = self.session.post(self.endpoint["stats"], json=search_request)
      return res #.json()['features']
  '''
  asset_link - string (typically found in item['_links']['assets'])
  returns - a dict containing all the assets' properties
  '''
  def getAllAssets(self, asset_link):
      assets = self.session.get(asset_link)
      return assets.json()

  '''
  asset - a single asset of the item, should be dict containing the activation link
  Returns  -  response.status_code == 204 => activation requested posted, 202 => activation successful
  
  '''
  def postActivationRequest(self, asset):
      response = self.session.post(asset['_links']['activate'])
      return response

  '''
  Returns - a string 'Inactive', 'Activating', or 'Active'
  '''
  def getActivationStatus(self, asset):
      response = self.session.get(asset['_links']['_self'])
      return response.json()['status']

