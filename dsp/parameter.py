'''Parameter classes
'''
import abc


class AudioProcessorParameter:
    '''Base class for all parameter types
    '''

    def __init__(self, identifier: str, name: str) -> None:
        self._identifier = identifier
        self._name = name

    @property
    def identifier(self) -> str:
        '''Returns the parameter id
        '''
        return self._identifier

    @property
    def name(self) -> str:
        '''Returns the parameter display name
        '''
        return self._name

    @property
    @abc.abstractmethod
    def value(self):
        '''Returns the current value
        '''
