# All the main reaction analysis

class RxnGrid(object):
    def __init__(self, grid_size, diff_rates, activation_rates, init_concs, timestep=0.1):
        self.grid_size = grid_size
        self.diff_rates = diff_rates
        self.activation_rates = activation_rates
        self.init_concs = init_concs
        self.timestep = timestep

        self.initialize()

    def initialize():
        self.num_reagents = len(diff_rates)
        self.grid_shape = (self.num_reagents,) + tuple(self.grid_size)
        self.grid = np.zeros(self.grid_shape)

        for reagent in range(self.num_reagents):
            self.grid[reagent, :] += self.init_concs[reagent, :]

        # self.activity_shape = (num_reagents, num_reagents) + tuple(self.grid_size))
        # self.activity = self.ones(self.activity_shape)
        # for reagent1 in range(self.num_reagents):
        #     for reagent2 in range(self.num_reagents):
        #         self.activity[reagent1, reagent2, :, :] *= self.activation_rates[reagent1, reagent2]



    def run():
        net_diffusion = self.getDiffusion()
        net_production = self.getProduction()
        self.grid += net_diffusion + net_production

        return self.grid

    def getDiffusion():
        net_diffusion = np.zeros(self.grid_shape)

    def getProduction():
        net_production = np.zeros(self.grid_shape)
        for reagent1 in range(self.num_reagents):
            for reagent2 in range(self.num_reagents):
                net_production[reagent1, :] += self.activation_rates[reagent2][reagent1] * self.grid[reagent2, :]

        return net_production


