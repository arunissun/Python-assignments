def main():

    fruits = ["orange", "apple", "banana", "strawberry", "kiwi"]
    desks = ["A", "B", "C"]

    'create a string that has the first characters of the `fruits` list in order "oabsk" '

    first_char = "".join(fruit[0] for fruit in fruits)
    print(first_char)
    "do the same but first order the fruits based on their 3rd character"

    third_char = "".join(fruit[0] for fruit in sorted(fruits, key=lambda x: x[2]))
    print(third_char)

    "do this with the last characters, the last characters in reverse order"

    lasts = "".join(fruits[i][len(fruits[i]) - 1] for i in range(len(fruits)))[::-1]
    print(lasts)

    "create a dictionary that cyclically matches the desks to the fruits like in class"

    fruit_desk = {x: desks[i % len(desks)] for i, x in enumerate(fruits)}
    print(fruit_desk)

    "Make a long string that has the following sentence for each fruit: " "The orange is at desk 'A'" " Do this with both f-strings and the `.format()` method."

    f_str_sentence = "".join(
        f"The {k} is at desk '{v}'. " for k, v in fruit_desk.items()
    )
    print(f_str_sentence)

    format_str_sentence = "".join(
        "The {fruit} is at desk '{desk}'. ".format(fruit=k, desk=v)
        for k, v in fruit_desk.items()
    )
    print(format_str_sentence)

    """Using the dictionary you created and the format method create a string that
      lists the desks' of the fruit in alphabetical order of the fruits. Also do it
      reverse alphabetical."""

    desk_alphabetical = "".join(
        "{desk}, ".format(desk=v, fruit=k) for k, v in sorted(fruit_desk.items())
    )
    print(desk_alphabetical)

    desk_alphabetical_r = "".join(
        "{desk}, ".format(desk=v, fruit=k)
        for k, v in sorted(fruit_desk.items(), reverse=True)
    )
    print(desk_alphabetical_r)

    "make a list of every second element of fruits"
    second_element_list = fruits[1::2]
    print(second_element_list)

    "- concatenate the strings in the fruit list, then make a list of every third character of this new string"

    every_third_char = "".join(fruits)[2::3]
    print(every_third_char)

    """
    - from the fruit:desk dictionary create a new dictionary which is desk:how many
      fruits are at the desk"""

    new_dict = [[key, fruit_desk[key]] for key in fruit_desk]
    cnt_a = 0
    cnt_b = 0
    cnt_c = 0
    for i in range(len(new_dict)):
        if new_dict[i][1] == "A":
            cnt_a += 1
        if new_dict[i][1] == "B":
            cnt_b += 1
        if new_dict[i][1] == "C":
            cnt_c += 1
    new_dict = {"A": cnt_a, "B": cnt_b, "C": cnt_c}
    print(new_dict)

    "using this new dictionary, make a string for each desk that says Desk A has 002 fruits, with leading zeros like here."

    for k, v in new_dict.items():
        x = "".join(
            "Desk {desk} has {value} fruits. ".format(desk=k, value=str(v).zfill(3))
        )
    print(x)


if __name__ == "__main__":
    main()
