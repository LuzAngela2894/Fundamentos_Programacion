angulo=float(input("\nIngrese el valor del ángulo en grados: "))

if angulo<90:
    print("\nEl ángulo se considera AGUDO")
elif angulo>90:
    print("\nEl ángulo se considera OBTUSO")
elif angulo==90:
    print("\nEl ángulo se considera RECTO")
