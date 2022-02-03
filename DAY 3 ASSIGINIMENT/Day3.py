# From a dictionary, print the Key whose Value is maximum in the dictionary.

names={"India":90,"USA":190,"UK":78}
max=0
str=""
for i in names:
    for j in i:
        if names [i] > max:
            str=i
            max= names[i]
print(str)
