from cryptography.fernet import Fernet

# Key + master_pwd + text to encrypt = random text (VERY basic run down of cryptography encryption)
# Create Key - only need to run one time to get master key then comment out
'''def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)'''

# Load Key
def load_key():
  file = open("key.key", "rb")
  key = file.read()
  file.close()
  return key

key = load_key()
fer = Fernet(key)


def view():
  with open('passwords.txt', 'r') as file:
    for line in file.readlines():
      data = line.rstrip() #removes returns at the end of the line
      user, passw = data.split('|')
      print(f"User: {user}, Password: {fer.decrypt(passw.encode()).decode()}")

def add():
  name = input("Account Name: ")
  password = input("Password: ")

  with open('passwords.txt', 'a') as file: #this is opening a file to append a new item (R = read/W = write(will open file and start a completely blank one)/A = allows reading and appending to the very end of the file as options)
    file.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:
  mode = input("Would you like to add a new password or view existing ones? (View/Add) or press Q to quit. ").lower()
  if mode == 'q':
    break

  if mode == 'view':
    view()
  elif mode == 'add':
    add()
  else:
    print("Invalid mode.")
    continue