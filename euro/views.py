from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

import os
from . import service
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from datetime import datetime

# Create your views here.
country_to_flag = {
    "GER": "🇩🇪",
    "SUI": "🇨🇭",
    "HUN": "🇭🇺",
    "SCO": "🏴󠁧󠁢󠁳󠁣󠁴󠁿",
    "ESP": "🇪🇸",
    "ITA": "🇮🇹",
    "ALB": "🇦🇱",
    "CRO": "🇭🇷",
    "SVN": "🇸🇮",
    "DEN": "🇩🇰",
    "SRB": "🇷🇸",
    "ENG": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    "NED": "🇳🇱",
    "FRA": "🇫🇷",
    "POL": "🇵🇱",
    "AUT": "🇦🇹",
    "UKR": "🇺🇦",
    "SVK": "🇸🇰",
    "BEL": "🇧🇪",
    "ROU": "🇷🇴",
    "POR": "🇵🇹",
    "CZE": "🇨🇿",
    "GEO": "🇬🇪",
    "TUR": "🇹🇷"
}

player_of_match = ['played_time', 'goals', 'passes_accuracy',
                   'assists', 'top_speed', 'distance_covered']

stat_match = ['attempts', 'attempts_on_target', 'ball_possession', 'passes_attempted',
              'passes_accuracy', 'fouls_committed', 'yellow_cards', 'red_cards', 'offsides', 'corners']


def getTeam(request):
    teams = service.getEuroTeam()

    return render(request, 'teams.html', {'teams': teams})


def getStats(request):
    stats = service.getEuroTeamStats()

    nameCol = []
    for name in stats[0]['statistics']:
        dict_col = {"name": name['name'], "colname": name['name'].replace(
            "_", " ").capitalize()}
        nameCol.append(dict_col)

    return render(request, 'stats.html', {'stats': stats, 'nameCol': nameCol})


def getGroup(request):
    groups = service.getEuroGroup()

    for group in groups:
        groupId = group["group"]["id"]
        formGuide = service.getEuroFormGuide(groupId)

        dict_formGuide = {}
        for match in formGuide:
            homeId = match['homeTeam']['id']
            awayId = match['awayTeam']['id']

            if match['status'] == 'FINISHED':
                homeScore = match['score']['total']['home']
                awayScore = match['score']['total']['away']

                if homeScore > awayScore:
                    if homeId in dict_formGuide:
                        dict_formGuide[homeId].append("W")
                    else:
                        dict_formGuide[homeId] = ["W"]

                    if awayId in dict_formGuide:
                        dict_formGuide[awayId].append("L")
                    else:
                        dict_formGuide[awayId] = ["L"]
                elif homeScore < awayScore:
                    if homeId in dict_formGuide:
                        dict_formGuide[homeId].append("L")
                    else:
                        dict_formGuide[homeId] = ["L"]

                    if awayId in dict_formGuide:
                        dict_formGuide[awayId].append("W")
                    else:
                        dict_formGuide[awayId] = ["W"]
                elif homeScore == awayScore:
                    if homeId in dict_formGuide:
                        dict_formGuide[homeId].append("D")
                    else:
                        dict_formGuide[homeId] = ["D"]

                    if awayId in dict_formGuide:
                        dict_formGuide[awayId].append("D")
                    else:
                        dict_formGuide[awayId] = ["D"]

        for team in group['items']:
            lst_form = dict_formGuide.get(team['team']['id'])
            if lst_form:
                while len(lst_form) < 3:
                    lst_form.insert(0, "N")

            team['formGuide'] = lst_form

    return render(request, 'group.html', {'groups': groups})


