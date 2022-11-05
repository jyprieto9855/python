# Jesse Prieto
# This is a user-friendly Calorie Calculator! This helps people from all sorts of demographics to understand their caloric intake based on certain goals!
print("Hello! " * int(
    17 % 9))  # string operator * used to multiply the string by the value of 17 % 9 rather than typing it over and over again. The value given by 17 % 9 is because modulus give us the remainder of 17 divided by 9
name = input(
    "Sorry! I'm just really excited! My name is KCAL! I can help you find your" + "\n" + "caloric intake based on certain demographics like age and weight! Before we get into that, what is your name? " + "\n")
print(("Hi ") + name + (
    "! It's very nice to meet you!"))  # string operator + is used here to concatenate the two strings and the variable to make it one large string.
print("Before we get started, I want to learn about you!")
gender = input("Are you male or female? ")
print("Sweet! I'm just a robot!")
age = int(input("How old are you? "))
if age <= 626 // 5 ** 2:  # floor division and exponent // * are used to expand a numeric value of 25 into an equation to show understanding
    print("Wow! So young!")
else:
    print("Jeez, you're old like a fossil!")
height = input("What is your height in centimeters? ")
height = float(height)
print("Perfect! Just a couple more questions and you'll be all set! ")
weight = input("How much do you weigh in kilograms? ")
weight = float(weight)
print("Wow! I'm like 10 times heavier than you!")
amount_of_exercise = input("How many times do you exercise a week? ")
amount_of_exercise = int(amount_of_exercise)
print("This is GREAT!", end=" ")
print("I feel like we are already best friends!", end=" ")
print("Let's see")
print("what your basal metabolic rate is!")
if gender == "male":
    print((("Your basal metabolic rate is ") + str(
        int((66.47 + (13.75 * weight) + (5.003 * height) - (
                6.755 * age))))) + " kcal!")  # here, numeric operators * + - were all used to solve for BMR using the Harris-Benedict equation
else:
    print((("Your basal metabolic rate is ") + str(
        int((655.1 + (9.563 * weight) + (1.850 * height) - (
                    4.676 * age))))) + " kcal!")
male_basal_metabolic_rate = float(
    (66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)))
female_basal_metabolic_rate = float(
    (655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)))
print("Now that we know what your basal metabolic rate is, lets",
      "find your caloric intake base on your goals!",
      sep='\n')
print(
    "In order to find our maintenance calories, we need to add roughly 200" + "\n" + "calories to your basal metabloic rate!")
male_maintenance_calories = int((male_basal_metabolic_rate + 200))
female_maintenance_calories = int((female_basal_metabolic_rate + 200))
if gender == "male":
    print(("Your maintenance calories without weekly exercise is" + " " + str(
        male_maintenance_calories)) + "!")
else:
    print(("Your maintenance calories without weekly exercise is" + " " + str(
        female_maintenance_calories)) + "!")
print(
    "Now we must take our weekly exercise into account for our daily caloric intake. We assume that for every hour of exercise we lose 200 calories per hour!")
additional_calories = (200 * int(amount_of_exercise))
male_maint_cal_inc_exersice = int((male_maintenance_calories + int(
    additional_calories)))  # variable is maintenance calories including weekly exercise
female_maint_cal_inc_exersice = int(
    (female_maintenance_calories + int(additional_calories)))
if gender == "male":
    print(
        "Your maintenance calories after including your weekly exercise is " + str(
            male_maint_cal_inc_exersice) + "!")
else:
    print(
        "Your maintenance calories after including your weekly exercise is " + str(
            female_maint_cal_inc_exersice) + "!")
print(
    "In order to see how many calories you have to consume in total, I need to know how many pounds you would like to lose in a week!")
weight_loss = input(
    "Would you like to lose .5, 1, 1.5, or 2 pounds per week? ")
if gender == "male" and weight_loss == ".5":
    print("Your calories per day for .5 pounds lost in a week is" + " " + str(
        int(.9 * int(
            male_maint_cal_inc_exersice) / 1)) + "!")  # division by 1 simply to demonstrate my understanding as there is no real purpose for /1 in the equation
elif gender == "male" and weight_loss == "1":
    print("Your calories per day for 1 pound lost in a week is" + " " + str(
        int(.8 * int(male_maint_cal_inc_exersice))) + "!")
