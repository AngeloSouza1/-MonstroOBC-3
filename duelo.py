def duelo(lutador1, lutador2):
   
    # Determinar ordem de ataque com base no poder
    if lutador1["poder"] > lutador2["poder"]:
        primeiro, segundo = lutador1, lutador2
    else:
        primeiro, segundo = lutador2, lutador1

    # Duelo
    while primeiro["vida"] > 0 and segundo["vida"] > 0:
        # Primeiro ataca segundo
        segundo["vida"] -= primeiro["poder"]
        if segundo["vida"] <= 0:
            return f"{primeiro['nome']} 🏆"

        # Segundo ataca primeiro
        primeiro["vida"] -= segundo["poder"]
        if primeiro["vida"] <= 0:
            return f"{segundo['nome']} 🏆"
