from django.apps import AppConfig


class ShopConfig(AppConfig):
    """
    Configuration class for the 'shop' application.

    This class provides configuration for the 'shop' Django application,
    including settings for the default auto field type used for models.

    Attributes:
    :param default_auto_field: The type of auto field to use for models on the application
    :type default_auto_fields: str
    :param name: The name of the application
    :type name: str
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'

