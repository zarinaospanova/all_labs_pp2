import json
# we use the function 'load()' to get we're working with file objects(our 'my_file' is 'file object')
# we use the function 'loads()' when working with a string that contains JSON data in it
with open("/Users/darinaospanova/Documents/pp2_all_labs/labs/lab4/JSON/sample-data.json", "r") as f: # opening a json file as file
    data = json.load(f) # getting a dictionary from the content of a json file 

print("Inherit status")
print("="*84)
DN = "DN"
Description = "Description"
Speed = "Speed"
MTU = "MTU"
print(f"{DN:50} {Description:20} {Speed:7} {MTU:7}") # :<20 is for left-alignment of words in a field of 20 characters
print("-"*84)
for item in data["imdata"]: # data['imdata'] is a list
    attr = item["l1PhysIf"]["attributes"] # every ith element of data['imdata'] contains a
    # the dictionary 'attributes' contains many keys
    dn = attr.get("dn")
    descr = attr.get("descr") # we'll get an empty string '' as a default if it's
    speed = attr.get("speed") # we'll get 'inherit' as a default if it's missing
    mtu = attr.get("mtu") # we'll get an empty string '' as a default if it's missing
    print(f"{dn:50} {descr:20} {speed:7} {mtu:7}")


