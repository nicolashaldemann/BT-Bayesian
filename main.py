import pandas as pd
import numpy as np
from scipy.stats import norm

# Datensatz mit historischen Kursdaten
df = pd.read_csv("aktienkursdaten.csv")

# Aktueller Aktienkurs
aktienkurs_heute = 100

# Priors
mu_0 = 0  # Mittelwert der Normalverteilung
sigma_0 = 1  # Standardabweichung der Normalverteilung

# Likelihood-Funktion
def likelihood(x, mu, sigma):
  return norm.pdf(x, loc=mu, scale=sigma)

# Bayes'sche Analyse
def bayes_analyse(aktienkurs_heute, mu_0, sigma_0):
  # Posterior-Verteilung
  mu_posterior = (mu_0 * sigma_0**2 + aktienkurs_heute) / (sigma_0**2 + 1)
  sigma_posterior = np.sqrt((sigma_0**2 * 1) / (sigma_0**2 + 1))

  # Wahrscheinlichkeit, dass der Kurs steigt
  p_steigt = norm.cdf(aktienkurs_heute, loc=mu_posterior, scale=sigma_posterior)

  # Entscheidungsempfehlung
  if p_steigt > 0.5:
    empfehlung = "Halten"
  else:
    empfehlung = "Verkaufen"

  return mu_posterior, sigma_posterior, p_steigt, empfehlung

# Ausgabe der Ergebnisse
mu_posterior, sigma_posterior, p_steigt, empfehlung = bayes_analyse(aktienkurs_heute, mu_0, sigma_0)

print("Posteriorer Mittelwert:", mu_posterior)
print("Posteriore Standardabweichung:", sigma_posterior)
print("Wahrscheinlichkeit, dass der Kurs steigt:", p_steigt)
print("Empfehlung:", empfehlung)
