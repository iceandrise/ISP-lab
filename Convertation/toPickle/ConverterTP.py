import simplejson as json
import pickle
import toml
try:
    filename="convert"
    f = open(filename+'.toml', 'r')
    tomlData = toml.load(f)
    f.close()
except FileNotFoundError:('File not find')

ff = open("convert2"+'.pkl', 'wb')
pickleData = {'func':'\t', 'arr':'','null':'', 'bool1':'','bool2':'', 'string':'','fred':'', 'emptyArray':'','emptyObject':'', 'emptyString':''}
pickleData['func'] = tomlData['func']
pickleData['arr'] = tomlData['arr']
pickleData['null'] = tomlData['null']
pickleData['bool1'] = tomlData['bool1']
pickleData['bool2'] = tomlData['bool2']
pickleData['string'] = tomlData['string']
pickleData['fred'] = tomlData['fred']
pickleData['emptyArray'] = tomlData['emptyArray']
pickleData['emptyObject'] = tomlData['emptyObject']
pickleData['emptyString'] = tomlData['emptyString']
pickleData['code'] = tomlData['code']
pickleData['base64'] = tomlData['base64']
pickle.dump(pickleData, ff)