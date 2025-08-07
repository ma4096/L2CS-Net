from dataclasses import dataclass
import numpy as np

@dataclass
class GazeResultContainer:

    pitch: np.ndarray
    yaw: np.ndarray
    bboxes: np.ndarray|None
    landmarks: np.ndarray|None
    scores: np.ndarray|None
    detection: bool