from logging import config
from pathlib import Path

import yaml


def logging_setup(cfg_path: Path, logging_cfg_file: str = "logging-conf.yaml") -> None:
    full_logging_cfg_path: Path = cfg_path / logging_cfg_file
    with open(full_logging_cfg_path, "rt") as file:
        cfg = yaml.safe_load(file.read())
        config.dictConfig(cfg)
