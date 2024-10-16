#use this as a template to securely re-use these creds, serverinfo.py is a part of gitignore
class ServerInfo:
    _server = {
        "sonarr_url":"",
        "radarr_url":"",
        "sonarr_api":"",
        "radarr_api":"",
    }
    @staticmethod
    def getSonarr():
        return {"url":ServerInfo._server['sonarr_url'],"key":ServerInfo._server['sonarr_api']}
    @staticmethod
    def getRadarr():
        return {"url":ServerInfo._server['radarr_url'],"key":ServerInfo._server['radarr_api']}