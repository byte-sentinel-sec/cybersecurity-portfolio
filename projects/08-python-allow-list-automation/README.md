# 8. Algorithm for File Updates in Python

**Skills:** Python · file I/O · lists & loops · conditionals · security automation

## Overview
Access to restricted content is controlled by an allow list of IP addresses (`allow_list.txt`). I wrote an algorithm that removes any IP address found in a `remove_list` from the allow list.

## How it works
1. Open `allow_list.txt` with a `with` statement (read mode)
2. `.read()` the contents into a string
3. `.split()` the string into a list
4. Loop through `remove_list`; if an element is in the allow list, `.remove()` it
5. `.join()` the list back into a newline-separated string
6. Reopen the file in write mode and `.write()` the updated list

See [`update_allow_list.py`](update_allow_list.py). The IPs in `remove_list` and `allow_list.txt` are sample data.

📄 [Original report](original-report.pdf)
