from rest_framework import viewsets
from rest_framework.response import Response
from .models import Brand, Clothes
from .serializers import BrandSerializer, ClothesSerializer


class ClothesViewSet(viewsets.ModelViewSet):
    serializer_class = ClothesSerializer

    def get_queryset(self):
        list_clothes = Clothes.objects.all()
        return list_clothes

    def create(self, request, *args, **kwargs):
        data = request.data
        new_clothes = None
        brand_id = data['brand']['id']

        if brand_id != None:
            clothes_brand = Brand.objects.get(id=data['brand']['id'])
            new_clothes = Clothes.objects.create(
                color=data['color'], material=data['material'], size=data['size'], brand=clothes_brand)

        if brand_id == None:
            brand_name = data['brand']['name']
            brand_country = data['brand']['country']
            clothes_brand = Brand.objects.create(name=brand_name, country=brand_country)
            clothes_brand.save()
            new_clothes = Clothes.objects.create(
                color=data['color'], material=data['material'], size=data['size'], brand=clothes_brand)

        new_clothes.save()

        serializer = ClothesSerializer(new_clothes)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        current_clothes = self.get_object()
        data = request.data
        brand_id = data['brand']['id']
        brand_update = None

        if brand_id != None :
            brand_update = Brand.objects.get(id = brand_id)
            current_clothes.brand = brand_update
        
        if brand_id == None:
            brand_name = data['brand']['name']
            brand_country = data['brand']['country']
            brand_update = Brand.objects.create(name=brand_name, country=brand_country)
            brand_update.save()
            current_clothes.brand = brand_update

        current_clothes.color = data['color']
        current_clothes.material = data['material']
        current_clothes.size = data['size']

        current_clothes.save()

        serializer = ClothesSerializer(current_clothes)

        return Response(serializer.data)


class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer

    def get_queryset(self):
       list_brand = Brand.objects.all()
       return list_brand
