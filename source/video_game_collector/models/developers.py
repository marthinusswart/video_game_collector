class Developers():
    _developers = []

    def load_developers(self):
        from video_game_collector.api.catalog_api import CatalogApi
        catalog_api = CatalogApi()
        developers_json = catalog_api.get_developers()
        self._developers = [(c['id'], c['name']) for c in developers_json]

    def get_developer_id(self, developer_name):
        for developer in self._developers:
            if developer[1] == developer_name:
                return developer[0]

        return -1
