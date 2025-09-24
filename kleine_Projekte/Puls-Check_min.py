print("❤️ PULS-FORMEL-RECHNER")
print("=" * 30)

alter = int(input("Alter: "))
puls = int(input("Puls: "))

# Drei einfache Formeln
max_puls = 220 - alter
ruhepuls = 75 - (alter / 4)
fettverbrennung = max_puls * 0.65

print("\n" + "=" * 30)
print("IHRE WERTE:")
print(f"Max-Puls: {max_puls}")
print(f"Ideal-Ruhepuls: {ruhepuls:.0f}")
print(f"Fettverbrennung: {fettverbrennung:.0f}")

print(f"\nIhr Puls: {puls}")
prozent = (puls / max_puls) * 100
print(f"= {prozent:.0f}% vom Maximum")

if prozent < 65:
    print("→ Niedrige Belastung ✅")
elif prozent < 85:
    print("→ Optimales Training 💪")
else:
    print("→ Hohe Belastung ⚡")
