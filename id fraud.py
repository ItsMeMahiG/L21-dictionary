data={'id1': 
     {'name': ['sarah'], 
      'class': [11],
      'subintegration': ['english, math, science']},
      'id2': 
     {'name': ['tom'], 
      'class': [8],
      'subintegration': ['physics, math, science']},
      'id3': 
     {'name': ['sarah'], 
      'class': [11],
      'subintegration': ['english, math, science']},
     'id4' : 
     {'name': ['mahi'], 
      'class': [6],
      'subintegration': ['computer, math, science']},
        }

result={} 
for key,value in data.items() :
    if value not in result.values() :
        result[key]=value


print(result)