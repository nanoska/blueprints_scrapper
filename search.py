# Importo librerias
from google_search import GoogleSearch
from results_parser import ResultParser
from file_downloader import FileDownloader
import os
from dotenv import load_dotenv, set_key
import argparse
import sys


def env_config():
    """
    Configurar el archivo .env con los valores proporcionados por el usuario
    """
    api_key = input("Introduce tu API Key de Google: ")
    search_engine_id = input("Introduce tu Search Engine ID de Google: ")
    set_key(".env", "GOOGLE_API_KEY", api_key)
    set_key(".env", "GOOGLE_SEARCH_ENGINE_ID", search_engine_id)
    print("Archivo .env configurado correctamente")


def main(query, configure_env, lang, init_page, pages,
         output_json, output_html, output_txt,
         download):
    env_exists = os.path.exists(".env")
    if not env_exists or configure_env:
        env_config()
        print("Archivo .env configurado correctamente")
        sys.exit(1)

    load_dotenv()

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", None)
    GOOGLE_SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID", None)

    if not GOOGLE_API_KEY or not GOOGLE_SEARCH_ENGINE_ID:
        print("Error: Debes configurar el archivo .env")
        sys.exit(1)

    if not query:
        print("Error: Debes introducir una query")
        sys.exit(1)

    lang = "lang_es"
    init_page = 1
    querys = [
        'intitle:"index of" (blueprints OR "technical drawings") ext:pdf OR ext:dwg OR ext:doc',
        '"blueprint" OR "invention design" ext:pdf OR ext:dwg',
        'intitle:"index of" "database" ext:sql OR ext:db OR ext:csv',
        'filetype:sql OR filetype:csv OR filetype:db inurl:"/backup/" OR inurl:"/db/"',
        'filetype:pdf "invention" OR "patent" OR "technical drawings"',
        'filetype:pdf ("blueprint" OR "patent" OR "invention")',
        'intitle:"index of" "documentary" ext:mp4 OR ext:avi OR ext:mkv OR ext:mov',
        'intitle:"index of" "documentary" OR "documentaries" (ext:mp4 OR ext:avi OR ext:mkv OR ext:mov)',
        'intitle:"index of" "ebooks" OR "books" ext:pdf OR ext:epub OR ext:mobi',
        'filetype:pdf "inventions" OR "design" OR "technical manual"',
        'intitle:"index of" "ftp" (blueprints OR inventions OR databases) ext:sql OR ext:pdf OR ext:db'
    ]

    query = 'colectores solares ext:pdf'
    gsearch = GoogleSearch(GOOGLE_API_KEY, GOOGLE_SEARCH_ENGINE_ID)
    resultados = gsearch.search(query, lang, init_page, pages)

    parser = ResultParser(resultados)

    parser.mostrar_pantalla()

    if output_json:
        parser.exportar_json(output_json)
    
    if output_html:
        parser.exportar_html(output_html)

    if output_txt:
        parser.exportar_txt(output_txt)

    if download:
        file_types = download.split(",")
        urls = [resultado["link"] for resultado in resultados]

        downloader = FileDownloader("Descargas")
        downloader.filtrar_descargar_archivos(urls, file_types)

if __name__ == "__main__":

    #Configuracion de los argumentos del programa
    parser = argparse.ArgumentParser(description='Busca en Google')
    parser.add_argument('-q', '--query', type=str, help='Query a buscar', required=True)
    parser.add_argument('-c', '--config', action='store_true', help='Configuracion de la API Key y el Search Engine ID')
    parser.add_argument('-l', '--lang', type=str, help='Lenguaje de busqueda', required=False)
    parser.add_argument('-i', '--init-page', type=int, help='Pagina de inicio', required=False)
    parser.add_argument('-p', '--pages', type=int, help='Numero de paginas a buscar', required=False)

    parser.add_argument('--json', type=str, help='Exportar a JSON')
    parser.add_argument('--html', type=str, help='Exportar a HTML')
    parser.add_argument('--txt', type=str, help='Exportar a TXT')
    parser.add_argument('-d', '--download', type=str, help='Descargar archivos')
    #Parseo de los argumentos
   
    args = parser.parse_args()
    print(args)

    main(query=args.query,
         configure_env=args.config,
         lang=args.lang,
         init_page=args.init_page,
         pages=args.pages,
         output_json=args.json,
         output_html=args.html,
         output_txt=args.txt,
         download=args.download)    