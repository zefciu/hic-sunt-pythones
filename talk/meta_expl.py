class NazwaKlasy(Bazowa1, Bazowa2):
    atr1 = 'wartosc1'
    atr2 = 'wartosc2'

NazwaKlasy = type('NazwaKlasy', (Bazowa1, Bazowa2), {
    'atr1': 'wartosc1', 'atr1': 'wartosc2'
})
