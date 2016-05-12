import json
import urllib2

locu_key = 'f84c1ddef4547856d4915ae4c3eac481388b1a92';

def locu_search(query, category):
  api_key = locu_key
  url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
  final_url = url + "&locality="+ query +"&category=" + category
  json_obj = urllib2.urlopen(final_url)
  data = json.load(json_obj)

  for item in data['objects']:
    print item['name'], item['phone']


if __name__ == "__main__":
  locu_search('Polanco' , 'restaurant')