def getMatches(request):
    matches = service.getEuroMatches()
    for match in matches:
        value = service.convert_time_between_offsets(
            match.get("kickOffTime").get("dateTime"))
        match["kickOffTime"]["dateTime"] = value.strftime("%a, %B %d")
        match["kickOffTime"]["time"] = value.strftime("%H:%M")
        match["kickOffTime"]["date"] = value.strftime("%Y-%m-%d")

        if 'playerEvents' in match:
            if 'redCards' in match['playerEvents']:
                for redCard in match['playerEvents']['redCards']:
                    if redCard['teamId'] == match['awayTeam']['id']:
                        match['awayTeam']['redCard'] = True

                    if redCard['teamId'] == match['homeTeam']['id']:
                        match['homeTeam']['redCard'] = True

    groups = service.getEuroGroup()
    teams = []
    for group in groups:
        for item in group['items']:
            item['team']['emojiCode'] = country_to_flag[item['team']['countryCode']]
            teams.append(item['team'])

    return render(request, 'matches.html', {'matches': matches, 'teams': teams, 'groups': groups})


def getMatchDetail(request, matchid):
    lineup = service.getEuroLineUp(matchid)
    match = service.getEuroMatch(matchid)
    match_stat = service.getEuroStatMatch(matchid)
    eventLineup = service.getEuroEventLineUp(matchid)

    match[0]['homeTeam']['iconHtml'] = country_to_flag[match[0]
                                                       ['homeTeam']['teamCode']]
    match[0]['awayTeam']['iconHtml'] = country_to_flag[match[0]
                                                       ['awayTeam']['teamCode']]

    homeTeamId = match[0]['homeTeam']['id']
    awayTeamId = match[0]['awayTeam']['id']

    match_stat_result = []
    for stat in stat_match:
        dct_stat = {}
        dct_stat['name'] = stat

        for team in match_stat:
            if team['teamId'] == homeTeamId:
                for origin_stat_home in team['statistics']:
                    if origin_stat_home['name'] == stat:
                        dct_stat['homeTeamValue'] = origin_stat_home['value']
                        dct_stat['nameDisplay'] = origin_stat_home['translations']['name']['EN']
            elif team['teamId'] == awayTeamId:
                for origin_stat_away in team['statistics']:
                    if origin_stat_away['name'] == stat:
                        dct_stat['awayTeamValue'] = origin_stat_away['value']

        match_stat_result.append(dct_stat)

    playerOfMatch = {}
    if 'playerOfTheMatch' in match[0]:
        playerOfMatchFullData = service.getEuroStatPlayerOfMatch(
            matchid, match[0]['playerOfTheMatch']['player']['id'])[0]

        statistics = []
        playerOfMatch['playerId'] = playerOfMatchFullData['playerId']
        playerOfMatch['teamId'] = playerOfMatchFullData['teamId']

        for stat in playerOfMatchFullData['statistics']:
            if stat['name'] in player_of_match:
                statistics.append(stat)

        playerOfMatch['statistics'] = statistics

    value = service.convert_time_between_offsets(
        match[0].get("kickOffTime").get("dateTime"))
    match[0]["kickOffTime"]["dateTime"] = value.strftime("%a, %B %d")

    if lineup['lineupStatus'] == 'TACTICAL_AVAILABLE':
        lineup['awayTeam']['textColor'] = service.get_complementary_color(
            lineup['awayTeam']['shirtColor'])
        lineup['homeTeam']['textColor'] = service.get_complementary_color(
            lineup['homeTeam']['shirtColor'])

    return render(request, 'matchdetail.html', {'lineup': lineup, 'match': match[0], 'playerOfMatch': playerOfMatch, 'matchStat': match_stat_result, 'eventLineup': eventLineup[::-1]})


def getBraketview(request):
    braket = service.getEuroBraket()

    for match in braket:
        value = service.convert_time_between_offsets(
            match.get("kickOffTime").get("dateTime"))
        match["kickOffTime"]["dateTime"] = value.strftime("%a, %B %d")
        match["kickOffTime"]["time"] = value.strftime("%H:%M")
        match["kickOffTime"]["timeBraket"] = value.strftime("%B %d, %H:%M")

    round16 = [braket[11]] + [braket[13]] + [braket[9]] + [braket[10]
                                                           ] + [braket[8]] + [braket[7]] + [braket[12]] + [braket[14]]
    quarter = [braket[6]] + [braket[5]] + [braket[3]] + [braket[4]]
    semi = braket[2:0:-1]
    final = braket[0]

    return render(request, 'braket.html', {'final': final, 'semi': semi, 'quarter': quarter, 'round16': round16, 'matches': braket[::-1]})


