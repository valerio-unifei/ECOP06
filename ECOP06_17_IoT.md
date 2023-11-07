![image](https://github.com/valerio-unifei/ECOP06/assets/56478031/772f8634-6335-4bab-80fd-6253dddf2a2c)# LoRa
A plataforma sem fio de longo alcance e baixo consumo de energia é a escolha tecnológica predominante para a 
construção de redes IoT em todo o mundo.

<img src="https://tekzitel.com/wp-content/uploads/2020/04/lorawan_schema_resize.png" />

As aplicações inteligentes de IoT melhoraram a forma como interagimos e estão a dar resposta a alguns dos maiores desafios 
enfrentados pelas cidades e comunidades: alterações climáticas, controlo da poluição, alerta precoce de catástrofes naturais 
e salvamento de vidas. As empresas também estão a beneficiar, através de melhorias nas operações e eficiência, bem como da redução de custos.

Esta tecnologia de RF sem fio está sendo integrada em carros, iluminação pública, equipamentos de fabricação, eletrodomésticos, 
dispositivos vestíveis – qualquer coisa, na verdade. A tecnologia LoRa® está tornando o nosso mundo um Planeta Inteligente.

<img src="https://www.mokosmart.com/wp-content/uploads/2020/01/lorawan-technology02.jpg" />

## Protocolo LoRaWAN

Passo a passo do desenvolvimento de uma aplicação LoRaWAN:
 1. Baixe o repositório LMIC-node do GitHub (https://github.com/lnlp/LMIC-node).
 2. Abra o Visual Studio Code com a extensão PlatformIO instalada.
 3. Importe o projeto LMIC-node no PlatformIO.
 4. Edite o arquivo platformio.ini e configure as seguintes opções:
```ini
default_envs = heltec_wifi_lora_32_v2
build_flags = -D ABP_ACTIVATION
build_flags = -D CFG_au915=1
```
 5. Edite o arquivo src/LMIC-node.cpp e ajuste a configuração da sub-banda:
  - No trecho "#elif defined(CFG_us915) || defined(CFG_au915)", altere o valor de LMIC_selectSubBand de 1 para 0.
 6. Acesse o site do The Things Network (TTN) (https://www.thethingsnetwork.org/) e crie uma conta.
 7. Acesse o cluster Australiano do TTN (https://au1.cloud.thethings.network/console).
 8. Crie uma nova aplicação no TTN.
 9. Crie um novo dispositivo (End Device) para a aplicação, selecione a frequência Australiana e escolha o modo de autenticação ABP.
 10. Gere aleatoriamente as chaves necessárias e salve o dispositivo.
 11. Copie as chaves (DevAddr, NwkSKey e AppSKey) do TTN para o arquivo de firmware do PlatformIO (keyfiles/lorawan-keys.h).
 5. Edite o arquivo keyfiles/lorawan-keys.h e preencha as seguintes informações:
```c
#define ABP_DEVADDR
#define ABP_NWKSKEY
#define ABP_APPSKEY
```

## Message Queuing Telemetry Transport (MQTT)

É um protocolo de comunicação máquina para máquina (M2M - Machine to Machine) com 
foco em Internet of Things (IoT) que funciona em cima do protocolo TCP/IP. 

Usa sistema cliente/servidor:
- Cliente: publish (publicação) ou subscriber (inscrição)
- Servidor: Broker MQTT
- Informação organizada em Tópicos (Topic) </br>
<img src="https://hackernoon.com/hn-images/1*-GHFC93E4ODwNc98IE5_vA.gif"/>

## Atividade 1
### Biblioteca Python

Instalação:
```console
pip install paho-mqtt
```
[Documentação on-line](https://github.com/eclipse/paho.mqtt.python/tree/master/examples)

### Proposta

1. Monte um cliente para publicação (publish)
2. Crie uma carga de dados (payload) em JSON com:
   - o carimbo de tempo (timestamp) do computador cliente
   - seu número de matrícula
   - IP do computador
3. Publique no tópico (Topic) "ECOP06-ECA-2022"
4. Use QOS mais seguro
5. Repita a publicação a cada 30 segundos exatos

## WebHook

Um webhook em IoT (Internet of Things) é uma técnica de comunicação que permite que 
dispositivos IoT enviem dados para serviços ou aplicativos na web de forma assíncrona. 
Um webhook é um endpoint (ponto de extremidade) da web que fica à espera de receber 
informações de dispositivos IoT quando eventos específicos ocorrem.

A ideia principal é que um dispositivo IoT seja configurado para enviar informações, 
como dados de sensores, status ou eventos, para um URL específico na web sempre que 
ocorra algo de interesse. Isso pode incluir a detecção de um movimento, uma alteração 
na temperatura, um evento de segurança, ou qualquer outro evento relevante para a 
aplicação do IoT.

O processo geralmente envolve os seguintes passos:
1. **Configuração**: O dispositivo IoT é configurado para enviar dados para um URL (o webhook) 
especificado, geralmente fornecido pelo serviço ou aplicativo que deseja receber os dados.
2. **Evento**: Quando um evento ocorre no dispositivo IoT, como uma leitura de sensor, o 
dispositivo envia automaticamente os dados para o webhook.
3. **Processamento**: O serviço ou aplicativo no webhook processa os dados recebidos, 
toma ações apropriadas com base nesses dados e pode até mesmo gerar notificações ou acionar outros dispositivos ou sistemas.

Essa abordagem é útil para integrar dispositivos IoT com serviços na web, como 
painéis de controle, sistemas de gerenciamento ou aplicativos de monitoramento. 
Permite que os dispositivos IoT forneçam informações em tempo real, tornando mais 
fácil a tomada de decisões ou a automação de tarefas com base nos eventos registrados 
pelos dispositivos. Além disso, os webhooks podem ser configurados para garantir a 
segurança dos dados e a autenticação, protegendo a integridade das informações transmitidas.

## Atividade 2

Para criar um webhook em Python usando o framework Flask, você pode seguir os seguintes passos:

1. Instale o Flask (se ainda não estiver instalado) usando o pip:
```console
pip install Flask
```

2. Crie um arquivo Python para o seu aplicativo Flask. Por exemplo, vamos chamá-lo de `app.py`.

3. Importe o Flask e crie uma instância do aplicativo:
```python
from flask import Flask

app = Flask(__name__)
```

4. Crie uma rota (endpoint) que receberá as solicitações do webhook. Você pode usar o decorador `@app.route` para definir a rota. Por exemplo:
```python
@app.route('/webhook', methods=['POST'])
def webhook():
    # Aqui você pode processar os dados recebidos do webhook
    # e executar ações com base nesses dados.
    
    # Por exemplo, você pode acessar os dados POST assim:
    data = request.get_json()
    
    # Faça algo com os dados, como imprimir no console
    print(data)
    
    # Retorne uma resposta para o webhook, se necessário
    return "Webhook recebido com sucesso!", 200
```

5. Inicie o aplicativo Flask:
```python
if __name__ == '__main__':
    app.run(debug=True)
```

Este código cria um aplicativo Flask com uma rota '/webhook' que aceita solicitações POST. Quando o webhook receber uma solicitação, ele processará os dados e retornará uma resposta.

### Proposta

Com o envio de dados pelo webhook, mostre uma caixa de texto recebendo a informação do webhook e um gráfico para exibir esses dados em tempo real.


