import simplejson as json
import yaml
import toml
try:
    filename="convert"
    f = open(filename+'.toml', 'r')
    tomlData = toml.load(f)
    f.close()
except FileNotFoundError:('File not find')

ff = open("convert2"+'.yaml', 'w+')
yamlData = {'func':'\t', 'arr':'','null':'', 'bool1':'','bool2':'', 'string':'','fred':'', 'emptyArray':'','emptyObject':'', 'emptyString':''}
yamlData['func'] = tomlData['func']
yamlData['arr'] = tomlData['arr']
yamlData['null'] = tomlData['null']
yamlData['bool1'] = tomlData['bool1']
yamlData['bool2'] = tomlData['bool2']
yamlData['string'] = tomlData['string']
yamlData['fred'] = tomlData['fred']
yamlData['emptyArray'] = tomlData['emptyArray']
yamlData['emptyObject'] = tomlData['emptyObject']
yamlData['emptyString'] = tomlData['emptyString']
yamlData['code'] = tomlData['code']
yamlData['base64'] = tomlData['base64']
yaml.dump(yamlData, ff)