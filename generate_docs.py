import os

# Lista delle app Django
apps = [
    "courses",
    "students",
    "social",
    "profiles",
    "report",
    "cal",
    "maps",
    "chat_app",
    "icdl",
    "quiz",
    "classroom",
    "tools",
    "ai",
    "games"
]

# Percorso della cartella di documentazione
docs_path = os.path.join(os.getcwd(), "docs", "apps")

# Creare la cartella apps/ se non esiste
if not os.path.exists(docs_path):
    os.makedirs(docs_path)

# Generare i file Markdown per ogni app
for app in apps:
    file_path = os.path.join(docs_path, f"{app}.md")
    
    # Contenuto predefinito per ogni file
    content = f"""# {app.capitalize()} App

## Modelli

::: {app}.models
    options:
      heading_level: 2

## Views

::: {app}.views
    options:
      heading_level: 2

## Forms 

::: {app}.forms
    options:
      heading_level: 2

## Serializers 

::: {app}.serializers
    options:
      heading_level: 2
"""

    # Scrivere il contenuto nel file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Creato: {file_path}")

print("\n✅ Tutti i file Markdown sono stati generati correttamente!")
