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


def convert_time_between_offsets(datetime_str, from_offset=2, to_offset=7):
    date = datetime.fromisoformat(datetime_str.rstrip('Z'))
    new_date = date + timedelta(hours=to_offset)

    return new_date
