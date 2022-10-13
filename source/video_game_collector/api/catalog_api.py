import requests


class CatalogApi():
    def get_conditions(self):
        r = requests.get(
            'http://localhost:5005/api/v1/video_game_collector/catalogitemconditions')
        return r.json()

    def get_regions(self):
        r = requests.get(
            'http://localhost:5005/api/v1/video_game_collector/catalogitemregions')
        return r.json()

    def get_formats(self):
        r = requests.get(
            'http://localhost:5005/api/v1/video_game_collector/catalogitemformats')
        return r.json()

    def get_ratings(self):
        r = requests.get(
            'http://localhost:5005/api/v1/video_game_collector/catalogitemaudienceratings')
        return r.json()

    def get_platforms(self):
        r = requests.get(
            'http://localhost:5005/api/v1/video_game_collector/gameplatforms')
        return r.json()

    def get_developers(self):
        r = requests.get(
            'http://localhost:5005/api/v1/video_game_collector/developers')
        return r.json()

    def get_publishers(self):
        r = requests.get(
            'http://localhost:5005/api/v1/video_game_collector/publishers')
        return r.json()

    def get_genres(self):
        r = requests.get(
            'http://localhost:5005/api/v1/video_game_collector/cataloggenres')
        return r.json()

    def get_games(self):
        r = requests.get(
            'http://localhost:5005/api/v1/video_game_collector/games')
        return r.json()        

    def post_publishers(self, publisher_name):
        data = {'name': publisher_name}
        r = requests.post(
            'http://localhost:5005/api/v1/video_game_collector/publishers', json=data
        )
        return r

    def post_genres(self, genre_name):
        data = {'name': genre_name}
        r = requests.post(
            'http://localhost:5005/api/v1/video_game_collector/cataloggenres', json=data
        )
        return r

    def post_developers(self, developer_name):
        data = {'name': developer_name}
        r = requests.post(
            'http://localhost:5005/api/v1/video_game_collector/developers', json=data
        )
        return r

    def post_conditions(self, condition_name):
        data = {'name': condition_name}
        r = requests.post(
            'http://localhost:5005/api/v1/video_game_collector/catalogitemconditions', json=data
        )
        return r

    def post_audience_ratings(self, audience_rating_name):
        data = {'name': audience_rating_name}
        r = requests.post(
            'http://localhost:5005/api/v1/video_game_collector/catalogitemaudienceratings', json=data
        )
        return r

    def post_regions(self, region_name):
        data = {'name': region_name}
        r = requests.post(
            'http://localhost:5005/api/v1/video_game_collector/catalogitemregions', json=data
        )
        return r

    def post_formats(self, format_name):
        data = {'name': format_name}
        r = requests.post(
            'http://localhost:5005/api/v1/video_game_collector/catalogitemformats', json=data
        )
        return r

    def post_platforms(self, platform_name):
        data = {'name': platform_name}
        r = requests.post(
            'http://localhost:5005/api/v1/video_game_collector/gameplatforms', json=data
        )
        return r
