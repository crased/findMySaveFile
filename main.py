import subprocess
def find_save_game():
  try:
   game = input("Enter gameTitle: ")
   cmdPipe = subprocess.Popen(['find', '.', '-type', 'd'], stdout=subprocess.PIPE)
   cmd = ['grep' , '-i', game]
   result =  subprocess.Popen(cmd, stdin=cmdPipe.stdout, stdout=subprocess.PIPE, text=True)
   cmdPipe.stdout.close()
   output, error = result.communicate()
   dir_path = output.strip()
   return dir_path.splitlines()[0]
  except:
   print("output is None")
   return None
def search_for_save():
   try: 
    output = find_save_game()
    search_pattern = "save|gi"
    cmd = ['grep','-rE', search_pattern, output]
    result = subprocess.run(cmd, capture_output=True, text=True)
    formated = result.stdout.partition(":")[0]
    print(formated)
   except:
    print("No directory found.")
    return     
def main():
   search_for_save()


if __name__ == "__main__":
   main(); 