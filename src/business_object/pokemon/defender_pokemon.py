from src.business_object.abstract_pokemon import AbstractPokemon


class DefenderPokemon(AbstractPokemon):
    def __init__(self, stat_max, stat_current, level, name):
        super().__init__(self, stat_max, stat_current, level, name, "Defender")

    def get_pokemon_attack_coef(self) -> float:
        return 1 + (self.attack_current + self.defense_current) / 200
