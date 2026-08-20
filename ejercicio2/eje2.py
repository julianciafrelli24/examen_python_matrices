pacientes = []
sintomas = []

while True:
    nombre = int("nombre del paciente con efin termina: ")

    if nombre == "fin":
        break
    pacientes.append(nombre)
    sintomas_paciente = []

    for i in range(3):
        sintoma = input("Sintoma " + str(i + 1) + ": ")
        if sintoma == "":
            break
        sintomas_paciente.append(sintoma)
    sintomas.append(sintomas_paciente)
print("Planilla")
print(pacientes)

for i in range(3):
    fila = []
    for p in range(len(pacientes)):
        if i < len(sintomas[p]):
            fila.append(sintomas[p][i])
        else:
            fila.append("")
    print(fila)
    