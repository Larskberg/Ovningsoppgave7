from emner import Emne

class Studieplan:
    def __init__(self, plan_id, tittel):
        self.plan_id = plan_id
        self.tittel = tittel
        # Lister med emner per semester
        self.semestre = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: []
        }

    def __str__(self):
        return f"Studieplan {self.plan_id}: {self.tittel}"


# Felles ordbok med studieplaner: id -> Studieplan
studieplaner = {}


def lag_ny_studieplan():
    print("\n--- Lag ny studieplan ---")

    plan_id = input("Skriv inn ID for studieplan: ")
    if plan_id in studieplaner:
        print("En studieplan med denne ID finnes allerede.")
        return

    tittel = input("Skriv inn tittel for studieplan: ")

    # Opprett ny tom studieplan
    ny_plan = Studieplan(plan_id, tittel)
    studieplaner[plan_id] = ny_plan

    print(f"Ny studieplan opprettet: {ny_plan}")

