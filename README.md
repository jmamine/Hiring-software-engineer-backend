# Processus de Recrutement BIGmama

Votre candidature a été retenue pour le processus de recrutement de
BIGmama qui est le suivant:

- Entretien téléphonique (optionnel):

  - L'objet de cet échange est de donner un aperçu des principales étapes du processus de recrutement.

- Test pratique:
  - Un dépôt privé sur GitLab est partagé avec vous pour héberger les résultats du test expliqué ci-dessous.
  - Développer la solution en utilisant Git et GitLab pour versionner le projet.
  - Envoyer un mail signifiant que vous avez terminé le développement.
  - Nous allons ensuite tester l'application.

## Entretien technique:

Un entretien est programmé dans les locaux de BIGmama. Le but de cet
entretien est de donner l'opportunité au candidat d'exposer le spèctre
de ses compétences. Ramener son ordinateur personnel est vivement encouragé.

## Entretien relationnel (optionnel):

Un second entretien sera planifié dans la mesure du possible. Suite à l'entretien,
vous receverez une réponse.

Il arrive qu'un candidat nous intéresse mais que nous ne puissions pas l'embaucher
immédiatement. Nous gardons soigneusement ce candidat dans une liste à part et nous
le contacterons dès que nous avons une opportunité de recruter.

## Foire aux Questions:

### Pour quel poste?

Le poste est celui de "Software Engineer" basé à Alger.

### Je ne suis pas en mesure de me présenter pour un entretien?

Répondre à la chaine mail pour informer de votre indisponibilité au
minimum 24h avant la date prévue de l'entretien, ou appeler la personne
qui vous a contaté par téléphone.

### Où en est ma candidature?

Nous envoyons des réponses à tous les candidats ayant répondu au test.
Cela peut parfois prendre du temps, mais nous tenons à donner un retour.
Nous allons vous contacter quelle que soit la décision prise.

### Je ne peux pas répondre au test présentement (cas de force majeure)

Envoyer un mail qui explique la situation.

### Quel langage dois-je utiliser?

Le meilleur langage pour le job.

Traîter ce dépôt comme un réel projet. Une application qui servira
le modèle aux utilisateurs.

## Test

The test consists of implementing a reliable communication stream protocol based on UDP (User Datagram Protocol). You are free to implement a protocol standard like [Reliable User Datagram Protocol](https://en.wikipedia.org/wiki/Reliable_User_Datagram_Protocol). However, for simplicity purposes the only requirements for this test is the reliability and flow control aspects. i.e: you don't have to follow the standard exactly. And since the time is limited, you should only focus on the correctness rather than performance.

For the programming language and framework used, it is preferable to work with one of the following:
- C/C++ (Any networking library)
- Python (sockets/asyncio)
- Golang (built-in net package)
- Rust (built-in net package/Tokio)

Other than the above requirements, feel free to test the protocol in any way you want (Server/Client, Peer-to-Peer ...etc)


You can find some useful resources at:

- [UDP RFC 768](https://www.ietf.org/rfc/rfc768.txt)
- [Reliable UDP protocol draft](https://datatracker.ietf.org/doc/html/draft-ietf-sigtran-reliable-udp-00/)
