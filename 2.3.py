s=0
pupils={
    'Vitaliy': set(['ua', 'ru', 'en', 'fr', 'pl']),
    'Denis': set(['ua', 'ru', 'en', 'fr', 'pl', 'du']),
    'Dyma': set (['ua', 'ru', 'en', 'fr', 'pl', 'du', 'it']),
    'Vlad': set (['ua', 'ru', 'en', 'fr', 'pl', 'du', 'bl']),
    'Vladislav': set (['ua', 'ru', 'en', 'kr', 'pl', 'du', 'bl'])
    }
lang = pupils['Vitaliy']
for i in pupils.keys():
    lang.intersection(pupils[i])
    
    if len(pupils[i])>s:
                        s=len(pupils[i])
print(lang)
print(s)
