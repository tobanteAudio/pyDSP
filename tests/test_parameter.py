# pylint: skip-file
import pytest

import dsp


@pytest.mark.parametrize("test_case", [
    ('test'),
    ('foo'),
    ('bar'),
    ('baz'),
])
def test_audio_parameter_identifier(test_case):
    param = dsp.AudioParameter(test_case, 'name')
    assert param.identifier == test_case


@pytest.mark.parametrize("test_case", [
    ('test'),
    ('foo'),
    ('bar'),
    ('baz'),
])
def test_audio_parameter_name(test_case):
    param = dsp.AudioParameter('id', test_case)
    assert param.name == test_case


@pytest.mark.parametrize("test_case", [
    (False),
    (True),
])
def test_audio_parameter_bool_value(test_case):
    param = dsp.AudioParameterBool('id', 'name', test_case)
    assert param.value == test_case
    assert param.default_value == test_case
