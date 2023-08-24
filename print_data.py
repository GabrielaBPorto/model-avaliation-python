import json
import os

def imprimir_resultados(dados):
    for size, info in dados.items():
        print(f"Size: {size}")
        thresholds = info["threshold_range"]
        valores = info["values"]
        
        print("Thresholds:")
        for threshold in thresholds:
            details = valores[str(threshold)]
            tp = details["tp"]
            fp = details["fp"]
            fn = details["fn"]
            iou = details["iou"]

            print(f"  Threshold: {threshold:.2f}")
            print(f"  TP: {tp}, FP: {fp}, FN: {fn}, IoU: {iou}%\n")

def main():
    caminho_dos_arquivos = os.path.join(os.getcwd(), "temp")
    caminho_do_resultado = os.path.join(caminho_dos_arquivos, "resultados_finais.txt")
    
    if not os.path.exists(caminho_do_resultado):
        print("Arquivo de resultados finais não encontrado!")
        return
    
    with open(caminho_do_resultado, 'r') as arquivo:
        dados = json.load(arquivo)
        imprimir_resultados(dados)

if __name__ == "__main__":
    main()
