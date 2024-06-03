from nestipy.common import Module
from nestipy_prisma import PrismaModule
from app_controller import AppController
from app_service import AppService


@Module(
    imports=[
        PrismaModule.for_root()
    ],
    controllers=[AppController],
    providers=[AppService]
)
class AppModule:
    ...
