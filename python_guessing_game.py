release_year = int(input("When was python 1.0 released?: "))

if release_year > 1994:
    print("It was earlier than that!")
    int(input("When was python 1.0 released?: "))
if release_year < 1994:
    print("It was later than that!")
    int(input("When was python 1.0 released?: "))
if release_year == 1994:
    print("Correct. That is the correct year")
    