import random
times = ["Утром", "Днем", "Вечером", "Ночью", "После обеда", "Перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises =["гостей из забытого прошлого", "встреч со старыми знакомыми", "неожиданного праздника", "приятных перемен"]

i = 0

while i < 3:
    t = random.choice(times)
    a = random.choice(advices)
    p = random.choice(promises)
    print(t + " " + a + " " + p )
    i = i + 1
    