# Scripts de Análise de Dados e Cálculo de Métricas

Esse arquivo tem como objetivo explicar como realizar o uso dos scripts de maneira separada, ou junta para testes locais.

## Visão Geral dos Scripts

1. **Script de Limpeza de Dados (`data_cleaning.py`):** Este script lê os arquivos de dados brutos, formata os dados e salva os resultados limpos em um diretório especificado.

2. **Script de Cálculo de Métricas (`metrics_calculation.py`):** Este script lê os dados limpos, calcula as métricas como Verdadeiros Positivos (TP), Falsos Positivos (FP), Falsos Negativos (FN), Precisão, Recall e F1-Score, e imprime os resultados de forma amigável.

3. **Script de Controle Principal (`main_controller.py`):** Este script irá basicamente rodar data_cleaning.py && metrics_calculation.py após, e irá limpar os arquivos temporários criados por data cleaning.

## Como Usar

### 1. Limpeza de Dados
Responsável pela limpeza e formatação dos dados brutos.
Execute `data_cleaning.py` com um parâmetro opcional de caminho para especificar o local dos arquivos de dados brutos. Se nenhum caminho for fornecido, ele procurará no diretório atual.

```bash
python3 data_cleaning.py /caminho/para/dados/brutos
```

### 2. Cálculo de Métricas
Calcula métricas como precisão, revocação e F1-Score.
Execute `metrics_calculation.py` para calcular e imprimir as métricas. Certifique-se de que os dados limpos da etapa 1 estejam disponíveis ( irá buscar a pasta temporária criada no script anterior).

```bash
python3 metrics_calculation.py
```

### 3. Controlador principal

Execute `main_controller.py` para rodar o data cleaning e metrics_calculations, limpando a pasta de arquivos temporárias criada no primeiro script.

```bash
python3 main_controller.py
```

## Conclusão

Estes scripts fornecem um processo simplificado para limpar dados, calcular métricas essenciais e identificar os melhores resultados no contexto da detecção de objetos.

