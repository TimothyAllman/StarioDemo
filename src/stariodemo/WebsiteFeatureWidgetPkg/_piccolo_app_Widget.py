"""
Import all of the Tables subclasses in your app here, and register them with
the APP_CONFIG.
"""

import os

from piccolo.conf.apps import AppConfig

from stariodemo.WebsiteFeatureWidgetPkg.DbWidgetModule import WidgetDb

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


APP_CONFIG = AppConfig(
    app_name="WebsiteFeatureWidgetPkg",
    migrations_folder_path=os.path.join(CURRENT_DIRECTORY, "piccolo_migrations"),
    table_classes=[
        WidgetDb,
    ],
    migration_dependencies=[],
    commands=[],
)
