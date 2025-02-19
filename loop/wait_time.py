import time

wait_time = 1
attempt=0
max_attempt=5

while attempt<max_attempt:
    print(f"Attempt {attempt+1} of wait time {wait_time}")
    time.sleep(wait_time)
    wait_time*=2
    attempt+=1

