import requests
import shutil
import json
import unicodedata
import re

globalurl = "http://www.funnystatusvideos.com/videostatus/"
globalpath = "F://video status//"
payload={}
headers = {
  'Cookie': '__cfduid=db107fae0231098d7f87024e7d7d7639a1608411416'
}
globalarray  = json.loads('[]')


def download_file(url,local_filename):
    #local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

def get_valid_filename(s):
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)



f = open("out.json", "r")

json_array = json.load(f,strict=False)
#print(json_array)

for item in json_array:
    print (item)
    name = item['name'] +' '+ item['category'] +' - '+item['subcategory']
    updatename = get_valid_filename(name)
    url = item['url']

    download_file(globalurl + url,updatename+".jpg")
    download_file(globalurl + url+".mp4",updatename+".mp4")
