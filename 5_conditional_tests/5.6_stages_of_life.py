age = 23

if age < 2:
    stage_of_life = "bebê"
elif age < 4:
    stage_of_life = "criança pequena (Toddler)"
elif age < 13:
    stage_of_life = "criança"
elif age < 20:
    stage_of_life = "adolescente"
elif age < 65:
    stage_of_life = "adulto(a)"
elif age >= 65:
    stage_of_life = "idoso(a)"

print(f"A pessoa é um(a) {stage_of_life}")