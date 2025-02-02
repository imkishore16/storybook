import json
import requests
import re
import urllib.parse

def _extractBingImages(html):
    pattern = r'mediaurl=(.*?)&amp;.*?expw=(\d+).*?exph=(\d+)'
    matches = re.findall(pattern, html)
    result = []

    for match in matches:
        url, width, height = match
        if url.endswith('.jpg') or url.endswith('.png') or url.endswith('.jpeg'):
            result.append({'url': urllib.parse.unquote(url), 'width': int(width), 'height': int(height)})

    return result


def _extractGoogleImages(html):
  images = []
  regex = re.compile(r"AF_initDataCallback\({key: 'ds:1', hash: '2', data:(.*?), sideChannel: {}}\);")
  match = regex.search(html)
  print()
  if match:
      print("2")
      dz = json.loads(match.group(1))         
      for c in dz[56][1][0][0][1][0]:
          try:
              thing = list(c[0][0].values())[0]
              images.append(thing[1][3])
          except:
              pass
  return images

#  returns a list of urls
# eg: [{'url': 'https://airandspace.si.edu/sites/default/files/images/editoral-stories/thumbnails/rocket-launch-67720_1920.jpg', 'width': 
# 1175, 'height': 1920}]
def getBingImages(query, retries=5):
    query = query.replace(" ", "+")
    images = []
    tries = 0
    while(len(images) == 0 and tries < retries):
        response = requests.get(f"https://www.bing.com/images/search?q={query}&first=1")
        if(response.status_code == 200):
            print(response.text)
            images = _extractBingImages(response.text)
        else:
            print("Error While making bing image searches", response.text)
            raise Exception("Error While making bing image searches")
    if(images):
        return images
    raise Exception("Error While making bing image searches")


def extract_data(html_content):
    regex = re.compile(r"AF_initDataCallback\({key: 'ds:1', hash: '2', data:(.*?), sideChannel: {}}\);")
    match = regex.search(html_content)
    if match:
        data = match.group(1)
        # Process the extracted data as needed
        print(data)
    else:
        print("No match found")


if __name__=="__main__":
    print("streted")
    response=getBingImages("rocket taking of")
    # print(response[0].get("url"))
    
    