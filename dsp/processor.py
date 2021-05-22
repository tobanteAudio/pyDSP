'''ToDo
'''
import abc
import typing

import numpy as np

from .parameter import AudioParameter


class ProcessorSpec:
    '''ToDo
    '''

    def __init__(
            self,
            sample_rate: float = 44100.0,
            block_size: int = 1024,
            channels: int = 1
    ):
        self._sample_rate = sample_rate
        self._block_size = block_size
        self._channels = channels

    @property
    def sample_rate(self):
        '''ToDo
        '''
        return self._sample_rate

    @property
    def block_size(self):
        '''ToDo
        '''
        return self._block_size

    @property
    def channels(self):
        '''ToDo
        '''
        return self._channels


class AudioProcessor(abc.ABC):
    '''Base class for all audio effects & analyzers
    '''
    _spec: ProcessorSpec = ProcessorSpec()
    _parameters: typing.Dict[(str, AudioParameter)] = {}

    @abc.abstractmethod
    def prepare(self, spec: ProcessorSpec):
        '''Needs to be implemented in the child class
        '''

    @abc.abstractmethod
    def process(self, buffer: np.ndarray) -> np.ndarray:
        '''Needs to be implemented in the child class
        '''

    @abc.abstractmethod
    def release(self) -> None:
        '''Needs to be implemented in the child class
        '''

    @property
    def spec(self) -> ProcessorSpec:
        '''Returns the current processor specs
        '''
        return self._spec

    @property
    def parameters(self) -> typing.Dict[(str, AudioParameter)]:
        '''Returns the current processor specs
        '''
        return self._parameters

    def add_parameter(self, parameter: AudioParameter) -> None:
        '''Adds a parameter to the list of parameters for this processor.
        '''
        self._parameters[parameter.identifier] = parameter

    @property
    def state(self) -> typing.Dict:
        '''Returns the current processor state
        '''
        state = {}
        for key, param in self.parameters.items():
            state[key] = param.value
        return state

    @state.setter
    def state(self, state: typing.Dict) -> None:
        '''Sets the current processor state
        '''
        for key, value in state.items():
            self._parameters[key].value = value
