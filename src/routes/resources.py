from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from app import app

resources_router = APIRouter(prefix="/resources", tags=["resources"])

PATHS_API_INTERNAL = ["/docs", "/openapi", "/redoc"]


class ResourceDetail(BaseModel):
    name: str
    description: str


class Resource(BaseModel):
    name: str
    description: str
    resources_details: List[ResourceDetail]


class Dictionary(BaseModel):
    resources: List[Resource]


def find_resource(resources: List[Resource], name: str) -> Resource:
    return next((resource for resource in resources if resource.name == name), None)


@resources_router.get(
    "/",
    name="resources:list",
    description="List all resources available in the application",
    response_model=Dictionary,
)
def get_resources():
    dictionary = Dictionary(resources=[])
    for route in app.routes:
        path = str(route.path).strip("/")

        resource_exist = find_resource(dictionary.resources, path)

        if not resource_exist:
            new_resource = Resource(
                name=path,
                description=f"Managements yours {path}",
                resources_details=[ResourceDetail(name=route.name, description="")],
            )
            dictionary.resources.append(new_resource)
        else:
            resource_exist.resources_details.append(
                ResourceDetail(name=route.name, description="")
            )

    return dictionary
