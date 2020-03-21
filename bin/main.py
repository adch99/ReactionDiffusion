import src.configure as configlib
import src.rxn as rxnlib
import src.video as vidlib
import matplotlib.pyplot as plt
import matplotlib as mpl

config = configlib.getRxnConfig()
grid = rxnlib.RxnGrid(*config[0], **config[1])
snapshots = grid.run(10, return_snaps=True)
video_params = configlib.getVideoParams()
vidlib.makeVideo(snapshots, **video_params)
video_save_params = configlib.getSaveParams()
vidlib.saveVideo(**video_save_params)