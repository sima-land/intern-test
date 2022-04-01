import random

import pandas as pd


class PopularRecommender:
    def __init__(self, max_items=10, days=7,
                 item_column="item_id", dt_column="date"):
        self.max_items = max_items
        self.days = days
        self.item_column = item_column
        self.dt_column = dt_column
        self.recommendations = []
        self.recommendations_metainfo = []
        self.users = []

    def fit(self, df):
        self._build_model(df)
        self._load_metainfo()
        self._load_userinfo()

    def _build_model(self, df):
        min_date = df[self.dt_column].max().normalize() \
                   - pd.DateOffset(days=self.days)
        self.recommendations = (
            df.loc[df[self.dt_column] > min_date, self.item_column]
            .value_counts()
            .head(self.max_items)
            .index.values
        )

    def _load_metainfo(self):
        items_df = PopularRecommender.get_df_from_csv("data/items.csv")
        recs_df = pd.DataFrame(self.recommendations, columns=["item_id"])
        df = pd.merge(
            recs_df, items_df,
            left_on="item_id", right_on="item_id", how="left"
        )
        self.recommendations_metainfo = \
            df[["item_id", "title"]].to_dict("records")

    def _load_userinfo(self):
        users_df = PopularRecommender.get_df_from_csv("data/users.csv")
        self.users = users_df["user_id"].unique()

    def recommend_for_user(self, user_id: int, shuffle=False):
        if user_id not in self.users:
            raise KeyError()
        recs = self.recommendations_metainfo
        if shuffle:
            random.shuffle(recs)
        return recs

    @staticmethod
    def get_df_from_csv(title, parse_dates=[]):
        df = pd.read_csv(title, parse_dates=parse_dates)
        return df

    @staticmethod
    def build_model():
        # создаем и обучаем модель
        train = PopularRecommender.get_df_from_csv(
            "data/interactions.csv", parse_dates=["last_watch_dt"]
        )
        pop_model = PopularRecommender(dt_column="last_watch_dt")
        pop_model.fit(train)
        return pop_model
