[Click here to see the English version](README.md)

## Chatbot em Python

Este código refere-se à palestra "Chatbot em Python", do SciPy #1 de 29/07/2017.
[Ver slides da apresentação](https://www.slideshare.net/AmirdoNascimentoElem/chatbots-em-python?utm_source=slideshow&utm_medium=ssemail&utm_campaign=post_upload_view_cta)

### Requisitos

* Python 3.6
* Conta no Microsoft LUIS
* Módulo `luis`

### Instalação

> Nota: Os seguintes comandos funcionam em Linux e macOS. Se você está usando Windows, os passos são os mesmos, porém os comandos podem ser diferentes.  

* Baixe e instale Python 2.7+ ou 3.6+ do [site oficial](https://www.python.org/downloads/).  
* Crie uma conta no serviço Microsoft LUIS, [através do site](https://www.luis.ai).  
* Baixe o projeto e extraia seu conteúdo, você deve ver uma pasta chamada `chatbot-python`.  
* No Terminal ou Prompt de Comando, acesse a pasta onde você extraiu o projeto.  
* Copie a pasta chatbot-python para sua pasta Home:  
```$ cp -R chatbot-python ~/```  
* Acesse a pasta Home:  
```$ cd ~/```  
* Instale o módulo Virtualenv para isolar o código:  
```$ pip3 install virtualenv```  
* Crie o virtual environment:   
```virtualenv chatbot-python```  
* Entre na pasta do projeto:  
```$ cd chatbot-python```  
* Ative o virtual environment:  
```$ source bin/activate```  
* Instale os módulos do Python:  
```$ pip3 install -r requirements.txt``` 

### Criando a estrutura básica

O primeiro passo é importar e inicializar os módulos necessários, além de criar a estrutura para que o código seja feito usando Programação Orientada a Objetos.  

Para isso, vamos:
* Inserir o shebang, na linha 1.
* Importar o módulo que faz a conexão com o LUIS, na linha 2.
* Armazenar a URL do enpoint numa constante, na quarta linha. [Veja como conseguir ela aqui](https://docs.microsoft.com/pt-br/azure/cognitive-services/luis/publishapp)
* Inicializar o módulo usando a constante que armazena a URL do endpoint, na linha 5.
* Apontar que o método `start()` da classe `Main()` é o método principal da classe e deve ser o chamado quando o arquivo é executado, nas linhas 7 e 8.

```
#!/usr/bin/python
import luis

LUIS_ENDPOINT = "" # Coloque aqui a URL do seu endpoint
LUIS = luis.Luis(url=LUIS_ENDPOINT")

if __name__ == '__main__':
    Main().start()
```

### Adicionando o dicionário de respostas

Agora vamos criar categorias de perguntas e suas respostas.  

Para isso, vamos criar um dicionário `ANSWERS`, que recebe como chave a categoria, chamada de intent pelo LUIS, e o valor do dicionário é a resposta.   

Este dicionário será criado localmente na classe `Main()`. Vamos criar também o método `start()`, para manter o código de acordo com a especificação de execução, feitas no passo anterior.  

O código abaixo deve ser inserido na linha 6, abaixo da inicialização do módulo `luis` na constante `LUIS`.   

```
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

    def start(self):
        """Initializa o bot"""
        pass
```

### Recebendo a mensagem do usuário

Vamos criar o código para receber a mensagem do usuário e responder de acordo.  
  
Primeiro, vamos colocar uma mensagem indicando o início da interação. (linha 3)  
Depois, a mensagem recebida pelo usuário é armazenada numa variável. (linha 6)  
Esta variável é passada como parâmetro para método `replies()` que fará a análise da mensagem e retornará a resposta. Daqui a pouco criaremos este método `replies()`. (linha 7)  
A resposta, então, é exibida para o usuário. (linha 8).  
Vamos colocar o processo de receber a mensagem e responder num loop, para que possa haver múltiplas interações.  

No método `start()`, substitua o `pass` pelo código abaixo.  

```
    def start(self):
        """Initializa o bot"""
        print("Início da interação:")

        while True:
            question = input()
            answer = self.replies(question)
            print(answer)
```

### Identificando a melhor resposta

Para responder o usuário de forma mais adequada, vamos utilizar o serviço Microsoft LUIS.  

Para isso, vamos criar o método `replies()` que, a partir de uma mensagem, consulta o LUIS, e retorna o texto da resposta mais adequada.  

Na linha 3, vamos fazer o envio da mensagem para análise, através do método `analyze()`.  
Este método retorna o atributo `best_intent()`, que retorna com dois itens, o primeiro sendo a intent com maior probabilidade de ser a correta e o segundo é a probabilidade em si.  
Vamos pegar apenas o nome da intent, através do atributo `intent` e armazenar numa variável.  

Com o nome da intent, vamos fazer a busca no dicionário ANSWERS e retornaremos a resposta, nas linhas 4 e 5.  
Mais pra frente, criaremos as intents no LUIS.  

Coloque este código dentro da classe `Main()`, logo acima do método `start()`  
```
    def replies(self, text):
        """Baseado na pergunta do usuário, identifica qual a sua intenção"""
        intent = LUIS.analyze(text).best_intent().intent
        answer = self.ANSWERS[intent]
        return answer
```

### Treinamento das intents no Microsoft LUIS

Nosso código está pronto, porém as perguntas não serão entendidas sem que o LUIS tenha sido treinado.  

Primeiro, vamos criar o app:  
* Após login no [Microsoft LUIS](https://www.luis.ai), na aba **My Apps**, clique no botão **New App**.
* Coloque o nome da aplicação, como por exemplo "Chatbot Python".
* Coloque o idioma para "Brazilian Portuguese".
* Como Enpoint key, selecione "BoostrapKey".

A explicação detalhada de como criar o app no LUIS por ser encontrada [aqui](https://docs.microsoft.com/pt-br/azure/cognitive-services/luis/create-new-app).   

Agora que temos o App criado, temos que adicionar as intents:  

* No menu lateral, clique em **intents**.
* Agora, clique no botão **Add Intent**, para adicionar uma nova intent.
* Coloque o nome da intent, de acordo com uma das chaves do nosso dicionário `ANSWERS`.
* Clique no botão **Save**.
* Faça este passo até que todas as chaves do dicionário `ANSWERS` tenham uma intent no Microsoft LUIS. A intent None é criada por padrão e não precisa ser criada novamente.  

A explicação detalhada de como criar intents no LUIS por ser encontrada [aqui](https://docs.microsoft.com/pt-br/azure/cognitive-services/luis/add-intents).   

Depois de criada, a intent precisa ser treinada:  

* Clique no nome de uma intent.
* Na caixa de input, onde está escrito **Type a new utterance & press Enter**, digite a mensagem que será categorizada naquela intent. Por exemplo, na intent WELCOME, colocamos a mensagem "oi".
* Crie um número razoável de mensagens. Quanto mais mensagens, mais preciso fica o sistema de identificação.
* Crie mensagens para todas as intents. Apesar de ser opcional fazer isso para a intent None, é recomendável que mensagens não relacionadas a nenhuma das outras intents sejam inseridas em None.  

A explicação detalhada de como adicionar mensagens numa intent do LUIS por ser encontrada [aqui](https://docs.microsoft.com/pt-br/azure/cognitive-services/luis/add-example-utterances)

Depois de criar todas as intents e inserir mensagens e todas elas, precisamos fazer o treinamento em si.  

* No menu lateral, clique em **Train & Test**.
* Clique no botão **Train Application**.
* Ao final do treinamento, é possível testar a precisão do treinamento na caixa de input **Type a test utterance & press Enter**.

A explicação detalhada de como fazer o treinamento no LUIS por ser encontrada [aqui](https://docs.microsoft.com/pt-br/azure/cognitive-services/luis/train-test)

Caso o treinamento não esteja satisfatório, coloque mais mensagens nas intents (passo anterior) e refaça o treinamento (este passo).  

Com a aplicação treinada, precisamos publicá-la para uso externo.  

* No menu lateral, clique em **Publish App**.
* Caso a **Endpoint Key** não esteja selecionada, selecione "BootstrapKey".
* Em **Endpoint slot**, selecione "Production".
* Clique no botão **Publish**.
* Será gerada a **Endpoint URL**. Copie a URL e cole no código, atribuido ela como String à constante `LUIS_ENDPOINT`

```
LUIS_ENDPOINT = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/LETRASENUMEROS?subscription-key=NUMERODASUBSCRIPTIONKEY8&timezoneOffset=0&verbose=true&q="
```

Toda vez que fizer um novo treinamento, as alterações só estarão disponíveis após fazer a publicação (este passo). A publicação tem que ser feita todas as vezes.   

A explicação detalhada de como fazer a publicação do App do LUIS por ser encontrada [aqui](https://docs.microsoft.com/pt-br/azure/cognitive-services/luis/publishapp)

### Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE)
