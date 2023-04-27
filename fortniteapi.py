import fortnite_api
import json
import requests
from requests.auth import HTTPBasicAuth
import discord

def stat(nik):
    auth = '02a3650e-85b0-499c-a065-822e547812e1'
    api = fortnite_api.FortniteAPI(api_key=auth)
    #url = 'https://fortnite-api.com/v2/stats/br/v2'

    #name = 'e-lectrica'
    name = nik
    try:
        output = api.stats.fetch_by_name(name=name)
        output = output.raw_data

        level = output['battlePass']['level']
        minutes = output['stats']['all']['overall']['minutesPlayed']
        wins = output['stats']['all']['overall']['wins']
        kills = output['stats']['all']['overall']['kills']
        winRate = output['stats']['all']['overall']['winRate']
        kd = output['stats']['all']['overall']['kd']

        message = f" Текущий уровень БП - {level}  \n" \
                  f" Суток наиграно - {round(minutes / 60 / 24)}  \n" \
                  f" Кол-во побед - {wins}  \n" \
                  f" Кол-во киллов - {kills}  \n" \
                  f" % побед - {winRate}  \n" \
                  f" K/D - {kd}  \n" \

        return message
    except Exception as err:
        if err.args[0] == 'the requested account does not exist':
            message = 'Запрошенный аккаунт EpicGames не найден!'
            return message
        elif err.args[0] == '''the requested account's stats are not public''''':
            message = 'Аккаунт EpicGames не являетя публичным!'
            return message
