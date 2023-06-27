from .api import API
from .dataset import ProductDataset, get_dataset
from .ocr import OCRResult
from .types import APIConfig, APIVersion, Country, DatasetType, Environment, Flavor
from .utils import get_logger

# Instantiate root logger
get_logger()

__all__ = [
    "API",
    "APIConfig",
    "APIVersion",
    "Country",
    "DatasetType",
    "Flavor",
    "Environment",
    "OCRResult",
    "ProductDataset",
    "get_dataset",
]

__version__ = "0.1.3"
