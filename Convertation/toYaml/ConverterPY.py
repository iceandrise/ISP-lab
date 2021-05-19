import simplejson as json
import pickle
import yaml
try:
    filename="convert"
    f = open(filename+'.pkl', 'rb')
    pickleData = pickle.load(f)
    f.close()
except FileNotFoundError:('File not find')

filename2=input()
ff = open("convert2"+'.yaml', 'w+')
yamlData = {'func':'\t', 'arr':'','null':'', 'bool1':'','bool2':'', 'string':'','fred':'', 'emptyArray':'','emptyObject':'', 'emptyString':''}
yamlData['func'] = pickleData['func']
yamlData['arr'] = pickleData['arr']
yamlData['null'] = pickleData['null']
yamlData['bool1'] = pickleData['bool1']
yamlData['bool2'] = pickleData['bool2']
yamlData['string'] = pickleData['string']
yamlData['fred'] = pickleData['fred']
yamlData['emptyArray'] = pickleData['emptyArray']
yamlData['emptyObject'] = pickleData['emptyObject']
yamlData['emptyString'] = pickleData['emptyString']
yamlData['code'] = pickleData['code']
yamlData['base64'] = pickleData['base64']
yaml.dump(yamlData, ff)