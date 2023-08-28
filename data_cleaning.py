import os
import argparse
import json

size_key = "size"
threshold_range_key = "threshold_range"
values_key = "values"

def leitura_por_arquivo(caminho_do_arquivo):
    linhas = []
    with open(caminho_do_arquivo, 'r') as arquivo:
        for linha in arquivo:
            if "for conf_thresh" in linha:
                linhas.append(linha)
    return linhas

def formatacao_de_dados(linhas):
    resultado = {
        threshold_range_key: [],
        values_key: {}
    }

    for linha in linhas:
        parts = linha.split(",")
        threshold_value = float(parts[0].split('=')[-1].strip())
        tp = float(parts[1].split('=')[-1].strip())
        fp = float(parts[2].split('=')[-1].strip())
        fn = float(parts[3].split('=')[-1].strip())
        iou = float(parts[4].split('=')[-1].strip().strip('%'))

        resultado[threshold_range_key].append(threshold_value)
        resultado[values_key][threshold_value] = {
            "tp": tp,
            "fp": fp,
            "fn": fn,
            "iou": iou
        }

    resultado[threshold_range_key].sort()
    return resultado

def impressao_dos_resultados_finais(resultados_finais):
    for size, dados in resultados_finais.items():
        print(f"Size: {size}")
        for threshold in dados[threshold_range_key]:
            detalhes = dados[values_key][threshold]
            tp = detalhes["tp"]
            fp = detalhes["fp"]
            fn = detalhes["fn"]
            iou = detalhes["iou"]

            print(f"  Threshold: {threshold}")
            print(f"  TP: {tp}, FP: {fp}, FN: {fn}, IoU: {iou}\n")


def salvar_resultados_finais(resultados_finais, caminho_da_saida):
    with open(caminho_da_saida, 'w') as arquivo_saida:
        json.dump(resultados_finais, arquivo_saida, indent=4)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Clean and format Yolov4 cell data.")
    parser.add_argument("--path", help="Path to the folder containing the files to be cleaned", default=".")
    return parser.parse_args()

args = parse_arguments()
caminho_dos_arquivos = os.path.abspath(args.path)

tamanhos = [512, 608, 800]
resultados_finais = {}

caminho_atual = os.getcwd()
pasta_temporaria = os.path.join(caminho_atual, "temp")
os.makedirs(pasta_temporaria, exist_ok=True)

for tamanho in tamanhos:
    caminho_do_arquivo = os.path.join(caminho_dos_arquivos, str(tamanho) + '_yolov4_5000_dados_celulas.txt')
    linhas = leitura_por_arquivo(caminho_do_arquivo)
    resultado_formatado = formatacao_de_dados(linhas)
    resultados_finais[size_key + "_" + str(tamanho)] = resultado_formatado

caminho_da_saida = os.path.join(pasta_temporaria, "resultados_finais.txt")
salvar_resultados_finais(resultados_finais, caminho_da_saida)
print(f"Resultados salvos em: {caminho_da_saida}")