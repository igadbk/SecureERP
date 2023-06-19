import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):

    new_id = []
    for i in range(number_of_small_letters):
        new_id.append(random.choice(string.ascii_lowercase))
    for i in range(number_of_capital_letters):
        new_id.append(random.choice(string.ascii_uppercase))
        new_id.append(str(random.choice(string.digits)))
        new_id.append(str(random.choice(allowed_special_chars)))

    random.shuffle(new_id)
    new_id = "".join(new_id)
    return new_id