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
    print(f"Error has occurred: {e}")
    return    

def delete_pattern(search_list):    
   try: 
    print(search_list)
    time.sleep(2)

    if len(search_list) != 0:
     data = input("enter name to delete: ")
     search_list.remove(data)
     with open('patterns.json', 'w') as f:
        json.dump(search_list, f, indent=4) 
     return search_list 
    print("you have no patterns") 
    return
   except Exception as e:
    print(f"Error has occurred: {e}")    
    return