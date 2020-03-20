import src.configure as configlib
import src.rxn as rxnlib
import src.video as vidlib
import matplotlib.pyplot as plt
import matplotlib as mpl

config = configlib.getConfig()
grid = rxnlib.RxnGrid(*config[0], **config[1])
snapshots = grid.run(1, return_snaps=True)
video_params = vidlib.getVideoParams()
video = vidlib.makeVideo(snapshots, *video_params)
video_save_params = vidlib.getSaveParams()
vidlib.saveVideo(video, *video_save_params)