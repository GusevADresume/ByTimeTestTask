from fastapi import FastAPI
from requestScrab import bs4_main
from seleniumScrab import selenium_main
import uvicorn

app = FastAPI()


@app.get("/{parser}")
def start_pars(parser: str):
    if parser == 'bs4':
        return bs4_main()
    elif parser == 'selen':
        return selenium_main()
    else:
        return {"message": "Resource Not Found"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
