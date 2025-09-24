import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches


def erzeuge_ekg_signal(herzfrequenz=70):
    """Erzeugt ein vereinfachtes EKG-Signal"""
    # Zeitachse für einen Herzschlag
    t = np.linspace(0, 1, 500)

    # P-Welle (Vorhof-Kontraktion)
    p_welle = 0.15 * np.exp(-100 * (t - 0.15) ** 2)

    # QRS-Komplex (Ventrikel-Kontraktion)
    q_welle = -0.1 * np.exp(-500 * (t - 0.35) ** 2)
    r_welle = 1.0 * np.exp(-200 * (t - 0.4) ** 2)
    s_welle = -0.15 * np.exp(-500 * (t - 0.45) ** 2)

    # T-Welle (Erholung)
    t_welle = 0.2 * np.exp(-50 * (t - 0.65) ** 2)

    # Kombiniere alle Komponenten
    ekg = p_welle + q_welle + r_welle + s_welle + t_welle

    return t, ekg


def herzschlag_simulator():
    """Interaktiver Herzschlag-Simulator"""
    print("=" * 50)
    print("🫀 BIOMEDIZINISCHER HERZSCHLAG-SIMULATOR")
    print("=" * 50)

    # Benutzereingabe
    print("\nGeben Sie die Patientendaten ein:")
    name = input("Patient Name: ")

    try:
        alter = int(input("Alter: "))
    except:
        alter = 25
        print(f"Ungültige Eingabe, verwende Standardalter: {alter}")

    print("\nWählen Sie einen Zustand:")
    print("1. Ruhezustand (60-70 bpm)")
    print("2. Leichte Aktivität (80-100 bpm)")
    print("3. Sport (120-150 bpm)")
    print("4. Stress/Angst (100-120 bpm)")

    wahl = input("\nIhre Wahl (1-4): ")

    # Herzfrequenz basierend auf Zustand
    if wahl == "1":
        herzfrequenz = np.random.randint(60, 71)
        zustand = "Ruhezustand"
        farbe = 'green'
    elif wahl == "2":
        herzfrequenz = np.random.randint(80, 101)
        zustand = "Leichte Aktivität"
        farbe = 'blue'
    elif wahl == "3":
        herzfrequenz = np.random.randint(120, 151)
        zustand = "Sport"
        farbe = 'orange'
    elif wahl == "4":
        herzfrequenz = np.random.randint(100, 121)
        zustand = "Stress/Angst"
        farbe = 'red'
    else:
        herzfrequenz = 70
        zustand = "Normal"
        farbe = 'green'

    # Berechne maximale Herzfrequenz (Faustformel)
    max_herzfrequenz = 220 - alter
    prozent_max = (herzfrequenz / max_herzfrequenz) * 100

    # Erstelle EKG-Visualisierung
    fig = plt.figure(figsize=(12, 8))

    # Oberer Plot: EKG-Signal (70% der Höhe)
    ax1 = plt.subplot2grid((10, 1), (0, 0), rowspan=6)

    # Unterer Bereich: Info-Box (30% der Höhe)
    ax2 = plt.subplot2grid((10, 1), (6, 0), rowspan=4)

    fig.suptitle(f'EKG-Monitor - Patient: {name}', fontsize=16, fontweight='bold')

    # EKG-Signal Setup
    t, ekg = erzeuge_ekg_signal(herzfrequenz)

    # Oberer Plot konfigurieren
    ax1.set_xlim(0, 4)
    ax1.set_ylim(-0.5, 1.5)
    ax1.set_xlabel('Zeit (Sekunden)', fontsize=12)
    ax1.set_ylabel('Amplitude (mV)', fontsize=12)
    ax1.set_title(f'Elektrokardiogramm - Zustand: {zustand}', fontsize=14)
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.set_facecolor('#f8f8f8')

    # EKG-Linie
    line, = ax1.plot([], [], 'darkgreen', linewidth=2)

    # Herzschlag-Marker
    marker, = ax1.plot([], [], 'ro', markersize=10)

    # Unterer Plot konfigurieren
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')

    # Hintergrund-Box für Informationen
    info_box = patches.FancyBboxPatch((0.5, 1), 9, 7,
                                      boxstyle="round,pad=0.1",
                                      linewidth=2,
                                      edgecolor=farbe,
                                      facecolor='white',
                                      alpha=0.9)
    ax2.add_patch(info_box)

    # Große BPM-Anzeige
    bpm_text = ax2.text(5, 6, f'❤️ {herzfrequenz} BPM',
                        fontsize=32, ha='center', fontweight='bold',
                        color=farbe)

    # Status-Text
    status_text = ax2.text(5, 4.5, f'Status: {zustand}',
                           fontsize=16, ha='center', color='black')

    # Detail-Informationen
    detail_text = f"""Patient: {name} | Alter: {alter} Jahre
Max. Herzfrequenz: {max_herzfrequenz} BPM
Aktuelle Belastung: {prozent_max:.1f}% der Max. HF"""

    details = ax2.text(5, 2.5, detail_text,
                       fontsize=11, ha='center', va='center',
                       color='darkblue')

    # Bewertung
    if prozent_max > 85:
        bewertung = "HOCH - Intensive Belastung"
        bewertung_farbe = 'red'
    elif prozent_max < 70:
        bewertung = "NORMAL - Gesunder Bereich"
        bewertung_farbe = 'green'
    else:
        bewertung = "MODERAT - Mittlere Belastung"
        bewertung_farbe = 'orange'

    bewertung_text = ax2.text(5, 1, bewertung,
                              fontsize=12, ha='center',
                              fontweight='bold', color=bewertung_farbe)

    # Daten für Animation vorbereiten
    # Erstelle längeres Signal für kontinuierliche Animation
    full_t = []
    full_ekg = []
    for i in range(10):  # 10 Herzschläge
        full_t.extend(t + i)
        full_ekg.extend(ekg)

    full_t = np.array(full_t)
    full_ekg = np.array(full_ekg)

    # Animation-Funktion
    def animate(frame):
        # Zeitfenster das sich bewegt
        current_time = frame * 0.01

        # Finde sichtbare Punkte
        mask = (full_t >= current_time) & (full_t <= current_time + 4)

        if np.any(mask):
            x_data = full_t[mask] - current_time
            y_data = full_ekg[mask]
            line.set_data(x_data, y_data)

            # Marker für aktuellen Herzschlag
            if len(x_data) > 0:
                # Finde R-Zacke (höchster Punkt)
                r_peaks = []
                for i in range(1, len(y_data) - 1):
                    if y_data[i] > 0.8 and y_data[i] > y_data[i - 1] and y_data[i] > y_data[i + 1]:
                        r_peaks.append(i)

                if r_peaks:
                    peak_idx = r_peaks[-1]
                    marker.set_data([x_data[peak_idx]], [y_data[peak_idx]])
                else:
                    marker.set_data([], [])

        # Pulsierender Text-Effekt
        scale = 1 + 0.1 * np.sin(frame * 0.15)
        bpm_text.set_fontsize(32 * scale)

        # Reset wenn am Ende
        if current_time > 6:
            return animate(0)

        return line, marker, bpm_text

    # Starte Animation
    anim = FuncAnimation(fig, animate, frames=600,
                         interval=50, blit=True, repeat=True)

    plt.tight_layout()

    # Medizinische Analyse in der Konsole
    print("\n" + "=" * 50)
    print("📊 MEDIZINISCHE ANALYSE")
    print("=" * 50)
    print(f"\n✓ Herzfrequenz: {herzfrequenz} BPM")
    print(f"✓ Zustand: {zustand}")
    print(f"✓ {prozent_max:.1f}% der maximalen Herzfrequenz")

    if herzfrequenz < 60:
        print("\n⚠️ Bradykardie: Herzfrequenz unter 60 BPM")
        print("   → Empfehlung: Arzt konsultieren")
    elif herzfrequenz > 100 and zustand == "Ruhezustand":
        print("\n⚠️ Tachykardie: Erhöhte Ruheherzfrequenz")
        print("   → Empfehlung: Weitere Untersuchung nötig")
    else:
        print("\n✅ Herzfrequenz im normalen Bereich für den Zustand")

    print(f"\n💡 Fun Fact: Ihr Herz schlägt etwa {herzfrequenz * 60 * 24:,} Mal pro Tag!")
    print("\n🔴 Zum Beenden: Fenster schließen")

    # Zeige das Fenster
    plt.show()


# Hauptprogramm
if __name__ == "__main__":
    try:
        herzschlag_simulator()
    except KeyboardInterrupt:
        print("\n\nProgramm wurde beendet.")
    except Exception as e:
        print(f"\nFehler aufgetreten: {e}")
        print("Bitte stellen Sie sicher, dass numpy und matplotlib installiert sind:")
        print("pip install numpy matplotlib")
