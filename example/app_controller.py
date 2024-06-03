from typing import Annotated
from dataclasses import dataclass

from nestipy.common import Controller, Get, Post, Put, Delete
from nestipy.ioc import Inject, Body, Param
from nestipy.openapi import ApiOkResponse, ApiBody
from app_service import AppService, PostDto


@ApiOkResponse()
@Controller()
class AppController:
    service: Annotated[AppService, Inject()]

    @Get()
    async def get(self) -> str:
        return await self.service.get()

    @ApiBody(PostDto)
    @Post()
    async def post(self, data: Annotated[PostDto, Body()]) -> str:
        return await self.service.post(data=data)

    @ApiBody(PostDto)
    @Put('/{id}')
    async def put(self, _id: Annotated[str, Param('id')], data: Annotated[PostDto, Body()]) -> str:
        return await self.service.put(id_=_id, data=data)

    @Delete('/{id}')
    async def delete(self, _id: Annotated[str, Param('id')]) -> None:
        await self.service.delete(id_=_id)
