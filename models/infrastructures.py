class Infra:
    def __init__(self, infra_id: str, length: float, infra_type: str, etat: str):
        self.infra_id = infra_id
        self.length = float(length)
        self.infra_type = infra_type
        self.etat = etat  # Nouvelle propriété : etat (a_remplacer, bon_etat, etc.)

    def needs_repair(self) -> bool:
        """
        Vérifie si l'infrastructure nécessite une réparation.
        Basé sur la colonne 'etat' du CSV.
        """
        return self.etat == "a_remplacer"

    def get_infra_difficulty(self) -> float:
        # Si pas de réparation, la difficulté est nulle (coût 0)
        if not self.needs_repair():
            return 0.0
            
        # Logique de difficulté existante
        coefficient = 1.0
        if "fourreau" in self.infra_type:
            coefficient = 1.5 
        elif "semi-aerien" in self.infra_type:
            coefficient = 1.2
        return self.length * coefficient

    def __radd__(self, other):
        # Permet l'utilisation de sum() : additionne la difficulté actuelle au total précédent
        return other + self.get_infra_difficulty()

    def __repr__(self):
        status = "HS" if self.needs_repair() else "OK"
        return f"<Infra {self.infra_id} [{status}]>"