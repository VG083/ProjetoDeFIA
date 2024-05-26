# Projeto

Este programa é uma aplicação de terminal que permite aos usuários criar histórias interativas. Utiliza uma API de geração de texto para gerar narrativas com base nas informações fornecidas pelo usuário. O usuário é solicitado a inserir os personagens da história, uma situação a ser tratada e detalhes adicionais, se houver.

# Resumo

## Bibliotecas necessárias

O projeto roda utilizando a versão 3.12.3 do Python porém é preciso ter as seguintes bibliotecas instaladas

pip install Pillow
pip install -q -U google-generativeai

## Rodando o projeto

O programa começa importando a biblioteca google.generativeai e configurando a chave da API necessária para acessar o modelo de geração de texto. Em seguida, define-se uma função coletar_detalhes() que permite ao usuário inserir detalhes adicionais para a história, se desejar.

A função gerar_historia() recebe os personagens, a situação e os detalhes e utiliza-os como entrada para gerar uma história usando o modelo de geração de texto configurado anteriormente.

A função main() é o ponto de entrada principal do programa. Dentro dela, o usuário é solicitado a inserir os personagens e a situação da história. Em seguida, tem a opção de fornecer detalhes adicionais. Depois de coletar todas as informações necessárias, o programa gera a história e a exibe ao usuário. O usuário também tem a opção de criar outra história ou encerrar o programa.

O programa é encerrado se o usuário pressionar Ctrl+C ou se ocorrer um erro inesperado durante a execução.

Este script oferece uma maneira simples e interativa de criar histórias personalizadas, permitindo que os usuários participem ativamente do processo de narração.