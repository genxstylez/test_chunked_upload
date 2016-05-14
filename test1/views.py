# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os.path

import zlib

...
@csrf_exempt
def upload(request):
    # print('meta:', request.META)
    decompressed_data=zlib.decompress(request.body, 16+zlib.MAX_WBITS)
    with open('a.jpg', 'wb') as f:
        f.write(request.body)

    return HttpResponse('yes')
