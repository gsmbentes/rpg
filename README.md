# ⚔️ Arena de Combate - POO RPG

Este projeto foi desenvolvido por **Gustavo** como um estudo prático de **Programação Orientada a Objetos (POO)** em Python. O sistema simula um combate entre diferentes classes de personagens, utilizando conceitos avançados de engenharia de software para gerenciar atributos, ataques e defesas de forma dinâmica.

## 🚀 Funcionalidades e Mecânicas

O jogo apresenta um sistema de combate por turnos onde a interação entre os objetos dita o fluxo da batalha:

* **Superclasse Jogo:** Define a base para todos os personagens, gerenciando o sistema de vida (HP) e garantindo que os valores nunca fiquem negativos.
* **Classe Herói:** Especialista em força física. Possui um bônus de dano baseado em seu "Poder" e utiliza um escudo físico que reduz o dano recebido.
* **Classe Mago:** Especialista em magia. Seus ataques são baseados em "Magia" pura e sua defesa utiliza uma barreira mística de alta absorção.
* **Sistema de Defesa Inteligente:** Cada classe calcula sua redução de dano de forma independente antes de atualizar o estado de vida global.

## 🛠️ Conceitos Técnicos Aplicados

Este projeto demonstra o domínio de pilares fundamentais da POO:

* **Herança:** As subclasses `Heroi` e `Mago` herdam as propriedades fundamentais da classe mãe `Jogo`, reaproveitando código e lógica.
* **Polimorfismo:** Os métodos `atacar` e `defender` são sobrescritos (Override) em cada subclasse para executar comportamentos específicos, mesmo mantendo a mesma assinatura.
* **Uso de `super()`:** Utilizado para chamar construtores e métodos da classe pai, garantindo que a lógica central de atualização de vida seja mantida sem redundância.
* **Lógica de Combate Automatizada:** O método de ataque de um objeto interage diretamente com o método de defesa do objeto inimigo.


## 📂 Estrutura do Projeto

O código está organizado em uma estrutura modular:
1.  **Módulo Base:** Definição dos atributos globais (Nome e Vida).
2.  **Módulos de Especialização:** Implementação das fórmulas de dano e redução de dano por classe.
3.  **Arena de Teste:** Área de execução onde os objetos são instanciados e as rodadas de combate são processadas.

---
*Projeto desenvolvido para fins de estudo sobre herança e polimorfismo em Python.*
