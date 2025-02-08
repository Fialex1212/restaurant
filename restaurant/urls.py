from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

import logging

logger = logging.getLogger(__name__)
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
    path("captcha/", include("captcha.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
