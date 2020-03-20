# Creates the configuration to the system.
# Provides API for possible frontends.
import numpy as np
def getConfig():
    reagent1 = np.zeros((10, 10))
    reagent1[5, 5] = 2
    reagent2 = np.zeros((10, 10))
    reagent2[3, 3] = 1
    args = [
        (10, 10), #grid_size
        [10, 5], #diff_rates
        np.array([[1, 1], [-1.5, 0]]), #activation_rates
        np.array([reagent1, reagent2]) #init_concs
    ]
    kwargs = {
        "timestep": 0.1
    }
    config = [args, kwargs]
    return config