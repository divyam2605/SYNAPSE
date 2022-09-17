# TATAKAE!

class Titandex:
    def __init__(self, titan_name, titan_height, titan_strength, titan_winning_streak):
        self.titan_name = titan_name
        self.titan_height = titan_height
        self.titan_strength = titan_strength
        self.titan_winning_streak = titan_winning_streak

    def TitanvsScout(self, name, strength):
        self.name = name
        self.strength = strength

        if self.titan_strength > strength:
            print(f'{self.titan_name} wins the contest!')
            self.titan_winning_streak += 1
        elif self.titan_strength < strength:
            print(f'{self.name} wins the contest!')
            self.titan_winning_streak = 0
        elif self.titan_strength == self.strength:
            print("Its a tie! What a great contest!")
            self.titan_winning_streak = 0

    def TitanvsTitan(self, titan2_name, titan2_strength):
        self.titan2_name = titan2_name
        self.titan2_strength = titan2_strength

        if self.titan_name == titan2_name:
            print("Now how is a Titan going to fight himself?\nEnter Again!")
        elif self.titan_strength > titan2_strength:
            print(f'{self.titan_name} wins the contest!')
            self.titan_winning_streak += 1
        elif self.titan_strength < titan2_strength:
            print(f'{self.titan2_name} wins the contest!')
            self.titan_winning_streak = 0
        elif self.titan_strength == self.titan2_strength:
            print("Its a tie! What a great contest!")
            self.titan_winning_streak = 0


t1 = Titandex("Founding Titan", 13, 350, 0)
t2 = Titandex("Attack Titan", 15, 275, 0)
t3 = Titandex("Armoured Titan", 15, 250, 0)
t4 = Titandex("Colossal Titan", 60, 300, 0)
t5 = Titandex("War Hammer Titan", 15, 235, 0)
t6 = Titandex("Beast Titan", 17, 250, 0)
t7 = Titandex("Cart Titan", 4, 175, 0)
t8 = Titandex("Female Titan", 14, 270, 0)
t9 = Titandex("Jaw Titan", 5, 225, 0)

t1.TitanvsScout("Hange", 230)
t2.TitanvsTitan("Colossal Titan", 300)

# Wanna See a Contest?

# For Titan vs Scout type:
#   t{index of 1st titan(see above)}.TitanvsScout("{scout name}", {scout strength})

# For Titan vs Titan type:
#   t{index of 1st titan(see above)}.TitanvsTitan("{titan name}", {titan strength})