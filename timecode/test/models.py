from timecode.fields import TimecodeField
from django.db import models


class TestModel(models.Model):
    timecode = TimecodeField(blank=True, null=True)
