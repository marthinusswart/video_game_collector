class Publishers():
    _publishers = []

    def load_publishers(self):
        from video_game_collector.api.catalog_api import CatalogApi
        catalog_api = CatalogApi()
        publishers_json = catalog_api.get_publishers()
        self._publishers = [(c['id'], c['name']) for c in publishers_json]

    def get_publisher_id(self, publisher_name):
        for publisher in self._publishers:
            if publisher[1] == publisher_name:
                return publisher[0]

        return -1
