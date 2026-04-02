
import subprocess
import sys
import os 

def find_save_game():
 raw_dir = input("Enter folder name: ") 
 if raw_dir is not None and raw_dir.strip() != "":
  try:
   pattern = f"*{raw_dir}*"
   # search root changes the level the search starts at rn its starting in home directory
   search_root = os.path.expanduser("~/Games")
   cmd = ['find', search_root, '-type', 'd', '-iname', f"*{raw_dir}*"]
   result =  subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
   output, error = result.communicate()
   if output.strip():
      paths = output.strip().splitlines()
      return paths[0]
   else:
      print(f"[!] No folder matching '{raw_dir}' found in {search_root}")
      return None   
  except Exception as e:
   print(f"[!] Error: {e}")
   return None
 print("[!] Game title cannot be empty.")
 return None



def search_for_save(search_pattern):
   try: 
    path = find_save_game()
    cmd = ['find', path, '-regextype', "sed", "-regex", search_pattern]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    if len(result.stdout) == 0:
       print("[!] No save files found. Try adding the folder name to your search patterns.")
    print(f"\n[+] Results:\n{result.stdout}")
   except Exception as e:
    print(f"[!] No directory found: {e}")
    return    