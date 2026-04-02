import os
import sys
import subprocess
import json
import time
from search_scripts import search_for_save, find_save_game
from pattern_scripts import add_pattern, delete_pattern

try:
 with open('patterns.json', 'r', encoding='utf-8') as f:
     search_list = json.load(f)
except: 
 search_list = ["sav"]  
 with open('patterns.json', 'w', encoding='utf-8') as f:
     json.dump(search_list, f, indent=4)
inner_pattern = r"\|".join(search_list)
search_pattern = rf".*\({inner_pattern})\).*"

   
def main():
 exit_code = False
 while exit_code == False:  
  try:
   print("'search': to enter search tool")
   print("'pattern': to add a pattern")
   print("'delete': to remove a pattern")
   print("'exit':  to exit tool")
   pick = input("type command: ")
   if pick == "search":
    search_for_save(search_pattern)
    time.sleep(5)
    continue

   if pick == "pattern":
    add_pattern(search_list)
    print(f"you've added :{search_list[-1:]} to patterns")
    time.sleep(5)
    continue
   elif pick == "delete":
    delete_pattern(search_list)  
    print(search_list)
    time.sleep(5)
    continue
   if pick == "exit":
    #not really needed but extra precaution
    exit_code = True
    sys.exit()
 
  except Exception as e:
   print(f"Error has occurred: {e}") 
   return 
if __name__ == "__main__":
   main(); 