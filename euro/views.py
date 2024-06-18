from django.shortcuts import render
from django.http import HttpResponse
from . import service

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
            # print(item['team']['countryCode'])
            item['team']['emojiCode'] = country_to_flag[item['team']['countryCode']]
            teams.append(item['team'])

    return render(request, 'matches.html', {'matches': matches, 'teams': teams, 'groups': groups})


def getMatchDetail(request, matchid):
    lineup = service.getEuroLineUp(matchid)
    match = service.getEuroMatch(matchid)

    value = service.convert_time_between_offsets(
            match[0].get("kickOffTime").get("dateTime"))
    match[0]["kickOffTime"]["dateTime"] = value.strftime("%a, %B %d")

    if lineup['lineupStatus'] == 'TACTICAL_AVAILABLE':
        lineup['awayTeam']['textColor'] = service.get_complementary_color(
            lineup['awayTeam']['shirtColor'])
        lineup['homeTeam']['textColor'] = service.get_complementary_color(
            lineup['homeTeam']['shirtColor'])

    return render(request, 'matchdetail.html', {'lineup': lineup, 'match': match[0]})


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
