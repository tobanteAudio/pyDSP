'''Parameter classes
'''
import abc


class AudioParameter:
    '''Base class for all parameter types
    '''

    def __init__(self, identifier: str, name: str):
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

    @property
    @abc.abstractmethod
    def default_value(self):
        '''Returns the default value
        '''


class AudioParameterBool(AudioParameter):
    '''Parameter of type bool
    '''

    def __init__(self, identifier: str, name: str, default_val: bool):
        super().__init__(identifier, name)
        self._value = default_val
        self._default_value = default_val

    @property
    def value(self):
        '''Returns the current value
        '''
        return self._value

    @property
    def default_value(self):
        '''Returns the default value
        '''
        return self._default_value
