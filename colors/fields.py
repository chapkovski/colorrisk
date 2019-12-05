from otree.db.serializedfields import _PickleField
from django import forms
from django.db.models import TextField
import json


class PickleField(TextField):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.null = True

    def to_python(self, value):
        """Convert our string value to JSON after we load it from the DB"""
        if value == "":
            return None

        try:
            if isinstance(value, str):
                return json.loads(value)
        except ValueError:
            pass

        return value

    def get_prep_value(self, value):
        """Convert our object to a string before we save"""
        if value == "" or value is None:
            return None


        return json.dumps(value)

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return json.dumps(value)


class AllocationField(forms.BooleanField):
    pass
    # def to_python(self, value):
    #     return bool(value)
