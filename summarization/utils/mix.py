import random
import numpy as np
import pandas as pd
import torch

from pathlib import Path


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def make_dir(dir_path: str) -> None:
    Path(dir_path).mkdir(parents=True, exist_ok=True)


def make_dirs(config: dict, dir_names: list[str]) -> None:
    for dir_name in dir_names:
        dir_path = join_path(base_dir=config["base_dir"], sub_path=config[dir_name])
        Path(dir_path).mkdir(parents=True, exist_ok=True)


def get_weights_file_path(config: dict, epoch: str) -> str:
    return join_path(
        base_dir=config["base_dir"],
        sub_path=f"{config['model_dir']}/{config['model_basename']}{epoch}.pt",
    )


def get_list_weights_file_paths(config: dict) -> None | list[Path]:
    model_dir = join_path(base_dir=config["base_dir"], sub_path=config["model_dir"])
    model_basename = config["model_basename"]
    weights_files = list(Path(model_dir).glob(pattern=f"{model_basename}*.pt"))
    if len(weights_files) == 0:
        return None
    return sorted(weights_files)


def noam_lr(
    model_size: int,
    step: int,
    warmup_steps: int,
    factor: float = 1.0,
) -> float:
    step = max(step, 1)
    return factor * (
        model_size ** (-0.5) * min(step ** (-0.5), step * warmup_steps ** (-1.5))
    )


def join_path(base_dir: str, sub_path: str) -> str:
    return str(Path(base_dir) / sub_path)


def write_to_csv(
    columns: list[str],
    data: list[list],
    file_path: str | Path,
) -> pd.DataFrame:
    obj = {}
    for i, column in enumerate(columns):
        obj[column] = data[i]

    df = pd.DataFrame(obj)

    file_path = str(file_path)
    dir_path = file_path.rsplit("/", 1)[0]
    make_dir(dir_path=dir_path)

    df.to_csv(file_path, index=False)

    return df
