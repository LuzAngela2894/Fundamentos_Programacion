nombre=input("\nIngrese el nombre del estudiante: ")
peso=float(input("\nIngrese el peso del estudiante: "))

if peso<40:
    print("\nEl estudiante",nombre,"se encuentra en el rango de peso de menos de 40 kg.")
elif peso>=40 and peso<50:
    print("\nEl estudiante",nombre,"se encuentra en el rango de peso entre 40 y 50 kg.")
elif peso>=50 and peso<60:
    print("\nEl estudiante",nombre,"se encuentra en el rango de peso entre más de 50 y menos de 60 kg.")
elif peso>=60:
    print("\nEl estudiante",nombre,"se encuentra en el rango de peso igual o más de 60kg.")
