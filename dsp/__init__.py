'''Audio DSP utility classes and functions
'''
from .parameter import AudioParameter, AudioParameterBool
from .processor import AudioProcessor, ProcessorSpec

__all__ = [
    'AudioParameter',
    'AudioParameterBool',
    'AudioProcessor',
    'ProcessorSpec',
]
