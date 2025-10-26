import requests
import random
import string
import re
import warnings
import time
import json
from datetime import datetime

warnings.filterwarnings('ignore', message='Unverified HTTPS request')

# Titre ASCII
print("""
████████╗██╗  ██╗██╗   ██╗████████╗    ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
╚══██╔══╝╚██╗██╔╝██║   ██║╚══██╔══╝   ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ██║    ╚███╔╝ ██║   ██║   ██║      ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
   ██║    ██╔██╗ ██║   ██║   ██║      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║   ██╔╝ ██╗╚██████╔╝   ██║      ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝ ╚═════╝    ╚═╝       ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
""")

class InstagramEmailScanner:
    def __init__(self):
        self.session = requests.Session()
        self.results = []
        self.language = "en"  # Langue par défaut: anglais
        
        # Dictionnaire de traductions
        self.translations = {
            "fr": {
                "scanning": "Scan de @{}...",
                "not_found": "Non trouvé",
                "error_user_not_found": "ERREUR: Utilisateur @{} non trouve ou banni",
                "error_connection": "ERREUR de connexion: {}",
                "error_unexpected": "ERREUR inattendue: {}",
                "results_for": "RESULTATS POUR @{}",
                "full_name": "Nom complet: {}",
                "user_id": "ID utilisateur: {}",
                "email": "Email: {}",
                "phone": "Telephone: {}",
                "verified": "Verifie: {}",
                "private": "Prive: {}",
                "followers": "Followers: {}",
                "following": "Following: {}",
                "posts": "Posts: {}",
                "bio": "Bio: {}",
                "not_available": "Non disponible",
                "yes": "Oui",
                "no": "Non",
                "scan_start": "Debut du scan de {} utilisateurs...",
                "no_results_export": "Aucun resultat a exporter",
                "results_exported": "Resultats exportes vers {}",
                "export_error": "Erreur lors de l'export: {}",
                "menu_title": "INSTAGRAM EMAIL SCANNER",
                "scan_single": "Scanner un utilisateur",
                "scan_multiple": "Scanner plusieurs utilisateurs",
                "export_results": "Exporter les resultats",
                "change_language": "Changer la langue",
                "quit": "Quitter",
                "choose_option": "Choisissez une option (1-5): ",
                "enter_username": "Entrez le nom d'utilisateur Instagram: ",
                "enter_usernames": "Entrez les noms d'utilisateurs (séparés par des virgules):",
                "goodbye": "Au revoir !",
                "invalid_option": "Option invalide, veuillez reessayer",
                "language_menu": "Choisissez la langue / Choose language:",
                "french": "Français",
                "english": "English",
                "continue_scan": "Voulez-vous continuer le scan? (y/n): ",
                "continue_scanning": "Continuer le scan? (y/n): "
            },
            "en": {
                "scanning": "Scanning @{}...",
                "not_found": "Not found",
                "error_user_not_found": "ERROR: User @{} not found or banned",
                "error_connection": "CONNECTION ERROR: {}",
                "error_unexpected": "UNEXPECTED ERROR: {}",
                "results_for": "RESULTS FOR @{}",
                "full_name": "Full name: {}",
                "user_id": "User ID: {}",
                "email": "Email: {}",
                "phone": "Phone: {}",
                "verified": "Verified: {}",
                "private": "Private: {}",
                "followers": "Followers: {}",
                "following": "Following: {}",
                "posts": "Posts: {}",
                "bio": "Bio: {}",
                "not_available": "Not available",
                "yes": "Yes",
                "no": "No",
                "scan_start": "Starting scan of {} users...",
                "no_results_export": "No results to export",
                "results_exported": "Results exported to {}",
                "export_error": "Error during export: {}",
                "menu_title": "INSTAGRAM EMAIL SCANNER",
                "scan_single": "Scan a user",
                "scan_multiple": "Scan multiple users",
                "export_results": "Export results",
                "change_language": "Change language",
                "quit": "Quit",
                "choose_option": "Choose an option (1-5): ",
                "enter_username": "Enter Instagram username: ",
                "enter_usernames": "Enter usernames (separated by commas):",
                "goodbye": "Goodbye!",
                "invalid_option": "Invalid option, please try again",
                "language_menu": "Choisissez la langue / Choose language:",
                "french": "Français",
                "english": "English",
                "continue_scan": "Do you want to continue scanning? (y/n): ",
                "continue_scanning": "Continue scanning? (y/n): "
            }
        }
    
    def t(self, key, *args):
        """Méthode pour obtenir les traductions."""
        return self.translations[self.language][key].format(*args) if args else self.translations[self.language][key]
    
    def change_language(self):
        """Permet de changer la langue."""
        print("\n" + "="*60)
        print(self.t("language_menu"))
        print("="*60)
        print("1. Français")
        print("2. English")
        print("="*60)
        
        choice = input("Choose / Choisissez (1-2): ").strip()
        if choice == "1":
            self.language = "fr"
            print("Langue changée en français")
        elif choice == "2":
            self.language = "en"
            print("Language changed to English")
        else:
            print("Invalid choice / Choix invalide")
    
    def ask_continue(self):
        """Demande à l'utilisateur s'il souhaite continuer."""
        while True:
            response = input(f"\n{self.t('continue_scan')}").strip().lower()
            if response in ['y', 'yes', 'oui', 'o']:
                return True
            elif response in ['n', 'no', 'non']:
                return False
            else:
                print("Please enter 'y' or 'n' / Veuillez entrer 'y' ou 'n'")
        
    def search(self, pattern, text):
        """Recherche un pattern et retourne le premier groupe."""
        match = re.search(pattern, text)
        return match.group(1) if match else self.t("not_found")
    
    def generate_headers(self):
        """Génère des en-têtes pour simuler l'app Instagram."""
        user_agent = "Instagram 237.0.0.14.102 Android (28/9; 300dpi; 900x1600; Asus; ASUS_I005DA; ASUS_I005DA; intel; en_US; 373310554)"
        
        return {
            "Host": "i.instagram.com",
            "X-Bloks-Version-Id": "4b46b3c208cf1843a50b6391ed2abed9ddf9b85a6a0a8beaad8bc4f2b9ff6e32",
            "Accept-Language": "en-US;q=1.0",
            "User-Agent": user_agent,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "ds_user_id=" + "".join(random.choice(string.ascii_lowercase) for _ in range(7))
        }
    
    def scan_user(self, username):
        """Scanne un utilisateur Instagram pour récupérer ses informations."""
        print(f"\n{self.t('scanning', username)}")
        
        try:
            headers = self.generate_headers()
            
            response = self.session.post(
                "https://i.instagram.com/api/v1/users/lookup/",
                headers=headers,
                data=f"q={username}",
                verify=False,
                timeout=10
            )
            
            response.raise_for_status()
            data = response.text
            
            if '"status":"ok"' in data:
                # Extraction des informations
                user_info = {
                    'username': username,
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'user_id': self.search(r'"user_id":(\d+)', data),
                    'full_name': self.search(r'"full_name":"([^"]*)"', data),
                    'email': self.search(r'"obfuscated_email":"([^"]*)"', data),
                    'phone': self.search(r'"obfuscated_phone":"([^"]*)"', data),
                    'is_verified': 'is_verified":true' in data,
                    'is_private': 'is_private":true' in data,
                    'follower_count': self.search(r'"follower_count":(\d+)', data),
                    'following_count': self.search(r'"following_count":(\d+)', data),
                    'media_count': self.search(r'"media_count":(\d+)', data),
                    'biography': self.search(r'"biography":"([^"]*)"', data)
                }
                
                # Affichage des résultats
                self.display_results(user_info)
                
                # Sauvegarde pour export
                self.results.append(user_info)
                
                return user_info
                
            else:
                print(self.t('error_user_not_found', username))
                return None
                
        except requests.exceptions.RequestException as e:
            print(self.t('error_connection', e))
            return None
        except Exception as e:
            print(self.t('error_unexpected', e))
            return None
    
    def display_results(self, user_info):
        """Affiche les résultats de manière formatée."""
        print("=" * 60)
        print(self.t('results_for', user_info['username']))
        print("=" * 60)
        
        # Informations de base
        print(self.t('full_name', user_info['full_name']))
        print(self.t('user_id', user_info['user_id']))
        print(self.t('email', user_info['email'] if user_info['email'] != self.t('not_found') else self.t('not_available')))
        print(self.t('phone', user_info['phone'] if user_info['phone'] != self.t('not_found') else self.t('not_available')))
        
        # Statuts
        print(self.t('verified', self.t('yes') if user_info['is_verified'] else self.t('no')))
        print(self.t('private', self.t('yes') if user_info['is_private'] else self.t('no')))
        
        # Statistiques
        if user_info['follower_count'] != self.t('not_found'):
            print(self.t('followers', user_info['follower_count']))
        if user_info['following_count'] != self.t('not_found'):
            print(self.t('following', user_info['following_count']))
        if user_info['media_count'] != self.t('not_found'):
            print(self.t('posts', user_info['media_count']))
        
        # Bio
        if user_info['biography'] != self.t('not_found') and user_info['biography']:
            print(self.t('bio', user_info['biography'][:100] + ('...' if len(user_info['biography']) > 100 else '')))
        
        print("=" * 60)
    
    def scan_multiple_users(self, usernames):
        """Scanne plusieurs utilisateurs."""
        print(self.t('scan_start', len(usernames)))
        
        for i, username in enumerate(usernames, 1):
            print(f"\n[{i}/{len(usernames)}]")
            self.scan_user(username)
            
            # Pause entre les requêtes pour éviter le rate limiting
            if i < len(usernames):
                time.sleep(2)
    
    def export_results(self, filename="instagram_scan_results.json"):
        """Exporte les résultats vers un fichier JSON."""
        if not self.results:
            print(self.t('no_results_export'))
            return
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, indent=2, ensure_ascii=False)
            print(self.t('results_exported', filename))
        except Exception as e:
            print(self.t('export_error', e))
    
    def show_menu(self):
        """Affiche le menu principal."""
        print("\n" + "="*60)
        print(self.t('menu_title'))
        print("="*60)
        print(f"1. {self.t('scan_single')}")
        print(f"2. {self.t('scan_multiple')}")
        print(f"3. {self.t('export_results')}")
        print(f"4. {self.t('change_language')}")
        print(f"5. {self.t('quit')}")
        print("="*60)

def main():
    scanner = InstagramEmailScanner()
    
    while True:
        scanner.show_menu()
        choice = input(f"\n{scanner.t('choose_option')}").strip()
        
        if choice == "1":
            username = input(scanner.t('enter_username')).strip()
            if username:
                scanner.scan_user(username)
                if not scanner.ask_continue():
                    print("Scan arrêté par l'utilisateur / Scan stopped by user")
        
        elif choice == "2":
            print(scanner.t('enter_usernames'))
            usernames_input = input("> ").strip()
            if usernames_input:
                usernames = [u.strip().replace("@", "") for u in usernames_input.split(",")]
                scanner.scan_multiple_users(usernames)
        
        elif choice == "3":
            scanner.export_results()
        
        elif choice == "4":
            scanner.change_language()
        
        elif choice == "5":
            print(scanner.t('goodbye'))
            break
        
        else:
            print(scanner.t('invalid_option'))

if __name__ == "__main__":
    main()
