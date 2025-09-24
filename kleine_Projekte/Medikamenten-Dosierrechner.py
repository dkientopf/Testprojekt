print("=" * 60)
print("    💊 MEDIKAMENTEN-DOSIERUNGSRECHNER FÜR KINDER")
print("         Sicher berechnen, Leben schützen")
print("=" * 60)

# Patientendaten eingeben
print("\n📋 PATIENTENDATEN:")
name = input("Name des Kindes: ")
gewicht = float(input("Gewicht in kg: "))
alter = int(input("Alter in Jahren: "))

# Medikament auswählen
print("\n💊 MEDIKAMENT AUSWÄHLEN:")
print("1. Paracetamol (Schmerzmittel)")
print("2. Ibuprofen (Entzündungshemmer)")
print("3. Amoxicillin (Antibiotikum)")

medikament = input("\nWählen Sie (1-3): ")

# Berechnung der Dosierung (vereinfachte medizinische Formeln)
if medikament == "1":
    # Paracetamol: 10-15 mg pro kg Körpergewicht
    med_name = "Paracetamol"
    dosis_min = gewicht * 10
    dosis_max = gewicht * 15
    max_tagesdosis = gewicht * 60  # Max 60mg/kg pro Tag
    intervall = "alle 6 Stunden"

elif medikament == "2":
    # Ibuprofen: 5-10 mg pro kg Körpergewicht
    med_name = "Ibuprofen"
    dosis_min = gewicht * 5
    dosis_max = gewicht * 10
    max_tagesdosis = gewicht * 30  # Max 30mg/kg pro Tag
    intervall = "alle 8 Stunden"

elif medikament == "3":
    # Amoxicillin: 20-40 mg pro kg Körpergewicht
    med_name = "Amoxicillin"
    dosis_min = gewicht * 20
    dosis_max = gewicht * 40
    max_tagesdosis = gewicht * 80  # Max 80mg/kg pro Tag
    intervall = "alle 8 Stunden"

else:
    print("❌ Ungültige Auswahl!")
    exit()

# Sicherheitsprüfung für Alter
if alter < 1:
    warnung = "⚠️ ACHTUNG: Säugling! Arzt konsultieren!"
    farbe = "🔴"
elif alter < 3:
    warnung = "⚠️ Kleinkind - besondere Vorsicht!"
    farbe = "🟡"
else:
    warnung = "✅ Altersgerechte Dosierung möglich"
    farbe = "🟢"

# Ergebnis anzeigen
print("\n")
print("=" * 60)
print("           📊 DOSIERUNGSEMPFEHLUNG")
print("=" * 60)
print(f"\nPatient: {name}")
print(f"Alter: {alter} Jahre | Gewicht: {gewicht} kg")
print(f"\nMedikament: {med_name}")
print(f"{farbe} Status: {warnung}")
print("\n" + "-" * 60)

print("\n💊 EMPFOHLENE EINZELDOSIS:")
print(f"   {dosis_min:.0f} - {dosis_max:.0f} mg")
print(f"   Einnahme: {intervall}")

print("\n📅 MAXIMALE TAGESDOSIS:")
print(f"   Nicht mehr als {max_tagesdosis:.0f} mg in 24 Stunden")

# Umrechnung in Löffel/Tabletten (praktisch!)
print("\n🥄 PRAKTISCHE DOSIERUNG:")
if med_name == "Paracetamol":
    # Saft: 200mg/5ml ist Standard
    ml_min = (dosis_min / 200) * 5
    ml_max = (dosis_max / 200) * 5
    print(f"   Saft (200mg/5ml): {ml_min:.1f} - {ml_max:.1f} ml")
    print(f"   = etwa {ml_min / 5:.1f} - {ml_max / 5:.1f} Teelöffel")
elif med_name == "Ibuprofen":
    # Saft: 100mg/5ml ist Standard
    ml_min = (dosis_min / 100) * 5
    ml_max = (dosis_max / 100) * 5
    print(f"   Saft (100mg/5ml): {ml_min:.1f} - {ml_max:.1f} ml")
    print(f"   = etwa {ml_min / 5:.1f} - {ml_max / 5:.1f} Teelöffel")

# Sicherheitshinweise
print("\n" + "=" * 60)
print("⚠️  WICHTIGE SICHERHEITSHINWEISE:")
print("=" * 60)
print("• Diese Berechnung ersetzt NICHT den Arztbesuch")
print("• Bei Unsicherheit immer Arzt oder Apotheker fragen")
print("• Packungsbeilage beachten")
print("• Bei Überdosierung sofort Giftnotruf: 📞 030-19240")

# Fun Fact
print("\n💡 WUSSTEN SIE?")
if gewicht < 10:
    print("Bei Babys ist die korrekte Dosierung EXTREM wichtig!")
    print("Schon kleine Fehler können gefährlich sein.")
elif gewicht < 20:
    print("Kinder verstoffwechseln Medikamente anders als Erwachsene.")
    print("Darum ist gewichtsbasierte Dosierung so wichtig!")
else:
    print("Falsche Dosierung ist eine der häufigsten Ursachen")
    print("für Medikamenten-Nebenwirkungen bei Kindern.")

print("\n✨ Darum ist Informatik in der Medizin wichtig:")
print("   Präzise Berechnungen können Leben retten!")
print("=" * 60)
