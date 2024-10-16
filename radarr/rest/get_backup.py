import requests
import json 
import argparse
import sys
import os

#local imports
#get parent dir path
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__),'..','..')))
from auth.serverinfo import ServerInfo

def main():
    #setup url and rest calls
    rest_url = server_info['url']
    rest_call = {
        "backups":f"{constants['api']}/system/backup",
    }

    #get backups
    bks = requests.get(
        url=f"{rest_url}/{rest_call['backups']}",
        headers=headers
    )


    #check if the backups were found
    if bks.status_code != 200:
        print(f"Error: [{bks.status_code}]-{bks.reason}")
        return
    else:
        bks = bks.json()

    #get most recent backup first element in list (LIFO)
    path = bks[0]['path']
    filename = path.split('/')[-1]
    download = requests.get(
        url=f"{rest_url}{path}",
        headers=headers,
        stream=True
    )
    
    #write to destination file(will be the root dir of this project unless explicitly changed)
    with open(filename,'wb') as outfile:
        for chunk in download.iter_content(chunk_size=512):
            if chunk:
                outfile.write(chunk)
    

if __name__ == "__main__":
    #server info is a static class which should contain a url and key
    server_info = ServerInfo.getRadarr()
    api_token = server_info['key'] 
    headers={"Authorization":f"Bearer {api_token}"}

    constants = {"radarrPageSize":{"pageSize":100},"api":"api/v3"}
    main()