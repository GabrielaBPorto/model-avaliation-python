# Tamanhos das imagens que voce quer ler
tamanhos = [512, 608, 800]

# Loop para passar por cada tamanho
for tamanho in tamanhos:
    # Criar o caminho do arquivo usando o tamanho
    caminho_do_arquivo = './' + str(tamanho) + '_Yolov4_5000_dados_celulas.txt'
    
    # Abrir o arquivo no modo de leitura
    with open(caminho_do_arquivo, 'r') as arquivo:
        # Ler e imprimir cada linha do arquivo
        for linha in arquivo:
            print(linha)
