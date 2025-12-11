from models.infrastructures import Infra


class Batiment:
    def __init__(self, id_building: str, list_infras: list[Infra]):
        self.id_building = id_building
        self.list_infras = list_infras

    def is_phase_0(self) -> bool:
        """
        RÈGLE MÉTIER : PHASE 0
        Retourne True si TOUTES les infrastructures connectées sont saines.
        Si une seule infra a besoin de réparation, ce n'est pas une Phase 0.
        """
        for infra in self.list_infras:
            if infra.needs_repair():
                return False
        return True

    def get_building_difficulty(self) -> float:
        return sum(self.list_infras)

    def __repr__(self):
        # Affichage conditionnel pour voir facilement la phase
        phase_label = "PHASE 0 (Sain)" if self.is_phase_0() else "À RÉPARER"
        return f"[{phase_label}] Bât {self.id_building} ({len(self.list_infras)} infras)"
    
    def __lt__(self, other):

        return self.get_building_difficulty() < other.get_building_difficulty()