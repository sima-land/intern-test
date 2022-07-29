import unittest
import torch
from model.model import RecSysNet, UserNet, ItemNet


class TestModel(unittest.TestCase):

    def setUp(self):
        self.model_user = UserNet()
        self.model_item = ItemNet()
        self.model = RecSysNet(self.model_item, self.model_user)
        self.batch_size = 256
        self.out_model = 384
        self.x1 = torch.randn(self.batch_size, 8813)
        self.x3 = torch.randn(self.batch_size, 16)
        self.x4 = torch.randn(self.batch_size, 6136)

    def testForward(self):
        self.assertEqual(self.model.forward(self.x1, self.x1, self.x3, self.x4).shape.numel(),
                         self.batch_size*self.out_model)
        self.assertEqual(str(self.model.forward(self.x1, self.x1, self.x3, self.x4).shape),
                         f'torch.Size([{self.batch_size}, {self.out_model}])')


if __name__ == '__main__':
    unittest.main()
