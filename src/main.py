from app import app
from routes.banks import banks_router
from routes.categories import categories_router
from routes.payments import payment_types_router
from routes.resources import resources_router
from routes.transactions import transactions_router

app.include_router(banks_router)
app.include_router(transactions_router)
app.include_router(payment_types_router)
app.include_router(categories_router)
app.include_router(resources_router)
