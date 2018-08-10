import json
import sys
import xmltodict as xmltodict

input_file = open(sys.argv[1], 'r')
read_input = input_file.read()

jsonString = json.dumps(xmltodict.parse(read_input), indent=4)

print("\nJSON output(output.json):")
print(jsonString)

with open("output.json", 'w') as f:
    f.write(jsonString)
