import requests
import json 
from itertools import islice
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
        "series":f"{constants['api']}/series",
        "editor":f"{constants['api']}/series/editor"
    }

    series = requests.get(
        url=f"{rest_url}/{rest_call['series']}",
        headers=headers
    )
    
    if series.status_code != 200:
        print(f"Error: [{series.status_code}]-{series.reason}")
        return
    else:
        series = series.json()

    all_anime = [show['id'] for show in series if "Anime" in show['genres']]
    print(all_anime)
    all_anime_info = {
        'seriesIds':all_anime,
        'rootFolderPath':f"{constants['path']}",
        'movieFiles':True
    }
    print(all_anime_info)
    req = requests.put(
        url=f"{rest_url}/{rest_call['editor']}",
        headers=headers,
        json=all_anime_info
    )
    
if __name__ == "__main__":

    server_info = ServerInfo.getSonarr()
    api_token = server_info['key']
    headers={"Authorization":f"Bearer {api_token}"}
    constants = {"radarrPageSize":{"pageSize":100},"api":"api/v3",'path':'/tv/anime'}
    main()