import random


# INFORMAÇÕES DO GRUPO

def mostrar_informacoes_iniciais():
    print("\n==============================")
    print("        QUIZ ARDUINO")
    print("==============================")
    print(" Matéria: Programação e Algoritmo")
    print("\n Grupo:")
    print("• Maria Eduarda Pinto de Oliveira Rodrigues")
    print("• Mariana Rasmussen Rezende Alves")
    print("• Natan Alexandro Silva Costa")
    print("• Pietro Fiorese Dopp")
    print("==============================\n")


# BANCO DE PERGUNTAS (50)

perguntas = [
    {"pergunta":"O Arduino é:",
     "alternativas":["Um cabo de energia","Uma plataforma de prototipagem eletrônica","Um sistema operacional","Um tipo de sensor","Um aplicativo móvel"],
     "correta":"B"},
     
    {"pergunta":"O país onde o Arduino foi criado é:",
     "alternativas":["Suécia","Itália","Japão","Alemanha","Estados Unidos"],
     "correta":"B"},
     
    {"pergunta":"O modelo mais popular de Arduino é o:",
     "alternativas":["Mega 2560","Pro Mini","Uno","Nano","Due"],
     "correta":"C"},
     
    {"pergunta":"O microcontrolador usado no Arduino Uno é:",
     "alternativas":["ATmega2560","ATmega328P","ESP8266","STM32","PIC16F84A"],
     "correta":"B"},
     
    {"pergunta":"A linguagem usada no Arduino IDE é baseada em:",
     "alternativas":["C/C++","C#","Python","JavaScript","HTML"],
     "correta":"A"},
     
    {"pergunta":"O pino 13 do Arduino Uno possui:",
     "alternativas":["Um buzzer interno","Um botão de reset","Um LED embutido","Uma entrada analógica","Um sensor de temperatura"],
     "correta":"C"},
     
    {"pergunta":"O Arduino pode ser alimentado por:",
     "alternativas":["Apenas USB","Somente energia solar","Pilhas, bateria ou USB","Apenas fonte de bancada","Apenas bateria de 9V"],
     "correta":"C"},
     
    {"pergunta":"O software usado para programar o Arduino chama-se:",
     "alternativas":["Arduino IDE","Eclipse","MPLAB","NetBeans","Visual Studio"],
     "correta":"A"},
     
    {"pergunta":"O Arduino Nano é:",
     "alternativas":["Menor e mais compacto que o Uno","Maior que o Arduino Mega","Igual ao Uno em tamanho","Um sensor de luz","Uma fonte de alimentação"],
     "correta":"A"},
     
    {"pergunta":"Os pinos analógicos do Arduino Uno são:",
     "alternativas":["A0 a A5","0 a 5","D0 a D5","2 a 7","A1 a A7"],
     "correta":"A"},
     
    {"pergunta":"O Arduino Uno trabalha com tensão de operação de:",
     "alternativas":["5V","3.3V","12V","9V","7V"],
     "correta":"A"},
     
    {"pergunta":"O pino GND do Arduino serve para:",
     "alternativas":["Comunicação serial","Energia positiva","Referência de terra (negativo)","Saída analógica","PWM"],
     "correta":"C"},
     
    {"pergunta":"O símbolo “~” nos pinos digitais indica:",
     "alternativas":["Pino de interrupção","Pino PWM","Pino analógico","Pino de reset","Pino de entrada"],
     "correta":"B"},
     
    {"pergunta":"O comando que configura um pino como saída é:",
     "alternativas":["attach()","pinMode()","digitalWrite()","digitalRead()","delay()"],
     "correta":"B"},
     
    {"pergunta":"Para acender um LED no pino 13, usa-se:",
     "alternativas":["digitalWrite(13, HIGH)","digitalRead(13, HIGH)","analogWrite(13, 255)","pinMode(13, HIGH)","digitalRead(13, LOW)"],
     "correta":"A"},
     
    {"pergunta":"O comando que pausa o programa por um tempo é:",
     "alternativas":["sleep()","wait()","pause()","delay()","stop()"],
     "correta":"D"},
     
    {"pergunta":"A função setup() é executada:",
     "alternativas":["Somente uma vez ao iniciar","Quando o botão reset é pressionado","A cada ciclo do programa","A cada 10 segundos","Sempre que o loop reinicia"],
     "correta":"A"},
     
    {"pergunta":"A função loop() é usada para:",
     "alternativas":["Encerrar o programa","Repetir continuamente as instruções","Ligar o LED embutido","Criar variáveis","Reiniciar o setup"],
     "correta":"B"},
     
    {"pergunta":"O comando Serial.begin(9600) serve para:",
     "alternativas":["Iniciar o monitor serial","Configurar um pino","Criar uma variável","Iniciar o loop","Iniciar o I2C"],
     "correta":"A"},
     
    {"pergunta":"A unidade de medida da resistência usada nos circuitos Arduino é:",
     "alternativas":["Ampère","Ohm","Volt","Hertz","Watt"],
     "correta":"B"},
     
    {"pergunta":"O sensor LDR detecta:",
     "alternativas":["Luz","Temperatura","Umidade","Som","Pressão"],
     "correta":"A"},
     
    {"pergunta":"O sensor DHT11 mede:",
     "alternativas":["Temperatura e umidade","Som e vibração","Pressão e altitude","Corrente elétrica","Velocidade do vento"],
     "correta":"A"},
     
    {"pergunta":"O módulo HC-SR04 é utilizado para medir:",
     "alternativas":["Distância","Corrente","Luz","Temperatura","Umidade"],
     "correta":"A"},
     
    {"pergunta":"O comando analogRead(A0) retorna:",
     "alternativas":["Um valor entre 0 e 1023","Um valor entre 0 e 255","Um valor entre 0 e 10","Um valor entre 0 e 100","Um valor entre 0 e 4095"],
     "correta":"A"},
     
    {"pergunta":"O comando analogWrite() gera:",
     "alternativas":["Um sinal digital","Um sinal PWM","Um valor analógico puro","Um sinal de ruído","Um sinal serial"],
     "correta":"B"},
     
    {"pergunta":"A biblioteca Servo.h é usada para:",
     "alternativas":["Servomotores","Displays LCD","Motores de passo","Sensores de luz","LEDs endereçáveis"],
     "correta":"A"},
     
    {"pergunta":"O comando digitalRead() serve para:",
     "alternativas":["Ler o estado de um pino","Escrever em um pino","Enviar dados pela serial","Ligar o LED","Calibrar sensores"],
     "correta":"A"},
     
    {"pergunta":"O comando map() serve para:",
     "alternativas":["Converter intervalos de valores","Alterar portas de comunicação","Enviar dados via Bluetooth","Conectar sensores","Ligar motores"],
     "correta":"A"},
     
    {"pergunta":"O módulo Bluetooth mais comum usado com Arduino é o:",
     "alternativas":["HC-05","ESP32","DHT11","ESP01","L298N"],
     "correta":"A"},
     
    {"pergunta":"A função Serial.print() é usada para:",
     "alternativas":["Imprimir dados no monitor serial","Controlar motores","Criar variáveis","Apagar a tela do monitor serial","Salvar dados em memória"],
     "correta":"A"},
     
    {"pergunta":"O comando delay(1000) faz o Arduino:",
     "alternativas":["Esperar 1 segundo","Esperar 10 segundos","Esperar 0,1 segundo","Esperar 100 segundos","Esperar 5 segundos"],
     "correta":"A"},
     
    {"pergunta":"O pino VIN é utilizado para:",
     "alternativas":["Alimentar o Arduino externamente","Entrada analógica","Comunicação serial","Controle PWM","Saída de 3.3V"],
     "correta":"A"},
     
    {"pergunta":"O Arduino Mega possui:",
     "alternativas":["54 pinos digitais","30 pinos digitais","14 pinos digitais","10 pinos digitais","8 pinos analógicos"],
     "correta":"A"},
     
    {"pergunta":"O Arduino pode se comunicar com outros dispositivos por:",
     "alternativas":["USB, Bluetooth, I2C e Serial","Apenas USB","Apenas SPI","Apenas Wi-Fi","Apenas Ethernet"],
     "correta":"A"},
     
    {"pergunta":"O comando Serial.available() verifica:",
     "alternativas":["Quantos bytes estão disponíveis na comunicação serial","Se o Arduino está ligado","Se há sensores conectados","O tempo de execução","Se o loop terminou"],
     "correta":"A"},
     
    {"pergunta":"O comando millis() retorna:",
     "alternativas":["O tempo em milissegundos desde o início do programa","A tensão atual","A quantidade de pinos","O número de loops","O consumo energético"],
     "correta":"A"},
     
    {"pergunta":"A biblioteca LiquidCrystal.h controla:",
     "alternativas":["Displays LCD","Relés","Motores","LEDs RGB","Bluetooth"],
     "correta":"A"},
     
    {"pergunta":"O módulo L298N é usado para:",
     "alternativas":["Controlar motores DC","Medir temperatura","Acender LEDs","Ler sensores analógicos","Comunicar via SPI"],
     "correta":"A"},
     
    {"pergunta":"O sensor PIR detecta:",
     "alternativas":["Movimento","Som","Luz","Vibração","Calor intenso"],
     "correta":"A"},
     
    {"pergunta":"O sensor ultrassônico HC-SR04 utiliza:",
     "alternativas":["Ondas sonoras","Raios infravermelhos","Luz visível","Corrente elétrica","Ondas de rádio"],
     "correta":"A"},
     
    {"pergunta":"O Arduino Due trabalha com tensão lógica de:",
     "alternativas":["3.3V","12V","5V","9V","1.8V"],
     "correta":"A"},
     
    {"pergunta":"O Arduino Leonardo pode funcionar como:",
     "alternativas":["Mouse ou teclado USB","Sensor de temperatura","Placa Wi-Fi","Alto-falante","Conversor analógico"],
     "correta":"A"},
     
    {"pergunta":"O protocolo I2C utiliza:",
     "alternativas":["2 fios (SDA e SCL)","1 fio","3 fios","5 fios","4 fios"],
     "correta":"A"},
     
    {"pergunta":"O comando Wire.begin() inicializa:",
     "alternativas":["Comunicação I2C","Comunicação serial","Comunicação SPI","Comunicação Bluetooth","Comunicação USB"],
     "correta":"A"},
     
    {"pergunta":"O Arduino pode ser integrado à Internet com:",
     "alternativas":["Módulo Ethernet ou Wi-Fi","Apenas cabo serial","Somente USB","Apenas Bluetooth","Somente rádio de longo alcance"],
     "correta":"A"},
     
    {"pergunta":"O módulo ESP8266 adiciona ao Arduino a capacidade de:",
     "alternativas":["Conexão Wi-Fi","Controle de motor","Medição de corrente","Gravar áudio","Comunicação serial"],
     "correta":"A"},
     
    {"pergunta":"O comando SPI.begin() é usado para:",
     "alternativas":["Iniciar comunicação SPI","Iniciar comunicação serial","Iniciar Wi-Fi","Iniciar Bluetooth","Ligar o LED"],
     "correta":"A"},
     
    {"pergunta":"O módulo RTC DS3231 é usado para:",
     "alternativas":["Registrar hora e data","Medir luz","Controlar motores","Medir vibração","Calcular distância"],
     "correta":"A"},
     
    {"pergunta":"O Arduino pode armazenar dados permanentes em:",
     "alternativas":["EEPROM","RAM","Flash","Buffer","Registradores"],
     "correta":"A"},
     
    {"pergunta":"O Arduino pode ser usado em projetos de:",
     "alternativas":["Internet das Coisas (IoT)","Somente automóveis","Somente drones","Apenas iluminação","Apenas motores industriais"],
     "correta":"A"},
]


