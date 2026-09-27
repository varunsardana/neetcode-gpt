import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        subtracted = z - np.max(z)
        softmax = np.exp(subtracted)
        return np.round(softmax/(np.sum(softmax)), decimals=4)

        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        pass
