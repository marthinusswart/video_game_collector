class Platforms():
    _platforms = []

    def load_platforms(self):
        from video_game_collector.api.catalog_api import CatalogApi
        catalog_api = CatalogApi()
        platforms_json = catalog_api.get_platforms()
        self._platforms = [(c['id'], c['name']) for c in platforms_json]

    def get_platform_id(self, platform_name):
        for platform in self._platforms:
            if platform[1] == platform_name:
                return platform[0]

        return -1
