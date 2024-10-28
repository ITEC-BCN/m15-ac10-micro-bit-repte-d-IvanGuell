llindar_temperatura = 0
llindar_llum = 0
temperatura = 0
llum = 0

def on_forever():
    global llindar_temperatura, llindar_llum, temperatura, llum
    # Estableix els llindars
    llindar_temperatura = 22
    llindar_llum = 128
    while True:
        # Llegeix la temperatura
        temperatura = input.temperature()
        # Mostra "calor" o "fred" segons la temperatura
        if temperatura > llindar_temperatura:
            basic.show_string("calor")
        else:
            basic.show_string("fred")
        # Llegeix el nivell de llum
        llum = input.light_level()
        # Reproduir melodia segons el nivell de llum
        if llum > llindar_llum:
            music.start_melody(music.built_in_melody(Melodies.BIRTHDAY), MelodyOptions.ONCE)
        else:
            music.start_melody(music.built_in_melody(Melodies.BLUES), MelodyOptions.ONCE)
        # Espera un moment abans de la següent lectura
        basic.pause(2000)
basic.forever(on_forever)
