#if temperature is greater than 30
#    it's a hot day
#otherwise if it's less than 10
#    it's a cold day
#otherwise
#    it's neither hot nor cold

hot_day = 35
if hot_day > 30:
    print("It's a hot day")
else:
    print("It's a cold day")

# exercise
#if name is less than 3 characters long
    #name must be at least 3 characters
#otherwise if it's more than 50 characters long
    #name can be a maximum of 50 characters
#otherwise
    #name looks good!

name = "Mirka"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")
