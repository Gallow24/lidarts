from flask_babelex import _, lazy_gettext
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, TextAreaField, RadioField
from wtforms_components import TimeField
from wtforms.fields import DateField
from wtforms.validators import DataRequired, Length, Optional


class RequiredIf(DataRequired):
    # a validator which makes a field required if
    # another field is set and has a truthy value

    field_flags = ('requiredif',)

    def __init__(self, other_field_name, message=None, *args, **kwargs):
        self.other_field_name = other_field_name
        self.message = message

    def __call__(self, form, field):
        other_field = form[self.other_field_name]
        if other_field is None:
            raise Exception('no field named "%s" in form' % self.other_field_name)
        if bool(other_field.data):
            super(RequiredIf, self).__call__(form, field)
        else:
            Optional().__call__(form, field)


class CreateTournamentForm(FlaskForm):
    name = StringField(lazy_gettext('Tournament name'),  validators=[DataRequired(), Length(min=3, max=50)])
    description = TextAreaField(lazy_gettext('Description'), validators=[Length(min=0, max=1000)])
    public_tournament = BooleanField(lazy_gettext('Open to the public'))
    registration_open = BooleanField(lazy_gettext('Player registration is open'))
    external_url = StringField(lazy_gettext('External URL'), validators=[RequiredIf('public_tournament'), Length(min=1, max=120)])
    start_date = DateField('Start date', format='%Y-%m-%d', validators=[RequiredIf('public_tournament')])
    start_time = TimeField('Start time', validators=[RequiredIf('public_tournament')])
    submit = SubmitField(lazy_gettext('Create Tournament'))
    submit_save = SubmitField(lazy_gettext('Save settings'))


class ConfirmStreamGameForm(FlaskForm):
    games = RadioField(lazy_gettext('Streamable games'), validators=[DataRequired()])
    submit = SubmitField(lazy_gettext('Select game'))
