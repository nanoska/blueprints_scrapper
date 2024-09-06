# Importo librerias

import requests
import os

# %%

class GoogleSearch:
    def __init__(self, api_key, engine_id):
        """
        Inicializa una nueva instancia de GoogleSearch

        Esta clase permite realizar peticiones autoatizadas a la API de Google Custom Search Engine

        Args:
            api_key (str): API Key de Google
            search_engine_id (str): ID del motor de busqueda de Google
            lang (str): Lenguaje de busqueda
            querys (list): Lista de dorks a buscar
        """
        self.api_key = api_key
        self.search_engine_id = engine_id


    def search(self, query, lang='all', init_page=1, pages=1):
        """
        Realiza una busqueda en Google

        Args:
            query (str): Query a buscar
            lang (str): Lenguaje de busqueda
            init_page (int): Pagina de inicio
            pages (int): Numero de paginas a buscar

        Returns:
            list: Lista de resultados
        """

        final_results = []
        results_per_page = 10
        google_api_url = "https://www.googleapis.com/customsearch/v1?"
        results = []

        if not pages:
            pages = 1

        for page in range(init_page, init_page + pages):
            start_index = (page - 1) * results_per_page + 1 + (page * results_per_page)
            url = f"{google_api_url}key={self.api_key}&cx={self.search_engine_id}&q={query}&start={start_index}&{lang}"
            response = requests.get(url)
            
            if response.status_code == 200:
                results = response.json().get("items", [])
                custom_results = self.custom_results(results)
                final_results.extend(custom_results)
            else:
                print(f"Error: {response.status_code}")
                break
        return final_results
    

    def custom_results(self, results):
        """
        Filtra los resultados de la busqueda

        Args:
            results (list): Lista de resultados

        Returns:
            list: Lista de resultados filtrados
        """

        custom_results = []

        for result in results:
            custom_result = {
                "title": result.get("title", ""),
                "link": result.get("link",  ""),
                "snippet": result.get("snippet", "")
            }

            custom_results.append(custom_result)

        return custom_results
    
    

    