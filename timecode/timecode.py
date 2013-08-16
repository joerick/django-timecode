

class Timecode():
    frames = 0

    def __init__(self, string=None, fps=25, total_frames=0):
        self.fps = fps

        if string is None:
            self.total_frames = int(total_frames)
        else:
            if len(string) != 11:
                raise ValueError('Timecodes must be in the format 00:00:00:00')

            unpacked = string.split(':')

            if len(unpacked) != 4:
                raise ValueError('Timecodes must have four numbers divided by a colon')

            hours, minutes, seconds, frames = (int(each) for each in unpacked)

            if hours > 99 or minutes > 59 or seconds > 59 or frames >= fps:
                raise ValueError('Invalid timecode %s' % string)

            self.total_frames = ((hours*60 + minutes)*60 + seconds)*fps + frames

    def __repr__(self):
        return "Timecode('%s', fps=%i)" % (str(self), self.fps)

    def __str__(self):
        return '%02i:%02i:%02i:%02i' % self.components()

    def __cmp__(self, other):
        if not isinstance(other, Timecode):
            raise TypeError
        return cmp(self.total_frames, other.total_frames)

    def __eq__(self, other):
        return isinstance(other, Timecode) and self.total_frames == other.total_frames

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.total_frames)

    def __int__(self):
        return self.total_frames

    def __add__(self, other):
        self._assert_equal_fps(other)
        return Timecode(total_frames=self.total_frames + int(other))

    def __sub__(self, other):
        self._assert_equal_fps(other)
        return Timecode(total_frames=self.total_frames - int(other))

    def components(self):
        frames_per_hour = self.fps * 60 * 60
        frames_per_minute = self.fps * 60

        hours, hours_remainder = divmod(self.total_frames, frames_per_hour)

        minutes, minutes_remainder = divmod(hours_remainder, frames_per_minute)

        seconds, frames = divmod(minutes_remainder, self.fps)

        return (hours, minutes, seconds, frames)

    def _assert_equal_fps(self, other):
        if self.fps != other.fps:
            raise self.FPSMismatch

    @property
    def hours(self):
        return self.components()[0]

    @property
    def minutes(self):
        return self.components()[1]

    @property
    def seconds(self):
        return self.components()[2]

    @property
    def frames(self):
        return self.components()[3]

    class FPSMismatch(Exception):
        pass
