class enemy:
    def __init__(self, x):
        self.energy = x
    def get_energy(self):
        print(self.energy)

enemy1 = enemy(9)
boss = enemy(10)

enemy1.get_energy()
boss.get_energy()