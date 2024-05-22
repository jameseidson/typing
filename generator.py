import random

# TODO: add a generator for "frequently used vim motions" so that I can get faster with vim
# Some motions to start the list:
#  * yiw
#  * yi]
#  * yi}
#  * v$
#  * v^

home_row = "asdfjkl;"
shift_home_row = "ASDFJKL:"

index = "c4rfv5tgb6yhn7ujm8"
shift_index = "C$RFV%TGB^YHN&UJM*"

middle = "3edx9ik,"
shift_middle = "#EDX,(IK<"

ring = "2wsz0ol."
shift_ring = "@WSZ)OL>"

pinky = "1qa-p;/=[']\\"
shift_pinky = "!QA_P:+{\"}|"

chars = index + shift_index + middle + shift_middle + ring + shift_ring + pinky + shift_pinky

def geometric_sample():
    word = []
    bernoulli_sample = True

    while bernoulli_sample:
        word.append(random.choice(chars))
        bernoulli_sample = random.choices([True, False], weights=[7, 3])[0]

    return "".join(word)


for _ in range(1500):
    print(geometric_sample(), end=" ")

print()
