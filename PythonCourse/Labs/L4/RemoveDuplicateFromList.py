# Functia pentru stergerea elementelor duplicate(transformam lista intr-un set care nu accepta element duplicat)
def remove_duplicates(input_list):
    return list(set(input_list))
# Citim o serie de numere
input_list = input("Enter a list of numbers: ").split(",")
# Stergerea duplicatelor
output_list = remove_duplicates(input_list)
print(f"List after removing duplicates: {output_list}")
