from emner import emner

def print_ut_emner():
    print("\n--- Registrerte emner ---")
    if not emner:
        print("Ingen emner registrert ennå.")
        return

    for i, e in enumerate(emner, start=1):
        print(f"{i}: {e}")
