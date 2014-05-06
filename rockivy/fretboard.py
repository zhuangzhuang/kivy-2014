from .tuning import get_string
from .util import R9, mutate

FRET_COUNT = 16
FRET_SPACING = 55

STRING_COUNT = 6
STRING_SPACING = 30

FRET_LENGTH = (STRING_COUNT - 1) * STRING_SPACING
STRING_LENGTH = FRET_COUNT * FRET_SPACING

LEGEND_OFFSET_X = 20
LEGEND_OFFSET_Y = 25

FB_OFFSET_LEFT = (960 - STRING_LENGTH) * 0.5 + LEGEND_OFFSET_X * 0.5
FB_OFFSET_BOTTOM = (540 - FRET_LENGTH) * 0.5 + LEGEND_OFFSET_Y


def update_tex_uv(tex_uv):
    tex_uv['fret'] = mutate(tex_uv['fret'], {5: FRET_LENGTH * 0.5})

    tex_uv.update([('string_%d' % c,
                    mutate(tex_uv['string'],
                           {4: STRING_LENGTH * 0.5 + tex_uv['fret'][4],
                            5: (c >> 1) + 1})) for c in xrange(STRING_COUNT)])


def _frets():
    return [R9(x=c * FRET_SPACING + FB_OFFSET_LEFT,
               y=FRET_LENGTH * 0.5 + FB_OFFSET_BOTTOM,
               rot=0, size=1, op=1, tex='fret')
            for c in xrange(FRET_COUNT + 1)]


def _strings():
    return [R9(x=STRING_LENGTH * 0.5 + FB_OFFSET_LEFT,
               y=FRET_LENGTH - (c * STRING_SPACING) + FB_OFFSET_BOTTOM,
               rot=0, size=1, op=1, tex='string_%d' % c)
            for c in xrange(STRING_COUNT)]


def _numbers():
    return [R9(x=(c - 0.5) * FRET_SPACING + FB_OFFSET_LEFT,
               y=FB_OFFSET_BOTTOM + 0.5 - LEGEND_OFFSET_Y,
               rot=0, size=1, op=1, tex='num_%d' % c)
            for c in xrange(1, FRET_COUNT + 1)]


def _tuning(notes):
    return [R9(x=FB_OFFSET_LEFT + 0.5 - LEGEND_OFFSET_X,
               y=FRET_LENGTH - (c * STRING_SPACING) - 0.5 + FB_OFFSET_BOTTOM,
               rot=0, size=1, op=1, tex='tun_%s' % notes[c])
            for c in xrange(STRING_COUNT)]


def _notes(string, notes):
    y = FRET_LENGTH - (string * STRING_SPACING) + FB_OFFSET_BOTTOM
    res = [R9(x=(c + 0.5) * FRET_SPACING + 0.5 + FB_OFFSET_LEFT,
              y=y, rot=0, size=1, op=1, tex='note')
           for c in xrange(FRET_COUNT)]
    return res + [R9(x=(c + 0.5) * FRET_SPACING + 0.5 + FB_OFFSET_LEFT,
                     y=y, rot=0, size=1, op=1, tex='note_%s' % next(notes))
                  for c in xrange(FRET_COUNT)]


def build_fretboard(tuning):
    res = []
    rx = res.extend

    rx(_frets())
    rx(_strings())
    rx(_numbers())
    rx(_tuning(tuning['notes']))
    for c in xrange(STRING_COUNT):
        rx(_notes(c, get_string(tuning['notes'][c], FRET_COUNT)))

    return res