import requests


class VendorApi():
    def get_vendors(self):
        r = requests.get(
            'http://localhost:5004/api/v1/video_game_collector/vendors')
        return r.json()

    def post_vendors(self, vendor_name):
        data = {'name': vendor_name}
        r = requests.post(
            'http://localhost:5004/api/v1/video_game_collector/vendors', json=data
        )
        return r
