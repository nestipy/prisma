import uvicorn

from app_module import AppModule
from nestipy.core import NestipyFactory
from nestipy.openapi import DocumentBuilder, SwaggerModule

app = NestipyFactory.create(AppModule)

document = (DocumentBuilder()
            .set_title("Nestipy Prisma")
            .set_description("API Schema to interact with prisma db")
            .build())
SwaggerModule.setup('api', app, document)
if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
