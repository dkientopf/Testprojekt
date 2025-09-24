print("❤️ PULS-CHECKER")
print("=" * 30)

alter = int(input("Alter: "))
puls = int(input("Puls: "))

# Berechne Normalbereich
if alter < 1:
    normal_min = 100
    normal_max = 160
elif alter < 10:
    normal_min = 70
    normal_max = 120
elif alter < 60:
    normal_min = 60
    normal_max = 100
else:
    normal_min = 60
    normal_max = 90

# Diagnose
print("\n" + "=" * 30)
if puls < normal_min:
    print("🐌 ZU LANGSAM!")
    print(f"Normal: {normal_min}-{normal_max}")
    print("→ Mögliche Unterfunktion")
elif puls > normal_max:
    print("🏃 ZU SCHNELL!")
    print(f"Normal: {normal_min}-{normal_max}")
    print("→ Stress? Sport? Koffein?")
else:
    print("✅ PERFEKT!")
    print(f"Puls {puls} ist normal")
    print(f"Bereich: {normal_min}-{normal_max}")
