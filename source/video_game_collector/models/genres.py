class Genres():
    _genres = []

    def load_genres(self):
        from video_game_collector.api.catalog_api import CatalogApi
        catalog_api = CatalogApi()
        genres_json = catalog_api.get_genres()
        self._genres = [(c['id'], c['name']) for c in genres_json]

    def get_genre_id(self, genre_name):
        for genre in self._genres:
            if genre[1] == genre_name:
                return genre[0]

        return -1