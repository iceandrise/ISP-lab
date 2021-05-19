import simplejson as json
import pickle
try:
    filename="convert"
    f = open(filename+'.json', 'r')
    jsonData = json.load(f)
    f.close()
except FileNotFoundError:('File not found')

ff = open("convert2"+'.pkl', 'wb')
pickleData = {'func':'', 'arr':'','null':'', 'bool1':'','bool2':'', 'string':'','fred':'', 'emptyArray':'','emptyObject':'', 'emptyString':''}
pickleData['func'] = jsonData['func']
pickleData['arr'] = jsonData['arr']
pickleData['null'] = jsonData['null']
pickleData['bool1'] = jsonData['bool1']
pickleData['bool2'] = jsonData['bool2']
pickleData['string'] = jsonData['string']
pickleData['fred'] = jsonData['fred']
pickleData['emptyArray'] = jsonData['emptyArray']
pickleData['emptyObject'] = jsonData['emptyObject']
pickleData['emptyString'] = jsonData['emptyString']
pickleData['code'] = jsonData['code']
pickleData['base64'] = jsonData['base64']
pickle.dump(pickleData, ff)