# pylint: skip-file
import pytest

import numpy as np

import dsp


@pytest.mark.parametrize("tc", [
    ({'sr': 44100.0, 'bs': 128, 'ch': 1}),
    ({'sr': 48000.0, 'bs': 512, 'ch': 1}),
    ({'sr': 88200.0, 'bs': 1024, 'ch': 2}),
    ({'sr': 96000.0, 'bs': 32, 'ch': 4}),
])
def test_processor_spec(tc):
    spec = dsp.ProcessorSpec(
        sample_rate=tc['sr'],
        block_size=tc['bs'],
        channels=tc['ch'],
    )
    assert spec.sample_rate == tc['sr']
    assert spec.block_size == tc['bs']
    assert spec.channels == tc['ch']


class TestProcessor(dsp.AudioProcessor):
    '''Base class for all audio effects & analyzers
    '''

    def prepare(self, spec: dsp.ProcessorSpec) -> None:
        '''Needs to be implemented in the child class
        '''

    def process(self, buffer: np.ndarray) -> np.ndarray:
        '''Needs to be implemented in the child class
        '''
        return buffer

    def release(self) -> None:
        '''Needs to be implemented in the child class
        '''


def test_audio_processor():
    effect = TestProcessor()
    assert effect.spec.sample_rate == 44100.0
    assert effect.spec.block_size == 1024
    assert effect.spec.channels == 1

    param = dsp.AudioParameterBool('1', 'name', False)
    effect.add_parameter(parameter=param)

    assert len(effect.parameters) == 1
    assert effect.parameters['1'].identifier == '1'
    assert effect.parameters['1'].name == 'name'
    assert not effect.parameters['1'].value
    assert not effect.parameters['1'].default_value

    effect.prepare(dsp.ProcessorSpec())
    assert effect.process(None) is None

    buffer = np.zeros((1024,), dtype=np.float64)
    assert type(effect.process(buffer)) == np.ndarray

    state = effect.state
    assert not effect.parameters['1'].value
    effect.parameters['1'].value = True
    assert effect.parameters['1'].value

    effect.state = {'1': False}
    assert not effect.parameters['1'].value

    effect.parameters['1'].value = True
    assert effect.parameters['1'].value

    effect.state = state
    assert not effect.parameters['1'].value
