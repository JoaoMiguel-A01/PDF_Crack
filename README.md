Descrição do Código - Força Bruta em Arquivos PDF com Processamento Paralelo (Atenção: Este código é para fins educacionais e deve ser usado apenas com arquivos que você tem permissão legal para acessar.)
Este projeto implementa uma ferramenta de força bruta para descobrir a senha de arquivos PDF protegidos. O script utiliza processamento paralelo para maximizar a performance em máquinas com múltiplos núcleos. Ele gera combinações de senhas com base em um conjunto de caracteres especificado e testa cada uma para desbloquear o PDF. A seguir, estão os principais componentes do código:

Geração de Senhas:

A função generate_passwords utiliza a biblioteca itertools para criar combinações de senhas com base em um conjunto de caracteres e comprimento fornecidos.
Tentativa de Descriptografia:

A função try_password tenta abrir o arquivo PDF usando uma senha específica. Caso a senha esteja correta, ela é retornada.
Processamento Paralelo:

A função brute_force_pdf_parallel distribui as tentativas de senha entre múltiplos processos, utilizando o número máximo de núcleos disponíveis na máquina para acelerar o processo.
Controle de Fluxo:

O script principal (if __name__ == '__main__') inicia com a tentativa de senhas de comprimento 1 e incrementa gradualmente, dependendo da entrada do usuário, até encontrar a senha ou o usuário decidir parar.
Barra de Progresso:

Utiliza a biblioteca tqdm para exibir uma barra de progresso, informando o status das tentativas.
Execução Iterativa:

Caso a senha não seja encontrada com o comprimento atual, o script solicita ao usuário se deseja continuar tentando com um comprimento maior.
Funcionalidades
Processamento otimizado com multiprocessamento.
Flexibilidade para definir caracteres e comprimento das senhas.
Uso de barras de progresso para acompanhar o progresso das tentativas.
Mensagens interativas para melhorar a experiência do usuário.
Como Utilizar
Certifique-se de que todas as bibliotecas utilizadas estão instaladas (PyPDF2, tqdm).
Modifique a variável pdf_file para o caminho do arquivo PDF que deseja testar.
Execute o script e acompanhe as tentativas. Responda às interações para ajustar os parâmetros de execução.

