class Jogo:
    def __init__(self, nome_persona):
        self.vida = 100
        self.nome_persona = nome_persona    

    def atacar(self, inimigo):
        """Ataque básico padrão para qualquer personagem."""
        dano = 10
        print(f"⚔️ {self.nome_persona} realiza um ataque básico!")
        inimigo.defender(dano)

    def defender(self, dano):
        """Lógica central de dano: garante que a vida não fique negativa."""
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"💥 {self.nome_persona} recebeu {dano} de dano! Vida restante: {self.vida}")


class Heroi(Jogo):
    def __init__(self, nome_persona, poder):
        super().__init__(nome_persona) 
        self.poder = poder

    def atacar(self, inimigo):
        """Ataque especial do Herói baseado em poder físico."""
        dano_total = 10 + self.poder
        print(f"\n🔥 {self.nome_persona} usou FORÇA BRUTA!")
        inimigo.defender(dano_total)

    def defender(self, dano):
        """Defesa com escudo: reduz o dano antes de aplicar à vida."""
        escudo = 20
        dano_final = dano - escudo
        if dano_final < 0:
            dano_final = 0
        
        print(f"🛡️ {self.nome_persona} usou o Escudo!")
        super().defender(dano_final)


class Mago(Jogo):
    def __init__(self, nome_persona, magia):
        super().__init__(nome_persona)
        self.magia = magia

    def atacar(self, inimigo):
        """Ataque especial do Mago baseado em poder mágico."""
        print(f"\n✨ {self.nome_persona} lançou uma MAGIA poderosa!")
        inimigo.defender(self.magia)

    def defender(self, dano):
        """Defesa com barreira: absorção mágica de dano."""
        barreira = 27
        dano_final = dano - barreira
        if dano_final < 0:
            dano_final = 0
        
        print(f"🔮 {self.nome_persona} criou uma Barreira Mágica!")
        super().defender(dano_final)


print("-" * 20, "ARENA DE COMBATE", "-" * 20)

heroi = Heroi("Gustavo Guerreiro", 15) 
mago = Mago("Gustavo Mago", 40)   

mago.atacar(heroi)    

heroi.atacar(mago)

print("\n" + "-" * 56)
print(f"ESTADO FINAL: {heroi.nome_persona}: {heroi.vida} HP | {mago.nome_persona}: {mago.vida} HP")
