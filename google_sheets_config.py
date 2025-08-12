"""
Configuração para integração com Google Sheets
"""

# Configurações do Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1PcAveY4HB4sAu-alSXaGArkqErY1Xa5J2VKZlM52xHs'  # Substitua pelo ID da sua planilha
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