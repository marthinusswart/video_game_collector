from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, TextAreaField, DecimalField
from wtforms.validators import InputRequired, Length


class AddGameForm(FlaskForm):
    title = StringField('Title longer title', validators=[InputRequired(),
                                                          Length(min=10, max=100)],
                        render_kw={
                        'class': 'form-control', 'aria-describedby': 'game-title-text'})
    sort_title = StringField('Sort Title', validators=[InputRequired(),
                                                       Length(min=10, max=100)],
                             render_kw={
        'class': 'form-control', 'aria-describedby': 'game-sort-title-text'})
    series = StringField('Series', validators=[InputRequired(),
                                               Length(min=10, max=100)],
                         render_kw={
        'class': 'form-control', 'aria-describedby': 'series-text'})

    release_date = DateField('Release Date', format='%Y-%m-%d',
                             render_kw={
                                 'class': 'form-control', 'aria-describedby': 'release-date-text'})

    purchase_price = DecimalField(
        'Purchase Price', validators=[InputRequired()],
        render_kw={
            'class': 'form-control', 'aria-describedby': 'purchase-price-text'})

    description = TextAreaField('Description',
                                validators=[InputRequired(),
                                            Length(max=200)],
                                render_kw={
                                    'class': 'form-control', 'aria-describedby': 'description-text'})

    condition_id = SelectField('Condition', coerce=int,
                               render_kw={
                                   'class': 'form-select', 'aria-describedby': 'condition-text'})
    vendor_id = SelectField('Vendor', coerce=int,
                            render_kw={
                                'class': 'form-select', 'aria-describedby': 'vendor-text'})

    game_platform_id = SelectField('Platform', coerce=int,
                                   render_kw={
                                       'class': 'form-select', 'aria-describedby': 'platform-text'})
    format_type_id = SelectField('Format', coerce=int,
                                 render_kw={
                                     'class': 'form-select', 'aria-describedby': 'format-text'})
    region_id = SelectField('Region', coerce=int,
                            render_kw={
                                'class': 'form-select', 'aria-describedby': 'region-text'})
    audience_rating_id = SelectField('Audience Rating', coerce=int,
                                     render_kw={
                                         'class': 'form-select', 'aria-describedby': 'rating-text'})
    publisher_id = SelectField('Publisher', coerce=int,
                               render_kw={
                                   'class': 'form-select', 'aria-describedby': 'publisher-text'})
    developer_id = SelectField('Developer', coerce=int,
                               render_kw={
                                   'class': 'form-select', 'aria-describedby': 'developer-text'})


class AddVendorForm(FlaskForm):
    vendor_name = StringField('Name', validators=[InputRequired(),
                                                  Length(min=3, max=100)],
                              render_kw={
        'class': 'form-control'})


class AddPublisherForm(FlaskForm):
    publisher_name = StringField('Name', validators=[InputRequired(),
                                                     Length(min=3, max=100)],
                                 render_kw={
        'class': 'form-control'})


class AddDeveloperForm(FlaskForm):
    developer_name = StringField('Name', validators=[InputRequired(),
                                                     Length(min=3, max=100)],
                                 render_kw={
        'class': 'form-control'})


class AddConditionForm(FlaskForm):
    condition_name = StringField('Name', validators=[InputRequired(),
                                                     Length(min=3, max=100)],
                                 render_kw={
        'class': 'form-control'})


class AddAudienceRatingForm(FlaskForm):
    audience_rating_name = StringField('Name', validators=[InputRequired(),
                                                           Length(min=1, max=100)],
                                       render_kw={
        'class': 'form-control'})


class AddRegionForm(FlaskForm):
    region_name = StringField('Name', validators=[InputRequired(),
                                                  Length(min=1, max=100)],
                              render_kw={
        'class': 'form-control'})


class AddFormatForm(FlaskForm):
    format_name = StringField('Name', validators=[InputRequired(),
                                                  Length(min=3, max=100)],
                              render_kw={
        'class': 'form-control'})


class AddPlatformForm(FlaskForm):
    platform_name = StringField('Name', validators=[InputRequired(),
                                                    Length(min=3, max=100)],
                                render_kw={
        'class': 'form-control'})
