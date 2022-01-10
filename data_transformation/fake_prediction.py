import numpy as np
import random

real_glucose = [113, 114, 116, 117, 117, 118, 118, 118, 118, 118, 119, 119, 119, 119, 119, 119, 117, 115, 119, 119, 118, 117, 116, 117, 118, 118, 119, 120, 120, 121, 122, 122, 122, 122, 122, 121, 121, 121, 121, 121, 121, 122, 125, 125, 122, 121, 121, 120, 120, 121, 121, 121, 121, 121, 121, 123, 124, 125, 124, 124, 123, 124, 124, 126, 126, 126, 125, 126, 126, 125, 124, 124, 125, 122, 121, 120, 121, 122, 122, 117, 116, 114, 112, 113, 115, 117, 119, 119, 117, 117, 115, 113, 115, 119, 126, 131, 136, 136, 131, 123, 115, 109, 105, 104, 104, 102, 101]

fake_prediction = []
for value in real_glucose:
    upper = value + 5
    lower = value - 3
    prediction = random.randint(lower, upper)
    fake_prediction.append(prediction)

# real_glucose = np.array(real_glucose)
print(real_glucose)
print(fake_prediction)
