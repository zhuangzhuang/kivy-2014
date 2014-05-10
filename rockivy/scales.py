from abc import ABCMeta, abstractproperty

from .tuning import get_seq

(S, T, I3) = range(3)


def get_notes(root_note, size):
    notes = get_seq(root_note)
    res = [root_note]
    for sz in size:
        for c in xrange(sz):
            next(notes)
        res.append(next(notes))
    return res


class BaseSeq(object):
    __metaclass__ = ABCMeta

    def __init__(self, root_note):
        self.root_note = root_note
        self.notes = set(get_notes(root_note, self.size))

    def __unicode__(self):
        return '%s %s' % (self.root_note.replace('#', u'\u266f'), self.cname)

    def nop(self):
        pass

    name = cname = size = abstractproperty(nop)


class Major(BaseSeq):
    '''Major Scale'''
    name = cname = __doc__
    size = (T, T, S, T, T, T, S)


class Minor(BaseSeq):
    '''Minor Scale'''
    name = cname = __doc__
    size = (T, S, T, T, S, T, T)


class Blues(BaseSeq):
    '''Blues Scale'''
    name = cname = __doc__
    size = (I3, T, S, S, I3, T)


class PentatonicMajor(BaseSeq):
    '''Pentatonic Major'''
    name = __doc__
    cname = 'Major Pentatonic Scale'
    size = (T, T, I3, T, I3)


class PentatonicMinor(BaseSeq):
    '''Pentatonic Minor'''
    name = __doc__
    cname = 'Minor Pentatonic Scale'
    size = (I3, T, T, I3, T)

SCALES = (Major, Minor, PentatonicMajor, PentatonicMinor, Blues)
