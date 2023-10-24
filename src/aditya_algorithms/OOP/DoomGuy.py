# write a class Player with following stats:

# health - it represents the current health (min:0, max: 100)
# stamina - it represents the current remaining stamina (min:0, max: 50)
# level - it represents current level of the player (min:1, max: 10)
# bag_capacity - carrying capacity - total weight of weapons (min: 10, max: 250) kg

# methods:
# get_health(self): should return int representing current health
# get_stamina(self): should return int representing current stamina
# get_bag_capacity(self): should return float representing current bag_capacity
# get_level(self): should return current level of the player (int)

# level_up(self): should increase health by 5% of the current health
# and increase stamina by 2.5% of the current stamina
# and increase bag_capacity by 7.5%
# if any stats exceeds maximum then use the maximum value


class Player:
    # write the body here
    def __init__(self, health: float, stamina: float, level: int, bag_capacity: float):
        self.health = health
        self.stamina = stamina
        self.level = level
        self.bag_capacity = bag_capacity

    def __repr__(self):
        return (
            f"Player(health={self.health:.2f}, stamina={self.stamina:.2f},"
            f" level={self.level:d}, bag_capacity={self.bag_capacity:.2f})"
        )

    def __str__(self):
        return (
            f"Player(health={self.health:.2f}, stamina={self.stamina:.2f},"
            f" level={self.level:d}, bag_capacity={self.bag_capacity:.2f})"
        )

    def level_up(self):
        self.health = min((1 + 5 / 100) * self.health, 100)
        self.stamina = min((1 + 2.5 / 100) * self.stamina, 50)
        self.bag_capacity = min((1 + 7.5 / 100) * self.bag_capacity, 250)
        self.level += 1


if __name__ == "__main__":
    p1 = Player(health=15, stamina=25, level=3, bag_capacity=20.0)
    print(p1)
    p1.level_up()
    p1.level_up()
    print(p1)
