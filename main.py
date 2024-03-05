import numpy as np

class BayesAktienkurs:

    def __init__(self, kursdaten):
        self.kursdaten = kursdaten
        self.steigungen = kursdaten[kursdaten > 0].shape[0]
        self.senkungen = kursdaten[kursdaten < 0].shape[0]
        self.gesamt = len(kursdaten)

    def prior(self):
        """
        Berechnet die Wahrscheinlichkeit a priori für Steigung und Senkung.
        """
        p_steigung = self.steigungen / self.gesamt
        p_senkung = self.senkungen / self.gesamt
        return p_steigung, p_senkung

    def likelihood(self, neuer_kurs):
        """
        Berechnet die Wahrscheinlichkeit der Kursentwicklung a posteriori.
        """
        if neuer_kurs > 0:
            p_steigung = neuer_kurs / self.steigungen
        else:
            p_steigung = 0
        if neuer_kurs < 0:
            p_senkung = -neuer_kurs / self.senkungen
        else:
            p_senkung = 0
        return p_steigung, p_senkung

    def posterior(self, neuer_kurs):
        """
        Berechnet die Wahrscheinlichkeit a posteriori für Steigung und Senkung.
        """
        p_steigung_prior, p_senkung_prior = self.prior()
        p_steigung_likelihood, p_senkung_likelihood = self.likelihood(neuer_kurs)
        p_steigung_posterior = (p_steigung_prior * p_steigung_likelihood) / (
            p_steigung_prior * p_steigung_likelihood + p_senkung_prior * p_senkung_likelihood
        )
        p_senkung_posterior = (p_senkung_prior * p_senkung_likelihood) / (
            p_steigung_prior * p_steigung_likelihood + p_senkung_prior * p_senkung_likelihood
        )
        return p_steigung_posterior, p_senkung_posterior

# Beispiel
kursdaten = np.array([1, 2, -3, 4, 5, -1, 2, 3])
model = BayesAktienkurs(kursdaten)

neuer_kurs = 2

p_steigung, p_senkung = model.posterior(neuer_kurs)

print(f"Wahrscheinlichkeit für Steigung: {p_steigung:.2f}")
print(f"Wahrscheinlichkeit für Senkung: {p_senkung:.2f}")

