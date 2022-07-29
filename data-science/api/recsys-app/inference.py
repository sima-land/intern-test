from model.model import UserNet, ItemNet, RecSysNet
import numpy as np
import pandas as pd
import torch
import os


class InferenceModel:

    def __init__(self, device: torch.device, model, count_items=10):
        self.count_items = count_items
        self.device = device
        self.model = model
        self.data = self.data_preparation("/data")
        self.item_vec = self.build_items_vec()

    @staticmethod
    def data_preparation(path: str):

        dir_name = os.path.dirname(__file__)
        train_users = pd.read_csv(os.path.join(dir_name + path + "/train_users.csv"))
        train_items = pd.read_csv(os.path.join(dir_name + path + "/train_items.csv"))
        train_interactions = pd.read_csv(os.path.join(dir_name + path + "/train_interactions.csv"))
        items_df = pd.read_csv(os.path.join(dir_name + path + "/items.csv"))

        interactions_matrix = np.zeros((train_interactions.uid.nunique(),
                                        train_interactions.iid.nunique()))

        for user_id, item_id in zip(train_interactions.uid, train_interactions.iid):
            interactions_matrix[user_id, item_id] += 1

        res = interactions_matrix.sum(axis=1)
        for i in range(len(interactions_matrix)):
            interactions_matrix[i] /= res[i]

        dict_data = {'train_users': train_users,
                     'train_items': train_items,
                     'train_interactions': train_interactions,
                     'items_df': items_df,
                     'interactions_matrix': interactions_matrix}

        return dict_data

    def build_items_vec(self) -> np.array:

        path_model = os.path.join(os.path.dirname(__file__) + "/model/RecsysNet.pth")
        self.model.load_state_dict(torch.load(path_model, map_location=self.device))
        self.model.eval()
        items_feats = torch.Tensor(self.data['train_items'].to_numpy())

        with torch.no_grad():

            items_feats = items_feats.to(self.device)

            item_vec = self.model.model_item(items_feats)

        return item_vec

    def relevant_titles(self, dists: np.array) -> pd.DataFrame:

        items_df = self.data['items_df']
        train_interactions = self.data['train_interactions']

        top_id = np.argsort(dists)[:self.count_items]
        item_id_df = train_interactions[["iid", "item_id"]].drop_duplicates().set_index("iid").to_dict()["item_id"]

        top_item_ids = [item_id_df[iid] for iid in top_id]

        rec_titles = items_df.loc[items_df.item_id.isin(top_item_ids)].title
        rec_item_id = items_df.loc[items_df.item_id.isin(top_item_ids)].item_id

        top_rec = pd.concat([rec_titles, rec_item_id], axis=1)

        return top_rec

    def inference(self, user_id: int) -> pd.DataFrame:
        user_feats = torch.Tensor(self.data['train_users'].iloc[user_id].to_numpy())
        user_interaction_vec = torch.Tensor(self.data['interactions_matrix'][user_id])

        path_model = os.path.join(os.path.dirname(__file__) + "/model/RecsysNet.pth")
        self.model.load_state_dict(torch.load(path_model, map_location=self.device))
        self.model.eval()

        with torch.no_grad():
            user_feats = user_feats.unsqueeze(0).to()

            user_interaction_vec = user_interaction_vec.unsqueeze(0).to(self.device)

            user_vec = self.model.model_user(user_feats, user_interaction_vec)

        ED = torch.nn.PairwiseDistance(p=2)
        dists = ED(user_vec, self.item_vec)
        dists = dists.cpu().detach().numpy()
        top_rec = self.relevant_titles(dists=dists)

        return top_rec


def build_model(count_items=10) -> InferenceModel:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = RecSysNet(ItemNet(), UserNet())

    inf_model = InferenceModel(device=device, model=model, count_items=count_items)

    return inf_model
