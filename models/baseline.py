import torch.nn as nn
import torch.nn.functional as f


class Baseline(nn.Module):
    """Baseline model based on CNN from Assignment 4"""

    def __init__(self, num_classes):
        super(Baseline, self).__init__()
        self.kernel_count = 5
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=self.kernel_count, kernel_size=3, stride=1)
        self.conv2 = nn.Conv2d(in_channels=self.kernel_count, out_channels=self.kernel_count, kernel_size=3, stride=1)
        self.pool = nn.MaxPool2d(2, stride=2)
        # self.fc1 = nn.Linear(10 * 23 * 12, 32)
        # self.fc1 = nn.Linear(10 * 73 * 41, 32)
        self.fc1 = nn.Linear(self.kernel_count * 54 * 54, 32)
        self.fc2 = nn.Linear(32, num_classes)

    def forward(self, x):
        x = self.pool(f.relu(self.conv1(x)))
        x = self.pool(f.relu(self.conv2(x)))
        # x = x.view(-1, 10 * 23 * 12)
        # x = x.view(-1, 10 * 73 * 41)
        x = x.view(-1, self.kernel_count * 54 * 54)
        x = f.relu(self.fc1(x))
        x = self.fc2(x)

        return x
