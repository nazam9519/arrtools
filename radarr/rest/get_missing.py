import requests
import json 

def main():
    rest_url = "<your url>"
    rest_call = {
        "missing":"api/v3/wanted/missing",
        "movie":"api/v3/movie",
        "command":"api/v3/command"
    }
    missing = radarr_req(
        path=f"{rest_url}/{rest_call['missing']}",
        params=constants["radarrPageSize"],
        method="GET"
    )
    if missing.status_code != 200:
        print(f"Error: [{missing.status_code}]-{missing.reason}")
        return
    else:
        missing = missing.json()
    x = [i for i in missing['records'] if "Godzilla" in i['title'] in i['title']]
    print(x)
    for i in x:        
        req = requests.post(
            url=f"{rest_url}/{rest_call['command']}",
            headers=headers,
            #params={"id":i['id']},
            json={"name":"MoviesSearch","movieIds":[i['id']]}
        )
        print(req.status_code)
        print(req.json())

def radarr_req(path: str,method: str,params:dict={})->requests.Request:
    return requests.request(
        method=method,
        url=path,
        headers=headers,
        params=params
    )

if __name__ == "__main__":
    api_token = "your api token"
    headers={"Authorization":f"Bearer {api_token}"}
    constants = {"radarrPageSize":{"pageSize":100},"api":"/api/v3"}
    main()
