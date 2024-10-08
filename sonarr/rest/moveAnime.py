import requests
import json 
from itertools import islice
import argparse

"""
    This script goes out to radarr, grabs missing movies and searches for them again
    Search can be limited with search with the specify_str variable(to be changed to argument parser)
"""
def main():
    #setup url and rest calls
    rest_url = ""
    rest_call = {
        "series":f"{constants['api']}/series",
        "editor":f"{constants['api']}/series/editor"
    }

    #get movies in missing status
    series = requests.get(
        url=f"{rest_url}/{rest_call['series']}",
        #params=constants["radarrPageSize"],
        headers=headers
    )
    
    #check if the movie was found
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
    """CONSTANT GLOBALS
       api_token- token from radarr -> settings -> general-> API Key
       headers- uses api_token for auth
    """
    api_token = ""
    headers={"Authorization":f"Bearer {api_token}"}

    """CONSTANTS
       radarrpagesize- defines how many missing movies are returned per page
                       pageSize is the actual parameter that radarr's rest api needs
       api- radarr's constant rest api path
    """
    constants = {"radarrPageSize":{"pageSize":100},"api":"api/v3",'path':'/tv/anime'}

    """FILTER CONSTANTS
       usage would be <exec> get_missing.py -f[--filter] 'optional movie filter' 
       specify-str: this will filter out movies without this title 
    """
    """parser = argparse.ArgumentParser(description="A script to automate ur downloads")
    parser.add_argument('-f','--filter',required=False,default=None)
    args = parser.parse_args()
    specify_str = args.filter"""
    main()