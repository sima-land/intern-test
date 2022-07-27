import torch
import torch.nn as nn

n_out = 128
item_input = 8813
user_input = 16
user_inter_input = 6136


class ItemNet(nn.Module):
    def __init__(self):
        super(ItemNet, self).__init__()

        self.linear_in = nn.Sequential(
            nn.Linear(item_input, n_out, bias=False),
            nn.ReLU())

        self.linear_2 = nn.Sequential(
            nn.Linear(n_out, n_out, bias=False),
            nn.ReLU())

        self.linear_out = nn.Sequential(
            nn.Linear(n_out, n_out, bias=False))

    def forward(self, x):
        x = self.linear_in(x)
        linear2_out = self.linear_2(x)
        output = self.linear_out(linear2_out + x)

        return output


class UserNet(nn.Module):
    def __init__(self):
        super(UserNet, self).__init__()
        self.linear1_feat = nn.Sequential(
            nn.Linear(user_input, n_out, bias=False),
            nn.ReLU())

        self.linear1_inter = nn.Sequential(
            nn.Linear(user_inter_input, n_out, bias=False),
            nn.ReLU())

        self.linear2_feat = nn.Sequential(
            nn.Linear(n_out, n_out, bias=False),
            nn.ReLU())

        self.linear_out = nn.Sequential(
            nn.Linear(2 * n_out, n_out, bias=False))

    def forward(self, feat_input, inter_input):
        skip_feat = self.linear1_feat(feat_input)
        inter_out = self.linear1_inter(inter_input)
        feat_out = self.linear2_feat(skip_feat) + skip_feat
        combined = torch.cat((feat_out, inter_out), dim=1)
        output = self.linear_out(combined)

        return output


class RecSysNet(nn.Module):
    def __init__(self, model_item, model_user):
        super(RecSysNet, self).__init__()
        self.model_item = model_item
        self.model_user = model_user

    def forward(self, x1, x2, x3, x4):
        item_out_neg = self.model_item(x1)
        item_out_pos = self.model_item(x2)
        user_out = self.model_user(x3, x4)
        output = torch.cat((user_out, item_out_pos, item_out_neg), dim=1)

        return output
