class Jogo:
    def __init__(self, nome_persona):
        self.vida = 100
        self.nome_persona = nome_persona    

    def atacar(self, inimigo):
        dano = 10
        print(f"⚔️ {self.nome_persona} realiza um ataque básico!")
        inimigo.defender(dano)

    def defender(self, dano):
        self.vida -= dano
        if self.vida < 0: 
            self.vida = 0
        print(f"🛡️ {self.nome_persona} recebeu {dano} de dano! Vida restante: {self.vida}")

class Heroi(Jogo):
    def __init__(self, nome_persona, poder):
        super().__init__(nome_persona) 
        self.poder = poder

    def atacar(self, inimigo):
        dano_total = 10 + self.poder
        print(f"🔥 {self.nome_persona} usou FORÇA BRUTA!")
        inimigo.defender(dano_total)

    def defender(self, dano):
        escudo = 20
        dano_final = dano - escudo
        if dano_final < 0:
            dano_final = 0
        self.vida -= dano_final
        print(f"🛡️ {self.nome_persona} usou o Escudo! Dano reduzido para: {dano_final}. Vida: {self.vida}")

class Mago(Jogo):
    def __init__(self, nome_persona, magia):
        super().__init__(nome_persona)
        self.magia = magia

    def atacar(self, inimigo):
        print(f"✨ {self.nome_persona} lançou uma MAGIA poderosa!")
        inimigo.defender(self.magia)

    def defender(self, dano):
        barreira = 27
        dano_final = dano - barreira
        if dano_final < 0:
            dano_final = 0
        
        self.vida -= dano_final
        print(f"🔮 {self.nome_persona} criou uma Barreira Mágica! Dano reduzido para: {dano_final}. Vida: {self.vida}")


print("-" * 20, "ARENA DE COMBATE", "-" * 20)
heroi = Heroi("Gustavo", 15) 
mago = Mago("Gustavo2", 40)   

mago.atacar(heroi)   
heroi.atacar(mago)
heroi.defender(12)
mago.defender(2)