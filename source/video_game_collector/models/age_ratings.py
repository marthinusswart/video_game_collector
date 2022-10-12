class AgeRatings():
    _ratings = []

    def load_age_ratings(self):
        from video_game_collector.api.catalog_api import CatalogApi
        catalog_api = CatalogApi()
        ratings_json = catalog_api.get_ratings()
        self._ratings = [(c['id'], c['name']) for c in ratings_json]

    def get_age_rating_id(self, age_rating_name):
        for age_rating in self._ratings:
            if age_rating[1] == age_rating_name:
                return age_rating[0]

        return -1
