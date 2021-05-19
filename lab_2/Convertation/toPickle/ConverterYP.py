import simplejson as json
import yaml
import pickle
try:
    filename="convert"
    f = open(filename+'.yaml', 'r')
    yamlData = yaml.load(f)
    f.close()
except FileNotFoundError:('File not find')

ff = open("convert2"+'.pkl', 'wb')
pickleData = {'func':'\t', 'arr':'','null':'', 'bool1':'','bool2':'', 'string':'','fred':'', 'emptyArray':'','emptyObject':'', 'emptyString':''}
pickleData['func'] = yamlData['func']
pickleData['arr'] = yamlData['arr']
pickleData['null'] = yamlData['null']
pickleData['bool1'] = yamlData['bool1']
pickleData['bool2'] = yamlData['bool2']
pickleData['string'] = yamlData['string']
pickleData['fred'] = yamlData['fred']
pickleData['emptyArray'] = yamlData['emptyArray']
pickleData['emptyObject'] = yamlData['emptyObject']
pickleData['emptyString'] = yamlData['emptyString']
pickleData['code'] = yamlData['code']
pickleData['base64'] = yamlData['base64']
pickle.dump(pickleData, ff)