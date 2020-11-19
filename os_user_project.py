import os
import time
import logging

print(os.getlogin())
print(os.cpu_count())
print(os.getcwd())
print("snapshot_manager_run_id", int(time.time() * 1000))
# time.sleep(10)
print("snapshot_manager_run_id", int(time.time() * 1000))
print("snapshot_manager_run_id", int(time.time() * 1000))
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())
logger.info('I am Ajay')
logger.error('I am a fake error')
logger.debug('I am a fake debug message')


def my_function(food_list):
    for x in food_list:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)
