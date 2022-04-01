import pickle

from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app.model import PopularRecommender


def load_model(path):
    return pickle.load(open(path, "rb"))


def save_model(model, path):
    pickle.dump(model, open(path, "wb"))


model_file = "model/model_popular.pkl"
app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.on_event("startup")
async def startup():
    app.state.recommender = load_model(model_file)


@app.get("/")
def read_form():
    return RedirectResponse("/form/")


@app.get("/form")
async def form_get(request: Request):
    return templates.TemplateResponse(
        "form.html",
        context={"request": request}
    )


@app.post("/form")
async def form_post(request: Request, user_id: int = Form(...)):
    try:
        recommendations = app.state.recommender.recommend_for_user(user_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="User not found")

    return templates.TemplateResponse(
        "form.html",
        context={
            "request": request,
            "recommendations": recommendations,
            "user_id": user_id,
        },
    )

# REST API


@app.get("/api/get_user_recommendations/{user_id}")
async def get_user_recommendations(user_id: int):
    try:
        recommendations = app.state.recommender.recommend_for_user(user_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="User not found")
    return {"recommendations": recommendations}


@app.get("/api/train")
async def train():
    app.state.recommender = PopularRecommender.build_model()
    # cохраняем модель
    save_model(app.state.recommender, model_file)
    return {"message": "Model built"}
