from tqdm import tqdm, trange
import time

##for i in tqdm(range(10)):
            ##time.sleep(0.3)
            
##for i in trange(15):
            ##time.sleep(2)
            
print(" Wait for a moment.... ".center(70,"=")) 
print("\n")           
##with tqdm(total=100) as pbur:
        ## for i in range(100):
              ##   time.sleep(0.1)
               ##  pbur.update(1)
                 
                 
progress_bar = tqdm(total=100)
for i in range(10):
            time.sleep(0.1)
            progress_bar.update(1)
progress_bar.close()

progress_bar = tqdm(total=100)
for i in range(20):
            time.sleep(0.1)
            progress_bar.update(1)
progress_bar.close()

progress_bar = tqdm(total=100)
for i in range(30):
            time.sleep(0.1)
            progress_bar.update(1)
progress_bar.close()

progress_bar = tqdm(total=100)
for i in range(40):
            time.sleep(0.1)
            progress_bar.update(1)
progress_bar.close()

progress_bar = tqdm(total=100)
for i in range(50):
            time.sleep(0.1)
            progress_bar.update(1)
progress_bar.close()

progress_bar = tqdm(total=100)
for i in range(60):
            time.sleep(0.1)
            progress_bar.update(1)
progress_bar.close()

progress_bar = tqdm(total=100)
for i in range(70):
            time.sleep(0.1)
            progress_bar.update(1)
progress_bar.close()

progress_bar = tqdm(total=100)
for i in range(80):
            time.sleep(0.1)
            progress_bar.update(1)
progress_bar.close()

progress_bar = tqdm(total=100)
for i in range(90):
            time.sleep(0.1)
            progress_bar.update(1)
progress_bar.close()

progress_bar = tqdm(total=100)
for i in range(100):
            time.sleep(0.1)
            progress_bar.update(1)
progress_bar.close()