import google.generativeai as genai

API_KEY = 'AIzaSyDBkg8HcwAg0VQWmmQ9DhK0mBWdnL9d9MQ'
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

def coletar_detalhes():
    detalhes = []
    while True:
        detalhe = input(">> Digite um detalhe adicional para a história (ou pressione Enter para finalizar): ")
        if detalhe.strip() == "":
            break
        detalhes.append(detalhe)
    return detalhes

def gerar_historia(model, personagens, situacao, detalhes):
    detalhes_texto = ""
    if detalhes:
        detalhes_texto = " Aqui estão alguns detalhes adicionais que devem ser incluídos na história: " + "; ".join(detalhes) + "."

    prompt = f"""
    Escreva um conto onde os personagens são {personagens}.
    A história deve descrever a situação a seguir: {situacao}.
    {detalhes_texto}
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Erro ao gerar a história: {e}")
        return None

def main():
    while True:
        personagens = input(">> Digite os personagens da história: ")
        situacao = input(">> Digite uma situação para ser tratada na história: ")
        detalhes = coletar_detalhes()

        historia = gerar_historia(model, personagens, situacao, detalhes)
        if historia:
            print("\nHistória gerada\n")
            print(historia)

        continuar = input("\n>> Deseja criar outra história? (s/n): ").strip().lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma encerrado pelo usuário.")
    except Exception as e:
        print(f"\n\nOcorreu um erro inesperado: {e}")
