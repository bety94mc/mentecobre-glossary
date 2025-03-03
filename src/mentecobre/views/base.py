from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.decorators.clickjacking import xframe_options_exempt

from mentecobre.models import Glossary

import locale

import logging

from mentecobre.views.errors import error_500

# Get an instance of a logger
logger = logging.getLogger(__name__)

locale.setlocale(locale.LC_TIME, "es_ES")


# Create your views here.
class GlossaryView(View):

    @xframe_options_exempt
    def get(self, request):
        try:
            search = request.GET.get("q", None)
            if search is not None:
                query = search
                object_list = Glossary.objects.filter(
                    Q(wordEn__icontains=query) | Q(wordEs__icontains=query)
                )

            else:
                object_list = None

            return render(
                request,
                "mentecobre/glossary.html",
                context={"object_list": object_list}
            )
        except Exception as ex:
            logger.error("Error - get - GlossaryView")
            logger.error(ex)
            return error_500(request)