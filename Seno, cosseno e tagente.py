import math
ângulo = float(input("digite o ângulo que deseja"))
seno = math.sin(math.radians(ângulo))
print("O ângulo de {} tem o seno de {:.2f} ".format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print("O ângulo de {} tem o cosseno de {:.2f} ".format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print("O ângulo de {} tem a tangente  de {:.2f} ".format(ângulo, tangente))