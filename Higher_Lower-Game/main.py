import art
import random
import game_data

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        if user_guess == "a":
            return True
        else:
            return False
    elif a_followers < b_followers:
        if user_guess == "b":
            return True
        else:
            return False
    return None


def format_data(info):
    info_name = info["name"]
    info_desc = info["description"]
    info_country = info["country"]
    return f"{info_name}, a {info_desc}, from {info_country}"

print(art.logo)
score = 0
option_b = random.choice(game_data.data)
continue_game = True

while continue_game:
    option_a = option_b
    option_b = random.choice(game_data.data)
    if option_a == option_b:
        option_b = random.choice(game_data.data)

    print(f"Compare A: {format_data(option_a)}")
    print(art.vs)
    print(f"Compare B: {format_data(option_b)}")

    guess = input("Who has more followers? Type 'A' or 'B'").lower()

    # Clear the screen
    print("\n" * 20)
    print(art.logo)

    a_followers = option_a["follower_count"]
    b_followers = option_b["follower_count"]

    #Check answer
    is_correct = check_answer(user_guess=guess,a_followers=a_followers,b_followers=b_followers)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        continue_game = False
