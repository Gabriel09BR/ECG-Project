from machine import Pin, ADC, DAC, Timer
import time, math, micropython, sys

# =============================================================================
# CONFIGURAÇÃO GERAL
# -----------------------------------------------------------------------------


# DAC_PIN:     GPIO25 (ESP32 tem DAC em 25 e 26). Saída analógica 8 bits (0..255).

# ADC_PIN:     GPIO35 (apenas entrada no ESP32; bom para ADC).

# FS:          taxa de amostragem (Hz) do Timer/ISR -> determina quantas vezes
#              por segundo o laço "processa uma amostra" (ex.: lê ADC e opcionalmente
#              escreve DAC). 


# BATCH_SIZE:  quantas leituras acumulamos antes de imprimir; imprimir em lote
#              reduz overhead do USB/serial e evita travamentos.
# =============================================================================

USE_DAC = False
DAC_PIN = 25
ADC_PIN = 35
FS = 4000
BATCH_SIZE = 1000
# =============================================================================

# Contador de eventos pendentes de processamento (produzidos pela ISR e
# consumidos no laço principal). Mantemos no "user land" para evitar
# trabalho pesado dentro da interrupção.
pending = 0


# _inc será chamado fora do contexto de interrupção (via micropython.schedule),
# apenas incrementando 'pending'. O parâmetro não é usado (por convenção, "_").
def _inc(_):
    global pending
    pending += 1


# Buffer de exceção de emergência para permitir tracebacks dentro de ISR,
# evitando "MemoryError" críticos quando algo dá errado em interrupções.
micropython.alloc_emergency_exception_buf(100)

# PERIFÉRICOS
# -----------------------------------------------------------------------------
# Configura ADC no pino definido. Atenuação 11 dB amplia o range ~0–3.3 V
# (na prática ~3.6V máx. medido, mas segure-se em 3.3V para segurança).
adc = ADC(Pin(ADC_PIN))
adc.atten(ADC.ATTN_11DB)



    
    
# _isr é a função de interrupção do Timer. 
def _isr(t):
    try:
        micropython.schedule(_inc, 0)   
    except:
      
        pass

# -----------------------------------------------------------------------------
# TIMER PERIÓDICO
# -----------------------------------------------------------------------------
# Timer(1) é um dos timers de hardware do ESP32. Aqui disparamos a ISR em FS Hz.

tim = Timer(1)
tim.init(freq=FS, mode=Timer.PERIODIC, callback=_isr)

# -----------------------------------------------------------------------------
# PIPELINE DE SAÍDA
# -----------------------------------------------------------------------------
# 'buf' acumula leituras convertidas para string
#'last_hb' faz um "heartbeat" periódico para indicar que o firmware está vivo mesmo sem dados.

buf = []
last_hb = time.ticks_ms()


print("adc12")  # header

# =============================================================================
# LOOP PRINCIPAL
# =============================================================================
while True:
    # HEARTBEAT a cada 500 ms: envia uma linha iniciada por '#'
    # Bom para depurar latência USB/plot: não mistura com dados (apenas log).
    if time.ticks_diff(time.ticks_ms(), last_hb) >= 500:
        sys.stdout.write("#\n")
        last_hb = time.ticks_ms()

    did = False  # marca se processamos ao menos uma amostra nesta iteração

    # Consumimos todos os "ticks" pendentes (cada pending ~ 1 período do timer).
    while pending > 0:
        pending -= 1
        did = True

        # Opcional: gera seno no DAC usando LUT — fora da ISR (seguro).
        if USE_DAC:
            lut_idx = (lut_idx + 1) % LUT_N
            dac.write(lut[lut_idx])       

        # Leitura do ADC (0..4095 em 12 bits). .
        v = adc.read()

        # Acumulamos em 'buf' como string para concatenar linhas rapidamente.
        
     
        # Enviar os números ao invés de string deve ser mais rápido        
        buf.append(str(v))

        # Quando atingimos BATCH_SIZE, vai tudo de uma vez:
        if len(buf) >= BATCH_SIZE:
            # join + newline no final: formato "uma amostra por linha"
            sys.stdout.write("\n".join(buf) + "\n")
            buf.clear()

    # Se não houve pending (nenhuma "batida" do timer a consumir),
    # tiramos o pé do acelerador para não ocupar 100% da CPU.
    if not did:
        time.sleep_ms(5)
