"""
############################################################
Jogo da Velha
############################################################

:Author: *Davi Porto*
:Author: *Ludmila Meirelles*
:Contact: davi.ideiaop@gmail.com
:Date: 2013/04/02
:Status: This is a "work in progress"
:Revision: 0.1.0
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.

Update - Bug fix, agora marca empate (velha)
"""
from browser import html, doc
jogo = doc["main_container"]
n=input('Digite o numero de lados que voce deseja que tenha o seu jogo da velha:' )
n = int(n)
XO = ["http://jimdscott.com/static/images/tic-tac-toe-O.png",
"http://jimdscott.com/static/images/tic-tac-toe-X.png"]
BRANCO = ["http://images.fashion.me/Items/Item-1781866-500.jpg"]*(n*n)
PECAS = XO *((n*n)//2+1)
LD = 30
xo = [html.IMG(src=j, height=LD, width=LD) for j in PECAS]
branco = [html.IMG(src=j, height=LD, width=LD) for j in BRANCO]
BLUE = 'http://www.clker.com/cliparts/Z/W/N/F/6/p/light-blue-square-md.png'
blues = []
for bl in range(12):
 blue = html.IMG(src=BLUE, height=LD, width=LD)
 blue.style.opacity = 0.3
 blue.style.marginLeft = '-30px'
 blues.append(blue)
tabuleiro = html.TABLE(border = 2)
campo = html.TBODY()
jogo <= tabuleiro
tabuleiro <= campo
xoj = xo[:]

class Casa:
    def __init__(self, e_img):
        self.e_casa = html.TD(e_img)
        e_img.onclick = self.clicou
        self.tipo_peca = 0

    def ganhou(self):
        def tp(tira):
           return [uma_casa.tipo_peca for uma_casa in tira]
        mp = matriz_tipo_pecas = [uma_casa.tipo_peca for uma_casa in matriz_casas]
        mp = matriz_casas

        inc=1
        tirasx = [mp[ini:ini+n:inc] for ini in range(0,((n-1)*n)+1,n)]
        inc=n
        tirasy = [mp[ini:ini+(((n-1)*n)+1):inc] for ini in range(0,n)]

        barra = [mp[ini:ini+(n-1)*inc+(n-1):inc] for inc, ini in [(n-1,n-1),(n+1,0)]]

        possiveis = tirasx + tirasy + barra
        ganhou = [tira for tira in possiveis
        if (tp(tira) == n*[1]) or (tp(tira) == n*[2])]

        return ganhou
        if ganhou == [none]:
            print ("Deu velha!!")

    def clicou(self, evento):
        self.e_casa.html = ''
        e_peca = xoj.pop()
        self.tipo_peca = XO.index(e_peca.src) + 1
        print(self.tipo_peca)
        self.e_casa <= e_peca
        ganhou = self.ganhou()
        if ganhou:
            print("GANHOU!!!", ganhou)
            #return
            [c.e_casa <= blues.pop()
            for tira in ganhou for c in tira]
        #print(len(xoj))

matriz_casas = []

for m in range(2):
    linha = html.TR()
    campo <= linha
    for p in range((n*n)/2):
        coluna = html.TD(xo.pop())
        linha <= coluna
for m in range(n):
    linha = html.TR()
    campo <= linha
    for p in range(n):
        coluna = Casa(branco.pop())
        matriz_casas.append(coluna)
        #matriz_casas += [coluna]
        linha <= coluna.e_casa

