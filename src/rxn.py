# All the main reaction analysis
import numpy as np

class RxnGrid(object):
    def __init__(self, grid_size, diff_rates, activation_rates, init_concs, timestep=0.1):
        self.grid_size = grid_size
        self.diff_rates = diff_rates
        self.activation_rates = activation_rates
        self.init_concs = init_concs
        self.timestep = timestep

        self.initialize()

    def initialize(self):
        self.num_reagents = len(self.diff_rates)
        self.grid_shape = (self.num_reagents,) + tuple(self.grid_size)
        # print(self.grid_shape)
        self.grid = np.zeros(self.grid_shape)

        for reagent in range(self.num_reagents):
            self.grid[reagent, :] += self.init_concs[reagent, :]

        # self.activity_shape = (num_reagents, num_reagents) + tuple(self.grid_size))
        # self.activity = self.ones(self.activity_shape)
        # for reagent1 in range(self.num_reagents):
        #     for reagent2 in range(self.num_reagents):
        #         self.activity[reagent1, reagent2, :, :] *= self.activation_rates[reagent1, reagent2]


    def run(self, time, return_snaps=False):
        num_steps = int(np.ceil(time / self.timestep))
        snapshots = [self.grid.copy()]
        for i in range(num_steps):
            snap = self.step()
            if return_snaps:
                snapshots.append(snap)

        if return_snaps:
            return snapshots

    def step(self):
        net_diffusion = self.getDiffusion()
        net_production = self.getProduction()
        self.grid += net_diffusion + net_production

        return self.grid.copy()

    def getDiffusion(self):
        l, h = self.grid_size
        padded_net_diff = np.zeros((self.num_reagents, l+2, h+2))
        # padded_grid = np.zeros((self.num_reagents, l+2, h+2))
        # padded_grid[:, 1:-1, 1:-1] = self.grid

        # mask is
        # 1  1  1
        # 1 -8  1
        # 1  1  1

        mask = np.ones((3, 3))
        mask[1, 1] = -8

        for reagent in range(self.num_reagents):
            rate = self.timestep * self.diff_rates[reagent] / 8
            # print("rate:", rate)
            # print("mask.shape:", mask.shape)
            for i in range(l):
                for j in range(h):
                    # print("self.grid[reagent].shape:",self.grid[reagent, i:i+3, j:j+3].shape)
                    # print("padded_net_diff[i:i+3, j:j+3].shape:", padded_net_diff[reagent, i:i+3, j:j+3].shape)
                    padded_net_diff[reagent, i:i+3, j:j+3] += self.grid[reagent, i, j] * mask * rate

        net_diffusion = padded_net_diff[:, 1:-1, 1:-1]
        # print(net_diffusion)
        return net_diffusion

    def getProduction(self):
        net_production = np.zeros(self.grid_shape)
        for reagent1 in range(self.num_reagents):
            for reagent2 in range(self.num_reagents):
                net_production[reagent1, :] += self.activation_rates[reagent2][reagent1] * self.grid[reagent2, :]

        return net_production


