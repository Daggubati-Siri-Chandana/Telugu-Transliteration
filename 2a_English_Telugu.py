from __future__ import unicode_literals
from NLP.Assignment1_Transliteration.telugu_transliteration.schemes import roman
from NLP.Assignment1_Transliteration.telugu_transliteration.schemes.brahmic import southern

try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache

# These variables are replicated here for backward compatibility.
# -------------

TELUGU = southern.TELUGU
# TITUS = roman.TITUS
HK = roman.HK
## NOTE: See the Scheme constructor documentation for a few general notes while defining schemes.
SCHEMES = {}
SCHEMES.update(roman.SCHEMES)

BRAHMIC_SCHEMES = {}
BRAHMIC_SCHEMES.update(southern.SCHEMES)


SCHEMES.update(BRAHMIC_SCHEMES)

class SchemeMap(object):
  """Maps one :class:`Scheme` to another. This class grabs the metadata and
  character data required for :func:`transliterate`.

  :param from_scheme: the source scheme
  :param to_scheme: the destination scheme
  """

  def __init__(self, from_scheme, to_scheme):
    """Create a mapping from `from_scheme` to `to_scheme`."""
    self.marks = {}
    self.virama = {}

    self.vowels = {}
    self.consonants = {}
    self.non_marks_viraama = {}
    self.from_scheme = from_scheme
    self.to_scheme = to_scheme
    self.max_key_length_from_scheme = max(len(x) for g in from_scheme
                                          for x in from_scheme[g])

    for group in from_scheme.keys():
      if group not in to_scheme.keys():
        continue
      conjunct_map = {}
      for (k, v) in zip(from_scheme[group], to_scheme[group]):
        conjunct_map[k] = v
        if k in from_scheme.synonym_map:
          for k_syn in from_scheme.synonym_map[k]:
            conjunct_map[k_syn] = v
      if group.endswith('marks'):
        self.marks.update(conjunct_map)
      elif group == 'virama':
        self.virama = conjunct_map
      else:
        self.non_marks_viraama.update(conjunct_map)
        if group.endswith('consonants'):
          self.consonants.update(conjunct_map)
        elif group.endswith('vowels'):
          self.vowels.update(conjunct_map)

  def __str__(self):
    import pprint
    return pprint.pformat({"vowels": self.vowels,
                           "marks":  self.marks,
                           "virama":  self.virama,
                           "consonants": self.consonants})


@lru_cache(maxsize=8)
def _get_scheme_map(input_encoding, output_encoding):
    """Provides a caching layer on top of `SchemeMap` objects to allow faster
    access to scheme maps we've instantiated once.

    :param input_encoding: Input encoding. Must be defined in `SCHEMES`.
    :param output_encoding: Input encoding. Must be defined in `SCHEMES`.
    """
    return SchemeMap(SCHEMES[input_encoding], SCHEMES[output_encoding])

def transliterate(data, _from=None, _to=None, scheme_map=None, **kw):
  """Transliterate `data` with the given parameters::

      output = transliterate('idam adbhutam', HK, DEVANAGARI)

  Each time the function is called, a new :class:`SchemeMap` is created
  to map the input scheme to the output scheme. This operation is fast
  enough for most use cases. But for higher performance, you can pass a
  pre-computed :class:`SchemeMap` instead::

      scheme_map = SchemeMap(SCHEMES[HK], SCHEMES[DEVANAGARI])
      output = transliterate('idam adbhutam', scheme_map=scheme_map)

  :param data: the data to transliterate
  :param scheme_map: the :class:`SchemeMap` to use. If specified, ignore
                     `_from` and `_to`. If unspecified, create a
                     :class:`SchemeMap` from `_from` to `_to`.
  """
  if scheme_map is None:
    scheme_map = _get_scheme_map(_from, _to)
  options = {
    'togglers': {'##'},
    'suspend_on': set('<'),
    'suspend_off': set('>')
  }
  options.update(kw)

  from NLP.Assignment1_Transliteration.telugu_transliteration.roman_mapper import _roman
  func = _roman
  return func(data, scheme_map, **options)


def get_standard_form(data, scheme_name):
  return transliterate(data=transliterate(data=data, _from=scheme_name, _to=DEVANAGARI), _from=DEVANAGARI, _to=scheme_name)

data = 'the men are over there'
print("English Sentence: ",data)
print("Transliterated text in Telugu: ",transliterate(data, HK, TELUGU))
