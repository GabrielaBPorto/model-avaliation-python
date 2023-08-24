import os


tamanhos = [512, 608, 800]

caminho_atual = os.getcwd()

for tamanho in tamanhos:
    caminho_do_arquivo = os.path.join(caminho_atual + '/'+ str(tamanho) + '_yolov4_5000_dados_celulas.txt')
    
    with open(caminho_do_arquivo, 'r') as arquivo:
        for linha in arquivo:
            print(linha)