SPREADSHEET_ID = '1mRjM0eLr41McMARa6xiEwBsmchfxulIaD1EbqmpUy1Q'


def get_request_gg(request):
    if request.method == "GET":
        """
        Lấy dữ liệu từ Google Sheet.

        :param spreadsheet_id: ID của Google Sheet (có thể lấy từ URL).
        :param range_: Range cần lấy dữ liệu (ví dụ: 'Sheet1!A1:C10').
        :return: Dữ liệu lấy được (dạng list 2D) hoặc None nếu xảy ra lỗi.
        """
        # Lấy Google Sheets service
        service = get_google_sheets_service()

        try:
            # Lấy dữ liệu từ Google Sheets
            result = service.spreadsheets().values().get(
                spreadsheetId=SPREADSHEET_ID,
                range='yc!B4:C'
            ).execute()

            # Trả về danh sách giá trị hoặc rỗng
            data = result.get('values', [])
            if data:
                # Chuyển dữ liệu thành hai mảng, loại bỏ null
                col_b = [row[0] for row in data if len(row) > 0 and row[0]] 
                col_c = [row[1] for row in data if len(row) > 1 and row[1]]

                return JsonResponse({
                    'status': 'success',
                    'message': 'Data fetched successfully!',
                    'data': {
                        'employ': col_b,
                        'channel': col_c
                    }
                }, status=200)

            return JsonResponse({'status': 'error', 'message': 'Failed to fetch data'}, status=400)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error: {e}'}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


def send_gg(request):
    if request.method == 'POST':
        try:
            # Lấy dữ liệu từ body request
            data = json.loads(request.body)
            now = datetime.now()

            employee = data.get('employee')
            order_id = data.get('order_id')
            source = data.get('source')
            info = data.get('info')
            print(str(now))
            RANGE = 'Sheet1!B:B'
            VALUES = [
                [None, str(now), employee, source, order_id, info]
            ]

            # Gọi hàm để chèn dữ liệu vào Google Sheet
            if insert_to_google_sheet(SPREADSHEET_ID, RANGE, VALUES):
                return JsonResponse({
                    'status': 'success',
                    'message': 'Data saved successfully!',
                    'data': {
                        'employee': employee,
                        'source': source,
                        'order_id': order_id,
                        'info': info
                    }
                }, status=201)

            return JsonResponse({'status': 'error', 'message': 'Invalid'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


# Biến toàn cục lưu trữ service
_google_sheets_service = None


def get_google_sheets_service():
    """
    Khởi tạo Google Sheets API service nếu chưa có và tái sử dụng.
    """
    global _google_sheets_service

    if _google_sheets_service is None:
        try:
            # Lấy thông tin Service Account từ biến môi trường
            cre = os.environ.get("CRE")
            credentials = Credentials.from_service_account_info(
                json.loads(cre),
                scopes=["https://www.googleapis.com/auth/spreadsheets"]
            )

            # Khởi tạo Google Sheets API service
            _google_sheets_service = build(
                'sheets', 'v4', credentials=credentials)

        except Exception as e:
            print(f"Lỗi khi khởi tạo Google Sheets API service: {e}")
            raise e

    return _google_sheets_service


def insert_to_google_sheet(spreadsheet_id, range_, values):
    """
    Chèn dữ liệu vào Google Sheet.

    :param spreadsheet_id: ID của Google Sheet (có thể lấy từ URL).
    :param range_: Range trong Google Sheet (ví dụ: 'Sheet1!A1:C3').
    :param values: Dữ liệu cần chèn vào sheet (dạng list 2D).
    """
    # Lấy Google Sheets service
    service = get_google_sheets_service()

    # Cấu trúc body của yêu cầu
    body = {
        'values': values
    }

    try:
        # Chèn dữ liệu vào Google Sheets
        result = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_,
            valueInputOption="RAW",  # Hoặc "USER_ENTERED"
            body=body
        ).execute()

        print(f"Đã chèn dữ liệu: {result}")
        return True
    except Exception as e:
        print(f"Lỗi khi chèn dữ liệu vào Google Sheets: {e}")
        return False
