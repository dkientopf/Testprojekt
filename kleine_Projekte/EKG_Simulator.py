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
    alter = int(input("Alter: "))

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
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    fig.suptitle(f'EKG-Monitor - Patient: {name}', fontsize=16, fontweight='bold')

    # EKG-Signal
    t, ekg = erzeuge_ekg_signal(herzfrequenz)

    # Oberer Plot: EKG-Signal
    ax1.set_xlim(0, 3)
    ax1.set_ylim(-0.5, 1.5)
    ax1.set_xlabel('Zeit (Sekunden)')
    ax1.set_ylabel('Amplitude (mV)')
    ax1.set_title(f'Elektrokardiogramm - Zustand: {zustand}')
    ax1.grid(True, alpha=0.3)
    ax1.set_facecolor('#f0f0f0')

    line, = ax1.plot([], [], 'k-', linewidth=2)

    # Unterer Plot: Herzfrequenz-Anzeige
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')

    # Herzfrequenz-Box
    rect = patches.Rectangle((1, 3), 8, 4, linewidth=2,
                             edgecolor=farbe, facecolor='white')
    ax2.add_patch(rect)

    # Text-Informationen
    info_text = ax2.text(5, 7.5, f'❤️ {herzfrequenz} BPM',
                         fontsize=30, ha='center', fontweight='bold', color=farbe)

    details = f"""
    Alter: {alter} Jahre
    Max. HF: {max_herzfrequenz} BPM
    Aktuell: {prozent_max:.1f}% der Max. HF

    Bewertung: {'⚠️ Hoch' if prozent_max > 85 else '✅ Normal' if prozent_max < 70 else '📊 Moderat'}
    """

    ax2.text(5, 2, details, fontsize=11, ha='center', va='top')

    # Animation
    def animate(frame):
        # Verschiebe das Signal nach links (Laufband-Effekt)
        x_data = []
        y_data = []

        for i in range(3):
            x_data.extend(t + i)
            y_data.extend(ekg)

        # Zeige nur einen Teil des Signals
        start = frame * 0.02
        x_display = np.array(x_data) - start

        # Filter die sichtbaren Punkte
        mask = (x_display >= 0) & (x_display <= 3)

        line.set_data(x_display[mask], np.array(y_data)[mask])

        # Pulsierendes Herz (Text)
        scale = 1 + 0.1 * np.sin(frame * 0.2)
        info_text.set_fontsize(30 * scale)

        return line, info_text

    anim = FuncAnimation(fig, animate, frames=1000,
                         interval=20, blit=True, repeat=True)

    plt.tight_layout()
    plt.show()

    # Medizinische Interpretation
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


# Hauptprogramm
if __name__ == "__main__":
    herzschlag_simulator()
