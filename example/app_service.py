from dataclasses import dataclass, asdict
from typing import Annotated

from nestipy.common import Injectable
from nestipy.ioc import Inject
from prisma.types import PostCreateInput, PostUpdateInput

from nestipy_prisma import PrismaService


@dataclass
class PostDto:
    title: str
    published: bool
    desc: str


@Injectable()
class AppService:
    prisma: Annotated[PrismaService, Inject()]

    async def get(self):
        result = await self.prisma.post.find_many()
        return [a.model_dump(mode="json") for a in result]

    async def post(self, data: PostDto):
        return (await self.prisma.post.create(
            PostCreateInput(**asdict(data))
        )).model_dump()

    async def put(self, id_: str, data: PostDto):
        return (await self.prisma.post.update(PostUpdateInput(**asdict(data)), where={
            "id": id_
        })).model_dump(mode="json")

    async def delete(self, id_: str):
        return (await self.prisma.post.delete(where={"id": id_})).model_dump(mode="json")
