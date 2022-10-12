from flask import Flask
import json


def create_app():
    app = Flask(__name__)

    f = open('video_game_collector/config/config.json')
    data = json.load(f)
    # print(data['config'])
    # print(data['config']['secret_key'])
    f.close()

    app.config['SECRET_KEY'] = data['config']['secret_key']
    app.config['CLIENT_ID'] = data['config']['client_id']
    app.config['CLIENT_SECRET'] = data['config']['client_secret']

    from .views import views

    app.register_blueprint(views, url_prefix='/')
    return app
