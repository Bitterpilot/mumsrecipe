from django.db import models
from django.utils.translation import gettext as _


class LandingPage(models.Model):
    business_name = models.CharField(_("Business Name"), max_length=200)
    about = models.TextField(_("About"))
    main_img = models.ImageField(_("Center piece image"), upload_to="media/upload/landingpage")
