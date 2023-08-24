# Scripts de Análise de Dados e Cálculo de Métricas

Este repositório contém três scripts para limpar dados, calcular métricas e analisar resultados relacionados à detecção de objetos. O processo envolve ler arquivos de dados brutos, formatar os dados, calcular métricas relevantes como precisão, recall e F1-Score e, finalmente, identificar os melhores resultados com base em certos critérios.

## Visão Geral dos Scripts

1. **Script de Limpeza de Dados (`data_cleaning.py`):** Este script lê os arquivos de dados brutos, formata os dados e salva os resultados limpos em um diretório especificado.

2. **Script de Cálculo de Métricas (`metrics_calculation.py`):** Este script lê os dados limpos, calcula as métricas como Verdadeiros Positivos (TP), Falsos Positivos (FP), Falsos Negativos (FN), Precisão, Recall e F1-Score, e imprime os resultados de forma amigável.

## Como Usar

### 1. Limpeza de Dados

Execute `data_cleaning.py` com um parâmetro opcional de caminho para especificar o local dos arquivos de dados brutos. Se nenhum caminho for fornecido, ele procurará no diretório atual.

```bash
python data_cleaning.py /caminho/para/dados/brutos
```

### 2. Cálculo de Métricas

Execute `metrics_calculation.py` para calcular e imprimir as métricas. Certifique-se de que os dados limpos da etapa 1 estejam disponíveis.

```bash
python metrics_calculation.py
```

## Utilização dos Scripts

Este projeto consiste em três scripts principais e um script de controle para limpeza de dados, cálculo de métricas e análise dos melhores resultados.

### Scripts Principais:

1. **`data_cleaning.py`**: Responsável pela limpeza e formatação dos dados brutos.
2. **`metrics_calculation.py`**: Calcula métricas como precisão, revocação e F1-Score.

### Script de Controle:

- **`main_controller.py`**: Este script executa todos os três scripts principais em ordem e, posteriormente, limpa os arquivos temporários criados.

### Execução:

Para executar o script de controle, utilize o seguinte comando:

```bash
python main_controller.py
```

Certifique-se de ter os caminhos corretos para os scripts principais e para a pasta temporária dentro do script de controle.

### Análise dos Melhores Resultados:

Os melhores resultados são determinados com base no F1-Score, que é uma medida de equilíbrio entre a precisão e a revocação. A análise é realizada no script `best_results_analysis.py`, e os detalhes completos dos melhores resultados são impressos no console.


## Compreendendo os Melhores Resultados

Os melhores resultados são identificados com base no F1-Score, uma métrica que equilibra precisão e recall. Aqui está o que esses termos significam:

- **Precisão:** A proporção de resultados positivos corretamente identificados entre os positivos identificados.

- **Recall:** A proporção de resultados positivos corretamente identificados entre todas as instâncias relevantes.

- **F1-Score:** A média harmônica da precisão e recall, calculada como `2 * (precisão * recall) / (precisão + recall)`. Ela fornece uma única pontuação que equilibra precisão e recall.

Os melhores resultados são aqueles com o F1-Score mais alto, indicando um equilíbrio mais otimizado entre precisão e recall. Isso garante que tanto os falsos positivos quanto os falsos negativos sejam minimizados, levando a uma detecção mais precisa e confiável.


### Limpeza de Arquivos Temporários:

O script de controle também cuida da limpeza dos arquivos temporários criados durante a execução dos scripts principais. Isso garante que não haja resíduos deixados no sistema após a análise.

## Conclusão

Estes scripts fornecem um processo simplificado para limpar dados, calcular métricas essenciais e identificar os melhores resultados no contexto da detecção de objetos. Ao focar no F1-Score, eles oferecem uma compreensão abrangente da eficácia da detecção, considerando tanto a precisão quanto o recall.

