from fastapi import FastAPI

app = FastAPI(root_path="/api/v1", debug=True, title="Financial Transactions API")
