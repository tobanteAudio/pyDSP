# pylint: skip-file
import pytest

import dsp


@pytest.mark.parametrize("test_case, expected", [
    ('test', 'test'),
    ('foo', 'foo'),
    ('bar', 'bar'),
    ('baz', 'baz'),
])
def test_effect_parameter_identifier(test_case, expected):
    param = dsp.AudioParameter(test_case, '')
    assert param.identifier == expected


@pytest.mark.parametrize("test_case, expected", [
    ('test', 'test'),
    ('foo', 'foo'),
    ('bar', 'bar'),
    ('baz', 'baz'),
])
def test_effect_parameter_name(test_case, expected):
    param = dsp.AudioParameter('', test_case)
    assert param.name == expected


@pytest.mark.parametrize("test_case, expected", [
    (False, False),
    (False, False),
])
def test_effect_bool_parameter_value(test_case, expected):
    param = dsp.AudioParameterBool('id', 'name', test_case)
    assert param.value == expected
