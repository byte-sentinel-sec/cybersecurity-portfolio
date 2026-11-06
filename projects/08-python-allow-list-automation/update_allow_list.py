"""Remove IP addresses on a remove list from an allow list file."""

import_file = "allow_list.txt"

# Sample data for demonstration; replace with your own remove list
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40"]

# Read the allow list
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Convert the string to a list
ip_addresses = ip_addresses.split()

# Remove any IP address that appears on the remove list
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Convert back to a string, one IP per line
ip_addresses = "\n".join(ip_addresses)

# Overwrite the file with the updated allow list
with open(import_file, "w") as file:
    file.write(ip_addresses)
