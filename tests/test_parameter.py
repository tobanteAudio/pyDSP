# pylint: skip-file
import pytest

from pyDSP import EffectParameter


@pytest.mark.parametrize("test_case, expected", [
    ('test', 'test'),
    ('foo', 'foo'),
    ('bar', 'bar'),
    ('baz', 'baz'),
])
def test_effect_parameter_id(test_case, expected):
    param = EffectParameter(test_case, '')
    assert param.id == expected


@pytest.mark.parametrize("test_case, expected", [
    ('test', 'test'),
    ('foo', 'foo'),
    ('bar', 'bar'),
    ('baz', 'baz'),
])
def test_effect_parameter_name(test_case, expected):
    param = EffectParameter('', test_case)
    assert param.name == expected
