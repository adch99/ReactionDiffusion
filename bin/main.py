import src.configure as configlib
import src.rxn as rxnlib
import src.video as vidlib

config = configlib.getConfig()
grid = rxnlib.RxnGrid(*config)
snapshots = grid.run(return_snaps=True)
video_params = vidlib.getVideoParams()
video = vidlib.makeVideo(snapshots, *video_params)
video_save_params = vidlib.getSaveParams()
vidlib.saveVideo(video, *video_save_params)