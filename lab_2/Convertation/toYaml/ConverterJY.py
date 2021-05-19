import simplejson as json
import yaml
try:
    filename="convert"
    f = open(filename+'.json', 'r')
    jsonData = json.load(f)
    f.close()
except FileNotFoundError:('File not find')

ff = open("convert2"+'.yaml', 'w+')
yamlData = {'func':'', 'arr':'','null':'', 'bool1':'','bool2':'', 'string':'','fred':'', 'emptyArray':'','emptyObject':'', 'emptyString':''}
yamlData['func'] = jsonData['func']
yamlData['arr'] = jsonData['arr']
yamlData['null'] = jsonData['null']
yamlData['bool1'] = jsonData['bool1']
yamlData['bool2'] = jsonData['bool2']
yamlData['string'] = jsonData['string']
yamlData['fred'] = jsonData['fred']
yamlData['emptyArray'] = jsonData['emptyArray']
yamlData['emptyObject'] = jsonData['emptyObject']
yamlData['emptyString'] = jsonData['emptyString']
yamlData['code'] = jsonData['code']
yamlData['base64'] = jsonData['base64']
yaml.dump(yamlData, ff)

