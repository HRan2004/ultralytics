# Ultralytics YOLO 🚀, GPL-3.0 license

__version__ = "8.0.21"

from core.yolo.engine.model import YOLO
from core.yolo.utils import ops
from core.yolo.utils.checks import check_yolo as checks

__all__ = ["__version__", "YOLO", "hub", "checks"]  # allow simpler import
