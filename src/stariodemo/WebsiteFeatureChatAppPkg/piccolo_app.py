"""
Import all of the Tables subclasses in your app here, and register them with
the APP_CONFIG.
"""

import os

from piccolo.conf.apps import AppConfig

from stariodemo.WebsiteFeatureChatAppPkg.ChatAppMessageDbModule import ChatAppMessageDb
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUserDbModule import ChatAppUserDb

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


APP_CONFIG = AppConfig(
    app_name="WebsiteFeatureChatAppPkg",
    migrations_folder_path=os.path.join(CURRENT_DIRECTORY, "piccolo_migrations"),
    table_classes=[
        ChatAppUserDb,
        ChatAppMessageDb,
    ],
    migration_dependencies=[],
    commands=[],
)
