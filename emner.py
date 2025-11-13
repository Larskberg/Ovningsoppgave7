class Emne:
    def __init__(self, kode, semester, studiepoeng):
        if semester not in ("H", "V"):
            raise ValueError("Semester må være 'H' (høst) eller 'V' (vår).")
        self.kode = kode
        self.semester = semester
        self.studiepoeng = studiepoeng

    def __str__(self):
        return f"{self.kode} ({self.semester}, {self.studiepoeng} sp)"


# Felles liste med emner
emner = []
