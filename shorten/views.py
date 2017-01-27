from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.shortcuts import redirect

from shorten.models import URLShortenerModel
from shorten.shortener import Base64Encoder
from shorten.serializers import URLShortenerSerializer


class URLShortenView(APIView):
    def get(self, request, url, format=None):
        try:
            latest_entry_id = URLShortenerModel.objects.values_list(
                'id', flat=True).latest('created_at')
        except:
            latest_entry_id = 0

        encoded_string = Base64Encoder().encode_num(latest_entry_id)
        serializer = URLShortenerSerializer(data={
            'original_url': url,
            'short_url': "{0}/{1}".format(request.get_host(), encoded_string)
        })

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data,
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class URLRedirectView(APIView):
    def get(self, request, urlhash, format=None):
        url_id = Base64Encoder().decode_num(urlhash)

        original_url = URLShortenerModel.objects.values_list(
            'original_url', flat=True).get(pk=url_id+1)
        return redirect(original_url, permanent=True)
