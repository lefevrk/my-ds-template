import os
from pathlib import Path

def remove_license_if_needed():
    """Supprime le fichier LICENSE si l'utilisateur a choisi 'No license file'."""
    license_choice = "{{ cookiecutter.open_source_license }}"
    if license_choice == "No license file":
        if Path("LICENSE").exists():
            Path("LICENSE").unlink()

def clean_jinja_artifacts():
    """Nettoie les artefacts d'encodage Jinja dans le pyproject.toml si nécessaire."""
    # Parfois tojson ajoute des caractères unicode échappés
    toml_path = Path("pyproject.toml")
    if toml_path.exists():
        text = toml_path.read_text()
        if r"\u0027" in text:
            clean_text = text.replace(r"\u0027", "'")
            toml_path.write_text(clean_text)

if __name__ == "__main__":
    # 1. Gérer la licence
    remove_license_if_needed()
    
    # 2. Nettoyage final
    clean_jinja_artifacts()