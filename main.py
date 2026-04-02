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
   print("\n--------- Save Game Finder ---------")
   print("  search  - Search for save files")
   print("  pattern - Add a search pattern")
   print("  delete  - Remove a search pattern")
   print("  exit    - Quit")
   print("=" * 36)
   pick = input("\n> ")
   if pick == "search":
    search_for_save(search_pattern)
    time.sleep(5)
    continue

   if pick == "pattern":
    add_pattern(search_list)
    print(f"[+] Added '{search_list[-1]}' to patterns")
    time.sleep(5)
    continue
   elif pick == "delete":
    delete_pattern(search_list)  
    print(f"[i] Current patterns: {', '.join(search_list) if search_list else '(none)'}")
    time.sleep(5)
    continue
   if pick == "exit":
    #not really needed but extra precaution
    exit_code = True
    sys.exit()
 
  except Exception as e:
   print(f"[!] Error: {e}")
   return 
if __name__ == "__main__":
   main(); 