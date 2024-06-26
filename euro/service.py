import requests
import json
from datetime import datetime, timedelta


def getEuroGroup():
    url = "https://standings.uefa.com/v1/standings?competitionId=3&phase=TOURNAMENT&seasonYear=2024"

    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'no-cache',
        'origin': 'https://www.uefa.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.uefa.com/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-api-key': 'ceeee1a5bb209502c6c438abd8f30aef179ce669bb9288f2d1cf2fa276de03f4'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)


def getEuroFormGuide(groupId):

    url = "https://match.uefa.com/v5/matches?competitionId=3&groupId=" + \
        groupId + "&limit=50&offset=0&order=ASC&seasonYear=2024"

    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'if-none-match': '"0cdbbda4bcf27370b9ce135dbd42ae18c"',
        'origin': 'https://www.uefa.com',
        'priority': 'u=1, i',
        'referer': 'https://www.uefa.com/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-api-key': 'ceeee1a5bb209502c6c438abd8f30aef179ce669bb9288f2d1cf2fa276de03f4'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)


def getEuroMatches():
    url = "https://match.uefa.com/v5/matches?competitionId=3&limit=55&offset=0&order=ASC&phase=ALL&seasonYear=2024&roundId=2001079"

    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'if-none-match': '"0e306ced558b916aace808e595d220fd2"',
        'origin': 'https://www.uefa.com',
        'priority': 'u=1, i',
        'referer': 'https://www.uefa.com/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-api-key': 'ceeee1a5bb209502c6c438abd8f30aef179ce669bb9288f2d1cf2fa276de03f4'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)


def getEuroMatch(matchid):
    url = "https://match.uefa.com/v5/matches?matchId=" + matchid

    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'if-none-match': '"0cef4b9d3549e56fda6abd751beb42a61"',
        'origin': 'https://www.uefa.com',
        'priority': 'u=1, i',
        'referer': 'https://www.uefa.com/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-api-key': 'ceeee1a5bb209502c6c438abd8f30aef179ce669bb9288f2d1cf2fa276de03f4'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)


def getEuroBraket():
    url = "https://match.uefa.com/v5/matches?competitionId=3&limit=55&matchType=FIRST_LEG%2CREPLAY%2CSECOND_LEG%2CSINGLE&offset=0&phase=TOURNAMENT&seasonYear=2024"

    payload = {}
    headers = {
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.uefa.com/',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-api-key': 'ceeee1a5bb209502c6c438abd8f30aef179ce669bb9288f2d1cf2fa276de03f4',
        'sec-ch-ua-platform': '"macOS"'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)


def getEuroTeam():
    url = "https://comp.uefa.com/v2/teams?competitionId=3&limit=55&offset=0&phase=ALL&seasonYear=2024"

    payload = {}
    headers = {
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.uefa.com/',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-api-key': 'ceeee1a5bb209502c6c438abd8f30aef179ce669bb9288f2d1cf2fa276de03f4',
        'sec-ch-ua-platform': '"macOS"'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)


def getEuroTeamStats():

    url = "https://compstats.uefa.com/v1/team-ranking?competitionId=3&limit=15&offset=0&optionalFields=PLAYER%2CTEAM&order=DESC&phase=TOURNAMENT&seasonYear=2024&stats=goals%2Cball_possession%2Cpasses_accuracy%2Cdribbling%2Ccorners%2Coffsides%2Crecovered_ball%2Ctackles%2Csaves%2Cclean_sheet%2Cfouls_committed%2Cyellow_cards%2Cred_cards"

    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'if-none-match': '"039483f88b0de58b4c12944f168727fe7"',
        'origin': 'https://www.uefa.com',
        'priority': 'u=1, i',
        'referer': 'https://www.uefa.com/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-api-key': 'ceeee1a5bb209502c6c438abd8f30aef179ce669bb9288f2d1cf2fa276de03f4'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)


def getEuroLineUp(matchid):
    url = "https://match.uefa.com/v5/matches/" + matchid + "/lineups"

    payload = {}
    headers = {
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.uefa.com/',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-api-key': 'ceeee1a5bb209502c6c438abd8f30aef179ce669bb9288f2d1cf2fa276de03f4',
        'sec-ch-ua-platform': '"macOS"'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)


def getEuroStatMatch(matchid):
    url = "https://matchstats.uefa.com/v1/team-statistics/" + matchid

    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'if-none-match': '"0e54de661b4cb4418a1b9901c054e5e8d"',
        'origin': 'https://www.uefa.com',
        'priority': 'u=1, i',
        'referer': 'https://www.uefa.com/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-api-key': 'ceeee1a5bb209502c6c438abd8f30aef179ce669bb9288f2d1cf2fa276de03f4'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)


def getEuroStatPlayerOfMatch(matchid, playerid):
    url = "https://matchstats.uefa.com/v1/player-statistics/" + \
        matchid + "?playerId=" + playerid

    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'no-cache',
        'origin': 'https://www.uefa.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.uefa.com/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-api-key': 'ceeee1a5bb209502c6c438abd8f30aef179ce669bb9288f2d1cf2fa276de03f4'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)


def getEuroEventLineUp(matchid):
    url = "https://match.uefa.com/v5/matches/" + matchid + \
        "/events?filter=LINEUP&limit=50&offset=0&order=DESC"

    payload = {}
    headers = {
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.uefa.com/',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-api-key': 'ceeee1a5bb209502c6c438abd8f30aef179ce669bb9288f2d1cf2fa276de03f4',
        'sec-ch-ua-platform': '"macOS"'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)


def convert_time_between_offsets(datetime_str, from_offset=2, to_offset=7):
    date = datetime.fromisoformat(datetime_str.rstrip('Z'))
    new_date = date + timedelta(hours=to_offset)

    return new_date


def get_complementary_color(hex_color):
    # Remove the hash if present
    hex_color = hex_color.lstrip('#')

    # Parse the hex color
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    # Compute the complementary color
    r = 255 - r
    g = 255 - g
    b = 255 - b

    # Convert back to hex and format the string
    complementary_color = f'#{r:02X}{g:02X}{b:02X}'

    return complementary_color
