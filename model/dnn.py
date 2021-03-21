import torch
import torch.nn as nn
from torch import optim
import time

from model.dataset_mediapipe import CusDataset

'''
    考虑的问题：mp对手势关键点的识别如果效果不好不知道影响大不大，答案是很大；光线较暗的情况下手部关键点的检测和追踪很不友好
    感觉如果是TSM，说不定已经在mobilenet网络中学到了手势关键点这一信息，反而还能加强网络的鲁棒性。
    单双手输入问题，是否要训练两个网络？
    输入网络的size为（b,n,21,6）,但是3维数据的lstm好像不太好处理, 2*16*11*3 = 1056
'''

class DNN(nn.Module):
    def __init__(self, input_dim = 1056, output_dim=13, n_hidden_1 = 128,n_hidden_2=64):
        super(DNN, self).__init__()

        self.layer1 = nn.Sequential(nn.Linear(input_dim, n_hidden_1), nn.BatchNorm1d(n_hidden_1), nn.ReLU(True),nn.Dropout(0.4))
        self.layer2 = nn.Sequential(nn.Linear(n_hidden_1, n_hidden_2), nn.BatchNorm1d(n_hidden_2), nn.ReLU(True),nn.Dropout(0.2))
        self.layer3 = nn.Sequential(nn.Linear(n_hidden_2, output_dim))


    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        return x
net = DNN()
print(net)
epoch = 100
# Training
def train(epoch,criterion,optimizer):
    print('\nEpoch: %d' % epoch)
    net.train()
    train_loss = 0
    correct = 0
    total = 0
    for batch_idx, (inputs, targets) in enumerate(trainloader):
        inputs, targets = inputs.to('cpu'), targets.to('cpu')
        optimizer.zero_grad()
        outputs = net(torch.tensor(inputs,dtype=torch.float32))
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

        train_loss += loss.item()
        _, predicted = outputs.max(1)
        total += targets.size(0)
        correct += predicted.eq(targets).sum().item()
        if batch_idx % 40 == 0:
            print("train:")
            print(batch_idx, len(trainloader), 'Loss: %.3f | Acc: %.3f%% (%d/%d)'
                % (train_loss/(batch_idx+1), 100.*correct/total, correct, total))

def test(epoch,criterion):
    global best_acc
    net.eval()
    test_loss = 0
    correct = 0
    total = 0
    with torch.no_grad():
        for batch_idx, (inputs, targets) in enumerate(testloader):
            inputs, targets = inputs.to('cpu'), targets.to('cpu')
            outputs = net(torch.tensor(inputs,dtype=torch.float32))
            loss = criterion(outputs, targets)

            test_loss += loss.item()
            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()

            if batch_idx % 20 == 0:
                print("Test:")
                print(batch_idx, len(testloader), 'Loss: %.3f | Acc: %.3f%% (%d/%d)'
                    % (test_loss/(batch_idx+1), 100.*correct/total, correct, total))




if __name__ == '__main__':


    trainset = CusDataset('C:/Users/Administrator/Desktop/trainset')
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

    testset = CusDataset('C:/Users/Administrator/Desktop/testset')
    testloader = torch.utils.data.DataLoader(testset, batch_size=32, shuffle=False)

    net = DNN()
    net = net.to('cpu')
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.1, momentum=0.9)

    for epoch in range(epoch):
        train(epoch,criterion,optimizer)
        test(epoch,criterion)

    torch.save(net.state_dict(),'./{}.pkl'.format(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())))
    # rnn = nn.GRU(3, 20, 2)
    # input = torch.randn( 5,21, 3)
    # h0 = torch.randn(2, 3, 20)
    # output, hn = rnn(input, h0)
    # print(output,hn)