elif gender == "male" and weight_loss == "1.5":
    print("Your calories per day for 1.5 pounds lost in a week is" + " " + str(
        int(.7 * int(male_maint_cal_inc_exersice))) + "!")
elif gender == "male" and weight_loss == "2":
    print("Your calories per day for 2 pounds lost in a week is" + " " + str(
        int(.6 * int(male_maint_cal_inc_exersice))) + "!")
elif gender == "female" and weight_loss == ".5":
    print("Your calories per day for .5 pounds lost in a week is" + " " + str(
        int(.9 * int(female_maint_cal_inc_exersice))) + "!")
elif gender == "female" and weight_loss == "1":
    print("Your calories per day for 1 pound lost in a week is" + " " + str(
        int(.8 * int(female_maint_cal_inc_exersice))) + "!")
elif gender == "female" and weight_loss == "1.5":
    print("Your calories per day for 1.5 pounds lost in a week is" + " " + str(
        int(.7 * int(female_maint_cal_inc_exersice))) + "!")
else:
    print("Your calories per day for 2 pounds lost in a week is" + " " + str(
        int(.6 * int(female_maint_cal_inc_exersice))) + "!")
print(
    "Congratulations! Now you know how many calories you should be eating at based on your goals and demographics!")
user_input = input(
    "While I have you here, would you like to learn about bulking, maintenance calories, or " + '\n' + "exit? Please enter a number 1 through 3 corresponding to the order of the " + "\n" + "options listed.")


def male_bulk_calories(bulk_gender):
    print(
        "I'll ask you some more questions just to ensure I'm still chatting with " + name + "!")
    bulk_gender = gender
    bulk_age = int(input("How old are you? "))
    print("Awesome! Just a couple more things and you'll be all set!!")
    bulk_starting_weight = int(
        input("Please enter your weight in kilograms. "))
    bulking_height = int(input("Please enter your height in centimeters. "))
    print("Alrighty! Let me make some quick calculations! ")
    if bulk_gender == "male":
        male_bulk_calories = 1.2 * (
                    (10 * bulk_starting_weight) + (6.25 * bulking_height) - (
                        5 * bulk_age) + 5)
        return male_bulk_calories


def female_bulk_calories(bulk_gender):
    print(
        "I'll ask you some more questions just to ensure I'm still chatting with " + name + "!")
    bulk_gender = gender
    bulk_age = int(input("How old are you? "))
    print("Awesome! Just a couple more things and you'll be all set!!")
    bulk_starting_weight = int(
        input("Please enter your weight in kilograms. "))
    bulking_height = int(input("Please enter your height in centimeters. "))
    print("Alrighty! Let me make some quick calculations! ")
    if bulk_gender == "female":
        female_bulk_calories = 1.2 * (
                    (10 * bulk_starting_weight) + (6.25 * bulking_height) - (
                        5 * bulk_age) - 161)
        return int(female_bulk_calories)


def main():
    bulk_gender = input(
        "WAIT! Are you a male or a female?? I forgot! Silly me! ")
    if bulk_gender == "male":
        print("Great! Your calories to bulk are " + str(
            male_bulk_calories(bulk_gender)) + "!")


def main2():
    bulk_gender = input(
        "WAIT! Are you a male or a female?? I forgot! Silly me! ")
    if bulk_gender == "female":
        print("Great! Your calories to bulk are " + str(
            female_bulk_calories(bulk_gender)) + "!")


if (user_input == "1" and gender == "male"):
    main()
elif (user_input == "1" and gender == "female"):
    main2()
elif user_input == "2":
    number_of_loops = int(input(
        "How many times would you like to test for your maintenace calories? "))
    for x in range(number_of_loops):
        gender = input("Please enter your gender. ")
        age = int(input("Please enter your age. "))
        height = int(input("Please enter your height in centimeters. "))
        weight = int(input("Please enter your weight in kilograms. "))
        number_of_loops = number_of_loops - 1
        if gender == "male":
            male_basal_metabolic_rate = int(
                (66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)))
            print("Your maintenance calories are " + str(
                int(male_basal_metabolic_rate + 200)) + "!")
        else:
            female_basal_metabolic_rate = int(
                (655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)))
            print("Your maintenance calories are " + str(
                int(female_basal_metabolic_rate + 200)) + "!")
elif user_input == "3":
    x = True
    while (x):
        print(
            "I hope you find all this information helpful. Until next time!!")
        x = not x
