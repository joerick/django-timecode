from django.test import TestCase
from timecode import Timecode
from .models import TestModel


class TimecodeTest(TestCase):
    def test_creation(self):
        self.assertRaises(ValueError, Timecode, '00:00:00:00:00')
        self.assertRaises(ValueError, Timecode, '00:00:00000')
        self.assertRaises(ValueError, Timecode, '00:00:0a:00')
        self.assertRaises(TypeError, Timecode, '00:00:00:00', fps="a string")
        self.assertRaises(TypeError, Timecode, 123)

        a = Timecode('12:34:56:12', fps=25)

        self.assertEqual(a.hours, 12)
        self.assertEqual(a.minutes, 34)
        self.assertEqual(a.seconds, 56)
        self.assertEqual(a.frames, 12)

    def test_total_frames(self):
        a = Timecode('12:34:56:12', fps=25)

        self.assertEqual(a.total_frames, ((a.hours*60 + a.minutes)*60 + a.seconds)*a.fps + a.frames)

    def test_printing(self):
        a_str = '12:34:56:12'

        a = Timecode(a_str, fps=25)

        self.assertEqual(str(a), a_str)

    def test_math(self):
        a = Timecode('12:34:56:12', fps=25)

        b = Timecode('00:00:01:10', fps=25)

        c = a + b

        self.assertEqual(c, Timecode('12:34:57:22', fps=25))

        d = a - b

        self.assertEqual(d, Timecode('12:34:55:02', fps=25))

    def test_fps_compatibility(self):
        a = Timecode('12:34:56:12', fps=25)
        b = Timecode('12:34:56:12', fps=50)

        def add(a1, a2):
            return a1 + a2

        def sub(a1, a2):
            return a1 - a2

        self.assertRaises(Timecode.FPSMismatch, add, a, b)
        self.assertRaises(Timecode.FPSMismatch, sub, a, b)


class TimecodeFieldTest(TestCase):

    def setUp(self):
        t1 = TestModel(timecode=Timecode('04:03:02:01'))
        t1.save()
        t2 = TestModel(timecode=Timecode('01:02:03:04', fps=50))
        t2.save()

    def test_timecode_recall(self):
        t1 = TestModel.objects.get(pk=1)
        self.assertEqual(t1.timecode, Timecode('04:03:02:01'))
        t2 = TestModel.objects.get(pk=2)
        self.assertEqual(t2.timecode, Timecode('01:02:03:04', fps=50))
