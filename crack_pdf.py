import itertools
from PyPDF2 import PdfReader
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm
import os
import multiprocessing

def generate_passwords(length, characters):
    """Gera senhas de um determinado comprimento usando os caracteres fornecidos."""
    return (''.join(candidate) for candidate in itertools.product(characters, repeat=length))

def try_password(pdf_path, password):
    """Tenta abrir o PDF usando uma senha específica."""
    try:
        reader = PdfReader(pdf_path)
        if reader.decrypt(password):
            return password
    except Exception:
        pass
    return None

def brute_force_pdf_parallel(pdf_path, length):
    """Tenta força bruta paralela em um arquivo PDF."""
    characters = '0123456789'
    num_workers = multiprocessing.cpu_count()  # Usa o número máximo de núcleos disponíveis
    print(f"Usando {num_workers} núcleos para força bruta no arquivo: {pdf_path}")
    
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        print(f"Tentando senhas com {length} caracteres...")
        passwords = generate_passwords(length, characters)

        # Processa as senhas em lotes para evitar consumo excessivo de memória
        batch_size = 100
        batch = []
        futures = []
        for password in passwords:
            batch.append(password)
            if len(batch) >= batch_size:
                # Envia um lote para o executor
                futures.extend(executor.submit(try_password, pdf_path, pw) for pw in batch)
                batch.clear()

        # Finaliza o último lote
        if batch:
            futures.extend(executor.submit(try_password, pdf_path, pw) for pw in batch)
        
        # Acompanha o progresso com a barra
        for future in tqdm(futures, total=len(futures), desc=f"Senhas de {length} caracteres"):
            result = future.result()
            if result:
                return result

    return None

if __name__ == '__main__':
    # Substitua pelo caminho do seu arquivo PDF
    pdf_file = "C:/Users/eujoa/Desktop/pdfcrack/09_2024_segunda-via_01.pdf"
    max_length = 5

    while True:
        result = brute_force_pdf_parallel(pdf_file, max_length)
        if result:
            print(f"Senha encontrada: {result}")
            break
        else:
            print(f"Senha com {max_length} caracteres não encontrada.")
            resposta = input(f"Deseja tentar com {max_length + 1} caracteres? (s/n): ").strip().lower()
            if resposta == 's':
                max_length += 1
            elif resposta == 'n':
                print("Encerrando tentativa de força bruta.")
                break
            else:
                print("Resposta inválida. Por favor, digite 's' ou 'n'.")
