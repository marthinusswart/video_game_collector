from flask import current_app
from igdb.wrapper import IGDBWrapper
from igdb.igdbapi_pb2 import GameResult, AgeRatingResult
import requests
import re


class igdbApi():
    def lookup_game(self, game_title):

        if 'IGDB_API_TOKEN' not in current_app.config:
            self.refresh_twitch_token()

        game = self.retrieve_game(game_title)
        return game

    def refresh_twitch_token(self):
        print('Refreshing App Token')
        response = requests.post(
            url='https://id.twitch.tv/oauth2/token',
            params={
                'client_id': current_app.config['CLIENT_ID'],
                'client_secret': current_app.config['CLIENT_SECRET'],
                'grant_type': 'client_credentials'
            }
        )

        response.raise_for_status()
        response_body = response.json()
        current_app.config['IGDB_API_TOKEN'] = response_body['access_token']

    def retrieve_game(self, search):
        app_token = current_app.config['IGDB_API_TOKEN']
        client_id = current_app.config["CLIENT_ID"]

        igdb = IGDBWrapper(client_id, app_token)
        query = f'search "{search}"'

        if re.match('igdb:[1-9]+', search):
            igdb_id = int(search.split(':')[1])
            query = f'where id = {igdb_id}'

        # print(query)

        byte_array = igdb.api_request(
            'games.pb',
            f'''
            fields
            name,
            category,
            first_release_date,
            collection.name,
            platforms.name,
            genres.name,
            cover.image_id,
            age_ratings,
            summary,          
            involved_companies.company.name,
            involved_companies.developer,
            involved_companies.porting,
            involved_companies.publisher;
            limit 1;
            {query};
            '''
        )

        response = GameResult()
        response.ParseFromString(byte_array)

        if not len(response.games):
            print('Game not found')
            return None

        #print(f'Games returned {len(response.games)}')
        game = response.games[0]
        return game

    def lookup_age_rating(self, age_rating_id):
        app_token = current_app.config['IGDB_API_TOKEN']
        client_id = current_app.config["CLIENT_ID"]

        igdb = IGDBWrapper(client_id, app_token)
        query = f'where id = {age_rating_id}'
        # print(query)

        byte_array = igdb.api_request(
            'age_ratings.pb',
            f'''
            fields
            rating,synopsis;
            limit 1;
            {query};
            '''
        )
        response = AgeRatingResult()
        response.ParseFromString(byte_array)

        #print(f'Age ratings returned {len(response.ageratings)}')
        age_rating = response.ageratings[0]
        # print(age_rating)
        from igdb.igdbapi_pb2 import AgeRatingRatingEnum
        # print(AgeRatingRatingEnum.items()[age_rating.rating][0])
        rating_name = AgeRatingRatingEnum.items()[age_rating.rating][0]
        return rating_name

    def _remove_commas(self, text):
        return text.replace(',', '')
