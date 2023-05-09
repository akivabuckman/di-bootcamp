brands = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
#Convert it into a list using Python (don’t do it by hand!).
brand_list = brands.split(', ')
print(brand_list)

#Print out a message saying how many manufacturers/companies are in the list.
print(f"there are {len(brand_list)} companies")

#Print the list of manufacturers in reverse/descending order (Z-A).
brand_list.sort(reverse=True)
print(brand_list)

#Find out how many manufacturers’ names have the letter ‘o’ in them.
count = 0
for i in brand_list:
    if 'o' in i.lower():
        count += 1

print(f"{count} have an o")

#Find out how many manufacturers’ names do not have the letter ‘i’ in them.
count = 0
for i in brand_list:
    if 'i' not in i.lower():
        count += 1

print(f"{count} don't have an i")

#Remove duplicates programmatically.
brands = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
brand_set = set(brands)
print(brand_set)

#Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo,
# Aston Martin, …”), also print out a message saying how many companies are now in the list.
output = ""
for i in brands:
    if brands.count(i) < 2:
        output += f"{i}, "
print(output)

#Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s
# name.
brands = list(brand_set)
brands.sort()
for i in brands:
    print(i[::-1])