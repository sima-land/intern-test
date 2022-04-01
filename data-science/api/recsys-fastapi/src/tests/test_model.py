from app.utils import load_model


def test_model():
    model_file = "model/model_popular.pkl"
    recommender = load_model(model_file)
    data = recommender.recommend_for_user(123)
    item_ids = [item["item_id"] for item in data]
    item_ids_expected = [
        9728, 15297, 10440, 14488, 13865, 12192, 341, 4151, 3734, 512
    ]
    assert item_ids == item_ids_expected
