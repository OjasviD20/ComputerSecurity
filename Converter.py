#Function to convert to octal. 
def permission_string_to_octal(perms):
    owner = (perms[0] == 'r') * 4 + (perms[1] == 'w') * 2 + (perms[2] == 'x') * 1
    group = (perms[3] == 'r') * 4 + (perms[4] == 'w') * 2 + (perms[5] == 'x') * 1
    public = (perms[6] == 'r') * 4 + (perms[7] == 'w') * 2 + (perms[8] == 'x') * 1
    return owner * 100 + group * 10 + public


choice = 1
while choice == 1:
  perms = input("Enter the Linux permission string (like 'rwxr-xr--'): ")
  if len(perms) != 9:
        raise ValueError("Invalid permission string. It should be 9 characters long.")
  permissions_integer = permission_string_to_octal(perms)
  print("The integer value of the permission string is: ", permissions_integer)
  choice = int(input("To try again type 1 "))


