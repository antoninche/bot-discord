# Bot Discord

Un bot Discord modulaire en Python (discord.py 2.x), avec modération, automod,
système de niveaux et tickets. Chaque commande existe en version préfixée
(`!ping`) et en slash (`/ping`).

Documentation complète : https://antoninche.github.io/bot-discord/

## Commandes

| Domaine | Commandes |
|---|---|
| Administration | `ping` `purge` |
| Modération | `ban` `kick` `timeout` `unban` `warn` `warnings` |
| Automod | `automod` `anticaps` `antilinks` `setlogchannel` |
| Niveaux | `rank` `leaderboard` `xp` |
| Rôles | `addrole` `removerole` `reactionrole` `roleinfo` |
| Tickets | `ticket` |
| Infos | `userinfo` `serverinfo` `avatar` |
| Vocal | `join` `leave` |
| Divers | `roll` `coinflip` `choose` `setprefix` |

Les commandes sensibles sont réservées aux membres ayant la permission
Administrateur. `purge` est borné à 200 messages, `roll` à 1000 faces.

## Fonctionnement

Chaque domaine est un module séparé dans `bot/`, chargé automatiquement au
démarrage. `config.json` est lu et validé avant la connexion : si un champ
manque ou n'a pas le bon type, le bot s'arrête avec un message explicite plutôt
que de planter plus tard.

Les préfixes, salons de logs et réglages d'automod sont stockés par serveur
(`guild_config.py`), ce qui permet au même bot de tourner sur plusieurs serveurs
avec des configurations différentes.

La synchronisation des slash commands est globale par défaut ; renseigner
`guild_id_for_dev_sync` dans la config la limite à un serveur de test, ce qui
évite d'attendre la propagation Discord pendant le développement.

## Lancer le bot

```bash
pip install -r requirements.txt
# renseigner le token dans config.json
python -m bot
```

Python 3.10 ou plus.

Licence MIT.
