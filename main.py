#'COUNTRIES'
# with open('apps/users/utils/filename.txt') as f:
#      a = tuple(f.readlines())
from decouple import config
a = config('COUNTRIES')
for i in a:
    i.replace('\\n','')

print(type(a), len(a))

print(a)