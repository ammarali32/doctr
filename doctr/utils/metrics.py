# Copyright (C) 2021, Mindee.

# This program is licensed under the Apache License version 2.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0.txt> for full license details.

from typing import Dict, List, Optional, Tuple

import cv2
import numpy as np
from scipy.optimize import linear_sum_assignment

from doctr.utils.geometry import rbbox_to_polygon

__all__ = ['TextMatch', 'box_iou', 'box_ioa', 'mask_iou', 'rbox_to_mask',
           'nms', 'LocalizationConfusion', 'OCRMetric', 'DetectionMetric']


