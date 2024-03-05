def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):

    p_not_a = 1 - p_a
    p_b = (p_b_given_a * p_a) + (p_b_given_not_a * p_not_a)

    p_a_given_b = (p_b_given_a * p_a) / p_b
    return p_a_given_b

# Beispielanwendung
# Annahmen: P(A) = Wahrscheinlichkeit des Ereignisses A
#           P(B|A) = Wahrscheinlichkeit des Ereignisses B unter der Bedingung, dass A eingetreten ist
#           P(B|¬A) = Wahrscheinlichkeit des Ereignisses B unter der Bedingung, dass A nicht eingetreten ist


volBuy = 800000
volSell = 200000



p_A = 0.5  # Beispielwert für P(A)
p_B_given_A = volBuy/(volBuy+volSell)  # Beispielwert für P(B|A)
p_B_given_not_A = volSell/(volBuy+volSell)  # Beispielwert für P(B|¬A)


result = bayes_theorem(p_A, p_B_given_A, p_B_given_not_A)
print(f'Die Wahrscheinlichkeit von A unter der Bedingung von B ist: {result}')






