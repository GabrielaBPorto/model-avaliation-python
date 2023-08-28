import subprocess
import shutil
import os

def run_script(script_name, arguments=[]):
    command = ["python3", script_name] + arguments
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode != 0:
        print(f"Erro ao executar {script_name}: {result.stderr.decode()}")
    else:
        print(f"Resultado de {script_name}:\n{result.stdout.decode()}")

def clean_temp_files(temp_folder):
    if os.path.exists(temp_folder):
        shutil.rmtree(temp_folder)
        print(f"Pasta temporária {temp_folder} removida.")
    else:
        print(f"Pasta temporária {temp_folder} não encontrada.")

def main():
    caminho_atual = os.getcwd()
    pasta_temporaria = os.path.join(caminho_atual, "temp")

    run_script("data_cleaning.py")

    run_script("metrics_calculator.py")

    clean_temp_files(pasta_temporaria)

if __name__ == "__main__":
    main()
