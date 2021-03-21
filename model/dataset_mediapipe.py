import os

import torch.utils.data as data
import numpy as np

class CusDataset(data.Dataset):
    def __init__(self, root_path='C:/Users/Administrator/Desktop/trainset'):
        self.root_path = root_path
        self.data_list = []
        self.labels = []
        self.xy_transform = [-0.001,0,0.001]
        self.scale_coef = [0.9,1.1]
        self.two_hand = [7,8,9,10]
        # a = np.ones(256)
        # for x in range(256):
        #     a[x] = x
        # a[1::3] = 999
        # print(a)

        # label_dirs = [os.path.join(root_path,label) for label in os.listdir(root_path)]
        for label in os.listdir(root_path):
             #  int(label)
            label_dir = os.path.join(root_path,label)
            txt_names = os.listdir(os.path.join(label_dir,'hand1'))
            # hands = ['hand1','hand2']
            for txt_name in txt_names:
                hand1 = np.loadtxt(os.path.join(label_dir,'hand1',txt_name)).reshape(-1)
                hand2 = np.loadtxt(os.path.join(label_dir,'hand2',txt_name)).reshape(-1)
                self.data_aug(hand1,hand2,int(label))



    def __getitem__(self, index):
        return self.data_list[index],self.labels[index]

    def __len__(self):
        return len(self.data_list)

    def data_aug(self,hand1,hand2,label):
        if label in self.two_hand:
            for x_coef in self.xy_transform:
                for y_coef in self.xy_transform:
                    for scale_coef in self.scale_coef:
                        hand1 = self._rand_add_sub(hand1,x_coef,y_coef)
                        hand2 = self._rand_add_sub(hand2,x_coef,y_coef)
                        hand1 = self._rand_scale(hand1,scale_coef)
                        hand2 = self._rand_scale(hand2,scale_coef)
                        input_data = np.concatenate((hand1, hand2))
                        self.data_list.append(input_data)
                        self.labels.append(int(label))
        else:
            for x_coef in self.xy_transform:
                for y_coef in self.xy_transform:
                    for scale_coef in self.scale_coef:
                        hand1 = self._rand_add_sub(hand1,x_coef,y_coef)
                        hand1 = self._rand_scale(hand1,scale_coef)
                        input_data = np.concatenate((hand1, hand2))
                        self.data_list.append(input_data)
                        self.labels.append(int(label))


    def _rand_add_sub(self, input_data, x_coef=0.001,y_coef=0.001):
        input_data[::3] += x_coef
        input_data[1::3] += y_coef
        return input_data

    def _rand_scale(self, input_data, coef=0.9):
        x = input_data[0]
        y = input_data[1]
        input_data[3::3] -= (input_data[3::3] - x)*(1-coef)
        input_data[4::3] -= (input_data[4::3] - y)*(1-coef)
        return input_data




class RNNDataset(data.Dataset):
    def __init__(self, root_path='C:/Users/Administrator/Desktop/trainset', n_frame=16):
        self.root_path = root_path
        self.data_list = []
        self.labels = []
        self.n_frame = n_frame
        self.xy_transform = [-0.001,0,0.001]
        self.scale_coef = [0.9,1.1]
        self.two_hand = [7,8,9,10]
        for label in os.listdir(root_path):
            label_dir = os.path.join(root_path,label)
            txt_names = os.listdir(os.path.join(label_dir,'hand1'))
            for txt_name in txt_names:
                hand1 = np.loadtxt(os.path.join(label_dir,'hand1',txt_name)).reshape(-1)
                hand2 = np.loadtxt(os.path.join(label_dir,'hand2',txt_name)).reshape(-1)
                self.data_aug(hand1,hand2,int(label))



    def __getitem__(self, index):
        return self.data_list[index],self.labels[index]

    def __len__(self):
        return len(self.data_list)

    def data_aug(self,hand1,hand2,label):
        if label in self.two_hand:
            for x_coef in self.xy_transform:
                for y_coef in self.xy_transform:
                    for scale_coef in self.scale_coef:
                        hand1 = self._rand_add_sub(hand1,x_coef,y_coef)
                        hand2 = self._rand_add_sub(hand2,x_coef,y_coef)
                        hand1 = self._rand_scale(hand1,scale_coef)
                        hand2 = self._rand_scale(hand2,scale_coef)
                        input_data = np.concatenate((hand1, hand2))
                        self.data_list.append(input_data.reshape(self.n_frame,-1))
                        self.labels.append(int(label))
        else:
            for x_coef in self.xy_transform:
                for y_coef in self.xy_transform:
                    for scale_coef in self.scale_coef:
                        hand1 = self._rand_add_sub(hand1,x_coef,y_coef)
                        hand1 = self._rand_scale(hand1,scale_coef)
                        input_data = np.concatenate((hand1, hand2))
                        self.data_list.append(input_data.reshape(self.n_frame,-1))
                        self.labels.append(int(label))


    def _rand_add_sub(self, input_data, x_coef=0.001,y_coef=0.001):
        input_data[::3] += x_coef
        input_data[1::3] += y_coef
        return input_data

    def _rand_scale(self, input_data, coef=0.9):
        x = input_data[0]
        y = input_data[1]
        input_data[3::3] -= (input_data[3::3] - x)*(1-coef)
        input_data[4::3] -= (input_data[4::3] - y)*(1-coef)
        return input_data
