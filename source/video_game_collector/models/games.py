class Games():
    _games = []

    def load_games(self):
        from video_game_collector.api.catalog_api import CatalogApi
        catalog_api = CatalogApi()
        games_json = catalog_api.get_games()        
        self._games = games_json

    def get_game_id(self, game_name):
        for game in self._games:
            if game[1] == game_name:
                return game[0]

        return -1

    def get_games(self):
        return self._games