import requests

# function to query Pulsedive
def queryPulsedive(key: str, query: str) -> tuple:
    r = requests.get(
            "https://pulsedive.com/api/info.php",
            params={"indicator": query, "pretty": "1", "key": key},
        )
    return (r.status_code, r.json())


# function to query VirusTotal
def queryVirusTotal(key: str, query: str) -> tuple:
    r = requests.get(
            "https://www.virustotal.com/api/v3/search",
            headers={"accept": "application/json", "x-apikey": key},
            params={"query": query},
        )
    return valVirusTotal((r.status_code, r.json()))

def valPulsedive(res: tuple[int, dict]) -> tuple[int, dict]:
    '''
    Function to return same tuple
    :param res: tuple (HTTP status code, request data in json)
    :return: same tuple
    '''
    return res

def valVirusTotal(res: tuple[int, dict]) -> tuple[int, dict]:
    if res[0] != 200:
        return (res[0], res[1]["error"]["message"])
    elif not res[1]["data"]:
        return (404, 'No matches found in VirusTotal database.')
    else:
        return (res[0], res[1])