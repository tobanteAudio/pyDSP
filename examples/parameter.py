import dsp


class PassThruProcessor(dsp.AudioProcessor):
    '''ToDo
    '''

    def prepare(self, spec: dsp.ProcessorSpec) -> None:
        '''ToDo
        '''

    def process(self, buffer):
        '''ToDo
        '''
        return buffer

    def release(self) -> None:
        '''ToDo
        '''


effect = PassThruProcessor()
param = dsp.AudioParameterBool('1', 'name', False)
effect.add_parameter(parameter=param)


state = effect.state
print(f"state: {state['1']}, fx: {effect.parameters['1'].value}")
effect.parameters['1'].value = True
print(f"state: {state['1']}, fx: {effect.parameters['1'].value}")
effect.state = state
print(f"state: {state['1']}, fx: {effect.parameters['1'].value}")
