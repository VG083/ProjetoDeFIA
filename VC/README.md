# Projeto

O projeto propõe criar um sistema de controle para o cursor do mouse sem a necessidade de um mouse ou touchpad tradicional, utilizando apenas movimentos das mãos capturados por uma câmera. Este sistema é particularmente útil em situações onde a interação física com dispositivos de entrada não é prática ou possível.

# Resumo

## Bibliotecas necessárias

O projeto roda utilizando a versão 3.12.3 do Python porém é preciso ter as seguintes bibliotecas instaladas

pip install mediapipe
pip install pyautogui
pip install screeninfo
pip install psutil

## Rodando o projeto

O programa começa importando as bibliotecas necessárias: "cv2" para captura de vídeo e manipulação de imagens, "mediapipe" para detecção e rastreamento das mãos, "pyautogui" para controlar o cursor do mouse e realizar cliques, "screeninfo" para obter informações sobre os monitores conectados, e "psutil" para monitorar o uso de memória do programa.

Funções específicas são definidas para verificar se os dedos estão estendidos. Essas funções incluem is_thumb_extended, is_index_finger_extended, is_middle_finger_extended, is_ring_finger_extended e is_pinky_finger_extended, cada uma responsável por determinar se um dedo específico está estendido com base nos pontos de referência da mão detectada.

A configuração inicial inicia a captura de vídeo da webcam e utiliza o modelo de detecção de mãos do mediapipe para detectar no máximo uma mão por frame. Além disso as dimensões do monitor principal são obtidas para definir a área de controle do mouse na tela.

No loop principal, os frames do vídeo são capturados e a imagem é invertida para espelhar a perspectiva. A imagem é então convertida para RGB e processada pelo modelo de detecção de mãos. Um retângulo central é desenhado na tela para delimitar a área de controle do mouse, e o uso de memória atual é exibido na tela. Se uma mão for detectada, os pontos de referência são desenhados, e é verificado se os dedos estão estendidos. A posição do dedo indicador dentro do retângulo é mapeada para mover o cursor na tela. E se o dedo indicador e o mínimo estiverem estendidos dentro da área do retângulo, um clique é realizado com um intervalo mínimo de 1 segundo entre cliques. 

Para encerrar a captura de vídeo e fechar o programa basta pressionar a tecla "q".