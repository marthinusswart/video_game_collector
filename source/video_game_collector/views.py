from flask import Blueprint, render_template, request, flash
from flask import jsonify
from video_game_collector.forms import AddGameForm, AddVendorForm, AddPublisherForm, AddDeveloperForm, AddGenreForm
from video_game_collector.forms import AddConditionForm, AddAudienceRatingForm, AddRegionForm, AddFormatForm
from video_game_collector.forms import AddPlatformForm, EditGameForm, DetailViewGameForm
from video_game_collector.api.vendor_api import VendorApi
from video_game_collector.api.catalog_api import CatalogApi
from video_game_collector.models.publishers import Publishers
from video_game_collector.models.developers import Developers
from video_game_collector.models.platforms import Platforms
from video_game_collector.models.age_ratings import AgeRatings
from video_game_collector.models.genres import Genres
from video_game_collector.models.games import Games
from video_game_collector.api.igdb_api import igdbApi
from datetime import datetime

views = Blueprint('views', __name__)
publishers = Publishers()
developers = Developers()
platforms = Platforms()
age_ratings = AgeRatings()
genres = Genres()
games = Games()

def load_comboboxes(form):
    vendor_api = VendorApi()
    vendors_json = vendor_api.get_vendors()
    vendors = [(v['id'], v['name']) for v in vendors_json]
    vendors.insert(0, (-1, ''))

    catalog_api = CatalogApi()
    conditions_json = catalog_api.get_conditions()
    conditions = [(c['id'], c['name']) for c in conditions_json]
    conditions.insert(0, (-1, ''))

    regions_json = catalog_api.get_regions()
    regions = [(c['id'], c['name']) for c in regions_json]
    regions.insert(0, (-1, ''))

    formats_json = catalog_api.get_formats()
    formats = [(c['id'], c['name']) for c in formats_json]
    formats.insert(0, (-1, ''))

    ratings_json = catalog_api.get_ratings()
    ratings = [(c['id'], c['name']) for c in ratings_json]
    ratings.insert(0, (-1, ''))

    platforms_json = catalog_api.get_platforms()
    platforms = [(c['id'], c['name']) for c in platforms_json]
    platforms.insert(0, (-1, ''))

    developers_json = catalog_api.get_developers()
    developers = [(c['id'], c['name']) for c in developers_json]
    developers.insert(0, (-1, ''))

    publishers_json = catalog_api.get_publishers()
    publishers = [(c['id'], c['name']) for c in publishers_json]
    publishers.insert(0, (-1, ''))

    genres_json = catalog_api.get_genres()
    genres = [(c['id'], c['name']) for c in genres_json]
    genres.insert(0, (-1, ''))

    form.vendor_id.choices = vendors
    form.condition_id.choices = conditions
    form.region_id.choices = regions
    form.format_type_id.choices = formats
    form.audience_rating_id.choices = ratings
    form.game_platform_id.choices = platforms
    form.developer_id.choices = developers
    form.publisher_id.choices = publishers
    form.genre_id.choices = genres


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        flash('Note added!', category='success')

    games.load_games()
    game_list = games.get_games()
    print(game_list[0]['release_date'])

    return render_template("home.html", game_list=game_list)


@views.route('/add_game', methods=['GET', 'POST'])
def add_game():
    form = AddGameForm()

    load_comboboxes(form)
    publishers.load_publishers()
    developers.load_developers()
    platforms.load_platforms()
    age_ratings.load_age_ratings()
    genres.load_genres()

    if request.method == 'POST':
        flash('Game added!', category='success')
        return render_template("home.html")

    return render_template("add_game.html", form=form)


@views.route('/lookup_game', methods=['GET'])
def lookup_game():
    if request.method == 'GET':
        #print('Lookup game')
        if request.is_json:
            igdb_api = igdbApi()
            game_title = request.args.get('game_title')
            game = igdb_api.lookup_game(game_title)

            if not game:
                return jsonify({
                'game_title': game_title,
                'sort_title': game_title,                
                'description': 'Game not found'                
            })

            igdb_id = game.id
            #print(igdb_id)
            game_title = _remove_commas(game.name)
            sort_title = _remove_commas(game.name)
            series = _remove_commas(game.collection.name)
            platform = _remove_commas(game.platforms[0].name)
            summary = game.summary
            release_date = datetime.utcfromtimestamp(
                game.first_release_date.seconds).strftime('%Y-%m-%d')

            age_rating_id = game.age_ratings[0].id
            # print(age_rating_id)
            age_rating = igdb_api.lookup_age_rating(age_rating_id)
            # print(age_rating)

            #print(game.genres[0].name)

            genre_id = -1
            developer_id = -1
            publisher_id = -1
            platform_id = -1
            age_rating_id = -1
            developer = ''
            publisher = ''

            for company in game.involved_companies:
                if company.developer:
                    developer = company.company.name

                if company.publisher:
                    publisher = company.company.name

            publisher_id = publishers.get_publisher_id(publisher)
            developer_id = developers.get_developer_id(developer)
            platform_id = platforms.get_platform_id(platform)
            genre_id = genres.get_genre_id(game.genres[0].name)
            age_rating_id = age_ratings.get_age_rating_id(age_rating)

            return jsonify({
                'game_title': game_title,
                'sort_title': sort_title,
                'series': series,
                'platform_id': platform_id,
                'release_date': release_date,
                'rating_id': age_rating_id,
                'developer_id': developer_id,
                'publisher_id': publisher_id,
                'description': summary,
                'igdb_id': igdb_id,
                'genre_id': genre_id
            })


