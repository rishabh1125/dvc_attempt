from pathlib import Path
from dvclive import Live
from random import random

with Live(dir= "experiments/logs",save_dvc_exp=True,exp_name="Exp1") as live:
  for epoch in range(1,20):
    live.log_metric("accuracy", epoch*random())
    live.log_metric("loss",  epoch*random())
    live.next_step()

live.log_param("Model","testing2")

