import simplejson as json
import yaml
import toml
try:
    filename="convert"
    f = open(filename+'.yaml', 'r')
    yamlData = yaml.load(f)
    f.close()
except FileNotFoundError:('File not find')

ff = open("convert2"+'.toml', 'w+')
tomlData = {'func':'\t', 'arr':'','null':'', 'bool1':'','bool2':'', 'string':'','fred':'', 'emptyArray':'','emptyObject':'', 'emptyString':''}
tomlData['func'] = yamlData['func']
tomlData['arr'] = yamlData['arr']
tomlData['null'] = yamlData['null']
tomlData['bool1'] = yamlData['bool1']
tomlData['bool2'] = yamlData['bool2']
tomlData['string'] = yamlData['string']
tomlData['fred'] = yamlData['fred']
tomlData['emptyArray'] = yamlData['emptyArray']
tomlData['emptyObject'] = yamlData['emptyObject']
tomlData['emptyString'] = yamlData['emptyString']
tomlData['code'] = yamlData['code']
tomlData['base64'] = yamlData['base64']
toml.dump(tomlData, ff)