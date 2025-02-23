from fastapi import APIRouter
from pydantic import BaseModel

from entities.category import Category
from presenters.category_presenter import CategoryPresenter
from repositories.in_memory.seeds.categories_seed import categories


class CategorySchemaValidation(BaseModel):
    name: str


categories_router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


@categories_router.post("/")
def create_category(category: CategorySchemaValidation):
    new_category = Category(name=category.name)
    categories.append(new_category)
    return new_category


@categories_router.get("/", response_model=list[CategoryPresenter])
def get_categories():
    return categories
