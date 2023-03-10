from django.db import models
from collections import defaultdict
# from .serializers import BankSerializer
# Now you can access MyClass without any circular import issues


# Create your models here.

class BaseService(models.Model):
    '''
    it is abstract Class for all services
    '''
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    image = models.URLField()
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        abstract = True

    @classmethod
    def get_all_services_by_location(cls, location):
        '''
        it get all services as dict
        key: the service
        value: is the object that match location
        '''
        result = {}
        # child is the subclass of services that mean it is service
        for child in cls.__subclasses__():
            result[child] = child.get_by_location(location)
        return result

    @classmethod
    def get_by_location(cls, location):
        '''
        it is used with the service not services
        '''
        return cls.objects.filter(location__icontains=location)
    
    def __str__(self) -> str:
        return f'Service {self.__class__.__name__}: {self.name}'
    

    


class Bank(BaseService):
    link = models.URLField()
    telephone = models.CharField(max_length=25, null=True, blank=True)

    


class Hotal(BaseService):
    review = models.SmallIntegerField()
    cleanlinsess_review = models.SmallIntegerField(null=True, blank=True)
    service_review = models.SmallIntegerField(null=True, blank=True)
    value_review = models.SmallIntegerField(null=True, blank=True)
    language_spoken = models.CharField(max_length=200)

 


class Restraunt(BaseService):
    telephone = models.CharField(max_length=25, null=True, blank=True)
    website = models.CharField(max_length=250, null=True, blank=True)
    open_from = models.TimeField(null=True, blank=True)
    open_to = models.TimeField(null=True, blank=True)
    rating = models.SmallIntegerField()
    cuisines = models.TextField(null=True, blank=True)
    features = models.TextField(null=True, blank=True)
    meals = models.TextField(null=True, blank=True)
    type_r = models.CharField(max_length=150, null=True, blank=True)
    menu = models.URLField(null=True, blank=True)

    



# from difflib import SequenceMatcher 

# objects = YourModel.objects.all() 
# similar_results = [] 

# for obj in objects:
#     ratio = SequenceMatcher(None, obj.name, 'word_to_compare').ratio()
#     if ratio >= 0.1: # set the threshold for cutting off results
#         similar_results.append(obj) 

# print(similar_results)