# FUNÇÕES DO PROGRAMA


def mostrar_menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Responder Quiz")
    print("2 - Exibir Regras")
    print("3 - Encerrar Programa")

def mostrar_regras():
    print("\n===== REGRAS DO QUIZ =====")
    print("• 20 perguntas sorteadas das 50 disponíveis.")
    print("• Cada questão vale 1 ponto.")
    print("• Nota máxima: 20 pontos.")
    print("• Alternativas são embaralhadas a cada execução.")
    print("• Digite A, B, C, D ou E.\n")

def sortear_questoes():
    return random.sample(perguntas, 20)

def exibir_questao(q, numero):
    print(f"\nQuestão {numero}: {q['pergunta']}")
    # Embaralhara alternativas
    alternativas = list(q['alternativas'])
    random.shuffle(alternativas)
    
    # Salvar mapa de letras para verificar resposta

    letra_corretas = {letra: alt for letra, alt in zip("ABCDE", alternativas)}
    for letra, alt in letra_corretas.items():
        print(f"{letra}) {alt}")
    # Retorna o mapa para validação
    return letra_corretas

def verificar_resposta(q, mapa):
    # Descobre qual letra atual corresponde à resposta correta
    correta_texto = q['alternativas'][ord(q['correta'])-65]
    correta_letra = [k for k, v in mapa.items() if v == correta_texto][0]
    while True:
        resposta = input("Sua resposta: ").strip().upper()
        if resposta not in ["A","B","C","D","E"]:
            print("Digite uma alternativa válida (A–E).")
        else:
            return resposta == correta_letra

def exibir_resultado(acertos):
    nota = acertos
    print("\n_____ RESULTADO FINAL _____")
    print(f"Acertos: {acertos}/20")
    print(f"Nota final: {nota:.1f} / 20.0")
    print("_____________________________\n")

def iniciar_quiz():
    questoes = sortear_questoes()
    acertos = 0
    for i, q in enumerate(questoes, start=1):
        mapa = exibir_questao(q, i)
        if verificar_resposta(q, mapa):
            acertos += 1
    exibir_resultado(acertos)

# PROGRAMA PRINCIPAL

def main():
    mostrar_informacoes_iniciais()
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if opcao=="1":
            iniciar_quiz()
        elif opcao=="2":
            mostrar_regras()
        elif opcao=="3":
            print("Programa encerrado. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__=="__main__":
    main()


