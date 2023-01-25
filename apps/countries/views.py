from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from apps.countries.serializers import CountrySerializer
from apps.countries.models import CountryModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests , json , datetime

@api_view(['GET'])
def fill(request):
    if request.method == 'GET':
        url = 'https://restcountries.com/v3/all?fields=name,capital,currencies,continents,flags,languages'
        rest = requests.get(url).content
        jsonA = json.loads(rest)

        errs = []
        for item in jsonA:
        # item = jsonA[0]

            #currencies
            currencies = ''
            for it in item['currencies']:
                currencies += ' '+it+': '+item['currencies'][it]['name']+','
            currencies = currencies[:-1]+'.'

            #continents
            continents = ''
            for cont in item['continents']:
                continents += ' '+cont+','
            continents = continents[:-1]+'.'
            #"languages"
            languages =''
            for cont in item['languages']:
                languages += ' '+item['languages'][cont]+','
            languages = languages[:-1]+'.'
            #capital
            
            capital = ''
            if item['capital'] == []:
                capital ='none'
            else:
                capital= item['capital'][0]
            objec = {
                'name': item['name']['common'],
                'official':item['name']['official'],
                'capital':capital,
                'currency':currencies.strip(' '),
                'continent':continents,
                'languages': languages,
                'flagSVG':item['flags'][0],
                'flagPNG':item['flags'][1]

            }
            
            # errs.append(objec)
            serializer_class=CountrySerializer(data = objec)
            if serializer_class.is_valid():
                serializer_class.save()
            else:
                errs.append(f'error: {serializer_class.errors}\n{serializer_class.data}\n')
                print(serializer_class.errors)
        if len(errs) > 0:
            log_file = open(f'./error.log', 'a')
            time = str(datetime.datetime.now())
            log_file.write(f'Fail AT {time[:-7]}=======\n')
            for err in errs:
                log_file.write(err)
            log_file.close()

        #return Response(jsonr,200)
        
        return Response(errs)
        #return Response(objec)
    return Response('hok')

class CountriesViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    serializer_class = CountrySerializer
    queryset = CountryModel.objects.all()

    def list(self, request, *args, **kwargs):
        
        

        return super().list(request, *args, **kwargs)

    
