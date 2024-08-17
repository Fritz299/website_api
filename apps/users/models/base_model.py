from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.main import generate_uuid


class BaseModel(models.Model):
    """
    Abstract model that contains common fields for all models, including tracking fields
    for creation and modification by users.
    """
    id = models.UUIDField(
        primary_key=True,
        default=generate_uuid,
        editable=False,
        help_text=_("Unique identifier for this object")
    )
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="created_%(class)s_set",
        editable=False,
        null=True,
        on_delete=models.SET_NULL
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="updated_%(class)s_set",
        editable=False,
        null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        abstract = True
