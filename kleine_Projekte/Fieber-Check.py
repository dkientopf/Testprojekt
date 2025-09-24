print("🌡️ FIEBER-SCHNELLDIAGNOSE")
print("=" * 40)

name = input("Patient: ")
temp = float(input("Temperatur in °C: "))
alter = int(input("Alter: "))

# Diagnose
print("\n" + "=" * 40)
print(f"Patient: {name}, {alter} Jahre")
print(f"Temperatur: {temp}°C")
print("=" * 40)

# Für Kinder gelten andere Grenzwerte!
if alter < 3:
    if temp < 36:
        print("❄️ UNTERKÜHLUNG - NOTFALL!")
    elif temp < 37.5:
        print("✅ Normal")
    elif temp < 38:
        print("🟡 Erhöhte Temperatur")
    elif temp < 39:
        print("🔴 Fieber - Arzt rufen!")
    else:
        print("🚨 HOHES FIEBER - NOTARZT!")
else:
    if temp < 36:
        print("❄️ UNTERKÜHLUNG - NOTFALL!")
    elif temp < 37:
        print("✅ Normal")
    elif temp < 38:
        print("🟡 Erhöhte Temperatur")
    elif temp < 40:
        print("🔴 Fieber - Medikamente geben")
    else:
        print("🚨 HOHES FIEBER - KRANKENHAUS!")

print("\n💊 Empfehlung:")
if temp > 38.5:
    dosis = 500 if alter > 12 else 250
    print(f"→ Paracetamol {dosis}mg")
    print("→ Viel trinken!")
    print("→ Wadenwickel")
