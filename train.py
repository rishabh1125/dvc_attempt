from pathlib import Path
from dvclive import Live
from random import random

with Live(save_dvc_exp=True) as live:
  for epoch in range(1,20):
    live.log_metric("accuracy", epoch*random())
    live.log_metric("loss",  epoch*random())
    live.next_step()

live.log_param("Model","testing")

