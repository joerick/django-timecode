from django.db import models
from django.core import exceptions, validators
from django import forms
from .timecode import Timecode

try:
    from south.modelsinspector import add_introspection_rules
except ImportError:
    pass
else:
    add_introspection_rules([], ["^timecode\.fields\.TimecodeField"])


class TimecodeWidget(forms.TextInput):
    def __init__(self, attrs={}):
        attrs.update({'class': 'timecode-widget'})
        super(TimecodeWidget, self).__init__(attrs)

    class Media:
        js = ('timecode/widget.js', 'timecode/jquery.caret.js',)


class TimecodeFormField(forms.Field):
    widget = TimecodeWidget

    def to_python(self, value):
        if value in validators.EMPTY_VALUES:
            return None
        try:
            return Timecode(value)
        except ValueError, e:
            raise exceptions.ValidationError(e)


class TimecodeField(models.Field):
    default_error_messages = {
        'invalid': "'%s' value must be in the format '00:00:00:00 25', where the latter is the fps.",
    }
    description = "Timecode"

    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 14
        models.Field.__init__(self, *args, **kwargs)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)

    def get_prep_value(self, value):
        if value is None:
            return None
        if isinstance(value, Timecode):
            return "%s %i" % (str(value), value.fps)
        raise TypeError('value is not a Timecode')

    def to_python(self, value):
        if value is None or value == '':
            return None
        if isinstance(value, Timecode):
            return value
        try:
            timecode_string, fps_string = value.split(' ')
            return Timecode(timecode_string, int(fps_string))
        except (TypeError, ValueError):
            msg = self.error_messages['invalid'] % value
            raise exceptions.ValidationError(msg)

    def get_internal_type(self):
        return 'CharField'

    def formfield(self, **kwargs):
        defaults = {'form_class': TimecodeFormField}
        defaults.update(kwargs)
        return super(TimecodeField, self).formfield(**defaults)
