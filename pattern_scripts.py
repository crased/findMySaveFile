import sys
import json
import time

def add_pattern(search_list):
   try:
    data = input("enter name of [folder Name | file Format] to add: ")  
    search_list.append(data)
    with open('patterns.json', 'w') as f:
        json.dump(search_list, f, indent=4)
    return search_list
   except Exception as e:   
    print(f"[!] Error: {e}")
    return

def delete_pattern(search_list):
   try:
    print(f"[i] Current patterns: {', '.join(search_list) if search_list else '(none)'}")
    time.sleep(2)

    if len(search_list) != 0:
     data = input("enter name to delete: ")
     search_list.remove(data)
     with open('patterns.json', 'w') as f:
        json.dump(search_list, f, indent=4) 
     return search_list 
    print("[i] No patterns to delete.")
    return
   except Exception as e:
    print(f"[!] Error: {e}")
    return