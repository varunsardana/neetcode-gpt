import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        z_exp = np.exp(-z)
        answer = (1/(1+z_exp))
        result = np.round(answer, decimals=5)
        return result



        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        pass

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        return np.maximum(0,z)
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        pass
