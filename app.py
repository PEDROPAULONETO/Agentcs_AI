import subprocess
import sys
import os

if __name__ == "__main__":
    print("Iniciando o AutoGen Studio na porta 8080...")
    
    # Obtém o caminho do executável do autogenstudio no mesmo diretório do python (ambiente virtual)
    autogenstudio_exe = os.path.join(os.path.dirname(sys.executable), "autogenstudio.exe")
    
    # Se o executável não existir (por exemplo, se o script não for rodado do venv), 
    # tenta rodar usando o comando 'autogenstudio' disponível no PATH
    if not os.path.exists(autogenstudio_exe):
        autogenstudio_exe = "autogenstudio"
        
    try:
        # Executa o comando: autogenstudio ui --port 8080
        subprocess.run([autogenstudio_exe, "ui", "--port", "8080"], check=True)
    except FileNotFoundError:
        print("Erro: O comando 'autogenstudio' não foi encontrado.")
        print("Certifique-se de que o ambiente virtual está ativado e o autogenstudio instalado.")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o AutoGen Studio: {e}")