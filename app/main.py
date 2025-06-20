from app.routers import products, categories, carts, users, auth, accounts
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


description = """
Welcome to the E-commerce API! 🚀

This API provides a comprehensive set of functionalities for managing your e-commerce platform.

Key features include:

- **Crud**
	- Create, Read, Update, and Delete endpoints.
- **Search**
	- Find specific information with parameters and pagination.
- **Auth**
	- Verify user/system identity.
	- Secure with Access and Refresh tokens.
- **Permission**
	- Assign roles with specific permissions.
	- Different access levels for User/Admin.
- **Validation**
	- Ensure accurate and secure input data.
"""

app = FastAPI(
            swagger_ui_parameters={
            "syntaxHighlight.theme": "monokai",
            "layout": "BaseLayout",
            "filter": True,
            "tryItOutEnabled": True,
            "onComplete": "Ok"
        },
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="E-Commerce API",
        description=description,
        version="1.0.0",
        contact={
            "name": "Yoqubjonov Omonjon",
            "url": "https://github.com/Bronnzy",
        },
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    openapi_schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

app.include_router(products.router)
app.include_router(categories.router)
app.include_router(carts.router)
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(auth.router)