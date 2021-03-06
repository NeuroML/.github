import collections

srefs = collections.OrderedDict()
jrefs = collections.OrderedDict()
pyrefs = collections.OrderedDict()
otherrefs = collections.OrderedDict()

workflows = {}

srefs['NeuroML2'] = 'NeuroML/NeuroML2'
srefs['LEMS'] = 'LEMS/LEMS'

jrefs['jLEMS'] = 'LEMS/jLEMS'
jrefs['org.neuroml.model.injectingplugin'] = 'NeuroML/org.neuroml.model.injectingplugin'
jrefs['org.neuroml1.model'] = 'NeuroML/org.neuroml1.model'
jrefs['org.neuroml.model'] = 'NeuroML/org.neuroml.model'
jrefs['org.neuroml.export'] = 'NeuroML/org.neuroml.export'
jrefs['org.neuroml.import'] = 'NeuroML/org.neuroml.import'
jrefs['jNeuroML'] = 'NeuroML/jNeuroML'

pyrefs['pylems'] = 'LEMS/pylems'
pyrefs['libNeuroML'] = 'neuralensemble/libNeuroML'
pyrefs['pyNeuroML'] = 'NeuroML/pyNeuroML'
pyrefs['NeuroMLlite'] = 'NeuroML/NeuroMLlite'


otherrefs['NeuroML Documentation'] = 'NeuroML/Documentation'
workflows['NeuroML Documentation'] = ['prs.yaml', 'publish.yml']

otherrefs['OMV'] = 'OpenSourceBrain/osb-model-validation'
otherrefs['OpenCortex'] = 'OpenSourceBrain/OpenCortex'
otherrefs['pyelectro'] = 'neuralensemble/pyelectro'
otherrefs['neurotune'] = 'neuralensemble/neurotune'
otherrefs['neuroConstruct'] = 'neuralensemble/neuroConstruct'
