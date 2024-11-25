import os
import json
from src.fcfs import fcfs
from src.sstf import sstf
from src.scan import scan
from src.cscan import cscan
from src.look import look
from src.clook import clook

def process_json_files():
    # Lista de archivos JSON en el directorio "inputs"
    json_files = [
        "inputs/dsa001.json",
        "inputs/dsa002.json",
        "inputs/dsa003.json",
        "inputs/dsa004.json",
        "inputs/dsa005.json",
        "inputs/dsa006.json",
        "inputs/dsa007.json",
        "inputs/dsa008.json",
        "inputs/dsa009.json",
        "inputs/dsa010.json",
        "inputs/dsa011.json",
    ]

    for i, filepath in enumerate(json_files):
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
                print(f"[{i+1}] Procesando archivo: {filepath}")
                process_request(data)
        except Exception as e:
            print(f"Error procesando el archivo {filepath}: {e}")
            continue

def process_request(data):
    algorithm = data["algorithm"]
    tracks = data["total_cylinders"]
    arm = data["initial_arm_position"]
    requests = data["requests"]

    print(f"Algorithm: {algorithm}")
    print(f"Total Cylinders: {tracks}")
    print(f"Initial Arm Position: {arm}")
    print(f"Requests: {requests}")

    if algorithm == 1:  # FCFS
        result = fcfs(arm, requests)
    elif algorithm == 2:  # SSTF
        result = sstf(arm, requests)
    elif algorithm == 3:  # SCAN
        result = scan(arm, requests, tracks)
    elif algorithm == 4:  # CSCAN
        result = cscan(arm, requests, tracks)
    elif algorithm == 5:  # LOOK
        result = look(arm, requests)
    elif algorithm == 6:  # CLOOK
        result = clook(arm, requests)
    else:
        result = {"error": "Invalid algorithm"}

    print(f"Result: {result}\n"+"*"*100)

if __name__ == "__main__":
    process_json_files()
