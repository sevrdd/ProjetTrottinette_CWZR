# SuperStyleTheGoodOne

Zachary Roy, William Champagne

Tableau de bord de trottinette

Traiter et présenter de manière claire et ergonomique au conducteurs les données de la trottinette.

## Prérequis
Une trottinette fonctionelle auquelle le module de tableau de bord est branché.

### Matériel
- Boitier
- PCB    
- Écran (raspberry PI)
### Logiciel
- PCB -> Altium
- Code -> STM32CubeIDE et VsCode
- Modèle 3D -> Fusion 360

### Limitations
L'affichage est limité à une vitesse de rafraîchissement de 5 Hz

## Structure

### Schéma
La section "Schematics" du dépôt github contient les shémas suivant : 
- Shéma bloc
- Shéma électrique
- Organigramme  

### Dossiers/codes
La section "Code" du dépôt github contient les codes suivant : 
- stm32_main.c -> Code main du microcontrolleur STM32. Il doit être renommé Main.c une fois dans le MCU
- tk_main.py -> Code python pour l'écran.
### Tests/validation

## Utilisation

### Pour un utilisateur
Voir [Guide d'utilisateur](<Guide d'utilisateur/guide.md>)

### Pour un developpeur

### Prochaines étapes (todo)