from django.db import models
from django.utils.translation import ugettext_lazy as _


class FileBrowser(models.Model):
    permission_verbose_name = 'Файловый менеджер'

    class Meta:
        managed = False
        verbose_name = _("FileBrowser")
        verbose_name_plural = _("FileBrowser")
        permissions = (("use_filebrowser", "Can use Filebrowser"),)

