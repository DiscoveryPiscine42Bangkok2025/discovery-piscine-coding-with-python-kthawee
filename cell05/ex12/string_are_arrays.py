import sys

if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    # ดึงเฉพาะตัว 'z'
    result = "".join([c for c in text if c == "z"])

    if result:
        print(result)
    else:
        print("none")
