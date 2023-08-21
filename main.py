from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty

#Classes de gerenciamento de tela:

class JanelaGerenciadora(ScreenManager):
    pass


class Inicio(Screen):
    pass


class Entrar(Screen):
    pass


class Criar(Screen):
    pass


class Sconta(Screen):
    pass


class Esqueceu_senha(Screen):
    pass


class Navegar(Screen):
    pass


class Anunciar(Screen):
    pass


class Anunciando(Screen):
    pass


class Anuncio(Screen):
    pass

#Classe princiapl do App (Serve para chamar o conteúdo kivy e também contem as funções globais):
class MyApp(MDApp):
    icone = StringProperty('cat')

    def build(self):
        return Builder.load_file('app.kv')

    #Função para montrar a categoria selecionada na tela "anunciar" que será exibida na tela "anunciando".
    def nicone(self, aicone):
        self.icone = aicone
        self.root.current = 'anunciando'


MyApp().run()
