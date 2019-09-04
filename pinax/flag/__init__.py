import pkg_resources


default_app_config = "pinax.flag.apps.AppConfig"
__version__ = pkg_resources.get_distribution("pinax-flag").version
