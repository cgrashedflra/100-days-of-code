import random

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"

title = "? DR.BOMB WIREBREAK: BOMB PROTOCOL ?"

print(title)

print(f"""
{YELLOW}RULES:{RESET}
- 3 wires: {RED}red{RESET}, {GREEN}green{RESET}, {CYAN}cyan{RESET}
- Cut in correct sequence
- Wrong cut = BOOM ?
""")

wires = ["red", "cyan", "green"]
diffuse_sequence = random.sample(wires, 3)

step = 0
game_over = False

while not game_over:

    user_input = input("Choose wire to cut: ").lower()

    if user_input not in diffuse_sequence:
        print(f"""
        ? ARE YOU KIDDING ME?!

        What on earth are you talking about?

        You said: "{user_input}"

        That color doesn?t even exist in this bomb setup.

        Are you color blind or just confused? ?

        Look carefully ? ONLY the valid wires are connected to this bomb.

        Think properly before choosing again...
        Otherwise we all go BOOM ?
        """)

        print("?? Choose again carefully... or the bomb will detonate.")
    else:
        if user_input == diffuse_sequence[step]:
            print(f"you just cut the {user_input} wire, nothing happend we are safe!!")

            step += 1

            if step == len(diffuse_sequence):
                print("? Bomb Defused! You win!")
                game_over = True

        else:
            print("? BOOM! Wrong wire!")
            game_over = True