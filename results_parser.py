
import json
from rich.console import Console
from rich.table import Table

class ResultParser:
    def __init__(self, resultados):
        self.resultados = resultados
    
    def exportar_html(self, archivo_salida):
        with open("html_template.html", 'r', encoding='utf-8') as file:
            html = file.read()

        elemento_html = ""

        for i, resultado in enumerate(self.resultados, start=1):
            elemento = f"""
            <div class="result">
                <h2>{resultado['title']}</h2>
                <a href="{resultado['link']}">{resultado['link']}</a>
                <p>{resultado['snippet']}</p>
            </div>
            """
            elemento_html += elemento
        
        html = html.replace("{{ resultados }}", elemento_html)
                
        with open(archivo_salida, 'w', encoding='utf-8') as file:
            file.write(html)

        print(f"Archivo {archivo_salida} exportado correctamente")

    def exportar_json(self, archivo_salida):
        with open(archivo_salida, 'w', encoding='utf-8') as file:
            json.dump(self.resultados, file, indent=4, ensure_ascii=False)

        print(f"Archivo {archivo_salida} exportado correctamente")

    def mostrar_pantalla(self):
        console = Console()

        table = Table(show_header=True, header_style="bold green")
        table.add_column("#", style="dim", width=5)
        table.add_column("Titulo", width=50)
        table.add_column("Link", width=50)
        table.add_column("Snippet", width=50)

        for i, resultado in enumerate(self.resultados, start=1):
            table.add_row(str(i), resultado["title"], resultado["link"], resultado["snippet"])
            table.add_row("", "", "", "")

        console.print(table)


    def exportar_txt(self, archivo_salida):
        with open(archivo_salida, 'w', encoding='utf-8') as file:
            for i, resultado in enumerate(self.resultados, start=1):
                file.write(f"{i}. {resultado['title']}\n")
                file.write(f"{resultado['link']}\n")
                file.write(f"{resultado['snippet']}\n\n")

        print(f"Archivo {archivo_salida} exportado correctamente")



    