@ views.route('/add_vendor', methods=['GET', 'POST'])
def add_vendor():
    form = AddVendorForm()

    if request.method == 'POST':
        vendor_api = VendorApi()
        vendor_name = form.vendor_name.data
        # print(form.vendor_name.data)
        r = vendor_api.post_vendors(vendor_name)
        if (r.status_code == 200):
            flash('Vendor added!', category='success')
        else:
            flash(f'Error {r.text}', category='error')
        return render_template("add_vendor.html", form=form)

    return render_template("add_vendor.html", form=form)


@ views.route('/add_publisher', methods=['GET', 'POST'])
def add_publisher():
    form = AddPublisherForm()

    if request.method == 'POST':
        catalog_api = CatalogApi()
        publisher_name = form.publisher_name.data
        # print(form.vendor_name.data)
        r = catalog_api.post_publishers(publisher_name)
        if (r.status_code == 200):
            flash('Publisher added!', category='success')
        else:
            flash(f'Error {r.text}', category='error')
        return render_template("add_publisher.html", form=form)

    return render_template("add_publisher.html", form=form)


@ views.route('/add_developer', methods=['GET', 'POST'])
def add_developer():
    form = AddDeveloperForm()

    if request.method == 'POST':
        catalog_api = CatalogApi()
        developer_name = form.developer_name.data
        # print(form.vendor_name.data)
        r = catalog_api.post_developers(developer_name)
        if (r.status_code == 200):
            flash('Developer added!', category='success')
        else:
            flash(f'Error {r.text}', category='error')
        return render_template("add_developer.html", form=form)

    return render_template("add_developer.html", form=form)


@ views.route('/add_condition', methods=['GET', 'POST'])
def add_condition():
    form = AddConditionForm()

    if request.method == 'POST':
        catalog_api = CatalogApi()
        condition_name = form.condition_name.data
        # print(form.vendor_name.data)
        r = catalog_api.post_conditions(condition_name)
        if (r.status_code == 200):
            flash('Condition added!', category='success')
        else:
            flash(f'Error {r.text}', category='error')
        return render_template("add_condition.html", form=form)

    return render_template("add_condition.html", form=form)


@ views.route('/add_audience_rating', methods=['GET', 'POST'])
def add_audience_rating():
    form = AddAudienceRatingForm()

    if request.method == 'POST':
        catalog_api = CatalogApi()
        audience_rating_name = form.audience_rating_name.data
        # print(form.vendor_name.data)
        r = catalog_api.post_audience_ratings(audience_rating_name)
        if (r.status_code == 200):
            flash('Audience Rating added!', category='success')
        else:
            flash(f'Error {r.text}', category='error')
        return render_template("add_audience_rating.html", form=form)

    return render_template("add_audience_rating.html", form=form)


@ views.route('/add_region', methods=['GET', 'POST'])
def add_region():
    form = AddRegionForm()

    if request.method == 'POST':
        catalog_api = CatalogApi()
        region_name = form.region_name.data
        # print(form.vendor_name.data)
        r = catalog_api.post_regions(region_name)
        if (r.status_code == 200):
            flash('Region added!', category='success')
        else:
            flash(f'Error {r.text}', category='error')
        return render_template("add_region.html", form=form)

    return render_template("add_region.html", form=form)


@ views.route('/add_format', methods=['GET', 'POST'])
def add_format():
    form = AddFormatForm()

    if request.method == 'POST':
        catalog_api = CatalogApi()
        format_name = form.format_name.data
        # print(form.vendor_name.data)
        r = catalog_api.post_formats(format_name)
        if (r.status_code == 200):
            flash('Format added!', category='success')
        else:
            flash(f'Error {r.text}', category='error')
        return render_template("add_format.html", form=form)

    return render_template("add_format.html", form=form)


@ views.route('/add_platform', methods=['GET', 'POST'])
def add_platform():
    form = AddPlatformForm()

    if request.method == 'POST':
        catalog_api = CatalogApi()
        platform_name = form.platform_name.data
        # print(form.vendor_name.data)
        r = catalog_api.post_platforms(platform_name)
        if (r.status_code == 200):
            flash('Platform added!', category='success')
        else:
            flash(f'Error {r.text}', category='error')
        return render_template("add_platform.html", form=form)

    return render_template("add_platform.html", form=form)

@ views.route('/add_genre', methods=['GET', 'POST'])
def add_genre():
    form = AddGenreForm()

    if request.method == 'POST':
        catalog_api = CatalogApi()
        genre_name = form.genre_name.data
        # print(form.vendor_name.data)
        r = catalog_api.post_genres(genre_name)
        if (r.status_code == 200):
            flash('genre added!', category='success')
        else:
            flash(f'Error {r.text}', category='error')
        return render_template("add_genre.html", form=form)

    return render_template("add_genre.html", form=form)    

@views.route('/edit_game', methods=['GET', 'POST'])
def edit_game():
    form = EditGameForm()

    #load_comboboxes(form)
    publishers.load_publishers()
    developers.load_developers()
    platforms.load_platforms()
    age_ratings.load_age_ratings()
    genres.load_genres()

    if request.method == 'POST':
        flash('Game updated!', category='success')
        return render_template("edit_game.html")

    return render_template("edit_game.html", form=form)

@views.route('/view_game', methods=['GET', 'POST'])
def view_game():
    form = DetailViewGameForm()

    #load_comboboxes(form)
    publishers.load_publishers()
    developers.load_developers()
    platforms.load_platforms()
    age_ratings.load_age_ratings()
    genres.load_genres()

    if request.method == 'POST':
        flash('Game updated!', category='success')
        return render_template("view_game.html")

    return render_template("view_game.html", form=form)

def _remove_commas(text):
    return text.replace(',', '')
