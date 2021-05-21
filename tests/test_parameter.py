# pylint: skip-file
import pytest

from pyDSP import EffectParameter


@pytest.mark.parametrize("test_case, expected", [
    ('test', 'test'),
])
def test_effect_parameter_id(test_case, expected):
    param = EffectParameter(test_case, test_case)
    assert param.id == expected
