# Turing Reaction Diffusion Mechanism

Spontaneous pattern formation in biological systems
is attributed to various phenomena. Among the prime
contenders is the Turing Reaction Diffusion mechanism
which says that starting with a bunch of chemical
that have different rates of diffusion and different
chemical actions, spontaneous patterns can emerge in
the system.

Here we have simulated this process on a grid with
diffusion and catalytic activities of reagents.

Original intention was to use `matplotlib.animation`
to make the video. However, that turned out to be
too complicated for my liking, so `ffmpeg` has been
used instead. This involves calling `ffmpeg` as a
shell command via `subprocess` but has arguably better
support and is easier to use. However, this will not
work out-of-the-box even if it is made into a Python
package since `ffmpeg` needs to be installed separately.

If you want to use this code for your own purposes
without getting into the details, then fork this repo
and rewrite the `src/configure.py` file as per your
requirements. Create `img` and `vid` directories for
the outputs.