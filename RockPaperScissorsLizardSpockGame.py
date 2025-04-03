class Jogo_mano_a_mano:

    def __init__(self):
        self.armas = ('Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock')
        self.regras = ('pedra quebra tesoura', 'pedra esmaga lagarto',
                       'papel cobre pedra', 'papel refuta spock', 'tesoura corta papel', 'tesoura degola lagarto',
                       'lagarto envenena spock', 'lagarto come papel', 'spock vaporiza pedra', 'spock quebra tesoura')
        self.partidas = ({self.armas.index('Pedra'): self.armas.index('Tesoura')},
                         {self.armas.index('Pedra'): self.armas.index('Lagarto')},
                         {self.armas.index('Papel'): self.armas.index('Pedra')},
                         {self.armas.index('Papel'): self.armas.index('Spock')},
                         {self.armas.index('Tesoura'): self.armas.index('Papel')},
                         {self.armas.index('Tesoura'): self.armas.index('Lagarto')},
                         {self.armas.index('Lagarto'): self.armas.index('Spock')},
                         {self.armas.index('Lagarto'): self.armas.index('Papel')},
                         {self.armas.index('Spock'): self.armas.index('Pedra')},
                         {self.armas.index('Spock'): self.armas.index('Tesoura')})

    def iniciar_jogo(self):
        boas_vindas = '''
            ______________________________________________________
          --                                                      --
          |  BEM-VINDO AO JOGO PEDRA-PAPEL-TESOURA-LAGARTO-SPOCK!  |
          --                                                      --
            ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
          '''
        print(f'{boas_vindas}\n\n')
        print(
            '\nO jogo tem 5 armas e 3 partidas, acabando quando:\n> um jogador vence 2 de 3 partidas\n> um empate ocorre em 2 de 3 partidas')
        print('\nPara cada arma, as regras são:')
        for regra in self.regras:
            print(f'> {regra}')
        print('\n\nIniciando o jogo...\n')

        jogando = 3
        vitorias_jogador_1 = 0
        vitorias_jogador_2 = 0
        empates = 0
        while jogando > 0:

            print('\nJogador 1, qual é sua arma?')
            for arma in self.armas:
                print(f'{self.armas.index(arma)} - {arma}')
            while True:
                try:
                    self.entrada_de_arma_1 = input('• ')
                    self.arma_1 = int(self.entrada_de_arma_1)
                    self.armas[self.arma_1]
                    break
                except (ValueError, IndexError):
                    print(f'\nArma {self.entrada_de_arma_1} inválida - qual é sua arma entre 0 e 4?')

            print('\nJogador 2, qual é sua arma?')
            for arma in self.armas:
                print(f'{self.armas.index(arma)} - {arma}')
            while True:
                try:
                    self.entrada_de_arma_2 = input('• ')
                    self.arma_2 = int(self.entrada_de_arma_2)
                    self.armas[self.arma_1]
                    break
                except (ValueError, IndexError):
                    print(f'\nArma {self.entrada_de_arma_2} inválida - qual é sua arma entre 0 e 4?')

            self.partida = {self.arma_1: self.arma_2}
            self.partida_invertida = {self.arma_2: self.arma_1}
            if self.partida in self.partidas:
                print(f'\n\nJogador 1 vence: {self.regras[self.partidas.index(self.partida)]}!\n')
                vitorias_jogador_1 += 1
            elif self.partida_invertida in self.partidas:
                print(f'\n\nJogador 2 vence: {self.regras[self.partidas.index(self.partida_invertida)]}!\n')
                vitorias_jogador_2 += 1
            else:
                print(f'\n\nEmpate: {self.armas[self.arma_1].lower()} contra {self.armas[self.arma_2].lower()}!\n')
                empates += 1

            if vitorias_jogador_1 == 2:
                jogando = 0
                print(f'\n\nO jogador 1 venceu o jogo, levando {vitorias_jogador_1} de 3 partidas!')
            elif vitorias_jogador_2 == 2:
                jogando = 0
                print(f'\n\nO jogador 2 venceu o jogo, levando {vitorias_jogador_2} de 3 partidas!')
            elif empates == 2 or (empates == 1 and vitorias_jogador_1 == vitorias_jogador_2):
                jogando = 0
                print(f'O jogo acabou empatado.')

        novo_jogo = input('\nIniciar novo jogo (s/n)?\n• ').lower()
        if novo_jogo == 's':
            Jogo_mano_a_mano().iniciar_jogo()


Jogo_mano_a_mano().iniciar_jogo()