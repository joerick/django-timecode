# django-timecode

A python class to store and manipulate timecodes with accompanying Django field.

## Examples

Timecodes can be created using a string representation

    >>> from timecode import Timecode
    >>> start = Timecode('09:59:50:00', fps=25)
    >>> end = Timecode('10:06:05:12', fps=25)

They will print themselves

    >>> start
    Timecode('09:59:50:00', fps=25)
    >>> str(start)
    '09:59:50:00'

They can add and subtract

    >>> delta = end - start
    >>> delta
    Timecode('00:06:15:12', fps=25)

Or you can get at the exact frames using the `total_frames` attribute

    >>> delta.total_frames
    9387

## In a Django model

### `models.py`

    from timecode.fields import TimecodeField
    from django.db import models


    class TestModel(models.Model):
        timecode = TimecodeField()

You can then store the timecode objects in the database.
