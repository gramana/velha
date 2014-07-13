from browser import html,doc
jogo = doc["main_container"]
XO = ["http://indervilla.com/home/2013/01/Demon-Dracula-HD.jpg",
"https://misteriosacontecem.files.wordpress.com/2011/07/steps_o_anjo.jpg"]
BRANCO = ["http://images.fashion.me/Items/Item-1781866-500.jpg"]* 16
PECAS = XO * 8
LD = 40
xo = [html.IMG(src=j, height=LD, width=LD) for j in PECAS]
branco = [html.IMG(src=j, height=LD, width=LD) for j in BRANCO]
tabuleiro = html.TABLE(border = 3)
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
        mp = matriz_tipo_pecas = [
            uma_casa.tipo_peca
            for uma_casa in
            matriz_casas]


        barra=[mp[ini:ini+3*inc+3:inc] for inc, ini in [(3,3),(5,0)]]

        #metodo ganhou funcionando nas tirasX
        inc = 1
        tirasx =[mp[ini:ini+4:inc] for ini in range(0,14,4)]

        #metodo ganhou funcionando nas tirasY
        inc = 4
        tirasy =[mp[ini:ini+14:inc] for ini in range(0,4)]


        possiveis = barra + tirasx + tirasy
        ganhou = any ([(tira == [1,1,1,1])
        or (tira == [2,2,2,2])
        for tira in possiveis])
        #print(mp)
        return ganhou

    def clicou(self, evento):
        self.e_casa.html = ''
        e_peca = xoj.pop()
        self.tipo_peca = XO.index(e_peca.src) + 1
        #print(self.tipo_peca)
        self.e_casa <= e_peca
        if self.ganhou():
            print("GANHOU!!!")
        #print(len(xoj))

matriz_casas = []

for m in range(2):
    linha = html.TR()
    campo <= linha
    for n in range(8):
        coluna = html.TD(xo.pop())
        linha <= coluna
for m in range(4):
    linha = html.TR()
    campo <= linha
    for n in range(4):
        coluna = Casa(branco.pop())
        matriz_casas.append(coluna)
        #matriz_casas += [coluna]
        linha <= coluna.e_casa