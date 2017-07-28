#!/usr/bin/env
import luis

LUIS_ENDPOINT = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/9fcf2e84-fef8-46e1-b4ee-992cd024c888?subscription-key=94c91f8f3a0d46d6bb516227bd208728&verbose=true&timezoneOffset=0&q="

LUIS = luis.Luis(url=LUIS_ENDPOINT)


class Main(object):
    """Baseado na pergunta do usuário, mostra a resposta mais adequada"""

    ANSWERS = {
        "BEST_LANGUAGE": "Sem sombra de dúvidas, a melhor linguagem de programação é Python.",
        "WORST_LANGUAGE": "Não sei, mas com a mais absoluta certeza, não é Python.",
        "ABOUT_PYTHON": "Python é a melhor linguagem de programação do mundo.",
        "WELCOME": "Oi amigo! Faça sua pergunta...",
        "GOODBYE": "Tchauzinho! :)",
        "SENTIDO_VIDA": "O sentido da vida é programar em Python",
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
            question = input()
            answer = self.replies(question)
            print(answer)


if __name__ == '__main__':
    Main().start()
