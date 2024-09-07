from django.apps import AppConfig


class ShopConfig(AppConfig):
    """
    Configuration class for the 'shop' application.

    This class provides configuration for the 'shop' Django application,
    including settings for the default auto field type used for models.

    Attributes:
        default_auto_field (str): The type of auto field to use for models in the application.
        name (str): The name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'

