#!/usr/bin/env python3
"""
Script de teste para verificar a integração com Google Sheets - Versão 2
"""

import os
import sys

def test_imports():
    """Testa se as dependências estão instaladas"""
    print("🔍 Testando importações...")
    
    try:
        import google.auth
        print("✅ google-auth instalado")
    except ImportError:
        print("❌ google-auth não instalado")
        return False
    
    try:
        import googleapiclient
        print("✅ google-api-python-client instalado")
    except ImportError:
        print("❌ google-api-python-client não instalado")
        return False
    
    return True

def test_config():
    """Testa se os arquivos de configuração existem"""
    print("\n🔍 Testando arquivos de configuração...")
    
    if not os.path.exists("google_sheets_config_v2.py"):
        print("❌ google_sheets_config_v2.py não encontrado")
        return False
    
    if not os.path.exists("google_sheets_manager_v2.py"):
        print("❌ google_sheets_manager_v2.py não encontrado")
        return False
    
    print("✅ Arquivos de configuração encontrados")
    return True

def test_credentials():
    """Testa se as credenciais estão configuradas"""
    print("\n🔍 Testando credenciais...")
    
    if not os.path.exists("credentials.json"):
        print("❌ credentials.json não encontrado")
        print("   Por favor, siga as instruções em SETUP_GOOGLE_SHEETS.md")
        return False
    
    print("✅ credentials.json encontrado")
    return True

def test_connection():
    """Testa a conexão com Google Sheets"""
    print("\n🔍 Testando conexão com Google Sheets...")
    
    try:
        from google_sheets_manager_v2 import GoogleSheetsManagerV2
        
        manager = GoogleSheetsManagerV2()
        
        if not manager.service:
            print("❌ Falha na autenticação")
            return False
        
        print("✅ Autenticação bem-sucedida")
        
        # Testa obter informações da planilha
        if manager.test_connection():
            print("✅ Conexão com Google Sheets estabelecida com sucesso!")
        else:
            print("❌ Falha na conexão com Google Sheets")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
        return False

def main():
    """Função principal de teste"""
    print("🧪 TESTE DE INTEGRAÇÃO COM GOOGLE SHEETS - VERSÃO 2")
    print("=" * 60)
    
    # Testa importações
    if not test_imports():
        print("\n❌ Dependências não instaladas. Execute:")
        print("   pip install -r requirements.txt")
        return False
    
    # Testa configuração
    if not test_config():
        print("\n❌ Arquivos de configuração não encontrados")
        return False
    
    # Testa credenciais
    if not test_credentials():
        return False
    
    # Testa conexão
    if not test_connection():
        print("\n❌ Falha na conexão com Google Sheets")
        print("   Verifique as instruções em SETUP_GOOGLE_SHEETS.md")
        return False
    
    print("\n🎉 TODOS OS TESTES PASSARAM!")
    print("✅ A integração com Google Sheets está funcionando corretamente")
    print("✅ Você pode executar o experimento: python the_chamber_v2.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 