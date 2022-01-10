import numpy as np
import pandas as pd

array_in = [185.4, 178.2, 169.2, 176.4, 172.8, 169.2, 165.6, 160.2, 156.6, 151.2, 147.6, 144.,
            142.2, 142.2, 140.4, 140.4, 138.6, 135., 135., 135., 136.8, 140.4, 144., 147.6,
            149.4, 149.4, 149.4, 147.6, 144., 142.2, 140.4, 136.8, 135., 133.2, 135., 136.8,
            140.4, 144., 149.4, 153., 156.6, 156.6, 158.4, 158.4, 158.4, 160.2, 163.8, 167.4,
            171., 176.4, 180., 185.4, 187.2, 190.8, 194.4, 194.4, 194.4, 194.4, 192.6, 190.8,
            187.2, 183.6, 183.6, 180., 178.2, 180., 185.4, 192.6, 199.8, 207., 214.2, 216.,
            219.6, 219.6, 217.8, 216., 214.2, 210.6, 207., 205.2, 201.6, 198., 196.2, 194.4,
            190.8, 187.2, 183.6, 180., 176.4, 174.6, 172.8, 171., 171., 172.8, 176.4, 178.2,
            180., 183.6, 183.6, 183.6]

print(array_in)

array_in = np.array(array_in)
array_in = array_in.reshape(-1, 1)
df = pd.DataFrame(array_in)
df.columns = ['glucose']
# df = df.drop(columns=['Unnamed: 0'])

# create time windows
window_interval = 30  # time in minutes, smallest possible interval is 5 minutes

frame_1 = 'glucose_minus_' + str(window_interval)
frame_2 = 'glucose_minus_' + str(window_interval * 2)
frame_3 = 'glucose_minus_' + str(window_interval * 3)

frame_shift_1 = int(window_interval / 5)
frame_shift_2 = int((window_interval * 2) / 5)
frame_shift_3 = int((window_interval * 3) / 5)
# print(frame_shift_1, frame_shift_2, frame_shift_3)

df[frame_1] = df['glucose'].shift(+frame_shift_1)
df[frame_2] = df['glucose'].shift(+frame_shift_2)
df[frame_3] = df['glucose'].shift(+frame_shift_3)

# drop na values
df = df.dropna()

x1, x2, x3, y = df[frame_1], df[frame_2], df[frame_3], df['glucose']
x1, x2, x3, y = np.array(x1), np.array(x2), np.array(x3), np.array(y)
x1, x2, x3, y = x1.reshape(-1, 1), x2.reshape(-1, 1), x3.reshape(-1, 1), y.reshape(-1, 1)
final_x = np.concatenate((x1, x2, x3), axis=1)

print(final_x)
