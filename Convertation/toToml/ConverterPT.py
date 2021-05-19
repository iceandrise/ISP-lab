import simplejson as json
import pickle
import toml
try:
    filename="convert"
    f = open(filename+'.pkl', 'rb')
    pickleData = pickle.load(f)
    f.close()
except FileNotFoundError:('File not find')

ff = open("convert2"+'.toml', 'w+')
tomlData = {'func':'\t', 'arr':'','null':'', 'bool1':'','bool2':'', 'string':'','fred':'', 'emptyArray':'','emptyObject':'', 'emptyString':''}
tomlData['func'] = pickleData['func']
tomlData['arr'] = pickleData['arr']
tomlData['null'] = pickleData['null']
tomlData['bool1'] = pickleData['bool1']
tomlData['bool2'] = pickleData['bool2']
tomlData['string'] = pickleData['string']
tomlData['fred'] = pickleData['fred']
tomlData['emptyArray'] = pickleData['emptyArray']
tomlData['emptyObject'] = pickleData['emptyObject']
tomlData['emptyString'] = pickleData['emptyString']
tomlData['code'] = pickleData['code']
tomlData['base64'] = pickleData['base64']
toml.dump(tomlData, ff)