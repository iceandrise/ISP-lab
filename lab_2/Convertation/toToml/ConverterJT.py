import simplejson as json
import toml
try:
    filename="convert"
    f = open(filename+'.json', 'r')
    jsonData = json.load(f)
    f.close()
except FileNotFoundError:('File not find')

filename2=input()
ff = open("convert2"+'.toml', 'w+')
tomlData = {'func':'', 'arr':'','null':'', 'bool1':'','bool2':'', 'string':'','fred':'', 'emptyArray':'','emptyObject':'', 'emptyString':''}
tomlData['func'] = jsonData['func']
tomlData['arr'] = jsonData['arr']
tomlData['null'] = jsonData['null']
tomlData['bool1'] = jsonData['bool1']
tomlData['bool2'] = jsonData['bool2']
tomlData['string'] = jsonData['string']
tomlData['fred'] = jsonData['fred']
tomlData['emptyArray'] = jsonData['emptyArray']
tomlData['emptyObject'] = jsonData['emptyObject']
tomlData['emptyString'] = jsonData['emptyString']
tomlData['code'] = jsonData['code']
tomlData['base64'] = jsonData['base64']
toml.dump(tomlData, ff)