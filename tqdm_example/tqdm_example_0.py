from tqdm import tqdm

index = 0
for i in tqdm(range(10000000)):
    index += 1

print("index: ", index)
