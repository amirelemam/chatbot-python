#!/usr/bin/env
import luis

LUIS_ENDPOINT = "" # Coloque aqui a URL do seu endpoint

LUIS = luis.Luis(url=LUIS_ENDPOINT)


class Main(object):
    """Baseado na pergunta do usuário, mostra a resposta mais adequada"""

    ANSWERS = {
        "BEST_LANGUAGE": "Sem sombra de dúvidas, a melhor linguagem de programação é Python.",
        "WORST_LANGUAGE": "Não sei, mas com a mais absoluta certeza, não é Python.",
        "ABOUT_PYTHON": "Python é a melhor linguagem de programação do mundo.",
        "WELCOME": "Oi amigo! Faça sua pergunta...",
        "GOODBYE": "Tchauzinho! :)",
        "SENTIDO_VIDA": "O sentido da vida é programar em Python.",
        "None": "Desculpe, não entendi. Por favor, tente escrever de outra forma."
    }

    def replies(self, text):
        """Baseado na pergunta do usuário, identifica qual a sua intenção"""
        intent = LUIS.analyze(text).best_intent().intent
        answer = self.ANSWERS[intent]
        return answer

    def start(self):
        """Initializa o bot"""
        print("Início da interação:")

        while True:
            question = input("Usuário: ")
            answer = self.replies(question)
            print(f"Bot: {answer}")


if __name__ == '__main__':
    Main().start()
