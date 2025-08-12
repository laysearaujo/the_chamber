"""
Configuração para integração com Google Sheets - Versão 2
"""

# Configurações do Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1iEZZ6iUJqmyp8FDGZXw4nX_Q_1XQJWFmH1q3S0LenOg'  # ID da planilha da versão 2
RANGE_NAME = 'A1'  # Range onde os dados serão inseridos (sem nome da aba)

# Instruções para configuração:
# 1. Vá para https://console.developers.google.com/
# 2. Crie um novo projeto ou selecione um existente
# 3. Ative a Google Sheets API
# 4. Crie credenciais de conta de serviço
# 5. Baixe o arquivo JSON das credenciais
# 6. Coloque o arquivo na mesma pasta deste projeto
# 7. Atualize o nome do arquivo abaixo
CREDENTIALS_FILE = 'credentials.json'  # Nome do arquivo de credenciais baixado 