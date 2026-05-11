## 16 Février
- Création du projet Altium
- Création du repo GitHub
- Début de la création du schéma électrique
    - Recherche des composantes nécessaires et des *datasheets* associées
- Installation de TouchGFX
    - Configuration de l'environnement et recherche sur la librairie

## 23 Février
- Finalisation du schéma électrique
    - Sélection du mode de communication (header choisi pour plus de polyvalence)
    - Examen par les pairs
- Création du BOM et envoi du BOM
- Recherche sur TouchGFX

## 9 Mars
- Début du PCB
- Recherche et début du code Python Tkinter
    - Structure générale créée, mais non fonctionnelle

## 16 Mars
- Finalisation du PCB et envoi en fabrication
- Finalisation du développement du code
    - Fonctionnel avec un petit système de simulation prêt

## 23 Mars
- Installation des librairies et configuration de l'environnement de déboggage Python pour le Raspberry Pi
- Test du code sur Raspberry Pi (succès)
- Début du modèle 3D

## 30 Mars
- Finalisation du boîtier et envoi en fabrication
- Début du guide d'utilisateur, de la documentation, du plan de test, etc.

## 13 Avril
- Assemblage du PCB
    - Les DELs étaient plus petites que les pads, donc un *bridge* avec un fil a dû être effectué
    - Les boutons étaient beaucoup trop gros pour les pads, donc seul le bouton de reset du STM32 a été installé
- Continuation de la documentation, du guide d'utilisateur, du plan de test, de la conception de l'ordinogramme, etc.

## 20 Avril
- Le boîtier a été envoyé en production
- Du contenu a été ajouté au README
- L'assemblage du PCB est terminé
    - Aucun fil disponible pour continuer le plan de test

## 27 Avril
- Un fil a été trouvé pour continuer le plan de test du PCB
- Les trous du boîtier pour fixer le PCB étaient trop éloignés l'un de l'autre
    - Après modifications, une nouvelle version a été envoyée en production

## 4 Mai
- Assemblage terminé
- Test de la carte
    - Le régulateur ne fonctionne pas. Un *bypass* a été effectué en alimentant directement le point de test 3V3, mais le STM32 ne s'allume pas (ou n'est pas reconnu par l'ordinateur)
    - Le Raspberry Pi ne laisse pas le code accéder au port UART. Malgré plusieurs essais, le port UART reste bloqué
- Finalisation du plan de test (complété et envoyé)
