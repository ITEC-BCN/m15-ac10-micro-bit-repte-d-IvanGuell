let llindar_temperatura = 0
let llindar_llum = 0
let temperatura = 0
let llum = 0
basic.forever(function () {
    // Estableix els llindars
    llindar_temperatura = 22
    llindar_llum = 128
    while (true) {
        // Llegeix la temperatura
        temperatura = input.temperature()
        // Mostra "calor" o "fred" segons la temperatura
        if (temperatura > llindar_temperatura) {
            basic.showString("calor")
        } else {
            basic.showString("fred")
        }
        // Llegeix el nivell de llum
        llum = input.lightLevel()
        // Reproduir melodia segons el nivell de llum
        if (llum > llindar_llum) {
            music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.Once)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Blues), MelodyOptions.Once)
        }
        // Espera un moment abans de la següent lectura
        basic.pause(2000)
    }
})
