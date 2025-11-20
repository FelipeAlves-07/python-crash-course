# Essa versão executará o bloco após o segundo elif
alien_color = "red"

if alien_color == "green":
    points_earned = 5
elif alien_color == "yellow":
    points_earned = 10
elif alien_color == "red":
    points_earned = 15

print(f"Você ganhou {points_earned} pontos!")