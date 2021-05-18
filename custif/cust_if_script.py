#!/usr/bin/env python3

message = 'Select from a list of dog breeds to select a name for your dog.'
list1 = ["Lab", "Poodle", "Greyhound", "Collie"]
print(list1)

dogbreed_input = input("Enter one of the dog breeds listed: ")

# if input value equals dog breed
if dogbreed_input == "Lab":
    print(dogbreed_input + " name is Rex")
elif dogbreed_input == "Poodle":
    print(dogbreed_input + " name is Daisy")
elif dogbreed_input == "Greyhound":
    print(dogbreed_input + " name is Haze")
elif dogbreed_input == "Collie":
    print(dogbreed_input + " name is Kelly")
else:
    print('Incorrect entry')
