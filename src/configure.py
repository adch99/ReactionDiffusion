# Creates the configuration to the system.
# Provides API for possible frontends.
import numpy as np
def getRxnConfig():
    """
    Returns the params used for creating the rxn.RxnGrid
    object as [args, kwargs]. See rxn.RxnGrid for more
    details.
    """
    reagent1 = np.zeros((10, 10))
    reagent1[4, 4] = 1
    reagent2 = np.zeros((10, 10))
    reagent2[1, 1] = 0.5
    reagent2[8, 8] = 0.5
    args = [
        (10, 10), #grid_size
        [1, 0.5], #diff_rates
        np.array([[0.5, 0.5], [-0.75, 0]]), #activation_rates
        np.array([reagent1, reagent2]) #init_concs
    ]
    kwargs = {
        "timestep": 0.1
    }
    config = [args, kwargs]
    return config

def getVideoParams():
    """
    Present for extending code later. Ignore for now.
    """
    config = {
    }
    return config

def getSaveParams():
    """
    Returns the parameters (fps, filename) used to save the
    video
    """
    config = {
        "filename": "vid/rxndiffusion_diagonal.mp4",
        "fps": 10
    }
    return config