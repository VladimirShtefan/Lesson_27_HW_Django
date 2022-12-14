import json

from django.http import JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from rest_framework.exceptions import ValidationError

from ads.models import Ads, AdsSerializer


def index(request):
    if request.method == 'GET':
        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdsListView(ListView):
    model = Ads

    def get(self, request, *args, **kwargs):
        super(AdsListView, self).get(request, *args, **kwargs)
        ads_serializer = AdsSerializer(self.object_list, many=True)
        return JsonResponse(ads_serializer.data, safe=False, status=200)

    def post(self, request):
        data = json.loads(request.body)
        serializer = AdsSerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError:
            return JsonResponse(serializer.errors, safe=False, status=422)
        serializer.save()
        return JsonResponse(serializer.data, safe=False)


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        try:
            super(AdsDetailView, self).get(request, *args, **kwargs)
        except Http404 as error:
            return JsonResponse({'error': error.args}, status=404)
        ads_serializer = AdsSerializer(self.object)
        return JsonResponse(ads_serializer.data, safe=False, status=200)


