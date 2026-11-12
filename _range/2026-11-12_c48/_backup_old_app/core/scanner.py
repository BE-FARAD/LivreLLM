import os
import subprocess
import shutil

def scan_pdf_with_marker(pdf_path: str, output_dir: str) -> str:
    """
    Convertit un PDF en Markdown via l'outil en ligne de commande 'marker_single'.
    
    Args:
        pdf_path: Chemin absolu vers le fichier PDF source.
        output_dir: Chemin absolu vers le dossier de destination (dossier du livre).
        
    Returns:
        str: Le chemin absolu vers le fichier Markdown généré (.md).
    
    Raises:
        Exception: Si la conversion échoue ou si le fichier n'est pas trouvé.
        FileNotFoundError: Si le PDF source n'existe pas.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Fichier source introuvable : {pdf_path}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    # 1. Construction de la commande
    # Syntaxe Marker v1 : marker_single <INPUT> --output_dir <OUTPUT>
    cmd = ["marker_single", pdf_path, "--output_dir", output_dir]
    
    print(f"[Core] Lancement de Marker : {' '.join(cmd)}")

    # 2. Exécution isolée
    try:
        process = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            check=False # On gère l'erreur manuellement pour les logs
        )
    except Exception as e:
        raise Exception(f"Echec du lancement du sous-processus Marker : {e}")

    # 3. Gestion d'erreur CLI
    if process.returncode != 0:
        error_msg = process.stderr.strip()
        
        # Tentative de fallback syntaxe (si version différente)
        if "no such option" in error_msg.lower() or "unexpected extra argument" in error_msg.lower():
            print("[Core] Tentative fallback syntaxe ancienne...")
            cmd_fallback = ["marker_single", pdf_path, output_dir]
            process_fb = subprocess.run(cmd_fallback, capture_output=True, text=True)
            
            if process_fb.returncode == 0:
                # Si ça a marché, on continue
                pass
            else:
                raise Exception(f"Marker a échoué (Code {process.returncode}).\nLogs:\n{error_msg}\n{process.stdout}")
        else:
            raise Exception(f"Marker a échoué (Code {process.returncode}).\nLogs:\n{error_msg}")

    # 4. Localisation du résultat
    # Marker crée souvent un sous-dossier avec le nom du fichier
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Chemins possibles pour le fichier .md
    candidates = [
        os.path.join(output_dir, pdf_name, f"{pdf_name}.md"), # Structure standard
        os.path.join(output_dir, f"{pdf_name}.md"),           # Structure plate
    ]

    final_md_path = None
    for path in candidates:
        if os.path.exists(path):
            final_md_path = path
            break
    
    # Recherche récursive de dernier recours
    if not final_md_path:
        for root, _, files in os.walk(output_dir):
            for file in files:
                if file.endswith(".md"):
                    final_md_path = os.path.join(root, file)
                    break 
    
    if not final_md_path:
        raise FileNotFoundError(f"Conversion terminée mais aucun fichier .md trouvé dans {output_dir}")

    return final_md_path

def cleanup_failed_scan(output_dir: str):
    """Nettoie le dossier en cas d'échec pour ne pas laisser de fichiers corrompus."""
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
