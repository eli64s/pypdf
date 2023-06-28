"""Configuration file for the application."""

from dataclasses import dataclass
from pathlib import Path

import dacite
import toml


@dataclass
class PathsConfig:
    """Paths configuration."""

    input: str
    output: str
    test_pdf: str


@dataclass
class RegexConfig:
    """Regex configuration."""

    name_pattern: str
    amount_pattern: str
    search_pattern: str


@dataclass
class AppConfig:
    """Application configuration."""

    paths: PathsConfig
    regex: RegexConfig


def read_config_file(file_path: Path) -> AppConfig:
    """Reads the configuration file and returns a configuration object."""
    with file_path.open("r") as f:
        toml_data = toml.load(f)
    conf_object = dacite.from_dict(data_class=AppConfig, data=toml_data)
    return conf_object
