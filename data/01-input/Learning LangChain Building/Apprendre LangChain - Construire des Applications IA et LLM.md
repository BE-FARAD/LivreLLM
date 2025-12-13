![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_3.jpeg)

## Félicitations pour *l'apprentissage de LangChain*

*Avec des explications claires et des techniques exploitables, il s'agit de la ressource incontournable pour tous ceux qui cherchent à exploiter la puissance de LangChain pour une IA et des agents génératifs prêts à la production. Une lecture incontournable pour les développeurs souhaitant repousser les limites de cette plateforme.*

—Tom Taulli, consultant informatique et auteur de *AI-Assisted Programming*

*Ce guide complet sur LangChain couvre tout, de la récupération et de l'indexation de documents au déploiement et à la surveillance d'agents IA en production. Avec des exemples attrayants, des illustrations intuitives et du code pratique, ce livre a rendu l'apprentissage de LangChain intéressant et amusant !*

—Rajat K. Goel, ingénieur logiciel senior, IBM

*Ce livre est un guide LLM complet couvrant les principes fondamentaux de la production, rempli d'informations techniques, de stratégies pratiques et de modèles d'IA robustes.*

—Gourav Singh Bais, scientifique des données principal et rédacteur de contenu technique principal, Allianz Services

*Le prototypage d'applications d'IA générative est simple, mais leur expédition est difficile. Les stratégies et les outils de Learning LangChain permettent de transformer les idées en applications modernes et prêtes pour la production.*

> —James Spiteri, directeur de la gestion des produits pour la sécurité, Elastic

*L'apprentissage de LangChain fournit une voie claire pour transformer la façon dont vous créez des applications basées sur l'IA. En décomposant des architectures flexibles et des points de contrôle robustes, il offre une base solide pour créer à grande échelle des agents d'IA fiables et prêts pour la production.*

—David O'Regan, responsable de l'ingénierie pour l'IA/ML, GitLab

*L'apprentissage de LangChain nous a aidé à éviter le passe-partout pour le débogage et la surveillance. Les nombreux modèles et informations utiles sur les outils nous ont permis d'avancer rapidement et de déployer des applications d'IA en toute confiance.*

—Chris Focke, scientifique en chef de l'IA, AppFolio

*Enseignant LangChain à travers des exemples clairs et exploitables, ce livre est une passerelle vers des applications agentiques aussi inspirantes que les romans de science-fiction d'Asimov.*

— Ilya Meyzin, vice-président directeur de la science des données, Dun & Bradstreet

## Apprentissage de LangChain

Création d'applications IA et LLM avec LangChain et LangGraph

Mayo Oshin et Nuno Campos

![](_page_4_Picture_3.jpeg)

## Apprentissage de LangChain

de Mayo Oshin et Nuno Campos

Copyright © 2025 Olumayowa "Mayo" Olufemi Oshin. Tous droits réservés.

Imprimé aux États-Unis d'Amérique.

Publié par O'Reilly Media, Inc., 1005 Gravenstein Highway North, Sébastopol, CA 95472.

Les livres O'Reilly peuvent être achetés à des fins éducatives, commerciales ou promotionnelles. Des éditions en ligne sont également disponibles pour la plupart des titres (*[http://oreilly.com](http://oreilly.com/)*). Pour plus d'informations, contactez notre service des ventes corporatives/institutionnelles : 800-998-9938 ou *corporate@oreilly.com*.

- Rédactrice des acquisitions : Nicole Butterfield
- Editeur du développement : Corbin Collins
- Monteuse de production : Clare Laylock
- Editeur : nSight, Inc.
- Correctrice : Helena Stirling
- Indexeur : Judith McConville
- Architecte d'intérieur : David Futato
- Créatrice de la couverture : Karen Montgomery
- Illustratrice : Kate Dullea
- Février 2025 : Première édition

## Historique des révisions de la première édition

2024-02-13 : Première version

Voir *<http://oreilly.com/catalog/errata.csp?isbn=9781098167288>* pour plus de détails sur la version.

Le logo O'Reilly est une marque déposée d'O'Reilly Media, Inc. *Learning LangChain*, l'image de couverture et la présentation commerciale associée sont des marques de O'Reilly Media, Inc.

Les opinions exprimées dans cet ouvrage sont celles des auteurs et ne représentent pas celles de l'éditeur. Bien que l'éditeur et les auteurs aient déployé des efforts de bonne foi pour garantir que les informations et les instructions contenues dans cet ouvrage sont exactes, l'éditeur et les auteurs déclinent toute responsabilité en cas d'erreurs ou d'omissions, y compris, sans limitation, la responsabilité pour les dommages résultant de l'utilisation de

ou la confiance dans ce travail. L'utilisation des informations et des instructions contenues dans cet ouvrage se fait à vos propres risques. Si des échantillons de code ou toute autre technologie que cet ouvrage contient ou décrit sont soumis à des licences open source ou aux droits de propriété intellectuelle de tiers, il est de votre responsabilité de vous assurer que votre utilisation est conforme à ces licences et/ou droits.

978-1-098-16728-8

[LSI]

## <span id="page-8-0"></span>Préface
<span id="page-8-3"></span><span id="page-8-1"></span>Le 30 novembre 2022, la société OpenAI, basée à San Francisco, a rendu public [ChatGPT](https://oreil.ly/uAnsr), le chatbot viral à IA capable de générer du contenu, de répondre aux questions et de résoudre des problèmes comme un humain. Dans les deux mois suivant son lancement, ChatGPT a attiré plus de 100 millions d'utilisateurs actifs [mensuellement](https://oreil.ly/ATsLe), soit le taux d'adoption le plus rapide d'une nouvelle application technologique grand public (jusqu'à présent). ChatGPT est une expérience de chatbot alimentée par une version optimisée pour les instructions et les dialogues de la famille GPT-3.5 de grands modèles de langage (LLM) d'OpenAI. Nous reviendrons très prochainement sur les définitions de ces concepts.

#### **REMARQUE**

<span id="page-8-4"></span><span id="page-8-2"></span>La création d'applications LLM avec ou sans LangChain nécessite l'utilisation d'un LLM. Dans ce livre, nous utiliserons l'API OpenAI comme fournisseur LLM que nous utilisons dans les exemples de code (les prix sont répertoriés sur sa [plateforme\)](https://oreil.ly/-YYoR). L'un des avantages de travailler avec LangChain est que vous pouvez suivre tous ces exemples en utilisant soit OpenAI, soit d'autres fournisseurs LLM commerciaux ou open source.

Trois mois plus tard, OpenAI a publié l'API [ChatGPT](https://oreil.ly/DwU7R), permettant aux développeurs d'accéder aux fonctionnalités de chat et de synthèse vocale. Cela a lancé un nombre incalculable de nouvelles applications

<span id="page-9-1"></span>et développements techniques sous le terme générique d'*IA générative*.

<span id="page-9-3"></span><span id="page-9-0"></span>Avant de définir l'IA générative et les LLM, abordons le concept d'*apprentissage automatique* (ML). Certains *algorithmes* informatiques (imaginez une recette reproductible pour accomplir une tâche prédéfinie, comme trier un jeu de cartes) sont directement écrits par un ingénieur logiciel. D'autres algorithmes informatiques sont plutôt *appris* à partir d'un grand nombre d'exemples de formation : le travail de l'ingénieur logiciel passe de l'écriture de l'algorithme lui-même à l'écriture de la logique de formation qui crée l'algorithme. Dans le domaine du ML, une grande attention a été portée au développement d'algorithmes permettant de prédire un certain nombre de choses, de la météo de demain à l'itinéraire de livraison le plus efficace pour un chauffeur Amazon.

<span id="page-9-4"></span>Avec l'avènement des LLM et d'autres modèles génératifs (tels que les modèles de diffusion pour générer des images, que nous n'abordons pas dans ce livre), ces mêmes techniques de ML sont désormais appliquées au problème de la génération de nouveau contenu, tel qu'un nouveau paragraphe de texte ou de dessin, qui est à la fois unique et éclairé par des exemples dans les données de formation. Les LLM en particulier sont des modèles génératifs dédiés à la génération de texte.

<span id="page-9-2"></span>Les LLM présentent deux autres différences par rapport aux algorithmes de ML précédents :

- Ils sont formés sur des quantités de données bien plus importantes ; former l’un de ces modèles à partir de zéro serait très coûteux.
- Ils sont plus polyvalents.

Le même modèle de génération de texte peut être utilisé pour le résumé, la traduction, la classification, etc., alors que les modèles ML précédents étaient généralement formés et utilisés pour une tâche spécifique.

Ces deux différences concourent à faire évoluer à nouveau le travail de l'ingénieur logiciel, avec de plus en plus de temps consacré à déterminer comment faire fonctionner un LLM pour son cas d'utilisation. Et c’est ce qu’est LangChain.

<span id="page-10-4"></span><span id="page-10-3"></span><span id="page-10-1"></span><span id="page-10-0"></span>Fin 2023, des LLM concurrents sont apparus, notamment Claude d'Anthropic et Bard de Google (rebaptisé plus tard Gemini), offrant un accès encore plus large à ces nouveaux capacités. Et par la suite, des milliers de startups et de grandes entreprises à succès ont intégré des API d’IA générative pour créer des applications pour divers cas d’utilisation, allant des chatbots de support client à l’écriture et au débogage de code.

<span id="page-10-2"></span>Le 22 octobre 2022, Harrison Chase [publié](https://oreil.ly/mCdYZ) le premier commit sur GitHub pour la bibliothèque open source LangChain. LangChain est parti du constat que le LLM le plus intéressant

les applications nécessaires pour utiliser les LLM avec « d'autres sources de calcul ou de [connaissances ». Pour](https://oreil.ly/uXiPi), vous pouvez essayer d'obtenir un LLM pour générer la réponse à cette question :

Combien de balles reste-t-il après avoir divisé 1 234 balles

Vous serez probablement déçu par ses prouesses en mathématiques. Cependant, si vous l'associez à une fonction de calculatrice, vous pouvez demander au LLM de reformuler la question en une entrée qu'une calculatrice pourrait gérer :

1 234 % 123
Ensuite, vous pouvez transmettre cela à une fonction de calculatrice et obtenir une réponse précise à votre question initiale. LangChain a été la première (et, au moment de la rédaction, la plus grande) bibliothèque à fournir de tels éléments de base et les outils nécessaires pour les combiner de manière fiable dans des applications plus vastes. Avant de discuter de ce qu'il faut pour créer des applications convaincantes avec ces nouveaux outils, familiarisons-nous davantage avec les LLM et LangChain.

## <span id="page-11-0"></span>Brève introduction aux LLM

<span id="page-12-6"></span><span id="page-12-3"></span><span id="page-12-1"></span>En termes simples, les LLM sont des algorithmes entraînés qui reçoivent une saisie de texte et prédisent et génèrent une sortie de texte semblable à celle d'un humain. Essentiellement, ils se comportent comme la fonctionnalité de saisie semi-automatique familière que l’on trouve sur de nombreux smartphones, mais poussée à l’extrême.

Décomposons le terme *grand modèle de langage* :

- <span id="page-12-7"></span><span id="page-12-4"></span><span id="page-12-0"></span>*Large* fait référence à la taille de ces modèles en termes de données d'entraînement et de paramètres utilisés pendant le processus d'apprentissage. Par exemple, le modèle GPT-3 d'OpenAI contient 175 milliards de *paramètres*, qui ont été appris lors d'un entraînement sur 45 téraoctets de données texte. Les *Paramètres* dans un modèle de réseau neuronal sont constitués des nombres qui contrôlent la sortie de chaque *neurone* et le poids relatif de ses connexions avec ses neurones voisins. (Le fait de savoir exactement quels neurones sont connectés à quels autres neurones varie pour chaque architecture de réseau neuronal et dépasse le cadre de ce livre.) **[1](#page-43-0)**
- <span id="page-12-5"></span><span id="page-12-2"></span>*Modèle linguistique* fait référence à un algorithme informatique formé pour recevoir du texte écrit (en anglais ou dans d'autres langues) et produire également un résultat sous forme de texte écrit (dans la même langue ou dans une autre). Il s'agit de *réseaux de neurones*, un type de modèle ML qui ressemble à une conception stylisée du cerveau humain, dont le résultat final résulte de la combinaison des sorties individuelles de nombreuses fonctions mathématiques simples, appelées *neurones*, et de leurs interconnexions. Si beaucoup

De ces neurones sont organisés de manière spécifique, avec le bon processus d'entraînement et les bonnes données d'entraînement, cela produit un modèle capable d'interpréter le sens de mots et de phrases individuels, ce qui permet de les utiliser pour générer un texte écrit plausible et lisible.

<span id="page-13-2"></span><span id="page-13-1"></span>En raison de la prévalence de l'anglais dans les données de formation, la plupart des modèles sont meilleurs en anglais que dans d'autres langues avec un plus petit nombre de locuteurs. Par « mieux », nous entendons qu'il est plus facile de les amener à produire les résultats souhaités en anglais. Il existe des LLM conçus pour une sortie multilingue, tels que [BLOOM,](https://oreil.ly/Nq7w0) qui utilisent une plus grande proportion de données de formation dans d'autres langues. Curieusement, la différence de performance entre les langues n'est pas aussi grande qu'on pourrait s'y attendre, même dans les LLM formés sur un corpus de formation majoritairement anglais. Les chercheurs ont découvert que les LLM sont capables de transférer une partie de leur compréhension sémantique vers d’autres langues. **[2](#page-43-1)**

<span id="page-13-0"></span>Ensemble, les *grands modèles linguistiques* sont des instances de grands modèles linguistiques à usage général qui sont formés sur de grandes quantités de texte. En d’autres termes, ces modèles ont appris des modèles présents dans de vastes ensembles de données de textes (livres, articles, forums et autres sources accessibles au public) pour effectuer des tâches générales liées aux textes. Ces tâches incluent la génération de texte, le résumé, la traduction, la classification, etc.

Disons que nous demandons à un LLM de compléter la phrase suivante :

La capitale de l'Angleterre est \_\_\_\_\_\_\_.

Le LLM prendra ce texte d'entrée et prédira la bonne réponse de sortie comme London . Cela ressemble à de la magie, mais ce n'est pas le cas. Sous le capot, le LLM estime la probabilité d'une séquence de mots étant donné une séquence de mots précédente.

**CONSEIL**

Techniquement parlant, le modèle fait des prédictions basées sur des jetons et non sur des mots. Un *jeton* représente une unité atomique de texte. Les jetons peuvent représenter des caractères individuels, des mots, des sous-mots ou même des unités linguistiques plus grandes, selon l'approche de tokenisation spécifique utilisée. Par exemple, en utilisant le tokenizer de GPT-3.5 (appelé cl100k ), la phrase *bonjour, mon cher ami* serait composée de cinq [jetons](https://oreil.ly/dU83b) (en utilisant \_ pour afficher le caractère espace) :

*Bien*

<span id="page-15-0"></span>Avec l'ID de jeton 19045

*\_matin*

Avec ID de jeton 6693

*\_de*

Avec l'ID de jeton 409

*s'arrête*

Avec l'ID de jeton 15795
*\_ami*

Avec ID de jeton 4333

Habituellement, les tokeniseurs sont formés dans le but d'avoir les mots les plus courants codés dans un seul jeton, par exemple, le mot *matin* est codé comme le jeton 6693 . Les mots moins courants, ou les mots dans d'autres langues (généralement les tokeniseurs sont formés sur le texte anglais), nécessitent plusieurs jetons pour les encoder. Par exemple, le mot *dearest* est codé sous forme de jetons 409, 15795 . Un jeton s'étend en moyenne sur quatre caractères de texte pour un texte anglais courant, soit environ les trois quarts d'un mot.

<span id="page-16-2"></span><span id="page-16-1"></span><span id="page-16-0"></span>Le moteur derrière le pouvoir prédictif des LLM est connu sous le nom d'*architecture de réseau neuronal transformateur*. L'architecture du transformateur permet aux modèles de gérer des séquences de données, telles que des phrases ou des lignes de code, et de faire des prédictions sur le(s) mot(s) suivant(s) le plus probable(s) de la séquence. Les transformateurs sont conçus pour comprendre le contexte de chaque mot dans une phrase en le considérant par rapport à tous les autres mots. Cela permet au modèle de construire une compréhension globale du sens d'une phrase, d'un paragraphe, etc. (en d'autres termes, d'une séquence de mots) en tant que signification commune de ses parties les unes par rapport aux autres. **[3](#page-43-2)**

Ainsi, lorsque le modèle voit la séquence de mots *la capitale de l'Angleterre est*, il fait une prédiction basée sur des exemples similaires qu'il a vus lors de sa formation. Dans le corpus de formation du modèle, le mot *Angleterre* (ou le ou les jetons qui le représentent) serait souvent apparu dans des phrases situées à des endroits similaires à des mots comme *France*, *États-Unis*, *Chine*. Le mot *capital* figurerait dans les données d'entraînement dans de nombreuses phrases contenant également des mots comme *Angleterre*, *France* et *US*, et des mots comme *Londres*, *Paris*, *Washington*. Cette répétition lors de l'entraînement du modèle a permis au modèle de prédire correctement que le mot suivant dans la séquence devrait être *Londres*.

<span id="page-17-5"></span><span id="page-17-4"></span>Les instructions et le texte de saisie que vous fournissez au modèle sont appelés une *invite*. Les invites peuvent avoir un impact significatif sur la qualité des résultats du LLM. Il existe plusieurs bonnes pratiques pour la *conception d'invites* ou l'*ingénierie d'invites*, notamment la fourniture d'instructions claires et concises avec des exemples contextuels, dont nous discuterons plus loin dans ce livre. Avant d'aller plus loin dans les invites, examinons différents types de LLM que vous pouvez utiliser.

<span id="page-17-3"></span><span id="page-17-2"></span><span id="page-17-1"></span>Le type de base, dont dérivent tous les autres, est communément appelé *LLM pré-entraîné* : il a été formé sur de très grandes quantités de texte (trouvé sur Internet et dans des livres, des journaux, du code, des transcriptions vidéo, etc.) dans un mode auto-supervisée. Cela signifie que, contrairement au ML supervisé, où avant la formation, le chercheur doit assembler un ensemble de données de paires de *entrée* à *sortie attendue*, pour les LLM, ces paires sont déduites des données de formation. En fait, la seule façon possible d’utiliser des ensembles de données aussi volumineux est d’assembler automatiquement ces paires à partir des données d’entraînement. Pour ce faire, deux techniques consistent à demander au modèle d'effectuer les opérations suivantes :

#### <span id="page-17-0"></span>*Prédire le mot suivant*

Supprimez le dernier mot de chaque phrase dans les données d'entraînement, et cela donne une paire d'*entrée* et de *sortie attendue*, telles que *La capitale de l'Angleterre est \_\_\_* et *Londres*.

#### *Prédire un mot manquant*

De même, si vous prenez chaque phrase et omettez un mot au milieu, vous avez maintenant d'autres paires d'entrée et de sortie attendue, telles que *Le \_\_\_ de l'Angleterre est Londres* et *capitale*.

Ces modèles sont assez difficiles à utiliser en l'état, ils nécessitent d'amorcer la réponse avec un préfixe approprié. Par exemple, si vous souhaitez connaître la capitale de l'Angleterre, vous pouvez obtenir une réponse en invitant le modèle avec *La capitale de l'Angleterre est*, mais pas avec la réponse plus naturelle *Quelle est la capitale de l'Angleterre ?*

### **LLM adaptés aux instructions**

<span id="page-18-1"></span>[Des chercheurs](https://oreil.ly/lP6hr) ont rendu les LLM pré-entraînés plus faciles à utiliser grâce à une formation complémentaire (formation supplémentaire appliquée en plus de la formation longue et coûteuse décrite dans la section précédente), également connue sous le nom de *mise au point* des éléments suivants :

#### *Ensembles de données spécifiques à une tâche*
<span id="page-18-0"></span>Il s'agit d'ensembles de données de paires de questions/réponses assemblées manuellement par les chercheurs, fournissant des exemples de réponses souhaitables à des questions courantes que les utilisateurs finaux pourraient poser au modèle. Par exemple, l'ensemble de données peut contenir la paire suivante : *Q : Quelle est la capitale de*

*L'Angleterre ? R : La capitale de l'Angleterre est Londres.* Contrairement aux ensembles de données de pré-entraînement, ceux-ci sont assemblés manuellement, ils sont donc nécessairement beaucoup plus petits :

*Apprentissage par renforcement à partir du feedback humain (RLHF)*

<span id="page-19-1"></span>Grâce à l'utilisation des [méthodes](https://oreil.ly/lrlAK) RLHF, ces ensembles de données assemblés manuellement sont complétés par les commentaires des utilisateurs reçus sur les résultats produits par le modèle. Par exemple, l'utilisateur A a préféré *La capitale de l'Angleterre est Londres* à *Londres est la capitale de l'Angleterre* pour répondre à la question précédente.

Le réglage des instructions a été essentiel pour élargir le nombre de personnes capables de créer des applications avec les LLM, car elles peuvent désormais recevoir des *instructions*, souvent sous la forme de questions telles que *Quelle est la capitale de l'Angleterre ?*, par opposition à *La capitale de l'Angleterre est*.

### **LLM optimisés pour le dialogue**

<span id="page-19-0"></span>Les modèles conçus pour le dialogue ou le chat constituent une nouvelle amélioration des LLM [instruction-tuned](https://oreil.ly/1DxW6). Différents fournisseurs de LLM utilisent différentes techniques, ce n'est donc pas nécessairement vrai pour tous les *modèles de chat*, mais cela se fait généralement via les éléments suivants :

#### *Ensembles de données de dialogue*

<span id="page-20-2"></span><span id="page-20-1"></span>Les ensembles de données de *réglage précis* assemblés manuellement sont étendus pour inclure davantage d'exemples d'interactions de dialogue multitours, c'est-à-dire des séquences de paires invite-réponse.

#### *Format de discussion*

<span id="page-20-8"></span><span id="page-20-7"></span><span id="page-20-6"></span><span id="page-20-5"></span><span id="page-20-3"></span><span id="page-20-0"></span>Les formats d'entrée et de sortie du modèle reçoivent une couche de structure sur du texte de forme libre, qui divise le texte en parties associées à un rôle (et éventuellement d'autres métadonnées comme un nom). Habituellement, les rôles disponibles sont *système* (pour les instructions et le cadrage de la tâche), *utilisateur* (la tâche ou la question réelle) et *assistant* (pour les sorties du [modèle\). Cette](https://oreil.ly/dINx0) méthode a évolué à partir des premières techniques d'ingénierie rapide et facilite l'adaptation de la sortie du modèle tout en rendant plus difficile pour les modèles de confondre les entrées de l'utilisateur avec les instructions. La confusion entre les entrées de l'utilisateur et les instructions préalables est également connue sous le nom de *jailbreaking*, ce qui peut, par exemple, conduire à ce que des invites soigneusement conçues, incluant éventuellement des secrets commerciaux, soient exposées aux utilisateurs finaux.

### <span id="page-20-4"></span>**LLM affinés**

<span id="page-21-0"></span>Des LLM affinés sont créés en prenant des LLM de base et en les formant davantage sur un ensemble de données propriétaire pour une tâche spécifique. Techniquement, les LLM optimisés pour les instructions et les dialogues sont des LLM optimisés, mais le terme « LLM optimisé » est généralement utilisé pour décrire les LLM optimisés par le développeur pour leur tâche spécifique. Par exemple, un modèle peut être affiné pour extraire avec précision le sentiment, les facteurs de risque et les chiffres financiers clés du rapport annuel d'une entreprise publique. Habituellement, les modèles affinés ont amélioré les performances sur la tâche choisie au prix d’une perte de généralité. Autrement dit, ils deviennent moins capables de répondre à des requêtes sur des tâches sans rapport.

Dans le reste de ce livre, lorsque nous utilisons le terme *LLM*, nous entendons des LLM orientés instructions, et pour *modèle de chat*, nous entendons des LLM orientés dialogue, tels que définis plus haut dans cette section. Ceux-ci devraient être vos bêtes de somme lorsque vous utilisez les LLM : les premiers outils que vous utilisez lorsque vous démarrez une nouvelle application LLM.

<span id="page-21-1"></span>Discutons maintenant rapidement de quelques techniques d'invite LLM courantes avant de plonger dans LangChain.

## Brève introduction à l'invite

<span id="page-22-3"></span>Comme nous l'avons évoqué plus tôt, la tâche principale de l'ingénieur logiciel travaillant avec des LLM n'est pas de former un LLM, ni même d'en peaufiner un (généralement), mais plutôt de prendre un LLM existant et de trouver comment l'amener à accomplir la tâche dont vous avez besoin pour votre application. Il existe des fournisseurs commerciaux de LLM, comme OpenAI, Anthropic et Google, ainsi que des LLM open source [\(Llama,](https://oreil.ly/ld3Fu) [Gemma](https://oreil.ly/RGKfi) et autres), publiés gratuitement sur lesquels d'autres peuvent s'appuyer. L'adaptation d'un LLM existant à votre tâche s'appelle *l'ingénierie rapide*.
<span id="page-22-0"></span>De nombreuses techniques d'incitation ont été développées au cours des deux dernières années et, au sens large, il s'agit d'un livre sur la manière de réaliser une ingénierie d'invite avec LangChain – comment utiliser LangChain pour amener les LLM à faire ce que vous avez en tête. Mais avant d'entrer dans LangChain proprement dit, il est utile de passer d'abord en revue certaines de ces techniques (et nous nous excusons d'avance si votre technique [invite](https://oreil.ly/8uGK_) préférée n'est pas répertoriée ici ; il y en a trop à couvrir).

<span id="page-22-2"></span>Pour suivre cette section, nous vous recommandons de copier ces invites dans OpenAI Playground pour les essayer vous-même :

<span id="page-22-1"></span>1. Créez un compte pour l'API OpenAI sur *[http://platform.openai.com](http://platform.openai.com/)*, qui vous permettra d'utiliser les LLM OpenAI par programme, c'est-à-dire en utilisant l'API de votre code Python ou JavaScript. Il vous donnera également accès à OpenAI Playground, où vous pourrez expérimenter les invites de votre navigateur Web.

- 2. Si nécessaire, ajoutez les détails de paiement de votre nouveau compte OpenAI. OpenAI est un fournisseur commercial de LLM et facture des frais pour chaque fois que vous utilisez leurs modèles via l'API d'OpenAI ou via Playground. Vous pouvez trouver les derniers tarifs sur leur [site Web.](https://oreil.ly/MiKRD) Au cours des deux dernières années, le prix d'utilisation des modèles OpenAI a considérablement baissé à mesure que de nouvelles fonctionnalités et optimisations sont introduites.
- 3. Rendez-vous sur OpenAI [Playground](https://oreil.ly/rxiAG) et vous êtes prêt à essayer les invites suivantes par vous-même. Nous utiliserons l'API OpenAI tout au long de ce livre.
- 4. Une fois que vous avez accédé au Playground, vous verrez un panneau de préréglages sur le côté droit de l'écran, comprenant le modèle de votre choix. Si vous regardez plus bas dans le panneau, vous verrez Température sous le titre « Configuration du modèle ». Déplacez le bouton Température du milieu vers la gauche jusqu'à ce que le nombre indique 0,00. Essentiellement, la température contrôle le caractère aléatoire de la sortie LLM. Plus la température est basse, plus les résultats du modèle sont déterministes.

<span id="page-23-0"></span>Passons maintenant aux invites !

### **Invite de tir zéro**

<span id="page-24-0"></span>La première technique d'invite, et la plus simple, consiste simplement à demander au LLM d'effectuer la tâche souhaitée :

Quel âge avait le 30ème président des États-Unis

C'est généralement ce que vous devriez essayer en premier, et cela fonctionnera généralement pour des questions simples, en particulier lorsque la réponse était probablement présente dans certaines données d'entraînement. Si nous invitons gpt-3.5-turbo d'OpenAI avec l'invite précédente, ce qui suit est renvoyé :

Le 30e président des États-Unis, Calvin C, la mère de son épouse, est décédée en 1926.

#### **REMARQUE**

Vous pourriez obtenir un résultat différent de celui que nous obtenons. Il existe un élément de hasard dans la manière dont les LLM génèrent des réponses, et OpenAI a peut-être mis à jour le modèle au moment où vous l'essayez.

Même si le modèle a correctement identifié le 30e président, la réponse n’est pas tout à fait exacte. Vous devrez souvent répéter les invites et les réponses pour obtenir un système fiable. Les sections suivantes expliquent comment.

### **Chaîne de pensée**

<span id="page-25-1"></span><span id="page-25-0"></span>Une itération très utile consiste à demander davantage au modèle de prendre le temps de *réfléchir*. Il a été constaté que cette [technique](https://oreil.ly/8xWcs) augmente les performances sur une variété de tâches. Curieusement, un article plus récent suggère que cette technique peut également réduire les performances du LLM sur des tâches où la réflexion réduit les performances humaines. Appelé invite de chaîne de pensée (CoT), cela se fait généralement en ajoutant à l'invite des instructions permettant au LLM de décrire comment il pourrait arriver à la réponse : **[4](#page-43-3)**

```
Think step by step.
```
Quel âge avait le 30ème président des États-Unis

Voyons maintenant ce que le même modèle produit pour cette nouvelle invite :

1. Tout d'abord, découvrez qui est le 30e président du pays en recherchant une liste des présidents américains ou en ligne. Vous trouverez cela Coolidge.

2. Ensuite, découvrez l'année où Calvin Coolidge a

être trouvé en effectuant une recherche en ligne ou dans une histoire du président de 1923 à 1929.

3. Maintenant, vous devez déterminer l'année de Calvi. Cela peut être fait en recherchant la vie et la mort de Coolidge. Vous constaterez qu'elle a vécu de 1879 à

4. Calculez l'âge de 78 ans de l'épouse de Calvin Coolidge.

5. Déterminer l'âge de Calvin Coolidge lorsqu'il est né, 1872, à partir de l'année de sa naissance, ce qui signifie que Calvin Coolidge avait 85 ans lorsque
Remarquez que le seul changement dans l'invite a été l'ajout de Think step by step et quelle différence cela a fait dans la sortie du modèle. Le modèle génère désormais une séquence d'étapes que vous pouvez suivre lorsque vous essayez de répondre à cette question. Malheureusement, même si les mesures sont très raisonnables,

le résultat final est toujours incorrect, étant donné que certains faits sont erronés, à savoir qu'il indique les mauvaises années de naissance et de décès pour la mère de l'épouse du président Coolidge. Voyons comment améliorer cela.

### **Génération augmentée par récupération**

<span id="page-27-1"></span><span id="page-27-0"></span>*La génération augmentée par récupération* (RAG) consiste à rechercher des éléments de texte pertinents, également appelés *contexte*, tels que des faits que vous trouveriez dans une encyclopédie, et à inclure ce contexte dans l'invite. La technique RAG peut (et dans les applications réelles devrait) être combinée avec CoT, mais par souci de simplicité, nous utiliserons ici ces techniques une par une. Voici l'invite incluant RAG :

Contexte :

- Calvin Coolidge (né John Calvin Coolidge Jr. ; 5 janvier 1933) était un avocat américain et 30e président des États-Unis de 1923 à

- Grace Anna Coolidge (née Goodhue ; 3 janvier 18 épouse du 30ème président des Etats-Unis,

- Grace Anna Goodhue est née le 3 janvier 1879, fille unique d'Andrew Issachar Goodhue et Lemira

- Lemira A. Goodhue (Barrett) ; Date de naissance : avril Burlington, comté de Chittenden, VT, États-Unis

Quel âge avait le 30ème président des États-Unis

Et le résultat du modèle :

Le 30e président des États-Unis, Calvin C, la mère de sa femme, Lemira A. Goodhue, est décédée en octobre

Nous sommes maintenant beaucoup plus proches de la bonne réponse, mais comme nous l'avons évoqué plus tôt, les LLM ne sont pas excellents en mathématiques prêtes à l'emploi. Dans ce cas, le résultat final de 54 ans est décalé de 3. Voyons comment nous pouvons améliorer ce point.

### **Appel d'outil**

<span id="page-28-0"></span>La technique *d'appel d'outil* consiste à faire précéder l'invite d'une liste de fonctions externes que le LLM peut utiliser, ainsi que des descriptions de l'utilité de chacune et des instructions sur la manière de signaler dans la sortie qu'il *veut* utiliser un (ou plusieurs) des

ces fonctions. Enfin, vous, le développeur de l'application, devez analyser le résultat et appeler les fonctions appropriées. Voici une façon de procéder :

```
Tools:
- calculator: This tool accepts math expressions 
- search: This tool accepts search engine queries
result.
If you want to use tools to arrive at the answer,
inputs in CSV format, with this header row `tool,
How old was the 30th president of the United Stat
```
Et voici le résultat que vous pourriez obtenir :

outil,entrée

calculatrice,2023-1892

recherche : "Quel âge avait Calvin Coolidge lorsque son mot

<span id="page-30-0"></span>Bien que le LLM ait correctement suivi les instructions de format de sortie, les outils et les entrées sélectionnés ne sont pas les plus appropriés pour cette question. Cela nous amène à l'une des choses les plus importantes à garder à l'esprit lors de l'incitation des LLM : *chaque technique d'incitation est plus utile lorsqu'elle est utilisée en combinaison avec (certaines des) autres*. Par exemple, nous pourrions ici améliorer cela en combinant l'appel d'outil, la chaîne de pensée et RAG dans une invite qui utilise les trois. Voyons à quoi cela ressemble :

Contexte :

- Calvin Coolidge (né John Calvin Coolidge Jr. ; 5 janvier 1933) était un avocat américain et président politique des États-Unis de 1923 à 1929.

- Grace Anna Coolidge (née Goodhue ; 3 janvier 18 du 30ème président des Etats-Unis, Calvi

- Grace Anna Goodhue est née le 3 janvier 1879, fille unique d'Andrew Issachar Goodhue et Lemira

- Lemira A. Goodhue (Barrett) ; Date de naissance : avril Burlington, comté de Chittenden, VT, États-Unis

Outils :

- calculatrice : Cet outil accepte les expressions mathématiques. Si vous souhaitez utiliser des outils pour arriver à la réponse, des saisies au format CSV, avec cet outil de ligne d'en-tête, réfléchissez étape par étape. Quel âge avait le 30ème président des États-Unis

Et avec cette invite, peut-être qu'après quelques essais, nous pourrions obtenir ce résultat :

outil,entrée

calculatrice,1929 - 1872

Si nous analysons cette sortie CSV et demandons à une fonction de calculatrice d'exécuter l'opération 1929 - 1827 , nous obtenons enfin la bonne réponse : 57 ans.

Comme dans l'exemple précédent, en combinant RAG avec une chaîne de pensée et des appels d'outils, vous pouvez récupérer les éléments les plus pertinents.

données pour ancrer la sortie de votre modèle, puis guidez-le étape par étape pour vous assurer qu'il utilise ce contexte efficacement.

### **Invite de quelques tirs**
<span id="page-32-1"></span>Enfin, nous arrivons à une autre technique d'invite très utile : *l'invite en quelques coups*. Cela consiste à fournir au LLM des exemples d'autres questions et les réponses correctes, ce qui permet au LLM d'*apprendre* comment effectuer une nouvelle tâche sans passer par une formation supplémentaire ou une mise au point. Par rapport au réglage fin, les invites en quelques étapes sont plus flexibles, vous pouvez les effectuer à la volée au moment de la requête, mais elles sont moins puissantes et vous pouvez obtenir de meilleures performances avec un réglage fin. Cela dit, vous devriez généralement toujours essayer des invites en quelques étapes avant d'affiner :

#### *Invite statique à quelques tirs*

<span id="page-32-2"></span>La version la plus basique des invites en quelques étapes consiste à assembler une liste prédéterminée d'un petit nombre d'exemples que vous incluez dans l'invite.

#### *Invite dynamique à quelques tirs*

<span id="page-32-0"></span>Si vous rassemblez un ensemble de données composé de nombreux exemples, vous pouvez à la place choisir les exemples les plus pertinents pour chaque nouveau

#### <span id="page-33-3"></span>requête.

La section suivante couvre l'utilisation de LangChain pour créer des applications à l'aide de LLM et de ces techniques d'invite.

## LangChain et pourquoi c'est important

<span id="page-33-1"></span>LangChain a été l'une des premières bibliothèques open source à fournir des blocs de construction LLM et d'invite ainsi que les outils nécessaires pour les combiner de manière fiable dans des applications plus vastes. Au moment de la rédaction, LangChain a accumulé plus de 28 millions de [téléchargements](https://oreil.ly/8OKbf) mensuels, 99 000 [GitHub](https://oreil.ly/bF5pc) étoiles et la plus grande communauté de développeurs en IA générative ([72 000+](https://oreil.ly/PNWL3) forte). Il a permis aux ingénieurs logiciels qui n'ont pas d'expérience en ML d'utiliser la puissance des LLM pour créer une variété d'applications, allant des chatbots IA aux agents IA capables de raisonner et d'agir de manière responsable.

<span id="page-33-2"></span><span id="page-33-0"></span>LangChain s'appuie sur l'idée soulignée dans la section précédente : les techniques d'incitation sont plus utiles lorsqu'elles sont utilisées ensemble. Pour faciliter cela, LangChain fournit des *abstractions* simples pour chaque technique d'invite majeure. Par abstraction, nous entendons les fonctions et classes Python et JavaScript qui encapsulent les idées de ces techniques dans des wrappers faciles à utiliser. Ces

les abstractions sont conçues pour bien fonctionner ensemble et pour être combinées dans une application LLM plus large.

<span id="page-34-1"></span><span id="page-34-0"></span>Tout d'abord, LangChain fournit des intégrations avec les principaux fournisseurs LLM, à la fois commerciaux [\(OpenAI](https://oreil.ly/TTLXA), [Anthropic](https://oreil.ly/O4UXw), [Google,](https://oreil.ly/12g3Z) et plus) et open source ([Llama,](https://oreil.ly/5WAVi) [Gemma,](https://oreil.ly/-40Ne) et autres). Ces intégrations partagent une interface commune, ce qui facilite grandement l'essai de nouveaux LLM au fur et à mesure de leur annonce et vous permet d'éviter d'être enfermé dans un seul fournisseur. Nous les utiliserons dans le [Chapitre](#page-44-0) 1.

<span id="page-34-2"></span>LangChain fournit également des abstractions de *modèle d'invite*, qui vous permettent de réutiliser les invites plus d'une fois, en séparant le texte statique dans l'invite des espaces réservés qui seront différents à chaque fois que vous l'enverrez au LLM pour générer une complétion. Nous en parlerons également davantage dans le [Chapitre](#page-44-0) 1. Les invites LangChain peuvent également être stockées dans le Hub LangChain pour être partagées avec des coéquipiers.

<span id="page-34-4"></span><span id="page-34-3"></span>LangChain contient de nombreuses intégrations avec des services tiers (tels que Google Sheets, Wolfram Alpha, Zapier, pour n'en nommer que quelques-uns) exposées sous la forme *tools*, qui est une interface standard pour les fonctions à utiliser dans la technique d'appel d'outils.

<span id="page-35-6"></span><span id="page-35-4"></span>Pour RAG, LangChain fournit des intégrations avec les principaux *modèles d'intégration* (modèles de langage conçus pour générer une représentation numérique, l'*intégration*, de la signification d'une phrase, d'un paragraphe, etc.), *magasins de vecteurs* (bases de données dédiées au stockage des intégrations) et *index vectoriels* (bases de données régulières avec capacités de stockage de vecteurs). Vous en apprendrez beaucoup plus à ce sujet dans les chapitres [2](#page-93-0) et [3](#page-163-0).

<span id="page-35-5"></span><span id="page-35-2"></span><span id="page-35-1"></span><span id="page-35-0"></span>Pour CoT, LangChain (via la bibliothèque LangGraph) fournit des abstractions *d'agent* qui combinent le raisonnement en chaîne de pensée et l'appel d'outils, popularisées pour la première fois par ReAct [papier.](https://oreil.ly/27BIC) Cela permet de créer des applications LLM qui effectuent les tâches suivantes :
- 1. Raisonnez sur les démarches à entreprendre.
- 2. Traduisez ces étapes en appels d'outils externes.
- 3. Recevez le résultat de ces appels d'outils.
- 4. Répétez jusqu'à ce que la tâche soit accomplie.

Nous les abordons dans les chapitres [5](#page-277-0) à [8.](#page-385-0)

<span id="page-35-3"></span>Pour les cas d'utilisation de chatbot, il devient utile de garder une trace des interactions précédentes et de les utiliser lors de la génération de la réponse à une interaction future. C'est ce qu'on appelle la *mémoire*, et le [Chapitre](#page-237-0) 4 explique son utilisation dans LangChain.

Enfin, LangChain fournit les outils nécessaires pour composer ces éléments de base en applications cohérentes. Les chapitres [1](#page-44-0) à [6](#page-315-0) en parlent davantage.

En plus de cette bibliothèque, LangChain fournit [LangSmith—](https://oreil.ly/geRgx) une plate-forme pour aider à déboguer, tester, déployer et surveiller les flux de travail d'IA — et LangGraph Platform — une plate-forme pour déployer et faire évoluer les agents LangGraph. Nous les abordons dans les chapitres [9](#page-424-0) et [10](#page-469-0).

## À quoi s'attendre de ce livre

Avec ce livre, nous espérons transmettre l'enthousiasme et la possibilité d'ajouter des LLM à votre ceinture d'outils de génie logiciel.

Nous nous sommes lancés dans la programmation parce que nous aimons construire des choses, arriver à la fin d'un projet, regarder le produit final et réaliser qu'il y a quelque chose de nouveau, et nous l'avons construit. La programmation avec les LLM est très excitante pour nous car elle élargit l'ensemble des choses que nous pouvons construire, elle rend des choses auparavant difficiles faciles (par exemple, extraire des nombres pertinents à partir d'un long texte) et des choses auparavant impossibles sont possibles - essayez de créer un assistant automatisé il y a un an et vous vous retrouvez avec le *téléphone*.

*l'enfer des arbres* que nous connaissons et aimons tous en appelant les numéros de support client.

Désormais, avec les LLM et LangChain, vous pouvez réellement créer des assistants agréables (ou une myriade d'autres applications) qui discutent avec vous et comprennent votre intention à un degré très raisonnable. La différence est le jour et la nuit ! Si cela vous semble passionnant (comme à nous), alors vous êtes au bon endroit.

Dans cette préface, nous vous avons rappelé ce qui motive les LLM et pourquoi exactement cela vous donne des super pouvoirs de « construction de choses ». Disposer de ces très grands modèles ML qui comprennent le langage et peuvent produire des réponses écrites en anglais conversationnel (ou dans une autre langue) vous donne un outil de génération de langage *programmable* (grâce à une ingénierie rapide) et polyvalent. À la fin du livre, nous espérons que vous comprendrez à quel point cela peut être puissant.

<span id="page-37-0"></span>Nous commencerons par un chatbot IA personnalisé, pour la plupart, à l'aide d'instructions simples en anglais. Cela seul devrait être une révélation : vous pouvez désormais « programmer » une partie du comportement de votre application sans code.

Vient ensuite la capacité suivante : donner à votre chatbot l'accès à vos propres documents, ce qui le fait passer d'un assistant générique à un assistant connaissant n'importe quel domaine de la connaissance humaine pour lequel vous pouvez trouver une bibliothèque de textes écrits. Cela vous permettra par exemple de demander au chatbot de répondre à des questions ou de résumer des documents que vous avez rédigés.

Après cela, nous ferons en sorte que le chatbot se souvienne de vos conversations précédentes. Cela l'améliorera de deux manières : il semblera beaucoup plus naturel d'avoir une conversation avec un chatbot qui se souvient de ce dont vous avez discuté précédemment, et au fil du temps, le chatbot pourra être personnalisé selon les préférences de chacun de ses utilisateurs individuellement.

Ensuite, nous utiliserons des techniques de chaîne de pensée et d'appel d'outils pour donner au chatbot la possibilité de planifier et d'agir sur ces plans, de manière itérative. Cela lui permettra de répondre à des demandes plus complexes, comme la rédaction d'un rapport de recherche sur un sujet de votre choix.

Au fur et à mesure que vous utilisez votre chatbot pour des tâches plus complexes, vous ressentirez le besoin de lui donner les outils nécessaires pour collaborer avec vous. Cela inclut à la fois la possibilité d'interrompre ou d'autoriser des actions avant qu'elles ne soient entreprises, ainsi que la possibilité pour le chatbot de demander plus d'informations ou des éclaircissements avant d'agir.

Enfin, nous vous montrerons comment déployer votre chatbot en production et discuterons de ce que vous devez prendre en compte avant et après cette étape, notamment la latence, la fiabilité et la sécurité. Nous vous montrerons ensuite comment surveiller votre chatbot en production et continuer à l'améliorer au fur et à mesure de son utilisation.

En cours de route, nous vous apprendrons les tenants et les aboutissants de chacune de ces techniques, de sorte que lorsque vous aurez terminé le livre, vous aurez véritablement ajouté un nouvel outil (ou deux) à votre ceinture d'outils de génie logiciel.

## Conventions utilisées dans ce livre
Les conventions typographiques suivantes sont utilisées dans ce livre :

*Italique*

Indique les nouveaux termes, URL, adresses e-mail, noms de fichiers et extensions de fichiers.

#### *Largeur constante*

Utilisé pour les listes de programmes, ainsi que dans les paragraphes pour faire référence à des éléments de programme tels que les noms de variables ou de fonctions, les bases de données, les types de données, les variables d'environnement, les instructions et les mots-clés.

#### **CONSEIL**

Cet élément signifie un conseil ou une suggestion.

#### **REMARQUE**

Cet élément signifie une note générale.

## Utilisation d'exemples de code

<span id="page-40-0"></span>Des documents supplémentaires (exemples de code, exercices, etc.) sont disponibles en téléchargement sur *https://oreil.ly/supp-[LearningLangChain](https://oreil.ly/supp-LearningLangChain)*.

Si vous avez une question technique ou un problème lors de l'utilisation des exemples de code, veuillez envoyer un e-mail à *[support@oreilly.com](mailto:support@oreilly.com)*.

Ce livre est là pour vous aider à accomplir votre travail. En général, si un exemple de code est proposé avec ce livre, vous pouvez l'utiliser dans vos programmes et votre documentation. Vous n'avez pas besoin de nous contacter pour obtenir une autorisation, sauf si vous reproduisez une partie importante du code. Par exemple, écrire un programme utilisant plusieurs morceaux de code de ce livre ne nécessite aucune autorisation. La vente ou la distribution d'exemples de livres O'Reilly nécessite une autorisation. Répondre à une question en citant ce livre

et citer un exemple de code ne nécessite pas d'autorisation. L'incorporation d'une quantité importante d'exemples de code de ce livre dans la documentation de votre produit nécessite une autorisation.

Nous apprécions l’attribution, mais ne l’exigeons généralement pas. Une attribution comprend généralement le titre, l'auteur, l'éditeur et l'ISBN. Par exemple : "*Learning LangChain* par Mayo Oshin et Nuno Campos (O'Reilly). Copyright 2025 Olumayowa "Mayo" Olufemi Oshin, 978-1-098-16728-8."

Si vous pensez que votre utilisation d'exemples de code ne respecte pas l'usage loyal ou l'autorisation donnée ci-dessus, n'hésitez pas à nous contacter à *[permissions@oreilly.com](mailto:permissions@oreilly.com)*.

## Apprentissage en ligne O'Reilly

#### **REMARQUE**

Depuis plus de 40 ans, *[O'Reilly](https://oreilly.com/) Media* propose des formations, des connaissances et des connaissances technologiques et commerciales pour aider les entreprises à réussir.

Notre réseau unique d'experts et d'innovateurs partage leurs connaissances et leur expertise à travers des livres, des articles et notre plateforme d'apprentissage en ligne. La plateforme d'apprentissage en ligne d'O'Reilly vous offre un accès à la demande à des cours de formation en direct, à des parcours d'apprentissage approfondis, à des environnements de codage interactifs et à une vaste collection de textes et de vidéos d'O'Reilly et de plus de 200 autres éditeurs. Pour plus d'informations, visitez *[https://oreilly.com](https://oreilly.com/)*.

## Comment nous contacter

<span id="page-42-0"></span>Veuillez adresser vos commentaires et questions concernant ce livre à l'éditeur :

O'Reilly Media, Inc.

1005, route Gravenstein Nord

Sébastopol, CA 95472

800-889-8969 (aux États-Unis ou au Canada)

707-827-7019 (international ou local)

707-829-0104 (télécopieur)

*[support@oreilly.com](mailto:support@oreilly.com)*

*<https://oreilly.com/about/contact.html>*

Nous avons une page Web pour ce livre, où nous répertorions les errata, des exemples et toute information supplémentaire. Vous pouvez accéder à cette page à *<https://oreil.ly/learning-langchain>*.

Pour des nouvelles et des informations sur nos livres et cours, visitez *[https://oreilly.com](https://oreilly.com/)*.

Retrouvez-nous sur LinkedIn : *<https://linkedin.com/company/oreilly-media>*.

Regardez-nous sur YouTube : *<https://youtube.com/oreillymedia>*.

## Remerciements

Nous tenons à exprimer notre gratitude et notre appréciation aux relecteurs – Rajat Kant Goel, Douglas Bailley, Tom Taulli, Gourav Bais et Jacob Lee – pour leurs précieux commentaires techniques sur l'amélioration de ce livre.

<span id="page-43-0"></span>Tom B. Brown et al., ["Langue](https://oreil.ly/1qoM6) Les modèles sont des apprenants peu nombreux", arXiv, 22 juillet 2020. **[1](#page-12-0)**

<span id="page-43-1"></span>Xiang Zhang et al., "Ne faites pas confiance à ChatGPT lorsque votre question n'est pas en anglais : une étude des capacités et des types de LLM [multilingues](https://oreil.ly/u5Cy1), Actes de la conférence 2023 sur les méthodes empiriques dans le traitement du langage naturel, du 6 au 10 décembre 2023. **[2](#page-13-0)**

<span id="page-43-2"></span>Pour plus d'informations, voir Ashish Vaswani et al., ["Attention](https://oreil.ly/Frtul) Is All You Need ", arXiv, 12 juin 2017. **[3](#page-16-0)**
<span id="page-43-3"></span>Ryan Liu et coll. "Faites attention à vos pas (par étape) : [Chaîne de pensée](https://oreil.ly/UHFp9) peut réduire les performances sur les tâches où la réflexion aggrave les humains", arXiv, 8 novembre 2024. **[4](#page-25-0)**

# <span id="page-44-0"></span>Chapitre 1. Fondamentaux du LLM avec LangChain

<span id="page-44-2"></span>La [Préface](#page-8-0) vous a donné un avant-goût de la puissance du LLM, où nous avons pu constater par nous-mêmes l'impact que différentes techniques d'incitation peuvent avoir sur ce que vous obtenez des LLM, en particulier lorsqu'elles sont judicieusement combinées. Le défi dans la création de bonnes applications LLM réside, en fait, dans la manière de construire efficacement l'invite envoyée au modèle et de traiter la prédiction du modèle pour renvoyer une sortie précise (voir [Figure](#page-44-1) 1-1).

<span id="page-44-1"></span>![](_page_44_Figure_2.jpeg)

Figure 1-1. Le défi de faire des LLM une partie utile de votre candidature

Si vous parvenez à résoudre ce problème, vous êtes sur la bonne voie pour créer des applications LLM, simples et complexes. Dans ce chapitre, vous en apprendrez davantage sur la façon dont les éléments de base de LangChain correspondent aux concepts LLM et comment, lorsqu'ils sont combinés efficacement, ils vous permettent de créer des applications LLM. Mais d'abord, la barre latérale « Pourquoi [LangChain ? »](#page-46-0) est une brève introduction aux raisons pour lesquelles nous pensons qu'il est utile d'utiliser LangChain pour créer des applications LLM.

#### <span id="page-46-0"></span>**POURQUOI LANGCHAIN ?**

<span id="page-46-1"></span>Vous pouvez bien sûr créer des applications LLM sans LangChain. L’alternative la plus évidente consiste à utiliser le kit de développement logiciel (SDK) – le package exposant les méthodes de leur API HTTP en tant que fonctions dans le langage de programmation de votre choix – du fournisseur LLM que vous avez essayé en premier (par exemple, OpenAI). Nous pensons qu’apprendre LangChain sera payant à court terme et à long terme en raison des facteurs suivants :

#### *Modèles courants prédéfinis*

LangChain est livré avec des implémentations de référence des modèles d'application LLM les plus courants (nous en avons mentionné certains dans la [Préface](#page-8-0) : chaîne de pensée, appel d'outils et autres). C'est le moyen le plus rapide de démarrer avec les LLM et peut souvent suffire. Nous vous suggérons de démarrer toute nouvelle application à partir de celles-ci et de vérifier si les résultats prêts à l'emploi sont suffisamment bons pour votre cas d'utilisation. Sinon, consultez l'élément suivant pour l'autre moitié des bibliothèques LangChain.

#### *Blocs de construction interchangeables*

Ce sont des composants qui peuvent être facilement remplacés par des alternatives. Chaque composant (un LLM, un modèle de discussion, un analyseur de sortie, etc. (nous y reviendrons prochainement) suit une spécification partagée, ce qui rend votre application évolutive. À mesure que de nouvelles fonctionnalités sont publiées par les fournisseurs de modèles et que vos besoins évoluent, vous pouvez faire évoluer votre application sans la réécrire à chaque fois.

Tout au long de ce livre, nous utilisons les principaux composants suivants dans les exemples de code :

- Modèle LLM/chat : OpenAI
- Intégrations : OpenAI
- Magasin de vecteurs : PGVector

Vous pouvez remplacer chacun d’entre eux par l’une des alternatives répertoriées sur les pages suivantes :

#### *Modèles de discussion*

<span id="page-47-5"></span><span id="page-47-4"></span><span id="page-47-1"></span><span id="page-47-0"></span>Voir la [documentation] de LangChain(https://oreil.ly/8Qlnb). Si vous ne souhaitez pas utiliser OpenAI (une API commerciale), nous vous suggérons [Anthropic](https://oreil.ly/XdGfD) comme alternative commerciale ou [Ollama](https://oreil.ly/eKy6-) comme alternative open source.

#### *Intégrations*

<span id="page-47-3"></span><span id="page-47-2"></span>Voir la [documentation] LangChain (https://oreil.ly/sKpfM). Si vous ne souhaitez pas utiliser OpenAI (une API commerciale), nous vous suggérons [Cohere](https://oreil.ly/o1D0C) comme alternative commerciale ou [Ollama](https://oreil.ly/FarfL) comme alternative open source.

*Magasins vectoriels*

<span id="page-48-3"></span><span id="page-48-2"></span><span id="page-48-0"></span>Voir la [documentation] de LangChain(https://oreil.ly/q3RF1). Si vous ne souhaitez pas utiliser PGVector (une extension open source de la base de données SQL populaire Postgres), nous vous suggérons d'utiliser soit [Weaviate](https://oreil.ly/XqlYa) (un magasin de vecteurs dédié) ou [OpenSearch](https://oreil.ly/1s357) (fonctionnalités de recherche de vecteurs qui font partie d'une base de données de recherche populaire).
Cet effort va au-delà, par exemple, du fait que tous les LLM ont les mêmes méthodes, avec des arguments et des valeurs de retour similaires. Regardons l'exemple des modèles de chat et de deux fournisseurs LLM populaires, OpenAI et Anthropic. Les deux ont une API de chat qui reçoit des *messages de chat* (vaguement définis comme des objets avec une chaîne de type et une chaîne de contenu) et renvoie un nouveau message généré par le modèle. Mais si vous essayez d'utiliser les deux modèles dans la même conversation, vous rencontrerez immédiatement des problèmes, car leurs formats de messages de discussion sont subtilement incompatibles. LangChain élimine ces différences pour permettre de créer des applications véritablement indépendantes d'un fournisseur particulier. Par exemple, avec LangChain, une conversation de chatbot dans laquelle vous utilisez à la fois les modèles OpenAI et Anthropic fonctionne.

<span id="page-48-1"></span>Enfin, lorsque vous développez vos applications LLM avec plusieurs de ces composants, nous avons trouvé utile de disposer des capacités *d'orchestration* de LangChain :

- Tous les composants majeurs sont instrumentés par le système de rappels pour l'observabilité (plus d'informations à ce sujet dans le [Chapitre](#page-385-0) 8).
- Tous les composants majeurs implémentent la même interface (nous en parlerons plus à la fin de ce chapitre).
- <span id="page-49-0"></span>Les applications LLM de longue durée peuvent être interrompues, reprises ou réessayées (plus d'informations à ce sujet dans le [Chapitre](#page-315-0) 6).

## Configuration avec LangChain

<span id="page-49-1"></span>Pour suivre le reste du chapitre et les chapitres à venir, nous vous recommandons de configurer d'abord LangChain sur votre ordinateur.

<span id="page-49-2"></span>Consultez les instructions dans la [Préface](#page-8-0) concernant la configuration d'un compte OpenAI et complétez-les si vous ne l'avez pas encore fait. Si vous préférez utiliser un autre fournisseur LLM, consultez « Pourquoi [LangChain ? »](#page-46-0) pour des alternatives.

Rendez-vous ensuite sur la page Clés API (https://oreil.ly/BKrtV) sur le site Web d'OpenAI (après vous être connecté à votre compte OpenAI), créez une clé API et enregistrez-la : vous en aurez bientôt besoin.

#### **REMARQUE**

Dans ce livre, nous présenterons des exemples de code en Python et en JavaScript (JS). LangChain offre les mêmes fonctionnalités dans les deux langues, alors choisissez simplement celle avec laquelle vous êtes le plus à l'aise et suivez les extraits de code respectifs tout au long du livre (les exemples de code pour chaque langue sont équivalents).

<span id="page-50-0"></span>Tout d'abord, quelques instructions de configuration pour les lecteurs utilisant Python :

- 1. Assurez-vous que Python [est installé. Voir](https://oreil.ly/20K9l) les instructions de votre système d'exploitation.
- 2. Installez Jupyter si vous souhaitez exécuter les exemples dans un environnement de notebook. Vous pouvez le faire en exécutant pip install notebook dans votre terminal.
- 3. Installez la bibliothèque LangChain en exécutant les commandes suivantes dans votre terminal :

pip installer langchain langchain-openai langchai pip installer langchain-text-splitters langchain-

4. Prenez la clé API OpenAI que vous avez générée au début de cette section et rendez-la disponible dans votre environnement de terminal. Vous pouvez le faire en exécutant ce qui suit :

```
export OPENAI_API_KEY=your-key
```
- 5. N'oubliez pas de remplacer votre clé par la clé API que vous avez générée précédemment.
- 6. Ouvrez un notebook Jupyter en exécutant cette commande :

<span id="page-51-0"></span>carnet Jupyter

Vous êtes maintenant prêt à suivre les exemples de code Python.

Voici les instructions pour les lecteurs utilisant JavaScript :

1. Prenez la clé API OpenAI que vous avez générée au début de cette section et rendez-la disponible dans votre environnement de terminal. Vous pouvez le faire en exécutant ce qui suit :

```
export OPENAI_API_KEY=your-key
```
2. N'oubliez pas de remplacer votre clé par la clé API que vous avez générée précédemment.

- 3. Si vous souhaitez exécuter les exemples sous forme de scripts Node.js, installez Node en suivant les [instructions](https://oreil.ly/5gjiO).
- 4. Installez les bibliothèques LangChain en exécutant les commandes suivantes dans votre terminal :

npm install langchain @langchain/openai @langch npm install @langchain/core pg

5. Prenez chaque exemple, enregistrez-le en tant que fichier *.js* et exécutez-le avec node ./file.js .

## Utilisation des LLM dans LangChain

<span id="page-52-1"></span><span id="page-52-0"></span>Pour récapituler, les LLM sont le moteur de la plupart des applications d'IA générative. LangChain fournit deux interfaces simples pour interagir avec n'importe quel fournisseur d'API LLM :

- Modèles de discussion
- LLM

L'interface LLM prend simplement une invite de chaîne en entrée, envoie l'entrée au fournisseur de modèle, puis renvoie la prédiction du modèle en sortie.
<span id="page-53-0"></span>Importons le wrapper OpenAI LLM de LangChain pour invoquer une prédiction de modèle à l'aide d'une simple invite :

<span id="page-53-2"></span>*Python*

```
from langchain_openai.llms import OpenAI
```

```
model = OpenAI(model="gpt-3.5-turbo")
```

```
model.invoke("The sky is")
```
*JavaScript*

```
import { OpenAI } from "@langchain/openai";
const model = new OpenAI({ model: "gpt-3.5-turbo"
await model.invoke("The sky is");
```
*La sortie :*

Bleu !

#### **CONSEIL**

<span id="page-54-2"></span>Remarquez le modèle de paramètres transmis à OpenAI . Il s'agit du paramètre le plus courant à configurer lors de l'utilisation d'un modèle LLM ou de chat, le modèle sous-jacent à utiliser, car la plupart des fournisseurs proposent plusieurs modèles avec différents compromis en termes de capacité et de coût (généralement les modèles plus grands sont plus performants, mais aussi plus chers et plus lents). Voir la [aperçu](https://oreil.ly/dM886) d'OpenAI des modèles qu'ils proposent.

D'autres paramètres utiles à configurer sont les suivants, proposés par la plupart des fournisseurs.

#### *température*

<span id="page-54-4"></span><span id="page-54-3"></span>Cela contrôle l'algorithme d'échantillonnage utilisé pour générer la sortie. Des valeurs inférieures produisent des résultats plus prévisibles (par exemple, 0,1), tandis que des valeurs plus élevées génèrent des résultats plus créatifs ou inattendus (tels que 0,9). Différentes tâches nécessiteront des valeurs différentes pour ce paramètre. Par exemple, la production d’un résultat structuré bénéficie généralement d’une température plus basse, tandis que les tâches d’écriture créative fonctionnent mieux avec une valeur plus élevée :

#### *max\_jetons*

<span id="page-54-1"></span>Cela limite la taille (et le coût) de la sortie. Une valeur inférieure peut amener le LLM à cesser de générer la sortie avant d'arriver à sa fin naturelle, de sorte qu'elle peut sembler avoir été tronquée.

Au-delà de ceux-ci, chaque fournisseur expose un ensemble différent de paramètres. Nous vous recommandons de consulter la documentation de celui que vous choisissez. Pour un exemple, reportez-vous à la plateforme [OpenAI](https://oreil.ly/5O1RW).

<span id="page-54-0"></span>Alternativement, l'interface du modèle de chat permet des conversations aller-retour entre l'utilisateur et le modèle. La raison pour laquelle il s'agit d'une interface distincte est que les fournisseurs LLM populaires comme OpenAI différencient les messages envoyés vers et depuis le modèle en rôles *user*, *assistant* et *system* (ici *role* désigne le type de contenu que le message contient) :

#### *Rôle système*

<span id="page-55-3"></span><span id="page-55-2"></span>Utilisé pour les instructions que le modèle doit utiliser pour répondre à une question de l'utilisateur

#### *Rôle utilisateur*

<span id="page-55-4"></span>Utilisé pour la requête de l'utilisateur et tout autre contenu produit par l'utilisateur

#### *Rôle d'assistant*

<span id="page-55-0"></span>Utilisé pour le contenu généré par le modèle

L'interface du modèle de chat facilite la configuration et la gestion des conversions dans votre application de chatbot IA. Voici un exemple utilisant le modèle ChatOpenAI de LangChain :

<span id="page-55-1"></span>*Python*

depuis langchain\_openai.chat\_models importer ChatOpen depuis langchain\_core.messages importer HumanMessage

```
model = ChatOpenAI()
prompt = [HumanMessage("What is the capital of Fr
model.invoke(prompt)
```
<span id="page-56-1"></span>*JavaScript*

```
import { ChatOpenAI } from '@langchain/openai'
import { HumanMessage } from '@langchain/core/mes
const model = new ChatOpenAI()
const prompt = [new HumanMessage('What is the cap
await model.invoke(prompt)
```
*La sortie :*

```
AIMessage(content='The capital of France is Paris
```
<span id="page-56-0"></span>Au lieu d'une seule chaîne d'invite, les modèles de chat utilisent différents types d'interfaces de message de chat associées à chaque rôle mentionné précédemment. Ceux-ci incluent les éléments suivants :

*Message humain*

<span id="page-57-2"></span>Un message envoyé du point de vue de l'humain, avec le rôle d'utilisateur

#### *Message AI*

<span id="page-57-0"></span>Un message envoyé du point de vue de l'IA avec laquelle l'humain interagit, avec le rôle d'assistant

#### *Message système*

<span id="page-57-4"></span>Un message définissant les instructions que l'IA doit suivre, avec le rôle système

*Message de discussion*

<span id="page-57-1"></span>Un message permettant une définition arbitraire du rôle

Incorporons une instruction SystemMessage dans notre exemple :

#### <span id="page-57-3"></span>*Python*

```
from langchain_core.messages import HumanMessage,
from langchain_openai.chat_models import ChatOpen
model = ChatOpenAI()
system_msg = SystemMessage(
```

```
 '''Vous êtes un assistant utile qui répond 
 points d'exclamation.'''
)
human_msg = HumanMessage('Quelle est la capitale de
modèle.invoke([system_msg, human_msg])
```
<span id="page-58-0"></span>*JavaScript*

```
importer { ChatOpenAI } depuis "@langchain/openai" ;
importer { HumanMessage, SystemMessage } depuis "@lan
modèle const = new ChatOpenAI();
invite const = [
 nouveau message système (
 `You are a helpful assistant that responds to
 exclamation marks.`,
 ),
 new HumanMessage("Quelle est la capitale de la France
];
wait model.invoke(prompt);
```
*The output:*

```
AIMessage('Paris!!!')
```
As you can see, the model obeyed the instruction provided in the SystemMessage even though it wasn't present in the user's question. This enables you to preconfigure your AI application to respond in a relatively predictable manner based on the user's input.

## <span id="page-59-1"></span>Making LLM Prompts Reusable

<span id="page-59-0"></span>The previous section showed how the prompt instruction significantly influences the model's output. Prompts help the model understand context and generate relevant answers to queries.

<span id="page-59-2"></span>Here is an example of a detailed prompt:

Answer the question based on the context below. I answered using the information provided, answer w

Context: The most recent advancements in NLP are Models (LLMs). These models outperform their smal become invaluable for developers who are creating

biliti D l t i t th d l

```
capacités. Les développeurs peuvent exploiter ces modèles
`transformers` bibliothèque, ou en utilisant OpenAI et
les bibliothèques `openai` et `cohere`, respectivement
Question : Quels fournisseurs de modèles proposent des LLM ?
Réponse :
```
Although the prompt looks like a simple string, the challenge is figuring out what the text should contain and how it should vary based on the user's input. In this example, the Context and Question values are hardcoded, but what if we wanted to pass these in dynamically?

<span id="page-60-0"></span>Fortunately, LangChain provides prompt template interfaces that make it easy to construct prompts with dynamic inputs:

<span id="page-60-1"></span>*Python*

```
à partir de langchain_core.prompts, importez PromptTemplate
template = PromptTemplate.from_template("""Réponse
 contexte ci-dessous. Si la question ne peut pas trouver de réponse
 fourni, répondez par "Je ne sais pas".
```
Context: {context}

```
Question : {question}
Réponse : """)
modèle.invoke({
 "context": """Les avancées les plus récentes en
 Modèles de langage (LLM). Ces modèles sont sortis
 homologues et sont devenus une valeur inestimable f
 applications avec des capacités NLP. Développer
 modèles via `transforme
 OpenAI and Cohere's offerings through the
 libraries, respectively.""",
 "question": "Which model providers offer LLMs
})
__PROTECTED_CODE_5__
import { PromptTemplate } from '@langchain/core/p
__PROTECTED_CODE_6__
Context: {context}
Question: {question}
Answer: ` de Hugging Face)
attendre modèle.invoke({
 contexte : `The most recent advancements in NLP a
 Language Models (LLMs). These models outperfo
 counterparts and have become invaluable for d
 applications with NLP capabilities. Developer
 through Hugging Face's \`transformers\` libra
 and Cohere's offerings through the \`openai\`
 respectively.`,
 question : « Quels fournisseurs de modèles proposent des LLM ? »
})
```
#### *The output:*

StringPromptValue(text='Answer the question based question cannot be answered using the informa don\'t know".\n\nContext: The most recent adv driven by Large Language Models (LLMs). These smaller counterparts and have become invaluab creating applications with NLP capabilities. models through Hugging Face\'s `transformateurs` OpenAI and Cohere\'s offerings through the `o

 Offres OpenAI et Cohere via o respectivement.\n\nQuestion : Quel modèle fournit

Cet exemple reprend l'invite statique du bloc précédent et la rend dynamique. Le modèle contient la structure de l'invite finale ainsi que la définition de l'endroit où les entrées dynamiques seront insérées.

En tant que tel, le modèle peut être utilisé comme recette pour créer plusieurs invites statiques et spécifiques. Lorsque vous formatez l'invite avec certaines valeurs spécifiques (dans ce cas, le contexte et la question), vous obtenez une invite statique prête à être transmise à un LLM.
<span id="page-63-3"></span><span id="page-63-1"></span><span id="page-63-0"></span>Comme vous pouvez le voir, l'argument de la question est passé dynamiquement via la fonction d'invocation. Par défaut, les invites LangChain suivent la syntaxe f-string de Python pour définir les paramètres dynamiques. Tout mot entouré d'accolades, tels que {question} , sont des espaces réservés pour les valeurs transmises lors de l'exécution. Dans l'exemple précédent, {question} a été remplacé par « Quels fournisseurs de modèles proposent des LLM ? »

Voyons comment nous intégrerions cela dans un modèle LLM OpenAI à l'aide de LangChain :

<span id="page-63-2"></span>*Python*

```
from langchain_openai.llms import OpenAI
from langchain_core.prompts import PromptTemplate
```

```
# both `template` and `model` can be reused many
```

```
template = PromptTemplate.from_template("""Answer
 context below. If the question cannot be answ
 provided, answer with "I don't know".
```
Contexte : {contexte}

Question : {question}

Réponse : """)

modèle = OpenAI()

# `prompt` et `completion` sont nos résultats

invite = modèle.invoke({

 "context": """Les avancées les plus récentes en matière de modèles de langage (LLM). Ces modèles surpassent leurs homologues et sont devenus des applications inestimables dotées de capacités PNL. Développez des modèles grâce aux `transforme OpenAI and Cohere's offerings through the libraries, respectively.""",

"question": "Which model providers offer LLMs

__PROTECTED_CODE_3__
#### <span id="page-65-0"></span>*JavaScript*

__PROTECTED_CODE_4__

__PROTECTED_CODE_5__
*The output:*

__PROTECTED_CODE_6__
If you're looking to build an AI chat application, the ChatPromptTemplate can be used instead to provide dynamic inputs based on the role of the chat message:

<span id="page-66-1"></span>*Python*

__PROTECTED_CODE_7__

__PROTECTED_CODE_8__
#### <span id="page-67-0"></span>*JavaScript*

__PROTECTED_CODE_9__
![](_page_68_Picture_0.jpeg)

#### *The output:*

ChatPromptValue(messages=[SystemMessage(content= the context below. If the question cannot be provided, answer with "I don\'t know".'), Hum The most recent advancements in NLP are being Models (LLMs). These models outperform their become invaluable for developers who are crea capabilities. Developers can tap into these m `transformers` library, or by utilizing OpenA

 through the `openai` and `cohere` libraries, (content='Question: Which model providers off

Notice how the prompt contains instructions in a SystemMessage and two instances of HumanMessage that contain dynamic context and question variables. You can still format the template in the same way and get back a static prompt that you can pass to a large language model for a prediction output:

#### *Python*

``` de Hugging Face.
depuis langchain_openai.chat_models importer ChatOpen
à partir de langchain_core.prompts, importez ChatPromptTemp
# `template` et `model` peuvent être réutilisés à plusieurs reprises 
modèle = ChatPromptTemplate.from_messages([
 (« système », «   Répondez à la question en fonction du
 on ne peut pas répondre à la question en utilisant l'information
 avec "Je ne sais pas".'''),
 ("humain", "Contexte : {contexte}"),
 (« humain », « Question : {question} »),
])
modèle = ChatOpenAI()
# `prompt` et `completion` sont nos résultats
invite = appel de modèle ({
```

```
invite = modèle.invoke({
 "context": """Les avancées les plus récentes en
 Grands modèles de langage (LLM). Ces modèles
 homologues et sont devenus une valeur inestimable f
 applications avec des capacités NLP. Développer
 modèles via `transforme
 OpenAI and Cohere's offerings through the
 libraries, respectively.""",
 "question": "Which model providers offer LLMs
})
model.invoke(prompt)
__PROTECTED_CODE_1__
import { ChatPromptTemplate } from '@langchain/co
import { ChatOpenAI } from '@langchain/openai'
const model = new ChatOpenAI()
const template = ChatPromptTemplate.fromMessages(
 ['system', ` de Hugging Face Répondez à la question en fonction du co
 on ne peut pas répondre en utilisant les informations fournies
 je ne sais pas".`],
 ['human', 'Context: {context}'],
 ['human', 'Question: {question}'],
])
__PROTECTED_CODE_2__
const prompt = await template.invoke({
 context: `Les avancées les plus récentes en PNL a
 Modèles de langage (LLM). Ces modèles surpassent
 homologues et sont devenus inestimables pour d
 applications avec des capacités NLP. Développeur
 à travers la Balance \`transformers\` de Hugging Face
 et les offres de Cohere via le \`openai\`
 respectivement.`,
 question: "Which model providers offer LLMs?"
})
await model.invoke(prompt)
__PROTECTED_CODE_3__
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel
class AnswerWithJustification(BaseModel):
 '''An answer to the user's question along wit
 answer.'''
 answer: str
 '''The answer to the user's question'''
__PROTECTED_CODE_4__
 justification: str
 '''Justification for the answer'''
__PROTECTED_CODE_5__
llm = ChatOpenAI(model="gpt-3.5-turbo", temperatu
structured_llm = llm.with_structured_output(Answe
__PROTECTED_CODE_6__
structured_llm.invoke("""What weighs more, a poun
 of feathers""")
__PROTECTED_CODE_7__
import { ChatOpenAI } from '@langchain/openai'
import { z } from "zod";
const answerSchema = z
 .object({
 answer: z.string().describe("The answer to th
 justification: z.string().describe(`Justifica
 réponse`),
 })
 .describe(`Une réponse à la question de l'utilisateur également
 la réponse.`);
const model = new ChatOpenAI({
 model: "gpt-3.5-turbo",
 temperature: 0,
}) withStructuredOutput(answerSchema)
__PROTECTED_CODE_8__
}).withStructuredOutput(answerSchema)
await model.invoke("What weighs more, a pound of
__PROTECTED_CODE_9__
{
 answer: "They weigh the same",
 justification: "Both a pound of bricks and a po
 The weight is the same, but the volu"... 42 m
}
```
<span id="page-74-1"></span><span id="page-74-0"></span>Donc, définissez d'abord un schéma. En Python, c'est plus simple à faire avec Pydantic (une bibliothèque utilisée pour valider les données par rapport aux schémas). En JS, c'est plus simple à faire avec Zod (une bibliothèque équivalente). La méthode with\_structured\_output utilisera ce schéma pour deux choses :

- Le schéma sera converti en un objet JSONSchema (un format JSON utilisé pour décrire la forme [types, noms, descriptions] des données JSON), qui sera envoyé au LLM. Pour chaque LLM, LangChain sélectionne la meilleure méthode pour ce faire, généralement un appel de fonction ou une invite.
- Le schéma sera également utilisé pour valider la sortie renvoyée par le LLM avant de la renvoyer ; cela garantit la sortie

produit respecte exactement le schéma que vous avez transmis.

### **Autres formats lisibles par machine avec analyseurs de sortie**

<span id="page-75-3"></span><span id="page-75-2"></span><span id="page-75-0"></span>Vous pouvez également utiliser un modèle LLM ou de chat pour produire une sortie dans d'autres formats, tels que CSV ou XML. C'est là que les analyseurs de sortie s'avèrent utiles. Les *analyseurs de sortie* sont des classes qui vous aident à structurer les grandes réponses d'un modèle de langage. Ils remplissent deux fonctions :

#### *Fournir des instructions de format*

<span id="page-75-1"></span>Les analyseurs de sortie peuvent être utilisés pour injecter des instructions supplémentaires dans l'invite qui aideront le LLM à sortir le texte dans le format qu'il sait analyser.

#### *Validation et analyse de la sortie*

La fonction principale est de prendre la sortie textuelle du modèle LLM ou de discussion et de la restituer dans un format plus structuré, tel qu'une liste, XML ou un autre format. Cela peut inclure la suppression des informations superflues, la correction des sorties incomplètes et la validation des valeurs analysées.

Voici un exemple du fonctionnement d'un analyseur de sortie :

#### <span id="page-76-2"></span>*Python*

```
from langchain_core.output_parsers import CommaSe
parser = CommaSeparatedListOutputParser()
items = parser.invoke("apple, banana, cherry")
```
<span id="page-76-1"></span>*JavaScript*

```
import { CommaSeparatedListOutputParser } from '@
const parser = new CommaSeparatedListOutputParser
await parser.invoke("apple, banana, cherry")
```
*La sortie :*

```
['apple', 'banana', 'cherry']
```
LangChain fournit une variété d'analyseurs de sortie pour divers cas d'utilisation, notamment CSV, XML, etc. Nous verrons comment combiner les analyseurs de sortie avec des modèles et des invites dans la section suivante.

# Assemblage des nombreux éléments d'une candidature LLM

<span id="page-77-2"></span>Les composants clés que vous avez découverts jusqu'à présent sont des éléments essentiels du framework LangChain. Ce qui nous amène à la question cruciale : comment les combiner efficacement pour créer votre application LLM ?

### **Utilisation de l'interface Runnable**

<span id="page-77-3"></span><span id="page-77-1"></span>Comme vous l'avez peut-être remarqué, tous les exemples de code utilisés jusqu'à présent utilisent une interface similaire et la méthode Invoke() pour générer des sorties à partir du modèle (ou du modèle d'invite ou de l'analyseur de sortie). Tous les composants ont les éléments suivants :

- <span id="page-77-0"></span>Il existe une interface commune avec ces méthodes :
	- Invoquer : transforme une seule entrée en une sortie
	- batch : transforme efficacement plusieurs entrées en plusieurs sorties
	- stream : diffuse la sortie d'une seule entrée au fur et à mesure de sa production
- Il existe des utilitaires intégrés pour les tentatives, les solutions de repli, les schémas et la configurabilité de l'exécution.

En Python, chacune des trois méthodes a des équivalents asyncio.

Ainsi, tous les composants se comportent de la même manière, et l’interface apprise pour l’un d’eux s’applique à tous :

<span id="page-78-1"></span>*Python*

```
from langchain_openai.llms import ChatOpenAI
model = ChatOpenAI()
completion = model.invoke('Hi there!')
# Hi!
completions = model.batch(['Hi there!', 'Bye!'])
# ['Hi!', 'See you!']
for token in model.stream('Bye!'):
 print(token)
 # Good
 # bye
 # !
```
<span id="page-78-0"></span>*JavaScript*

```
import { ChatOpenAI } from '@langchain/openai'
const model = new ChatOpenAI()
const completion = await model.invoke('Hi there!
// Hi!
const completions = await model.batch(['Hi there
// ['Hi!', 'See you!']
for await (const token of await model.stream('Bye
 console.log(token)
 // Good
 // bye
 // !
}
```
Dans cet exemple, vous voyez comment fonctionnent les trois méthodes principales :

- Invoquer() prend une seule entrée et renvoie une seule sortie.
- batch() prend une liste de sorties et renvoie une liste de sorties.
- stream() prend une seule entrée et renvoie un itérateur de parties de la sortie dès qu'elles deviennent disponibles.

Dans certains cas, où le composant sous-jacent ne prend pas en charge la sortie itérative, il y aura une seule partie contenant toute la sortie.

Vous pouvez combiner ces composants de deux manières :

#### *Impératif*

```
Call your components directly, for example, with
model.invoke(...)
```
*Déclaratif*

<span id="page-80-1"></span>Utiliser le langage d'expression LangChain (LCEL), comme expliqué dans une prochaine section

Le <span id="page-80-0"></span>[Table](#page-81-0) 1-1 résume leurs différences, et nous verrons chacun en action ensuite.

|                       | Impératif | Déclaratif |
|-----------------------|------------------------------------------------------------------------------------------|-------------|
| Syntaxe | Tout<br>Python<br>ou<br>JavaScript | LCEL |
| Exécution parallèle | Python :<br>avec<br>threads<br>ou<br>coroutines<br>JavaScript :<br>avec<br>Promise.al<br>l | Automatique |
| Diffusion | Avec<br>rendement<br>mot-clé | Automatique |
| Exécution asynchrone | Avec<br>fonctions asynchrones<br> | Automatique |

<span id="page-81-0"></span>Tableau 1-1. Les principales différences entre la composition impérative et déclarative.

### **Composition impérative**

<span id="page-81-1"></span>*Composition impérative* n'est qu'un nom sophistiqué pour écrire le code que vous avez l'habitude d'écrire, en composant ces composants en fonctions et classes. Voici un exemple combinant des invites, des modèles et des analyseurs de sortie :

<span id="page-81-2"></span>*Python*

depuis langchain\_openai.chat\_models importer ChatOpen depuis langchain core.prompts importer ChatPromptTemp

```
from langchain_core.runnables import chain
# the building blocks
template = ChatPromptTemplate.from_messages([
 ('system', 'You are a helpful assistant.'),
 ('human',
              '{question}'),
])
model = ChatOpenAI()
# combine them in a function
# @chain decorator adds the same Runnable interfa
@chain
def chatbot(values):
 prompt = template.invoke(values)
 return model.invoke(prompt)
# use it
chatbot.invoke({"question": "Which model provider
```
o a gc a \_co e p o pts pot C at o pt e p

<span id="page-82-0"></span>*JavaScript*

importer {ChatOpenAI} depuis '@langchain/openai'

```
import {ChatOpenAI} from '@langchain/openai'
import {ChatPromptTemplate} from '@langchain/core
import {RunnableLambda} from '@langchain/core/run
// the building blocks
const template = ChatPromptTemplate.fromMessages(
 ['system', 'You are a helpful assistant.'],
 ['human', '{question}'],
])
const model = new ChatOpenAI()
// combine them in a function
// RunnableLambda adds the same Runnable interfac
const chatbot = RunnableLambda.from(async values
 const prompt = await template.invoke(values)
 return await model.invoke(prompt)
})
// use it
await chatbot.invoke({
 "question": "Which model providers offer LLMs?"
})
```
*La sortie :*

```
AIMessage(content="Hugging Face's `transformers` 
 `openai` library, and Cohere using the `coher
```
Ce qui précède est un exemple complet de chatbot, utilisant un modèle d'invite et de chat. Comme vous pouvez le constater, il utilise la syntaxe Python familière et prend en charge toute logique personnalisée que vous souhaiterez peut-être ajouter à cette fonction.

D'un autre côté, si vous souhaitez activer la prise en charge du streaming ou de l'asynchrone, vous devrez modifier votre fonction pour la prendre en charge. Par exemple, la prise en charge du streaming peut être ajoutée comme suit :

<span id="page-84-0"></span>*Python*

```
@chain
def chatbot(values):
 prompt = template.invoke(values)
 for token in model.stream(prompt):
 yield token
for part in chatbot.stream({
 "question": "Which model providers offer LLMs
```

```
}):
 print(part)
```
<span id="page-85-0"></span>*JavaScript*

```
const chatbot = RunnableLambda.from(async functio
 const prompt = await template.invoke(values)
 for await (const token of await model.stream(pr
 yield token
 }
})
for await (const token of await chatbot.stream({
 "question": "Which model providers offer LLMs?"
})) {
 console.log(token)
}
```
*La sortie :*

```
AIMessageChunk(content="Hugging")
AIMessageChunk(content=" Face's")
```

```
AIMessageChunk(content=" `transformers`")
...
```
Ainsi, que ce soit en JS ou en Python, vous pouvez activer le streaming pour votre fonction personnalisée en fournissant les valeurs que vous souhaitez diffuser, puis en l'appelant avec stream .

<span id="page-86-0"></span>Pour une exécution asynchrone, vous réécrivez votre fonction comme ceci :

<span id="page-86-3"></span>*Python*

```
@chain
async def chatbot(values):
 prompt = await template.ainvoke(values)
 return await model.ainvoke(prompt)
await chatbot.ainvoke({"question": "Which model p
# > AIMessage(content="""Hugging Face's `transfor
 the `openai` library, and Cohere using the `c
```
<span id="page-86-2"></span><span id="page-86-1"></span>Celui-ci s'applique uniquement à Python, car l'exécution asynchrone est la seule option en JavaScript.

### **Composition déclarative**
<span id="page-87-1"></span><span id="page-87-0"></span>LCEL est un *langage déclaratif* pour composer des composants LangChain. LangChain compile les compositions LCEL selon un *plan d'exécution optimisé*, avec parallélisation automatique, streaming, traçage et prise en charge asynchrone.

Voyons le même exemple utilisant LCEL :

<span id="page-87-2"></span>*Python*

```
from langchain_openai.chat_models import ChatOpen
from langchain_core.prompts import ChatPromptTemp
# the building blocks
template = ChatPromptTemplate.from_messages([
 ('system', 'You are a helpful assistant.'),
 ('human',
              '{question}'),
])
model = ChatOpenAI()
# combine them with the | operator
chatbot = template | model
```

```
# use it
```
chatbot.invoke({"question": "Quel fournisseur de modèles

#### <span id="page-88-0"></span>*JavaScript*

```
import { ChatOpenAI } from '@langchain/openai'
import { ChatPromptTemplate } from '@langchain/co
import { RunnableLambda } from '@langchain/core/r
// the building blocks
const template = ChatPromptTemplate.fromMessages(
 ['system', 'You are a helpful assistant.'],
 ['human', '{question}'],
])
const model = new ChatOpenAI()
// combine them in a function
const chatbot = template.pipe(model)
// use it
```

```
await chatbot.invoke({
 "question": "Which model providers offer LLMs?"
})
```
*La sortie :*

```
AIMessage(content="Hugging Face's `transformers` 
 `openai` library, and Cohere using the `coher
```
Surtout, la dernière ligne est la même entre les deux exemples, c'est-à-dire que vous utilisez la fonction et la séquence LCEL de la même manière, avec Invoke/stream/batch . Et dans cette version, vous n'avez rien d'autre à faire pour utiliser le streaming :

<span id="page-89-0"></span>*Python*

```
chatbot = template | model
for part in chatbot.stream({
 "question": "Which model providers offer LLMs
}):
 print(part)
 # > AIMessageChunk(content="Hugging")
```
![](_page_90_Figure_0.jpeg)

<span id="page-90-0"></span>*JavaScript*

```
const chatbot = template.pipe(model)
for await (const token of await chatbot.stream({
 "question": "Which model providers offer LLMs?"
})) {
 console.log(token)
}
```
Et, pour Python uniquement, c'est la même chose pour l'utilisation de méthodes asynchrones :

*Python*

```
chatbot = template | model
await chatbot.ainvoke({
 "question": "Which model providers offer LLMs
})
```
## Résumé

<span id="page-91-1"></span>Dans ce chapitre, vous avez découvert les éléments de base et les composants clés nécessaires pour créer des applications LLM à l'aide de LangChain. Les applications LLM sont essentiellement une chaîne composée d'un grand modèle de langage pour effectuer des prédictions, de la ou des instructions d'invite pour guider le modèle vers un résultat souhaité et d'un analyseur de sortie facultatif pour transformer le format de la sortie du modèle.

<span id="page-91-0"></span>Tous les composants LangChain partagent la même interface avec les méthodes Invoke , Stream et Batch pour gérer diverses entrées et sorties. Ils peuvent être soit combinés et exécutés impérativement en les appelant directement, soit de manière déclarative à l'aide de LCEL.

<span id="page-91-2"></span>L'approche impérative est utile si vous avez l'intention d'écrire beaucoup de logique personnalisée, tandis que l'approche déclarative est utile pour simplement assembler des composants existants avec une personnalisation limitée.

Dans le [Chapitre](#page-93-0) 2, vous apprendrez comment fournir des données externes à votre chatbot IA en tant que *contexte* afin que vous puissiez créer une application LLM.

qui vous permet de « discuter » avec vos données.

## <span id="page-93-0"></span>Chapitre 2. RAG Partie I : Indexation de vos données

Dans le chapitre précédent, vous avez découvert les éléments de base importants utilisés pour créer une application LLM à l'aide de LangChain. Vous avez également créé un chatbot IA simple composé d'une invite envoyée au modèle et de la sortie générée par le modèle. Mais ce simple chatbot présente des limites majeures.

<span id="page-93-1"></span>Que se passe-t-il si votre cas d'utilisation nécessite des connaissances sur lesquelles le modèle n'a pas été formé ? Par exemple, disons que vous souhaitez utiliser l’IA pour poser des questions sur une entreprise, mais que les informations sont contenues dans un PDF privé ou un autre type de document. Bien que nous ayons vu des fournisseurs de modèles enrichir leurs ensembles de données de formation pour inclure de plus en plus d'informations publiques mondiales (quel que soit le format dans lequel elles sont stockées), deux limitations majeures continuent d'exister dans le corpus de connaissances de LLM :

#### *Données privées*

<span id="page-93-3"></span><span id="page-93-2"></span>Les informations qui ne sont pas accessibles au public ne sont, par définition, pas incluses dans les données de formation des LLM.

*Événements actuels*
<span id="page-94-0"></span>La formation d'un LLM est un processus coûteux et long qui peut s'étendre sur plusieurs années, la collecte de données étant l'une des premières étapes. Il en résulte ce qu'on appelle le seuil de connaissance, ou une date au-delà de laquelle le LLM n'a aucune connaissance des événements du monde réel ; il s'agit généralement de la date à laquelle l'ensemble de formation est finalisé. Cela peut remonter de quelques mois à quelques années, selon le modèle en question.

<span id="page-94-3"></span><span id="page-94-2"></span>Dans les deux cas, le modèle aura très probablement des hallucinations (trouvera des informations trompeuses ou fausses) et répondra avec des informations inexactes. L'adaptation de l'invite ne résoudra pas non plus le problème car elle repose sur les connaissances actuelles du modèle.

## L'objectif : choisir un contexte pertinent pour les LLM

<span id="page-94-1"></span>Si les seules données privées/actuelles dont vous aviez besoin pour votre cas d'utilisation LLM étaient une à deux pages de texte, ce chapitre serait beaucoup plus court : tout ce dont vous auriez besoin pour rendre ces informations disponibles au LLM est d'inclure l'intégralité de ce texte dans chaque invite que vous avez envoyée au modèle.

Le défi de la mise à disposition des données aux LLM est avant tout un problème de quantité. Vous disposez de plus d’informations que ne peut en contenir chaque invite que vous envoyez au LLM. Quel petit sous-ensemble de votre grande collection de texte incluez-vous chaque fois que vous appelez le modèle ? Ou en d’autres termes, comment choisir (à l’aide du modèle) quel texte est le plus pertinent pour répondre à chaque question ?

Dans ce chapitre et le suivant, vous apprendrez comment relever ce défi en deux étapes :

- 1. *Indexer* vos documents, c'est-à-dire les prétraiter de manière à ce que votre candidature puisse facilement trouver les plus pertinents pour chaque question
- <span id="page-95-3"></span><span id="page-95-2"></span><span id="page-95-0"></span>2. *Récupérer* ces données externes de l'index et les utiliser comme *contexte* pour le LLM afin de générer une sortie précise basée sur vos données

<span id="page-95-4"></span><span id="page-95-1"></span>Ce chapitre se concentre sur l'indexation, la première étape, qui implique le prétraitement de vos documents dans un format qui peut être compris et recherché avec les LLM. Cette technique est appelée *génération augmentée par récupération* (RAG). Mais avant de commencer, discutons des *pourquoi* vos documents nécessitent un prétraitement.

Supposons que vous souhaitiez utiliser les LLM pour analyser les performances financières et les risques dans le rapport [annuel](https://oreil.ly/Bp51E) 2022 de Tesla, qui est stocké sous forme de texte au format PDF. Votre objectif est de pouvoir poser une question telle que « À quels principaux risques Tesla a-t-il été confronté en 2022 ? » et obtenez une réponse humaine basée sur le contexte de la section sur les facteurs de risque du document.

En le décomposant, vous devez suivre quatre étapes clés (illustrées dans la [Figure](#page-96-0) 2-1) pour atteindre cet objectif :

- 1. Extrayez le texte du document.
- 2. Divisez le texte en morceaux gérables.
- 3. Convertissez le texte en nombres que les ordinateurs peuvent comprendre.
- 4. Stockez ces représentations numériques de votre texte dans un endroit qui permet de récupérer facilement et rapidement les sections pertinentes de votre document pour répondre à une question donnée.

<span id="page-96-0"></span>![](_page_96_Figure_6.jpeg)

Figure 2-1. Quatre étapes clés pour prétraiter vos documents pour une utilisation LLM

La <span id="page-97-3"></span><span id="page-97-2"></span>[Figure](#page-96-0) 2-1 illustre le flux de ce prétraitement et de cette transformation de vos documents, un processus appelé ingestion. *L'ingestion* est simplement le processus de conversion de vos documents en nombres que les ordinateurs peuvent comprendre et analyser, et de les stocker dans un type spécial de base de données pour une récupération efficace. Ces nombres sont officiellement connus sous le nom de *intégrations*, et ce type spécial de base de données est connu sous le nom de *magasin de vecteurs.* Examinons d'un peu plus près ce que sont les intégrations et pourquoi elles sont importantes, en commençant par quelque chose de plus simple que les intégrations alimentées par LLM.

# <span id="page-97-4"></span>Incorporations : conversion de texte en nombres

<span id="page-97-0"></span>*Intégration* fait référence à la représentation du texte sous la forme d'une (longue) séquence de nombres. Il s'agit d'une représentation avec perte, c'est-à-dire que vous ne pouvez pas récupérer le texte original de ces séquences de nombres. Vous stockez donc généralement à la fois le texte original et cette représentation numérique.

<span id="page-97-1"></span>Alors, pourquoi s'embêter ? Parce que vous gagnez la flexibilité et la puissance que procure le travail avec les chiffres : vous pouvez faire des mathématiques avec des mots ! Voyons pourquoi c'est excitant.

### **Intégrations avant les LLM**
<span id="page-98-0"></span>Bien avant les LLM, les informaticiens utilisaient les intégrations, par exemple pour activer les fonctionnalités de recherche en texte intégral sur les sites Web ou pour classer les e-mails comme spam. Voyons un exemple :

- 1. Prenez ces trois phrases :
	- Quelle journée ensoleillée.
	- Un ciel si lumineux aujourd'hui.
	- Je n'ai pas vu une journée ensoleillée depuis des semaines.
- 2. Répertoriez tous les mots uniques qu'ils contiennent : *quoi*, *a*, *ensoleillé*, *jour*, *tel*, *lumineux*, etc.
- 3. Pour chaque phrase, allez mot par mot et attribuez le chiffre 0 s'il n'est pas présent, 1 s'il est utilisé une fois dans la phrase, 2 s'il est présent deux fois, et ainsi de suite.

[Tableau](#page-99-0) 2-1 montre le résultat.

| Mot | Quelle<br>une<br>journée<br>ensoleillée. | Un ciel si<br>lumineux<br>aujourd'hui. | Je<br>n'ai pas<br>vu<br>une<br>journée<br>ensoleillée<br>depuis<br>semaines. |
|--------------|----------------------------|----------------------------------|---------------------------------------------------------------|
| quoi | 1 | 0 | 0 |
| un | 1 | 0 | 1 |
| ensoleillé | 1 | 0 | 1 |
| jour | 1 | 0 | 1 |
| tel | 0 | 1 | 0 |
| lumineux | 0 | 1 | 0 |
| ciels | 0 | 1 | 0 |
| aujourd'hui | 0 | 1 | 0 |
| Je | 0 | 0 | 1 |
| n'ai pas | 0 | 0 | 1 |
| vu | 0 | 0 | 1 |
| dans | 0 | 0 | 1 |

<span id="page-99-0"></span>Tableau 2-1. Intégrations de mots pour trois phrases

| Mot | Quelle<br>une<br>journée<br>ensoleillée. | Un ciel si<br>lumineux<br>aujourd'hui. | Je<br>n'ai pas<br>vu<br>une<br>journée<br>ensoleillée<br>depuis<br>semaines. |
|-------|----------------------------|-----------------------------------|---------------------------------------------------------------|
| semaines | 0 | 0 | 1 |

<span id="page-100-3"></span><span id="page-100-0"></span>Dans ce modèle, l'intégration de *Je n'ai pas vu de jour ensoleillé depuis des semaines* est la séquence de nombres *0 1 1 1 0 0 0 0 1 1 1 1 1*. C'est ce qu'on appelle le modèle *bag-of-words*, et ces intégrations sont également appelées * intégrations éparses* (ou vecteurs clairsemés - *vecteur* est un autre mot pour une séquence de nombres), car un grand nombre de nombres seront 0. La plupart des phrases anglaises n'utilisent qu'un très petit sous-ensemble de tous les mots anglais existants.

Vous pouvez utiliser avec succès ce modèle pour :

#### *Recherche par mot clé*

<span id="page-100-2"></span>Vous pouvez trouver quels documents contiennent un ou plusieurs mots donnés.

#### *Classification des documents*

<span id="page-100-1"></span>Vous pouvez calculer les intégrations pour une collection d'exemples précédemment étiquetés comme spam ou non spam, faire la moyenne et obtenir les fréquences moyennes des mots pour chacune des classes (spam ou non spam). Puis, chaque nouveau

Le document est comparé à ces moyennes et classé en conséquence.

La limite ici est que le modèle n’a aucune conscience du sens, seulement des mots réellement utilisés. Par exemple, les intégrations pour *jour ensoleillé* et *ciel lumineux* sont très différentes. En fait, ils n’ont aucun mot en commun, même si nous savons qu’ils ont une signification similaire. Ou bien, dans le cas du problème de classification des e-mails, un spammeur potentiel peut tromper le filtre en remplaçant les « mots de spam » courants par leurs synonymes.
Dans la section suivante, nous verrons comment les incorporations sémantiques répondent à cette limitation en utilisant des nombres pour représenter la signification du texte, au lieu des mots exacts trouvés dans le texte.

### **Intégrations basées sur LLM**

<span id="page-101-0"></span>Nous allons ignorer tous les développements ML intervenus entre les deux et passer directement aux intégrations basées sur LLM. Sachez simplement qu’il y a eu une évolution progressive de la méthode simple décrite dans la section précédente vers la méthode sophistiquée décrite dans celle-ci.

Vous pouvez considérer l’intégration de modèles comme une émanation du processus de formation des LLM. Si vous vous souvenez de la [Préface] (#page-8-0), le processus de formation LLM (apprentissage à partir de grandes quantités de texte écrit) permet aux LLM de compléter une invite (ou une entrée) avec la suite (sortie) la plus appropriée. Cette capacité découle d'une compréhension de la signification des mots et des phrases dans le contexte du texte environnant, tirée de la façon dont les mots sont utilisés ensemble dans les textes de formation. Cette *compréhension* de la signification (ou de la sémantique) de l'invite peut être extraite sous forme de représentation numérique (ou d'intégration) du texte saisi, et peut également être utilisée directement pour certains cas d'utilisation très intéressants.

En pratique, la plupart des modèles d'intégration sont formés dans ce seul but, en suivant des architectures et des processus de formation quelque peu similaires à ceux des LLM, car cela est plus efficace et aboutit à des intégrations de meilleure qualité. **[1](#page-161-0)**

<span id="page-102-3"></span><span id="page-102-2"></span><span id="page-102-1"></span><span id="page-102-0"></span>Un *modèle d'intégration* est alors un algorithme qui prend un morceau de texte et génère une représentation numérique de sa signification technique, une longue liste de nombres à virgule flottante (décimaux), généralement quelque part entre 100 et 2 000 nombres, ou *dimensions*. Ceux-ci sont également appelés plongements *denses*, par opposition aux plongements *clairsemés* de la section précédente, car ici, généralement, toutes les dimensions sont différentes de 0.

#### **CONSEIL**

Différents modèles produisent différents nombres et différentes tailles de listes. Tous ces éléments sont spécifiques à chaque modèle ; autrement dit, même si la taille des listes correspond, vous ne pouvez pas comparer les intégrations de différents modèles. La combinaison d’intégrations de différents modèles doit toujours être évitée.

### **Les intégrations sémantiques expliquées**

<span id="page-103-0"></span>Considérez ces trois mots : *lion*, *animal* et *chien*. Intuitivement, quelle paire de ces mots partage des caractéristiques similaires à première vue ? La réponse évidente est *animal* et *chien*. Mais les ordinateurs n’ont pas la capacité d’exploiter cette intuition ou cette compréhension nuancée de la langue anglaise. Pour qu'un ordinateur puisse faire la différence entre un lion, un animal de compagnie ou un chien, vous devez être capable de les traduire dans le langage des ordinateurs, qui est celui des chiffres*.*.

[Figure](#page-104-0) 2-2 illustre la conversion de chaque mot en représentations numériques hypothétiques qui conservent leur signification.

<span id="page-104-0"></span>![](_page_104_Figure_0.jpeg)

Figure 2-2. Représentations sémantiques des mots

La <span id="page-104-1"></span>[Figure](#page-104-0) 2-2 montre chaque mot avec son incorporation sémantique correspondante. Notez que les nombres eux-mêmes n'ont pas de signification particulière, mais que les séquences de nombres pour deux mots (ou phrases) dont la signification est proche doivent être *plus proches* que celles de mots non liés. Comme vous pouvez le voir, chaque nombre est une *valeur à virgule flottante*, et chacun d'eux représente une *dimension* sémantique. Voyons ce que nous entendons par *plus près* :

Si nous traçons ces vecteurs dans un espace tridimensionnel, cela pourrait ressembler à [Figure](#page-105-0) 2-3.

<span id="page-105-0"></span>![](_page_105_Figure_1.jpeg)

Figure 2-3. Tracé de vecteurs de mots dans un espace multidimensionnel

[Figure](#page-105-0) 2-3 montre que les vecteurs *pet* et *dog* sont plus proches l'un de l'autre en distance que le tracé *lion*. On peut également observer que les angles entre chaque parcelle varient en fonction de leur similitude. Par exemple, les mots *animal* et *lion* ont un angle plus large entre eux que *animal* et *chien*, ce qui indique davantage de similitudes partagées par ces dernières paires de mots. Plus l’angle ou la distance entre deux vecteurs est étroit, plus leurs similitudes sont étroites.
<span id="page-106-0"></span>Un moyen efficace de calculer le degré de similarité entre deux vecteurs dans un espace multidimensionnel est appelé similarité cosinus. *Similitude cosinus* calcule le produit scalaire des vecteurs et le divise par le produit de leurs grandeurs pour obtenir un nombre compris entre –1 et 1, où 0 signifie que les vecteurs ne partagent aucune corrélation, –1 signifie qu'ils sont absolument différents et 1 signifie qu'ils sont absolument similaires. Ainsi, dans le cas de nos trois mots ici, la similarité cosinus entre *animal* et *chien* pourrait être de 0,75, mais entre *animal* et *lion*, elle pourrait être de 0,1.

<span id="page-106-1"></span>La possibilité de convertir des phrases en intégrations qui capturent la signification sémantique, puis d'effectuer des calculs pour trouver des similitudes sémantiques entre différentes phrases nous permet d'obtenir un LLM pour trouver les documents les plus pertinents pour répondre à des questions sur un grand corps de texte comme notre document PDF Tesla. Maintenant que vous comprenez la situation dans son ensemble, revenons sur la première étape (indexation) du prétraitement de votre document.

#### **AUTRES UTILISATIONS DES INTÉGRATIONS**

<span id="page-107-0"></span>Ces séquences de nombres et de vecteurs ont un certain nombre de propriétés intéressantes :

- Comme vous l'avez appris plus tôt, si vous considérez un vecteur comme décrivant un point dans un espace de grande dimension, les points qui sont plus proches les uns des autres ont des significations plus similaires, donc une fonction de distance peut être utilisée pour mesurer la similarité.
- Des groupes de points proches les uns des autres peuvent être considérés comme liés ; par conséquent, un algorithme de regroupement peut être utilisé pour identifier des sujets (ou des groupes de points) et classer de nouvelles entrées dans l'un de ces sujets.
- Si vous faites la moyenne de plusieurs intégrations, on peut dire que l'intégration moyenne représente la signification globale de ce groupe ; c'est-à-dire que vous pouvez intégrer un long document (par exemple, ce livre) en :
	- 1. Intégration de chaque page séparément
	- 2. Prendre la moyenne des intégrations de toutes les pages comme intégration du livre
- Vous pouvez « parcourir » l'espace du « sens » en utilisant les opérations mathématiques élémentaires d'addition et de soustraction : par exemple, l'opération *roi – homme + femme = reine.* Si vous prenez le sens (ou l'intégration sémantique) de *roi*, soustrayez le sens de *homme*, probablement vous arrivez au plus

signification abstraite de *monarque*, à quel point, si vous ajoutez la signification de *femme*, vous êtes arrivé près de la signification (ou de l'intégration) du mot *reine*.

Il existe des modèles qui peuvent produire des intégrations de contenu non textuel, par exemple des images, des vidéos et des sons, en plus du texte. Cela permet, par exemple, de trouver les images les plus similaires ou les plus pertinentes pour une phrase donnée.

Nous n'explorerons pas tous ces attributs dans ce livre, mais il est utile de savoir qu'ils peuvent être utilisés pour un certain nombre d'[applications](https://oreil.ly/PU2C8) telles que :

#### *Rechercher*

Trouver les documents les plus pertinents pour une nouvelle requête

#### *Regroupement*

Étant donné un corpus de documents, les diviser en groupes (par exemple, sujets)

#### *Classement*

Affectation d'un nouveau document à un groupe ou une étiquette préalablement identifié (par exemple, un sujet)

#### *Recommandation*

Étant donné un document, faire apparaître des documents similaires

*Détection des anomalies*

Identifier les documents très différents de ceux vus précédemment

Nous espérons que cela vous laissera une certaine intuition que les intégrations sont assez polyvalentes et peuvent être utilisées à bon escient dans vos futurs projets.

## Conversion de vos documents en texte

<span id="page-109-0"></span>Comme mentionné au début du chapitre, la première étape du prétraitement de votre document consiste à le convertir en texte. Pour y parvenir, vous devrez créer une logique pour analyser et extraire le document avec une perte de qualité minimale. Heureusement, LangChain fournit des *chargeurs de documents* qui gèrent la logique d'analyse et vous permettent de « charger » des données provenant de diverses sources dans une classe Document composée de texte et de métadonnées associées.

<span id="page-109-1"></span>Par exemple, considérons un simple fichier *.txt*. Vous pouvez simplement importer une classe LangChain TextLoader pour extraire le texte, comme ceci :

*Python*

```
from langchain_community.document_loaders import
```

```
loader = TextLoader("./test.txt")
loader.load()
```
#### *JavaScript*

```
import { TextLoader } from "langchain/document_lo
const loader = new TextLoader("./test.txt");
const docs = await loader.load();
```
#### *Le résultat :*

```
[Document(page_content='text content \n', metadat
 './test.txt'})]
```
Le bloc de code précédent suppose que vous disposez d'un fichier nommé test.txt dans votre répertoire actuel. L'utilisation de tous les chargeurs de documents LangChain suit un modèle similaire :

- 1. Commencez par choisir le chargeur pour votre type de document dans la longue liste d'[intégrations](https://oreil.ly/iLJ33).
- 2. Créez une instance du chargeur en question, ainsi que tous les paramètres permettant de le configurer, y compris l'emplacement de vos documents (généralement un chemin du système de fichiers ou une adresse Web).
- 3. Chargez les documents en appelant load() , qui renvoie une liste de documents prêts à passer à l'étape suivante (nous en reparlerons bientôt).

Outre les fichiers *.txt*, LangChain fournit des chargeurs de documents pour d'autres types de fichiers populaires, notamment *.csv*, *.json* et Markdown, ainsi que des intégrations avec des plateformes populaires telles que Slack et Notion.

Par exemple, vous pouvez utiliser WebBaseLoader pour charger du HTML à partir d'URL Web et l'analyser en texte.

Installez le package beautifulsoup4 :

pip installer beautifulsoup4

<span id="page-111-0"></span>*Python*

depuis l'importation de langchain\_community.document\_loaders

```
loader = WebBaseLoader("https://www.langchain.com
loader.load()
```
#### <span id="page-112-0"></span>*JavaScript*

```
// install cheerio: npm install cheerio
import {
 CheerioWebBaseLoader
} from "@langchain/community/document_loaders/web
const loader = new CheerioWebBaseLoader("https://
const docs = await loader.load();
```
Dans le cas de notre cas d'utilisation Tesla PDF, nous pouvons utiliser PDFLoader de LangChain pour extraire le texte du document PDF :

#### <span id="page-112-1"></span>*Python*

```
# install the pdf parsing library
# pip install pypdf
```
depuis l'importation de langchain\_community.document\_loaders

```
loader = PyPDFLoader("./test.pdf")
pages = loader.load()
```
#### <span id="page-113-1"></span>*JavaScript*

```
// install the pdf parsing library: npm install p
import { PDFLoader } from "langchain/document_loa
const loader = new PDFLoader("./test.pdf");
const docs = await loader.load();
```
<span id="page-113-0"></span>Le texte a été extrait du document PDF et stocké dans la classe Document. Mais il y a un problème. Le document chargé comporte plus de 100 000 caractères, il ne rentre donc pas dans la fenêtre contextuelle de la grande majorité des LLM ou des modèles d'intégration. Afin de surmonter cette limitation, nous devons diviser le document en morceaux de texte gérables que nous pouvons ensuite convertir en intégrations et effectuer une recherche sémantique, nous amenant à la deuxième étape (récupération).

#### **CONSEIL**

Les LLM et les modèles d'intégration sont conçus avec une limite stricte quant à la taille des jetons d'entrée et de sortie qu'ils peuvent gérer. Cette limite est généralement appelée *fenêtre contextuelle* et s'applique généralement à la combinaison d'entrée et de sortie ; c'est-à-dire que si la fenêtre contextuelle est de 100 (nous parlerons d'unités en une seconde) et que votre entrée mesure 90, la sortie peut avoir une longueur maximale de 10. Les fenêtres contextuelles sont généralement mesurées en nombre de jetons, par exemple 8 192 jetons. Les jetons, comme mentionné dans la [Préface](#page-8-0), sont une représentation du texte sous forme de nombres, chaque jeton couvrant généralement entre trois et quatre caractères du texte anglais.

## <span id="page-114-0"></span>Diviser votre texte en morceaux

<span id="page-114-2"></span><span id="page-114-1"></span>À première vue, il peut sembler simple de diviser un grand corps de texte en morceaux, mais conserver ensemble des morceaux de texte *sémantiquement* liés (liés par le sens) est un processus complexe. Pour faciliter la division de documents volumineux en morceaux de texte petits mais toujours significatifs, LangChain fournit RecursiveCharacterTextSplitter , qui effectue les opérations suivantes :

- 1. Faites une liste de séparateurs, par ordre d'importance. Par défaut ce sont :
	- une. Le séparateur de paragraphe : \n\n
	- B. Le séparateur de ligne : \n
	- c. Le séparateur de mots : caractère espace
- 2. Pour respecter la taille de bloc donnée, par exemple 1 000 caractères, commencez par diviser les paragraphes.
- 3. Pour tout paragraphe plus long que la taille de morceau souhaitée, divisé par le séparateur suivant : les lignes. Continuez jusqu'à ce que tous les morceaux soient plus petits que la longueur souhaitée ou qu'il n'y ait plus de séparateurs supplémentaires à essayer.
- 4. Émettez chaque morceau en tant que Document , avec les métadonnées du document original transmises et des informations supplémentaires sur la position dans le document original.

Voyons un exemple :

#### <span id="page-115-0"></span>*Python*

```
à partir de langchain_text_splitters importer RecursiveCha
loader = TextLoader("./test.txt") # ou tout autre 
docs = chargeur.load()
séparateur = RecursiveCharacterTextSplitter (
 chunk_size=1000,
 chunk_overlap=200,
)
splitted_docs = splitter.split_documents(docs)
```
#### <span id="page-116-0"></span>*JavaScript*

```
importer { TextLoader } depuis "langchain/document_lo
importer { RecursiveCharacterTextSplitter } depuis "@
const chargeur = new TextLoader("./test.txt"); //o
const docs = waitloader.load();
const splitter = nouveau RecursiveCharacterTextSplitt
 taille du morceau : 1000,
 chunkOverlap : 200,
});
const splittedDocs = attendre splitter.splitDocument
```
In the preceding code, the documents created by the document loader are split into chunks of 1,000 characters each, with some overlap between chunks of 200 characters to maintain some context. The result is also a list of documents, where each document is up to 1,000 characters in length, split along the natural divisions of written text—paragraphs, new lines and finally, words. This uses the structure of the text to keep each chunk a consistent, readable snippet of text.

RecursiveCharacterTextSplitter can also be used to split code languages and Markdown into semantic chunks. This is done by using keywords specific to each language as the separators, which ensures, for instance, the body of each function is kept in the same chunk, instead of split between several. Usually, as programming languages have more structure than written text, there's less need to use overlap between the chunks. LangChain contains separators for a number of popular languages, such as Python, JS, Markdown, HTML, and many more. Here's an example:

*Python*

```
à partir de l'importation langchain_text_splitters (
 Langue,
 RécursiveCharacterTextSplitter,
)
PYTHON_CODE = """
def hello_world() :
 print("Bonjour le monde !")
# Appeler la fonction
bonjour_monde()
"""
```

```
python_splitter = RécursiveCharacterTextSplitter
 langue=Language.PYTHON, chunk_size=50, chun
)
python_docs = python_splitter.create_documents([P
```
#### *JavaScript*

```
importer { RecursiveCharacterTextSplitter } depuis "@
const PYTHON_CODE = `
def hello_world():
 print("Hello, World!")
# Call the function
hello_world()
`;
const pythonSplitter = RecursiveCharacterTextSpli
 taille du morceau: 50,
 chunkOverlap : 0,
});
const pythonDocs = attendre pythonSplitter.createDoc
```
*The output:*

[Document(page\_content='def hello\_world():\n p Document(page\_content='# Call the function\nh

#### Notice how we're still using

RecursiveCharacterTextSplitter as before, but now we're creating an instance of it for a specific language, using the from\_language method. This one accepts the name of the language, and the usual parameters for chunk size, and so on. Also notice we are now using the method create\_documents , which accepts a list of strings, rather than the list of documents we had before. This method is useful when the text you want to split doesn't come from a document loader, so you have only the raw text strings.

You can also use the optional second argument to create\_documents in order to pass a list of metadata to associate with each text string. This metadata list should have the same length as the list of strings and will be used to populate the metadata field of each Document returned.

Let's see an example for Markdown text, using the metadata argument as well:

#### *Python*

```
markdown_text = """
# LangueChaîne
⚡ Création d'applications avec des LLM via compos
## Installation rapide
```bash
pip install langchain
```
En tant que projet open source dans un environnement en développement rapide
 aux cotisations.
"""
md_splitter = RecursiveCharacterTextSplitter.from
 langue=Language.MARKDOWN, chunk_size=60, ch
)
md_docs = md_splitter.create_documents([markdown_
 [{"source": "https://www.langchain.com"}])
```
*JavaScript*

```
const markdownText = `
# LangChain
__PROTECTED_CODE_7__
⚡ Building applications with LLMs through compos
## Quick Install
\`\`\`bash
pip installer langchain
\`\`\`
As an open source project in a rapidly developing
 open to contributions.
`;
const mdSplitter = RécursiveCharacterTextSplitter
 taille du morceau: 60,
 chunkOverlap : 0,
});
const mdDocs = attendre mdSplitter.createDocuments([
 [{"source": "https://www.langchain.com"}]);
```
#### *The output:*

```
[Document(page_content='#LangChain', 
 metadata={"source": "https://www.langchain.co
 Document(page_content='⚡ Création d'applications 
   ⚡', metadata={"source": "https://www.langcha
```
⚡ , métadonnées { source : https://www.langcha Document(page\_content='## Installation rapide\n\n```ba metadata={"source": "https://www.langchain.co Document(page\_content='pip install langchain', metadata={"source": "https://www.langchain.co Document(page\_content='```', metadata={"source" Document(page\_content='En tant que projet open source, nous', metadata={"source": "https://www.langcha Document(page\_content='sommes extrêmement ouverts à con metadata={"source": "https://www.langchain.co

Remarquez deux choses :

- Le texte est divisé selon les points d'arrêt naturels dans le document Markdown ; par exemple, le titre est divisé en un seul bloc, la ligne de texte située en dessous dans un bloc séparé, et ainsi de suite.
- Les métadonnées que nous avons transmises dans le deuxième argument sont attachées à chaque document résultant, ce qui vous permet de suivre, par exemple, d'où vient le document et où vous pouvez aller voir l'original.

## <span id="page-122-2"></span>Génération d'intégrations de texte

<span id="page-122-4"></span><span id="page-122-3"></span><span id="page-122-1"></span><span id="page-122-0"></span>LangChain dispose également d'une classe Embeddings conçue pour s'interfacer avec les modèles d'intégration de texte, notamment OpenAI, Cohere et

Hugging Face – et générez des représentations vectorielles du texte. Cette classe fournit deux méthodes : une pour intégrer des documents et une pour intégrer une requête. Le premier prend une liste de chaînes de texte en entrée, tandis que le second prend une seule chaîne de texte.

Voici un exemple d'[intégration](https://oreil.ly/9tnzQ) d'un document utilisant le modèle d'intégration d'OpenAI :

#### <span id="page-123-1"></span>*Python*

```
from langchain_openai import OpenAIEmbeddings
model = OpenAIEmbeddings()
embeddings = model.embed_documents([
 "Hi there!",
 "Oh, hello!",
 "What's your name?",
 "My friends call me World",
 "Hello World!"
])
```
#### <span id="page-123-0"></span>*JavaScript*

importer { OpenAIEmbeddings } depuis "@langchain/open

```
const model = new OpenAIEmbeddings();
const embeddings = await embeddings.embedDocument
 "Hi there!",
 "Oh, hello!",
 "What' s your name?",
 "My friends call me World",
 "Hello World!"
]);
```
#### *Le résultat :*

```
[
 [
 -0.004845875, 0.004899438, -0.016358767, -0.0
 0.012571548, -0.019156644, 0.009036391, -0
 0.022861943, 0.010321903, -0.023479493, -0
 0.0026371893, 0.025206111, -0.012048521, 0.01
 -0.010580265, -0.003509951, 0.004070787, 0.00
 ... 1511 more items
 ]
 [
 -0.009446913, -0.013253193, 0.013174579, 0
 0.0077763423, -0.0260478, -0.0114384955, -0
 0.041797023, 0.01787183, 0.00552271, -0.004
     -0 01542166 0 033752076 0 006112323 0 02
```

```
 -0.01542166, 0.033752076, 0.006112323, 0.02
 -0.006623321, 0.016116094, -0.0061090477, -
 ... 1511 more items
 ]
 ... 3 more items
]
```
Notez que vous pouvez intégrer plusieurs documents en même temps ; vous devriez préférer cela plutôt que de les intégrer un par un, car cela sera plus efficace (en raison de la façon dont ces modèles sont construits). Vous obtenez une liste contenant plusieurs listes de nombres : chaque liste interne est un vecteur ou une incorporation, comme expliqué dans une section précédente.

<span id="page-125-1"></span><span id="page-125-0"></span>Voyons maintenant un exemple de bout en bout utilisant les trois fonctionnalités que nous avons vues jusqu'à présent :

- Chargeurs de documents, pour convertir n'importe quel document en texte brut
- Séparateurs de texte, pour diviser chaque gros document en plusieurs petits documents
- Modèles d'intégration, pour créer une représentation numérique de la signification de chaque scission

Voici le code :

<span id="page-125-2"></span>*Python*

```
from langchain_community.document_loaders import
from langchain_text_splitters import RecursiveCha
from langchain_openai import OpenAIEmbeddings
```

```
## Load the document
```

```
loader = TextLoader("./test.txt")
doc = loader.load()
```
"""

[

```
 Document(page_content='Document loaders\n\nUs
 from a source as `Document`\'s. A `Docume
 associated metadata. For example, there a
 loading a simple `.txt` file, for loading
 page, or even for loading a transcript of
 document loader exposes two methods:\n1. 
 the configured source\n2. "Load and split
 configured source and split them using th
 splitter\n\nThey optionally implement:\n\
 documents into memory lazily\n', metadata
```
] """

```
## Split the document
```
h k je 1000

text\_splitter = RecursiveCharacterTextSplitter(

```
 chunk_size=1000,
 chunk_overlap=20,
)
morceaux = text_splitter.split_documents(doc)
## Générer des intégrations
embeddings_model = OpenAIEmbeddings()
intégrations = intégrations_model.embed_documents(
 [chunk.page_content pour un morceau en morceaux]
)
"""
[[0,0053587136790156364,
-0,0004999046213924885,
 0,038883671164512634,
 -0,003001077566295862,
 -0.00900818221271038, ...], ...]
"""
```
#### <span id="page-127-0"></span>*JavaScript*

```
importer { TextLoader } depuis "langchain/document_lo
importer { RecursiveCharacterTextSplitter } depuis "@
importer { OpenAIEmbeddings } depuis "@langchain/open
// Charge le document
```

```
const chargeur = new TextLoader("./test.txt");
const docs = waitloader.load();
// Divise le document
const splitter = nouveau RecursiveCharacterTextSplitt
 taille du morceau : 1000,
 chunkOverlap : 200,
});
const chunks = wait splitter.splitDocuments(docs
// Générer des intégrations
const model = new OpenAIEmbeddings();
attendre embeddings.embedDocuments(chunks.map(c => c
```
<span id="page-128-0"></span>Once you've generated embeddings from your documents, the next step is to store them in a special database known as a vector store.

## Storing Embeddings in a Vector Store

<span id="page-128-1"></span>Earlier in this chapter, we discussed the cosine similarity calculation to measure the similarity between vectors in a vector space. A vector store is a database designed to store vectors and perform complex calculations, like cosine similarity, efficiently and quickly.

Unlike traditional databases that specialize in storing structured data (such as JSON documents or data conforming to the schema of a relational database), vector stores handle unstructured data, including text and images. Like traditional databases, vector stores are capable of performing create, read, update, delete (CRUD), and search operations.

<span id="page-129-1"></span>Vector stores unlock a wide variety of use cases, including scalable applications that utilize AI to answer questions about large documents, as illustrated in [Figure](#page-129-0) 2-4.

<span id="page-129-0"></span>![](_page_129_Figure_3.jpeg)

Figure 2-4. Loading, embedding, storing, and retrieving relevant docs from a vector store

[Figure](#page-129-0) 2-4 illustrates how document embeddings are inserted into the vector store and how later, when a query is sent, similar embeddings are retrieved from the vector store.

Currently, there is an abundance of vector store providers to choose from, each specializing in different capabilities. Your selection should depend on the critical requirements of your

application, including multitenancy, metadata filtering capabilities, performance, cost, and scalability.

Although vector stores are niche databases built to manage vector data, there are a few disadvantages working with them:

- Most vector stores are relatively new and may not stand the test of time.
- Managing and optimizing vector stores can present a relatively steep learning curve.
- Managing a separate database adds complexity to your application and may drain valuable resources.

Fortunately, vector store capabilities have recently been extended to PostgreSQL (a popular open source relational database) via the pgvector extension. This enables you to use the same database you're already familiar with and to power both your transactional tables (for instance your users table) as well as your vector search tables.

### <span id="page-130-0"></span>**Getting Set Up with PGVector**

<span id="page-130-1"></span>To use Postgres and PGVector you'll need to follow a few setup steps:

- 1. Ensure you have Docker installed on your computer, following the [instructions](https://oreil.ly/Gn28O) for your operating system.
- 2. Run the following command in your terminal; it will launch a Postgres instance in your computer running on port 6024:

```
exécution du docker \
 --name pgvecteur-conteneur \
 -e POSTGRES_USER=chaîne de langage \
 -e POSTGRES_PASSWORD = chaîne de langage \
 -e POSTGRES_DB = chaîne de langage \
 -p 6024:5432 \
 -d vecteurpg/vecteurpg:pg16
```
Open your docker dashboard containers and you should see a green running status next to pgvector-container .

3. Save the connection string to use in your code; we'll need it later:

postgresql+psycopg://langchain:langchain@localh

### **Working with Vector Stores**

Picking up where we left off in the previous section on embeddings, now let's see an example of loading, splitting, embedding, and storing a document in PGVector:

#### <span id="page-132-0"></span>*Python*

```
# d'abord, pip install langchain-postgres
à partir de l'importation langchain_community.document_loaders
à partir de langchain_openai importer OpenAIEmbeddings
à partir de langchain_text_splitters importer RecursiveCha
à partir de langchain_postgres.vectorstores importer PGVec
à partir de langchain_core.documents importer un document
importer l'uuid
```

```
# Chargez le document, divisez-le en morceaux
raw_documents = TextLoader('./test.txt').load()
text_splitter = RecursiveCharacterTextSplitter(ch
```

```
 chunk_overlap=200)
documents = text_splitter.split_documents(raw_doc
```

```
# intégrer chaque morceau et l'insérer dans le vecteur 
embeddings_model = OpenAIEmbeddings()
connexion = 'postgresql+psycopg://langchain:lang
db = PGVector.from_documents(documents, intégration
```
#### <span id="page-133-0"></span>*JavaScript*

```
importer { TextLoader } depuis "langchain/document_lo
importer { RecursiveCharacterTextSplitter } depuis "@
importer { OpenAIEmbeddings } depuis "@langchain/open
importer { PGVectorStore } depuis "@langchain/communi
importer { v4 comme uuidv4 } depuis 'uuid' ;
// Charge le document, divise-le en morceaux
const chargeur = new TextLoader("./test.txt");
const raw_docs = attendre chargeur.load();
const splitter = nouveau RecursiveCharacterTextSplitt
 taille du morceau : 1000,
 chunkOverlap : 200,
});
const docs = attendre splitter.splitDocuments(docs)
// intègre chaque morceau et l'insère dans le vecteur
const embeddings_model = new OpenAIEmbeddings();
const db = attendre PGVectorStore.fromDocuments(docs
 postgresConnectionOptions : {
 chaîne de connexion : 'postgresql://langchain:lan
 }
})
```
Notice how we reuse the code from the previous sections to first load the documents with the loader and then split them into smaller chunks. Then, we instantiate the embeddings model we want to use—in this case, OpenAI's. Note that you could use any other embeddings model supported by LangChain here.

Next, we have a new line of code, which creates a vector store given documents, the embeddings model, and a connection string. This will do a few things:

- Establish a connection to the Postgres instance running in your computer (see "Getting Set Up with [PGVector"](#page-130-0).)
- Run any setup necessary, such as creating tables to hold your documents and vectors, if this is the first time you're running it.
- Create embeddings for each document you passed in, using the model you chose.
- Store the embeddings, the document's metadata, and the document's text content in Postgres, ready to be searched.

Let's see what it looks like to search documents:

*Python*

```
db.similarity_search("requête", k=4)
```
*JavaScript*

await pgvectorStore.similaritySearch("query", 4);

This method will find the most relevant documents (which you previously indexed), by following this process:

- The search query—in this case, the word query —will be sent to the embeddings model to retrieve its embedding.
- Then, it will run a query on Postgres to find the N (in this case 4) previously stored embeddings that are most similar to your query.
- Finally, it will fetch the text content and metadata that relates to each of those embeddings.
- The model can now return a list of Document sorted by how similar they are to the query—the most similar first, the second most similar after, and so on.

You can also add more documents to an existing database. Let's see an example:

*Python*

```
identifiants = [str(uuid.uuid4()), str(uuid.uuid4())]
db.add_documents(
 [
 Document(
 page_content="il y a des chats dans le p
 metadata={"location": "étang", "sujet"
 ),
 Document(
 page_content="on trouve également des canards dans
 metadata={"location": "étang", "sujet"
 ),
 ],
 identifiants = identifiants,
)
```
*JavaScript*

```
const ids = [uuidv4(), uuidv4()];
attendre db.addDocuments(
 [
 {
 pageContenu : "il y a des chats dans l'étang",
 métadonnées : {emplacement : "étang", sujet : "animal
 },
 {
```

```
{
 pageContent : "on trouve également des canards dans le p
 métadonnées : {emplacement : "étang", sujet : "animal
 },
 ],
 {identifiants}
);
```
The add\_documents method we're using here will follow a similar process to fromDocuments :

- Create embeddings for each document you passed in, using the model you chose.
- Store the embeddings, the document's metadata, and the document's text content in Postgres, ready to be searched.

In this example, we are using the optional ids argument to assign identifiers to each document, which allows us to update or delete them later.

Here's an example of the delete operation:

*Python*

db.delete(ids=[1])

*JavaScript*

```
attendre db.delete({ identifiants : [ids[1]] })
```
Cela supprime le deuxième document inséré à l'aide de son identifiant unique universel (UUID). Voyons maintenant comment procéder de manière plus systématique.

## Suivi des modifications apportées à vos documents
<span id="page-138-1"></span>L'un des principaux défis liés au travail avec des magasins de vecteurs est de travailler avec des données qui changent régulièrement, car les changements impliquent une réindexation. Et la réindexation peut conduire à des recalculs coûteux d’intégrations et de duplications de contenu préexistant.

<span id="page-138-2"></span>Heureusement, LangChain fournit une API d'indexation pour faciliter la synchronisation de vos documents avec votre magasin de vecteurs. L'API utilise une classe ( RecordManager ) pour suivre les écritures de documents dans le magasin de vecteurs. Lors de l'indexation du contenu, des hachages sont calculés pour chaque document et les informations suivantes sont stockées dans RecordManager :

- Le hachage du document (hachage du contenu de la page et des métadonnées)
- Écrire l'heure
- L'identifiant de la source (chaque document doit inclure des informations dans ses métadonnées pour déterminer la source ultime de ce document).

<span id="page-139-0"></span>De plus, l'API d'indexation fournit des modes de nettoyage pour vous aider à décider comment supprimer les documents existants dans le magasin de vecteurs. Par exemple, si vous avez modifié la façon dont les documents sont traités avant l'insertion ou si les documents sources ont changé, vous souhaiterez peut-être supprimer tous les documents existants provenant de la même source que les nouveaux documents en cours d'indexation. Si certains documents sources ont été supprimés, vous souhaiterez supprimer tous les documents existants dans le magasin vectoriel et les remplacer par les documents réindexés.

Les modes sont les suivants :

- Le mode Aucun n'effectue aucun nettoyage automatique, permettant à l'utilisateur d'effectuer manuellement un nettoyage de l'ancien contenu.
- Les modes incrémentiel et complet suppriment les versions précédentes du contenu si le contenu du document source ou des documents dérivés a changé.

Le mode complet supprimera en outre tous les documents non inclus dans les documents en cours d'indexation.

Voici un exemple d'utilisation de l'API d'indexation avec une base de données Postgres configurée en gestionnaire d'enregistrements :

#### <span id="page-140-0"></span>*Python*

```
from langchain.indexes import SQLRecordManager, i
from langchain_postgres.vectorstores import PGVec
from langchain_openai import OpenAIEmbeddings
from langchain.docstore.document import Document
connection = "postgresql+psycopg://langchain:lang
collection_name = "my_docs"
embeddings_model = OpenAIEmbeddings(model="text-e
namespace = "my_docs_namespace"
vectorstore = PGVector(
 embeddings=embeddings_model,
 collection_name=collection_name,
 connection=connection,
 use_jsonb=True,
)
record_manager = SQLRecordManager(
 namespace,
```

```
 db_url="postgresql+psycopg://langchain:langch
)
# Create the schema if it doesn't exist
record_manager.create_schema()
# Create documents
docs = [
 Document(page_content='there are cats in the 
 "id": 1, "source": "cats.txt"}),
 Document(page_content='ducks are also found i
 "id": 2, "source": "ducks.txt"}),
]
# Index the documents
index_1 = index(
 docs,
 record_manager,
 vectorstore,
 cleanup="incremental", # prevent duplicate d
 source_id_key="source", # use the source fie
)
print("Index attempt 1:", index_1)
# second time you attempt to index, it will not a
index_2 = index(
 docs,
 record manager,
```

```
 vectorstore,
 cleanup="incremental",
 source_id_key="source",
)
print("Index attempt 2:", index_2)
# If we mutate a document, the new version will b
# versions sharing the same source will be delete
docs[0].page_content = "I just modified this docu
index_3 = index(
 docs,
 record_manager,
 vectorstore,
 cleanup="incremental",
 source_id_key="source",
)
print("Index attempt 3:", index_3)
```
\_ g ,

<span id="page-142-0"></span>*JavaScript*

/\*\* 1 Assurez-vous que Docker est installé et en cours d'exécution (https 1. Assurez-vous que Docker est installé et en cours d'exécution (https 2. Exécutez la commande suivante pour démarrer Postgre

```
docker run \
```
--name pgvecteur-conteneur \

-e POSTGRES\_USER=langchain\

- -e POSTGRES\_PASSWORD=langchain\
- -e POSTGRES\_DB=langchain\
- -p 6024:5432 \

-d vecteurpg/vecteurpg:pg16

```
3. Use the connection string below for the postgr
*/
```

```
import { PostgresRecordManager } from '@langchain
import { index } from 'langchain/indexes';
import { OpenAIEmbeddings } from '@langchain/open
import { PGVectorStore } from '@langchain/communi
import { v4 as uuidv4 } from 'uuid';
```

```
const tableName = 'test_langchain';
const connectionString =
```
 'postgresql://langchain:langchain@localhost:602 // Charge le document, divise-le en morceaux

```
const config = {
 postgresConnectionOptions: {
 connectionString,
 },
 tableName: tableName
```

```
 Nom de la table : Nom de la table,
 colonnes : {
 idColumnName : 'id',
vecteurColumnName : 'vecteur',
 contentColumnName : 'contenu',
 metadataColumnName : 'métadonnées',
 },
} ;
const vectorStore = attendre PGVectorStore.initializ
 nouveau OpenAIEmbeddings(),
 configuration
);
// Créer un nouveau gestionnaire d'enregistrements
const recordManagerConfig = {
 postgresConnectionOptions : {
 chaîne de connexion,
 },
 nom de la table : 'upsertion_records',
} ;
const recordManager = nouveau PostgresRecordManager (
 'test_espace de noms',
 recordManagerConfig
);
// Crée le schéma s'il n'existe pas
attendre recordManager.createSchema();
```

```
const documents = [
 {
 pageContent : "il y a des chats dans l'étang",
 métadonnées : { id : uuidv4(), source : 'cats.txt'
 },
 {
 pageContent : 'on trouve également des canards dans le pon
 métadonnées : { id : uuidv4(), source : 'ducks.txt
 },
];
// la première tentative indexera les deux documents
const index_attempt_1 = attendre l'index ({
 docsSource : docs,
 gestionnaire d'enregistrements,
 vecteurStore,
 options : {
 // empêche les documents en double par identifiant de bei
 nettoyage : 'incrémentiel',
 // la clé dans les métadonnées qui sera utilisée 
 sourceIdKey : 'source',
 },
});
console.log(index_attempt_1);
// la deuxième tentative ignorera l'indexation car 
// existe déjà
```

```
// existe déjà
const index_attempt_2 = attendre l'index ({
 docsSource : docs,
 gestionnaire d'enregistrements,
 vecteurStore,
 options : {
 nettoyage : 'incrémentiel',
 sourceIdKey : 'source',
 },
});
console.log(index_attempt_2);
// Si on mute un document, la nouvelle version sera 
// les versions partageant la même source seront supprimées
docs[0].pageContent = 'J'ai modifié le premier document
const index_attempt_3 = attendre l'index ({
 docsSource : docs,
 gestionnaire d'enregistrements,
 vecteurStore,
 options : {
 nettoyage : 'incrémentiel',
 sourceIdKey : 'source',
 },
});
console.log(index_attempt_3);
```
Tout d’abord, vous créez un gestionnaire d’enregistrements, qui garde la trace des documents qui ont déjà été indexés. Ensuite, vous utilisez la fonction index pour synchroniser votre magasin de vecteurs avec la nouvelle liste de documents. Dans cet exemple, nous utilisons le mode incrémentiel, donc tous les documents ayant le même identifiant que les précédents seront remplacés par la nouvelle version.

## <span id="page-147-1"></span>Optimisation de l'indexation

<span id="page-147-0"></span>Une étape d'indexation RAG de base implique le fractionnement naïf du texte et l'intégration de morceaux d'un document donné. Cependant, cette approche basique conduit à des résultats de récupération incohérents et à une fréquence relativement élevée d'hallucinations, en particulier lorsque la source de données contient des images et des tableaux.

Il existe diverses stratégies pour améliorer la précision et les performances de l’étape d’indexation. Nous en aborderons trois dans les sections suivantes : MultiVectorRetriever, RAPTOR et ColBERT.

### **MultiVectorRetriever**

<span id="page-147-2"></span>Un document contenant un mélange de texte et de tableaux ne peut pas être simplement divisé par texte en morceaux et intégré comme contexte : le tableau entier peut être facilement perdu. Pour résoudre ce problème, nous pouvons découpler les documents que nous souhaitons utiliser pour la synthèse des réponses d'une référence que nous souhaitons utiliser pour le [retriever. La figure](#page-148-0) 2-5 illustre comment.

<span id="page-148-0"></span>![](_page_148_Figure_1.jpeg)

Figure 2-5. Indexation de plusieurs représentations d'un même document

Par exemple, dans le cas d'un document contenant des tableaux, nous pouvons d'abord générer et intégrer des résumés des éléments du tableau, en garantissant que chaque résumé contient une référence d'identifiant au tableau brut complet. Ensuite, nous stockons les tables brutes référencées dans une docstore distincte. Enfin, lorsque la requête d'un utilisateur récupère un résumé de table, nous transmettons l'intégralité de la table brute référencée comme contexte à l'invite finale envoyée au LLM pour la synthèse des réponses. Cette approche nous permet de fournir au modèle le contexte complet des informations nécessaires pour répondre à la question.

Voici un exemple. Tout d'abord, utilisons le LLM pour générer des résumés des documents :

#### <span id="page-149-0"></span>*Python*
depuis langchain\_community.document\_loaders importer depuis langchain\_text\_splitters importer RecursiveCha depuis langchain\_openai importer OpenAIEmbeddings depuis langchain\_postgres.vectorstores importer PGVec depuis langchain\_core.output\_parsers importer StrOutp depuis langchain\_core.prompts importer ChatPromptTemp depuis pydantic importer BaseModel depuis langchain\_core.runnables import RunnablePass depuis langchain\_openai import ChatOpenAI depuis langchain\_core.documents import Document depuis langchain.retrievers.multi\_vector import Mul depuis langchain.storage import InMemoryStore import uuid connection = "postgresql+psycopg://langchain:lang collection\_name = "summaries" embeddings\_model = OpenAIEmbeddings() # Charger le document chargeur = TextLoader("./test.txt", encoding="utf-8 docs = chargeur.load()

print("longueur des documents chargés : ", len(docs[0].page

```
# Split the document
splitter = RecursiveCharacterTextSplitter(chunk_s
chunks = splitter.split_documents(docs)
# The rest of your code remains the same, startin
prompt_text = "Summarize the following document:\
prompt = ChatPromptTemplate.from_template(prompt_
llm = ChatOpenAI(temperature=0, model="gpt-3.5-tu
summarize_chain = {
 "doc": lambda x: x.page_content} | prompt | l
# batch the chain across the chunks
summaries = summarize_chain.batch(chunks, {"max_c
```
Définissons ensuite le magasin de vecteurs et le docstore pour stocker les résumés bruts et leurs intégrations :

#### <span id="page-150-0"></span>*Python*

)

```
# The vectorstore to use to index the child chunk
vectorstore = PGVector(
 embeddings=embeddings_model,
 collection_name=collection_name,
 connection=connection,
 use_jsonb=True,
```

```
)
# The storage layer for the parent documents
store = InMemoryStore()
id_key = "doc_id"
# indexing the summaries in our vector store, whi
# documents in our document store:
retriever = MultiVectorRetriever(
 vectorstore=vectorstore,
 docstore=store,
 id_key=id_key,
)
# Changed from summaries to chunks since we need 
doc_ids = [str(uuid.uuid4()) for _ in chunks]
# Each summary is linked to the original document
summary_docs = [
 Document(page_content=s, metadata={id_key: do
 for i, s in enumerate(summaries)
]
# Add the document summaries to the vector store 
retriever.vectorstore.add_documents(summary_docs)
# Store the original documents in the document st
# via doc_ids
# This allows us to first search summaries effici
# docs when needed
```
retriever.docstore.mset(list(zip(doc\_ids, morceaux)

```
# vector store retrieves the summaries
sub_docs = retriever.vectorstore.similarity_searc
 "chapter on philosophy", k=2)
```
Enfin, récupérons le document de contexte complet pertinent en fonction d'une requête :

<span id="page-152-1"></span>*Python*

```
# Whereas the retriever will return the larger so
retrieved_docs = retriever.invoke("chapter on phi
```
Voici l'implémentation complète en JavaScript :

<span id="page-152-0"></span>*JavaScript*

```
import * as uuid from 'uuid';
import { MultiVectorRetriever } from 'langchain/r
import { OpenAIEmbeddings } from '@langchain/open
import { RecursiveCharacterTextSplitter } from '@
```

```
import { InMemoryStore } from '@langchain/core/st
import { TextLoader } from 'langchain/document_lo
import { Document } from '@langchain/core/documen
import { PGVectorStore } from '@langchain/communi
import { ChatOpenAI } from '@langchain/openai';
import { PromptTemplate } from '@langchain/core/p
import { RunnableSequence } from '@langchain/core
import { StringOutputParser } from '@langchain/co
const connectionString =
 'postgresql://langchain:langchain@localhost:602
const collectionName = 'summaries';
const textLoader = new TextLoader('./test.txt');
const parentDocuments = await textLoader.load();
const splitter = new RecursiveCharacterTextSplitt
 chunkSize: 10000,
 chunkOverlap: 20,
});
const docs = await splitter.splitDocuments(parent
const prompt = PromptTemplate.fromTemplate(
 `Summarize the following document:\n\n{doc}`
);
const llm = new ChatOpenAI({ modelName: 'gpt-3.5-
const chain = RunnableSequence.from([
```

```
 { doc: (doc) => doc.pageContent },
 rapide,
 llm,
 nouveau StringOutputParser(),
]);
// chaîne de récapitulation par lots à travers les morceaux
résumés const = wait chain.batch(docs, {
 maxConcurrency : 5,
});
const idKey = 'doc_id';
const docIds = docs.map((_) => uuid.v4());
// crée des documents récapitulatifs avec des métadonnées liées à t
const summaryDocs = summaries.map((summary, i) =>
 const résuméDoc = nouveau document ({
 contenu de la page : résumé,
 métadonnées : {
 [idKey] : docIds[i],
 },
 });
renvoyer le résuméDoc ;
});
// Le byteStore à utiliser pour stocker le chu original
const byteStore = new InMemoryStore();
```
// vector store for the summaries

```
const vectorStore = attendre PGVectorStore.fromDocum
 des documents,
 nouveau OpenAIEmbeddings(),
 {
 postgresConnectionOptions : {
 chaîne de connexion,
 },
 }
);
const retriever = nouveau MultiVectorRetriever ({
 magasin vectoriel : magasin vectoriel,
 octetStore,
 clé d'identification,
});
const keyValuePairs = docs.map((originalDoc, i) =
// Utilisez le récupérateur pour ajouter les morceaux d'origine t
attendre retriever.docstore.mset(keyValuePairs);
// Vectorstore récupère seul les petits morceaux
const vectorstoreResult = wait retriever.vectors
 'chapitre sur la philosophie',
 2
);
console.log(`summary: ${vectorstoreResult[0].page
console.log(
__PROTECTED_CODE_1__
 `summary longueur récupérée : ${vectorstoreResult[
);
// Retriever renvoie un résultat plus gros
const retrieverResult = wait retriever.invoke('c
console.log(
 `longueur du morceau récupéré multi-vecteur : ${retriev
);
```
### **RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval**

<span id="page-156-2"></span><span id="page-156-1"></span>RAG systems need to handle lower-level questions that reference specific facts found in a single document or higherlevel questions that distill ideas that span many documents. Handling both types of questions can be a challenge with typical k-nearest neighbors (k-NN) retrieval over document chunks.

<span id="page-156-3"></span><span id="page-156-0"></span>*Recursive abstractive processing for tree-organized retrieval* (RAPTOR) is an effective strategy that involves creating document summaries that capture higher-level concepts, embedding and clustering those documents, and then [summarizing](https://oreil.ly/VdIpJ) each cluster. This is done recursively, producing a tree of summaries with increasingly high-level concepts. The **[2](#page-162-0)**

summaries and initial documents are then indexed together, giving coverage across lower-to-higher-level user questions. [Figure](#page-157-0) 2-6 illustrates.

<span id="page-157-0"></span>![](_page_157_Figure_1.jpeg)

Figure 2-6. Recursively summarizing documents

### **ColBERT: Optimizing Embeddings**

<span id="page-157-1"></span>One of the challenges of using embeddings models during the indexing stage is that they compress text into fixed-length (vector) representations that capture the semantic content of the document. Although this compression is useful for retrieval, <span id="page-158-1"></span>embedding irrelevant or redundant content may lead to hallucinations in the final LLM output.

One solution to this problem is to do the following:

- 1. Generate contextual embeddings for each token in the document and query.
- 2. Calculate and score similarity between each query token and all document tokens.
- 3. Sum the maximum similarity score of each query embedding to any of the document embeddings to get a score for each document.

<span id="page-158-0"></span>This results in a granular and effective embedding approach for better retrieval. Fortunately, the embedding model called ColBERT embodies the solution to this problem. **[3](#page-162-1)**

Here's how we can utilize ColBERT for optimal embedding of our data:

#### <span id="page-158-2"></span>*Python*

# RAGatouille is a library that makes it simple t #! pip install -U ragatouille

from ragatouille import RAGPretrainedModel

```
RAG = RAGPretrainedModel.from_pretrained("colbert
```

```
demandes d'importation
```
g p

data = response.json()

```
def get_wikipedia_page(titre : str) :
 """
 Récupérer le contenu intégral d'un Wikipédia
 :param title: str - Titre du pa Wikipédia
 :return: str - Contenu intégral de la page 
 """
 # Point de terminaison de l'API Wikipédia
 URL = "https://en.wikipedia.org/w/api.php"
 # Paramètres pour la requête API
 paramètres = {
 "action": "requête",
 "format": "json",
 "titres": titre,
 "prop": "extraits",
 "explaintext": Vrai,
 }
 # En-tête User-Agent personnalisé pour se conformer à Wik
 headers = {"User-Agent": "RAGatouille_tutoria
 réponse = requêtes.get(URL, params=params, h
```

```
 # Extraire le contenu de la page
 page = next(iter(data["query"]["pages"].value
 return page["extract"] si "extract" dans la page e
full_document = get_wikipedia_page("Hayao_Miyazak
## Créer un index
RAG.index(
 collection=[document_complet],
 index_name="Miyazaki-123",
 max_document_length=180,
 split_documents=Vrai,
)
#requête
results = RAG.search(query="Quel studio d'animation
résultats
#utiliser le récupérateur de langchain
récupérateur = RAG.as_langchain_retriever(k=3)
retriever.invoke("Quel studio d'animation a fait Miyaz
```
p j ()

En utilisant ColBERT, vous pouvez améliorer la pertinence des documents récupérés utilisés comme contexte par le LLM.

## Résumé

<span id="page-161-1"></span>Dans ce chapitre, vous avez appris comment préparer et prétraiter vos documents pour votre application LLM à l'aide de divers modules de LangChain. Les chargeurs de documents vous permettent d'extraire du texte de votre source de données, les séparateurs de texte vous aident à diviser votre document en morceaux sémantiquement similaires et les modèles d'incorporation convertissent votre texte en représentations vectorielles de sa signification.

Séparément, les magasins de vecteurs vous permettent d'effectuer des opérations CRUD sur ces intégrations ainsi que des calculs complexes pour calculer des morceaux de texte sémantiquement similaires. Enfin, les stratégies d'optimisation de l'indexation permettent à votre application d'IA d'améliorer la qualité des intégrations et d'effectuer une récupération précise des documents contenant des données semi-structurées, notamment des tableaux.

Dans le [Chapitre](#page-163-0) 3, vous apprendrez comment récupérer efficacement les morceaux de documents les plus similaires de votre magasin de vecteurs en fonction de votre requête, les fournir comme contexte que le modèle peut voir, puis générer une sortie précise.

<span id="page-161-0"></span>Arvind Neelakantan et al., "Incorporations de texte et de code par Contrastive [Pré-formation"](https://oreil.ly/YOVmh), arXiv, 21 janvier 2022. **[1](#page-102-0)**

<span id="page-162-0"></span>Parth Sarthi et al., "RAPTOR : Recursive Abstractive Processing for [Tree-Organized](https://oreil.ly/hS4NB) Retrieval", arXiv, 31 janvier 2024. Article publié à l'ICLR 2024. **[2](#page-156-0)**

<span id="page-162-1"></span>Keshav Santhanam et al., "ColBERTv2 : Récupération efficace et efficiente via une [interaction légère et tardive",](https://oreil.ly/9spW2) arXiv, 2 décembre 2021. **[3](#page-158-0)**

## <span id="page-163-0"></span>Chapitre 3. RAG Partie II : Discuter avec vos données

Dans le chapitre précédent, vous avez appris à traiter vos données et à créer et stocker des intégrations dans un magasin de vecteurs. Dans ce chapitre, vous apprendrez comment récupérer efficacement les intégrations et les morceaux de documents les plus pertinents en fonction de la requête d'un utilisateur. Cela vous permet de créer une invite contenant des documents pertinents comme contexte, améliorant ainsi la précision du résultat final du LLM.

Ce processus, qui consiste à intégrer la requête d'un utilisateur, à récupérer des documents similaires à partir d'une source de données, puis à les transmettre comme contexte à l'invite envoyée au LLM, est officiellement connu sous le nom de *génération augmentée par récupération* (RAG).

<span id="page-163-1"></span>RAG est un composant essentiel pour créer des applications LLM compatibles avec le chat qui sont précises, efficaces et à jour. Dans ce chapitre, vous passerez des bases aux stratégies avancées pour créer un système RAG efficace pour diverses sources de données (telles que les magasins de vecteurs et les bases de données) et les structures de données (structurées et non structurées).

Mais d’abord, définissons RAG et discutons de ses avantages.

# Présentation de la génération augmentée par récupération

<span id="page-164-2"></span>RAG est une technique utilisée pour améliorer la précision des résultats générés par les LLM en fournissant un contexte à partir de sources externes. Le terme a été inventé à l'origine dans un article rédigé par des chercheurs de Meta AI qui ont découvert que les modèles compatibles RAG sont plus factuels et spécifiques que les modèles non RAG. **[1](#page-235-0)**

<span id="page-164-0"></span>Sans RAG, le LLM s'appuie uniquement sur ses données pré-entraînées, qui peuvent être obsolètes. Par exemple, posons à ChatGPT une question sur un événement en cours et voyons sa réponse :

#### <span id="page-164-1"></span>*Entrée*

Quel pays est le dernier vainqueur du F masculin

#### *Sortie*

Le dernier vainqueur de la Coupe du Monde de la FIFA est la France.

La réponse du LLM est factuellement incorrecte et dépassée. Le dernier vainqueur au moment de la publication de ce livre est l'Argentine, qui a remporté la Coupe du monde en 2022. Bien que cet exemple de question puisse être trivial, l'hallucination LLM peut avoir des conséquences désastreuses si l'on s'appuie sur ses réponses pour vérifier les faits ou prendre une décision importante.

<span id="page-165-1"></span>Pour lutter contre ce problème, nous devons fournir au LLM des informations factuelles et à jour à partir desquelles il peut formuler une réponse précise. Dans la continuité de l'exemple précédent, passons à la page Wikipédia de la Coupe FIFA [Monde](https://oreil.ly/LpLOV), copions le paragraphe d'introduction, puis ajoutons-le comme *contexte* à notre invite à ChatGPT :

<span id="page-165-0"></span>Quel pays est le dernier vainqueur de l'épreuve F masculine

Voir le contexte ci-dessous.
La Coupe du Monde de la FIFA, souvent appelée Coupe du Monde, est une compétition de football entre les équipes seniors masculines, l'instance dirigeante mondiale de la Fédération Internationale de Football Associa. Le tournoi a été le tournoi inaugural en 1930, à l'exception de la Seconde Guerre mondiale. Les champions en titre sont titulaires de l'Arge lors du tournoi 2022.

Notez que la dernière phrase contient le contexte nécessaire que le LLM peut utiliser pour fournir une réponse précise. Voici la réponse du LLM :

Le dernier vainqueur de la Coupe du Monde masculine de la FIFA est le titre du tournoi 2022.

Grâce au contexte supplémentaire à jour fourni, le LLM a pu générer une réponse précise à l'invite. Mais copier et coller des informations pertinentes en tant que contexte n'est ni pratique ni évolutif pour une application d'IA de production. Nous avons besoin d'un système automatisé pour récupérer les informations pertinentes en fonction de la requête d'un utilisateur, les ajouter comme contexte à l'invite, puis exécuter la demande de génération au LLM.

### **Récupération des documents pertinents**

<span id="page-166-2"></span>Un système RAG pour une application d'IA suit généralement trois étapes principales :

*Indexation*

<span id="page-166-3"></span><span id="page-166-1"></span><span id="page-166-0"></span>Cette étape implique le prétraitement de la source de données externe et le stockage des intégrations qui représentent les données dans un

magasin de vecteurs où ils peuvent être facilement récupérés.

#### *Récupération*

Cette étape consiste à récupérer les intégrations et les données pertinentes stockées dans le magasin de vecteurs en fonction de la requête d'un utilisateur.

#### *Génération*

Cette étape consiste à synthétiser l'invite d'origine avec les documents pertinents récupérés comme une invite finale envoyée au modèle pour une prédiction.

Les trois étapes de base ressemblent à la [Figure](#page-167-0) 3-1.

<span id="page-167-0"></span>![](_page_167_Figure_6.jpeg)

Figure 3-1. Les étapes clés du RAG

L'étape d'indexation de ce processus a été largement couverte dans le [Chapitre](#page-93-0) 2, où vous avez appris à utiliser les chargeurs de documents,

séparateurs de texte, intégrations et magasins de vecteurs.

Reprenons un exemple à partir de zéro, en commençant par l'étape d'indexation :

<span id="page-168-1"></span>*Python*

```
from langchain_community.document_loaders import
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCha
from langchain_postgres.vectorstores import PGVec
```

```
# Load the document, split it into chunks
raw_documents = TextLoader('./test.txt').load()
text_splitter = RecursiveCharacterTextSplitter(ch
 chunk_overlap=200)
documents = text_splitter.split_documents(raw_doc
```

```
# embed each chunk and insert it into the vector 
model = OpenAIEmbeddings()
connection = 'postgresql+psycopg://langchain:lang
db = PGVector.from_documents(documents, model, co
```
<span id="page-168-0"></span>*JavaScript*

```
import { TextLoader } from "langchain/document_lo
import { RecursiveCharacterTextSplitter } from "@
import { OpenAIEmbeddings } from "@langchain/open
import { PGVectorStore } from "@langchain/communi
// Load the document, split it into chunks
const loader = new TextLoader("./test.txt");
const raw_docs = await loader.load();
const splitter = new RecursiveCharacterTextSplitt
 chunkSize: 1000,
 chunkOverlap: 200,
});
const docs = await splitter.splitDocuments(docs)
// embed each chunk and insert it into the vector
const model = new OpenAIEmbeddings();
const db = await PGVectorStore.fromDocuments(docs
 postgresConnectionOptions: {
 connectionString: 'postgresql://langchain:lan
 }
})
```
[Chapitre](#page-93-0) 2 contient plus de détails sur l'étape d'indexation.

<span id="page-169-0"></span>L'étape d'indexation est maintenant terminée. Afin d'exécuter l'étape de récupération, nous devons effectuer des calculs de recherche de similarité, tels que la similarité cosinus, entre les noms de l'utilisateur.

requête et nos intégrations stockées, de sorte que les morceaux pertinents de notre document indexé soient récupérés (voir [Figure](#page-171-0) 3-2).

<span id="page-171-0"></span>![](_page_171_Figure_0.jpeg)

Figure 3-2. Un exemple de flux de documents d'indexation parallèlement à la récupération de documents pertinents à partir d'un magasin vectoriel ; la boîte Hierarchical Navigable Small World (HNSW) représente le calcul de la similarité des documents par rapport à la requête de l'utilisateur

La <span id="page-172-0"></span>[Figure](#page-171-0) 3-2 illustre les étapes du processus de récupération :

- 1. Convertissez la requête de l'utilisateur en intégrations.
- 2. Calculez les intégrations dans le magasin de vecteurs qui ressemblent le plus à la requête de l'utilisateur.
- 3. Récupérez les intégrations de documents pertinentes et leur morceau de texte correspondant.
Nous pouvons représenter ces étapes par programme en utilisant LangChain comme suit :

#### <span id="page-172-2"></span>*Python*

```
# create retriever
retriever = db.as_retriever()
# fetch relevant documents
docs = retriever.invoke("""Who are the key figure
 history of philosophy?""")
```
#### <span id="page-172-1"></span>*JavaScript*

```
// create retriever
const retriever = db.asRetriever()
```

```
// fetch relevant documents
const docs = await retriever.invoke(`Who are the 
 greek history of philosophy?`)
```
Notez que nous utilisons une méthode de stockage vectoriel que vous n'avez jamais vue auparavant : as\_retriever . Cette fonction résume la logique d'intégration de la requête de l'utilisateur et les calculs de recherche de similarité sous-jacents effectués par le magasin de vecteurs pour récupérer les documents pertinents.

<span id="page-173-0"></span>Il existe également un argument k , qui détermine le nombre de documents pertinents à récupérer dans le magasin de vecteurs. Par exemple :

*Python*

```
# create retriever with k=2
retriever = db.as_retriever(search_kwargs={"k": 2
# fetch the 2 most relevant documents
docs = retriever.invoke("""Who are the key figure
 of philosophy?""")
```
*JavaScript*

```
// create retriever with k=2
const retriever = db.asRetriever({k: 2})
// fetch the 2 most relevant documents
const docs = await retriever.invoke(`Who are the 
 greek history of philosophy?`)
```
Dans cet exemple, l'argument k est spécifié comme 2. Cela indique au magasin de vecteurs de renvoyer les deux documents les plus pertinents en fonction de la requête de l'utilisateur.

Il peut sembler contre-intuitif d’utiliser une valeur k faible, mais il n’est pas toujours préférable de récupérer davantage de documents. Plus de documents sont récupérés, plus votre application fonctionnera lentement, plus l'invite (et le coût de génération associé) sera grande et plus grande sera la probabilité de récupérer des morceaux de texte contenant des informations non pertinentes, ce qui provoquera des hallucinations du LLM.

<span id="page-174-0"></span>Maintenant que nous avons terminé l'étape de récupération du système RAG, passons à l'étape de génération finale.

### **Génération de prédictions LLM à l'aide de documents pertinents**

<span id="page-175-1"></span>Une fois que nous avons récupéré les documents pertinents en fonction de la requête de l'utilisateur, la dernière étape consiste à les ajouter à l'invite d'origine en tant que contexte, puis à invoquer le modèle pour générer une sortie finale [\(Figure](#page-175-0) 3-3).

<span id="page-175-0"></span>![](_page_175_Figure_1.jpeg)

Figure 3-3. Un exemple de flux illustrant l'indexation de documents, la récupération de documents pertinents à partir d'un magasin de vecteurs et l'inclusion de documents récupérés comme contexte dans l'invite LLM

Voici un exemple de code faisant suite à notre exemple précédent :

<span id="page-176-0"></span>*Python*

```
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemp
retriever = db.as_retriever()
prompt = ChatPromptTemplate.from_template("""Answ
 the following context:
{context}
Question: {question}
""")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temp
chain = prompt | llm
# fetch relevant documents 
docs = retriever.get_relevant_documents("""Who ar
 ancient greek history of philosophy?""")
# run
```
h i i k ({" t t" d " ti " """Wh

```
chain.invoke({"context": docs,"question": """Who 
 ancient greek history of philosophy?"""})
```
<span id="page-177-0"></span>*JavaScript*

```
import {ChatOpenAI} from '@langchain/openai'
import {ChatPromptTemplate} from '@langchain/core
const retriever = db.asRetriever()
const prompt = ChatPromptTemplate.fromTemplate(`A
 on the following context:
{context}
Question: {question}
`)
const llm = new ChatOpenAI({temperature: 0, model
const chain = prompt.pipe(llm)
// fetch relevant documents
const docs = await retriever.invoke(`Who are the 
 greek history of philosophy?`)
await chain.invoke({context: docs, question: `Who
 ancient greek history of philosophy?`})
```
![](_page_178_Picture_0.jpeg)

Notez les changements suivants :

- Nous implémentons des variables de contexte et de question dynamiques dans notre invite, ce qui nous permet de définir un ChatPromptTemplate que le modèle peut utiliser pour générer une réponse.
- Nous définissons une interface ChatOpenAI pour faire office de LLM. La température est réglée sur 0 pour éliminer la créativité dans les sorties du modèle.
- Nous créons une chaîne pour composer le prompt et le LLM. Un rappel : le | L'opérateur (ou méthode pipe en JS) prend la sortie de l'invite et l'utilise comme entrée pour llm .
- Nous invoquons la chaîne passant dans la variable de contexte (nos documents pertinents récupérés) et la question de l'utilisateur pour générer une sortie finale.
Nous pouvons encapsuler cette logique de récupération dans une seule fonction :

#### *Python*

depuis langchain\_openai importer ChatOpenAI depuis langchain\_core.prompts importer ChatPromptTemp depuis langchain\_core.runnables chaîne d'importation

```
retriever = db.as_retriever()
prompt = ChatPromptTemplate.from_template("""Answ
 the following context:
{context}
Question: {question}
""")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperatu
@chain
def qa(input):
 # fetch relevant documents 
 docs = retriever.get_relevant_documents(input
 # format prompt
 formatted = prompt.invoke({"context": docs,
                                              "
 # generate answer
 answer = llm.invoke(formatted)
 return answer
# run
qa.invoke("Who are the key figures in the ancient
```
*JavaScript*

```
import {ChatOpenAI} from '@langchain/openai'
import {ChatPromptTemplate} from '@langchain/core
import {RunnableLambda} from '@langchain/core/run
const retriever = db.asRetriever()
const prompt = ChatPromptTemplate.fromTemplate(`A
 on the following context:
{context}
Question: {question}
`)
const llm = new ChatOpenAI({temperature: 0, model
```

```
const qa = RunnableLambda.from(async input => {
 // fetch relevant documents
 const docs = await retriever.invoke(input)
 // format prompt
 const formatted = await prompt.invoke({context
 // generate answer
 const answer = await llm.invoke(formatted)
 return answer
})
```
attendre qa.invoke(`Who are the key figures in the a philosophy?`)

| p<br>p<br>y<br>) |  |
|------------------|--|
|                  |  |
|                  |  |
|                  |  |

Remarquez que nous disposons désormais d'une nouvelle fonction qa exécutable qui peut être appelée avec une simple question et qui prend soin de récupérer d'abord les documents pertinents pour le contexte, de les formater dans l'invite et enfin de générer la réponse. Dans le code Python, le décorateur @chain transforme la fonction en une chaîne exécutable. Cette notion d'encapsulation de plusieurs étapes dans une seule fonction sera essentielle pour créer des applications intéressantes avec les LLM.

Vous pouvez également renvoyer les documents récupérés pour une inspection plus approfondie :

#### *Python*

```
@chain
def qa(input):
 # fetch relevant documents 
 docs = retriever.get_relevant_documents(input
 # format prompt
 formatted = prompt.invoke({"context": docs,
                                             "
 # generate answer
 answer = llm.invoke(formatted)
 return {"answer": answer, "docs": docs}
```
#### *JavaScript*

```
const qa = RunnableLambda.from(async input => {
 // fetch relevant documents
 const docs = await retriever.invoke(input)
 // format prompt
 const formatted = await prompt.invoke({context
 // generate answer
 const answer = await llm.invoke(formatted)
 return {answer, docs}
})
```
Félicitations ! Vous avez maintenant créé un système RAG de base pour alimenter une application d'IA destinée à un usage personnel.

<span id="page-182-0"></span>Cependant, une application d'IA prête pour la production et utilisée par plusieurs utilisateurs nécessite un système RAG plus avancé. Afin de construire un système RAG robuste, nous devons répondre efficacement aux questions suivantes :

- Comment gérons-nous la variabilité de la qualité de la contribution d'un utilisateur ?
- Comment acheminer les requêtes pour récupérer des données pertinentes à partir de diverses sources de données ?
- Comment transformer le langage naturel en langage de requête de la source de données cible ?
- Comment optimiser notre processus d'indexation, c'est-à-dire l'intégration, le fractionnement du texte ?

Nous discuterons ensuite des dernières stratégies fondées sur la recherche pour répondre à ces questions et créer un système RAG prêt pour la production. Ces stratégies peuvent être résumées dans la [Figure](#page-183-0) 3-4.

<span id="page-183-0"></span>![](_page_183_Figure_3.jpeg)

Figure 3-4. Stratégies efficaces pour optimiser la précision de votre système RAG

#### **REMARQUE**

<span id="page-184-0"></span>Tous les blocs de code du reste de ce chapitre utilisent le magasin de vecteurs que nous avons configuré au début du chapitre.

## Transformation de requête

<span id="page-184-1"></span>L'un des problèmes majeurs d'un système RAG de base est qu'il s'appuie trop sur la qualité de la requête d'un utilisateur pour générer un résultat précis. Dans un environnement de production, un utilisateur est susceptible de construire sa requête de manière incomplète, ambiguë ou mal formulée, ce qui conduit à une hallucination du modèle.
<span id="page-184-3"></span><span id="page-184-2"></span>*La transformation de requête* est un sous-ensemble de stratégies conçues pour modifier la saisie de l'utilisateur afin de répondre à la première question du problème RAG : Comment gérer la variabilité de la qualité de la saisie d'un utilisateur ? La [Figure](#page-185-0) 3-5 illustre la gamme de stratégies de transformation de requêtes, allant de celles qui rendent la saisie d'un utilisateur plus ou moins abstraite afin de générer une sortie LLM précise. La section suivante commence par une stratégie intermédiaire.

<span id="page-185-0"></span>![](_page_185_Figure_0.jpeg)

Figure 3-5. Diverses méthodes pour transformer la requête d'un utilisateur en fonction du niveau d'abstraction

### **Réécrire-Récupérer-Lire**

<span id="page-185-2"></span><span id="page-185-1"></span>La stratégie Réécriture-Récupération-Lecture proposée par une équipe Microsoft Research invite simplement le LLM à réécrire la requête de l'utilisateur avant d'effectuer la récupération. Pour illustrer, revenons à la chaîne que nous avons construite dans la section précédente, cette fois invoquée avec une requête utilisateur mal formulée : **[2](#page-235-1)**

*Python*

```
@chain
def qa(input):
 # fetch relevant documents 
 docs = retriever.get_relevant_documents(input
 # format prompt
 formatted = prompt.invoke({"context": docs,
                                             "
 # generate answer
 answer = llm.invoke(formatted)
 return answer
qa.invoke("""Today I woke up and brushed my teeth
```

```
 news. But then I forgot the food on the cooke
 the ancient greek history of philosophy?""")
```
#### *JavaScript*

```
const qa = RunnableLambda.from(async input => {
 // fetch relevant documents
 const docs = await retriever.invoke(input)
 // format prompt
 const formatted = await prompt.invoke({context
 // generate answer
 const answer = await llm.invoke(formatted)
 return answer
})
```
ça je k (`T d I k d b h d t

__PROTECTED_CODE_3__
*The output* (remember: if you rerun it, your output might be different from this):

__PROTECTED_CODE_4__
The model failed to answer the question because it was distracted by the irrelevant information provided in the user's query.

Now let's implement the Rewrite-Retrieve-Read prompt:

<span id="page-187-0"></span>*Python*

__PROTECTED_CODE_5__

__PROTECTED_CODE_6__
<span id="page-188-0"></span>*JavaScript*

const rewritePrompt = ChatPromptTemplate.fromTemp query for web search engine to answer the given with '\*\*'. Question: {question} Answer:`)

const rewriter = rewritePrompt pipe(llm) pipe(mes

```
const rewriter = rewritePrompt.pipe(llm).pipe(mes
 return message.content.replaceAll('"'
                                       ,
                                         '').repl
})
const qa = RunnableLambda.from(async input => {
 const newQuery = await rewriter.invoke({questio
 // fetch relevant documents
 const docs = await retriever.invoke(newQuery)
 // format prompt
 const formatted = await prompt.invoke({context
 // generate answer
 const answer = await llm.invoke(formatted)
 return answer
})
await qa.invoke(`Today I woke up and brushed my t
 the news. But then I forgot the food on the coo
 figures in the ancient greek history of philoso
```
*La sortie :*

Sur la base du contexte donné, certains personnages clés de la philosophie incluent : Thémistocle (un sta
Notez que nous avons demandé à un LLM de réécrire la requête distraite initiale de l'utilisateur en une requête beaucoup plus claire, et c'est cette requête plus ciblée qui est transmise au récupérateur pour récupérer les documents les plus pertinents. Remarque : cette technique peut être utilisée avec n'importe quelle méthode de récupération, qu'il s'agisse d'un magasin vectoriel comme celui que nous avons ici ou, par exemple, d'un outil de recherche sur le Web. L'inconvénient de cette approche est qu'elle introduit une latence supplémentaire dans votre chaîne, car nous devons désormais effectuer deux appels LLM en séquence.

### <span id="page-190-1"></span>**Récupération multi-requêtes**

<span id="page-190-0"></span>La requête unique d'un utilisateur peut s'avérer insuffisante pour capturer l'ensemble des informations requises pour répondre de manière exhaustive à la requête. La stratégie de récupération multi-requêtes résout ce problème en demandant à un LLM de générer plusieurs requêtes basées sur la requête initiale d'un utilisateur, en exécutant une récupération parallèle de chaque requête à partir de la source de données, puis en insérant les résultats récupérés comme contexte d'invite pour générer une sortie de modèle finale. [Figure](#page-191-0) 3-6 illustre.

<span id="page-191-0"></span>![](_page_191_Figure_0.jpeg)

Figure 3-6. Démonstration de la stratégie de récupération multi-requêtes

Cette stratégie est particulièrement utile pour les cas d'utilisation où une seule question peut s'appuyer sur plusieurs perspectives pour fournir une réponse complète.

Voici un exemple de code de récupération multi-requêtes en action :

<span id="page-191-1"></span>*Python*

![](_page_191_Picture_5.jpeg)

 recherche de similarité. Fournissez ces nouvelles lignes alternatives. Question initiale : {question}""")

```
def parse_queries_output(message):
 return message.content.split('\n')
```

```
query_gen = perspectives_prompt | llm | parse_que
```
<span id="page-192-0"></span>*JavaScript*

```
const perspectivesPrompt = ChatPromptTemplate.fro
 language model assistant. Your task is to gener
 of the given user question to retrieve relevant
 database. By generating multiple perspectives o
 goal is to help the user overcome some of the l
 distance-based similarity search. Provide these
 separated by newlines. Original question: {ques
const queryGen = perspectivesPrompt.pipe(llm).pip
 return message.content.split('\n')
})
```
Notez que le modèle d'invite est conçu pour générer des variantes de questions basées sur la requête initiale de l'utilisateur. Ensuite, nous prenons la liste des requêtes générées, récupérons les documents les plus pertinents pour chacune d'elles en parallèle, puis combinons pour obtenir l'union unique de tous les documents pertinents récupérés :

*Python*

```
def get_unique_union(document_lists):
 # Flatten list of lists, and dedupe them
 deduped_docs = {
 doc.page_content: doc
 for sublist in document_lists for doc in
 }
 # return a flat list of unique docs
 return list(deduped_docs.values())
retrieval_chain = query_gen | retriever.batch | g
```
*JavaScript*

```
const retrievalChain = queryGen
 .pipe(retriever.batch.bind(retriever))
 .pipe(documentLists => {
 const dedupedDocs = {}
 documentLists.flat().forEach(doc => {
```

```
 dedupedDocs[doc.pageContent] = doc
 })
 return Object.values(dedupedDocs)
 })
```
Étant donné que nous récupérons des documents du même récupérateur avec plusieurs requêtes (liées), il est probable qu'au moins certaines d'entre elles soient répétées. Avant de les utiliser comme contexte pour répondre à la question, nous devons les dédupliquer, pour obtenir une seule instance de chacun. Ici, nous déduisons les documents en utilisant leur contenu (une chaîne) comme clé dans un dictionnaire (ou objet en JS), car un dictionnaire ne peut contenir qu'une seule entrée pour chaque clé. Après avoir parcouru tous les documents, nous obtenons simplement toutes les valeurs du dictionnaire, qui sont désormais exemptes de doublons.

Notez également notre utilisation de .batch , qui exécute toutes les requêtes générées en parallèle et renvoie une liste des résultats – dans ce cas, une liste de listes de documents, que nous aplatissons et déduisons ensuite comme décrit précédemment.

Cette dernière étape consiste à construire une invite, comprenant la question de l'utilisateur et les documents pertinents récupérés combinés, ainsi qu'une interface modèle pour générer la prédiction :

*Python*

```
prompt = ChatPromptTemplate.from_template("""Answ
 on this context:
{context}
Question: {question}
""")
@chain
def multi_query_qa(input):
 # fetch relevant documents 
 docs = retrieval_chain.invoke(input)
 # format prompt
 formatted = prompt.invoke({"context": docs,
                                              "
 # generate answer
 answer = llm.invoke(formatted)
 return answer
# run
multi_query_qa.invoke("""Who are some key figures
 of philosophy?""")
```
*JavaScript*

const invite = ChatPromptTemplate.fromTemplate(`A
```
 question based on this context:
{context}
Question: {question}
`)
const multiQueryQa = RunnableLambda.from(async in
 // fetch relevant documents
 const docs = await retrievalChain.invoke(input)
 // format prompt
 const formatted = await prompt.invoke({context
 // generate answer
 const answer = await llm.invoke(formatted)
 return answer
})
await multiQueryQa.invoke(`Who are some key figur
 history of philosophy?`)
```
<span id="page-196-0"></span>Remarquez à quel point cela n'est pas si différent de nos précédentes chaînes d'assurance qualité, car toute la nouvelle logique pour la récupération multi-requêtes est contenue dans retrieval\_chain . C'est la clé pour faire bon usage de ces techniques : implémenter chaque technique comme une chaîne autonome (dans ce cas, retrieval\_chain ), ce qui facilite leur adoption et même leur combinaison.

### **RAG-Fusion**

<span id="page-197-2"></span><span id="page-197-0"></span>La stratégie RAG-Fusion partage des similitudes avec la stratégie de récupération multi-requêtes, sauf que nous appliquerons une étape finale de reclassement à tous les documents récupérés. Cette étape de reclassement utilise l'algorithme de *fusion de rangs réciproques* (RRF), qui consiste à combiner les classements de différents résultats de recherche pour produire un classement unique et unifié. En combinant les classements de différentes requêtes, nous plaçons les documents les plus pertinents en haut de la liste finale. RRF est bien adapté pour combiner les résultats de requêtes pouvant avoir différentes échelles ou distributions de scores. **[3](#page-235-2)**

Montrons RAG-Fusion dans le code. Tout d’abord, nous créons une invite similaire à la stratégie de récupération multi-requêtes pour générer une liste de requêtes basées sur la requête de l’utilisateur :

#### <span id="page-197-1"></span>*Python*

depuis langchain.prompts importer ChatPromptTemplate depuis langchain\_openai importer ChatOpenAI

```
prompt_rag_fusion = ChatPromptTemplate.from_templ
 assistant that generates multiple search quer
 query. \n
```
Générez plusieurs requêtes de recherche liées à :

```
 Generate multiple search queries related to: 
 Output (4 queries):""")
def parse_queries_output(message):
 return message.content.split('\n')
llm = ChatOpenAI(temperature=0)
query_gen = prompt_rag_fusion | llm | parse_queri
```
#### <span id="page-198-0"></span>*JavaScript*

```
import {ChatPromptTemplate} from '@langchain/core
import {ChatOpenAI} from '@langchain/openai';
import {RunnableLambda} from '@langchain/core/run
const perspectivesPrompt = ChatPromptTemplate.fro
 assistant that generates multiple search querie
 query. \n
 Generate multiple search queries related to: {q
 Output (4 queries):`)
const queryGen = perspectivesPrompt.pipe(llm).pip
```

```
 return message.content.split('\n')
})
```
Une fois que nous avons généré nos requêtes, nous récupérons les documents pertinents pour chaque requête et les transmettons à une fonction pour *reclasser* (c'est-à-dire *réorganiser* en fonction de la pertinence) la liste finale des documents pertinents.

La fonction reciprocal\_rank\_fusion prend une liste des résultats de recherche de chaque requête, donc une liste de listes de documents, où chaque liste interne de documents est triée selon leur pertinence pour cette requête. L'algorithme RRF calcule ensuite un nouveau score pour chaque document en fonction de son classement (ou position) dans les différentes listes et les trie pour créer une liste finale reclassée.

Après avoir calculé les scores fusionnés, la fonction trie les documents par ordre décroissant de ces scores pour obtenir la liste finale reclassée, qui est ensuite renvoyée :

*Python*

def reciprocal\_rank\_fusion(results : list[list], k """fusion de rangs réciproques sur plusieurs listes o et un paramètre facultatif k utilisé dans le RR """

```
 # Initialize a dictionary to hold fused score
 # Documents will be keyed by their contents t
 fused_scores = {}
 documents = {}
```

```
 # Iterate through each list of ranked documen
 for docs in results:
 # Iterate through each document in the li
 # with its rank (position in the list)
 for rank, doc in enumerate(docs):
 # Use the document contents as the ke
 doc_str = doc.page_content
 # If the document hasn't been seen ye
 # - initialize score to 0
 # - save it for later
 if doc_str not in fused_scores:
 fused_scores[doc_str] = 0
 documents[doc_str] = doc
 # Update the score of the document us
 # 1 / (rank + k)
 fused_scores[doc_str] += 1 / (rank +
 # Sort the documents based on their fused sco
 # to get the final reranked results
 reranked_doc_strs = sorted(
```

```
 fused_scores, key=lambda d: fused_scores[
```
# récupérer la doc correspondante pour chaque doc

```
 )
```

```
 # récupérer la doc correspondante pour chaque doc
 revenir [
documents[doc_str]
 pour doc_str dans reranked_doc_strs
 ]
récupération_chain = générer_queries | retriever.ba
```
#### *JavaScript*

```
fonction reciprocalRankFusion (résultats, k = 60) {
 // Initialise un dictionnaire pour contenir les scores fusionnés
 // Les documents seront indexés par leur contenu pour
 const fusedScores = {}
 const documents = {}
 résultats.forEach(docs => {
 docs.forEach((doc, rang) => {
 // Utilise le contenu du document comme clé pour
 clé const = doc.pageContent
 // Si le document n'a pas encore été vu,
 // - initialise le score à 0
 // - sauvegarde-le pour plus tard
 if (!(entrez fusedScores)) {
 fusedScores[clé] = 0
```
d t [k ] 0

```
 documents[clé] = 0
 }
 // Mettre à jour la partition du document en utilisant t
 // 1 / (rang + k)
 fusedScores[clé] += 1 / (rang + k)
 })
 })
 // Trie les documents en fonction de leur score fusionné
 // pour obtenir les résultats finaux reclassés
 const trié = Object.entries (fusedScores).sort
 // récupère la doc correspondante pour chaque clé
 return sorted.map(([clé]) => documents[clé])
}
const récupérationChain = queryGen
 .pipe(retriever.batch.bind(récupérateur))
 .pipe (réciprocalRankFusion)
```
<span id="page-202-0"></span>Notice that the function also takes a k parameter, which determines how much influence documents in each query's result sets have over the final list of documents. A higher value indicates that lower-ranked documents have more influence.

Finally, we combine our new retrieval chain (now using RRF) with the full chain we've seen before:

*Python*

```
prompt = ChatPromptTemplate.from_template("""Réponse
 dans ce contexte :
{contexte}
Question : {question}
""")
llm = ChatOpenAI (température = 0)
@chaine
def multi_query_qa (entrée) :
 # récupérer les documents pertinents 
 docs = retrieval_chain.invoke (entrée)
 # invite de formatage
 formaté = prompt.invoke({"context": docs,
                                              "
 # générer une réponse
 réponse = llm.invoke (formaté)
 retourner la réponse
multi_query_qa.invoke("""Qui sont les chiffres clés
 de philosophie?""")
```
#### *JavaScript*

```
const rewritePrompt = ChatPromptTemplate.fromTemp
 question basée sur ce contexte:
{contexte}
Question : {question}
`)
const llm = new ChatOpenAI({temperature: 0})
const multiQueryQa = RunnableLambda.from(async in
 // fetch relevant documents
 const docs = await retrievalChain.invoke(input)
 // format prompt
 const formatted = await prompt.invoke({context
 // generate answer
 const answer = await llm.invoke(formatted)
 return answer
})
__PROTECTED_CODE_4__
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutp
from langchain_openai import ChatOpenAI
prompt_hyde = ChatPromptTemplate.from_template(""
 answer the question.\n Question: {question} \n
__PROTECTED_CODE_5__
 prompt_hyde | ChatOpenAI(temperature=0) | Str
)
__PROTECTED_CODE_6__
import {ChatOpenAI} from '@langchain/openai'
import {ChatPromptTemplate} from '@langchain/core
import {RunnableLambda} from '@langchain/core/run
const prompt = ChatPromptTemplate.fromTemplate(`P
 répondre à la question
Question : {question}
Passage :`)
const llm = new ChatOpenAI({temperature: 0})
const generateDoc = prompt.pipe(llm).pipe(msg =>
```
Ensuite, nous prenons le document hypothétique et l'utilisons comme entrée du retriever , qui générera son intégration et recherchera des documents similaires dans le magasin de vecteurs :

*Python*

récupération\_chain **=** générer\_doc **|** récupérateur
*JavaScript*

```
const retrievalChain = generateDoc.pipe(retriever
```
Enfin, nous prenons les documents récupérés, les transmettons comme contexte à l'invite finale et demandons au modèle de générer une sortie :

*Python*

@chaine

```
prompt = ChatPromptTemplate.from_template("""Answ
 on this context:
{context}
Question: {question}
""")
llm = ChatOpenAI(temperature=0)
```

```
@chain
def qa(input):
 # fetch relevant documents from the hyde retrie
 docs = retrieval_chain.invoke(input)
 # format prompt
 formatted = prompt.invoke({"context": docs, "qu
 # generate answer
 answer = llm.invoke(formatted)
 return answer
qa.invoke("""Who are some key figures in the anci
 philosophy?""")
```
*JavaScript*

```
const prompt = ChatPromptTemplate.fromTemplate(`A
 question based on this context:
{context}
Question: {question}
`)
const llm = new ChatOpenAI({temperature: 0})
const qa = RunnableLambda.from(async input => {
  // fetch relevant documents from the hyde retri
```

```
 // fetch relevant documents from the hyde retri
 const docs = await retrievalChain.invoke(input)
 // format prompt
 const formatted = await prompt.invoke({context
 // generate answer
 const answer = await llm.invoke(formatted)
 return answer
})
await qa.invoke(`Who are some key figures in the 
 philosophy?`)
```
Pour récapituler ce que nous avons abordé dans cette section, la transformation de requête consiste à prendre la requête d'origine de l'utilisateur et à effectuer les opérations suivantes :

- Réécriture en une ou plusieurs requêtes
- Combiner les résultats de ces requêtes en un seul ensemble de résultats les plus pertinents

La réécriture de la requête peut prendre plusieurs formes, mais elle s'effectue généralement de la même manière : prenez la requête d'origine de l'utilisateur (une invite que vous avez écrite) et demandez à un LLM d'écrire une ou plusieurs nouvelles requêtes. Voici quelques exemples de modifications typiques apportées :

Suppression du texte non pertinent/sans rapport de la requête.

- Baser la requête sur l'historique des conversations passées. Par exemple, pour donner un sens à une requête telle que *et qu'en est-il à Los Angeles*, nous devons la combiner avec une question hypothétique passée sur la météo à SF, pour arriver à une requête utile telle que *météo à Los Angeles*.
- Élargir le réseau pour les documents pertinents en récupérant également des documents pour des requêtes connexes.
- Décomposer une question complexe en plusieurs questions plus simples, puis inclure les résultats de chacune d'entre elles dans l'invite finale pour générer une réponse.

La bonne stratégie de réécriture à utiliser dépendra de votre cas d'utilisation.

Maintenant que nous avons couvert les principales stratégies de transformation des requêtes, abordons la deuxième question majeure à laquelle il faut répondre afin de construire un système RAG robuste : comment acheminer les requêtes pour récupérer des données pertinentes à partir de plusieurs sources de données ?

## <span id="page-211-1"></span>Routage des requêtes

<span id="page-211-0"></span>Bien que l'utilisation d'un seul magasin de vecteurs soit utile, les données requises peuvent résider dans diverses sources de données, notamment des bases de données relationnelles ou d'autres magasins de vecteurs.

Par exemple, vous pouvez avoir deux magasins de vecteurs : un pour la documentation LangChain Python et un autre pour la documentation LangChain JS. Compte tenu de la question d'un utilisateur, nous aimerions *acheminer* la requête vers la source de données déduites appropriée pour récupérer les documents pertinents. Le *routage des requêtes* est une stratégie utilisée pour transmettre la requête d'un utilisateur vers la source de données appropriée.

### <span id="page-212-2"></span>**Routage logique**

<span id="page-212-1"></span>Dans le *routage logique*, nous donnons au LLM la connaissance des différentes sources de données à notre disposition, puis laissons le LLM déterminer quelle source de données appliquer en fonction de la requête de l'utilisateur, comme indiqué dans la [Figure](#page-212-0) 3-8.

<span id="page-212-0"></span>![](_page_212_Figure_3.jpeg)

Figure 3-8. Routage des requêtes vers les sources de données pertinentes

<span id="page-213-0"></span>Pour y parvenir, nous utilisons des modèles d'appel de fonctions tels que GPT-3.5 Turbo pour nous aider à classer chaque requête dans l'une des routes disponibles. Un *appel de fonction* implique de définir un schéma que le modèle peut utiliser pour générer les arguments d'une fonction basée sur la requête. Cela nous permet de générer des sorties structurées qui peuvent être utilisées pour exécuter d'autres fonctions. Le code Python suivant définit le schéma de notre routeur sur la base de trois documents pour différents langages :

<span id="page-213-1"></span>*Python*

)

```
en tapant import Literal
à partir de langchain_core.prompts, importez ChatPromptTemp
à partir de langchain_core.pydantic_v1, importez BaseModel,
depuis langchain_openai importer ChatOpenAI
# Modèle de données
classe RouteQuery (BaseModel) :
 """Acheminer une requête utilisateur vers la donnée la plus pertinente
 source de données : littéral["python_docs"
                                   ,
"js_docs"]
 ...,
 description="""Étant donné une question d'utilisateur, cho
 le plus pertinent pour répondre à leur question
```

```
 )
# LLM avec appel de fonction 
llm = ChatOpenAI(model="gpt-3.5-turbo"
                                    , température
structuré_llm = llm.with_structured_output(Route
# Invite 
system = """Vous êtes un expert dans le routage d'un utilisateur q
 source.
Basé sur le langage de programmation, la question est
 source de données pertinente."""
prompt = ChatPromptTemplate.from_messages(
 [
 ("système"
                , système),
 ("humain"
               ,
                 "{question}"),
 ]
)
# Définir le routeur 
routeur = invite | structuré_llm
```
<span id="page-214-0"></span>*JavaScript*

```
importer { ChatOpenAI } depuis "@langchain/openai" ;
importer { z } depuis "zod" ;
```

```
const routeQuery = z.object({
 source de données : z.enum(["python_docs", "js_docs"])
 question, choisissez quelle source de données serait mo
 leur question`),
}).describe("Route a user query to the most relev
const llm = new ChatOpenAI({model: "gpt-3.5-turbo
const structuredLlm = llm.withStructuredOutput(ro
const prompt = ChatPromptTemplate.fromMessages([
 ['system', `Vous êtes un expert dans le routage d'un utilisateur
 source de données.
Basé sur le langage de programmation, la question est
```
Now we invoke the LLM to extract the data source based on the predefined schema:

const router = prompt.pipe(structuredLlm)

the relevant data source.`],

['human', '{question}']

*Python*

])

```
question = """Pourquoi le code suivant ne fonctionne-t-il pas
à partir de langchain_core.prompts, importez ChatPromptTemp
prompt = ChatPromptTemplate.from_messages(["humain
prompt.invoke("français")
"""
résultat = routeur.invoke({"question": question})
résultat.source de données
# "python_docs"
```
*JavaScript*

```
question constante = `Why doesn't the following code 
from langchain_core.prompts import ChatPromptTemp
prompt = ChatPromptTemplate.from_messages(["human
prompt.invoke("french")
`
```
await router.invoke({ question })

*The output:*

```
{
 source de données : "python_docs"
}
```
Notice how the LLM produced JSON output, conforming to the schema we defined earlier. This will be useful in many other tasks.

Once we've extracted the relevant data source, we can pass the value into another function to execute additional logic as required:

*Python*

```
def choisir_route (résultat):
 si "python_docs" dans result.datasource.lower()
 ### Logique ici 
 renvoie "chaîne pour python_docs"
 sinon :
```
![](_page_218_Figure_0.jpeg)

#### *JavaScript*

```
fonction choisirRoute (résultat) {
 if (result.datasource.toLowerCase().includes('p
 renvoie 'chaîne pour python_docs' ;
 } autre {
 renvoie 'chaîne pour js_docs' ;
 }
}
const fullChain = router.pipe (choisirRoute)
```
Notice how we don't do an exact string comparison but instead first turn the generated output to lowercase, and then do a substring match. This makes our chain more resilient to the LLM going off script and producing output that doesn't quite conform to the schema we asked for.

Resilience to the random nature of LLM outputs is an important theme to keep in mind when building your LLM applications.

Logical routing is most suitable when you have a defined list of data sources from which relevant data can be retrieved and utilized by the LLM to generate an accurate output. These can range from vector stores to databases and even APIs.

### <span id="page-219-1"></span>**Semantic Routing**

<span id="page-219-3"></span><span id="page-219-2"></span>Unlike logical routing, *semantic routing* involves embedding various prompts that represent various data sources alongside the user's query and then performing vector similarity search to retrieve the most similar prompt. [Figure](#page-219-0) 3-9 illustrates.

<span id="page-219-0"></span>![](_page_219_Figure_4.jpeg)

Figure 3-9. Semantic routing to improve the accuracy of retrieved documents

#### **TIP**

The following is an example of semantic routing:

<span id="page-220-0"></span>*Python*

```
à partir de langchain.utils.math importer cosine_similarit
à partir de langchain_core.output_parsers importer StrOutp
à partir de langchain_core.prompts, importez PromptTemplate
à partir de la chaîne d'importation langchain_core.runnables
depuis langchain_openai importer ChatOpenAI, OpenAIEm
# Deux invites
physical_template = """Vous êtes un physicien très intelligent
 répondre à des questions sur la physique de manière concise
 Quand tu ne connais pas la réponse à une question,
Voici une question :
{requête}"""
math_template = """Vous êtes un très bon mathématicien
 questions mathématiques. Tu es si bon parce que tu es un
 problèmes dans leurs composants, réponse t
rassemblez-les pour répondre à la quête plus large
Voici une question :
{requête}"""
```
# Embed prompts

```
intégrations = OpenAIEmbeddings()
prompt_templates = [physics_template, math_templa
prompt_embeddings = embeddings.embed_documents(pr
# Acheminer la question vers l'invite
@chaine
def prompt_router (requête) :
 # Intégrer la question
 query_embedding = embeddings.embed_query(quer
 # Calculer la similarité
 similarité = cosinus_similarité([query_embeddi
 # Choisissez l'invite la plus similaire à l'entrée q
 most_similar = prompt_templates[similarité.ar
 return PromptTemplate.from_template(most_simi
sémantique_routeur = (
 invite_router
 | ChatOpenAI()
 | StrOutputParser()
)
print(semantic_router.invoke("Qu'est-ce qu'un trou noir
```
<span id="page-221-0"></span>*JavaScript*

import {cosineSimilarity} from '@langchain/core/u

```
importer {ChatOpenAI, OpenAIEmbeddings} depuis '@lang
importer {PromptTemplate} depuis '@langchain/core/pro
importer {RunnableLambda} depuis '@langchain/core/run
```
import {cosineSimilarity} from @langchain/core/u

```
const physicalTemplate = `You are a very smart phy
 at answering questions about physics in a conci
 manner. When you don't know the answer to a que
 don't know.
__PROTECTED_CODE_3__
Here is a question:
{query}`
```

```
const mathTemplate = `You are a very good mathema
 answering math questions. You are so good becau
 hard problems into their component parts, answe
 then put them together to answer the broader qu
__PROTECTED_CODE_5__
Here is a question:
{query}`
```

```
const intégrations = new OpenAIEmbeddings()
```

```
const promptTemplates = [physicsTemplate, mathTem
const promptEmbeddings = attendre l'intégration.embedDo
```

```
const promptRouter = RunnableLambda.from(query =>
 // Intégrer la question
 const queryEmbedding = attendre l'intégration.embedQu
```

```
 // Calculer la similarité
 similitudes const = cosineSimilarity([queryEmb
 // Choisissez l'invite la plus similaire à l'entrée qu
 const mostSimilar = similarités[0] > similarit
 ? promptTemplates[0]
 : promptTemplates[1]
 retourner PromptTemplate.fromTemplate (mostSimilar)
})
const semanticRouter = promptRouter.pipe (nouveau chat
wait semanticRouter.invoke("Qu'est-ce qu'un trou noir"
```
Now that you've seen how to route a user's query to the relevant data source, let's discuss the third major question when building a robust RAG system: "How do we transform natural language to the query language of the target data source?"

## <span id="page-223-0"></span>Query Construction

<span id="page-224-1"></span>As discussed earlier, RAG is an effective strategy to embed and retrieve relevant unstructured data from a vector store based on a query. But most data available for use in production apps is structured and typically stored in relational databases. In addition, unstructured data embedded in a vector store also contains structured metadata that possesses important information.

<span id="page-224-2"></span>*Query construction* is the process of transforming a natural language query into the query language of the database or data source you are interacting with. See [Figure](#page-224-0) 3-10.

<span id="page-224-0"></span>![](_page_224_Figure_2.jpeg)

Figure 3-10. Illustration of query languages for various data sources

For example, consider the query: *What are movies about aliens in the year 1980?* This question contains an unstructured topic that can be retrieved via embeddings (*aliens*), but it also contains potential structured components (*year == 1980*).

The following sections dive deeper into the various forms of query construction.

### **Text-to-Metadata Filter**

<span id="page-225-1"></span>Most vector stores provide the ability to limit your vector search based on metadata. During the embedding process, we can attach metadata key-value pairs to vectors in an index and then later specify filter expressions when you query the index.

LangChain provides a SelfQueryRetriever that abstracts this logic and makes it easier to translate natural language queries into structured queries for various data sources. The self-querying utilizes an LLM to extract and execute the relevant metadata filters based on a user's query and predefined metadata schema:

#### <span id="page-225-0"></span>*Python*

```
de langchain.chains.query_constructor.base impo
à partir de l'importation langchain.retrievers.self_query.base
depuis langchain_openai importer ChatOpenAI
champs = [
 AttributInfo(
 nom="genre",
```

```
 description="Le genre du film",
 type="chaîne ou liste[chaîne]",
 ),
 AttributInfo(
 nom="année",
description="L'année de sortie du film
 type="entier",
 ),
 AttributInfo(
 nom="directeur",
 description="Le nom du film direct
 type="chaîne",
 ),
 AttributInfo(
 name="rating", description="Une note de 1 à 10
 ),
]
description = "Bref résumé d'un film"
llm = ChatOpenAI (température = 0)
récupérateur = SelfQueryRetriever.from_llm(
 llm, db, description, champs,
)
print(retriever.invoke(
 "Qu'est-ce qu'une science-fiction très bien notée (au-dessus de 8,5) ?
```
g ,

#### <span id="page-227-0"></span>*JavaScript*

```
importer { ChatOpenAI } depuis "@langchain/openai" ;
importer { SelfQueryRetriever } depuis "langchain/ret
importer { FunctionalTranslator } depuis "@langchain/
/**
 * Tout d'abord, nous définissons les attributs que nous voulons être 
 * dans ce cas, nous voulons pouvoir interroger sur t
 * note et durée du film.
 * Nous fournissons également une description de chaque attribut
 * Ceci est utilisé pour générer les invites de requête.
 */
champs const = [
 {
 nom : "genre",
 description : "Le genre du film",
 tapez : "chaîne ou tableau de chaînes",
 },
 {
 nom : "année",
 description : "L'année de sortie du film
 tapez : "numéro",
 },
 {
 nom : "réalisateur",
 description : "Le réalisateur du film",
   tapez : "chaîne"
```

```
 tapez : "chaîne",
 },
 {
 nom : "note",
 description : "La note du film (1-10)"
 tapez : "numéro",
 },
 {
 nom : "longueur",
 description : "La durée du film en minutes
 tapez : "numéro",
 },
];
const description = "Bref résumé d'un film";
const llm = new ChatOpenAI();
const attributsInfos = champs.map((champ) => nouveau
 champ.description, champ.type));

const selfQueryRetriever = SelfQueryRetriever.fro
 llm,
 base de données,
 descriptif,
 attributInfo : attributInfos,
 /**
 * Nous devons utiliser un traducteur qui traduit 
 * format de filtre que le magasin vectoriel peut prendre en charge
 *ici.
  */
```

```
 structuréQueryTranslator : nouveau FunctionalTransl
});
attendre selfQueryRetriever.invoke(
 "Qu'est-ce qu'une science-fiction très bien notée (au-dessus de 8,5) ?
);
```
/

This results in a retriever that will take a user query, and split it into:

- A filter to apply on the metadata of each document first
- A query to use for semantic search on the documents

To do this, we have to describe which fields the metadata of our documents contain; that description will be included in the prompt. The retriever will then do the following:

- 1. Send the query generation prompt to the LLM.
- 2. Parse metadata filter and rewritten search query from the LLM output.
- 3. Convert the metadata filter generated by the LLM to the format appropriate for our vector store.
- 4. Issue a similarity search against the vector store, filtered to only match documents whose metadata passes the generated

<span id="page-230-3"></span>filter.

### **Text-to-SQL**

<span id="page-230-4"></span>SQL and relational databases are important sources of structured data, but they don't interact directly with natural language. Although we can simply use the LLM to translate a user's query to SQL queries, there is little margin for error.

Here are some useful strategies for effective text to SQL translations:

#### *Database description*

<span id="page-230-1"></span>To ground SQL queries, an LLM must be provided with an accurate description of the database. One common text-to-SQL prompt employs an idea reported in this paper and others: provide the LLM with a CREATE TABLE description for each table, including column names and types. We can also provide a few (for instance, three) example rows from the table. **[5](#page-236-1)**

#### <span id="page-230-0"></span>*Few-shot examples*

<span id="page-230-2"></span>Feeding the prompt with few-shot examples of questionquery matches can improve the query generation accuracy. This can be achieved by simply appending

standard static examples in the prompt to guide the agent on how it should build queries based on questions.

<span id="page-231-0"></span>![](_page_231_Figure_1.jpeg)

See [Figure](#page-231-0) 3-11 for a visual of the process.

Figure 3-11. A user's query transformed to a SQL query

Here's a full code example:

#### <span id="page-231-1"></span>*Python*

from langchain\_community.tools import QuerySQLDat from langchain\_community.utilities import SQLData from langchain.chains import create\_sql\_query\_cha from langchain\_openai import ChatOpenAI

```
# remplacez ceci par vos informations de connexion
db = SQLDatabase.from_uri("sqlite:///Chinook.db")
llm = ChatOpenAI(model="gpt-4", température=0)
```

```
# convertir la question en requête SQL
write_query = create_sql_query_chain(llm, db)
# Exécuter la requête SQL
exécuter_query = QuerySQLDatabaseTool(db=db)
# combiné
chaîne = write_query | exécuter_query
# invoque la chaîne
chain.invoke('Combien y a-t-il d'employés ?');
```
<span id="page-232-0"></span>*JavaScript*

```
importer { ChatOpenAI } depuis "@langchain/openai" ;
importer { createSqlQueryChain } depuis "langchain/ch
importer { SqlDatabase } depuis "langchain/sql_db" ;
importer { DataSource } depuis "typeorm" ;
importer { QuerySqlTool } depuis "langchain/tools/sql
const source de données = nouvelle source de données ({
 tapez : "sqlite",
 base de données : "./Chinook.db", // devrait être ici le
});
const db = attendre SqlDatabase.fromDataSourceParams
```

```
 appDataSource : source de données,
});
const llm = new ChatOpenAI({ modèle : "gpt-4", temp
// convertit la question en requête SQL
const writeQuery = wait createSqlQueryChain({ll
// exécute la requête
const exécuterQuery = new QuerySqlTool(db);
// combiné
const chain = writeQuery.pipe(executeQuery);
// invoque la chaîne
wait chain.invoke('Combien y a-t-il d'employés ?
```
Nous convertissons d'abord la requête de l'utilisateur en une requête SQL adaptée au dialecte de notre base de données. Ensuite, nous exécutons cette requête sur notre base de données. Notez que l'exécution de requêtes SQL arbitraires sur votre base de données générées par un LLM à partir d'une entrée utilisateur est dangereuse dans une application de production. Pour utiliser ces idées en production, vous devez prendre en compte un certain nombre de mesures de sécurité afin de réduire le risque d'exécution de requêtes involontaires dans votre base de données. Voici quelques exemples :

- Exécutez les requêtes sur votre base de données avec un utilisateur disposant d'autorisations en lecture seule.
- L'utilisateur de la base de données exécutant les requêtes doit avoir accès uniquement aux tables que vous souhaitez rendre disponibles pour les requêtes.
- Ajouter un time-out aux requêtes exécutées par cette application ; cela garantirait que même si une requête coûteuse est générée, elle est annulée avant d'utiliser trop de ressources de votre base de données.

Il ne s’agit pas d’une liste exhaustive de considérations de sécurité. La sécurité des applications LLM est un domaine actuellement en développement, avec davantage de mesures de sécurité ajoutées aux recommandations à mesure que de nouvelles vulnérabilités sont découvertes.

## <span id="page-234-0"></span>Résumé

Ce chapitre traite de diverses stratégies de pointe pour récupérer efficacement les documents les plus pertinents en fonction de la requête d'un utilisateur et les synthétiser avec votre invite pour aider le LLM à générer une sortie précise et à jour.

Comme indiqué, un système RAG robuste et prêt pour la production nécessite un large éventail de stratégies efficaces capables d'exécuter des requêtes.

transformation, construction de requêtes, routage et optimisation de l'indexation.

<span id="page-235-4"></span><span id="page-235-3"></span>La transformation de requête permet à votre application d'IA de transformer une requête utilisateur ambiguë ou mal formée en une requête représentative optimale pour la récupération. La construction de requêtes permet à votre application d'IA de convertir la requête de l'utilisateur dans la syntaxe du langage de requête de la base de données ou de la source de données où se trouvent les données structurées. Le routage permet à votre application d'IA d'acheminer dynamiquement la requête de l'utilisateur pour récupérer les informations pertinentes à partir de la source de données appropriée.

Dans le [Chapitre](#page-237-0) 4, nous nous appuierons sur ces connaissances pour ajouter de la mémoire à votre chatbot IA afin qu'il puisse se souvenir et apprendre de chaque interaction. Cela permettra aux utilisateurs de « discuter » avec l'application dans des conversations à plusieurs tours comme ChatGPT.

<span id="page-235-0"></span>Patrick Lewis et al., ["Récupération augmentée](https://oreil.ly/Qzd2K) Génération pour les tâches PNL à forte intensité de connaissances", arXiv, 12 avril 2021. **[1](#page-164-0)**

<span id="page-235-1"></span>Xinbei Ma et al., "Query Rewriting for [Retrieval-Augmented](https://oreil.ly/zyw5E) Large Language Models", arXiv, 23 octobre 2023. Recherche commandée par Microsoft Research Asia. **[2](#page-185-1)**

<span id="page-235-2"></span>Zackary Rackauckas, "RAG-Fusion : A New Take on [Retrieval-Augmented](https://oreil.ly/k7TTY) Generation", arXiv, 21 février 2024. Tiré du *International Journal on Natural Language Computing*, vol. 13, non. 1 (février 2024). **[3](#page-197-0)**

- <span id="page-236-0"></span>Luyu Gao et al., "Récupération précise Zero-Shot Dense sans étiquettes [Pertinence](https://oreil.ly/7aTnS)", arXiv, 20 décembre 2022. **[4](#page-205-0)**
- <span id="page-236-1"></span>Nitarshan Rajkumar et al., ["Évaluer](https://oreil.ly/WOrzt) les capacités Text-to-SQL des grands modèles de langage", arXiv, 15 mars 2022. **[5](#page-230-0)**

# <span id="page-237-0"></span>Chapitre 4. Utiliser LangGraph pour ajouter de la mémoire à votre chatbot
Dans le [Chapitre](#page-163-0) 3, vous avez appris comment fournir à votre application de chatbot IA un contexte à jour et pertinent. Cela permet à votre chatbot de générer des réponses précises basées sur les entrées de l'utilisateur. Mais cela ne suffit pas pour créer une application prête pour la production. Comment pouvez-vous permettre à votre application de réellement « discuter » avec l'utilisateur, tout en mémorisant les conversations antérieures et le contexte pertinent ?

<span id="page-237-2"></span><span id="page-237-1"></span>Les grands modèles de langage sont *sans état*, ce qui signifie que chaque fois que le modèle est invité à générer une nouvelle réponse, il n'a aucune mémoire de l'invite ou de la réponse du modèle précédente. Afin de fournir ces informations historiques au modèle, nous avons besoin d'un système de mémoire robuste qui gardera une trace des conversations et du contexte précédents. Ces informations historiques peuvent ensuite être incluses dans l'invite finale envoyée au LLM, lui donnant ainsi une « mémoire ». La [Figure](#page-238-0) 4-1 illustre cela.

<span id="page-238-0"></span>![](_page_238_Figure_0.jpeg)

Figure 4-1. Mémoire et récupération utilisées pour générer des réponses contextuelles à partir d'un LLM

Dans ce chapitre, vous apprendrez comment créer ce système de mémoire essentiel à l'aide des modules intégrés de LangChain pour faciliter ce processus de développement.

## Construire un système de mémoire Chatbot

<span id="page-238-1"></span>Il y a deux décisions de conception fondamentales derrière tout système de mémoire robuste :

- Comment l'état est stocké
- Comment l'état est interrogé

Un moyen simple de créer un système de mémoire de chatbot intégrant des solutions efficaces à ces décisions de conception consiste à stocker et à réutiliser l'historique de toutes les interactions de chat entre l'utilisateur et le modèle. L'état de ce système mémoire peut être :

- Stocké sous forme de liste de messages (reportez-vous au [Chapitre](#page-44-0) 1 pour en savoir plus sur les messages)
- Mis à jour en ajoutant des messages récents après chaque tour
- Ajouté à l'invite en insérant les messages dans l'invite

La [Figure](#page-239-0) 4-2 illustre ce système de mémoire simple.

<span id="page-239-0"></span>![](_page_239_Figure_4.jpeg)

Figure 4-2. Un système de mémoire simple utilisant l'historique des discussions dans les invites pour générer des réponses modèles

Voici un exemple de code qui illustre une version simple de ce système de mémoire utilisant LangChain :

<span id="page-239-1"></span>*Python*

depuis langchain\_core.prompts importer ChatPromptTemp depuis langchain\_openai importer ChatOpenAI

prompt = ChatPromptTemplate à partir des messages ([

```
prompt = ChatPromptTemplate.from_messages([
 ("system", """You are a helpful assistant. An
 of your ability."""),
 ("placeholder",
                 "{messages}"),
])
model = ChatOpenAI()
chain = prompt | model
chain.invoke({
 "messages": [
 ("human","""Translate this sentence from 
 programming."""),
 ("ai", "J'adore programmer."),
 ("human", "What did you just say?"),
 ],
})
```
<span id="page-240-0"></span>*JavaScript*

importer {ChatPromptTemplate} depuis '@langchain/core importer {ChatOpenAI} depuis '@langchain/openai' invite const = ChatPromptTemplate.fromMessages([

```
 ["system", `You are a helpful assistant. Answer
 of your ability.`],
 ["placeholder", "{messages}"],
])
const model = new ChatOpenAI()
const chain = prompt.pipe(model)
await chain.invoke({
 "messages": [
 ["human",`Translate this sentence from Englis
 programming.`],
 ["ai", "J'adore programmer."],
 ["human", "What did you just say?"],
 ],
})
```
#### *Le résultat :*

J'ai dit "J'adore programmer", ce qui veut dire "J'aime

Notez comment l'incorporation de la conversation précédente dans la chaîne a permis au modèle de répondre à la question de suivi d'une manière contextuelle.

Bien que cela soit simple et efficace, lorsque vous mettez votre application en production, vous serez confronté à d'autres défis liés à la gestion de la mémoire à grande échelle, tels que :

- Vous devrez mettre à jour la mémoire après chaque interaction, de manière atomique (c'est-à-dire ne pas enregistrer uniquement la question ou uniquement la réponse en cas d'échec).
- Vous souhaiterez stocker ces souvenirs dans un stockage durable, tel qu'une base de données relationnelle.
- Vous souhaiterez contrôler combien et quels messages sont stockés pour plus tard, et combien d'entre eux sont utilisés pour de nouvelles interactions.
- Vous souhaiterez inspecter et modifier cet état (pour l'instant, juste une liste de messages) en dehors d'un appel à un LLM.

<span id="page-242-0"></span>Nous allons maintenant présenter de meilleurs outils, qui nous aideront dans ce chapitre et dans tous les chapitres suivants.

# Présentation de LangGraph
<span id="page-243-4"></span><span id="page-243-3"></span><span id="page-243-2"></span>Pour le reste de ce chapitre et les chapitres suivants, nous commencerons à utiliser [LangGraph,](https://oreil.ly/TKCb6), une bibliothèque open source créée par LangChain. LangGraph a été conçu pour permettre aux développeurs d'implémenter des architectures cognitives multiacteurs, multi-étapes et avec état, appelées *graphs*. Cela fait beaucoup de mots regroupés dans une courte phrase ; prenons-les un à la fois. La [Figure](#page-243-0) 4-3 illustre l'aspect multiacteur.

<span id="page-243-1"></span><span id="page-243-0"></span>![](_page_243_Figure_1.jpeg)

Figure 4-3. Des applications mono-acteur aux applications multi-acteurs

Une équipe de spécialistes peut construire ensemble quelque chose qu’aucun d’entre eux ne pourrait construire seul. Il en va de même pour les applications LLM : une invite LLM (idéale pour la génération de réponses et la planification de tâches <span id="page-244-0"></span>et bien d'autres choses) est beaucoup plus puissante lorsqu'elle est associée à un moteur de recherche (meilleur pour trouver des faits actuels), ou même lorsqu'elle est associée à différentes invites LLM. Nous avons vu des développeurs créer des applications étonnantes, comme [Perplexity](https://oreil.ly/bVlu7) ou Arc [Search](https://oreil.ly/NPOlF), lorsqu'ils combinent ces deux éléments de base (et d'autres) de manière innovante.

Et tout comme une équipe humaine a besoin de plus de coordination qu’une personne travaillant seule, une application avec plusieurs acteurs a besoin d’une couche de coordination pour faire ces choses :

- Définir les acteurs impliqués (les nœuds dans un graphe) et comment ils se répartissent le travail (les bords de ce graphe).
- Planifier l'exécution de chaque acteur au moment opportun, en parallèle si nécessaire, avec des résultats déterministes.

[Figure](#page-245-0) 4-4 illustre la dimension en plusieurs étapes.

<span id="page-245-0"></span>![](_page_245_Figure_0.jpeg)

Figure 4-4. Des applications multiacteurs aux applications multiétapes

Alors que chaque acteur confie le travail à un autre (par exemple, une invite LLM demandant à un outil de recherche les résultats d'une requête de recherche donnée), nous devons donner un sens aux allers-retours entre plusieurs acteurs. Nous devons savoir dans quel ordre cela se produit,

combien de fois chaque acteur est appelé, et ainsi de suite. Pour ce faire, nous pouvons modéliser l’interaction entre les acteurs comme se produisant à travers plusieurs étapes discrètes dans le temps. Lorsqu'un acteur confie le travail à un autre acteur, cela entraîne la planification de l'étape suivante du calcul, et ainsi de suite, jusqu'à ce qu'aucun acteur ne confie le travail à d'autres et que le résultat final soit atteint.

La [Figure](#page-246-0) 4-5 illustre l'aspect avec état.

<span id="page-246-0"></span>![](_page_246_Figure_2.jpeg)

Figure 4-5. Des applications multi-étapes aux applications avec état

La communication entre les étapes nécessite de suivre un certain état, sinon lorsque vous appellerez l'acteur LLM pour la deuxième fois, vous obtiendrez le même résultat que la première fois. Il est très utile de retirer cet état de chacun des acteurs et de faire en sorte que tous les acteurs collaborent pour mettre à jour un état central unique. Avec un État central unique, nous pouvons :

- Capturez et stockez l'état central pendant ou après chaque calcul.
- Suspendre et reprendre l'exécution, ce qui facilite la récupération des erreurs.
- Implémenter des contrôles humains dans la boucle (plus d'informations à ce sujet dans le [Chapitre](#page-385-0) 8).

Chaque *graphique* est alors composé des éléments suivants :

#### *État*

<span id="page-247-1"></span>Les données reçues de l'extérieur de l'application, modifiées et produites par l'application pendant son exécution.

#### *Nœuds*

<span id="page-247-0"></span>Chaque étape à franchir. Les nœuds sont simplement des fonctions Python/JS, qui reçoivent l'état actuel en entrée et peuvent renvoyer une mise à jour de cet état (c'est-à-dire qu'ils peuvent y ajouter et modifier ou supprimer des données existantes).

#### *Bords*

<span id="page-248-0"></span>Les connexions entre les nœuds. Les bords déterminent le chemin emprunté du premier nœud au dernier, et ils peuvent être fixes (c'est-à-dire qu'après le nœud B, visitez toujours le nœud D) ou conditionnels (évaluer une fonction pour décider du prochain nœud à visiter après le nœud C).

LangGraph propose des utilitaires pour visualiser ces graphiques et de nombreuses fonctionnalités pour déboguer leur fonctionnement en cours de développement. Ces graphiques peuvent ensuite facilement être déployés pour servir les charges de travail de production à grande échelle.

<span id="page-248-2"></span>Si vous avez suivi les instructions du [Chapitre](#page-44-0) 1, LangGraph sera déjà installé. Sinon, vous pouvez l'installer en exécutant l'une des commandes suivantes dans votre terminal :

#### <span id="page-248-3"></span>*Python*

<span id="page-248-1"></span>pip installer langgraph

*JavaScript*
npm je @langchain/langgraph

Pour vous aider à vous familiariser avec LangGraph, nous allons créer un chatbot simple à l'aide de LangGraph, qui est un excellent exemple d'architecture d'appel LLM avec une seule utilisation d'un LLM. Ce chatbot répondra directement aux messages des utilisateurs. Bien que simple, il illustre les concepts fondamentaux de la construction avec LangGraph.

## <span id="page-249-0"></span>Création d'un StateGraph

<span id="page-249-1"></span>Commencez par créer un StateGraph . Nous allons ajouter un nœud pour représenter l'appel LLM :

#### <span id="page-249-2"></span>*Python*

à partir de la saisie import Annoté, TypedDict

depuis langgraph.graph importer StateGraph, START, EN depuis langgraph.graph.message importer add\_messages

#### état de classe (TypedDict) :

# Les messages sont du type "liste". Les `add\_mes

- # La fonction dans l'annotation définit comment cela
- # être mis à jour (dans ce cas, il ajoute un nouveau moi
- # liste, plutôt que de remplacer les messages précédents : Annoté[liste, add\_messages]

```
builder = StateGraph(State)
```

```
JavaScript
```

```
import {
 StateGraph,
 StateType,
 Annotation,
 messagesStateReducer,
 START, END
} from '@langchain/langgraph'
const State = {
 /**
 * The State defines three things:
 * 1. The structure of the graph's state (which 
 * read/write)
 * 2. The default values for the state's channel
 * 3. The reducers for the state's channels. Red
 * determine how to apply updates to the state. 
 * appended to the messages array.
 */
 messages: Annotation({
 reducer: messagesStateReducer,
 default: () => []
 })
```
# }), } constructeur const = nouveau StateGraph(État)

#### **REMARQUE**

<span id="page-251-1"></span>La première chose que vous faites lorsque vous définissez un graphique est de définir l'état du graphique. L'*état* comprend la forme, ou le schéma, de l'état du graphique, ainsi que des fonctions de réduction qui spécifient comment appliquer les mises à jour à l'état. Dans cet exemple, l'état est un dictionnaire avec une seule clé : messages . La clé des messages est annotée avec la fonction de réduction add\_messages, qui indique à LangGraph d'ajouter de nouveaux messages à la liste existante, plutôt que de l'écraser. Les clés d'état sans annotation seront écrasées à chaque mise à jour, stockant la valeur la plus récente. Vous pouvez écrire vos propres fonctions de réduction, qui sont simplement des fonctions qui reçoivent comme arguments : l'argument 1 est l'état actuel et l'argument 2 est la prochaine valeur écrite dans l'état et doit renvoyer l'état suivant, c'est-à-dire le résultat de la fusion de l'état actuel avec la nouvelle valeur. L'exemple le plus simple est une fonction qui ajoute la valeur suivante à une liste et renvoie cette liste.

Alors maintenant, notre graphique sait deux choses :

- Chaque nœud que nous définissons recevra l'état actuel en entrée et renverra une valeur qui met à jour cet état.
- Les <span id="page-251-0"></span>les messages seront *ajoutés* à la liste actuelle, plutôt que directement écrasés. Ceci est communiqué via la fonction prédéfinie [add\\_messages](https://oreil.ly/sK-Ry) dans la syntaxe annotée du

Exemple Python ou la fonction de réduction pour l'exemple JavaScript.

Ensuite, ajoutez le nœud chatbot. Les nœuds représentent des unités de travail. Ce ne sont généralement que des fonctions :

<span id="page-252-1"></span>*Python*

```
from langchain_openai import ChatOpenAI
model = ChatOpenAI()
def chatbot(state: State):
 answer = model.invoke(state["messages"])
 return {"messages": [answer]}
# The first argument is the unique node name
# The second argument is the function or Runnable
builder.add_node("chatbot", chatbot)
```
<span id="page-252-0"></span>*JavaScript*

```
import {ChatOpenAI} from '@langchain/openai'
import {
 AIMessage,
```

```
 SystemMessage,
 HumanMessage
} from "@langchain/core/messages";
const model = new ChatOpenAI()
async function chatbot(state) {
 const answer = await model.invoke(state.message
 return {"messages": answer}
}
builder = builder.addNode('chatbot', chatbot)
```
Ce nœud reçoit l'état actuel, effectue un appel LLM, puis renvoie une mise à jour de l'état contenant le nouveau message produit par le LLM. Le réducteur add\_messages ajoute ce message aux messages déjà dans l'état.

Et enfin ajoutons les arêtes :

g

<span id="page-253-0"></span>*Python*

```
builder.add_edge(START, 'chatbot')
builder.add_edge('chatbot', END)
```

```
graph = builder.compile()
```
*JavaScript*

```
builder = builder
 .addEdge(START, 'chatbot')
 .addEdge('chatbot', END)
let graph = builder.compile()
```
Cela fait plusieurs choses :

- Il indique au graphique par où commencer son travail à chaque fois que vous l'exécutez.
- Cela indique au graphique où il doit se terminer (ceci est facultatif, car LangGraph arrêtera l'exécution une fois qu'il n'y aura plus de nœuds à exécuter).
- Il compile le graphique en un objet exécutable, avec les méthodes familières d'invocation et de flux.

Nous pouvons également dessiner une représentation visuelle du graphique :

<span id="page-254-1"></span>*Python*

<span id="page-255-1"></span>graph.get\_graph().draw\_mermaid\_png()

*JavaScript*

attendre graph.getGraph().drawMermaidPng()

<span id="page-255-0"></span>Le graphique que nous venons de créer ressemble à la [Figure](#page-255-0) 4-6.

![](_page_255_Figure_4.jpeg)

Figure 4-6. Un simple chatbot

Vous pouvez l'exécuter avec la méthode familière stream() que vous avez vue dans les chapitres précédents :

*Python*

```
input = {"messages": [HumanMessage('hi!)]}
for chunk in graph.stream(input):
 print(chunk)
```
*JavaScript*

```
const input = {messages: [new HumanMessage('hi!)]
for await (const chunk of await graph.stream(inpu
 console.log(chunk)
}
```
*La sortie :*

```
{ "chatbot": { "messages": [AIMessage("How can I
```
Remarquez que l'entrée du graphique avait la même forme que l'objet State que nous avons défini précédemment ; c'est-à-dire que nous avons envoyé une liste de

<span id="page-257-3"></span>messages dans la clé messages d'un dictionnaire. De plus, la fonction stream diffuse la valeur complète de l'état après chaque étape du graphique.

## <span id="page-257-0"></span>Ajout de mémoire à StateGraph

<span id="page-257-4"></span><span id="page-257-2"></span><span id="page-257-1"></span>LangGraph a une persistance intégrée, qui est utilisée de la même manière pour le graphique le plus simple au plus complexe. Voyons à quoi cela ressemble de l'appliquer à cette première architecture. Nous allons recompiler notre graphique, en attachant maintenant un *checkpointer*, qui est un adaptateur de stockage pour LangGraph. LangGraph est livré avec une classe de base que tout utilisateur peut sous-classer pour créer un adaptateur pour sa base de données préférée ; au moment de la rédaction, LangGraph est livré avec plusieurs adaptateurs maintenus par LangChain :

- Un adaptateur en mémoire, que nous utiliserons pour nos exemples ici
- Un adaptateur SQLite, utilisant la base de données en cours populaire, approprié pour les applications et les tests locaux
- Un adaptateur Postgres, optimisé pour la base de données relationnelle populaire et adapté aux applications à grande échelle.

De nombreux développeurs ont écrit des adaptateurs pour d'autres systèmes de bases de données, tels que Redis ou MySQL :

```
from langgraph.checkpoint.memory import MemorySav
graph = builder.compile(checkpointer=MemorySaver(
```
<span id="page-258-0"></span>*JavaScript*

```
import {MemorySaver} from '@langchain/langgraph'
const graph = builder.compile({ checkpointer: new
```
Cela renvoie un objet exécutable avec les mêmes méthodes que celle utilisée dans le bloc de code précédent. Mais maintenant, il stocke l'état à la fin de chaque étape, de sorte que chaque invocation après la première ne part pas d'une page vierge. Chaque fois que le graphique est appelé, il commence par utiliser le point de contrôle pour récupérer l'état enregistré le plus récent, le cas échéant, et combine la nouvelle entrée avec l'état précédent. Et ce n’est qu’alors qu’il exécute les premiers nœuds.

Voyons la différence en action :

#### *Python*

```
thread1 = {"configurable": {"thread_id": "1"}}
result_1 = graph.invoke(
 { "messages": [HumanMessage("hi, my name is J
 thread1
)
// { "chatbot": { "messages": [AIMessage("How can
result_2 = graph.invoke(
 { "messages": [HumanMessage("what is my name?
 thread1
)
// { "chatbot": { "messages": [AIMessage("Your na
```
*JavaScript*

```
const thread1 = {configurable: {thread_id: '1'}}
const result_1 = await graph.invoke(
 { "messages": [new HumanMessage("hi, my name is
 thread1
)
// { "chatbot": { "messages": [AIMessage("How can
```
résultat const 2 = attendre l'invocation du graphique (

```
const result_2 = await graph.invoke(
 { "messages": [new HumanMessage("what is my nam
 thread1
)
// { "chatbot": { "messages": [AIMessage("Your na
```
<span id="page-260-1"></span><span id="page-260-0"></span>Remarquez l'objet thread1 , qui identifie l'interaction actuelle comme appartenant à un historique particulier d'interactions appelées *threads* dans LangGraph. Les fils de discussion sont créés automatiquement lors de la première utilisation. Toute chaîne est un identifiant valide pour un thread (généralement, des identifiants universels uniques [UUID] sont utilisés). L'existence de threads vous aide à franchir une étape importante dans votre candidature LLM ; il peut désormais être utilisé par plusieurs utilisateurs avec des conversations indépendantes et jamais mélangées.
Comme auparavant, le nœud chatbot est d'abord appelé avec un seul message (celui que nous venons de transmettre) et renvoie un autre message, qui sont ensuite tous deux enregistrés dans l'état.

La deuxième fois que nous exécutons le graphique sur le même thread, le nœud chatbot est appelé avec trois messages, les deux enregistrés lors de la première exécution et la question suivante de l'utilisateur. C'est l'essence de la mémoire : l'état précédent est toujours là, ce qui permet, par exemple, de répondre à des questions.

à propos de quelque chose qui a été dit auparavant (et faire bien d'autres choses intéressantes, dont nous verrons plus tard).

Vous pouvez également inspecter et mettre à jour l’état directement ; voyons comment :

<span id="page-261-1"></span>*Python*

<span id="page-261-0"></span>graph.get\_state(thread1)

*JavaScript*

attendre graph.getState (thread1)

Cela renvoie l'état actuel de ce thread.

Et vous pouvez mettre à jour l'état comme ceci :

*Python*

graph.update\_state(thread1, [HumanMessage('J'aime

*JavaScript*

attendre graph.updateState (thread1, [nouveau HumanMessag

<span id="page-262-0"></span>Cela ajouterait un message supplémentaire à la liste des messages dans l'état, à utiliser la prochaine fois que vous appellerez le graphique sur ce fil.

## Modification de l'historique des discussions

<span id="page-262-1"></span>Dans de nombreux cas, les messages de l'historique des discussions ne sont pas dans le meilleur état ou format pour générer une réponse précise de la part du modèle. Pour surmonter ce problème, nous pouvons modifier l'historique des discussions de trois manières principales : couper, filtrer et fusionner les messages.

### **Coupage des messages**

<span id="page-262-3"></span><span id="page-262-2"></span>Les LLM ont des *fenêtres contextuelles* limitées ; en d’autres termes, il existe un nombre maximum de jetons que les LLM peuvent recevoir en guise d’invite. En tant que tel, l'invite finale envoyée au modèle ne doit pas dépasser cette limite (propre à chaque mode), car les modèles refuseront une invite trop longue ou la tronqueront. De plus, des informations excessives peuvent distraire le modèle et conduire à des hallucinations.

Une solution efficace à ce problème consiste à limiter le nombre de messages extraits de l’historique des discussions et ajoutés à l’invite. En pratique, il suffit de charger et de stocker les messages les plus récents. Utilisons un exemple d'historique de discussion avec quelques messages préchargés.

Heureusement, LangChain fournit l'assistant trim\_messages intégré qui intègre diverses stratégies pour répondre à ces exigences. Par exemple, l'assistant trimmer permet de spécifier le nombre de jetons que nous souhaitons conserver ou supprimer de l'historique des discussions.

Voici un exemple qui récupère le dernier max\_tokens dans la liste des messages en définissant un paramètre de stratégie sur "last" :

<span id="page-263-0"></span>*Python*

```
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
trimmer = trim_messages(
 max_tokens=65,
 strategy="last",
 token_counter=ChatOpenAI(model="gpt-4o"),
 include_system=True,
```
![](_page_264_Figure_0.jpeg)

#### <span id="page-264-0"></span>*JavaScript*

importer { AIMessage, HumanMessage,

```
 SystemMessage,
 trimMessages,
} from "@langchain/core/messages";
import { ChatOpenAI } from "@langchain/openai";
const trimmer = trimMessages({
 maxTokens: 65,
 strategy: "last",
 tokenCounter: new ChatOpenAI({ modelName: "gpt-
 includeSystem: true,
 allowPartial: false,
 startOn: "human",
});
const messages = [
 new SystemMessage("you're a good assistant"),
 new HumanMessage("hi! I'm bob"),
 new AIMessage("hi!"),
 new HumanMessage("I like vanilla ice cream"),
 new AIMessage("nice"),
 new HumanMessage("what's 2 + 2"),
 new AIMessage("4"),
 new HumanMessage("thanks"),
 new AIMessage("no problem!"),
 new HumanMessage("having fun?"),
 new AIMessage("yes!"),
```
]

```
const trimmed = await trimmer.invoke(messages);
```
#### *Le résultat :*

```
[SystemMessage(content="you're a good assistant")
 HumanMessage(content='what's 2 + 2'),
 AIMessage(content='4'),
 HumanMessage(content='thanks'),
 AIMessage(content='no problem!'),
 HumanMessage(content='having fun?'),
 AIMessage(content='yes!')]
```
#### Notez les points suivants :

- La stratégie des paramètres contrôle s'il faut commencer par le début ou la fin de la liste. Habituellement, vous souhaiterez donner la priorité aux messages les plus récents et supprimer les messages plus anciens s'ils ne correspondent pas. Autrement dit, commencez par la fin de la liste. Pour ce comportement, choisissez la valeur last . L'autre option disponible est first , qui donnerait la priorité aux messages les plus anciens et supprimerait les messages les plus récents s'ils ne correspondent pas.
- Le token\_counter est un modèle LLM ou chat, qui sera utilisé pour compter les jetons en utilisant le tokenizer approprié à cela

modèle.

- On peut ajouter le paramètre include\_system=True pour s'assurer que le trimmer conserve le message système.
- Le paramètreallow\_partial détermine s'il faut couper le contenu du dernier message pour qu'il rentre dans la limite. Dans notre exemple, nous définissons ceci sur false , ce qui supprime complètement le message qui enverrait le total au-delà de la limite.
- Le paramètre start\_on="human" garantit que nous ne supprimons jamais un AIMessage (c'est-à-dire une réponse du modèle) sans également supprimer un HumanMessage correspondant (la question pour cette réponse).

### <span id="page-267-1"></span>**Filtrage des messages**

<span id="page-267-0"></span>À mesure que la liste des messages de l'historique des discussions s'allonge, une plus grande variété de types, de sous-chaînes et de modèles peuvent être utilisés. L'assistant filter\_messages de LangChain facilite le filtrage des messages de l'historique des discussions par type, identifiant ou nom.

Voici un exemple où nous filtrons les messages humains :

<span id="page-267-2"></span>*Python*

à partir de l'importation langchain\_core.messages ( AIMessage,

```
 HumanMessage,
 SystemMessage,
 filter_messages,
)
messages = [
 SystemMessage("you are a good assistant", id=
 HumanMessage("example input", id="2", name="e
 AIMessage("example output", id="3", name="exa
 HumanMessage("real input", id="4", name="bob"
 AIMessage("real output", id="5", name="alice"
]
filter_messages(messages, include_types="human")
```
g

<span id="page-268-0"></span>*JavaScript*

```
import {
 HumanMessage,
 SystemMessage,
 AIMessage,
 filterMessages,
} from "@langchain/core/messages";
const messages = [
 new SystemMessage({content: "you are a good ass
```

```
 new HumanMessage({content: "example input", id
 new AIMessage({content: "example output", id: "
 new HumanMessage({content: "real input", id: "4
 new AIMessage({content: "real output", id: "5",
];
filterMessages(messages, { includeTypes: ["human"
```
*La sortie :*

```
[HumanMessage(content='example input', name='exam
 HumanMessage(content='real input', name='bob', i
```
Essayons un autre exemple dans lequel nous filtrons pour exclure les utilisateurs et les identifiants et inclure les types de messages :

*Python*

```
filter_messages(messages, exclude_names=["example
"""
[SystemMessage(content='you are a good assistant
HumanMessage(content='real input', name='bob', id
```

```
AIMessage(content='real output', name='alice', id
"""
filter_messages(
 messages,
 include_types=[HumanMessage, AIMessage],
 exclude_ids=["3"]
)
"""
[HumanMessage(content='example input', name='exam
 HumanMessage(content='real input', name='bob', i
 AIMessage(content='real output', name='alice', i
"""
```
*JavaScript*

```
filterMessages(
 messages,
 { excludeNames: ["example_user",
 "example_assistant"] }
);
```
/\*

```
[SystemMessage(content='you are a good assistant
HumanMessage(content='real input', name='bob', id
```

```
AIMessage(content='real output', name='alice', id
*/
filterMessages(messages, { includeTypes: ["human"
/*
[HumanMessage(content='example input', name='exam
 HumanMessage(content='real input', name='bob', i
 AIMessage(content='real output', name='alice', i
*/
```
L'assistant filter\_messages peut également être utilisé de manière impérative ou déclarative, ce qui facilite la composition avec d'autres composants d'une chaîne :

*Python*

```
model = ChatOpenAI()
filter_ = filter_messages(exclude_names=["example
chain = filter_ | model
```
#### *JavaScript*

```
const model = new ChatOpenAI()
const filter = filterMessages({
 excludeNames: ["example_user", "example_assista
})
const chain = filter.pipe(model)
```
### **Fusion de messages consécutifs**

<span id="page-272-0"></span>Certains modèles ne prennent pas en charge les entrées, y compris les messages consécutifs du même type (par exemple, les modèles de chat Anthropic). L'utilitaire merge\_message\_runs de LangChain facilite la fusion de messages consécutifs du même type :

<span id="page-272-1"></span>*Python*

à partir de l'importation langchain\_core.messages ( AIMessage, HumanMessage, SystemMessage, merge\_message\_runs,

```
messages = [
 SystemMessage("you're a good assistant."),
 SystemMessage("you always respond with a joke
 HumanMessage(
 [{"type": "text", "text": "i wonder why i
 ),
 HumanMessage("and who is harrison chasing any
 AIMessage(
 '''Well, I guess they thought "WordRope" 
 didn\'t have the same ring to it!'''
 ),
 AIMessage("""Why, he's probably chasing after
 office!"""),
]
merge_message_runs(messages)
```
<span id="page-273-0"></span>*JavaScript*

)
importer { HumanMessage, SystemMessage, AIMessage, mergeMessageRuns,

} de "@langchain/core/messages" ;

```
const messages = [
 new SystemMessage("you're a good assistant."),
 new SystemMessage("you always respond with a jo
 new HumanMessage({
 content: [{ type: "text", text: "i wonder why
 }),
 new HumanMessage("and who is harrison chasing a
 new AIMessage(
 `Well, I guess they thought "WordRope" and "S
 have the same ring to it!`
 ),
 new AIMessage(
 "Why, he's probably chasing after the last cu
 ),
];
mergeMessageRuns(messages);
```
} o @ a gc a /co e/ messages ;

#### *Le résultat :*

[SystemMessage(content="tu es un bon assistant.\ blague."), HumanMessage(content=[{'type': 'text', 'text': " langchain"}, 'et qui est Harrison à la poursuite d'un AIMessage(content='Eh bien, je suppose qu'ils ont pensé "W

j'ai fait \' h h i i \ h

 Cela ne sonnait tout simplement pas la même chose !\nEh bien, la dernière tasse de café au bureau !')]

Notez que si le contenu de l'un des messages à fusionner est une liste de blocs de contenu, alors le message fusionné aura une liste de blocs de contenu. Et si les deux messages à fusionner ont un contenu de chaîne, alors ceux-ci sont concaténés avec un caractère de nouvelle ligne.

L'assistant merge\_message\_runs peut être utilisé de manière impérative ou déclarative, ce qui facilite la composition avec d'autres composants d'une chaîne :

*Python*

```
model = ChatOpenAI()
merger = merge_message_runs()
chain = merger | model
```
*JavaScript*

```
const model = new ChatOpenAI()
const merger = mergeMessageRuns()
const chain = merger.pipe(model)
```
## Résumé

<span id="page-276-0"></span>Ce chapitre a couvert les principes fondamentaux de la création d'un système de mémoire simple qui permet à votre chatbot IA de se souvenir de ses conversations avec un utilisateur. Nous avons expliqué comment automatiser le stockage et la mise à jour de l'historique des discussions à l'aide de LangGraph pour rendre cela plus facile. Nous avons également discuté de l'importance de modifier l'historique des discussions et exploré diverses stratégies pour découper, filtrer et résumer les messages de discussion.

Dans le [Chapitre](#page-277-0) 5, vous apprendrez comment permettre à votre chatbot IA de faire plus que simplement répondre : par exemple, votre nouveau modèle sera capable de prendre des décisions, de choisir des actions et de réfléchir à ses résultats passés.

# <span id="page-277-0"></span>Chapitre 5. Architectures cognitives avec LangGraph

<span id="page-277-2"></span>Jusqu'à présent, nous avons examiné les fonctionnalités les plus courantes des applications LLM :

- Techniques d'invite dans la [Préface](#page-8-0) et le [Chapitre](#page-44-0) 1
- RAG dans les chapitres [2](#page-93-0) et [3](#page-163-0)
- Mémoire dans [Chapitre](#page-237-0) 4

<span id="page-277-1"></span>La question suivante devrait être : comment assembler ces éléments en une application cohérente qui atteint l'objectif que nous nous sommes fixé ? Pour faire un parallèle avec le monde de la brique et du mortier, une piscine et une maison à un étage sont construites avec les mêmes matériaux, mais répondent évidemment à des objectifs très différents. Ce qui les rend particulièrement adaptés à leurs différents objectifs, c'est la manière dont ces matériaux sont combinés, c'est-à-dire leur architecture. Il en va de même lors de la création d'applications LLM. Les décisions les plus importantes que vous devez prendre sont de savoir comment assembler les différents composants dont vous disposez (tels que RAG, techniques d'invite, mémoire) en quelque chose qui atteint votre objectif.

Avant d'examiner des architectures spécifiques, passons en revue un exemple. Toute application LLM que vous pourriez créer partira d'un objectif : ce pour quoi l'application est conçue. Supposons que vous souhaitiez créer un assistant de messagerie, une application LLM qui lit vos e-mails avant vous et vise à réduire la quantité d'e-mails que vous devez consulter. L'application peut le faire en archivant quelques messages inintéressants, en répondant directement à certains et en marquant d'autres comme méritant votre attention plus tard.

Vous souhaiteriez probablement aussi que l'application soit liée par certaines contraintes dans son action. La liste de ces contraintes est extrêmement utile, car elles contribueront à éclairer la recherche de la bonne architecture. Le [Chapitre](#page-385-0) 8 couvre ces contraintes plus en détail et comment travailler avec elles. Pour cet hypothétique assistant de messagerie, disons que nous aimerions qu'il fasse ce qui suit :

- Minimisez le nombre de fois où il vous interrompt (après tout, le but est de gagner du temps).
- Evitez que vos correspondants email reçoivent une réponse que vous n'auriez jamais envoyée vous-même.
<span id="page-278-2"></span><span id="page-278-1"></span><span id="page-278-0"></span>Cela fait allusion au compromis clé souvent rencontré lors de la création d'applications LLM : le compromis entre *l'agence* (ou la capacité d'agir de manière autonome) et la *fiabilité* (ou le degré auquel vous pouvez faire confiance à ses résultats). Intuitivement, l'assistant de messagerie sera plus

utile s'il entreprend plus d'actions sans votre implication, mais si vous allez trop loin, il enverra inévitablement des e-mails que vous auriez souhaité ne pas avoir.

<span id="page-279-0"></span>Une façon de décrire le degré d'autonomie d'une application LLM consiste à évaluer dans quelle mesure le comportement de l'application est déterminé par un LLM (par rapport au code) :

- Demandez à un LLM de décider du résultat d'une étape (par exemple, rédiger un brouillon de réponse à un e-mail).
- Demandez à un LLM de décider de la prochaine étape à suivre (par exemple, pour un nouvel e-mail, décidez entre les trois actions qu'il peut entreprendre sur un e-mail : archiver, répondre ou marquer pour révision).
- Demandez à un LLM de décider quelles étapes sont disponibles (par exemple, demandez au LLM d'écrire du code qui exécute une action dynamique que vous n'avez pas préprogrammée dans l'application).

<span id="page-279-1"></span>Nous pouvons classer un certain nombre de *recettes* populaires pour créer des applications LLM en fonction de leur situation dans ce spectre d'autonomie, c'est-à-dire lesquelles des trois tâches que nous venons de mentionner sont gérées par un LLM et lesquelles restent entre les mains du développeur ou de l'utilisateur. Ces recettes peuvent être appelées *architectures cognitives*. Dans le domaine de l'intelligence artificielle, le terme *architecture cognitive* est utilisé depuis longtemps pour désigner les modèles de raisonnement humain (et leurs implémentations dans les ordinateurs).

<span id="page-280-1"></span>Une architecture cognitive LLM (le terme a été appliqué pour la première fois aux LLM, à notre connaissance, dans un article) peut être définie comme une recette pour les étapes à suivre par une application LLM (voir [Figure](#page-280-0) 5-1). Une *étape* est, par exemple, la récupération des documents pertinents (RAG) ou l'appel d'un LLM avec une invite de chaîne de pensée. **[1](#page-314-0)**

<span id="page-280-0"></span>![](_page_280_Figure_1.jpeg)

<span id="page-280-2"></span>Figure 5-1. Architectures cognitives pour les applications LLM

Examinons maintenant chacune des principales architectures, ou recettes, que vous pouvez utiliser lors de la création de votre application (comme indiqué dans la [Figure](#page-280-0) 5-1) :

#### *0 : Code*

Il ne s'agit pas d'une architecture cognitive LLM (c'est pourquoi nous l'avons numérotée **0**), car elle n'utilise pas du tout de LLM. Vous pouvez considérer cela comme un logiciel classique que vous avez l'habitude d'écrire. La première architecture intéressante (pour ce livre, en tout cas) est en fait la suivante.

#### *1 : appel LLM*

Il s'agit de la majorité des exemples que nous avons vus dans le livre jusqu'à présent, avec un seul appel LLM. Ceci est surtout utile lorsqu'il fait partie d'une application plus vaste qui utilise un LLM pour accomplir une tâche spécifique, telle que traduire ou résumer un morceau de texte.

#### *2 : Chaîne*

Le niveau supérieur, pour ainsi dire, consiste à utiliser plusieurs appels LLM dans une séquence prédéfinie. Par exemple, une application texte vers SQL (qui reçoit en entrée de l'utilisateur une description en langage naturel d'un calcul à effectuer sur une base de données) pourrait utiliser deux appels LLM en séquence :

Un appel LLM pour générer une requête SQL, à partir de la requête en langage naturel, fournie par l'utilisateur, et d'une description du contenu de la base de données, fournie par le développeur.

Et un autre appel LLM pour écrire une explication de la requête appropriée pour un utilisateur non technique, étant donné le

requête générée lors de l’appel précédent. Celui-ci pourrait alors être utilisé pour permettre à l'utilisateur de vérifier si la requête générée correspond à sa requête.

#### *3 : Routeur*

Cette prochaine étape consiste à utiliser le LLM pour définir la séquence d'étapes à suivre. Autrement dit, alors que l'architecture de chaîne exécute toujours une séquence statique d'étapes (quel que soit leur nombre) déterminées par le développeur, l'architecture de routeur se caractérise par l'utilisation d'un LLM pour choisir entre certaines étapes prédéfinies. Un exemple serait une application RAG avec plusieurs index de documents provenant de différents domaines, avec les étapes suivantes :

- 1. Un appel LLM pour choisir lequel des index disponibles utiliser, en fonction de la requête fournie par l'utilisateur et de la description des index fournie par le développeur.
- 2. Une étape de récupération qui interroge l'index choisi pour les documents les plus pertinents pour la requête de l'utilisateur.
- 3. Un autre appel LLM pour générer une réponse, compte tenu de la requête fournie par l'utilisateur et de la liste des documents pertinents extraits de l'index.
C'est tout ce que nous irons dans ce chapitre. Nous parlerons tour à tour de chacune de ces architectures. Les chapitres suivants abordent les architectures agentiques, qui font encore plus appel aux LLM. Mais parlons d’abord de meilleurs outils pour nous aider dans ce voyage.

## <span id="page-283-1"></span>Architecture n°1 : appel LLM

<span id="page-283-0"></span>À titre d'exemple d'architecture d'appel LLM, nous reviendrons au chatbot que nous avons créé dans le [Chapitre](#page-237-0) 4. Ce chatbot répondra directement aux messages des utilisateurs.

Commencez par créer un StateGraph , auquel nous ajouterons un nœud pour représenter l'appel LLM :

<span id="page-283-2"></span>*Python*

```
from typing import Annotated, TypedDict
```
depuis langgraph.graph importer StateGraph, START, EN depuis langgraph.graph.message importer add\_messages depuis langchain\_openai importer ChatOpenAI

```
model = ChatOpenAI()
```

```
class State(TypedDict):
 # Messages have the type "list". The `add_mes
 # function in the annotation defines how this
 # be updated (in this case, it appends new me
 # list, rather than replacing the previous me
 messages: Annotated[list, add_messages]
def chatbot(state: State):
 answer = model.invoke(state["messages"])
 return {"messages": [answer]}
builder = StateGraph(State)
builder.add_node("chatbot", chatbot)
builder.add_edge(START, 'chatbot')
builder.add_edge('chatbot', END)
```

```
graph = builder.compile()
```
<span id="page-284-0"></span>*JavaScript*

importer { StateGraph, Annotation, messagesStateReducer, DÉBUT, FIN

```
} from '@langchain/langgraph'
import {ChatOpenAI} from '@langchain/openai'
const model = new ChatOpenAI()
const State = {
 /**
 * The State defines three things:
 * 1. The structure of the graph's state (which 
 * read/write)
 * 2. The default values for the state's channel
 * 3. The reducers for the state's channels. Red
 * determine how to apply updates to the state. 
 * appended to the messages array.
 */
 messages: Annotation({
 reducer: messagesStateReducer,
 default: () => []
 }),
}
async function chatbot(state) {
 const answer = await model.invoke(state.message
 return {"messages": answer}
}
const builder = new StateGraph(State)
 .addNode('chatbot', chatbot)
 .addEdge(START, 'chatbot')
```

```
 .addEdge(START, chatbot )
 .addEdge('chatbot', END)
```

```
const graph = builder.compile()
```
Nous pouvons également dessiner une représentation visuelle du graphique :

*Python*

graph.get\_graph().draw\_mermaid\_png()

*JavaScript*

attendre graph.getGraph().drawMermaidPng()

Le graphique que nous venons de réaliser ressemble à la [Figure](#page-287-0) 5-2.

<span id="page-287-0"></span>![](_page_287_Figure_0.jpeg)

Figure 5-2. L’architecture des appels LLM

Vous pouvez l'exécuter avec la méthode familière stream() que vous avez vue dans les chapitres précédents :

#### *Python*

```
input = {"messages": [HumanMessage('hi!)]}
for chunk in graph.stream(input):
 print(chunk)
```
#### *JavaScript*

```
const input = {messages: [new HumanMessage('hi!)]
for await (const chunk of await graph.stream(inpu
 console.log(chunk)
}
```
*La sortie :*

```
{ "chatbot": { "messages": [AIMessage("How can I
```
Remarquez que l'entrée du graphique avait la même forme que l'objet State que nous avons défini précédemment ; c'est-à-dire que nous avons envoyé une liste de messages dans la clé de messages d'un dictionnaire.

Il s’agit de l’architecture la plus simple possible pour utiliser un LLM, ce qui ne veut pas dire qu’il ne faut jamais l’utiliser. Voici quelques exemples d’endroits où vous pourriez le voir en action dans des produits populaires, entre autres :

Les fonctionnalités basées sur l'IA telles que la synthèse et la traduction (telles que celles que vous pouvez trouver dans Notion, un logiciel d'écriture populaire) peuvent être alimentées par un seul appel LLM.

<span id="page-289-2"></span>La génération de requêtes SQL simples peut être alimentée par un seul appel LLM, en fonction de l'UX et de l'utilisateur cible que le développeur a en tête.

### Architecture #2 : Chaîne

<span id="page-289-1"></span>Cette architecture suivante étend tout cela en utilisant plusieurs appels LLM, dans une séquence prédéfinie (c'est-à-dire que différentes invocations de l'application effectuent la même séquence d'appels LLM, bien qu'avec des entrées et des résultats différents).

Prenons comme exemple une application text-to-SQL, qui reçoit en entrée de l'utilisateur une description en langage naturel d'un calcul à effectuer sur une base de données. Nous avons mentionné précédemment que cela pouvait être réalisé avec un seul appel LLM, pour générer une requête SQL, mais nous pouvons créer une application plus sophistiquée en utilisant plusieurs appels LLM en séquence. Certains auteurs appellent cette architecture *ingénierie des flux*. **[2](#page-314-1)**
<span id="page-289-3"></span><span id="page-289-0"></span>Décrivons d'abord le flux avec des mots :

1. Un appel LLM pour générer une requête SQL à partir de la requête en langage naturel, fournie par l'utilisateur, et d'une description du contenu de la base de données, fournie par le développeur.

2. Un autre appel LLM pour écrire une explication de la requête appropriée pour un utilisateur non technique, compte tenu de la requête générée lors de l'appel précédent. Celui-ci pourrait alors être utilisé pour permettre à l'utilisateur de vérifier si la requête générée correspond à sa requête.

Vous pouvez également étendre cela encore plus loin (mais nous ne le ferons pas ici) en prenant des mesures supplémentaires après les deux précédentes :

- 3. Exécute la requête sur la base de données, qui renvoie une table bidimensionnelle.
- 4. Utilise un troisième appel LLM pour résumer les résultats de la requête dans une réponse textuelle à la question originale de l'utilisateur.

Et maintenant implémentons cela avec LangGraph :

<span id="page-290-0"></span>*Python*

```
from typing import Annotated, TypedDict
from langchain_core.messages import HumanMessage,
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGrap
from langgraph.graph.message import add_messages
```

```
# useful to generate SQL query
model_low_temp = ChatOpenAI(temperature=0.1)
# useful to generate natural language outputs
model_high_temp = ChatOpenAI(temperature=0.7)
class State(TypedDict):
 # to track conversation history
 messages: Annotated[list, add_messages]
 # input
 user_query: str
 # output
 sql_query: str
 sql_explanation: str
class Input(TypedDict):
 user_query: str
class Output(TypedDict):
 sql_query: str
 sql_explanation: str
generate_prompt = SystemMessage(
```

```
 """You are a helpful data analyst who generat
 on their questions."""
```
)

```
def generate_sql(state: State) -> State:
 user_message = HumanMessage(state["user_query
   messages = [generate prompt *state["messages
```

```
 messages = [generate_prompt, state[ messages
 res = model_low_temp.invoke(messages)
 return {
 "sql_query": res.content,
 # update conversation history
 "messages": [user_message, res],
 }
explain_prompt = SystemMessage(
 "You are a helpful data analyst who explains 
)
def explain_sql(state: State) -> State:
 messages = [
 explain_prompt,
 # contains user's query and SQL query fro
 *state["messages"],
 ]
 res = model_high_temp.invoke(messages)
 return {
 "sql_explanation": res.content,
 # update conversation history
 "messages": res,
 }
builder = StateGraph(State, input=Input, output=O
builder.add_node("generate_sql", generate_sql)
builder.add_node("explain_sql", explain_sql)
```
constructeur ajouter un bord (START "générer sql")

```
builder.add_edge(START, generate_sql )
builder.add_edge("generate_sql", "explain_sql")
builder.add_edge("explain_sql", END)
```

```
graph = builder.compile()
```

```
JavaScript
```

```
import {
 HumanMessage,
 SystemMessage
} from "@langchain/core/messages";
import { ChatOpenAI } from "@langchain/openai";
import {
 StateGraph,
 Annotation,
 messagesStateReducer,
 START,
 END,
} from "@langchain/langgraph";
// useful to generate SQL query
const modelLowTemp = new ChatOpenAI({ temperature
// useful to generate natural language outputs
const modelHighTemp = new ChatOpenAI({ temperatur
const annotation = Annotation.Root({
```

```
const annotation Annotation.Root({
 messages: Annotation({ reducer: messagesStateRe
 user_query: Annotation(),
 sql_query: Annotation(),
 sql_explanation: Annotation(),
});
const generatePrompt = new SystemMessage(
 `You are a helpful data analyst who generates S
 their questions.`
);
async function generateSql(state) {
 const userMessage = new HumanMessage(state.user
 const messages = [generatePrompt, ...state.mess
 const res = await modelLowTemp.invoke(messages)
 return {
 sql_query: res.content as string,
 // update conversation history
 messages: [userMessage, res],
 };
}
const explainPrompt = new SystemMessage(
 "You are a helpful data analyst who explains SQ
);
async function explainSql(state) {
 const messages = [explainPrompt, ...state.messa
```

```
 const messages [explainPrompt, ...state.messa
 const res = await modelHighTemp.invoke(messages
 return {
 sql_explanation: res.content as string,
 // update conversation history
 messages: res,
 };
}
const builder = new StateGraph(annotation)
 .addNode("generate_sql", generateSql)
 .addNode("explain_sql", explainSql)
 .addEdge(START, "generate_sql")
 .addEdge("generate_sql", "explain_sql")
 .addEdge("explain_sql", END);
const graph = builder.compile();
```
La représentation visuelle du graphique est présentée dans la [Figure](#page-296-0) 5-3.

<span id="page-296-0"></span>![](_page_296_Figure_0.jpeg)

![](_page_296_Figure_1.jpeg)

Voici un exemple d'entrées et de sorties :

*Python*

graph.invoke({

```
 "user_query": "What is the total sales for each
})
```
*JavaScript*

```
await graph.invoke({
 user_query: "What is the total sales for each p
})
```
*La sortie :*

```
{
 "sql_query": "SELECT product_name, SUM(sales_am
 sales\nGROUP BY product_name;",
 "sql_explanation": "This query will retrieve th
 by summing up the sales_amount column for e
 results by product_name.",
}
```
Tout d'abord, le nœud generate\_sql est exécuté, qui remplit la clé sql\_query dans l'état (qui fera partie de la sortie finale) et met à jour la clé messages avec les nouveaux messages.

Ensuite, le nœud expliquer\_sql s'exécute, prenant la requête SQL générée à l'étape précédente et remplissant la clé sql\_explanation dans l'état. À ce stade, l’exécution du graphique se termine et la sortie est renvoyée à l’appelant.

Notez également l'utilisation de schémas d'entrée et de sortie séparés lors de la création du StateGraph . Cela vous permet de personnaliser les parties de l'état qui sont acceptées comme entrées par l'utilisateur et celles qui sont renvoyées comme sortie finale. Les clés d'état restantes sont utilisées en interne par les nœuds du graphique pour conserver l'état intermédiaire et sont mises à la disposition de l'utilisateur dans le cadre de la sortie de streaming produite par stream() .

### <span id="page-298-1"></span>Architecture n°3 : Routeur

<span id="page-298-0"></span>Cette prochaine architecture fait progresser l'échelle d'autonomie en attribuant aux LLM la prochaine des responsabilités que nous avons décrites précédemment : décider de la prochaine étape à franchir. Autrement dit, alors que l'architecture en chaîne exécute toujours une séquence statique d'étapes (quel que soit leur nombre), l'architecture de routeur se caractérise par l'utilisation d'un LLM pour choisir entre certaines étapes prédéfinies.

Prenons l'exemple d'une application RAG avec accès à plusieurs index de documents de différents domaines (reportez-vous au [Chapitre](#page-93-0) 2 pour en savoir plus sur l'indexation). Habituellement, vous pouvez extraire de meilleures performances des LLM en évitant l'inclusion d'informations non pertinentes dans l'invite. Par conséquent, lors de la création de cette application, nous devons essayer de choisir le bon index à utiliser pour chaque requête et de n’utiliser que celui-là. Le développement clé de cette architecture consiste à utiliser un LLM pour prendre cette décision, en utilisant efficacement un LLM pour évaluer chaque requête entrante et décider quel index elle doit utiliser pour cette requête *particulière*.

#### **REMARQUE**

Avant l'avènement des LLM, la manière habituelle de résoudre ce problème serait de créer un modèle de classificateur à l'aide de techniques de ML et d'un ensemble de données mappant des exemples de requêtes utilisateur vers le bon index. Cela pourrait s’avérer assez difficile, car cela nécessite les éléments suivants :

- Assembler cet ensemble de données à la main
- Générer suffisamment de *caractéristiques* (attributs quantitatifs) à partir de chaque requête utilisateur pour permettre la formation d'un classificateur pour la tâche

Les LLM, étant donné leur codage du langage humain, peuvent efficacement servir de classificateur avec zéro, ou très peu d’exemples ou de formation supplémentaire.

Tout d’abord, décrivons le flux avec des mots :

1. Un appel LLM pour choisir lequel des index disponibles utiliser, en fonction de la requête fournie par l'utilisateur et de la description des index fournie par le développeur.

- 2. Une étape de récupération qui interroge l'index choisi pour les documents les plus pertinents pour la requête utilisateur
- 3. Un autre appel LLM pour générer une réponse, compte tenu de la requête fournie par l'utilisateur et de la liste des documents pertinents extraits de l'index

Et maintenant implémentons-le avec LangGraph :

#### <span id="page-300-0"></span>*Python*

```
from typing import Annotated, Literal, TypedDict
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage,
from langchain_core.vectorstores.in_memory import
from langchain_openai import ChatOpenAI, OpenAIEm
from langgraph.graph import END, START, StateGrap
from langgraph.graph.message import add_messages
embeddings = OpenAIEmbeddings()
# useful to generate SQL query
model_low_temp = ChatOpenAI(temperature=0.1)
# useful to generate natural language outputs
model_high_temp = ChatOpenAI(temperature=0.7)
class State(TypedDict):
```

```
 # to track conversation history
 messages: Annotated[list, add_messages]
 # input
```
(ouais)

```
 user_query: str
 # output
 domain: Literal["records", "insurance"]
 documents: list[Document]
 answer: str
```

```
class Input(TypedDict):
 user_query: str
```

```
class Output(TypedDict):
 documents: list[Document]
 answer: str
```
# reportez-vous au chapitre 2 pour savoir comment remplir un stockage vectoriel.

```
insurance_faqs_store = InMemoryVectorStore.from_d
insurance_faqs_retriever = insurance_faqs_store.a
```

```
router_prompt = SystemMessage(
 """You need to decide which domain to route t
 domains to choose from:
 - records: contains medical records of 
         diagnosis, treatment, and prescriptions
```

```
 d ag os s, t eat e t, a d p esc pt o s
 - insurance: contains frequently asked 
 policies, claims, and coverage.
Output only the domain name."""
)
def router_node(state: State) -> State:
 user_message = HumanMessage(state["user_query
 messages = [router_prompt,
                           *state["messages"]
 res = model_low_temp.invoke(messages)
 return {
 "domain": res.content,
 # update conversation history
 "messages": [user_message, res],
 }
def pick_retriever(
 state: State,
) -> Literal["retrieve_medical_records", "retriev
 if state["domain"] == "records":
 return "retrieve_medical_records"
 else:
 return "retrieve_insurance_faqs"
def retrieve_medical_records(state: State) -> Sta
 documents = medical_records_retriever.invoke(
 return {
 "documents": documents,
```

```
 }
def retrieve_insurance_faqs(state: State) -> Stat
 documents = insurance_faqs_retriever.invoke(s
 return {
 "documents": documents,
 }
medical_records_prompt = SystemMessage(
 """You are a helpful medical chatbot who answ
 patient's medical records, such as diagno
 prescriptions."""
)
insurance_faqs_prompt = SystemMessage(
 """You are a helpful medical insurance chatbo
 questions about insurance policies, claim
)
def generate_answer(state: State) -> State:
 if state["domain"] == "records":
 prompt = medical_records_prompt
 else:
 prompt = insurance_faqs_prompt
 messages = [
 prompt,
 *state["messages"],
 HumanMessage(f"Documents: {state["documen
```
docu e ts docu e ts,

```
 ]
 res = model_high_temp.invoke(messages)
 return {
 "answer": res.content,
 # update conversation history
 "messages": res,
 }
```
u un message( ocu e ts {state[ docu e

```
builder = StateGraph(State, input=Input, output=O
builder.add_node("router", router_node)
builder.add_node("retrieve_medical_records", retr
builder.add_node("retrieve_insurance_faqs", retri
builder.add_node("generate_answer", generate_answ
builder.add_edge(START, "router")
builder.add_conditional_edges("router", pick_retr
builder.add_edge("retrieve_medical_records", "gen
builder.add_edge("retrieve_insurance_faqs", "gene
builder.add_edge("generate_answer", END)
```

```
graph = builder.compile()
```
<span id="page-304-0"></span>*JavaScript*

```
import {
 HumanMessage,
  SystemMessage
```

```
 SystemMessage
} from "@langchain/core/messages";
import {
 ChatOpenAI,
 OpenAIEmbeddings
} from "@langchain/openai";
import {
 MemoryVectorStore
} from "langchain/vectorstores/memory";
import {
 DocumentInterface
} from "@langchain/core/documents";
import {
 StateGraph,
 Annotation,
 messagesStateReducer,
 START,
 END,
} from "@langchain/langgraph";
const embeddings = new OpenAIEmbeddings();
// useful to generate SQL query
const modelLowTemp = new ChatOpenAI({ temperature
// useful to generate natural language outputs
const modelHighTemp = new ChatOpenAI({ temperatur
const annotation = Annotation.Root({
 messages: Annotation({ reducer: messagesStateRe
 user_query: Annotation(),
```
d je je ()

```
 domain: Annotation(),
 documents: Annotation(),
 answer: Annotation(),
});
// refer to Chapter 2 on how to fill a vector sto
const medicalRecordsStore = await MemoryVectorSto
 [],
 embeddings
);
const medicalRecordsRetriever = medicalRecordsSto
const insuranceFaqsStore = await MemoryVectorStor
 [],
 embeddings
);
const insuranceFaqsRetriever = insuranceFaqsStore
const routerPrompt = new SystemMessage(
 `You need to decide which domain to route the u
 domains to choose from:
 - records: contains medical records of th
 treatment, and prescriptions.
 - insurance: contains frequently asked qu
 policies, claims, and coverage.
Output only the domain name.`
);
```

```
fonction asynchrone routerNode(state) {
 const userMessage = nouveau HumanMessage (état.utilisateur
 const messages = [routerPrompt, ...state.messag
 const res = attendre modelLowTemp.invoke (messages)
 retourner {
 domaine : res.content comme "enregistrements" | "assurance
 // met à jour l'historique des conversations
 messages : [userMessage, res],
 } ;
}
fonction pickRetriever (état) {
 if (state.domain === "enregistrements") {
renvoyer "retrieve_medical_records" ;
 } autre {
 renvoyer "retrieve_insurance_faqs" ;
 }
}
fonction asynchrone retrieveMedicalRecords(state) {
 const documents = attendre médicalRecordsRetriever
 retourner {
 documents,
 } ;
}
fonction asynchrone retrieveInsuranceFaqs (état) {
```
d i i i

```
 const documents = attendre l'assuranceFaqsRetriever
 retourner {
 documents,
 } ;
}
const medicalRecordsPrompt = nouveau SystemMessage (
 `You are a helpful medical chatbot who answers 
 patient's medical records, such as diagnosis,
 prescriptions.`
);
const assuranceFaqsPrompt = nouveau SystemMessage (
 `You are a helpful medical insurance chatbot wh
 questions about insurance policies, claims, a
);
async function generateAnswer(state) {
 const prompt =
 state.domain === "records" ? medicalRecordsPr
 const messages = [
 prompt,
 ...state.messages,
 new HumanMessage(`Documents : ${state.document
 ];
 const res = attendre modelHighTemp.invoke (messages
 retourner {
 réponse : res.content sous forme de chaîne,
```
// d i hi

```
 // met à jour l'historique des conversations
 messages : rés,
 } ;
}
const builder = nouveau StateGraph (annotation)
 .addNode("routeur", noeud de routeur)
 .addNode("retrieve_medical_records", récupérerMe
 .addNode("retrieve_insurance_faqs", retrieveIns
 .addNode("generate_answer", generateAnswer)
 .addEdge(START, "routeur")
 .addConditionalEdges("routeur", pickRetriever)
 .addEdge("retrieve_medical_records", "generate_
 .addEdge("retrieve_insurance_faqs", "generate_a
 .addEdge("generate_answer", FIN);
const graph = builder.compile();
```
The visual representation is shown in [Figure](#page-310-0) 5-4.

<span id="page-310-0"></span>![](_page_310_Figure_0.jpeg)

Figure 5-4. The router architecture

Notice how this is now starting to become more useful, as it shows the two possible paths through the graph, through retrieve\_medical\_records or through retrieve\_insurance\_faqs , and that for both of those, we first visit the router node and finish by visiting the generate\_answer node. These two possible paths were implemented through the use of a conditional edge, implemented in the function pick\_retriever , which maps the domain picked by the LLM to one of the two nodes mentioned earlier. The conditional edge is shown in [Figure](#page-310-0) 5-4 as dotted lines from the source node to the destination nodes.

And now for example inputs and outputs, this time with streaming output:

*Python*

```
entrée = {
 "user_query": "Suis-je couvert pour le traitement COVID-19
}
pour c dans graph.stream (entrée):
 imprimer(c)
```
*JavaScript*

```
entrée const = {
 user_query : "Suis-je couvert pour les traitements contre le COVID-19
}
pour wait (morceau const de wait graph.stream (inpu
console.log(morceau)
}
```
*The output* (the actual answer is not shown, since it would depend on your documents):

```
{
 "routeur": {
 "messages": [
 HumanMessage(content="Suis-je couvert pour
 AIMessage(content="assurance"),
 ],
 "domain": "assurance",
 }
}
{
 "retrieve_insurance_faqs": {
 "documents" : [...]
 }
}
{
 "generate_answer": {
 "messages": AIMessage(
 contenu="...",
 ),
 "réponse": "...",
 }
}
```
Ce flux de sortie contient les valeurs renvoyées par chaque nœud exécuté lors de cette exécution du graphique. Prenons-le un à la fois. La clé de niveau supérieur dans chaque dictionnaire est le nom du nœud, et la valeur de cette clé est ce que ce nœud a renvoyé :

- 1. Le nœud du routeur a renvoyé une mise à jour des messages (cela nous permettrait de poursuivre facilement cette conversation en utilisant la technique de mémoire décrite précédemment), et le domaine choisi par le LLM pour la requête de cet utilisateur, dans ce cas l'assurance.
- 2. Ensuite, la fonction pick\_retriever s'est exécutée et a renvoyé le nom du prochain nœud à exécuter, en fonction du domaine identifié par l'appel LLM à l'étape précédente.
- 3. Ensuite, le nœud retrieve\_insurance\_faqs s'est exécuté, renvoyant un ensemble de documents pertinents à partir de cet index. Cela signifie que sur le dessin du graphique vu plus tôt, nous avons pris le chemin de gauche, comme décidé par le LLM.
- 4. Enfin, le nœud generate\_answer s'est exécuté, qui a pris ces documents et la requête originale de l'utilisateur et a produit une réponse à la question, qui a été écrite dans l'état (avec une mise à jour finale de la clé des messages).

### <span id="page-313-0"></span>Résumé

Ce chapitre a parlé du compromis clé lors de la création d'applications LLM : agence contre surveillance. Plus une application LLM est autonome, plus elle peut faire grand-chose, mais cela augmente le

besoin de davantage de mécanismes de contrôle sur ses actions. Nous sommes passés à différentes architectures cognitives qui établissent différents équilibres entre agence et surveillance.
Le [Chapitre](#page-315-0) 6 parle de la plus puissante des architectures cognitives que nous ayons vues jusqu'à présent : l'architecture des agents.

<span id="page-314-0"></span>Theodore R. Sumers et al., "Cognitive [Architectures](https://oreil.ly/cuQnT) for Language Agents", arXiv, 5 septembre 2023, mis à jour le 15 mars 2024. **[1](#page-280-1)**

<span id="page-314-1"></span>Tal Ridnik et al., "Génération de code avec [AlphaCodium :](https://oreil.ly/0wHX4) De l'ingénierie d'invite à l'ingénierie de flux", arXiv, 16 janvier 2024. **[2](#page-289-0)**

## <span id="page-315-0"></span>Chapitre 6. Architecture des agents

S'appuyant sur les architectures décrites dans le [Chapitre](#page-277-0) 5, ce chapitre couvrira ce qui est peut-être la plus importante de toutes les architectures LLM actuelles, l'architecture des agents. Tout d’abord, nous présentons ce qui rend les agents LLM uniques, puis nous montrons comment les créer et comment les étendre pour des cas d’utilisation courants.

<span id="page-315-3"></span><span id="page-315-1"></span>Dans le domaine de l'intelligence artificielle, il existe une longue histoire de création d'agents (intelligents), qui peuvent être plus simplement définis comme « quelque chose qui agit », selon les mots de Stuart Russell et Peter Norvig dans leur manuel *Artificial Intelligence* (Pearson, 2020). Le mot *actes* a en fait un peu plus de sens qu'il n'y paraît :

- Agir nécessite une certaine capacité à décider quoi faire.
- Décider quoi faire implique d'avoir accès à plus d'une ligne d'action possible. Après tout, une décision sans options n’est pas du tout une décision.
- Pour décider, l'agent a également besoin d'accéder à des informations sur l'environnement externe (tout ce qui est extérieur à l'agent lui-même).

<span id="page-315-2"></span>Ainsi, une application LLM *agentic* doit être une application qui utilise un LLM pour choisir parmi un ou plusieurs plans d'action possibles, compte tenu de certains

contexte sur l’état actuel du monde ou sur un prochain état souhaité. Ces attributs sont généralement implémentés en mélangeant deux techniques d'invite que nous avons rencontrées pour la première fois dans la [Préface :](#page-8-0)

#### *Appel de l'outil*

<span id="page-316-1"></span>Incluez une liste de fonctions externes que le LLM peut utiliser dans votre invite (c'est-à-dire les actions qu'il peut décider d'entreprendre) et fournissez des instructions sur la façon de formater son choix dans la sortie qu'il génère. Vous verrez dans un instant à quoi cela ressemble dans l'invite.

#### *Chaîne de pensée*

<span id="page-316-0"></span>Les chercheurs ont découvert que les LLM « prennent de meilleures décisions » lorsqu'on leur donne des instructions pour raisonner sur des problèmes complexes en les décomposant en étapes granulaires à suivre dans l'ordre. Cela se fait généralement soit en ajoutant des instructions du type « penser étape par étape », soit en incluant des exemples de questions et leur décomposition en plusieurs étapes/actions.

Voici un exemple d'invite utilisant à la fois l'appel d'outil et la chaîne de pensée :

h thi t l t b h d

Outils :

recherche : cet outil accepte une requête de recherche sur le Web et une calculatrice : cet outil accepte les expressions mathématiques et

Si vous souhaitez utiliser des outils pour arriver à la réponse, saisissez au format CSV, avec la ligne d'en-tête : outil,i

Pensez étape par étape ; si vous devez donner plusieurs réponses, renvoyez uniquement la première.

Quel âge avait le 30ème président des États-Unis

outil,entrée

Et la sortie, lorsqu'elle est exécutée sur gpt-3.5-turbo à une température de 0 (pour garantir que le LLM suit le format de sortie souhaité, CSV) et une nouvelle ligne comme séquence d'arrêt (qui demande au LLM d'arrêter de produire une sortie lorsqu'il atteint ce caractère). Cela fait que le LLM produit une seule action (comme prévu, étant donné l'invite demandée) :

recherche,30ème président des États-Unis

Les LLM et les modèles de discussion les plus récents ont été affinés pour améliorer leurs performances pour les applications d'appel d'outils et de chaîne de pensée, éliminant ainsi le besoin d'ajouter des instructions spécifiques à l'invite :

ajouter un exemple d'invite et de sortie pour le mo d'appel d'outil

## La boucle Planifier-Faire

<span id="page-318-0"></span>Ce qui différencie l'architecture de l'agent des architectures abordées dans le [Chapitre](#page-277-0) 5 est un concept que nous n'avons pas encore abordé : la boucle pilotée par LLM.

<span id="page-318-2"></span><span id="page-318-1"></span>Tous les programmeurs ont déjà rencontré des boucles dans leur code. Par *boucle*, nous entendons exécuter le même code plusieurs fois jusqu'à ce qu'une condition d'arrêt soit remplie. La clé de l'architecture de l'agent est qu'un LLM contrôle la condition d'arrêt, c'est-à-dire décide quand arrêter la boucle.

Ce que nous exécuterons dans cette boucle sera une variante de ce qui suit :

- Planifier une ou plusieurs actions
- Exécuter lesdites actions
En reprenant l'exemple de la section précédente, nous allons ensuite exécuter l'outil de recherche avec l'entrée 30e président des États-Unis , qui produit ce résultat :

Calvin Coolidge (né John Calvin Coolidge Jr. ; / 5, 1933) était un avocat et homme politique américain des États-Unis de 1923 à 1929. John Calv

Et puis nous réexécuterons l'invite, avec un petit ajout :

Outils : recherche : cet outil accepte une requête de recherche sur le Web et calculatrice : cet outil accepte les expressions mathématiques une sortie : cet outil met fin à l'interaction. Utilisez-le wh Si vous souhaitez utiliser des outils pour arriver à la réponse, saisissez au format CSV, avec cette ligne d'en-tête : outil, Réfléchissez étape par étape ; si vous devez donner plusieurs réponses, renvoyez uniquement la première. Quel âge avait le 30e président des États-Unis, outil d'entrée

recherche,30ème président des États-Unis

recherche : Calvin Coolidge (né John Calvin Coolidg le 5 janvier 1933) était un avocat américain et président politique des États-Unis de 1923 à 1929.

outil,entrée

Et le résultat :

calculatrice,1933 - 1872

Notez que nous avons ajouté deux choses :

- Un outil de « sortie » — que le LLM devrait utiliser lorsqu'il a trouvé la réponse finale, et que nous utiliserions comme signal pour arrêter la boucle.
- Le résultat de l'appel de l'outil de l'itération précédente, avec simplement le nom de l'outil et sa sortie (texte). Ceci est inclus afin de permettre au LLM de passer à l'étape suivante de l'interaction. En d’autres termes, nous disons au LLM : « Hé, nous avons obtenu les résultats que vous avez demandés, que voulez-vous faire ensuite ? »

Continuons avec une troisième itération :

Outils : recherche : cet outil accepte une requête de recherche sur le Web et calculatrice : cet outil accepte les expressions mathématiques et

Si vous souhaitez utiliser des outils pour arriver à la réponse, saisissez au format CSV, avec cette ligne d'en-tête : outil, sortie : cet outil termine l'interaction. Utilisez-le quand

Pensez étape par étape ; si vous devez donner plusieurs réponses, renvoyez uniquement la première.

Quel âge avait le 30ème président des États-Unis

outil,entrée

recherche,30ème président des États-Unis

recherche : Calvin Coolidge (né John Calvin Coolidg le 5 janvier 1933) était un avocat américain et président politique des États-Unis de 1923 à 1929.

calculatrice,1933-1872

calculatrice : 61

outil, saisie

Et le résultat :

sortie, 61

Avec le résultat de l'outil de calcul, le LLM dispose désormais de suffisamment d'informations pour fournir la réponse finale, il a donc choisi l'outil de sortie et a choisi « 61 » comme réponse finale.

<span id="page-322-0"></span>C'est ce qui rend l'architecture d'agent si utile : le LLM est laissé à l'agence pour décider. L’étape suivante consiste à parvenir à une réponse et à décider combien de mesures prendre, c’est-à-dire quand s’arrêter.

<span id="page-322-3"></span><span id="page-322-2"></span>Cette architecture, appelée [ReAct,](https://oreil.ly/M7hF-) a été proposée pour la première fois par Shunyu Yao et al. Le reste de ce chapitre explore comment améliorer les performances de l'architecture de l'agent, motivé par l'exemple de l'assistant de messagerie du [Chapitre](#page-277-0) 5.

<span id="page-322-1"></span>Mais d'abord, voyons à quoi ressemble l'implémentation de l'architecture d'agent de base à l'aide d'un modèle de chat et de LangGraph.

## Construire un agent LangGraph

<span id="page-323-1"></span><span id="page-323-0"></span>Pour cet exemple, nous devons installer des dépendances supplémentaires pour l'outil de recherche que nous avons choisi d'utiliser, DuckDuckGo. Pour l'installer pour Python :

*Python*

pip installer duckduckgo-search

Et pour JS, nous devons également installer une dépendance pour l'outil de calcul :

*JavaScript*

npm je canard-canard-gratte expr-eval

Cela fait, passons au code proprement dit pour implémenter l'architecture de l'agent :

<span id="page-323-2"></span>*Python*

```
import ast
from typing import Annotated, TypedDict
```

```
from langchain_community.tools import DuckDuckGoS
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
```
à partir de langgraph.graph importer START, StateGraph à partir de langgraph.graph.message importer add\_messages à partir de langgraph.prebuilt importer ToolNode, tools\_co

```
@tool
```

```
def calculator(query: str) -> str:
 """A simple calculator tool. Input should be 
 return ast.literal_eval(query)
```

```
search = DuckDuckGoSearchRun()
tools = [search, calculator]
model = ChatOpenAI(temperature=0.1).bind_tools(to
```

```
class State(TypedDict):
 messages: Annotated[list, add_messages]
```

```
def model_node(state: State) -> State:
 res = model.invoke(state["messages"])
 return {"messages": res}
```

```
constructeur = StateGraph (État)
builder.add_node("modèle", model_node)
builder.add_node("outils", ToolNode(outils))
builder.add_edge(START, "modèle")
builder.add_conditional_edges("modèle", tools_cond
builder.add_edge("outils", "modèle")
graphique = builder.compile()
```
#### <span id="page-325-0"></span>*JavaScript*

```
importer {
 DuckDuckGoRecherche
} de "@langchain/community/tools/duckduckgo_sea
importer {
 Calculatrice
} depuis "@langchain/community/tools/calculator" ;
importer {
 Graphique d'état,
 Annotations,
 messagesStateRéducteur,
 COMMENCER,
} de "@langchain/langgraph" ;
importer {
 Noeud Outil,
 outilsCondition
```
} from "@langchain/langgraph/prebuilt";

```
const recherche = new DuckDuckGoSearch();
const calculatrice = nouvelle calculatrice ();
const tools = [recherche, calculatrice] ;
modèle const = nouveau ChatOpenAI ({
 température : 0,1
}).bindTools(outils);
const annotation = Annotation.Root({
 messages : Annotation({
 réducteur : messagesStateReducer,
 par défaut : () => []
 }),
});
fonction asynchrone modelNode(state) {
 const res = wait model.invoke(state.messages);
 renvoyer {messages : res} ;
}
const builder = nouveau StateGraph (annotation)
 .addNode("modèle", modèleNode)
 .addNode("outils", nouveau ToolNode(outils))
 .addEdge(START, "modèle")
 .addConditionalEdges("modèle", outilsCondition)
 .addEdge("outils", "modèle");
```

```
const graph = builder.compile();
```
The visual representation is shown in [Figure](#page-327-0) 6-1.

<span id="page-327-0"></span>![](_page_327_Figure_2.jpeg)

Figure 6-1. The agent architecture

A few things to notice here:

We're using two tools in this example: a search tool and a calculator tool, but you could easily add more or replace the ones we used. In the Python example, you also see an example of creating a custom tool.

- We've used two convenience functions that ship with LangGraph. ToolNode serves as a node in our graph; it executes the tool calls requested in the latest AI message found in the state and returns a ToolMessage with the results of each. ToolNode also handles exceptions raised by tools—using the error message to build a ToolMessage that is then passed to the LLM—which may decide what to do with the error.
- tools\_condition serves as a conditional edge function that looks at the latest AI message in the state and routes to the tools node if there are any tools to execute. Otherwise, it ends the graph.
- Finally, notice that this graph loops between the model and tools nodes. That is, the model itself is in charge of deciding when to end the computation, which is a key attribute of the agent architecture. Whenever we code a loop in LangGraph, we'll likely want to use a conditional edge, as that allows you to define the *stop condition* when the graph should exit the loop and stop executing.

Now let's see how it does in the previous example:

*Python*

```
entrée = {
 "messages": [
 HumanMessage("""Quel âge avait le 30ème prés
 quand il est mort?""")
 ]
}
pour c dans graph.stream (entrée):
 imprimer(c)
```
*JavaScript*

```
entrée const = {
 messages : [
 Message humain (`How old was the 30th president 
 died?`)
 ]
}
pour wait (const c de wait graph.stream(input))
 console.log(c)
}
```
*The output:*

{

```
 "modèle": {
 "messages": AIMessage(
 contenu="",
 outil_calls=[
 {
 "name": "duckduckgo_search",
 "arguments": {
 "query": "30ème président 
 la mort"
 },
 "id": "call_ZWRbPmjvo0fYkwyo4
 "type": "appel_outil",
 }
 ],
 )
 }
}
{
 "outils": {
 "messages": [
 Message d'outil (
 content="Calvin Coolidge (né Ju
 États-Unis — décédé le 5 janvier 1933, non
 le 30ème président de l'Université
 a accédé à la présidence après
 Warren G. Harding, tout comme le
```

```
 à la lumière....",
 nom="duckduckgo_search",
 tool_call_id="call_ZWRbPmjvo0fYkw
 )
 ]
 }
}
{
 "modèle": {
 "messages": AIMessage(
 content="Calvin Coolidge, le 30e pr
 décédé le 5 janvier 1933 à l'âge de
 )
 }
}
```
En parcourant cette sortie :

- 1. D'abord, le nœud modèle s'est exécuté et a décidé d'appeler l'outil duckduckgo\_search, ce qui a conduit le bord conditionnel à nous acheminer vers le nœud outils après.
- 2. Le ToolNode a exécuté l'outil de recherche et a obtenu les résultats de recherche imprimés ci-dessus, qui contiennent en fait la réponse "Âge et année du décès. 5 janvier 1933 (60 ans)".
- 3. L'outil modèle a été appelé à nouveau, cette fois avec les résultats de la recherche comme dernier message, et a produit la réponse finale

<span id="page-332-1"></span>(sans plus d'appels d'outils) ; par conséquent, l’arête conditionnelle termine le graphique.

Examinons ensuite quelques extensions utiles de cette architecture d'agent de base, en personnalisant à la fois la planification et l'appel d'outils.

## Toujours appeler un outil en premier
<span id="page-332-0"></span>Dans l'architecture d'agent standard, le LLM est toujours appelé à décider quel outil appeler ensuite. Cette disposition présente un avantage évident : elle donne au LLM une flexibilité ultime pour adapter le comportement de l'application à chaque requête utilisateur entrante. Mais cette flexibilité a un prix : l'imprévisibilité. Si, par exemple, vous, développeur de l’application, savez que l’outil de recherche doit toujours être appelé en premier, cela peut en réalité être bénéfique pour votre application :

- 1. Cela réduira la latence globale, car cela ignorera le premier appel LLM qui générerait cette demande d'appel à l'outil de recherche.
- 2. Cela empêchera le LLM de décider par erreur qu'il n'a pas besoin d'appeler l'outil de recherche pour certaines requêtes des utilisateurs.

D'un autre côté, si votre application n'a pas de règle claire du type « vous devez toujours appeler cet outil en premier », l'introduction d'une telle contrainte aggraverait en réalité votre application.

Voyons à quoi cela ressemble de faire ceci :

#### <span id="page-333-0"></span>*Python*

```
import ast
from typing import Annotated, TypedDict
from uuid import uuid4
from langchain_community.tools import DuckDuckGoS
from langchain_core.messages import AIMessage, Hu
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_co
@tool
def calculator(query: str) -> str:
 """A simple calculator tool. Input should be 
 return ast.literal_eval(query)
search = DuckDuckGoSearchRun()
tools = [search, calculator]
model = ChatOpenAI(temperature=0.1).bind_tools(to
class State(TypedDict):
    messages: Annotated[list add messages]
```

```
def model_node(state: State) -> State:
 res = model.invoke(state["messages"])
 return {"messages": res}
```

```
def first_model(state: State) -> State:
 query = state["messages"][-1].content
 search_tool_call = ToolCall(
 name="duckduckgo_search", args={"query":
 )
 return {"messages": AIMessage(content=""
                                         , too
```

```
builder = StateGraph(State)
builder.add_node("first_model", first_model)
builder.add_node("model", model_node)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "first_model")
builder.add_edge("first_model", "tools")
builder.add_conditional_edges("model", tools_cond
builder.add_edge("tools", "model")
```

```
graph = builder.compile()
```
<span id="page-334-0"></span>*JavaScript*

```
import {
 DuckDuckGoSearch
} from "@langchain/community/tools/duckduckgo_sea
import {
 Calculator
} from "@langchain/community/tools/calculator";
import {
 AIMessage,
} from "@langchain/core/messages";
import {
 StateGraph,
 Annotation,
 messagesStateReducer,
 START,
} from "@langchain/langgraph";
import {
 ToolNode,
 toolsCondition
} from "@langchain/langgraph/prebuilt";
const search = new DuckDuckGoSearch();
const calculator = new Calculator();
const tools = [search, calculator];
const model = new ChatOpenAI({ temperature: 0.1 }
const annotation = Annotation.Root({
 messages: Annotation({ reducer: messagesStateRe
});
```

```
async function firstModelNode(state) {
 const query = state.messages[state.messages.len
 const searchToolCall = {
 name: "duckduckgo_search",
 args: { query },
 id: Math.random().toString(),
 };
 return {
 messages: [new AIMessage({ content: ""
                                         , tool_
 };
}
async function modelNode(state) {
 const res = await model.invoke(state.messages);
 return { messages: res };
}
const builder = new StateGraph(annotation)
 .addNode("first_model", firstModelNode)
 .addNode("model", modelNode)
 .addNode("tools", new ToolNode(tools))
 .addEdge(START, "first_model")
 .addEdge("first_model", "tools")
 .addEdge("tools", "model")
 .addConditionalEdges("model", toolsCondition);
```

```
const graph = builder.compile();
```
La représentation visuelle est présentée dans la [Figure](#page-338-0) 6-2.

<span id="page-338-0"></span>![](_page_338_Figure_0.jpeg)

Figure 6-2. Modifier l'architecture de l'agent pour toujours appeler en premier un outil spécifique

Notez les différences par rapport à la section précédente :

- Maintenant, nous commençons toutes les invocations en appelant first\_model , ce qui n'appelle pas du tout de LLM. Il crée simplement un appel d'outil pour l'outil de recherche, en utilisant le message de l'utilisateur textuellement comme requête de recherche. L'architecture précédente demandait au LLM de générer cet appel d'outil (ou une autre réponse qu'il jugeait meilleure).
- Après cela, nous passons à tools , qui est identique à l'exemple précédent, et de là nous passons au nœud agent comme auparavant.

Voyons maintenant un exemple de résultat, pour la même requête que précédemment :

*Python*

```
input = {
 "messages": [
 HumanMessage("""How old was the 30th pres
 when he died?""")
 ]
}
for c in graph.stream(input):
print(c)
```
#### *JavaScript*

```
const input = {
 messages: [
 HumanMessage(`How old was the 30th president 
 died?`)
 ]
}
for await (const c of await graph.stream(input))
 console.log(c)
}
```
*La sortie :*

```
{
 "first_model": {
 "messages": AIMessage(
 content="",
 tool_calls=[
 {
 "name": "duckduckgo_search",
 "args": {
 "query": "How old was the
                 States when he died?"
```

```
 States when he died?"
 },
 "id": "9ed4328dcdea4904b1b544
 "type": "tool_call",
 }
 ],
 )
 }
}
{
 "tools": {
 "messages": [
 ToolMessage(
 content="Calvin Coolidge (born Ju
 U.S.—died January 5, 1933, No
 the 30th president of the Uni
 acceded to the presidency aft
 Warren G. Harding, just as th
 to light....",
 name="duckduckgo_search",
 tool_call_id="9ed4328dcdea4904b1b
 )
 ]
 }
}
{
 "model": {
 "messages": AIMessage(
       content="Calvin Coolidge the 30th pr
```

```
 content= Calvin Coolidge, the 30th pr
 was born on July 4, 1872, and die
 calculate his age at the time of 
 birth year from his death year. \
 Birth year\nAge at death = 1933 -
 years\n\nCalvin Coolidge was 61 y
 )
 }
}
```
Cette fois, nous avons sauté l’appel LLM initial. Nous sommes d'abord allés au nœud first\_model, qui a directement renvoyé un appel d'outil pour l'outil de recherche. De là, nous sommes passés au flux précédent, c'est-à-dire que nous avons exécuté l'outil de recherche et sommes finalement revenus au nœud de modèle pour générer la réponse finale.

<span id="page-342-1"></span>Voyons ensuite ce que vous pouvez faire lorsque vous disposez de nombreux outils que vous souhaitez mettre à la disposition du LLM.

## <span id="page-342-0"></span>Gérer de nombreux outils

<span id="page-342-2"></span>Les LLM sont loin d'être parfaits, et ils ont actuellement plus de difficultés lorsqu'on leur propose des choix multiples ou des informations excessives dans une invite. Ces limites s’étendent également à la planification des prochaines actions à entreprendre. Lorsqu'on leur donne de nombreux outils (disons plus de 10), les performances de planification (c'est-à-dire la capacité du LLM à choisir le bon outil) commencent à en souffrir. La solution à ce problème consiste à réduire le nombre d’outils parmi lesquels le LLM peut choisir. Mais que se passe-t-il si vous disposez de nombreux outils que vous souhaitez voir utilisés pour différentes requêtes d'utilisateurs ?

Une solution élégante consiste à utiliser une étape RAG pour présélectionner les outils les plus pertinents pour la requête actuelle, puis à alimenter le LLM uniquement avec ce sous-ensemble d'outils au lieu de l'ensemble de l'arsenal. Cela peut également contribuer à réduire le coût d'appel du LLM (les LLM commerciaux facturent généralement en fonction de la longueur de l'invite et des résultats). D'un autre côté, cette étape RAG introduit une latence supplémentaire à votre application et ne doit donc être effectuée que lorsque vous constatez une diminution des performances après l'ajout d'outils supplémentaires.

Voyons comment procéder :

#### <span id="page-343-0"></span>*Python*

```
import ast
from typing import Annotated, TypedDict
from langchain_community.tools import DuckDuckGoS
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
```
f l h i t l i t t l

```
from langchain_core.tools import tool
from langchain_core.vectorstores.in_memory import
from langchain_openai import ChatOpenAI, OpenAIEm
```
à partir de langgraph.graph importer START, StateGraph à partir de langgraph.graph.message importer add\_messages à partir de langgraph.prebuilt importer ToolNode, tools\_co

```
@tool
```

```
def calculator(query: str) -> str:
 """A simple calculator tool. Input should be 
 return ast.literal_eval(query)
```

```
search = DuckDuckGoSearchRun()
tools = [search, calculator]
```

```
embeddings = OpenAIEmbeddings()
model = ChatOpenAI(temperature=0.1)
```

```
tools_retriever = InMemoryVectorStore.from_docume
 [Document(tool.description, metadata={"name"
 embeddings,
```

```
).as_retriever()
```

```
class State(TypedDict):
 messages: Annotated[list, add_messages]
 selected_tools: list[str]
```
d f d l d ( t t St t ) > St t

```
def model_node(état : État) -> État :
 outils_sélectionnés = [
 outil pour outil dans outils si outil.nom dans st
 ]
 res = model.bind_tools(selected_tools).invoke
 return {"messages": res}
def select_tools(état : État) -> État :
 requête = état["messages"][-1].content
 tool_docs = tools_retriever.invoke(requête)
 return {"selected_tools": [doc.metadata["nom
constructeur = StateGraph (État)
builder.add_node("select_tools", select_tools)
builder.add_node("modèle", model_node)
builder.add_node("outils", ToolNode(outils))
builder.add_edge(START, "select_tools")
builder.add_edge("select_tools", "modèle")
builder.add_conditional_edges("modèle", tools_cond
builder.add_edge("outils", "modèle")
graphique = builder.compile()
```
<span id="page-345-0"></span>*JavaScript*

import { DuckDuckGoSearch } from "@langchain/comm import { Calculator } from "@langchain/community/

```
importer { ChatOpenAI } depuis "@langchain/openai" ;
importer { OpenAIEmbeddings } depuis "@langchain/open
importer { Document } depuis "@langchain/core/documen
importer { MemoryVectorStore } depuis "langchain/vect
importer {
 Graphique d'état,
 Annotations,
 messagesStateRéducteur,
 COMMENCER,
} de "@langchain/langgraph" ;
importer { ToolNode, toolsCondition } depuis "@langch
importer { HumanMessage } depuis "@langchain/core/mes

const recherche = new DuckDuckGoSearch();
const calculatrice = nouvelle calculatrice ();
const tools = [recherche, calculatrice] ;
const embeddings = new OpenAIEmbeddings();
modèle const = nouveau ChatOpenAI ({ température : 0,1 }
const toolsStore = attendre MemoryVectorStore.fromDo
 outils.map(
 (outil) =>
 nouveau document({
 contenu de la page : outil.description,
 métadonnées : { nom : outil.constructeur.nom }
 })
 ),
```
embeddings

```
);
const toolsRetriever = toolsStore.asRetriever();
const annotation = Annotation.Root({
 messages : Annotation ({ réducteur : messagesStateRe
 selected_tools : Annotation(),
});
fonction asynchrone modelNode(state) {
 const selectedTools = tools.filter((outil) =>
 state.selected_tools.includes(tool.constructo
 );
 const res = attendre model.bindTools (selectedTools
 renvoyer {messages : res} ;
}
fonction asynchrone selectTools(state) {
 const requête = state.messages[state.messages.len
 const toolDocs = wait toolsRetriever.invoke(qu
 retourner {
 selected_tools : toolDocs.map((doc) => doc.met
 } ;
}
const builder = nouveau StateGraph (annotation)
 .addNode("select_tools", selectTools)
 .addNode("modèle", modèleNode)
```
![](_page_348_Figure_0.jpeg)

You can see the visual representation in [Figure](#page-348-0) 6-3.

<span id="page-348-0"></span>![](_page_348_Figure_2.jpeg)

Figure 6-3. Modifying the agent architecture to deal with many tools

#### **NOTE**

This is very similar to the regular agent architecture. The only difference is that we stop by the select\_tools node before entering the actual agent loop. After that, it works just as the regular agent architecture we've seen before.

Now let's see some example output for the same query as before:

*Python*

```
entrée = {
 "messages": [
 HumanMessage("""Quel âge avait le 30ème président
 il est mort?""")
 ]
}
pour c dans graph.stream (entrée):
imprimer(c)
```
*JavaScript*

```
entrée const = {
 messages : [
```

```
 Message humain (`How old was the 30th president 
 died?`)
 ]
}
pour wait (const c de wait graph.stream(input))
 console.log(c)
}
```
#### *The output:*

```
{
 "select_tools": {
 "selected_tools' : ['duckduckgo_search', 
 }
}
{
 "modèle": {
 "messages": AIMessage(
 contenu="",
 outil_calls=[
 {
 "name": "duckduckgo_search",
 "arguments": {
 "query": "30ème président 
 },
 "identifiant": "9ed4328dcdea4904b1b544
            "type": "appel d'outil"
```

```
 tapez : appel_outil,
 }
 ],
 )
 }
}
{
 "outils": {
 "messages": [
 Message d'outil (
 content="Calvin Coolidge (né Ju
 États-Unis — décédé le 5 janvier 1933, non
 le 30ème président de l'Université
 a accédé à la présidence après
 Warren G. Harding, tout comme le
 à la lumière....",
 nom="duckduckgo_search",
 tool_call_id="9ed4328dcdea4904b1b
 )
 ]
 }
}
{
 "modèle": {
 "messages": AIMessage(
 content="Calvin Coolidge, le 30e pr
 est né le 4 juillet 1872 et est décédé
 calculer son âge au moment de 
 année de naissance à partir de son année de décès. \
```
![](_page_352_Figure_0.jpeg)

<span id="page-352-0"></span>Remarquez que la première chose que nous avons faite a été d'interroger le récupérateur pour obtenir les outils les plus pertinents pour la requête actuelle de l'utilisateur. Ensuite, nous sommes passés à l’architecture d’agent standard.

## Résumé

Ce chapitre a présenté le concept d'*agence* et a expliqué ce qu'il faut pour rendre une application LLM *agentique* : donner au LLM la possibilité de décider entre plusieurs options en utilisant des informations externes.

Nous avons parcouru l'architecture d'agent standard construite avec LangGraph et examiné deux extensions utiles : comment toujours appeler un outil spécifique en premier et comment gérer de nombreux outils.

Le [Chapitre](#page-353-0) 7 examine les extensions supplémentaires de l'architecture de l'agent.

## <span id="page-353-0"></span>Chapitre 7. Agents II
[Chapitre](#page-315-0) 6 a introduit l'architecture *agent*, la plus puissante des architectures LLM que nous ayons vues jusqu'à présent. Il est difficile d’exagérer le potentiel de cette combinaison d’incitations en chaîne de pensée, d’utilisation d’outils et de boucles.

Ce chapitre traite de deux extensions de l'architecture de l'agent qui améliorent les performances dans certains cas d'utilisation :

#### *Réflexion*

En sortant une autre page du répertoire des schémas de pensée humains, il s'agit de donner à votre application LLM la possibilité d'analyser ses résultats et ses choix passés, ainsi que la capacité de se souvenir des réflexions des itérations passées.

#### *Multi-agents*

De la même manière qu'une équipe peut accomplir plus qu'une seule personne, il existe des problèmes qui peuvent être mieux résolus par des équipes d'agents LLM.

Commençons par la réflexion.

## Réflexion

<span id="page-354-2"></span><span id="page-354-0"></span>Une technique d'incitation que nous n'avons pas encore abordée est la *réflexion* (également connue sous le nom d'*autocritique*). *La réflexion* est la création d'une boucle entre une invite de créateur et une invite de réviseur. Cela reflète le processus de création de nombreux artefacts créés par l'homme, comme ce chapitre que vous lisez actuellement, qui est le résultat d'un va-et-vient entre les auteurs, les réviseurs et l'éditeur jusqu'à ce que tous soient satisfaits du produit final.

Comme pour la plupart des techniques d'incitation que nous avons vues jusqu'à présent, la réflexion peut être combinée avec d'autres techniques, telles que la chaîne de pensée et l'appel d'outils. Dans cette section, nous examinerons la réflexion de manière isolée.

<span id="page-354-1"></span>Un parallèle peut être établi avec les modes de pensée humaine connus sous le nom de *Système 1* (réactif ou instinctif) et *Système 2* (méthodique et réflexif), introduits pour la première fois par Daniel Kahneman dans le livre *Thinking, Fast and Slow* (Farrar, Straus et Giroux, 2011). Lorsqu'elle est appliquée correctement, l'autocritique peut aider les applications LLM à se rapprocher de quelque chose qui ressemble au comportement du Système 2 [\(Figure](#page-355-0) 7-1).

<span id="page-355-0"></span>![](_page_355_Figure_0.jpeg)

Figure 7-1. Pensée Système 1 et Système 2

Nous allons implémenter la réflexion sous forme de graphe à deux nœuds : générer et refléter . Ce graphique sera chargé de rédiger des essais de trois paragraphes, avec le nœud de génération rédigeant ou révisant les ébauches de l'essai, et réfléchira à la rédaction d'une critique pour éclairer la prochaine révision. Nous exécuterons la boucle un nombre fixe de fois, mais une variante de cette technique consisterait à laisser le nœud de réflexion décider quand terminer. Voyons à quoi cela ressemble :

<span id="page-356-0"></span>*Python*

```
from typing import Annotated, TypedDict
from langchain_core.messages import (
 AIMessage,
 BaseMessage,
 HumanMessage,
 SystemMessage,
)
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGrap
from langgraph.graph.message import add_messages
model = ChatOpenAI()
class State(TypedDict):
 messages: Annotated[list[BaseMessage], add_me
generate_prompt = SystemMessage(
 """You are an essay assistant tasked with wri
 essays."""
 "Generate the best essay possible for the use
```

```
 """If the user provides critique, respond wit
 previous attempts."""
)
def generate(state: State) -> State:
 answer = model.invoke([generate_prompt] + sta
 return {"messages": [answer]}
reflection_prompt = SystemMessage(
 """You are a teacher grading an essay submiss
 recommendations for the user's submission
 """Provide detailed recommendations, includin
 style, etc."""
)
def reflect(state: State) -> State:
 # Invert the messages to get the LLM to refle
 cls_map = {AIMessage: HumanMessage, HumanMess
 # First message is the original user request
 # We hold it the same for all nodes
 translated = [reflection_prompt, state["messa
 cls_map[msg.__class__](content=msg.conten
 for msg in state["messages"][1:]
 ]
 answer = model.invoke(translated)
 # We treat the output of this as human feedba
 return {"messages": [HumanMessage(content=ans
```

```
def should_continue(state: State):
 if len(state["messages"]) > 6:
 # End after 3 iterations, each with 2 mes
 return END
 else:
 return "reflect"
builder = StateGraph(State)
builder.add_node("generate", generate)
builder.add_node("reflect", reflect)
builder.add_edge(START, "generate")
builder.add_conditional_edges("generate", should_
builder.add_edge("reflect", "generate")
```

```
graph = builder.compile()
```
<span id="page-358-0"></span>*JavaScript*

```
importer {
 Message AIM,
 Message de base,
 Message système,
 Message humain,
} de "@langchain/core/messages" ;
importer { ChatOpenAI } depuis "@langchain/openai" ;
importer {
```

```
 Graphique d'état,
 Annotations,
 messagesStateRéducteur,
 COMMENCER,
 FIN,
} de "@langchain/langgraph" ;
modèle const = new ChatOpenAI();
const annotation = Annotation.Root({
 messages : Annotation ({ réducteur : messagesStateRe
});
// corrige la chaîne multiligne
const generatePrompt = nouveau SystemMessage (
 `You are an essay assistant tasked with writing
 Generate the best essay possible for the user's
 If the user provides critique, respond with a r
 previous attempts.`
);
fonction asynchrone générer (état) {
 const réponse = wait model.invoke([generateProm
 renvoyer { messages : [réponse] } ;
}
const réflexionPrompt = nouveau message système (
 `You are a teacher grading an essay submission
__PROTECTED_CODE_1__
 recommendations for the user's submission.
 Provide detailed recommendations, including req
 style, etc.`
);
fonction asynchrone réfléchir (état) {
 // Inversez les messages pour que le LLM reflète
 const clsMap : { [clé : chaîne] : nouveau (contenu : st
 ai : Message humain,
 humain : AIMessage,
 } ;
 // Le premier message est la demande originale de l'utilisateur. 
 // Nous le gardons de la même manière pour tous les nœuds
 const traduit = [
 invite de réflexion,
 état.messages[0],
 ...état.messages
 .tranche(1)
 .map((msg) => nouveau clsMap[msg._getType()](ms
 ];
 const réponse = wait model.invoke(traduit);
 // Nous traitons le résultat de ceci comme un feedback humain
 renvoyer { messages : [nouveau HumanMessage ({ contenu
}
la fonction devraitContinuer(état) {
 si (état.messages.longueur > 6) {
 // Fin après 3 itérations, chacune avec 2 messages
```

```
 retourner FIN ;
 } autre {
 renvoyer "réfléchir" ;
 }
}
const builder = nouveau StateGraph (annotation)
 .addNode("générer", générer)
 .addNode("réfléchir", réfléchir)
 .addEdge(START, "générer")
 .addConditionalEdges("générer", devraitContinuer
 .addEdge("réfléchir", "générer");
const graph = builder.compile();
```
The visual representation of the graph is shown in [Figure](#page-362-0) 7-2.

<span id="page-362-0"></span>![](_page_362_Figure_0.jpeg)

Figure 7-2. The reflection architecture

Notice how the reflect node tricks the LLM into thinking it is critiquing essays written by the user. And in tandem, the generate node is made to think that the critique comes from the user. This subterfuge is required because dialogue-tuned LLMs are trained on pairs of human-AI messages, so a sequence of many messages from the same participant would result in poor performance.

One more thing to note: you might, at first glance, expect the end to come after a revise step, but in this architecture we have <span id="page-363-0"></span>a fixed number of iterations of the generate-reflect loop; therefore we terminate after generate (so that the last set of revisions requested are dealt with). A variation on this architecture would instead have the reflect step make the decision to end the process (once it had no more comments).

Let's see what one of the critiques looks like:

```
 'messages' : [
```
{

 HumanMessage(content='Your essay on the t and its message in modern life is wel have effectively highlighted the endu themes and its importance in today\'s few areas where you could enhance you While you touch upon the themes of ch nurturing connections, and understand consider delving deeper into each of examples from the book to support you themes manifest in contemporary life analyzing how the book\'s messages ca societal issues or personal experienc discuss how the Little Prince\'s pers to consumer culture or explore how hi can inform interpersonal dynamics in \*\*Length\*\*: Expand on your ideas by a

```
 discuter des contre-arguments, ou explo
 "Le Petit Prince" en différentes parties
 enrichissez la profondeur de votre analyse et
 compréhension de la pertinence du livre
 est clair et bien structuré. Pour améliorer
 lecteurs, pensez à inclure une citation
 points clés ou incluant des anecdotes à 
 \n\n5. **Conclusion** : Concluez votre 
 signification durable de « Le Petit 
 peut inspirer un changement positif dans le monde moderne
 implications plus larges du livre
 avec une impression durable.\n\nPar expa
 incorporant plus d'exemples et approfondi
 les messages du livre, vous pouvez créer un mo
 essai convaincant sur l'actualité de
 la vie. Bravo pour votre réflexion et
 ça marche !', id='70c22b1d-ec96-4dc3-9fd0-d
```
#### And the final output:

],

}

```
{
 'messages' : [
 AIMessage(content=""Le Petit Prince" par
 se présente comme un chef-d'œuvre intemporel qui
```

```
 un aperçu des relations humaines et
 lecteurs à travers les générations. Le récit
 voyages et rencontres avec une myriade 
 tapisserie de représentation allégorique
 {'token_usage' : {'completion_tokens'
'total_tokens' : 2921}, 'model_name' : 
 'system_fingerprint' : aucun, 'finish_r
 Aucun}, id='run-2e8f9f13-f625-4820-9c8
 utilisation_metadata={'input_tokens' : 2501,
 'total_tokens' : 2921}),
 ],
}
```
This simple type of reflection can sometimes improve performance by giving the LLM multiple attempts at refining its output and by letting the reflection node adopt a different persona while critiquing the output.

There are several possible variations of this architecture. For one, we could combine the reflection step with the agent architecture of [Chapter](#page-315-0) 6, adding it as the last node right before sending output to the user. This would make the critique appear to come from the user, and give the application a chance to improve its final output without direct user intervention. Obviously this approach would come at the expense of higher latency.

In certain use cases, it could be helpful to ground the critique with external information. For instance, if you were writing a code-generation agent, you could have a step before reflect that would run the code through a linter or compiler and report any errors as input to reflect .

#### **TIP**

<span id="page-366-0"></span>Whenever this approach is possible, we strongly recommend giving it a try, as it's likely to increase the quality of the final output.

## Subgraphs in LangGraph

<span id="page-366-1"></span>Before we dive into multi-agent architectures, let's look at an important technical concept in LangGraph that enables it. *Subgraphs* are graphs that are used as part of another graph. Here are some use cases for subgraphs:

- Building multi-agent systems (discussed in the next section).
- When you want to reuse a set of nodes in multiple graphs, you can define them once in a subgraph and then use them in multiple parent graphs.
- When you want different teams to work on different parts of the graph independently, you can define each part as a

subgraph, and as long as the subgraph interface (the input and output schemas) is respected, the parent graph can be built without knowing any details of the subgraph.

<span id="page-367-0"></span>There are two ways to add subgraph nodes to a parent graph:

*Add a node that calls the subgraph directly*

This is useful when the parent graph and the subgraph share state keys, and you don't need to transform state on the way in or out.

*Add a node with a function that invokes the subgraph*

This is useful when the parent graph and the subgraph have different state schemas, and you need to transform state before or after calling the subgraph.

Let's look at each in turn.

### **Calling a Subgraph Directly**

<span id="page-367-1"></span>The simplest way to create subgraph nodes is to attach a subgraph directly as a node. When doing so, it is important that the parent graph and the subgraph share state keys, because those shared keys will be used to communicate. (If your graph and subgraph do not share any keys, see the next section.)

#### **NOTE**

If you pass extra keys to the subgraph node (that is, in addition to the shared keys), they will be ignored by the subgraph node. Similarly, if you return extra keys from the subgraph, they will be ignored by the parent graph.

Let's see what it looks like in action:

#### <span id="page-368-0"></span>*Python*

```
à partir de langgraph.graph importer START, StateGraph
en tapant import TypedDict
État de classe (TypedDict) :
 foo: str # cette clé est partagée avec le subgra
classe SubgraphState (TypedDict) :
 foo : str # cette clé est partagée avec le parent
 barre : str
# Définir le sous-graphe
def subgraph_node (état : SubgraphState) :
 # notez que ce nœud de sous-graphe peut communiquer
 # via la clé partagée "foo"
 return {"foo": state["foo"] + "bar"}
subgraph_builder = StateGraph (SubgraphState)
générateur de sous-graphe ajouter un nœud (nœud de sous-graphe)
```

```
subgraph_builder.add_node(subgraph_node)
...
sous-graphe = subgraph_builder.compile()
# Définir le graphe parent
constructeur = StateGraph (État)
builder.add_node("sous-graphe", sous-graphe)
...
graphique = builder.compile()
```
<span id="page-369-0"></span>*JavaScript*

```
importer { StateGraph, Annotation, START } depuis "@l
const StateAnnotation = Annotation.Root({
 foo : Annotation(),
});
const SubgraphStateAnnotation = Annotation.Root({
 // notez que cette clé est partagée avec le parent
 foo : Annotation(),
 barre : Annotation(),
});
// Définir le sous-graphe
const subgraphNode = async (état) => {
 // notez que ce nœud de sous-graphe peut communiquer
```

```
 // le graphe parent via la clé partagée "foo"
return { foo : state.foo + "bar" } ;
} ;
const subgraph = nouveau StateGraph (SubgraphStateAnno
 .addNode("sous-graphe", subgraphNode);
 ...
 .compile();
// Définir le graphe parent
const parentGraph = nouveau StateGraph (StateAnnotatio
 .addNode("sous-graphe", sous-graphe)
 .addEdge(START, "sous-graphe")
 // Une configuration supplémentaire du graphique parent irait ici
 .compile();
```
### **Calling a Subgraph with a Function**

<span id="page-370-0"></span>You might want to define a subgraph with a completely different schema. In that case, you can create a node with a function that invokes the subgraph. This function will need to transform the input (parent) state to the subgraph state before invoking the subgraph and transform the results back to the parent state before returning the state update from the node.

Let's see what it looks like:

#### <span id="page-371-0"></span>*Python*

```
État de classe (TypedDict) :
 foo : str
classe SubgraphState (TypedDict) :
 # aucune de ces clés n'est partagée avec le pare
 barre : str
 baz : str
# Définir le sous-graphe
def subgraph_node (état : SubgraphState) :
 return {"bar": state["bar"] + "baz"}
subgraph_builder = StateGraph (SubgraphState)
subgraph_builder.add_node(subgraph_node)
...
sous-graphe = subgraph_builder.compile()
# Définir le graphe parent
nœud def (état : état) :
 # transformer l'état en état de sous-graphe
 réponse = subgraph.invoke({"bar": state["foo
 # transformer la réponse vers l'état parent
 return {"foo": réponse["bar"]}
constructeur = StateGraph (État)
```
# t th t i ` d ` f ti i t d

```
# notez que nous utilisons la fonction `node` à la place 
builder.add_node(nœud)
...
graphique = builder.compile()
```
#### <span id="page-372-0"></span>*JavaScript*

```
importer { StateGraph, START, Annotation } depuis "@l
const StateAnnotation = Annotation.Root({
 foo : Annotation(),
});
const SubgraphStateAnnotation = Annotation.Root({
 // notez qu'aucune de ces clés n'est partagée avec
 barre : Annotation(),
 baz : Annotation(),
});
// Définir le sous-graphe
const subgraphNode = async (état) => {
 return {bar : state.bar + "baz" } ;
} ;
```

```
const subgraph = nouveau StateGraph (SubgraphStateAnno
 .addNode("sous-graphe", subgraphNode);
 ...
 .compile();
// Définir le graphe parent
const subgraphWrapperNode = async (état) => {
 // transforme l'état en état de sous-graphe
 réponse const = attendre subgraph.invoke({
 barre : state.foo,
 });
 // transforme la réponse en l'état parent
 retourner {
 foo : réponse.bar,
 } ;
}
const parentGraph = nouveau StateGraph (StateAnnotatio
 .addNode("sous-graphe", subgraphWrapperNode)
 .addEdge(START, "sous-graphe")
 // Une configuration supplémentaire du graphique parent irait ici
 .compile();
```
<span id="page-373-0"></span>Maintenant que nous savons comment utiliser les sous-graphes, examinons l'un de leurs principaux cas d'utilisation : les architectures multi-agents.

## Architectures multi-agents

<span id="page-374-0"></span>À mesure que la taille, la portée ou la complexité des agents LLM augmentent, plusieurs problèmes peuvent apparaître et avoir un impact sur leurs performances, tels que les suivants :

- <span id="page-374-4"></span>L'agent a trop d'outils parmi lesquels choisir et prend de mauvaises décisions quant à l'outil à appeler ensuite [\(Chapitre](#page-315-0) 6 a discuté de certaines approches de ce problème).
- <span id="page-374-1"></span>Le contexte devient trop complexe pour qu'un seul agent puisse en assurer le suivi ; c'est-à-dire que la taille des invites et le nombre de choses qu'elles mentionnent dépassent les capacités du modèle que vous utilisez.
- <span id="page-374-3"></span>Vous souhaitez utiliser un sous-système spécialisé pour un domaine particulier, par exemple la planification, la recherche, la résolution de problèmes mathématiques, etc.

<span id="page-374-2"></span>Pour résoudre ces problèmes, vous pouvez envisager de diviser votre application en plusieurs agents plus petits et indépendants et de les composer dans un système multi-agents. Ces agents indépendants peuvent être aussi simples qu'une invite et un appel LLM ou aussi complexes qu'un agent ReAct (introduit dans le [Chapitre](#page-315-0) 6). La [Figure](#page-375-0) 7-3 illustre plusieurs façons de connecter des agents dans un système multi-agents.

<span id="page-375-0"></span>![](_page_375_Figure_0.jpeg)

Figure 7-3. Plusieurs stratégies pour coordonner plusieurs agents

Regardons la [Figure](#page-375-0) 7-3 plus en détail :

*Réseau*

Chaque agent peut communiquer avec tous les autres agents. N'importe quel agent peut décider quel autre agent doit être exécuté ensuite.

*Superviseur*
<span id="page-376-0"></span>Chaque agent communique avec un seul agent, appelé *superviseur*. L'agent superviseur décide quel agent (ou quels agents) doit être appelé ensuite. Un cas particulier de cette architecture implémente l'agent superviseur sous forme d'appel LLM avec des outils, comme couvert dans le [Chapitre](#page-315-0) 6.

#### *Hiérarchique*

Vous pouvez définir un système multi-agents avec un superviseur de superviseurs. Il s'agit d'une généralisation de l'architecture du superviseur et permet des flux de contrôle plus complexes.

#### *Workflow multi-agent personnalisé*

Chaque agent communique uniquement avec un sous-ensemble d'agents. Certaines parties du flux sont déterministes et seuls des agents sélectionnés peuvent décider quels autres agents appeler ensuite.

La section suivante approfondit l'architecture du superviseur, qui, selon nous, présente un bon équilibre entre capacités et facilité d'utilisation.

### **Architecture du superviseur**

Dans cette architecture, nous ajoutons chaque agent au graphe en tant que nœud et ajoutons également un nœud superviseur, qui décide quels agents doivent être appelés ensuite. Nous utilisons des arêtes conditionnelles pour acheminer

exécution vers le nœud d'agent approprié en fonction de la décision du superviseur. Reportez-vous au [Chapitre](#page-277-0) 5 pour une introduction à LangGraph, qui passe en revue les concepts de nœuds, d'arêtes, etc.

Voyons d'abord à quoi ressemble le nœud superviseur :

<span id="page-377-0"></span>*Python*

```
from typing import Literal
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
```

```
class SupervisorDecision(BaseModel):
 next: Literal["researcher", "coder", "FINISH"
```

```
model = ChatOpenAI(model="gpt-4o", temperature=0)
model = model.with_structured_output(SupervisorDe
```

```
agents = ["researcher", "coder"]
```

```
system_prompt_part_1 = f"""You are a supervisor t
conversation between the following workers: {agen
request, respond with the worker to act next. Eac
task and respond with their results and status. W
respond with FINISH."""
```

```
system_prompt_part_2 = f"""Given the conversation
 should we FINISH? Select one of: {', '.join(a
def supervisor(state):
 messages = [
 ("system", system_prompt_part_1),
 *state["messages"],
 ("system", system_prompt_part_2)
 ]
 return model.invoke(messages)
```
<span id="page-378-0"></span>*JavaScript*

```
import { ChatOpenAI } from 'langchain-openai';
import { z } from 'zod';
const SupervisorDecision = z.object({
 next: z.enum(['researcher', 'coder', 'FINISH'])
});
const model = new ChatOpenAI({ model: 'gpt-4o', t
const modelWithStructuredOutput = model.withStruc
const agents = ['researcher', 'coder'];
```

```
const systemPromptPart1 = `You are a supervisor t
 conversation between the following workers: ${a
 following user request, respond with the worker
 will perform a task and respond with their resu
 finished, respond with FINISH.`;
```

```
const systemPromptPart2 = `Given the conversation
 should we FINISH? Select one of: ${agents.join(
```

```
const supervisor = async (state) => {
 const messages = [
 { role: 'system', content: systemPromptPart1
 ...state.messages,
 { role: 'system', content: systemPromptPart2
 ];
 return await modelWithStructuredOutput.invoke({
};
```
#### **REMARQUE**

<span id="page-379-0"></span>Le code dans l'invite exige que les noms de vos sous-agents soient explicites et distincts. Par exemple, s'ils étaient simplement appelés agent\_1 et agent\_2 , le LLM n'aurait aucune information pour décider lequel est approprié pour chaque tâche. Si nécessaire, vous pouvez modifier l'invite pour ajouter une description de chaque agent, ce qui pourrait aider le LLM à choisir un agent pour chaque requête.

Voyons maintenant comment intégrer ce nœud superviseur dans un graphe plus grand qui comprend deux autres sous-agents, que nous appellerons chercheur et codeur. Notre objectif global avec ce graphe est de traiter des requêtes auxquelles le chercheur peut répondre seul, ou le codeur lui-même, ou même les deux successivement. Cet exemple n'inclut pas d'implémentations pour le chercheur ou le codeur. L'idée clé est qu'il peut s'agir de n'importe quel autre graphe ou nœud LangGraph :

#### <span id="page-380-0"></span>*Python*

```
from typing import Literal
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesS
model = ChatOpenAI()
class AgentState(BaseModel):
 next: Literal["researcher", "coder", "FINISH"
def researcher(state: AgentState):
 response = model.invoke(...)
 return {"messages": [response]}
def coder(state: AgentState):
 response = model.invoke(...)
```

```
 return {"messages": [réponse]}
constructeur = StateGraph (AgentState)
builder.add_node (superviseur)
builder.add_node (chercheur)
builder.add_node (codeur)
builder.add_edge(START, "superviseur")
# itinéraire vers l'un des agents ou sortie en fonction du
builder.add_conditional_edges("superviseur", lambd
builder.add_edge("chercheur", "superviseur")
builder.add_edge("codeur", "superviseur")
superviseur = builder.compile()
```
#### <span id="page-381-0"></span>*JavaScript*

```
importer {
 Graphique d'état,
 Annotations,
 MessagesAnnotation,
 COMMENCER,
 FIN,
} de "@langchain/langgraph" ;
importer { ChatOpenAI } depuis "@langchain/openai" ;
```

```
modèle const = nouveau ChatOpenAI ({
 modèle : "gpt-4o",
});
const StateAnnotation = Annotation.Root({
 ...MessagesAnnotation.spec,
 suivant : Annotation(),
});
const chercheur = async (état) => {
 const réponse = wait model.invoke(...);
 return { messages : [réponse] } ;
} ;
const codeur = async (état) => {
 const réponse = wait model.invoke(...);
 return { messages : [réponse] } ;
} ;
const graph = nouveau StateGraph (StateAnnotation)
 .addNode("superviseur", superviseur)
 .addNode("chercheur", chercheur)
 .addNode("codeur", codeur)
 .addEdge(START, "superviseur")
 // route vers l'un des agents ou sortie en fonction de 
 .addConditionalEdges("superviseur", asynchrone (état
 state.next === 'TERMINER' ? FIN : état.suivant)
 .addEdge("chercheur", "superviseur")
```

```
 .addEdge("codeur", "superviseur")
 .compile();
```
Quelques points à noter : dans cet exemple, les deux sous-agents (chercheur et codeur) peuvent voir le travail de chacun, car toute la progression est enregistrée dans la liste des messages. Ce n'est pas la seule façon d'organiser cela. Chacun des sous-agents pourrait être plus complexe. Par exemple, un sous-agent pourrait être son propre graphique qui maintient son état interne et ne produit qu'un résumé du travail qu'il a effectué.

Après l'exécution de chaque agent, nous retournons au nœud superviseur, qui décide s'il y a plus de travail à faire et à quel agent déléguer cela si c'est le cas. Ce routage n'est pas une exigence stricte pour cette architecture ; nous pourrions demander à chaque sous-agent de décider si sa sortie doit être renvoyée directement à l'utilisateur. Pour ce faire, nous remplacerions la limite dure entre, disons, le chercheur et le superviseur, par une limite conditionnelle (qui lirait une clé d'état mise à jour par le chercheur).

## <span id="page-383-0"></span>Résumé

Ce chapitre a couvert deux extensions importantes de l'architecture d'agent : les architectures de réflexion et multi-agents. Le chapitre a également examiné comment travailler avec des sous-graphes dans

LangGraph, qui constitue un élément clé des systèmes multi-agents.

Ces extensions ajoutent plus de puissance à l'architecture d'agent LLM, mais elles ne devraient pas être la première chose que vous recherchez lors de la création d'un nouvel agent. Le meilleur point de départ est généralement l'architecture simple dont nous avons parlé dans le [Chapitre](#page-315-0) 6.

[Chapitre](#page-385-0) 8 revient sur le compromis entre fiabilité et agence, qui est la décision de conception clé lors de la création d'applications LLM aujourd'hui. Ceci est particulièrement important lors de l’utilisation d’architectures à agents ou multi-agents, car leur puissance se fait au détriment de la fiabilité si rien n’est fait pour les contrôler. Après avoir approfondi les raisons pour lesquelles ce compromis existe, le [Chapitre](#page-385-0) 8 couvrira les techniques les plus importantes à votre disposition pour prendre cette décision et, à terme, améliorer vos applications et agents LLM.

## <span id="page-385-0"></span>Chapitre 8. Modèles pour tirer le meilleur parti des LLM

Les LLM ont aujourd'hui des limites majeures, mais cela ne signifie pas que l'application LLM de vos rêves est impossible à créer. L'expérience que vous concevez pour les utilisateurs de votre application doit contourner, et idéalement avec, les limitations.

<span id="page-385-4"></span><span id="page-385-3"></span><span id="page-385-2"></span><span id="page-385-1"></span>[Chapitre](#page-277-0) 5 a abordé le compromis clé auquel nous sommes confrontés lors de la création d'applications LLM : le compromis entre *l'agence* (le La capacité du LLM à agir de manière autonome) et la *fiabilité* (le degré auquel nous pouvons faire confiance à ses résultats). Intuitivement, toute application LLM nous sera plus utile si elle entreprend plus d'actions sans notre implication, mais si nous laissons l'agence aller trop loin, l'application fera inévitablement des choses que nous souhaiterions qu'elle ne fasse pas.

La [Figure](#page-386-0) 8-1 illustre ce compromis.

<span id="page-386-0"></span>![](_page_386_Figure_0.jpeg)

<span id="page-386-2"></span><span id="page-386-1"></span>Figure 8-1. Le compromis agence-fiabilité
Pour emprunter un concept à d'autres domaines, nous pouvons visualiser le compromis comme une *frontière* : tous les points sur la ligne courbe de la frontière sont des architectures LLM optimales pour certaines applications, marquant différents choix entre agence et fiabilité. (Reportez-vous au [Chapitre](#page-277-0) 5 pour un aperçu des différentes architectures d'applications LLM.) À titre d'exemple, remarquez comment l'architecture de la chaîne a une agence relativement faible mais une fiabilité plus élevée, **[1](#page-423-0)**

alors que l'architecture Agent a une agence plus élevée au détriment d'une fiabilité moindre.

Abordons brièvement un certain nombre d'objectifs supplémentaires (mais toujours importants) que vous souhaiteriez peut-être que votre candidature LLM ait. Chaque application LLM sera conçue pour une combinaison différente d'un ou plusieurs de ces objectifs :

#### *Latence*

<span id="page-387-1"></span>Réduire le temps nécessaire pour obtenir la réponse finale

#### *Autonomie*

<span id="page-387-0"></span>Minimiser les interruptions dues à la contribution humaine

#### *Écart*

<span id="page-387-2"></span>Minimiser les variations entre les invocations

Il ne s'agit pas d'une liste exhaustive de tous les objectifs possibles, mais plutôt d'une illustration des compromis auxquels vous êtes confronté lors de la création de votre application. Chaque objectif est quelque peu en contradiction avec tous les autres (par exemple, le chemin le plus simple vers une fiabilité plus élevée nécessite soit une latence plus élevée, soit une autonomie plus faible). Chaque objectif annulerait les autres s’il était pleinement pris en compte (par exemple, l’application à latence minimale est celle qui ne fait rien du tout). La [Figure](#page-388-0) 8-2 illustre ce concept.

<span id="page-388-0"></span>![](_page_388_Figure_0.jpeg)

Figure 8-2. Déplacer les frontières, ou plus d'agence, pour la même fiabilité

Ce que nous souhaitons vraiment en tant que développeurs d’applications, c’est déplacer la frontière vers l’extérieur. Pour le même niveau de fiabilité, nous aimerions atteindre une agence plus élevée ; et pour le même niveau d'agence, nous aimerions atteindre une plus grande fiabilité. Ce chapitre couvre un certain nombre de techniques que vous pouvez utiliser pour y parvenir :

#### *Streaming/sortie intermédiaire*

Une latence plus élevée est plus facile à accepter s'il y a une certaine communication de la progression/du résultat intermédiaire tout au long.

#### *Sortie structurée*

Exiger qu'un LLM produise un résultat dans un format prédéfini augmente la probabilité qu'il soit conforme aux attentes.

#### *L'humain dans la boucle*

Les architectures des agences supérieures bénéficient de l'intervention humaine pendant leur fonctionnement : interruption, approbation, bifurcation ou annulation.

#### *Modes d'envoi de doubles SMS*

<span id="page-389-0"></span>Plus une application LLM met du temps à répondre, plus il est probable que l'utilisateur lui envoie une nouvelle entrée avant la fin du traitement de la précédente.

## Sortie structurée

<span id="page-389-1"></span>Il est souvent crucial que les LLM renvoient une sortie structurée, soit parce qu'une utilisation en aval de cette sortie attend des éléments dans un *schéma* spécifique (une définition des noms et des types des

divers champs dans une sortie structurée) ou simplement pour réduire la variance par rapport à ce qui serait autrement une sortie texte complètement libre.

<span id="page-390-1"></span>Il existe différentes stratégies que vous pouvez utiliser pour cela avec différents LLM :

#### *Invite*

<span id="page-390-0"></span>C'est à ce moment-là que vous demandez (très gentiment) au LLM de renvoyer la sortie dans le format souhaité (par exemple, JSON, XML ou CSV). Le gros avantage de l'invite est qu'elle fonctionne dans une certaine mesure avec n'importe quel LLM ; l'inconvénient est qu'il s'agit davantage d'une suggestion au LLM et non d'une garantie que le résultat sera publié dans ce format.

#### *Appel de l'outil*

<span id="page-390-2"></span>Ceci est disponible pour les LLM qui ont été affinés pour choisir parmi une liste de schémas de sortie possibles et pour produire quelque chose qui est conforme à celui choisi. Cela implique généralement d'écrire, pour chacun des schémas de sortie possibles : un nom pour l'identifier, une description pour aider le LLM à décider quand c'est le choix approprié, et un schéma pour le format de sortie souhaité (généralement en notation JSONSchema).

*Mode JSON*

<span id="page-391-0"></span>Il s'agit d'un mode disponible dans certains LLM (tels que les modèles OpenAI récents) qui oblige le LLM à générer un document JSON valide.

Différents modèles peuvent en prendre en charge différentes variantes, avec des paramètres légèrement différents. Pour permettre aux LLM de renvoyer facilement une sortie structurée, les modèles LangChain implémentent une interface commune, une méthode appelée
.avec\_structured\_output . En appelant cette méthode et en transmettant un schéma JSON ou un modèle Pydantic (en Python) ou Zod (en JS), le modèle ajoutera tous les paramètres de modèle et analyseurs de sortie nécessaires pour produire et renvoyer la sortie structurée. Lorsqu'un modèle particulier implémente plusieurs des stratégies précédentes, vous pouvez configurer la méthode à utiliser.

Créons un schéma à utiliser :

<span id="page-391-1"></span>*Python*

à partir de l'importation pydantic BaseModel, Field

blague de classe (BaseModel):

```
 setup: str = Field(description="The setup of 
 punchline: str = Field(description="The punch
```
<span id="page-392-0"></span>*JavaScript*

c ass Jo e (ase ode)

```
import { z } from "zod";
const joke = z.object({
 setup: z.string().describe("The setup of the jo
 punchline: z.string().describe("The punchline t
});
```
Remarquez comment nous prenons soin d'ajouter une description à chaque champ. Ceci est essentiel car, avec le nom du champ, ce sont les informations que le LLM utilisera pour décider quelle partie du résultat doit être placée dans chaque champ. Nous aurions également pu définir un schéma en notation brute JSONSchema, qui ressemblerait à ceci :

```
{'properties': {'setup': {'description': 'The set
 'title': 'Setup',
 'type': 'string'},
 'punchline': {'description': 'The punchline to t
```

```
'title': 'Punchline'
```

```
 'title': 'Punchline',
 'type': 'string'}},
 'required': ['setup', 'punchline'],
 'title': 'Joke',
 'type': 'object'}
```
Et maintenant, obtenons un LLM pour générer une sortie conforme à ce schéma :

<span id="page-393-1"></span>*Python*

```
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-3.5-turbo", tempera
model = model.with_structured_output(Joke)
model.invoke("Tell me a joke about cats")
```
<span id="page-393-0"></span>*JavaScript*

```
import { ChatOpenAI } from "@langchain/openai";
let model = new ChatOpenAI({
 model: "gpt-3.5-turbo",
```

```
 temperature: 0
});
model = model.withStructuredOutput(joke);
await structuredLlm.invoke("Tell me a joke about
```
#### *Un exemple de sortie*

```
{
 setup: "Why don't cats play poker in the wild
 punchline: "Too many cheetahs."
}
```
Quelques choses à remarquer :

- Nous créons l'instance du modèle comme d'habitude, en spécifiant le nom du modèle à utiliser et d'autres paramètres.
- Une température basse convient généralement bien à une sortie structurée, car elle réduit le risque que le LLM produise une sortie invalide non conforme au schéma.
- Ensuite, nous attachons le schéma au modèle, qui renvoie un nouvel objet, qui produira une sortie correspondant au schéma fourni. Lorsque vous passez un objet Pydantic ou Zod

pour le schéma, cela sera également utilisé pour la validation ; autrement dit, si le LLM produit une sortie non conforme, une erreur de validation vous sera renvoyée au lieu de la sortie ayant échoué.

Enfin, nous invoquons le modèle avec notre entrée (de forme libre) et recevons une sortie qui correspond à la structure souhaitée.

Ce modèle d'utilisation de la sortie structurée peut être très utile à la fois en tant qu'outil autonome et en tant que partie d'une application plus vaste ; par exemple, reportez-vous au [Chapitre](#page-277-0) 5, où nous utilisons cette capacité pour implémenter l'étape de routage de l'architecture du routeur.

### **Sortie intermédiaire**

<span id="page-395-0"></span>Plus votre architecture LLM devient complexe, plus son exécution risque de prendre plus de temps. Si vous repensez aux diagrammes d'architecture des chapitres [5](#page-277-0) et [6,](#page-315-0) chaque fois que vous voyez plusieurs étapes (ou nœuds) connectées en séquence ou en boucle, cela indique que le temps nécessaire pour un appel complet augmente.

<span id="page-395-1"></span>Cette augmentation de la latence, si elle n'est pas résolue, peut bloquer l'adoption par les utilisateurs des applications LLM, la plupart des utilisateurs s'attendant à ce que les applications informatiques produisent des résultats en quelques secondes. Il existe plusieurs stratégies pour rendre la latence plus élevée plus

acceptable, mais ils relèvent tous de la *sortie en streaming*, c'est-à-dire recevoir la sortie de l'application pendant qu'elle est encore en cours d'exécution.

Pour cette section, nous utiliserons la dernière architecture décrite dans ["Dealing](#page-342-0) with Many Tools". Reportez-vous au [Chapitre](#page-315-0) 6 pour l'extrait de code complet.

<span id="page-396-3"></span><span id="page-396-1"></span>Pour générer une sortie intermédiaire avec LangGraph, tout ce que vous avez à faire est d'invoquer le graphe avec la méthode stream, qui produira la sortie de chaque nœud dès que chacun se terminera. Voyons à quoi cela ressemble :
<span id="page-396-2"></span>*Python*

```
input = {
 "messages": [
 HumanMessage("""How old was the 30th pres
 when he died?""")
 ]
}
for c in graph.stream(input, stream_mode='updates
 print(c)
```
<span id="page-396-0"></span>*JavaScript*

```
const input = {
 messages: [
 new HumanMessage(`How old was the 30th presid
 he died?`)
 ]
}
const output = await graph.stream(input, streamMo
for await (const c of output) {
 console.log(c)
}
```
*La sortie :*

```
{
 "select_tools": {
 "selected_tools": ['duckduckgo_search', 
 }
}
{
 "model": {
 "messages": AIMessage(
 content="",
 tool_calls=[
 {
 "name": "duckduckgo_search",
```

```
 "args": {
 "query": "30th president 
 },
 "id": "9ed4328dcdea4904b1b544
 "type": "tool_call",
 }
 ],
 )
 }
}
{
 "tools": {
 "messages": [
 ToolMessage(
 content="Calvin Coolidge (born Ju
 U.S.—died January 5, 1933, No
 the 30th president of the Uni
 acceded to the presidency aft
 Warren G. Harding, just as th
 to light....",
 name="duckduckgo_search",
 tool_call_id="9ed4328dcdea4904b1b
 )
 ]
 }
}
{
 "model": {
```

```
 "messages": AIMessage(
 content="Calvin Coolidge, the 30th pr
 was born on July 4, 1872, and die
 calculate his age at the time of 
 birth year from his death year. \
 Birth year\nAge at death = 1933 -
 years\n\nCalvin Coolidge was 61 y
 )
 }
}
```
Remarquez comment chaque entrée de sortie est un dictionnaire avec le nom du nœud émis comme clé et la sortie de ce nœud comme valeur. Cela vous donne deux informations clés :

- Où se trouve actuellement la demande ; Autrement dit, si vous repensez aux diagrammes d'architecture présentés dans les chapitres précédents, où en sommes-nous actuellement dans ce diagramme ?
- Chaque mise à jour de l'état partagé de l'application, qui ensemble constitue la sortie finale du graphique.

<span id="page-399-0"></span>De plus, LangGraph prend en charge davantage de modes de flux :

- <span id="page-399-1"></span>mises à jour. Il s'agit du mode par défaut, décrit ci-dessus.
- <span id="page-399-2"></span>valeurs . Ce mode donne l'état actuel du graphique à chaque fois qu'il change, c'est-à-dire après la fin de chaque ensemble de nœuds.

exécution. Cela peut être utile lorsque la façon dont vous affichez la sortie à vos utilisateurs suit de près la forme de l'état du graphique.

- <span id="page-400-1"></span><span id="page-400-0"></span>débogage. Ce mode génère des événements détaillés chaque fois que quelque chose se produit dans votre graphique, notamment :
	- événements de point de contrôle, chaque fois qu'un nouveau point de contrôle de l'état actuel est enregistré dans la base de données
	- événements de tâches, émis chaque fois qu'un nœud est sur le point de commencer à s'exécuter
	- événements task\_result, émis chaque fois qu'un nœud termine son exécution
- <span id="page-400-5"></span>Enfin, vous pouvez combiner ces modes ; par exemple, demander à la fois des mises à jour et des valeurs en transmettant une liste.

<span id="page-400-3"></span>Vous contrôlez le mode flux avec l'argument stream\_mode de stream() .

### **Streaming de sortie LLM jeton par jeton**

<span id="page-400-4"></span><span id="page-400-2"></span>Parfois, vous souhaiterez peut-être également obtenir une sortie en streaming de chaque appel LLM dans votre application LLM plus grande. Cela peut être utile pour divers projets, comme lors de la création d'un chatbot interactif, où vous souhaitez que chaque mot soit affiché dès qu'il est produit par le LLM.

<span id="page-401-1"></span>Vous pouvez également y parvenir avec LangGraph :

#### <span id="page-401-2"></span>*Python*

```
input = {
 "messages": [
 HumanMessage("""How old was the 30th pres
 when he died?""")
 ]
}
output = app.astream_events(input, version="v2")
async for event in output:
 if event["event"] == "on_chat_model_stream":
 content = event["data"]["chunk"].content
 if content:
 print(content)
```
<span id="page-401-0"></span>*JavaScript*

```
const input = {
 messages: [
 new HumanMessage(`How old was the 30th presid
 he died?`)
 ]
```

```
}
const output = await agent.streamEvents(input, {v
for await (const { event, data } of output) {
 if (event === "on_chat_model_stream") {
 const msg = data.chunk as AIMessageChunk;
 if (msg.content) {
 console.log(msg.content);
 }
 }
}
```
Celui-ci émettra chaque mot (techniquement chaque jeton) dès qu'il sera reçu du LLM. Vous pouvez trouver plus de détails sur ce modèle sur [LangChain](https://oreil.ly/ExYll).

### **Modalités de l'humain dans la boucle**
<span id="page-402-0"></span>À mesure que nous gravissons les échelons de l'autonomie (ou de l'agence), nous nous retrouvons de plus en plus à abandonner le contrôle (ou la surveillance) en échange de capacités (ou d'autonomie). Le modèle d'état partagé utilisé dans LangGraph (voir [Chapitre](#page-277-0) 5 pour une introduction) facilite l'observation, l'interruption et la modification de l'application. Cela permet d'utiliser de nombreux modes différents *human-in-the-loop*, ou

moyens permettant au développeur/utilisateur final d'une application d'influencer ce que fait le LLM.

Pour cette section, nous utiliserons à nouveau la dernière architecture décrite dans ["Dealing](#page-342-0) with Many Tools". Reportez-vous au [Chapitre](#page-315-0) 6 pour l'extrait de code complet. Pour tous les modes "humain dans la boucle", nous devons d'abord attacher un [point de contrôle](#page-257-0) au graphique ; reportez-vous à « Ajout de mémoire à StateGraph » pour plus de détails à ce sujet :

#### <span id="page-403-0"></span>*Python*

à partir de langgraph.checkpoint.memory import MemorySav graph = builder.compile(checkpointer=MemorySaver(

#### *JavaScript*

```
import {MemorySaver} from '@langchain/langgraph'
graph = builder.compile({ checkpointer: new Memor
```
<span id="page-403-1"></span>Cela renvoie une instance du graphique qui stocke l'état à la fin de chaque étape, de sorte que chaque invocation après la première ne démarre pas

à partir d'une page vierge. Chaque fois que le graphique est appelé, il commence par utiliser le point de contrôle pour récupérer l'état enregistré le plus récent (le cas échéant) et combine la nouvelle entrée avec l'état précédent. Et ce n’est qu’alors qu’il exécute les premiers nœuds. Ceci est essentiel pour permettre les modalités de l'humain dans la boucle, qui reposent toutes sur le graphe mémorisant l'état précédent.

<span id="page-404-0"></span>Le premier mode, interruption , est la forme de contrôle la plus simple : l'utilisateur regarde la sortie en streaming de l'application au fur et à mesure de sa production, et l'interrompt manuellement quand il le juge opportun (voir [Figure](#page-405-0) 8-3). L'état est enregistré à partir de la dernière étape complète avant que l'utilisateur n'appuie sur le bouton d'interruption. À partir de là, l'utilisateur peut choisir de :

- Reprenez à partir de ce moment, et le calcul se poursuivra comme s'il n'avait pas été interrompu (voir ["Resume"\)](#page-411-0).
- Envoyez une nouvelle entrée dans l'application (par exemple, un nouveau message dans un chatbot), ce qui annulera toutes les étapes futures en attente et commencera à traiter la nouvelle entrée (voir ["Redémarrer"](#page-412-0)).
- Ne faites rien et rien d'autre ne fonctionnera.

<span id="page-405-0"></span>![](_page_405_Figure_0.jpeg)

Figure 8-3. Le modèle d'interruption

Voyons comment procéder dans LangGraph :

*Python*

importer un événement asyncio = asyncio.Event()

```
input = {
 "messages": [
 HumanMessage("""How old was the 30th pres
 when he died?""")
 ]
}
config = {"configurable": {"thread_id": "1"}}
async with aclosing(graph.astream(input, config))
 async for chunk in stream:
 if event.is_set():
 break
 else:
 ... # do something with the output
# Somewhere else in your application
event.set()
```
#### *JavaScript*

```
const controller = new AbortController()
const input = {
  "messages": [
```

```
 messages : [
 new HumanMessage(`How old was the 30th presid
 he died?`)
 ]
}
const config = {"configurable": {"thread_id": "1"
try {
 const output = await graph.stream(input, {
 ...config,
 signal: controller.signal
 });
 for await (const chunk of output) {
 console.log(chunk); // do something with the 
 }
} catch (e) {
 console.log(e);
}
// Somewhere else in your application
controller.abort()
```
Cela utilise un événement ou un signal, afin que vous puissiez contrôler l'interruption depuis l'extérieur de l'application en cours d'exécution. Notez dans le bloc de code Python l'utilisation de aclosing ; cela garantit que le flux est correctement fermé lorsqu'il est interrompu. Notez dans JS l'utilisation <span id="page-408-2"></span>de l'instruction try-catch, car l'interruption de l'exécution entraînera la levée d'une exception d'abandon. Notez enfin que l'utilisation du point de contrôle nécessite de transmettre un identifiant pour ce thread, afin de distinguer cette interaction avec le graphique de toutes les autres.

<span id="page-408-0"></span>![](_page_408_Figure_1.jpeg)

Figure 8-4. Le modèle d'autorisation

<span id="page-408-1"></span>Un deuxième mode de contrôle est authorize , dans lequel l'utilisateur définit à l'avance qu'il souhaite que l'application lui cède le contrôle à chaque fois qu'un nœud particulier est sur le point d'être appelé (voir [Figure](#page-408-0) 8-4). Ceci est généralement implémenté pour la confirmation de l'outil. Avant qu'un outil (ou des outils particuliers) ne soit appelé, l'application s'arrêtera et demandera une confirmation, auquel cas l'utilisateur peut à nouveau :
- Reprendre le calcul en acceptant l'appel de l'outil.
- Envoyer un nouveau message pour guider le bot dans une direction différente, auquel cas l'outil ne sera pas appelé.
- Ne fais rien.

Voici le code :

*Python*

```
input = {
 "messages": [
 HumanMessage("""How old was the 30th pres
 when he died?""")
 ]
}
config = {"configurable": {"thread_id": "1"}}
output = graph.astream(input, config, interrupt_b
async for c in output:
 ... # do something with the output
```
#### *JavaScript*

```
const input = {
 "messages": [
 new HumanMessage(`How old was the 30th presid
 he died?`)
 ]
}
const config = {"configurable": {"thread_id": "1"
const output = await graph.stream(input, {
 ...config,
 interruptBefore: ['tools']
});
for await (const chunk of output) {
 console.log(chunk); // do something with the ou
}
```
Cela exécutera le graphique jusqu'à ce qu'il soit sur le point d'entrer dans le nœud appelé tools , vous donnant ainsi la possibilité d'inspecter l'état actuel et de décider de continuer ou non. Notez que l'interruption\_before est une liste où l'ordre n'est pas important ; si

vous transmettez plusieurs noms de nœuds, il s'interrompra avant de saisir chacun d'eux.

#### <span id="page-411-0"></span>**Reprendre**

<span id="page-411-1"></span>Pour continuer à partir d'un graphe interrompu, comme lors de l'utilisation de l'un des deux modèles précédents, il vous suffit de ré-invoquer le graphe avec une entrée nulle (ou None en Python). Ceci est considéré comme un signal pour continuer le traitement de l'entrée non nulle précédente :

*Python*

```
config = {"configurable": {"thread_id": "1"}}
output = graph.astream(None, config, interrupt_be
async for c in output:
 ... # do something with the output
```
*JavaScript*

const config = {"configurable": {"thread\_id": "1"

```
const output = await graph.stream(null, {
 ...config,
 interruptBefore: ['tools']
});
for await (const chunk of output) {
 console.log(chunk); // do something with the ou
}
```
#### <span id="page-412-0"></span>**Redémarrer**

<span id="page-412-1"></span>Si à la place vous souhaitez qu'un graphe interrompu recommence à partir du premier nœud, avec une nouvelle entrée supplémentaire, il vous suffit de l'invoquer avec une nouvelle entrée :

*Python*

```
input = {
 "messages": [
 HumanMessage("""How old was the 30th pres
 when he died?""")
 ]
}
```

```
config = {"configurable": {"thread_id": "1"}}
output = graph.astream(input, config)
async for c in output:
 ... # do something with the output
```
#### *JavaScript*

```
const input = {
 "messages": [
 new HumanMessage(`How old was the 30th presid
 he died?`)
 ]
}
const config = {"configurable": {"thread_id": "1"
const output = await graph.stream(input, config);
for await (const chunk of output) {
 console.log(chunk); // do something with the ou
}
```
Cela conservera l'état actuel du graphique, le fusionnera avec la nouvelle entrée et recommencera à partir du premier nœud.

Si vous souhaitez perdre l'état actuel, modifiez simplement le thread\_id , ce qui démarrera une nouvelle interaction à partir d'une ardoise vierge. Toute valeur de chaîne est un thread\_id valide ; nous vous recommandons d'utiliser des UUID (ou d'autres identifiants uniques) comme identifiants de thread.

#### **Modifier l'état**

<span id="page-414-0"></span>Parfois, vous souhaiterez peut-être mettre à jour l'état du graphique avant de reprendre ; ceci est possible avec la méthode update\_state. Vous souhaiterez généralement d’abord inspecter l’état actuel avec get\_state .

Voici à quoi cela ressemble :

*Python*

```
config = {"configurable": {"thread_id": "1"}}
state = graph.get_state(config)
# something you want to add or replace
update = { }
```

```
graph.update_state(config, update)
```
*JavaScript*

```
const config = "configurable": {"thread_id": "1"}
const state = await graph.getState(config)
// something you want to add or replace
const update = { }
await graph.updateState(config, update)
```
Cela créera un nouveau point de contrôle contenant votre mise à jour. Après cela, vous êtes prêt à reprendre le graphique à partir de ce nouveau point. Voir ["Resume"](#page-411-0) pour savoir comment procéder.

#### **Fourchette**

<span id="page-415-0"></span>Vous pouvez également parcourir l'historique de tous les états passés par lesquels le graphique est passé, et chacun d'entre eux peut être visité à nouveau, par exemple, pour obtenir une réponse alternative. Cela peut être très utile dans des applications plus créatives, où chaque parcours du graphique devrait produire un résultat différent.

Voyons à quoi cela ressemble :

#### *Python*

```
config = {"configurable": {"thread_id": "1"}}
history = [
 state for state in
 graph.get_state_history(config)
]
# replay a past state
graph.invoke(None, history[2].config)
```
*JavaScript*

```
const config = "configurable": {"thread_id": "1"}
const history = attendre Array.fromAsync (graph.getSt
// rejoue un état passé
attendre graph.invoke(null, history[2].config)
```
Remarquez comment nous collectons l'historique dans une liste/un tableau dans les deux langues ; get\_state\_history renvoie un itérateur d'états (pour permettre de consommer paresseusement). Les états renvoyés par la méthode historique sont triés en commençant par le plus récent et en dernier par le plus ancien.

<span id="page-417-2"></span>La véritable puissance des commandes humaines dans la boucle vient de leur mélange de la manière qui convient à votre application.

### **LLM multitâches**

<span id="page-417-1"></span><span id="page-417-0"></span>Cette section couvre le problème de la gestion des entrées simultanées pour les applications LLM. Il s'agit d'un problème particulièrement pertinent étant donné que les LLM sont assez lents, d'autant plus lorsqu'ils produisent de longues sorties ou lorsqu'ils sont enchaînés dans des architectures à plusieurs étapes (comme vous pouvez le faire avec LangGraph). Même si les LLM deviennent plus rapides, la gestion des entrées simultanées restera un défi, car les améliorations de la latence ouvriront également la porte à des cas d'utilisation de plus en plus complexes, de la même manière que même la personne la plus productive est toujours confrontée à la nécessité de prioriser des demandes concurrentes sur son temps.

Passons en revue les options.

#### **Refuser les entrées simultanées**

<span id="page-418-0"></span>Toute entrée reçue lors du traitement d'une précédente est rejetée. Il s'agit de la stratégie la plus simple, mais elle ne couvre probablement pas tous les besoins, car elle implique en fait de confier la gestion de la concurrence à l'appelant.

### **Gérer de manière indépendante**

<span id="page-418-2"></span>Une autre option simple consiste à traiter toute nouvelle entrée comme une invocation indépendante, en créant un nouveau thread (un conteneur pour mémoriser l'état) et en produisant une sortie dans ce contexte. Cela présente l'inconvénient évident de devoir être présenté à l'utilisateur sous la forme de deux invocations distinctes et inconciliables, ce qui n'est pas toujours possible ou souhaitable. D'un autre côté, il présente l'avantage de s'adapter à des tailles arbitrairement grandes et c'est quelque chose que vous utiliserez presque certainement dans une certaine mesure dans votre application. Par exemple, c’est ainsi que l’on pourrait envisager le problème consistant à faire en sorte qu’un chatbot « discute » simultanément avec deux utilisateurs différents.

#### **Mettre en file d'attente les entrées simultanées**

<span id="page-418-1"></span>Toute entrée reçue lors du traitement d'une précédente est mise en file d'attente et traitée lorsque l'entrée actuelle est terminée. Cette stratégie présente quelques avantages :

- Il prend en charge la réception d'un nombre arbitraire de requêtes simultanées.
- Parce que nous attendons que l'entrée actuelle termine le traitement, peu importe si la nouvelle entrée arrive presque immédiatement après avoir commencé à traiter l'entrée actuelle ou immédiatement avant de terminer ; le résultat final sera le même, car nous terminerons le traitement de l'entrée actuelle avant de passer à la suivante.

La stratégie souffre également de quelques inconvénients :

- Le traitement de toutes les entrées en file d'attente peut prendre un certain temps ; en fait, la file d’attente peut s’allonger de manière illimitée si les intrants sont produits à un rythme plus rapide que traités.
- Les entrées peuvent être périmées au moment où elles sont traitées, étant donné qu'elles sont mises en file d'attente avant de voir la réponse à la précédente, et ne sont pas modifiées par la suite. Cette stratégie n'est pas appropriée lorsque les nouvelles entrées dépendent des réponses précédentes.

#### **Interruption**

<span id="page-419-0"></span>Lorsqu'une nouvelle entrée est reçue alors qu'une autre est en cours de traitement, abandonnez le traitement de l'entrée actuelle et redémarrez la chaîne.

avec la nouvelle entrée. Cette stratégie peut varier en fonction de ce qui est conservé de l'exécution interrompue. Voici quelques options :

- Ne gardez rien. La saisie précédente est complètement oubliée, comme si elle n'avait jamais été envoyée ou traitée.
- Conserver la dernière étape réalisée. Dans une application de point de contrôle (qui stocke la progression au fur et à mesure du calcul), conservez l'état produit par la dernière étape terminée, supprimez toutes les mises à jour d'état en attente de l'étape en cours d'exécution et commencez à gérer la nouvelle entrée dans ce contexte.
- Conserver la dernière étape terminée, ainsi que l'étape en cours en cours. Essayez d'interrompre l'étape en cours tout en prenant soin de sauvegarder toutes les mises à jour incomplètes en cours de production à ce moment-là. Il est peu probable que cela se généralise au-delà des architectures les plus simples.
- Attendez la fin du nœud actuel (mais pas des nœuds suivants), puis enregistrez et interrompez.

Cette option présente certains avantages par rapport à la mise en file d'attente des entrées simultanées :

- Les nouvelles entrées sont traitées dès que possible, réduisant ainsi la latence et le risque de produire des sorties obsolètes.
- Pour la variante "ne rien conserver", le résultat final ne dépend pas du moment où la nouvelle entrée a été reçue.
Mais cela présente aussi des inconvénients :

- En effet, cette stratégie se limite encore à traiter une entrée à la fois ; toute ancienne entrée est abandonnée lorsqu'une nouvelle entrée est reçue.
- Garder des mises à jour partielles de l'état pour la prochaine exécution nécessite que l'état soit conçu dans cet esprit ; sinon, votre candidature risque de se retrouver dans un état invalide. Par exemple, les modèles de discussion OpenAI nécessitent qu'un message d'IA demandant que les appels d'outils soient immédiatement suivis de messages d'outils avec les sorties de l'outil. Si votre course est interrompue entre-temps, soit vous nettoyez défensivement l’état intermédiaire, soit vous risquez de ne pas pouvoir progresser davantage.
- Les résultats finaux produits sont très sensibles au moment où la nouvelle entrée est reçue ; la nouvelle entrée sera traitée dans le contexte des progrès (incomplets) précédemment réalisés vers la gestion de l'entrée précédente. Cela peut entraîner des résultats fragiles ou imprévisibles si vous ne concevez pas en conséquence.

#### **Fork et fusionner**

<span id="page-421-0"></span>Une autre option consiste à gérer les nouvelles entrées en parallèle, en bifurquant l'état du thread tel qu'il est lorsque la nouvelle entrée est reçue et en fusionnant les états finaux à mesure que les entrées finissent d'être traitées. Cette option nécessite de concevoir votre état pour qu'il soit fusionnable

sans conflits (par exemple, en utilisant des types de données répliquées sans conflit [CRDT] ou d'autres algorithmes de résolution de conflits) ou en demandant à l'utilisateur de résoudre manuellement les conflits avant de pouvoir donner un sens à la sortie ou envoyer une nouvelle entrée dans ce fil. Si l’une de ces deux conditions est remplie, il s’agit probablement de la meilleure option dans l’ensemble. De cette façon, les nouvelles entrées sont traitées en temps opportun, la sortie est indépendante de l’heure de réception et prend en charge un nombre arbitraire d’exécutions simultanées.

<span id="page-422-0"></span>Certaines de ces stratégies sont implémentées dans LangGraph Platform, qui seront couvertes dans le [Chapitre](#page-424-0) 9.

### Résumé

Dans ce chapitre, nous sommes revenus sur le principal compromis auquel vous êtes confronté lors de la création d'applications LLM : agence versus fiabilité. Nous avons appris qu'il existe des stratégies pour déjouer partiellement les pronostics et obtenir plus de fiabilité sans sacrifier l'agence, et vice versa.

Nous avons commencé par couvrir les sorties structurées, qui peuvent améliorer la prévisibilité du texte généré par LLM. Ensuite, nous avons discuté de l'émission de flux de sortie/sortie intermédiaire à partir de votre application, ce qui peut rendre les applications à haute latence (un effet secondaire inévitable de l'agence actuellement) agréables à utiliser.

Nous avons également passé en revue une variété de contrôles humains (c'est-à-dire des techniques permettant de redonner une certaine surveillance à l'utilisateur final de votre application LLM) qui peuvent souvent faire la différence dans la fiabilité des architectures de haute agence. Enfin, nous avons évoqué le problème de la gestion des entrées simultanées dans votre application, un problème particulièrement important pour les applications LLM compte tenu de leur latence élevée.

Dans le chapitre suivant, vous apprendrez comment déployer votre application d'IA en production.

<span id="page-423-0"></span>En finance, la *frontière efficace* dans l'optimisation de portefeuille ; en économie, une *frontière des possibilités de production* ; en ingénierie, le *front Pareto*. **[1](#page-386-1)**

# <span id="page-424-0"></span>Chapitre 9. Déploiement : lancement de votre application d'IA en production

Jusqu'à présent, nous avons exploré les concepts, idées et outils clés pour vous aider à créer les fonctionnalités de base de votre application d'IA. Vous avez appris à utiliser LangChain et LangGraph pour générer des sorties LLM, indexer et récupérer des données, et activer la mémoire et l'agence.

Mais votre application est limitée à votre environnement local, les utilisateurs externes ne peuvent donc pas encore accéder à ses fonctionnalités.

Dans ce chapitre, vous découvrirez les meilleures pratiques pour déployer votre application d'IA en production. Nous explorerons également divers outils pour déboguer, collaborer, tester et surveiller vos applications LLM.

Commençons.

## Prérequis

<span id="page-424-1"></span>Afin de déployer efficacement votre application d'IA, vous devez utiliser divers services pour héberger votre application, stocker et récupérer des données, et surveiller votre application. Dans l'exemple de déploiement de ce chapitre, nous intégrerons les services suivants :

*Magasin de vecteurs*

Supabase

*Surveillance et débogage*

LangSmith

*API back-end*

Plateforme LangGraph

Nous approfondirons chacun de ces composants et services et verrons comment les adapter à votre cas d’utilisation. Mais d’abord, installons les dépendances nécessaires et configurons les variables d’environnement.
Si vous souhaitez suivre [exemple, fork](https://oreil.ly/brqVm) ce modèle LangChain sur votre compte GitHub. Ce référentiel contient la logique complète d'une application d'IA basée sur un agent de récupération.

### **Installer les dépendances**

<span id="page-425-0"></span>Tout d'abord, suivez les instructions du fichier *[README.md](https://oreil.ly/N5eqe)* pour installer les dépendances du projet.

Si vous n'utilisez pas le modèle, vous pouvez installer les dépendances individuellement à partir des fichiers *pyproject.toml* ou *package.json* respectifs.

Deuxièmement, créez un fichier *.env* et stockez les variables suivantes :

```
OPENAI_API_KEY=
SUPABASE_URL=
SUPABASE_SERVICE_ROLE_KEY=
# for tracing
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.c
LANGCHAIN_API_KEY=
```
Nous passerons ensuite en revue le processus de récupération des valeurs de chacune de ces variables.

### **Grand modèle de langage**

<span id="page-426-0"></span>Le LLM est chargé de générer la sortie basée sur une requête donnée. LangChain donne accès aux fournisseurs LLM populaires, notamment OpenAI, Anthropic, Google et Cohere. <span id="page-427-1"></span>Dans cet exemple de déploiement, nous utiliserons OpenAI en récupérant les [clés](https://oreil.ly/MIpY5) de l'API, comme indiqué dans la [Figure](#page-427-0) 9-1. Une fois que vous avez récupéré vos clés API, saisissez la valeur OPENAI\_API\_KEY dans votre fichier *.env*.

<span id="page-427-0"></span>![](_page_427_Picture_1.jpeg)

Figure 9-1. Tableau de bord des clés API OpenAI

### **Magasin de vecteurs**

<span id="page-427-2"></span>Comme indiqué dans les chapitres précédents, un magasin de vecteurs est une base de données spéciale chargée de stocker et de gérer les représentations vectorielles de vos données, en d'autres termes, les intégrations. Un magasin de vecteurs permet la recherche de similarité et la récupération de contexte pour aider le LLM à générer des réponses précises basées sur la requête de l'utilisateur.

<span id="page-428-0"></span>Pour notre déploiement, nous utiliserons Supabase, une base de données PostgreSQL, comme magasin de vecteurs. Supabase utilise l'extension pgvector pour stocker les intégrations et les vecteurs de requête pour la recherche de similarité.

Si vous ne l'avez pas encore fait, créez un compte [Supabase](https://oreil.ly/CXDsx). Une fois que vous avez créé un compte, cliquez sur « Nouveau projet » sur la page du tableau de bord. Suivez les étapes et enregistrez le mot de passe de la base de données après l'avoir créé, comme indiqué dans la [Figure](#page-429-0) 9-2.

<span id="page-429-0"></span>

| Créer un nouveau projet | Votre projet aura sa propre instance dédiée et une base de données Postgres complète.<br>Une API sera mise en place afin que vous puissiez facilement interagir avec votre nouvelle base de données. |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Organisation | MVP bâtiment DB<br>V |
| Nom du projet | Nom du projet |
| Mot de passe de la base de données | Tapez un mot de passe fort<br>Il s'agit du mot de passe de votre base de données Postgres, il doit donc être<br>fort et difficile à deviner. Générer un mot de passe |
| Région | Est des États-Unis (Virginie du Nord)<br>V<br>Sélectionnez la région la plus proche de vos utilisateurs pour obtenir les meilleures performances.                                                        |
| OPTIONS DE SÉCURITÉ > |                                                                                                                                                           |
| Annuler | Vous pourrez renommer votre projet ultérieurement Créer un nouveau projet |

Figure 9-2. Tableau de bord de création de projet Supabase

Une fois votre projet Supabase créé, accédez à l'onglet Paramètres du projet et sélectionnez API sous Configuration. Sous ce nouvel onglet, vous verrez l'URL du projet et les clés API du projet.

Dans votre fichier *.env*, copiez et collez l'URL du projet comme valeur dans SUPABASE\_URL et la clé API secrète service\_role comme valeur dans SUPABASE\_SERVICE\_ROLE\_KEY .

Accédez à l'éditeur SQL dans le menu Supabase et exécutez les scripts SQL suivants. Tout d'abord, activons pgvector :

## Activer l'extension pgvector pour fonctionner avec le vecteur d'extension emb create ;

Créez maintenant une table appelée documents pour stocker les vecteurs de vos données :

```
## Créez un tableau pour stocker vos documents
créer des documents de table (
identifiant la clé primaire bigserial,
 texte du contenu, -- correspond à Document.pageCo
 métadonnées jsonb, -- correspond à Document.meta
 vecteur d'intégration (1536) -- 1536 fonctionne pour OpenAI
);
```
You should now see the documents table in the Supabase database.

Now you can create a script to generate the embeddings of your data, store them, and query from the database. Open the

Supabase SQL editor again and run the following script:

```
## Créer une fonction pour rechercher des documents
créer la fonction match_documents (
 vecteur query_embedding (1536),
 match_count int DEFAULT nul,
 filtre jsonb PAR DÉFAUT '{}'
) renvoie le tableau (
 je suis bigint,
 texte de contenu,
 métadonnées jsonb,
 intégrer jsonb,
 similarité flotteur
)
langage plpgsql
comme $$
#variable_conflict use_column
commencer
 requête de retour
 sélectionner
 pièce d'identité,
 contenu,
 métadonnées,
 (embedding::text)::jsonb comme intégration,
 1 - (documents.embedding <=> query_embedding)
 à partir de documents
 où les métadonnées @> filtrent
```

```
 trier par documents.embedding <=> query_embeddin
 limiter match_count ;
fin;
$$ ;
```
The match\_documents database function takes a query\_embedding vector and compares it to embeddings in the documents table using cosine similarity. It calculates a similarity score for each document (1 -

```
( documents.embedding <=> query_embedding )), puis
renvoie les correspondances les plus similaires. Les résultats sont :
```
- 1. Filtered first by the metadata criteria specified in the filter argument (using JSON containment @>).
- 2. Ordered by similarity score (highest first).
- 3. Limited to the number of matches specified in match\_count .

Once the vector similarity function is generated, you can use Supabase as a vector store by importing the class and providing the necessary parameters. Here's an example of how it works:

*Python*

import os

```
à partir de langchain_community.vectorstores importer Supa
à partir de langchain_openai importer OpenAIEmbeddings
à partir de supabase.client import Client, create_client
```

```
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_SERVICE_R
supabase : Client = create_client (supabase_url, su
```

```
intégrations = OpenAIEmbeddings()
```

```
## En supposant que vous avez déjà généré des intégrations o
```

```
vecteur_store = SupabaseVectorStore (
 intégration = intégrations,
 client = supabase,
 nom_table="documents",
 query_name="match_documents",
)
## Testez que la recherche de similarité fonctionne
query = "De quoi parle ce document ?"
```

```
matched_docs = vector_store.similarity_search(que
```

```
imprimer(matched_docs[0].page_content)
```
#### *JavaScript*

```
importer {
 SupabaseVectorStore
} de "@langchain/community/vectorstores/supabas
importer { OpenAIEmbeddings } depuis "@langchain/open
importer { createClient } depuis "@supabase/supabase-
const embeddings = new OpenAIEmbeddings();
const supabaseClient = createClient(
 processus.env.SUPABASE_URL,
 processus.env.SUPABASE_SERVICE_ROLE_KEY
);
const vectorStore = new SupabaseVectorStore (intégrer
 client : supabaseClient,
 Nom de la table : "documents",
 Nom de la requête : "match_documents",
});
// Exemple de structure de documents de vos données
const document1 : Document = {
 pageContenu : « La centrale électrique de la cellule est le
```

```
 métadonnées : { source : "https://example.com" },
} ;
const document2 : Document = {
 pageContent : "Les bâtiments sont en brique",
 métadonnées : { source : "https://example.com" },
} ;
const documents = [document1, document2]
//Incorporer et stocker les données dans la base de données
wait vectorStore.addDocuments(documents, { identifiants :
// Interroge le magasin de vecteurs
const filtre = { source : "https://exemple.com" } ;
const similaritySearchResults = attendre vectorStore
 "biologie",
 2,
 filtrer
);
pour (doc const de similaritéSearchResults) {
 console.log(`* ${doc.pageContent} [${JSON.strin
}
```
*La sortie :*

La centrale électrique de la cellule est la mitochondrie [{

Vous pouvez consulter la logique complète de l'implémentation du magasin de vecteurs Supabase dans le modèle Github LangChain mentionné précédemment.

### **API back-end**

<span id="page-436-0"></span>Comme indiqué dans les chapitres précédents, LangGraph est un framework open source de bas niveau utilisé pour créer des systèmes agentiques complexes alimentés par des LLM. LangGraph permet un contrôle précis du flux et de l'état de votre application, une persistance intégrée et des fonctionnalités avancées d'humain dans la boucle et de mémoire. [Figure](#page-437-0) 9-3 illustre le flux de contrôle de LangGraph.

<span id="page-437-0"></span>![](_page_437_Figure_0.jpeg)

Figure 9-3. Exemple de flux de contrôle de l'API LangGraph
<span id="page-437-1"></span>Pour déployer une application d'IA qui utilise LangGraph, nous utiliserons LangGraph Platform. LangGraph Platform est un service géré permettant de déployer et d'héberger des agents LangGraph à grande échelle.

À mesure que votre cas d’utilisation agent gagne du terrain, une répartition inégale des tâches entre les agents peut surcharger le système, entraînant des temps d’arrêt. La plate-forme LangGraph gère des files d'attente de tâches à mise à l'échelle horizontale, des serveurs et un point de contrôle Postgres robuste pour gérer de nombreux utilisateurs simultanés et stocker efficacement des états et des threads volumineux. Cela garantit une évolutivité tolérante aux pannes.

La plateforme LangGraph est conçue pour prendre en charge des modèles d'interaction du monde réel. En plus des fonctionnalités de streaming et d'intervention humaine, LangGraph Platform permet les éléments suivants :

- Double textos pour gérer les nouvelles entrées utilisateur sur les fils de discussion graphiques en cours
- Travaux d'arrière-plan asynchrones pour les tâches de longue durée
- Tâches Cron pour exécuter des tâches courantes selon un calendrier

LangGraph Platform fournit également une solution intégrée pour collaborer, déployer et surveiller des applications d'IA agentique. Il comprend [LangGraph](https://oreil.ly/2Now-) Studio, un terrain de jeu visuel pour le débogage, l'édition et le test des agents. LangGraph Studio vous permet également de partager votre agent LangGraph avec les membres de l'équipe pour un retour collaboratif et une itération rapide, comme le montre la [Figure](#page-439-0) 9-4.

<span id="page-439-0"></span>![](_page_439_Figure_0.jpeg)

Figure 9-4. Instantané de l'interface utilisateur de LangGraph Studio

De plus, LangGraph Platform simplifie le déploiement agent en permettant les soumissions en un clic.

### **Créez un compte LangSmith**

<span id="page-439-1"></span>LangSmith est une plateforme de développement tout-en-un qui vous permet de déboguer, collaborer, tester et surveiller vos applications LLM.

LangGraph Platform est parfaitement intégré à LangSmith et est accessible depuis l'interface utilisateur de LangSmith.

Pour déployer votre application sur LangGraph Platform, vous devez créer un compte [LangSmith](https://oreil.ly/2WVCn). Une fois connecté au tableau de bord, accédez à la page Paramètres, puis faites défiler jusqu'à la section Clés API et cliquez sur Créer une clé API. Vous devriez voir une interface utilisateur similaire à [Figure](#page-440-0) 9-5.

<span id="page-440-0"></span>

| Créer une clé API | ai été converti |
|-----------------------------------------------------------------|-------------------|
| Descriptif |                   |
| Descriptif |                   |
| Type de clé |                   |
| · Jeton d'accès personnel | Créé à |
| Utilisé pour s'authentifier auprès de l'API en tant qu'individu |                   |
| utilisateur.<br>Clé de service | 01/05/2024, 1:07 : |
| Lié à un principal de service pour l'automatisation et les workflows CI<br>. |                   |
| Créer une clé API |                   |

Figure 9-5. Créer une interface utilisateur de clé API LangSmith

Copiez la valeur de la clé API en tant que LANGCHAIN\_API\_KEY dans votre fichier *.env*.

<span id="page-441-1"></span>Accédez à « Utilisation et facturation » et configurez vos informations de facturation. Cliquez ensuite sur l'onglet « Forfaits et facturation » et sur le bouton « Mettre à niveau vers Plus » pour obtenir des instructions sur la transition vers un plan LangSmith Plus, qui permettra l'utilisation de la plateforme LangGraph. Si vous préférez utiliser un déploiement auto-hébergé gratuit, vous pouvez suivre les [instructions](https://oreil.ly/TBgSQ) ici. Veuillez noter que cette option nécessite une gestion de l'infrastructure, y compris la configuration et la maintenance des bases de données et des instances Redis requises.

## Comprendre l'API de la plateforme LangGraph

Avant de déployer votre application d'IA sur LangGraph Platform, il est important de comprendre le fonctionnement de chaque composant de l'API LangGraph. Ces composants peuvent généralement être divisés en modèles de données et fonctionnalités.

### **Modèles de données**

<span id="page-441-0"></span>L'API LangGraph Platform se compose de quelques modèles de données de base :

- Assistants
- Fils
- Fonctionne
- Emplois Cron

#### **Assistants**
<span id="page-442-0"></span>Un *assistant* est une instance configurée d'un CompiledGraph . Il résume l'architecture cognitive du graphe et contient une configuration et des métadonnées spécifiques à l'instance. Plusieurs assistants peuvent référencer le même graphique mais peuvent contenir des configurations et des métadonnées différentes, ce qui peut différencier le comportement des assistants. Un assistant (c'est-à-dire le graphique) est invoqué dans le cadre d'une exécution.

L'API LangGraph Platform fournit plusieurs points de terminaison pour la création et la gestion d'assistants.

#### **Discussions**

<span id="page-442-1"></span>Un *thread* contient l'état accumulé d'un groupe d'exécutions. Si une exécution est exécutée sur un thread, alors l'état du graphique sous-jacent de l'assistant sera conservé dans le thread. L'état actuel et historique d'un thread peut être récupéré. Pour conserver l’état, un thread doit être créé avant d’exécuter une exécution. L'état d'un thread à un moment donné est appelé un *point de contrôle*.

L'API LangGraph Platform fournit plusieurs points de terminaison pour la création et la gestion des threads et de l'état des threads.

#### **Fonctionne**

<span id="page-443-2"></span>Un *run* est une invocation d'un assistant. Chaque exécution peut avoir ses propres entrées, configurations et métadonnées, ce qui peut affecter l'exécution et la sortie du graphique sous-jacent. Une exécution peut éventuellement être exécutée sur un thread.

L'API LangGraph Platform fournit plusieurs points de terminaison pour la création et la gestion des exécutions.

### **Tâches Cron**

<span id="page-443-0"></span>LangGraph Platform prend en charge les *tâches cron*, qui permettent d'exécuter des graphiques selon un calendrier défini par l'utilisateur. L'utilisateur spécifie un planning, un assistant et une entrée. Ensuite, LangGraph Platform crée un nouveau thread avec l'assistant spécifié et envoie l'entrée spécifiée à ce thread.

### **Caractéristiques**

<span id="page-443-1"></span>L'API LangGraph Platform offre également plusieurs fonctionnalités pour prendre en charge les architectures d'agent complexes, notamment les suivantes :

- Diffusion
- Humain dans la boucle
- Doubles SMS
- Courses apatrides
- Webhooks

#### **Diffusion**

<span id="page-444-0"></span>Le streaming est essentiel pour garantir que les applications LLM répondent aux besoins des utilisateurs finaux. Lors de la création d'une exécution de streaming, le mode de streaming détermine quelles données sont renvoyées au client API. L'API LangGraph Platform prend en charge cinq modes de streaming :

#### *Valeurs*

Diffusez l’état complet du graphique après l’exécution de chaque super-étape.

#### *Messages*

Diffusez des messages complets (à la fin de l'exécution du nœud) ainsi que des jetons pour tous les messages générés à l'intérieur d'un nœud. Ce mode est principalement destiné à alimenter les applications de chat. Ceci n'est une option que si votre graphique contient une clé de messages.

#### *Mises à jour*

Mises à jour en continu de l'état du graphique après l'exécution de chaque nœud.

#### *Événements*

Diffusez tous les événements (y compris l'état du graphique) qui se produisent pendant l'exécution du graphique. Cela peut être utilisé pour effectuer un streaming jeton par jeton pour les LLM.

#### *Débogage*

Diffusez les événements de débogage tout au long de l’exécution du graphique.

#### **L'humain dans la boucle**

<span id="page-445-0"></span>S'il s'exécute de manière autonome, un agent complexe peut entreprendre des actions involontaires, conduisant à des résultats d'application catastrophiques. Pour éviter cela, une intervention humaine est recommandée, notamment aux points de contrôle où la logique applicative implique l’appel de certains outils ou l’accès à des documents spécifiques. LangGraph Platform vous permet d'insérer ce comportement humain dans la boucle pour garantir que votre graphique n'entraîne pas de résultats indésirables.

### **Doubles SMS**

<span id="page-446-0"></span>L'exécution du graphique peut prendre plus de temps que prévu et les utilisateurs peuvent souvent envoyer un message puis, avant la fin de l'exécution du graphique, envoyer un deuxième message. C'est ce qu'on appelle le *double texto*. Par exemple, un utilisateur peut remarquer une faute de frappe dans sa demande d'origine, modifier l'invite et la renvoyer. Dans de tels scénarios, il est important d’éviter que vos graphiques se comportent de manière inattendue et de garantir une expérience utilisateur fluide. LangGraph Platform propose quatre solutions différentes pour gérer les doubles textos :

#### *Rejeter*

Cela rejette toute exécution de suivi et n'autorise pas l'envoi de doubles SMS.

#### *Mettre en file d'attente*

Cette option continue la première exécution jusqu'à ce qu'elle termine l'exécution entière, puis envoie la nouvelle entrée en tant qu'exécution distincte.

#### *Interruption*

Cette option interrompt l'exécution en cours mais enregistre tout le travail effectué jusque-là. Il insère ensuite l'entrée de l'utilisateur et continue à partir de là. Si vous activez cette option, votre graphique devrait être capable de gérer les cas extrêmes étranges qui peuvent survenir.

#### *Retour en arrière*
Cette option annule tout le travail effectué jusque-là. Il envoie ensuite l'entrée de l'utilisateur, comme si elle suivait simplement l'entrée d'exécution d'origine.

#### **Fonctions apatrides**

<span id="page-447-0"></span>Toutes les exécutions utilisent le point de contrôle intégré pour stocker les points de contrôle des exécutions. Cependant, il peut souvent être utile de simplement lancer une exécution sans se soucier de créer explicitement un fil de discussion et de conserver ces points de contrôle. Les exécutions *Stateless* vous permettent de le faire en exposant un point de terminaison qui effectue les opérations suivantes :

- Prend en compte les entrées de l'utilisateur
- Crée un fil de discussion
- Exécute l'agent, mais ignore toutes les étapes de contrôle
- Nettoie le fil par la suite

Les exécutions sans état sont réessayées tout en gardant la mémoire intacte. Cependant, dans le cas d'exécutions en arrière-plan sans état, si le travailleur chargé de la tâche décède à mi-chemin, l'exécution entière sera retentée à partir de zéro.

### **Webhooks**

<span id="page-448-2"></span>La plate-forme LangGraph prend également en charge les *webhooks* de complétion. Une URL de webhook est fournie, qui avertit votre application chaque fois qu'une exécution est terminée.

# <span id="page-448-1"></span>Déploiement de votre application d'IA sur la plateforme LangGraph

À ce stade, vous avez créé des comptes pour les services recommandés, rempli votre fichier *.env* avec les valeurs de toutes les variables d'environnement nécessaires et complété la logique de base de votre application d'IA. Ensuite, nous prendrons les mesures nécessaires pour déployer efficacement votre application.

### **Créer une configuration d'API LangGraph**

<span id="page-448-0"></span>Avant le déploiement, vous devez configurer votre application avec un fichier de configuration de l'API LangGraph appelé *[langgraph.json](https://oreil.ly/aVDhd)*. Voici un exemple de ce à quoi ressemble le fichier dans un dépôt Python :

*Python*

```
 "dependencies": ["./my_agent"],
 "graphs": {
 "agent": "./my_agent/agent.py:graph"
 },
 "env": ".env"
}
```
Et voici un exemple de structure de référentiel :

![](_page_449_Figure_2.jpeg)

Notez que le fichier *langgraph.json* est placé au même niveau ou à un niveau supérieur aux fichiers contenant les graphiques compilés et les dépendances associées.

De plus, les dépendances sont spécifiées dans un fichier *requirements.txt*. Mais ils peuvent également être spécifiés dans les fichiers *pyproject.toml*, *setup.py* ou *package.json*.

Voici ce que signifie chacune des propriétés :

*Dépendances*

Tableau de dépendances pour le serveur API LangGraph Platform

*Graphiques*

Mappage de l'ID du graphique au chemin où le graphique compilé ou une fonction qui crée un graphique est défini

*Env*

Chemin d'accès à votre fichier *.env* ou un mappage de la variable d'environnement à sa valeur (vous pouvez en savoir plus sur les configurations du fichier langgraph.json [ici](https://oreil.ly/bPA0W))

### **Testez votre application LangGraph localement**

<span id="page-450-0"></span>Tester votre application localement garantit qu'il n'y a pas d'erreurs ou de conflits de dépendances avant le déploiement. Pour ce faire, nous utiliserons la CLI LangGraph, qui inclut des commandes pour exécuter un serveur de développement local avec des capacités de rechargement à chaud et de débogage.

Pour Python, installez le package Python langgraph-cli (remarque : cela nécessite Python 3.11 ou supérieur) :

pip install -U "langgraph-cli[inmem]"

Ou pour JavaScript, installez le package comme suit :

npm je @langchain/langgraph-cli

Une fois la CLI installée, exécutez la commande suivante pour démarrer l'API :

développeur de langage

Cela démarrera le serveur API LangGraph localement. Si cela fonctionne correctement, vous devriez voir quelque chose comme ceci :

```
Ready!
API: http://localhost:2024
Docs: http://localhost:2024/docs
```
La référence de l'API LangGraph Platform est disponible avec chaque déploiement sur le chemin URL */docs* (*http://localhost:2024/docs*).

Le moyen le plus simple d'interagir avec votre serveur API local consiste à utiliser l'interface utilisateur de LangGraph Studio lancée automatiquement. Vous pouvez également interagir avec le serveur API local à l'aide de cURL, comme le montre cet exemple :

```
curl --request POST \
 --url http://localhost:8123/runs/stream \
 --header 'Content-Type: application/json' \
 --data '{
 "assistant_id": "agent",
 "input": {
 "messages": [
 {
 "role": "user",
 "content": "How are you?"
 }
 ]
 },
 "metadata": {},
 "config": {
 "configurable": {}
 },
 "multitask_strategy": "reject",
```

```
 "stream_mode": [
 "values"
 ]
}'
```
Si vous recevez une réponse valide, votre candidature fonctionne bien. Ensuite, nous pouvons interagir avec le serveur à l'aide du SDK LangGraph.

Voici un exemple d'initialisation du client SDK et d'appel du graphique :

*Python*

```
à partir de langgraph_sdk importer get_client
# ne transmet l'argument url à get_client() que si y
# lors de l'appel de Langgraph
client = get_client()
# Utilisation du graphe déployé avec le nom "agent"
assistant_id = "agent"
thread = attendre client.threads.create()
input = {"messages": [{"role": "utilisateur", "contenu"
asynchrone pour le morceau dans client.runs.stream(
```

```
 fil["thread_id"],
 assistant_id,
 entrée = entrée,
 stream_mode="mises à jour",
) :
 print(f"Réception d'un nouvel événement de type : {chunk.e
 imprimer (morceau.données)
 imprimer("\n\n")
```
*JavaScript*

{

```
importer {Client} depuis "@langchain/langgraph-sdk"
// ne définit l'apiUrl que si vous avez modifié la valeur par défaut
const client = nouveau Client();
// Utilisation du graphe déployé avec le nom "agent"
const assistantId = "agent" ;
const thread = attendre client.threads.create();
entrée const = {
 messages : [{ "role": "user", "content": "qu'est-ce que
}
const streamResponse = client.runs.stream(
 fil["thread_id"],
 identifiant d'assistant,
```

```
 {
 entrée: entrée,
 streamMode : "mises à jour",
 }
);
pour wait (morceau const de streamResponse) {
 console.log(`Receiving new event of type: ${chu
 console.log(chunk.data);
 console.log("\n\n");
}
```
<span id="page-455-1"></span>Si votre application LangGraph fonctionne correctement, vous devriez voir la sortie de votre graphique affichée dans la console.

### **Déployer à partir de l'interface utilisateur de LangSmith**

<span id="page-455-0"></span>À ce stade, vous devriez avoir terminé toutes les étapes préalables et votre API LangGraph devrait fonctionner localement. Votre prochaine étape consiste à accéder au panneau de votre tableau de bord LangSmith et à cliquer sur l'onglet Déploiements. Vous devriez voir une interface utilisateur similaire à [Figure](#page-456-0) 9-6.

<span id="page-456-0"></span>![](_page_456_Picture_0.jpeg)

Figure 9-6. Page de l'interface utilisateur de déploiement de la plateforme LangGraph

Ensuite, cliquez sur le bouton Nouveau déploiement dans le coin supérieur droit de la page.

#### **REMARQUE**

Si vous ne voyez pas de page avec le bouton Nouveau déploiement, il est probable que vous n'ayez pas encore mis à niveau vers un plan LangSmith Plus conformément aux instructions du paramètre « Utilisation et facturation ».

Vous devriez maintenant voir une page de trois champs de formulaire à remplir.

#### **Détails du déploiement**

- 1. Sélectionnez « Importer avec GitHub » et suivez le flux de travail GitHub OAuth pour installer et autoriser l'application GitHub hébergée de LangChain à accéder aux référentiels sélectionnés. Une fois l'installation terminée, revenez au panneau Créer un nouveau déploiement et sélectionnez le référentiel GitHub à déployer dans le menu déroulant.
- 2. Spécifiez un nom pour le déploiement et le chemin complet vers le fichier de configuration de l'API LangGraph, y compris le nom du fichier. Par exemple, si le fichier *langgraph.json* se trouve à la racine du référentiel, spécifiez simplement *langgraph.json*.
- 3. Spécifiez la référence git souhaitée (nom de branche) de votre référentiel à déployer.

#### **Type de développement**

Sélectionnez Production dans la liste déroulante. Cela permettra un déploiement de production pouvant traiter jusqu'à 500 requêtes/seconde et doté d'un stockage hautement disponible et de sauvegardes automatiques.

#### **Variables d'environnement**

<span id="page-457-0"></span>Fournissez ici les propriétés et les valeurs dans votre *.env*. Pour les valeurs sensibles, comme votre OPENAI\_API\_KEY , assurez-vous de cocher la case Secret avant de saisir la valeur.

Une fois que vous avez rempli les champs, cliquez sur le bouton pour soumettre le déploiement et attendez quelques secondes que la construction soit terminée. Vous devriez voir une nouvelle révision associée au déploiement.

Étant donné que LangGraph Platform est intégré à LangSmith, vous pouvez obtenir une visibilité plus approfondie sur votre application et suivre et surveiller également l'utilisation, les erreurs, les performances et les coûts de production. [Figure](#page-458-0) 9-7 montre un graphique récapitulatif visuel du nombre de traces montrant les traces réussies, en attente et d'erreur sur une période donnée. Vous pouvez également afficher toutes les informations de surveillance de votre serveur en cliquant sur le bouton "Tous les graphiques".

<span id="page-458-0"></span>![](_page_458_Figure_2.jpeg)

Figure 9-7. Révisions de déploiement et nombre de traces sur le tableau de bord

Pour afficher les journaux de build et de déploiement, sélectionnez la révision souhaitée dans l'onglet Révisions, puis choisissez l'onglet Déployer pour afficher l'historique complet des journaux de déploiement. Vous pouvez également ajuster la plage de date et d’heure.

Pour créer un nouveau déploiement, cliquez sur le bouton Nouvelle révision dans la barre de navigation. Remplissez les champs nécessaires, y compris le chemin du fichier de configuration de l'API LangGraph, la référence git et les variables d'environnement, comme indiqué précédemment.

<span id="page-459-0"></span>Enfin, vous pouvez accéder à la documentation de l'API en cliquant sur le lien Documents de l'API, qui devrait afficher une page similaire à l'interface utilisateur présentée dans la [Figure](#page-460-0) 9-8.

<span id="page-460-0"></span>
| fourmi | OBTENIR |                     |      |                                                                                               |       |          |        |   |
|------------------|-------|-----------|------|----------------------------------------------------------------------------------------------|-------|----------|--------|---|
| instantané | DEL | SERVEUR |      |                                                                                               |       |          |        |   |
| permanent | PATCH |                     |      | https://chat-langchain-langgraph-ci-d4a7041e91b655bab3bbd4fe1472e0cd.default.us.langgraph.app |       |          |        |   |
| graphique de fourmi | HEC | CLÉ API (X-API-KEY) |      |                                                                                               |       |          |        |   |
| Sous-graphiques de fourmis | HEC | Jeton |      |                                                                                               |       |          |        | @ |
| Sous-graphiques de fourmi par | OBTENIR |                     |      |                                                                                               |       |          |        |   |
| 0 |       | BIBLIOTHÈQUES CLIENTÈLES |      |                                                                                               |       |          |        |   |
| Schémas de fourmis | OBTENIR | >_ Coquille | Rubis | @ Node.js | @PHP | @Python | - Plus |   |
| Versions fourmis | POSTER | Coquille cURL |      |                                                                                               |       |          |        |   |
| Version Assistante | POSTER |                     |      |                                                                                               |       |          |        |   |
|                   |       |                     |      |                                                                                               |       |          |        |   |
| 3 |       |                     |      |                                                                                               |       |          |        |   |
| Fonctionne |       |                     |      |                                                                                               |       |          |        |   |
| entreprise uniquement) |       | Assistantes |      |                                                                                               |       |          |        |   |

|     | POSTE /assistants |
|-----|------------------------------------------------------|
|     | POST /assistants/recherche |
| OBTENIR | /assistants/{assistant_id} |
|     | SUPPRIMER /assistants/{assistant_id} |
|     | PATCH /assistants/{assistant_id} |
|     | GET /assistants/{assistant_id}/graph |
|     | GET /assistants/{assistant_id}/subgraphs |
|     | GET /assistants/{assistant_id}/subgraphs/{namespace} |
|     | GET /assistants/{assistant_id}/schemas |
|     | POST /assistants/{assistant_id}/versions |
|     | POST /assistants/{assistant_id}/latest |
|     |                                                      |

<span id="page-460-1"></span>Figure 9-8. Documentation de l'API LangGraph

### **Lancez LangGraph Studio**

LangGraph Studio fournit un IDE d'agent spécialisé pour visualiser, interagir avec et déboguer des applications agentiques complexes. Il permet aux développeurs de modifier le résultat d'un agent (ou la logique sous-jacente à un nœud spécifique) à mi-chemin de la trajectoire de l'agent. Cela crée un processus itératif en vous permettant d'interagir avec l'état et de le manipuler à ce moment-là.

Une fois que vous avez déployé votre application d'IA, cliquez sur le bouton LangGraph Studio dans le coin supérieur droit du tableau de bord de déploiement, comme vous pouvez le voir dans la [Figure](#page-461-0) 9-9.

<span id="page-461-0"></span>
| 27 ht-prix-dependable=85 |                  |            |                                                                                                                                         | + Nouvelle révision |              |
|----------------------------------------------|--------|------------|----------------------------------------------------------------------------------------------------------------------------------------|----------------|--------------|
|                                              |                  |            | Lisez notre documentation Languagh Cloud et démarrez rapidement le combbridge uniquement, la décision est autorisée par langue et en augmentation quasiment. |                |              |
| PROJET DE TRAÇAGE<br>28 ht-dependable-prize-85 |                  | DÉPÔT | API UN<br>O mayoearlanggraph warmpe O https://1r/decombing/2015072030322ed.default.us.inggrach.pp 0 /occ 19/09/2024,114110 | UN DOCUMENT | DERNIÈRE MISE À JOUR |
| TYPE DE DÉPLOIEMENT<br>Production | PARTAGEABLE<br>Oui |            |                                                                                                                                         |                |              |

Figure 9-9. Interface utilisateur de déploiement LangGraph

Après avoir cliqué sur le bouton, vous devriez voir l'interface utilisateur de LangGraph Studio (par exemple, voir [Figure](#page-462-0) 9-10).

<span id="page-462-0"></span>![](_page_462_Figure_0.jpeg)

Figure 9-10. Interface utilisateur de LangGraph Studio

Pour appeler un graphique et démarrer une nouvelle exécution, procédez comme suit :

- 1. Sélectionnez un graphique dans le menu déroulant dans le coin supérieur gauche du volet gauche. Le graphique de la [Figure](#page-462-0) 9-10 est appelé *agent*.
- 2. Dans la section Entrée, cliquez sur l'icône "+ Message" et saisissez un message *humain*, mais l'entrée variera en fonction des définitions de l'état de votre application.
- 3. Cliquez sur Soumettre pour appeler le graphique sélectionné.
- 4. Affichez le résultat de l'invocation dans le volet de droite.

La sortie de votre graphique invoqué devrait ressembler à [Figure](#page-463-0) 9-11.

<span id="page-463-0"></span>![](_page_463_Figure_3.jpeg)

Figure 9-11. Sortie d'appel de LangGraph Studio

En plus de l'invocation, LangGraph Studio vous permet de modifier les configurations d'exécution, de créer et de modifier des threads, d'interrompre vos graphiques, de modifier le code du graphique et de permettre une intervention humaine dans la boucle. Vous pouvez lire le [guide](https://oreil.ly/xUU37) complet pour en savoir plus.

#### **REMARQUE**

LangGraph Studio est également disponible sous forme d'application de bureau (pour Apple Silicon), qui vous permet de tester votre application d'IA localement.

Si vous avez suivi le guide d'installation du modèle GitHub et déployé avec succès votre application d'IA, elle est désormais disponible pour une utilisation en production. Mais avant de partager avec des utilisateurs externes ou d'utiliser l'API backend dans des applications existantes, il est important d'être conscient des principales considérations de sécurité.

## <span id="page-464-0"></span>Sécurité

<span id="page-464-1"></span>Bien que les applications d'IA soient puissantes, elles sont vulnérables à plusieurs risques de sécurité pouvant entraîner une corruption ou une perte de données, un accès non autorisé à des informations confidentielles et une performance compromise. Ces risques peuvent entraîner des conséquences juridiques, réputationnelles et financières défavorables.

<span id="page-464-2"></span>Pour atténuer ces risques, il est recommandé de suivre les bonnes pratiques générales en matière de sécurité des applications, notamment les suivantes :

#### *Limiter les autorisations*

<span id="page-464-3"></span>Autorisations de portée spécifiques aux besoins de l'application. L'octroi d'autorisations larges ou excessives peut introduire d'importantes vulnérabilités de sécurité. Pour éviter de telles vulnérabilités, envisagez d'utiliser des informations d'identification en lecture seule, d'interdire l'accès aux ressources sensibles et d'utiliser des techniques de sandboxing (telles que l'exécution dans un conteneur).

#### *Anticiper les abus potentiels*

<span id="page-465-1"></span>Partez toujours du principe que tout accès au système ou informations d'identification peuvent être utilisés de la manière autorisée par les autorisations qui leur sont attribuées. Par exemple, si une paire d'informations d'identification de base de données permet de supprimer des données, il est plus sûr de supposer que tout LLM capable d'utiliser ces informations d'identification peut en fait supprimer des données.

#### *Défense en profondeur*

<span id="page-465-2"></span><span id="page-465-0"></span>Il est souvent préférable de combiner plusieurs approches de sécurité à plusieurs niveaux plutôt que de s'appuyer sur une seule couche de défense pour garantir la sécurité. Par exemple, utilisez à la fois les autorisations en lecture seule et le sandboxing pour garantir que les LLM ne peuvent accéder qu'aux données qui leur sont explicitement destinées.
Voici trois exemples de scénarios mettant en œuvre ces stratégies d’atténuation :

*Accès aux fichiers*

<span id="page-466-3"></span><span id="page-466-2"></span>Un utilisateur peut demander à un agent ayant accès au système de fichiers de supprimer les fichiers qui ne doivent pas être supprimés ou de lire le contenu des fichiers contenant des informations sensibles. Pour atténuer ce risque, limitez l'agent à utiliser uniquement un répertoire spécifique et autorisez-le uniquement à lire ou à écrire des fichiers dont la lecture ou l'écriture est sûre. Envisagez de mettre davantage l'agent en sandbox en l'exécutant dans un conteneur.

#### *Accès API*

<span id="page-466-0"></span>Un utilisateur peut demander à un agent disposant d'un accès en écriture à une API externe d'écrire des données malveillantes dans l'API ou de supprimer des données de cette API. Pour atténuer ces problèmes, attribuez à l'agent des clés API en lecture seule ou limitez-le à l'utilisation de points de terminaison déjà résistants à une telle utilisation abusive.

#### *Accès à la base de données*

<span id="page-466-1"></span>Un utilisateur peut demander à un agent ayant accès à une base de données de supprimer une table ou de muter le schéma. Pour atténuer ce problème, limitez les informations d'identification aux seules tables auxquelles l'agent doit accéder et envisagez de délivrer des informations d'identification en lecture seule.

En plus des mesures de sécurité précédentes, vous pouvez prendre des mesures supplémentaires pour limiter les abus de votre application d'IA. En raison de la dépendance des fournisseurs d'API LLM externes (tels qu'OpenAI), il existe un coût direct associé à l'exécution de votre

demande. Pour éviter les abus de votre API et les coûts exponentiels, vous pouvez mettre en œuvre les éléments suivants :

#### *Vérification de la création du compte*

<span id="page-467-0"></span>Cela inclut généralement une forme de connexion d'authentification, telle que la vérification d'un e-mail ou d'un numéro de téléphone.

#### *Limitation de débit*

<span id="page-467-2"></span>Implémentez un mécanisme de limitation de débit dans le middleware de l'application pour empêcher les utilisateurs de faire trop de requêtes sur une courte période de temps. Cela devrait vérifier le nombre de demandes qu'un utilisateur a faites au cours des X dernières minutes et "timeout" ou "bannir" l'utilisateur si l'abus est grave.

#### *Mettre en place des garde-fous d'injection rapide*

<span id="page-467-1"></span>*L'injection d'invite* se produit lorsqu'un utilisateur malveillant injecte une invite pour tenter de tromper le LLM pour qu'il agisse de manière involontaire. Cela inclut généralement l’extraction de données confidentielles ou la génération de résultats sans rapport. Pour atténuer ce problème, vous devez vous assurer que le LLM dispose d'une portée d'autorisation appropriée et que les invites de l'application sont spécifiques et strictes par rapport aux résultats souhaités.

## Résumé

Tout au long de ce chapitre, vous avez appris les meilleures pratiques pour déployer votre application d'IA et permettre aux utilisateurs d'interagir avec elle. Nous avons exploré les services recommandés pour gérer divers composants clés de l'application en production, notamment le LLM, le magasin de vecteurs et l'API backend.

Nous avons également discuté de l'utilisation de LangGraph Platform en tant que service géré pour déployer et héberger des agents LangGraph à grande échelle en conjonction avec LangGraph Studio, pour visualiser, interagir avec et déboguer votre application.

Enfin, nous avons brièvement exploré diverses bonnes pratiques de sécurité pour atténuer les risques de violation de données souvent associés aux applications d'IA.

Dans le [Chapitre](#page-469-0) 10, vous apprendrez comment évaluer, surveiller, comparer et améliorer efficacement les performances de votre application d'IA.

# <span id="page-469-0"></span>Chapitre 10. Tests : évaluation, suivi et amélioration continue

Dans le [Chapitre](#page-424-0) 9, vous avez appris à déployer votre application d'IA en production et à utiliser LangGraph Platform pour héberger et déboguer votre application.

<span id="page-469-1"></span>Bien que votre application puisse répondre aux entrées de l'utilisateur et exécuter des tâches complexes, son LLM sous-jacent est non déterministe et sujet aux hallucinations. Comme indiqué dans les chapitres précédents, les LLM peuvent générer des sorties inexactes et obsolètes pour diverses raisons, notamment l'invite, le format de la saisie de l'utilisateur et le contexte récupéré. De plus, les résultats LLM préjudiciables ou trompeurs peuvent nuire considérablement à la marque d'une entreprise et à la fidélité de ses clients.

Pour lutter contre cette tendance aux hallucinations, vous devez créer un système efficace pour tester, évaluer, surveiller et améliorer continuellement les performances de vos applications LLM. Ce processus de test robuste vous permettra de déboguer et de résoudre rapidement les problèmes liés à l'IA avant et après la mise en production de votre application.

Dans ce chapitre, vous apprendrez à créer un système de tests itératifs à travers les étapes clés du cycle de vie de développement d'applications LLM et à maintenir des performances élevées de votre application.

# Techniques de test tout au long du cycle de développement d'applications LLM
<span id="page-470-0"></span>Avant de construire le système de test, examinons brièvement comment les tests peuvent être appliqués aux trois étapes clés du développement d'applications LLM :

#### *Conception*

Dans cette étape, les tests LLM sont appliqués directement à votre candidature. Ces tests peuvent être des assertions exécutées au moment de l'exécution qui renvoient les échecs au LLM pour une autocorrection. Le but des tests à ce stade est la gestion des erreurs au sein de votre application avant qu'elles n'affectent les utilisateurs.

#### *Préproduction*

Dans cette étape, les tests sont exécutés juste avant le déploiement en production. Le but des tests à ce stade est de détecter et de corriger toute régression avant que l'application ne soit proposée aux utilisateurs réels.

#### *Production*

<span id="page-471-1"></span>Dans cette étape, des tests sont exécutés pendant que votre application est en production pour aider à surveiller et détecter les erreurs affectant les utilisateurs réels. L’objectif est d’identifier les problèmes et de les réintégrer dans les phases de conception ou de pré-production.

La combinaison des tests à travers ces étapes crée un cycle d'amélioration continue dans lequel ces étapes sont répétées : conception, test, déploiement, surveillance, correction et refonte. Voir [Figure](#page-471-0) 10-1.

<span id="page-471-0"></span>![](_page_471_Figure_3.jpeg)

Figure 10-1. Les trois étapes clés du cycle de développement d'une application LLM

Essentiellement, ce cycle vous aide à identifier et à résoudre les problèmes de production de manière efficace et rapide.

Examinons plus en détail les techniques de test à chacune de ces étapes.

## L'étape de conception : RAG autocorrectif

<span id="page-472-0"></span>Comme indiqué précédemment, votre application peut intégrer une gestion des erreurs au moment de l'exécution qui transmet les erreurs au LLM pour une autocorrection. Explorons un cas d'utilisation de RAG utilisant LangGraph comme cadre pour orchestrer la gestion des erreurs.

<span id="page-472-1"></span>Les applications d'IA de base basées sur RAG sont sujettes aux hallucinations en raison d'une récupération inexacte ou incomplète du contexte pertinent pour générer des résultats. Mais vous pouvez utiliser un LLM pour évaluer la pertinence de la récupération et résoudre les problèmes d'hallucinations.

<span id="page-472-2"></span>LangGraph vous permet d'implémenter efficacement le flux de contrôle de ce processus, comme indiqué dans la [Figure](#page-473-0) 10-2.

<span id="page-473-0"></span>![](_page_473_Figure_0.jpeg)

Figure 10-2. Flux de contrôle RAG autocorrectif

Les étapes du flux de contrôle sont les suivantes :

- 1. Lors de l'étape de routage, chaque question est acheminée vers la méthode de récupération appropriée, c'est-à-dire le magasin de vecteurs et la recherche sur le Web.
- 2. Si, par exemple, la question est acheminée vers un magasin de vecteurs pour être récupérée, le LLM dans le flux de contrôle récupérera et classera les documents en fonction de leur pertinence.
- 3. Si le document est pertinent, le LLM procède à la génération d'une réponse.
- 4. Le LLM vérifiera la réponse pour les hallucinations et ne procédera à l'affichage de la réponse à l'utilisateur que si le résultat est précis et pertinent.

5. En solution de secours, si le document récupéré n'est pas pertinent ou si la réponse générée ne répond pas à la question de l'utilisateur, le flux utilise la recherche sur le Web pour récupérer les informations pertinentes comme contexte.

<span id="page-474-0"></span>Ce processus permet à votre application de générer de manière itérative des réponses, d'auto-corriger les erreurs et les hallucinations, et d'améliorer la qualité des résultats.

Passons en revue un exemple d'implémentation de code de ce flux de contrôle. Tout d’abord, téléchargez les packages requis et initialisez les clés API pertinentes. Pour ces exemples, vous devrez définir vos clés API OpenAI et LangSmith comme variables d'environnement.

Tout d’abord, nous allons créer un index de trois articles de blog :

*Python*

depuis langchain.text\_splitter importer RecursiveChar depuis langchain\_community.document\_loaders importer depuis langchain\_community.vectorstores importer InMe depuis langchain\_openai importer OpenAIEmbeddings depuis langchain\_core.prompts importer ChatPromptTemp depuis pydantic importer BaseModel, champ depuis langchain\_openai importer ChatOpenAI

```
 
# --- Créer un index des documents ---

URL = [
 "https://blog.langchain.dev/top-5-langgraph-a
 "https://blog.langchain.dev/langchain-state-o
 " https://blog.langchain.dev/introducing-ambie
]

docs = [WebBaseLoader(url).load() pour l'url dans les URL
docs_list = [élément pour la sous-liste dans la documentation pour l'élément dans

text_splitter = RecursiveCharacterTextSplitter.fr
 chunk_size=250, chunk_overlap=0
)
doc_splits = text_splitter.split_documents(docs_l

# Ajouter à vectorDB
vectorstore = InMemoryVectorStore.from_documents(
 documents=doc_splits,
 intégration=OpenAIEmbeddings(),
)
récupérateur = vectorstore.as_retriever()

# Récupérer les documents pertinents
résultats = retriever.invoke(
 "Quels sont les 2 agents LangGraph utilisés dans la production ?
```

```
print("Résultats : \n"
                   , résultats)
```
#### *JavaScript*

```
importer { RecursiveCharacterTextSplitter } depuis '@
importer {
 CheerioWebBaseLoader
} depuis "@langchain/community/document_loaders/web
importer {
 InMemoryVectorStore
} de '@langchain/community/vectorstores/in_memo
importer { OpenAIEmbeddings } depuis '@langchain/open
importer { ChatPromptTemplate } depuis '@langchain/co
importer { z } depuis 'zod' ;
importer { ChatOpenAI } depuis '@langchain/openai' ;

URL const = [
 'https://blog.langchain.dev/top-5-langgraph-age
 'https://blog.langchain.dev/langchain-state-of-
 'https://blog.langchain.dev/introducing-ambient
];

// Charger des documents à partir d'URL
const loadDocs = async (urls) => {
 const docs = [];
  pour (const url des urls) {
```

```
 pour (const url des urls) {
 const chargeur = nouveau CheerioWebBaseLoader (url);
 constloadedDocs = waitloader.load();
 docs.push(...loadedDocs);
 }
 retourner les documents ;
} ;

const docsList = wait loadDocs(urls);

// Initialise le séparateur de texte
const textSplitter = nouveau RecursiveCharacterTextSp
 taille du morceau : 250,
 chunkOverlap : 0,
});

// Divise les documents en morceaux plus petits
const docSplits = textSplitter.splitDocuments(doc

// Ajouter à la base de données vectorielles
const vectorstore = attendre InMemoryVectorStore.fro
 docSplits,
 nouveau OpenAIEmbeddings()
);

// L'objet `retriever` peut désormais être utilisé pour que
const retriever = vectorstore.asRetriever();

const question = 'Qu'utilisent les 2 agents LangGraph ?
```

```
const question = Qu'utilisent les 2 agents LangGraph

const docs = retriever.invoke(question);

console.log('Documents récupérés : \n', docs[0].pa
```
As discussed previously, the LLM will grade the relevancy of the retrieved documents from the index. We can construct this instruction in a system prompt:

#### *Python*

```
### Niveleuse de récupération
à partir de langchain_core.prompts, importez ChatPromptTemp
à partir de langchain_core.pydantic_v1, importez BaseModel,
depuis langchain_openai importer ChatOpenAI
# Modèle de données
classe GradeDocuments (BaseModel) :
 """Score binaire pour le contrôle de pertinence lors de la récupération
 score_binaire : str = Champ (
 description="Les documents sont pertinents pour le
 )
```

```
# LLM avec appel de fonction
llm = ChatOpenAI(model="gpt-3.5-turbo"
                                    , température
structuré_llm_grader = llm.with_structured_outpu
# Invite
system = """Vous êtes un évaluateur évaluant la pertinence 
 question de l'utilisateur. 
 Si le document contient des mots-clés ou un sémant
 question, notez-la comme pertinente. 
 Donnez un score binaire « oui » ou « non » pour indiquer
 pertinent par rapport à la question."""
grade_prompt = ChatPromptTemplate.from_messages(
 [
 ("système"
                , système),
 ("humain"
               ,
                 """Document récupéré : \n\n {faire
 {question}"""),
 ]
)
récupération_grader = grade_prompt | structuré_llm_
question = "mémoire de l'agent"
docs = retriever.get_relevant_documents(question)
doc_txt = docs[0].page_content # à titre d'exemple
retrieval_grader.invoke({"question": question,
                                             "d
```
#### *JavaScript*

```
importer { ChatPromptTemplate } depuis "@langchain/co
importer { z } depuis "zod" ;
importer { ChatOpenAI } depuis "@langchain/openai" ;
// Définir le schéma à l'aide de Zod
const GradeDocumentsSchema = z.object({
 score_binaire : z.string().describe(`Documents ar
 'yes' or 'no'`),
});
```
// Initialize LLM with structured output using Zo const llm = new ChatOpenAI({ model: "gpt-3.5-turb const structuredLLMGrader = llm.withStructuredOut

```
// Modèle de système et d'invite
const systemMessage = `You are a grader assessing
 document to a user question. 
If the document contains keyword(s) or semantic m
 question, grade it as relevant.
Give a binary score 'yes' or 'no' to indicate whe
 to the question.`;
const gradePrompt = ChatPromptTemplate.fromMessag
 { rôle : "système", contenu : systemMessage },
 {
```

```
 rôle : "humain",
 content : "Document récupéré : \n\n {document}
 Question de l'utilisateur : {question}",
 },
]);
// Combine l'invite avec la sortie structurée
const retrievalGrader = gradePrompt.pipe (structure
const question = "mémoire de l'agent" ;
const docs = wait retriever.getRelevantDocuments
attendre retrievalGrader.invoke({
 question,
 document : docs[1].pageContent,
});
```
*The output:*

```
binaire_score='oui'
```
Notez l'utilisation de Pydantic/Zod pour aider à modéliser la sortie de décision binaire dans un format qui peut être utilisé pour décider par programme vers quel nœud du flux de contrôle se déplacer.
<span id="page-482-0"></span>Dans LangSmith, vous pouvez voir une trace du flux logique à travers les nœuds discutés précédemment (voir [Figure](#page-483-0) 10-3).

<span id="page-483-0"></span>![](_page_483_Figure_0.jpeg)

Figure 10-3. Résultats des traces LangSmith

Testons pour voir ce qui se passe lorsque les documents récupérés dans l'index ne peuvent pas répondre à la question d'entrée.

Tout d’abord, utilisez LangGraph pour faciliter la construction, l’exécution et le débogage du flux de contrôle complet. Consultez la définition complète du graphique dans le [dépôt GitHub.](https://oreil.ly/v63Vr) du livre. Notez que nous avons ajouté un nœud transform\_query pour aider à réécrire la requête d'entrée dans un format que la recherche sur le Web peut utiliser pour récupérer des résultats de meilleure qualité.

Dans une dernière étape, nous configurons notre outil de recherche Web et exécutons le graphique en utilisant la question hors contexte. La trace LangSmith montre que l'outil de recherche Web a été utilisé comme solution de secours pour récupérer les informations pertinentes avant la réponse finale générée par LLM (voir [Figure](#page-485-0) 10-4).

<span id="page-485-0"></span>![](_page_485_Figure_0.jpeg)

![](_page_485_Figure_1.jpeg)

<span id="page-486-1"></span>Passons à l'étape suivante des tests d'application LLM : la préproduction.

## L'étape de préproduction

<span id="page-486-2"></span>L'objectif de l'étape de test de préproduction est de mesurer et d'évaluer les performances de votre application avant la production. Cela vous permettra d'évaluer efficacement la précision, la latence et le coût de l'utilisation du LLM.

### **Création d'ensembles de données**

<span id="page-486-0"></span>Avant les tests, vous devez définir un ensemble de scénarios que vous souhaitez tester et évaluer. Un *ensemble de données* est une collection d'exemples qui fournissent des entrées et des sorties attendues utilisées pour évaluer votre application LLM.

Il existe trois méthodes courantes pour créer des ensembles de données à des fins d'évaluation :

#### *Exemples sélectionnés manuellement*

Il s'agit d'exemples manuscrits basés sur les entrées utilisateur attendues et les résultats générés idéaux. Un petit ensemble de données se compose de 10 à 50 exemples de qualité. Fini

Au fil du temps, davantage d'exemples peuvent être ajoutés à l'ensemble de données en fonction des cas extrêmes qui émergent en production.

#### *Journaux des applications*

<span id="page-487-0"></span>Une fois l'application en production, vous pouvez stocker les entrées utilisateur en temps réel et les ajouter ultérieurement à l'ensemble de données. Cela permettra de garantir que l’ensemble de données est réaliste et couvre les questions les plus courantes des utilisateurs.

#### *Données synthétiques*

<span id="page-487-2"></span>Il s'agit d'exemples générés artificiellement qui simulent divers scénarios et cas extrêmes. Cela vous permet de générer de nouvelles entrées en échantillonnant les entrées existantes, ce qui est utile lorsque vous ne disposez pas de suffisamment de données réelles sur lesquelles tester.

<span id="page-487-1"></span>Dans LangSmith, vous pouvez créer un nouvel ensemble de données en sélectionnant Ensembles de données et tests dans la barre latérale et en cliquant sur le bouton « + Nouvel ensemble de données » en haut à droite de l'application, comme indiqué dans la [Figure](#page-488-0) 10-5.

Dans la fenêtre ouverte, saisissez les détails de l'ensemble de données pertinent, notamment un nom, une description et un type d'ensemble de données. Si vous souhaitez utiliser votre propre ensemble de données, cliquez sur le bouton « Télécharger un ensemble de données CSV ».

<span id="page-488-0"></span>![](_page_488_Picture_0.jpeg)

Figure 10-5. Création d'un nouvel ensemble de données dans l'interface utilisateur LangSmith

LangSmith propose trois types d'ensembles de données différents :

#### *ensemble de données kv (valeur-clé)*

- <span id="page-488-1"></span>*Inputs* et *outputs* sont représentés sous forme de paires clé-valeur arbitraires.
- L'ensemble de données kv est le plus polyvalent et constitue le type par défaut. L'ensemble de données kv convient à un large éventail de scénarios d'évaluation.
- Ce type d'ensemble de données est idéal pour évaluer les chaînes et les agents qui nécessitent plusieurs entrées ou génèrent plusieurs sorties.

#### *ensemble de données LLM (grand modèle de langage)*

- <span id="page-489-1"></span>L'ensemble de données llm est conçu pour évaluer les modèles de langage de style de complétion.
- Le dictionnaire d'entrées contient une seule touche d'entrée mappée à la chaîne d'invite.
- Le dictionnaire de sorties contient une seule clé de sortie mappée à la chaîne de réponse correspondante.
- Ce type d'ensemble de données simplifie l'évaluation des LLM en fournissant un format standardisé pour les entrées et les sorties.

#### *ensemble de données de discussion*

- <span id="page-489-0"></span>L'ensemble de données de discussion est conçu pour évaluer les messages de discussion structurés LLM en tant qu'entrées et sorties.
- Le dictionnaire *inputs* contient une seule touche *input* mappée à une liste de messages de discussion sérialisés.
- Le dictionnaire *outputs* contient une seule clé *output* mappée à une liste de messages de discussion sérialisés.
- Ce type d'ensemble de données est utile pour évaluer les systèmes d'IA conversationnelle ou les chatbots.
### L'option la plus flexible est le type de données clé-valeur (voir [Figure](#page-490-0) 10-6).

<span id="page-490-0"></span>

| ← Nouvel ensemble de données |                                                                                                                                                                                                                                | Annuler Créer |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| Créer un ensemble de données |                                                                                                                                                                                                                                |               |
| Importer un fichier CSV | Téléchargez un fichier CSV ou faites un glisser-déposer<br>0 |               |
| Détails de l'ensemble de données | Nom |               |
|                       | ds-pli-artistique-46 |               |
|                       | Descriptif |               |
|                       | Description du type |               |
|                       |                                                                                                                                                                                                                                |               |
| Sélectionnez un type d'ensemble de données | Les ensembles de données Key-Value<br>Key Value (KV) sont le type par défaut, permettant des entrées sous forme de dictionnaires. Utile pour les flux de travail personnalisés, mais une configuration supplémentaire peut être nécessaire pour une évaluation multi-clés.                                    |               |
|                       | Chat<br>Les ensembles de données de chat utilisent un dictionnaire « d'entrées » avec une seule clé « d'entrée » pour les messages de chat sérialisés et un dictionnaire de « sorties » avec une seule clé « de sortie » pour les messages de chat sérialisés.                                |               |
|                       | LLM<br>Les bases de données LLM ont un dictionnaire « d'entrées » qui contient une seule clé « d'entrée » mappée à une seule chaîne d'invite. De même, le dictionnaire « sorties »<br>contient une seule clé « sortie » mappée à une seule chaîne de réponse. |               |

Figure 10-6. Sélection d'un type d'ensemble de données dans l'interface utilisateur de LangSmith

Ensuite, ajoutez des exemples à l'ensemble de données en cliquant sur Ajouter un exemple. Fournissez les exemples d'entrée et de sortie sous forme d'objets JSON, comme indiqué dans la [Figure](#page-491-0) 10-7.

<span id="page-491-0"></span>

| ← Ajouter un exemple à l'ensemble de données clé-valeur |          |              | Annuler | Soumettre |
|---------------------------------|----------|--------------|--------|--------|
| Entrée<br>Modifier les entrées<br>Afficher le schéma d'entrée | 1 | {} |        |        |
| Sortie<br>Modifier les sorties | 1 | {} |        |        |
| Afficher le schéma de sortie |          |              |        |        |
| Fractionnements d'ensembles de données | base (X) | Choisissez diviser |        |        |

Figure 10-7. Ajouter des exemples d'ensembles de données clé-valeur dans l'interface utilisateur de LangSmith

Vous pouvez également définir un schéma pour votre ensemble de données dans la section « Schéma de l'ensemble de données », comme indiqué dans la [Figure](#page-492-0) 10-8.

<span id="page-492-0"></span>![](_page_492_Figure_0.jpeg)

<span id="page-492-2"></span>Figure 10-8. Ajout d'un schéma d'ensemble de données dans l'interface utilisateur de LangSmith

### **Définir vos critères d'évaluation**
<span id="page-492-1"></span>Après avoir créé votre ensemble de données, vous devez définir des métriques d'évaluation pour évaluer les résultats de votre application avant de la déployer en production. Cette évaluation par lots sur une suite de tests prédéterminée est souvent appelée *évaluation hors ligne***.**

<span id="page-492-3"></span>Pour une évaluation hors ligne, vous pouvez éventuellement étiqueter les résultats attendus (c'est-à-dire les références de vérité terrain) pour les points de données <span id="page-493-2"></span>sur lesquels vous effectuez les tests. Cela vous permet de comparer la réponse de votre application avec les références de vérité terrain, comme indiqué dans la [Figure](#page-493-0) 10-9.

<span id="page-493-0"></span>![](_page_493_Figure_1.jpeg)

Figure 10-9. Diagramme d'évaluation de l'IA

<span id="page-493-1"></span>Il existe trois évaluateurs principaux pour évaluer les performances de votre application LLM :

#### *Évaluateurs humains*

<span id="page-493-4"></span>Si vous ne pouvez pas exprimer vos exigences en matière de tests sous forme de code, vous pouvez utiliser les commentaires humains pour exprimer des caractéristiques qualitatives et étiqueter les réponses des applications avec des scores. LangSmith accélère le processus de collecte et d'intégration des commentaires humains dans les files d'attente d'annotations.

#### *Évaluateurs heuristiques*

<span id="page-493-3"></span>Il s'agit de fonctions et d'assertions codées en dur qui effectuent des calculs pour déterminer un score. Vous pouvez utiliser des heuristiques sans référence (par exemple, vérifier si la sortie est un JSON valide) ou des heuristiques basées sur des références telles que la précision. L'évaluation basée sur des références compare un résultat à une vérité terrain prédéfinie, tandis que l'évaluation sans référence évalue les caractéristiques qualitatives sans vérité terrain. Les évaluateurs heuristiques personnalisés sont utiles pour les tâches de génération de code telles que la vérification de schéma et les tests unitaires avec une logique d'évaluation codée en dur.

#### *Évaluateurs LLM-as-a-juge*

<span id="page-494-1"></span>Cet évaluateur intègre des règles de notation humaine dans une invite LLM pour évaluer si le résultat est correct par rapport à la réponse de référence fournie à partir de la sortie de l'ensemble de données. Au fur et à mesure que vous itérez en pré-production, vous devrez auditer les scores et ajuster le LLM en tant que juge pour produire des scores fiables.

<span id="page-494-0"></span>Pour commencer l'évaluation, commencez simplement avec les évaluateurs heuristiques. Mettez ensuite en œuvre des évaluateurs humains avant de passer au LLM-as-a-juge pour automatiser votre évaluation humaine. Cela vous permet d'ajouter de la profondeur et de l'échelle une fois vos critères bien définis.

**CONSEIL**

Lorsque vous utilisez des évaluateurs LLM en tant que juge, utilisez des invites simples qui peuvent facilement être reproduites et comprises par un humain. Par exemple, évitez de demander à un LLM de produire des scores sur une plage de 0 à 10 avec de vagues distinctions entre les scores.

[Figure](#page-495-0) 10-10 illustre l'évaluateur LLM en tant que juge dans le contexte d'un cas d'utilisation RAG. Notez que la réponse de référence est la vérité terrain.

<span id="page-495-0"></span>![](_page_495_Figure_3.jpeg)

Figure 10-10. Évaluateur LLM en tant que juge utilisé dans un cas d'utilisation RAG

#### **Améliorer les performances des évaluateurs LLM en tant que juge**

<span id="page-495-1"></span>L'utilisation d'un LLM en tant que juge est une méthode efficace pour noter les résultats en langage naturel des applications LLM. Cela implique de passer

le résultat généré vers un LLM distinct pour jugement et évaluation. Mais comment pouvez-vous faire confiance aux résultats de l’évaluation LLM-as-a-juge ?

<span id="page-496-1"></span><span id="page-496-0"></span>Souvent, des cycles d'ingénierie rapide sont nécessaires pour améliorer la précision, ce qui est fastidieux et prend du temps. Heureusement, LangSmith propose une solution d'invite *quelques plans* dans laquelle les corrections humaines des résultats du LLM en tant que juge sont stockées sous forme d'exemples de quelques plans, qui sont ensuite réinjectés dans l'invite dans les itérations futures.

En utilisant l'apprentissage en quelques étapes, le LLM peut améliorer la précision et aligner les résultats sur les préférences humaines en fournissant des exemples de comportement correct. Ceci est particulièrement utile lorsqu'il est difficile de construire des instructions sur la façon dont le LLM doit se comporter ou être formaté.

L'évaluateur en quelques coups suit ces étapes :

- 1. L'évaluateur LLM fournit des commentaires sur les résultats générés, en évaluant des facteurs tels que l'exactitude, la pertinence ou d'autres critères.
- 2. Il ajoute des corrections humaines pour modifier ou corriger les commentaires de l'évaluateur LLM dans LangSmith. C’est là que les préférences et le jugement humains sont capturés.
- 3. Ces corrections sont stockées sous forme d'exemples de quelques prises dans LangSmith, avec une option permettant de laisser des explications sur les corrections.
- 4. Les quelques exemples sont incorporés dans les invites futures lors des évaluations ultérieures.
Au fil du temps, l’évaluateur en quelques coups s’alignera de plus en plus sur les préférences humaines. Ce mécanisme d'auto-amélioration réduit le besoin d'une ingénierie rapide et fastidieuse, tout en améliorant la précision et la pertinence des évaluations LLM en tant que juge.

Voici comment configurer facilement l'évaluateur LLM-as-a-juge dans LangSmith pour une évaluation hors ligne. Tout d’abord, accédez à la section « Ensembles de données et tests » dans la barre latérale et sélectionnez l’ensemble de données pour lequel vous souhaitez configurer l’évaluateur. Cliquez sur le bouton Ajouter un évaluateur automatique en haut à droite du tableau de bord pour ajouter un évaluateur à l'ensemble de données. Cela ouvrira un modal que vous pourrez utiliser pour configurer l'évaluateur.

<span id="page-497-0"></span>Sélectionnez l'option LLM-as-a-judge et donnez un nom à votre évaluateur. Vous aurez désormais la possibilité de définir une invite en ligne ou de charger une invite à partir du hub d'invite qui sera utilisée pour évaluer les résultats des exécutions de l'expérience. Pour les besoins de cet exemple, choisissez l'option Créer un évaluateur de quelques tirs, comme indiqué dans la [Figure](#page-499-0) 10-11.

<span id="page-499-0"></span>![](_page_499_Picture_0.jpeg)

| Nom de l'auto-évaluateur |   |      |          |
|------------------------------|---|------|---------------|
| Postuler aux exécutions passées<br>e |   |      |          |
| Juge |   |      |          |
| Fournisseur |   |      |          |
| OpenAl | > | Discuter | Instruire |
| Modèle |   |      |          |
| gpt-40 |   |      | V |
| Température<br>C |   |      | 0 |

| Essayez une suggestion d'invite d'évaluateur<br>Utilisez l'une de nos invites personnalisables prêtes à l'emploi | RECOMMANDÉ |  |  |
|------------------------------------------------------------------------------------------------------------------|-------------|--|--|
| Créez un évaluateur en quelques plans<br>Alignez automatiquement votre évaluateur avec les préférences humaines via des exemples en quelques plans |             |  |  |
| Créez une invite à partir de zéro<br>Utilisez notre éditeur de modèles pour rédiger votre propre invite |             |  |  |
| Utiliser une invite du LangChain Hub<br>Utiliser les invites fournies par la communauté |             |  |  |

Figure 10-11. Options de l'interface utilisateur LangSmith pour l'évaluateur LLM-as-a-juge

Cette option créera un ensemble de données contenant quelques exemples qui se rempliront automatiquement lorsque vous apporterez des corrections aux commentaires de l'évaluateur. Les exemples de cet ensemble de données seront insérés dans le message d'invite du système.

Vous pouvez également spécifier les critères de notation dans le champ Schéma et basculer entre les types primitifs, par exemple entier et booléen (voir [Figure](#page-501-0) 10-12).

<span id="page-501-0"></span>

| score = {{score}} |   |
|--------------------------------------------------------------|--------|
| Raisonnement : {{few_shot_explanation}} |   |
| REQUÊTE : {{query}}<br>RÉPONSE : {{response}}<br>RÉFÉRENCE : {{référence}} | D |

| Noter<br>Notez le quiz en fonction des critères ci-dessus avec un score. |               |           |          |   |
|--------------------------------------------------------------------|---------------|---------------|----------|---|
| score<br>Fournir le score :<br>Définir les valeurs autorisées | V<br>Obligatoire | Entier V | ÉDITEUR C | U |
| Ajouter des critères |               |           |          |   |

<span id="page-501-1"></span>Figure 10-12. Critères de notation des évaluateurs LLM-as-a-juge

Enregistrez l'évaluateur et revenez à la page de détails de l'ensemble de données. À l'avenir, chaque expérience ultérieure exécutée à partir de l'ensemble de données sera évaluée par l'évaluateur que vous avez configuré.

#### **Évaluation par paires**

<span id="page-502-0"></span>Classer les résultats du LLM par préférence peut être moins exigeant sur le plan cognitif pour les évaluateurs humains ou LLM en tant que juge. Par exemple, évaluer quelle sortie est la plus informative, spécifique ou sûre. L'évaluation par paires compare simultanément deux sorties de différentes versions d'une application pour déterminer quelle version répond le mieux aux critères d'évaluation.

<span id="page-502-1"></span>LangSmith prend en charge de manière native l'exécution et la visualisation des générations d'applications LLM par paire, en mettant en évidence la préférence pour une génération par rapport à une autre en fonction des directives définies par l'évaluateur par paire. L'évaluation par paire de LangSmith vous permet d'effectuer les opérations suivantes :

- Définir un évaluateur LLM-as-a-juge personnalisé par paire en utilisant les critères souhaités
- Comparez deux générations LLM à l'aide de cet évaluateur

Conformément aux [docs] LangSmith (https://oreil.ly/ruFvy), vous pouvez utiliser des évaluateurs par paires personnalisés dans le SDK LangSmith et visualiser les résultats des évaluations par paires dans l'interface utilisateur de LangSmith.

Après avoir créé une expérience d'évaluation, vous pouvez accéder à l'onglet Expériences par paires dans la section Ensembles de données et expériences. L'interface utilisateur vous permet de plonger dans chaque paire

expérience, montrant quelle génération LLM est préférée en fonction de nos critères. Si vous cliquez sur le score RANKED\_PREFERENCE sous chaque réponse, vous pouvez approfondir chaque trace d'évaluation (voir [Figure](#page-503-0) 10-13).

<span id="page-503-2"></span><span id="page-503-0"></span>

| Affichage d'une expérience par paire |                                                                                                                                                                                                                                                                |                                                                                                                                                                          |  |  |  |  |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|
| résumé-opon-21590361 vs résumé-cird-1992a55c-4ced v comparé par comparé par @ RANKED PREFERL. v |                                                                                                                                                                                                                                                                |                                                                                                                                                                          |  |  |  |  |
| bouche | résumé-opus-21590361 7<br>(80) (29)<br>V | résumé-cand-r-1092x55c 7<br>(26) (89) |  |  |  |  |
| Les grands modèles de langage peuvent-ils raisonner un | Les LLM peuvent-ils vraiment planifier et raisonner ? Titre : "OPT-4 : Récupération impressionnante, mais non - | "LLM = 7 Parming ( 7 Détrompez-vous ! _ " = Les grands modèles de langage ne raisonnent ni ne planifient réellement, malgré la pop | | | | |
| Exemple #102f * | · PRÉFÉRENCE CLASSÉE : 1 · = SCORE D'ENGAGEMENT RÉSUMÉ : 8 · | · PRÉFÉRENCE CLASSÉE : 0 · B ENGAGEMENT BUMMAIRE, SCORE : B = |  |  |  |  |
| Segmenter n'importe quoi Alexander Kirillov | Voici un tweet récapitulatif pour le document Segment Anything. Un segment n'importe quoi : A | Nouvelle recherche RAI de @MetaAlllesearch ! Découvrez la dernière innovation en matière de vision par ordinateur, le Segm |  |  |  |  |
| Exemple Pladia • | · PRÉFÉRENCE CLASSÉE : 1 · + 5 : SCORE D'ENGAGEMENT RÉSUMÉ : 5 = | · PRÉFÉRENCE CLASSÉE : 0 + |  |  |  |  |
| LangRoPE : Extension du contexte LLM Wi<br>Exemple #2b53 # | Voici un tweet pour résumer l'article de LongRoPE : @ LongRoPE : Extending LLM Co<br>· PRÉFÉRENCE CLASSÉE : 0 + = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = | Une nouvelle recherche étend la fenêtre de contisel #LLM à un énorme LJ Million Tokent L. Introduction : Actuel<br>· PRÉFÉRENCE CLASSÉE : 1 + ] = ENGAGEMENT RÉSUMÉ, SCORE : 4 +<br>= |  |  |  |  |
| Renforcer le modèle de langage étendu A | Voici un tweet potentiel pour résumer l'article "Autonomiser les modules de grands langages | Une nouvelle recherche donne du pouvoir aux agents de modèles de grands langages ! @ L'approche innovante, LearnAct, permet | | | | |
| Exemple #4409 # | · PRÉFÉRENCE CLASSÉE : 1 + = 5 NOTE D'ENGASEMENT RÉSUMÉ : 5 + | · PRÉFÉRENCE CLASSÉE : 0 -> |  |  |  |  |
| Jamba : un transformateur hybride-Mamba | Voici un tweet résumant le Jamba : Un puissant transformateur hybride | Nouveau PLLM Aiert Jambat, le modèle de langage hybride Transformer Mamba qui a tout pour plaire ga Jamba |  |  |  |  |
| Exemple #4424 + | · PRÉFÉRENCE CLASSÉE : 0 + ] @ SCORE SOMMAIRE D'ENGASEMENT : 5 + | PRÉFÉRENCE CLASSÉE B : 1 + ] @ SCONE D'ENGAGEMENT RÉSUMÉ : 4 + |  |  |  |  |
| Swin Transformer V2 : augmentation du plafond | Voici une suggestion de Tweet qui résume l'article "Swin Transformer VZ". Titre : Suisse | Nouveaux BSwinTransformer & à 38 paramètres ! @ 1536x1536 reste Innovations clés : Poste résident |  |  |  |  |
| Exemple #5681 * | · PRÉFÉRENCE CLASSÉE : 1 + = SCORE D'ENGAGEMENT RÉSUMÉ : 5 + | · PRÉFÉRENCE CLASSÉE : 0 + ] @ ENGAGEMENT SOMMAIRE, SCORE : 2 + |  |  |  |  |
| À condition qu'une attribution appropriée soit fournie | Voici une suggestion de Tweet In résumant l'article "All You Need": ( ) Tra- | Nouveau papier Alerti. "L'attention est tout ce dont vous avez besoin". une étude transformatrice @Trom @GoogleAl. @ Présenter |  |  |  |  |
| Exemple #c9d7 + | · PRÉFÉRENCE CLASSÉE : 1 + = SCORE D'ENGAGEMENT RÉSUMÉ ! S + | · PRÉFÉRENCE CLASSÉE : 0 + ] @ RÉSUMÉ ENGAGEMENT, SCORE ! 6 + |  |  |  |  |
| ROF ORMER : TRANSFOR AMÉLIORÉ | Voici une suggestion de Tweet qui résume l'article de RoFormer : [+] Rotary Position Em | Présentation du « Riformer » : un transformateur amélioré qui fait pivoter vos intégrations de position ! & "Quoi | | | | |
| Exemple #d518 = | · PRÉFÉRENCE CLASSÉE : 1 · = SCORE D'ENGAGEMENT RÉSUMÉ : 8 · | · PRÉFÉRENCE CLASSÉE : 0 · SCORE D'ENGAGEMENT BBUMMARY ! 4 + |  |  |  |  |
| Rapport technique Phi-3 : Un puissant Capa | Voici une suggestion de Tweet pour résumer le rapport technique phi-3 : w Mighty Mini- | Voici un brouillon du Tweet pour le téléavertisseur que vous avez fourni : يل يل "Ph-3 Min' Your Phone's New Bent Friend" (j) - Trail |  |  |  |  |
| Exemple #e319 * | · PRÉFÉRENCE CLASSÉE : 1 · · 5 NOTE D'ENGAGEMENT RÉSUMÉ : 5 · | · PRÉFÉRENCE CLASSÉE : 0 + ] B ENGAGEMENT BUMMAIRE, SCORE : B = |  |  |  |  |
| Extension du contexte de Llama-3 par dix | @ Llama-3 Leags vers BOK Contaxt du jour au lendemain avec QLoRA Fine-Tuning ! _ Points clés - | Voici une ébauche du Tweet pour cet article : Nouvelle recherche : Extension du concours LLM et LLama-J 1 conte |  |  |  |  |
| Exemple #13d5 # | · PRÉFÉRENCE CLASSÉE : 1 + = 5 = 5SCORE D'ENGASEMENT RÉSUMÉ : 5 = | · PRÉFÉRENCE CLASSÉE : 0 + = = ENGAGEMENT RÉSUMÉ, SCORE : \$ = |  |  |  |  |

<span id="page-503-1"></span>Figure 10-13. Trace d'évaluation de l'interface utilisateur d'expérimentation par paires

### **Tests de régression**

<span id="page-503-3"></span>Dans le développement de logiciels traditionnel, les tests sont censés réussir à 100 % en fonction des exigences fonctionnelles. Cela garantit un comportement stable une fois le test validé. En revanche, cependant, les performances de sortie des modèles d'IA peuvent varier considérablement en raison de la *dérive* du modèle (dégradation due à des changements dans la distribution des données ou

mises à jour du modèle). Par conséquent, tester les applications d’IA ne conduit pas toujours à un score parfait sur l’ensemble de données d’évaluation.

Cela a plusieurs implications. Tout d’abord, il est important de suivre les résultats et les performances de vos tests au fil du temps afin d’éviter une régression des performances de votre application. Les tests de *Régression* garantissent que les dernières mises à jour ou modifications du modèle LLM de votre application ne *régressent* (moins bien) par rapport à la ligne de base.

Deuxièmement, il est crucial de comparer les points de données individuels entre deux ou plusieurs essais expérimentaux pour voir où le modèle a eu raison ou tort.

<span id="page-504-0"></span>La vue de comparaison de LangSmith prend en charge nativement les tests de régression, vous permettant de voir rapidement les exemples qui ont changé par rapport à la ligne de base. Les exécutions qui ont régressé ou amélioré sont mises en évidence différemment dans le tableau de bord LangSmith (voir [Figure](#page-505-0) 10-14).

<span id="page-505-0"></span>![](_page_505_Picture_0.jpeg)

Figure 10-14. Vue comparative des expériences de LangSmith

Dans le tableau de bord Comparing Experiments de LangSmith, vous pouvez effectuer les opérations suivantes :

- Comparez plusieurs expériences et exécutions associées à un ensemble de données. Les statistiques globales des exécutions sont utiles pour la migration de modèles ou d'invites, ce qui peut entraîner des améliorations de performances ou une régression sur des exemples spécifiques.
- Définissez une exécution de référence et comparez-la aux versions précédentes de l'application pour détecter les régressions inattendues. Si une régression se produit, vous pouvez isoler à la fois la version de l'application et les exemples spécifiques contenant des modifications de performances.

Explorez les points de données qui se sont comportés différemment entre les expériences et les exécutions comparées.

Ces tests de régression sont essentiels pour garantir que votre application maintient des performances élevées dans le temps, quelles que soient les mises à jour et les modifications LLM.

Maintenant que nous avons couvert diverses stratégies de tests de préproduction, explorons un cas d'utilisation spécifique.

### **Évaluer les performances de bout en bout d'un agent**

<span id="page-506-0"></span>Bien que les agents se montrent très prometteurs dans l'exécution de tâches et de flux de travail autonomes, tester les performances d'un agent peut s'avérer difficile. Dans les chapitres précédents, vous avez appris comment les agents utilisent les appels d'outils avec la planification et la mémoire pour générer des réponses. En particulier, l'appel d'outil permet au modèle de répondre à une invite donnée en générant un outil à invoquer et les arguments d'entrée requis pour exécuter l'outil.

Étant donné que les agents utilisent un LLM pour décider du flux de contrôle de l'application, chaque exécution d'agent peut avoir des résultats très différents. Par exemple, différents outils peuvent être appelés, les agents peuvent rester coincés dans une boucle ou le nombre d'étapes du début à la fin peut varier considérablement.

Idéalement, les agents devraient être testés à trois niveaux de granularité différents :

#### *Réponse*

<span id="page-507-0"></span>La réponse finale de l'agent pour se concentrer sur les performances de bout en bout. Les entrées sont une invite et une liste facultative d'outils, tandis que la sortie est la réponse finale de l'agent.

#### *Une seule étape*

<span id="page-507-1"></span>Toute étape unique et importante de l'agent pour explorer des appels ou des décisions d'outils spécifiques. Dans ce cas, le résultat est un appel d’outil.

#### *Trajectoire*

<span id="page-507-2"></span>La trajectoire complète de l'agent. Dans ce cas, le résultat est la liste des appels d’outils.

[Figure](#page-508-0) 10-15 illustre ces niveaux :

<span id="page-508-0"></span>![](_page_508_Figure_0.jpeg)

Figure 10-15. Un exemple de flux d'une application agent

Examinons plus en détail chacune de ces trois granularités de test d'agent.

#### **Test de la réponse finale d'un agent**
<span id="page-508-1"></span>Afin d'évaluer les performances globales d'un agent sur une tâche, vous pouvez traiter l'agent comme une boîte noire et définir le succès en fonction de son achèvement ou non de la tâche.

Le test de la réponse finale de l'agent implique généralement les éléments suivants :

*Entrées*

Saisie utilisateur et (éventuellement) outils prédéfinis

*Sortie*

Réponse finale de l'agent

*Évaluateur*

LLM-en tant que juge

Pour mettre en œuvre cela de manière programmatique, créez d'abord un ensemble de données qui comprend les questions et les réponses attendues de l'agent :

*Python*

```
from langsmith import Client
client = Client()
# Create a dataset
examples = [
 ("Which country's customers spent the most? A
 """The country whose customers spent the 
 expenditure of $523.06"""),
 ("What was the most purchased track of 2013?"
 "The most purchased track of 2013 was Hot
 ("How many albums does the artist Led Zeppeli
```

```
 "Led Zeppelin has 14 albums"),
 ("What is the total price for the album "Big 
 "The total price for the album 'Big Ones
 ("Which sales agent made the most in sales in
 "Steve Johnson made the most sales in 200
]
dataset_name = "SQL Agent Response"
if not client.has_dataset(dataset_name=dataset_na
 dataset = client.create_dataset(dataset_name=
 inputs, outputs = zip(
 *[({"input": text}, {"output": label}) fo
 )
 client.create_examples(inputs=inputs, outputs
## chain
def predict_sql_agent_answer(example: dict):
 """Use this for answer evaluation"""
 msg = {"messages": ("user", example["input"])
 messages = graph.invoke(msg, config)
 return {"response": messages['messages'][-1]
```
*JavaScript*

importer {Client} depuis 'langsmith' ;

```
const client = new Client();
```

```
// Create a dataset
const examples = [
 ["Which country's customers spent the most? And
 `The country whose customers spent the most i
 expenditure of $523.06`],
 ["What was the most purchased track of 2013?",
 "The most purchased track of 2013 was Hot Gir
 ["How many albums does the artist Led Zeppelin 
 "Led Zeppelin has 14 albums"],
 ["What is the total price for the album 'Big On
 "The total price for the album 'Big Ones' is 
 ["Which sales agent made the most in sales in 2
 "Steve Johnson made the most sales in 2009"],
];
const datasetName = "SQL Agent Response";
async function createDataset() {
 const hasDataset = await client.hasDataset({ da
 if (!hasDataset) {
 const dataset = await client.createDataset(da
 const inputs = examples.map(([text]) => ({ in
 const outputs = examples.map(([, label]) => (
 await client.createExamples({ inputs, outputs
```
}

```
 }
}
createDataset();
// Chain function
async function predictSqlAgentAnswer(example) {
 // Use this for answer evaluation
 const msg = { messages: [{ role: "user", conten
 const output = await graph.invoke(msg, config);
 return { response: output.messages[output.messa
}
```
Ensuite, comme indiqué précédemment, nous pouvons utiliser le LLM pour comparer la réponse générée avec la réponse de référence :

*Python*

```
from langchain import hub
from langchain_openai import ChatOpenAI
from langsmith.evaluation import evaluate
# Grade prompt
grade_prompt_answer_accuracy = hub.pull("langchai
def answer_evaluator(run, example) -> dict:
    """
```

```
 A simple evaluator for RAG answer accuracy
 """
```

```
 # Get question, ground truth answer, RAG chai
 input_question = example.inputs["input"]
 reference = example.outputs["output"]
 prediction = run.outputs["response"]
```

```
 # LLM grader
 llm = ChatOpenAI(model="gpt-4o", temperature=
```

```
 # Structured prompt
 answer_grader = grade_prompt_answer_accuracy
```

```
 # Run evaluator
```

```
 score = answer_grader.invoke({"question": inp
 "correct_answer
                       "student_answer
```

```
 score = score["Score"]
```

```
 return {"key": "answer_v_reference_score", "s
```

```
## Run evaluation
experiment_results = evaluate(
 predict_sql_agent_answer,
 data=dataset_name,
```
évaluateurs=[réponse évaluateur]

```
 evaluators=[answer_evaluator],
 num_repetitions=3,
)
```
#### *JavaScript*

```
importer { pull } depuis "langchain/hub" ;
importer { ChatOpenAI } depuis "langchain_openai" ;
importer { évaluer } depuis "langsmith/evaluation" ;
fonction asynchroneanswerEvaluator(exécuter, exemple) {
 /**
 * Un évaluateur simple pour la précision des réponses RAG
 */
 // Obtenez la question, la réponse à la vérité terrain, la chaîne RAG
 const inputQuestion = exemple.inputs["input"];
 référence const = exemple.outputs["output"];
 const prédiction = run.outputs["response"];
 // Évaluatrice LLM
 const llm = nouveau ChatOpenAI({ modèle : "gpt-4o", t
// Invite de note 
 const gradePromptAnswerAccuracy = pull(
 "langchain-ai/rag-answer-vs-reference"
 )
```

```
 // Invite structurée
 const réponseGrader = gradePromptAnswerAccuracy
 // Exécuter l'évaluateur
 const scoreResult = attendre réponseGrader.invoke({
 question : question d'entrée,
 correct_answer : référence,
 student_answer : prédiction
 });
 const score = scoreResult["Score"];
 return { clé : "answer_v_reference_score", score
}
// Exécuter l'évaluation
const experienceResults = évaluer (predictSqlAgen
 données : nom de l'ensemble de données,
 évaluateurs : [answerEvaluator],
 numRépétitions : 3,
});
```
**Testing a single step of an agent**

);

<span id="page-516-1"></span><span id="page-516-0"></span>Testing an agent's individual action or decision enables you to identify and analyze specifically where your application is underperforming. Testing for a single step of an agent involves the following:

#### *Inputs*

User input to a single step (for example, user prompt, set of tools). This can also include previously completed steps.

#### *Output*

LLM response from the inputs step, which often contains tool calls indicating what action the agent should take next.

#### *Evaluator*

Binary score for correct tool selection and heuristic assessment of the tool input's accuracy.

The following example checks a specific tool call using a custom evaluator:

*Python*

from langsmith.schemas import Example, Run

```
def predict_assistant (exemple : dict) :
 """Assistant d'appel pour l'évaluation des appels d'outil unique
 msg = [ ("utilisateur", exemple["entrée"]) ]
 résultat = assistant_runnable.invoke({"messages
 return {"réponse": résultat}
```

```
def check_specific_tool_call (root_run : exécuter, exemple
 """
 Vérifiez si le premier appel d'outil dans la réponse 
 """
 # Appel d'outil attendu
 attendu_tool_call = 'sql_db_list_tables'
 # Exécuter
 réponse = root_run.outputs["réponse"]
 # Recevoir l'appel de l'outil
 essaye :
 tool_call = getattr(réponse, 'tool_calls
 sauf (IndexError, KeyError) :
 tool_call = Aucun
 score = 1 si tool_call == Expected_tool_call
 return {"score": score, "key": "single_tool_c
```

```
experience_results = évaluer (
```

```
 prédire_assistant,
 data=nom_ensemble de données,
 évaluateurs=[check_special_tool_call],
 num_repetitions=3,
 métadonnées={"version": métadonnées},
)
```
#### *JavaScript*

```
importer {evaluate} depuis 'langsmith/evaluation' ;
// Assistant de prédiction
fonction prédictAssistant (exemple) {
 /**
 * Invoquer l'assistant pour l'évaluation des appels à un seul outil
 */
 const msg = [{ rôle : "utilisateur", contenu : exemple
 résultat const = assistantRunnable.invoke({ mes
 return { réponse : résultat } ;
}
// Vérifier l'appel d'un outil spécifique
fonction checkSpecificToolCall (rootRun, exemple)
 /**
 * Vérifiez si le premier outil appelle dans la réponse
 *appel d'outil.
```

```
 */
 // Appel d'outil attendu
 const attenduToolCall = "sql_db_list_tables"
 // Exécuter
 const réponse = rootRun.outputs.response;
 // Récupère l'appel de l'outil
 laissez toolCall ;
 essayez {
 toolCall = réponse.tool_calls?.[0]?.name
 } attraper (erreur) {
 outilAppel = nul ;
 }
 score const = toolCall === ExpectToolCall ?
 return {score, clé : "single_tool_call" } ;
}
// Résultats de l'expérience
const experienceResults = évaluer (predictAssista
 données : nom de l'ensemble de données,
 évaluateurs : [checkSpecificToolCall],
 numRépétitions : 3,
});
```
The preceding code block implements these distinct components:

- Invoke the assistant, assistant\_runnable , with a prompt and check if the resulting tool call is as expected.
- Utilize a specialized agent where the tools are hardcoded rather than passed with the dataset input.
- <span id="page-520-0"></span>Specify the reference tool call for the step that we are evaluating for expected\_tool\_call .

#### **Testing an agent's trajectory**

<span id="page-520-1"></span>It's important to look back on the steps an agent took in order to assess whether or not the trajectory lined up with expectations of the agent—that is, the number of steps or sequence of steps taken.

Testing an agent's trajectory involves the following:

*Inputs*

User input and (optionally) predefined tools.

*Output*

Expected sequence of tool calls or a list of tool calls in any order.

#### *Evaluator*

Function over the steps taken. To test the outputs, you can look at an exact match binary score or metrics that focus on the number of incorrect steps. You'd need to evaluate the full agent's trajectory against a reference trajectory and then compile as a set of messages to pass into the LLM-as-a-judge.

The following example assesses the trajectory of tool calls using custom evaluators:

#### *Python*

```
def predict_sql_agent_messages (exemple : dict) :
 """Utilisez ceci pour l'évaluation des réponses"""
 msg = {"messages": ("utilisateur", exemple["entrée"])
 messages = graph.invoke(msg, configuration)
 return {"réponse": messages}
def find_tool_calls(messages):
 """
 Rechercher tous les appels d'outils dans les messages renvoyés
 """
 appels_outils = [
 tc['nom']
```
f i [' '] f i

```
 pour m dans les messages['messages'] pour tc dans g
 ]
 retourner les appels_outils
def contient_all_tool_calls_any_order(
 root_run : Exécuter, exemple : Exemple
) -> dicté :
 """
 Vérifiez si tous les outils attendus sont appelés dans n'importe quel
 """
 attendu = [
 'sql_db_list_tables',
 'sql_db_schema',
 'sql_db_query_checker',
 'sql_db_query',
 'check_result'
 ]
 messages = root_run.outputs["réponse"]
 tool_calls = find_tool_calls(messages)
 # En option, enregistrez les appels de l'outil -
 #print("Voici mes appels d'outils :")
 #print(appels_outils)
 si set (attendu) <= set (tool_calls) :
 note = 1
 sinon :
 note = 0
 return {"score": int(score), "key": "multi_to
```
d f i ll l ll i d (

```
def contain_all_tool_calls_in_order (root_run : Ru
 """
 Vérifiez si tous les outils attendus sont appelés en exa
 """
 messages = root_run.outputs["réponse"]
 tool_calls = find_tool_calls(messages)
 # En option, enregistrez les appels de l'outil -
 #print("Voici mes appels d'outils :")
 #print(appels_outils)
 il = iter (tool_calls)
 attendu = [
 'sql_db_list_tables',
 'sql_db_schema',
 'sql_db_query_checker',
 'sql_db_query',
 'check_result'
 ]
 si tout (elem dedans pour elem est attendu):
 note = 1
 sinon :
 note = 0
 return {"score": int(score), "key": "multi_to
def contient_all_tool_calls_in_order_exact_match(
 root_run : Exécuter, exemple : Exemple
) -> dicté :
 """
 Vérifiez si tous les outils attendus sont appelés en exa
```
ddi i l l ll

```
 appels d'outils supplémentaires.
 """
 attendu = [
 'sql_db_list_tables',
 'sql_db_schema',
 'sql_db_query_checker',
 'sql_db_query',
 'check_result'
 ]
 messages = root_run.outputs["réponse"]
 tool_calls = find_tool_calls(messages)
 # En option, enregistrez les appels de l'outil -
 #print("Voici mes appels d'outils :")
 #print(appels_outils)
 si tool_calls == attendu :
 note = 1
 sinon :
 note = 0
 return {"score": int(score), "key": "multi_to
experience_results = évaluer (
 prédire_sql_agent_messages,
 data=nom_ensemble de données,
 évaluateurs=[
 contient_all_tool_calls_any_order,
 contient_all_tool_calls_in_order,
 contient_all_tool_calls_in_order_exact_ma
```
]

```
 ],
 num_repetitions=3,
)
```
#### *JavaScript*

```
importer {evaluate} depuis 'langsmith/evaluation' ;
// Prédire les messages de l'agent SQL
fonction prédireSqlAgentMessages (exemple) {
 /**
 * Utilisez-le pour l'évaluation des réponses
 */
 const msg = { messages : [{ rôle : "utilisateur", contenu
 // Remplacez par votre graphique et votre configuration
 const messages = graph.invoke(msg, config);
 return { réponse : messages } ;
}
// Rechercher des appels d'outils
fonction findToolCalls({messages}) {
 /**
 * Retrouvez tous les appels d'outils dans les messages renvoyés
 */
 return messages.flatMap(m => m.tool_calls?.map(
}
```

```
// Contient tous les appels d'outils (dans n'importe quel ordre)
la fonction contientAllToolCallsAnyOrder(rootRun, ex
 /**
 * Vérifiez si tous les outils attendus sont appelés dans un
 */
 const attendu = [
 "sql_db_list_tables",
 "sql_db_schema",
 "sql_db_query_checker",
 "sql_db_query",
 "check_result"
 ];
 const messages = rootRun.outputs.response;
 const toolCalls = findToolCalls(messages);
 score const = attendu.every (outil => toolCalls
 return { score, clé : "multi_tool_call_any_order
}
// Contient tous les appels d'outils (dans l'ordre)
la fonction contientAllToolCallsInOrder(rootRun, exa
 /**
 * Vérifiez si tous les outils attendus sont appelés en ex
 */
 const messages = rootRun.outputs.response;
 const toolCalls = findToolCalls(messages);
 const attendu = [
```

```
 "sql_db_list_tables",
 "sql_db_schema",
 "sql_db_query_checker",
 "sql_db_query",
 "check_result"
 ];
 score const = attendu.every(outil => {
 soit trouvé = faux ;
 pour (laisser l'appel de toolCalls) {
 if (appel === outil) {
 trouvé = vrai ;
 pause;
 }
 }
 retour trouvé ;
 }) ? 1 : 0 ;
 return { score, clé : "multi_tool_call_in_order"
}
// Contient tous les appels d'outils (Ordre exact, Ma exact
la fonction contientAllToolCallsInOrderExactMatch(ro
 /**
 * Vérifiez si tous les outils attendus sont appelés en ex
 * appels d'outils supplémentaires.
 */
```

```
 const attendu = [
```

```
 "sql_db_list_tables",
 "sql_db_schema",
 "sql_db_query_checker",
 "sql_db_query",
 "check_result"
 ];
 const messages = rootRun.outputs.response;
 const toolCalls = findToolCalls(messages);
 score const = JSON.stringify(toolCalls) === JSO
 ? 1
 : 0;
 return { score, clé : "multi_tool_call_in_exact_
}
// Résultats de l'expérience
const experienceResults = évaluer (predictSqlAgen
 données : nom de l'ensemble de données,
 évaluateurs : [
 contientAllToolCallsAnyOrder,
 contientAllToolCallsInOrder,
 contientAllToolCallsInOrderExactMatch
 ],
 numRépétitions : 3,
});
```
This implementation example includes the following:

- Invoking a precompiled LangGraph agent graph.invoke with a prompt
- Utilizing a specialized agent where the tools are hardcoded rather than passed with the dataset input
- Extracting of the list of tools called using the function find\_tool\_calls
- Checking if all expected tools are called in any order using the function contains\_all\_tool\_calls\_any\_order or called in order using contains\_all\_tool\_calls\_in\_order
- Checking whether all expected tools are called in the exact order using

```
contient_all_tool_calls_in_order_exact_match
```
<span id="page-529-0"></span>All three of these agent evaluation methods can be observed and debugged in LangSmith's experimentation UI (see [Figure](#page-530-0) 10-16).

<span id="page-530-0"></span>

|  | sql-agent-multi-step-tool-calling-trajecory-in-order-55bd2954 |
|--|---------------------------------------------------------------|
|  |                                                               |

| 1 experiment ▼<br>multi_tool_call_in_ V<br>showing |         |                                        |                                                           | 6 | ->       |   |  |
|----------------------------------------------------|---------|----------------------------------------|-----------------------------------------------------------|---|----------|---|--|
| Input                                              |         | Reference Output                       | sql-agent-multi-step-tool-calling-trajecory-in-order-55bd |   | 7        | p |  |
| How many albums does                               | #36ce + | Led Zeppelin has 14 albums             | 3 REPS >                                                  |   | 0.00 µ   |   |  |
| What was the most purc                             | #4210 → | The most purchased track of 2013 wa    | 3 REPS >                                                  |   | . 0.00 µ |   |  |
| Which sales agent mad                              | #7338 → | Steve Johnson made the most sales i    | 3 REPS >                                                  |   | 0.00 U   |   |  |
| Which country's custo                              | #9372 + | The country whose customers spent t    | 3 REPS >                                                  |   | = 0.00 µ |   |  |
| What is the total price fo                         | #ad01 + | The total price for the album 'Big One | 3 REPS >                                                  |   | . 0.00 µ |   |  |

<span id="page-530-1"></span>Figure 10-16. Example of an agent evaluation test in the LangSmith UI

In general, these tests are a solid starting point to help mitigate an agent's cost and unreliability due to LLM invocations and variability in tool calling.

### Production

<span id="page-530-4"></span><span id="page-530-3"></span><span id="page-530-2"></span>Although testing in the preproduction phase is useful, certain bugs and edge cases may not emerge until your LLM application interacts with live users. These issues can affect latency, as well as the relevancy and accuracy of outputs. In addition, observability and the process of *online evaluation* can help ensure that there are guardrails for LLM inputs or outputs. These guardrails can provide much-needed protection from prompt injection and toxicity.

The first step in this process is to set up LangSmith's tracing feature.

### **Tracing**

<span id="page-531-0"></span>A *trace* is a series of steps that your application takes to go from input to output. LangSmith makes it easy to visualize, debug, and test each trace generated from your app.

Once you've installed the relevant LangChain and LLM dependencies, all you need to do is configure the tracing environment variables based on your LangSmith account credentials:

```
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=<votre-clé-api>
# Les exemples ci-dessous utilisent l'API OpenAI, bien que
export OPENAI_API_KEY=<votre-openai-api-key>
```
Une fois les variables d'environnement définies, aucun autre code n'est requis pour activer le traçage. Les traces seront automatiquement enregistrées <span id="page-532-1"></span>dans leur projet spécifique dans la section « Traçage des projets » du tableau de bord LangSmith. Les mesures fournies incluent le volume de traces, les taux de réussite et d'échec, la latence, le nombre et le coût des jetons, etc., comme le montre la [Figure](#page-532-0) 10-17.

<span id="page-532-0"></span>

| 1% | Équipe LangChain > Projets > 88 chat-langchain-langgraph-cloud |   |   |      |                                          |                  |                               |          |                   |            |
|----------|----------------------------------------------------------------------|---|---|------|----------------------------------------------|------------------|-------------------------------|----------|-------------------|------------|
| D | 88 chat-langchain-langgraph-cloud |   |   |      |                                          |                  | O ID<br>Conservation des données 400d √ |          | 4 Ajouter une règle / Modifier |            |
| 중국 | Exécutions<br>Threads<br>Surveillance<br>Configuration |   |   |      |                                          |                  |                               |          |                   |            |
| Un | Exécutions Root<br>8 7 derniers jours<br>Appels LLM<br>Toutes les exécutions<br>▼ 1 filtre |   |   |      |                                          |                  |                               |          | Colonnes |            |
| 0 | Commencez à comparer Sélectionnez l'une des traces ci-dessous dans le tableau pour commencer à comparer |   |   |      |                                          |                  |                               |          |                   | × |
| 20 |                                                                                | > | 0 | Nom | Entrée | Sortie | Heure de début | Latence | Ensemble de données | Annotations |
| B |                                                                                | > | 0 | discuter | humain : 你会说中文吗 | 《query":"你会说 | 31/07/2024, 9:20:31 | 3 2,63 s | 0<br>0 | 0 % |
| Ô |                                                                                | > | 0 | discuter | humain : pouvez-vous parler | {"query": "pouvez-vous | 31/07/2024, 9:20:15 | 3 2.865 | 00 | 0 % |
|          |                                                                                | > | 0 | discuter | humain : Expliquez multi- {"query": "Expliquez |                  | 31/07/2024, 9:06:39 | © 3.175 | 0<br>0 | 0 % |
|          | > | > | 0 | discuter | humain : j'utilise LAN {"query": "Je suis nous | | 31/07/2024, 9:05:52 | 3 2.944 | = | A<br>0 |
|          | 网站 上海网站 | > | 0 | discuter | humain : j'utilise LAN {"query": Je suis nous |                  | 31/07/2024, 9:05:32 -- | 3 2,694 | 0<br>0 | 02 |
| ்கு<br>0 |                                                                                | > | 0 | discuter | humain : j'utilise LAN {"query": "Je suis nous | | 31/07/2024, 9:05:17 --- | © 3.084 | 0<br>0 | 0 % |
|          |                                                                                | > | 0 | discuter | humain : Langchain est-il un {"query": est lang |                  | 31/07/2024, 9h01-38 | 3,68€ | 0<br>0 | 0 % |
|          |                                                                                | > | 0 | discuter | humain : Qu'est-ce que la {"query": "Qu'est-ce que | | 31/07/2024, 8:56:26 | 3 4.064 | 0<br>0 | 0 % |
|          |                                                                                | 3 | 0 | discuter | humain : 自己的資料(例 《"query":"自己的 | | 31/07/2024, 8:54:58 | @ 11.03s | 0<br>0 | 02 |
| e |                                                                                | > | 0 | discuter | humain : # nDay : précédent | {"query": "# nJour | 31/07/2024, 8:51:46 | 3 6.365 | 00 | 0 % |
| ici |                                                                                | > | 0 | discuter | humain : gemma2b을 | {"query": "gemme | 31/07/2024, 8:51:44 | © 4.255 | D<br>0 | 0 % |
|          | 1 | > | 0 | discuter | humain : 具體作法 | 《"query": "具體作 | 31/07/2024, 8:51:27 -- | 3 7.00s | 0<br>D | 0 % |
|          | 1990 | > | 0 | discuter | humain : 如何鹏文件存 | 《"query": "如何猫 | 31/07/2024, 8:51:15 P | ® 4,99 % | 0<br>0 | 0 % |

Figure 10-17. Un exemple de métriques de performances de trace de LangSmith

Vous pouvez consulter diverses stratégies pour mettre en œuvre le traçage en fonction de vos besoins.

### **Recueillir les commentaires en production**

<span id="page-533-0"></span>Contrairement à la phase de pré-production, les évaluateurs des tests de production ne disposent pas de réponses de référence fondées avec lesquelles le LLM peut comparer. Au lieu de cela, les évaluateurs doivent évaluer les performances en temps réel pendant que votre application traite les entrées des utilisateurs. Cette évaluation en temps réel et sans référence est souvent appelée *évaluation en ligne*.

Il existe au moins deux types de commentaires que vous pouvez collecter en production pour améliorer les performances de l'application :

#### *Commentaires des utilisateurs*

Vous pouvez directement collecter les commentaires des utilisateurs, de manière explicite ou implicite. Par exemple, donner aux utilisateurs la possibilité de cliquer sur un bouton J'aime ou Je n'aime pas ou de fournir des commentaires détaillés basés sur le résultat de l'application est un moyen efficace de suivre la satisfaction des utilisateurs. Dans LangSmith, vous pouvez joindre les commentaires des utilisateurs à n'importe quelle trace ou exécution intermédiaire (c'est-à-dire étendue) d'une trace, y compris l'annotation des traces en ligne ou la révision des exécutions ensemble dans une file d'attente d'annotations.

#### *Commentaires des évaluateurs du LLM-as-a-juge*

Comme indiqué précédemment, ces évaluateurs peuvent être mis en œuvre directement sur les traces pour identifier les hallucinations et les réponses toxiques.

La section de préproduction précédente expliquait déjà comment configurer l'évaluation automatique de LangSmith dans la section Ensembles de données et expériences du tableau de bord.

### **Classification et marquage**

<span id="page-534-1"></span>Afin de mettre en œuvre des garde-fous efficaces contre la toxicité ou de recueillir des informations sur l'analyse des sentiments des utilisateurs, nous devons créer un système efficace pour étiqueter les entrées des utilisateurs et les sorties générées.

Ce système dépend en grande partie du fait que vous disposez ou non d'un ensemble de données contenant des étiquettes de référence. Si vous n'avez pas d'étiquettes prédéfinies, vous pouvez utiliser l'évaluateur LLM-as-a-juge pour vous aider à effectuer la classification et l'étiquetage en fonction de critères spécifiés.

Si, toutefois, des étiquettes de classification de vérité terrain sont fournies, un évaluateur heuristique personnalisé peut être utilisé pour évaluer la sortie de la chaîne par rapport aux étiquettes de classe de vérité terrain.

### **Surveillance et correction des erreurs**

<span id="page-534-0"></span>Une fois votre application en production, le traçage de LangSmith détectera les erreurs et les cas extrêmes. Vous pouvez ajouter ces erreurs dans votre

tester l'ensemble de données pour une évaluation hors ligne afin d'éviter la récurrence des mêmes problèmes.

Une autre stratégie utile consiste à publier votre application par étapes auprès d'un petit groupe d'utilisateurs bêta avant qu'un public plus large puisse accéder à ses fonctionnalités. Cela vous permettra de découvrir des bogues cruciaux, de développer un ensemble de données d'évaluation solide avec des références de vérité terrain et d'évaluer les performances générales de l'application, y compris le coût, la latence et la qualité des résultats.

## <span id="page-535-0"></span>Résumé

Comme indiqué dans ce chapitre, des tests robustes sont essentiels pour garantir que votre application LLM est précise, fiable, rapide, non toxique et rentable. Les trois étapes clés du développement d'une application LLM créent un cycle de données qui contribue à garantir des performances élevées tout au long de la durée de vie de l'application.

Pendant la phase de conception, la gestion des erreurs dans l'application permet une autocorrection avant que l'erreur n'atteigne l'utilisateur. Les tests de préproduction garantissent que chacune des mises à jour de votre application évite la régression des mesures de performances. Enfin, le suivi de la production rassemble des informations en temps réel et des erreurs d'application qui éclairent le processus de conception ultérieur et les répétitions du cycle.
En fin de compte, ce processus de test, d'évaluation, de surveillance et d'amélioration continue vous aidera à résoudre les problèmes et à itérer plus rapidement et, plus important encore, à fournir un produit auquel les utilisateurs peuvent avoir confiance pour fournir systématiquement les résultats souhaités.

## Chapitre 11. Construire avec les LLM

<span id="page-537-2"></span><span id="page-537-1"></span>L'une des plus grandes questions ouvertes dans le monde des LLM aujourd'hui est de savoir comment les mettre entre les mains des utilisateurs finaux. À certains égards, les LLM constituent en fait une interface informatique plus intuitive que celle qui les a précédés. Ils pardonnent beaucoup plus les fautes de frappe, les lapsus et l’imprécision générale des humains que les applications informatiques traditionnelles. D'un autre côté, la capacité même à gérer des entrées « légèrement décalées » s'accompagne d'une tendance à produire parfois des résultats également « légèrement décalés », ce qui est également très différent des tendances informatiques précédentes.

<span id="page-537-3"></span><span id="page-537-0"></span>En fait, les ordinateurs ont été conçus pour répéter de manière fiable le même ensemble d'instructions avec les mêmes résultats à chaque fois. Au cours des dernières décennies, ce principe de fiabilité a imprégné la conception des interfaces homme-machine (appelées diversement HCI, UX et UI) dans la mesure où bon nombre des constructions habituelles finissent par être inférieures à la moyenne pour une utilisation dans des applications qui s'appuient fortement sur les LLM.

Prenons un exemple : Figma est un logiciel utilisé par les designers pour créer des rendus fidèles de designs pour des sites Web, des applications mobiles, des couvertures de livres ou de magazines, la liste est longue. Comme c'est le cas avec presque tous les logiciels de productivité

(logiciel pour la création d'une sorte de contenu long), son interface est une combinaison des éléments suivants :

- <span id="page-538-1"></span>Une palette d'outils et de *primitives* prédéfinies (blocs de construction fondamentaux), dans ce cas des lignes, des formes, des outils de sélection et de peinture, et bien d'autres encore
- <span id="page-538-0"></span>Un canevas, dans lequel l'utilisateur insère ces éléments de base et les organise dans leur création : une page de site Web, un écran d'application mobile, etc.

Cette interface part du principe que les capacités du logiciel sont connues à l’avance, ce qui est effectivement vrai dans le cas de Figma. Tous les éléments de base et outils ont été codés à l’avance par un ingénieur logiciel. Leur existence était donc connue au moment de la conception de l’interface. Cela semble presque idiot de le souligner, mais il n’en va pas de même pour les logiciels qui font un usage intensif des LLM.

Regardez un traitement de texte (par exemple, Microsoft Word ou Google Docs). Il s'agit d'une application logicielle permettant de créer un contenu textuel de longue durée, tel qu'un article de blog, un article, un chapitre de livre, etc. L'interface à notre disposition ici est également constituée d'une combinaison familière :

- Une palette d'outils et de *primitives* prédéfinies : dans le cas d'un traitement de texte, les primitives disponibles sont des tableaux, des listes, des titres, des espaces réservés pour les images, etc., et les outils sont la vérification orthographique, les commentaires, etc.
- *Un canevas* : dans ce cas, il s'agit littéralement d'une page blanche, où l'utilisateur tape des mots et peut inclure certains des éléments qui viennent d'être mentionnés.

Comment cette situation changerait-elle si nous devions construire un traitement de texte LLMnative ? Ce chapitre explore trois réponses possibles à cette question, qui sont largement applicables à toute application LLM. Pour chacun des modèles que nous explorons, nous passerons en revue les concepts clés dont vous auriez besoin pour le mettre en œuvre avec succès. Nous ne voulons pas dire que ce sont les seuls, il faudra un certain temps avant que la poussière retombe sur cette question particulière.

Examinons chacun de ces modèles, en commençant par le plus simple à ajouter à une application existante.

## Chatbots interactifs

<span id="page-539-0"></span>Il s'agit sans doute de l'ascenseur le plus simple à ajouter à une application logicielle existante. Dans sa conception la plus élémentaire, cette idée s'appuie simplement sur un compagnon d'IA (pour faire rebondir les idées), tandis que tout le travail se déroule toujours dans l'interface utilisateur existante de l'application. Un

<span id="page-540-3"></span><span id="page-540-1"></span>exemple voici GitHub Copilot Chat, qui peut être utilisé dans une barre latérale à l'intérieur de l'éditeur de code VSCode.
Une mise à niveau de ce modèle consiste à ajouter quelques points de communication entre l'extension AI Sidekick et l'application principale. Par exemple, dans VSCode, l'assistant peut « voir » le contenu du fichier en cours d'édition ou toute partie de ce code sélectionnée par l'utilisateur. Et dans l'autre sens, l'assistant peut insérer ou modifier du texte dans cet éditeur ouvert, aboutissant ainsi à une forme de collaboration de base entre l'utilisateur et le LLM.

#### **REMARQUE**

<span id="page-540-2"></span>Le chat en streaming tel que nous le décrivons ici est actuellement l'application prototypique des LLM. C'est presque toujours la première chose que les développeurs d'applications apprennent à développer au cours de leur parcours LLM, et c'est presque toujours la première chose que les entreprises recherchent lorsqu'elles ajoutent des LLM à leurs applications existantes. Cela restera peut-être le cas dans les années à venir, mais un autre résultat possible serait que le chat en streaming devienne la ligne de commande de l'ère LLM, c'est-à-dire la plus proche de l'accès direct à la programmation, devenant ainsi une interface de niche, tout comme elle l'a fait pour les ordinateurs.

<span id="page-540-0"></span>Pour créer le chatbot le plus basique, vous devez utiliser ces composants :

*Un modèle de chat*

<span id="page-541-0"></span>Leur réglage des dialogues se prête bien aux interactions multitours avec un utilisateur. Reportez-vous à la [Préface](#page-8-0) pour en savoir plus sur le réglage des dialogues.

*Historique des conversations*

<span id="page-541-2"></span>Un chatbot utile doit être capable de « dépasser le bonjour ». Autrement dit, si le chatbot ne peut pas se souvenir des entrées précédentes de l'utilisateur, il sera beaucoup plus difficile d'avoir des conversations significatives avec lui, qui font implicitement référence aux messages précédents.

Pour aller au-delà des bases, vous ajouteriez probablement ce qui suit :

#### *Sortie en streaming*

<span id="page-541-4"></span><span id="page-541-3"></span><span id="page-541-1"></span>Les meilleures expériences de chatbot diffusent actuellement la sortie LLM jeton par jeton (ou en morceaux plus grands, comme des phrases ou des paragraphes) directement à l'utilisateur, ce qui atténue la latence inhérente aux LLM actuels.

#### *Appel de l'outil*

<span id="page-541-5"></span>Pour donner au chatbot la possibilité d'interagir avec le canevas principal et les outils de l'application, vous pouvez les exposer en tant qu'outils que le modèle peut décider d'appeler, par exemple, un outil « obtenir le texte sélectionné » et un outil « insérer du texte à la fin du document ».

#### *L'humain dans la boucle*

<span id="page-542-1"></span>Dès que vous donnez au chatbot des outils qui peuvent modifier le contenu du canevas de l'application, vous créez le besoin de redonner un certain contrôle à l'utilisateur, par exemple en lui permettant de confirmer, voire de modifier, avant d'insérer un nouveau texte.

## Édition collaborative avec les LLM

<span id="page-542-0"></span>La plupart des logiciels de productivité intègrent une forme d'édition collaborative, que nous pouvons classer dans l'une de ces catégories (ou quelque part entre les deux) :

#### *Enregistrer et envoyer*

<span id="page-542-2"></span>Il s'agit de la version la plus basique, qui ne prend en charge qu'un seul utilisateur modifiant le document à la fois, avant de "refiler la responsabilité" à un autre utilisateur (par exemple, en envoyant le fichier par e-mail) et en répétant le processus jusqu'à ce que ce soit terminé. L’exemple le plus évident est la suite d’applications Microsoft Office : Excel, Word, PowerPoint.

#### *Contrôle de version*

<span id="page-542-3"></span>Il s'agit d'une évolution de la sauvegarde et de l'envoi qui prend en charge plusieurs éditeurs travaillant simultanément de manière indépendante (et ignorant les modifications des autres) en fournissant des outils pour combiner leur travail par la suite : stratégies de fusion (comment combiner des modifications non liées) et résolution de conflits (comment combiner des modifications incompatibles). L'exemple le plus populaire aujourd'hui est Git/GitHub, utilisé par les ingénieurs logiciels pour collaborer sur des projets logiciels.

#### *Collaboration en temps réel*

<span id="page-543-1"></span>Cela permet à plusieurs éditeurs de travailler sur le même document en même temps, tout en voyant les modifications des uns et des autres. Il s’agit sans doute de la forme la plus naturelle de collaboration logicielle, comme en témoigne la popularité de Google Docs et Google Sheets parmi les utilisateurs d’ordinateurs techniques et non techniques.

Ce modèle d'expérience utilisateur LLM consiste à employer un agent LLM comme l'un de ces « utilisateurs » contribuant à ce document partagé. Cela peut prendre plusieurs formes, notamment les suivantes :

- <span id="page-543-0"></span>Un "copilote" toujours actif vous donnant des suggestions sur la façon de compléter la phrase suivante
- Un "rédacteur" asynchrone, que vous chargez, par exemple, de partir faire des recherches sur le sujet en question et de revenir plus tard avec une section que vous pourrez intégrer dans votre document final

Pour construire cela, vous aurez probablement besoin des éléments suivants :
#### *État partagé*

<span id="page-544-1"></span>L'agent LLM et les utilisateurs humains devraient être sur le même pied en termes d'accès et de compréhension de l'état du document ; c'est-à-dire qu'ils seraient capables d'analyser l'état du document et de produire des modifications sur cet état dans un format compatible.

#### *Gestionnaire de tâches*

<span id="page-544-2"></span>Produire une modification utile du document sera invariablement un processus en plusieurs étapes, qui peut prendre du temps et échouer à mi-chemin. Cela crée le besoin d'une planification et d'une orchestration fiables des tâches de longue durée, avec mise en file d'attente, récupération des erreurs et contrôle des tâches en cours d'exécution.

#### *Fusion des fourches*

<span id="page-544-0"></span>Les utilisateurs continueront à modifier le document après avoir chargé l'agent LLM. Les sorties LLM devront donc être fusionnées avec le travail des utilisateurs, soit manuellement par l'utilisateur (une expérience comme Git), soit automatiquement (via des algorithmes de résolution de conflits tels que CRDT et la transformation opérationnelle (OT), utilisés par des applications telles que Google Docs).

#### *Concurrence*

<span id="page-545-3"></span>Le fait que l'utilisateur humain et l'agent LLM travaillent sur la même chose en même temps nécessite la capacité de gérer les interruptions, les annulations, les réacheminements (faites ceci à la place) et les files d'attente (faites cela également).

#### *Annuler/rétablir la pile*

<span id="page-545-5"></span>Il s'agit d'un modèle omniprésent dans les logiciels de productivité, qui est inévitablement nécessaire ici aussi. Les utilisateurs changent d'avis et souhaitent revenir à un état antérieur du document, et l'application LLM doit être capable de les suivre là-bas.

#### *Sortie intermédiaire*

<span id="page-545-4"></span><span id="page-545-2"></span>La fusion des résultats utilisateur et LLM est beaucoup plus facile lorsque ces résultats sont progressifs et arrivent au coup par coup dès qu'ils sont produits, de la même manière qu'une personne écrit une page de 10 paragraphes, une phrase à la fois.

## Informatique ambiante

<span id="page-545-1"></span><span id="page-545-0"></span>Un modèle UX très utile est le logiciel d'arrière-plan toujours actif qui s'affiche lorsque quelque chose d'« intéressant » a lieu.

s'est produit et mérite votre attention. Vous pouvez trouver cela dans de nombreux endroits aujourd'hui. Quelques exemples sont :

- Vous pouvez définir une alerte dans votre application de courtage pour vous avertir lorsqu'une action descend en dessous d'un certain prix.
- Vous pouvez demander à Google de vous avertir lorsque de nouveaux résultats de recherche correspondant à une requête de recherche sont trouvés.
- Vous pouvez définir des alertes pour votre infrastructure informatique afin de vous avertir lorsque quelque chose sort du comportement habituel.

Le principal obstacle au déploiement plus large de ce modèle pourrait être de parvenir à l'avance à une définition fiable de *intéressant* qui soit à la fois :

#### *Utile*

Il vous avertira lorsque vous le jugerez nécessaire.

#### *Pratique*

La plupart des utilisateurs ne voudront pas passer énormément de temps à pré-créer des règles interminables pour les alertes.

Les capacités de raisonnement des LLM peuvent débloquer de nouvelles applications de ce modèle d'*informatique ambiante* qui sont en même temps plus utiles (elles identifient davantage ce que vous trouveriez intéressant)

et moins de travail à mettre en place (leur raisonnement peut remplacer une grande partie ou la totalité de la configuration manuelle des règles).

La grande différence entre *collaborative* et *ambient* est la concurrence :

#### *Collaboratif*

Vous et le LLM travaillez généralement (ou parfois) en même temps et vous nourrissez mutuellement du travail de chacun.

#### *Ambiance*

Le LLM effectue continuellement une sorte de travail en arrière-plan pendant que vous, l'utilisateur, faites probablement autre chose.

Pour construire cela, vous avez besoin de :

#### *Déclencheurs*

<span id="page-547-0"></span>L'agent LLM doit recevoir (ou interroger périodiquement) de nouvelles informations de l'environnement. C’est d’ailleurs ce qui motive l’informatique ambiante : une source préexistante de nouvelles informations périodiques ou continues qui doivent être traitées.

*Mémoire à long terme*

<span id="page-548-1"></span>Il ne serait pas possible de détecter de nouveaux événements intéressants sans consulter une base de données d'informations reçues précédemment.

#### *Réflexion (ou apprentissage)*

<span id="page-548-3"></span>Comprendre ce qui est *intéressant* (ce qui mérite une contribution humaine) nécessite probablement d'apprendre de chaque événement intéressant précédent après qu'il se soit produit. C'est ce qu'on appelle généralement une *étape de réflexion*, dans laquelle le LLM produit une mise à jour de sa mémoire à long terme, modifiant éventuellement ses « règles » internes pour détecter de futurs événements intéressants.

#### *Résumer le résultat*
<span id="page-548-2"></span>Un agent travaillant en arrière-plan est susceptible de produire beaucoup plus de résultats que ce que l'utilisateur humain souhaiterait voir. Cela nécessite que l'architecture de l'agent soit modifiée pour produire des résumés du travail effectué et présenter à l'utilisateur uniquement ce qui est nouveau ou remarquable.

#### *Gestionnaire de tâches*

<span id="page-548-4"></span><span id="page-548-0"></span>Le fait qu'un agent LLM travaille continuellement en arrière-plan nécessite l'emploi d'un système pour gérer le travail, mettre en file d'attente les nouvelles exécutions, ainsi que gérer et récupérer des erreurs.

## Résumé

Les LLM ont le potentiel de changer non seulement la façon dont nous construisons [les logiciels, mais](https://oreil.ly/RqnCm) également les logiciels mêmes que nous construisons. Cette nouvelle capacité dont nous disposons, les développeurs, pour générer du nouveau contenu améliorera non seulement de nombreuses applications existantes, mais elle peut également rendre possibles de nouvelles choses dont nous n'avons pas encore rêvé.

Il n'y a pas de raccourci ici. Vous avez vraiment besoin de créer quelque chose de merdique, de parler aux utilisateurs, de rincer et de répéter jusqu'à ce que quelque chose de nouveau et d'inattendu sorte de l'autre côté.

Avec ce dernier chapitre, et le livre dans son ensemble, nous avons essayé de vous donner les connaissances qui, selon nous, peuvent vous aider à construire quelque chose d'uniquement bon avec les LLM. Nous tenons à vous remercier d’avoir entrepris ce voyage avec nous et vous souhaitons la meilleure des chances dans votre carrière et votre avenir.

## Indice

### **Symboles**

{} (accolades), Création d'invites LLM [Réutilisable](#page-63-0)

#### **A**

abstractions, [LangChain](#page-33-0) et Pourquoi il est important [agence, cognitif](#page-322-0) [Architectures](#page-278-0) avec LangGraph, La boucle Plan-Do, [Patterns](#page-385-1) pour tirer le meilleur parti du compromis agence-fiabilité des LLM, Architectures cognitives avec [LangGraph, Patterns](#page-278-1) pour tirer le meilleur parti des LLM-Patterns pour tirer le meilleur parti des abstractions d'agent de l'architecture d'agent LLM, [LangChain](#page-35-0) et pourquoi il est important de toujours appeler les outils en premier, [Toujours](#page-332-0) Appeler un outil en premier-[Toujours](#page-342-1) Appeler un outil D'abord traiter de nombreux outils, [Dealing](#page-342-2) avec de nombreux [Outils-Dealing](#page-352-0) avec de nombreux outils Création d'agent LangGraph, Construction d'un [LangGraph](#page-323-0) Agent-Construction d'un [LangGraph](#page-332-1) Architectures multi-agents d'agent, Multi-Agent [Architectures-](#page-374-0)Superviseur [Architecture,](#page-383-0) [Multitâche](#page-417-0) Boucle plan-faire des LLM, La boucle [Plan-Do](#page-318-0) - La boucle [Plan-Do](#page-322-1)

technique d'incitation à la réflexion, [Réflexion](#page-354-0)[-Réflexion](#page-366-0) aspects uniques des agents [Architecture](#page-315-1), évaluation des performances de la [réponse, Test](#page-516-0) finale d'un agent [réponse](#page-508-1) -Test d'une seule étape des niveaux d'un agent de [test, Évaluation](#page-506-0) des performances de bout en bout d'un agent, [Test](#page-516-1) une seule étape d'un [agent-Testing](#page-520-0) une seule étape d'un agent [trajectoire, Test](#page-530-1) une [trajectoire-](#page-520-1)Test d'un agent chatbots IA de trajectoire (voir chatbots) Interface AIMessage, Utilisation des LLM dans les alertes [LangChain](#page-57-0), Algorithmes Ambient [Computing](#page-545-0), [Préface](#page-9-0) informatique ambiante, Ambient [Computing](#page-545-1) [Anthropique, P](#page-47-0)[refac](#page-10-0)[e, L](#page-47-0)[angChain](#page-34-0) et pourquoi c'est important, principes fondamentaux du LLM avec accès à l'API LangChain, protection, [Sécurité](#page-466-0) clés API, récupération, grande application de modèle [Langue](#page-427-1) logs, [Création](#page-487-0) Architecture des jeux de données (voir aussi architecture des agents ; architectures cognitives)

ReAct [architecture, L](#page-322-2)[angChain](#page-35-1) et pourquoi c'est important, le routeur Plan-Do Loop [architecture, A](#page-313-0)[rchitecture](#page-298-0) #3 : Architecture de routeur #3 : Réseau neuronal de transformateur de routeur [architecture, Brief](#page-16-1) Introduction aux LLM

ArcSearch, [Présentation](#page-244-0) LangGraph argument k, Récupération des [Documents](#page-173-0) assistant [rôle,](#page-55-0) [Dialogue-Tuned](#page-20-0) LLM, Utilisation des LLM dans les assistants LangChain (voir chatbots) assistants (LangGraph Platform), [Assistants](#page-442-0) exécution asynchrone, Utilisation de l'authentification de l'interface [Runnable](#page-80-0), [Sécurité](#page-467-0) mode d'autorisation, [Human-in-the-Loop](#page-408-1) Modalités [auto-évaluateurs, ajout, amélioration](#page-497-0) Performance des évaluateurs LLM-as-a-juge autonomie, Cognitive [Architectures](#page-279-0) avec [LangGraph, Patterns](#page-387-0) pour tirer le meilleur parti des LLM

#### **B**
modèle sac de mots, [Embeddings](#page-100-0) Avant les LLM Bard, [Préface](#page-10-1) méthode par lots, Utilisation de l'interface [Runnable](#page-77-0), [Résumé](#page-91-0) BLOOM, Brief [Primer](#page-13-1) sur les accolades LLM, bouclés ({}), Création d'invites LLM [Réutilisable](#page-63-0)

#### **C**

toiles, [Bâtiment](#page-538-0) avec LLM

chaîne [architecture,](#page-298-1) [Architecture](#page-289-1) #2 : Chaîne-Architecture #2 :

Chaîne

invite de chaîne de pensée (CoT), [Chaîne de pensée] (#page-25-1),

[LangChain](#page-35-2) et pourquoi c'est important, agent [Architecture](#page-316-0)

Chase, Harrison, [Préface](#page-10-2)

ensemble de données de discussion, [Création](#page-489-0) Ensembles de données

modèles de discussion

fournisseurs LLM alternatifs pour, LLM [Fundamentals](#page-47-1) avec

LangChaîne

chatbots interactifs, [Interactif](#page-541-0) Chatbots

interfaces de message dans, Utilisation des LLM dans [LangChain](#page-56-0)

rôles dans, Utilisation des LLM dans [LangChain](#page-54-0)

chatbots

ajouter de la mémoire aux chatbots, Ajouter de la mémoire à

[StateGraph-Adding](#page-257-1) Mémoire vers [StateGraph](#page-262-0)

composants avancés, [Interactif](#page-541-1) Chatbots

exécution asynchrone de, Impératif [Composition](#page-86-0)

composants de base, [Interactif](#page-540-0) Chatbots

création de mémoire de chatbot [systèmes, Création](#page-238-1) d'un système de mémoire de chatbot[-Construction](#page-242-0) d'un système de mémoire de chatbot ChatGPT, [Préface](#page-8-1) historique de conversation, [Modification](#page-262-1) Historique de discussion-[Résumé](#page-276-0), [Interactif](#page-541-2) Chatbots interactifs, [Interactif](#page-539-0) Limitation des chatbots simples, RAG Partie I : [Indexation](#page-93-1) Votre mémoire de données et, [LangChain](#page-35-3) et Pourquoi il est important de modifier l'historique des discussions, [Modification](#page-262-1) Historique des discussions[-Résumé](#page-276-0) aperçu de la création, Que faire [Attendez](#page-37-0) de l'invite de ce livre et exemple de modèle de discussion [de, Impératif](#page-81-1) Composition

prise en charge du streaming avec Python ou [JavaScript, Impératif](#page-84-0)

Composition

ChatGPT, [Préface](#page-8-1)

Interface ChatMessage, Utilisation des LLM dans [LangChain](#page-57-1)

[ChatPromptTemplate, Making](#page-71-0) Invites LLM [Réutilisable-](#page-66-0)Obtention de formats spécifiques à partir des LLM

événements de point de contrôle, [Intermédiaire](#page-400-0) Sortie

points de contrôle, ajout de mémoire à [StateGraph](#page-257-2)[, Human-in-the-](#page-403-0)Modalités de boucle

problèmes de classification, [Embeddings](#page-100-1) Avant les LLM

Claude, [Préface](#page-10-3)

exemples de code, obtention et utilisation, Utilisation du code [Exemples](#page-40-0)

architectures cognitives

chaîne [architecture,](#page-298-1) [Architecture](#page-289-1) #2 : Chaîne-Architecture #2 : Chaîne

définition de [terme, Cognitif](#page-279-1) Architectures avec

LangGraph

Architecture de l'appel LLM, [Architecture](#page-283-0) #1 : Appel LLM-

[Architecture](#page-289-2) #1 : Appel LLM

majeur LLM [architectures, Cognitive](#page-280-2) Architectures avec

LangGraph

routeur [architecture, A](#page-313-0)[rchitecture](#page-298-0) #3 : Routeur-Architecture

#3 : Routeur

Cohere, LLM [Fundamentals](#page-47-2) avec [LangChain, Generating](#page-122-0) Intégrations de texte

Modèle ColBERT, ColBERT : Optimisation des [Embeddings](#page-157-1)

édition collaborative, [Collaborative](#page-542-0) Édition avec LLM-

[Collaboratif](#page-545-2) Édition avec les LLM

commentaires et questions, Comment nous [Contacter](#page-42-0)

composition (voir composition déclarative ; impératif

composition)

simultanéité, [Collaboratif](#page-545-3) Édition avec les LLM

entrées concurrentes, traitement, Refuser les entrées [concurrentes](#page-418-0)-

Fork et [fusionner](#page-422-0)

contexte

sortie précise avec, L'objectif : Choisir un contexte pertinent pour les LLM, Présentation de la [Récupération-Augmentée](#page-95-0) Génération traitant d'[Architectures] multi-agents complexes (#page-374-1)

définition du terme, [Récupération-Augmentée](#page-27-0) Fenêtres contextuelles de génération, Conversion de vos [Documents](#page-113-0) en texte, [Découpage](#page-262-2) Messages
cycle continu d'[amélioration](#page-471-1), techniques de test tout au long du cycle de développement d'applications LLM (voir aussi tests), historique des conversations, [interactif](#page-541-2) copilotes de chatbots, [collaboratif](#page-543-0) édition avec la similarité cosinus des LLM, sémantique [Incorporations](#page-106-0) expliqué, récupération pertinente [Documents](#page-169-0) Invite CoT (voir invite de chaîne de pensée) [créer, lire, mettre à jour, supprimer](#page-129-1) (CRUD), stockage des intégrations dans un magasin de vecteurs tâches cron (plateforme LangGraph), [Cron](#page-443-0) tâches au format CSV, autres [lisibles par machine](#page-75-0) Formats avec analyseurs de sortie curly accolades ({}), création d'invites LLM [réutilisables](#page-63-0)

événements actuels, RAG Partie I : [Indexation](#page-94-0) Vos données, Présentation de la [Récupération-Augmentée](#page-164-1) Génération

**D**

indexation des données

conversion de documents en texte, Conversion de vos documents en [Conversion de texte](#page-109-0) Vos [Documents](#page-114-0) en intégrations de texte, [Incorporations :](#page-97-0) Conversion de texte en nombres - Conversion de vos [Documents](#page-109-0) en exemple de texte de bout en bout, Génération de texte [Embeddings-](#page-125-0)Génération de texte [Embeddings](#page-128-0) génération d'incorporations de texte, Génération de texte [Embeddings-](#page-122-1)Génération de texte [Embeddings](#page-125-1) limites des connaissances de LLM [corpus, RAG](#page-93-1) Partie I : Indexation de vos données optimisation, indexation [Optimisation](#page-147-0)-[Résumé](#page-161-1) processus de, Récupération des [Documents](#page-166-0) du contenu pertinent pour les LLM, L'objectif : Choisir le contexte pertinent pour les [LLM, Récupération](#page-94-1) [Documents] pertinents (#page-166-1) -Générer le LLM [Prédictions](#page-184-0) Utilisation de documents pertinents pour diviser le texte en morceaux, [Diviser](#page-114-1) Votre texte en morceaux-[Splitting](#page-122-2) Votre texte en morceaux stockant les intégrations dans des magasins de vecteurs, Stockage des intégrations dans un vecteur [Store-Working](#page-128-1) avec les magasins de vecteurs pour suivre les modifications apportées aux documents, suivre les modifications apportées à votre [Documents-Tracking](#page-138-1) Modifications apportées à vos modèles de données [Documents](#page-147-1) (plateforme LangGraph), données [Modèles](#page-441-0) requêtes de données

construction de requête, Requête [Construction](#page-224-1)-[Text-to-SQL](#page-234-0)

routage des requêtes, Requête [Routage](#page-211-0)[-Sémantique](#page-223-0) Routage

transformation de requête, Requête [Transformatio](#page-184-1)[n-Hypothetical](#page-211-1) Incorporations de documents

accès à la base de données, protection, [Sécurité](#page-466-1)

description de la base de données, [Text-to-SQL](#page-230-1)

ensembles de données

[création,](#page-492-1) [Création](#page-486-0) Ensembles de données – Définition de vos critères d'évaluation

ensembles de données de dialogue, [Dialogue-Tuned](#page-20-1) LLM

ensembles de données spécifiques à une tâche, [Instruction-Tuned](#page-18-0) LLM

mode débogage (LangGraph), [Intermédiaire](#page-400-1) Sortie

composition déclarative, Utilisation de l'interface [Runnable](#page-80-1),

Déclarative [Composition](#page-87-0)[-Résumé](#page-91-1)

défense en profondeur, [Sécurité](#page-465-0)

intégrations denses, basées sur LLM [Embeddings](#page-102-1)

dépendances, installation, Installer [Dépendances](#page-425-0)

déploiement

Fichier API LangGraph [configuration](#page-448-0), Créer une configuration d'API LangGraph

LangGraph [Studio, Lancement](#page-464-0) [LangGraph](#page-460-1) Lancement de Studio LangGraph Studio

à partir de l'interface utilisateur de LangSmith, déployer à partir de l'interface utilisateur de [LangSmith](#page-455-0) -

Variables [Environnement](#page-459-0)

prérequis, [Prérequis-](#page-424-1)Créer un compte [LangSmith](#page-441-1)

considérations de sécurité, [Sécurité](#page-464-1)

tester l'application LangGraph localement, Testez votre application LangGraph

[Localement-Test](#page-450-0) Votre application [LangGraph](#page-455-1) localement

phase de conception, tests pendant, La phase de conception : [Auto-correction](#page-472-0)

RAG-L'étape de conception : [Auto-correction](#page-486-1) RAG

réglage du dialogue, [Dialogue-Tuned](#page-19-0) LLM

dimensions, basé sur LLM [Embeddings](#page-102-2)

chargeurs de documents, Conversion de vos [Documents](#page-109-1) en documents texte

classification, [Embeddings](#page-100-1) Avant les LLM

[découplage, M](#page-156-1)[ultiVectorRetrieve](#page-147-2)[r-RAPTOR:](#page-156-1) Récursif

Traitement abstractif pour la récupération organisée par arborescence

suppression, suivi des modifications apportées à vos [documents](#page-139-0)

[prétraitement, The](#page-95-1) Objectif : choisir un contexte pertinent pour les LLM

reclassement/réorganisation, [RAG-Fusion](#page-199-0)

récupérer les [documents, Récupérer](#page-166-2) pertinents

Documents-Récupération de [Documents] pertinents (#page-174-0)
suivi des modifications apportées aux documents, suivi des modifications apportées à votre

[Documents-Tracking](#page-138-1) Modifications apportées à vos [Documents](#page-147-1)

double envoi de SMS (LangGraph Platform), [Double](#page-446-0) envoi de SMS

dérive, [Régression](#page-503-1) Test

DuckDuckGo, création d'un agent [LangGraph](#page-323-1)

invite dynamique de quelques prises de vue, Quelques prises de vue [Invite](#page-32-0)

entrées dynamiques, Création d'invites LLM [Réutilisable](#page-60-0)

#### **E**

bords, [Présentation](#page-248-0) Édition LangGraph, collaborative, [Collaborative](#page-542-0) Édition avec LLM-[Collaborative](#page-545-2) Édition avec des modèles d'intégration LLM, [LangChain](#page-35-4) et Pourquoi c'est important, Fondamentaux LLM avec [LangChain, Basé sur LLM](#page-47-3) [Embeddings](#page-102-3) modèle de sac de mots d'incorporation, [Embeddings](#page-100-0) Avant les avantages du LLM, [Embeddings:](#page-97-1) Conversion de texte en nombres [définition](#page-97-2) du terme, l'objectif : choisir un contexte pertinent pour les LLM générer des intégrations de texte, Générer du texte [Embeddings-](#page-122-1)Générer du texte [Embeddings](#page-125-1) intégrations basées sur LLM, optimiser des [Embeddings] basés sur LLM (#page-101-0), ColBERT : optimiser les [Embeddings](#page-157-1) récupérer les [embeddings pertinents, Récupération](#page-172-0) Documents pertinents incorporations sémantiques, [Embeddings sémantiques](#page-103-0) Explication-Sémantique [Embeddings](#page-106-1) Explication du stockage des incorporations dans des magasins de vecteurs, Stockage des incorporations dans un vecteur [Store-Working](#page-128-1) avec des magasins de vecteurs

utilise [for, E](#page-107-0)[mbeddings](#page-98-0) Avant les LLM, les intégrations sémantiques expliquées

variables d'environnement, gestion des erreurs des variables [Environnement](#page-457-0), étape de conception : [Auto-correction](#page-472-1) erreurs RAG, surveillance, [Surveillance](#page-534-0) et métriques d'évaluation de correction des erreurs (voir aussi les tests)

définir, Définir votre [évaluation](#page-492-2) Critères pour démarrer, Définir votre [évaluation](#page-494-0) Critères d'amélioration du LLM-en tant que juge [performance, Amélioration](#page-495-1) Évaluateurs LLM en tant que juge [amélioration de la performance](#page-501-1) Performance des évaluateurs LLM-en tant que juge principal évaluateurs, Définir votre [évaluation](#page-493-1) Critères d'évaluation par paire, [Evaluation] par paire(#page-502-0) résultat attendu, Brief [Amorce](#page-17-0) sur les LLM externes [données, récupération, L'](#page-95-2) Objectif : Choisir un contexte pertinent pour les LLM

### **F**

[commentaires, collecte](#page-533-0) en production, recueillir les commentaires en production, invite à quelques tirs, quelques coups [Invite](#page-32-1), [Text-to-SQL](#page-230-2), amélioration de [LLM-as-a-judge](#page-496-0) performances des évaluateurs, accès aux fichiers, protection, [Sécurité](#page-466-2)

réponse finale, évaluation, Test de la [réponse-](#page-508-1)[Testing](#page-516-0) finale d'un agent une seule étape d'un agent

mise au point

ensembles de données de dialogue, [Dialogue-Tuned](#page-20-2) LLM

LLM affinés, [Fine-Tuned](#page-21-0) LLM

valeurs à virgule flottante, sémantique [Embeddings](#page-104-1) expliqué

ingénierie des flux, [Architecture](#page-289-3) #2 : Chaîne

stratégie de fork et de fusion, Fork et [merge](#page-421-0)

formats

[lisible par machine, Autre](#page-75-0) Formats lisibles par machine avec

Analyseurs de sortie

fourniture de format [instructions, Autre](#page-75-1) Formats lisibles par machine avec analyseurs de sortie

spécification à partir des LLM, obtention de formats spécifiques à partir de

LLM-Autres formats [lisibles par machine](#page-71-1) avec sortie

Analyseurs

frontières, [Modèles](#page-386-2) pour tirer le meilleur parti des appels de fonctions LLM, [Routage] logique (#page-213-0)

### **G**

Gemma, brève introduction sur [Invite](#page-22-0)[, LangChain](#page-34-1) et pourquoi c'est important

boucle générer-réfléchir, [Réflexion](#page-363-0)

génération [étape, Génération](#page-175-1) Prédictions LLM utilisant des

Documents

IA générative

débuts de, [Préface](#page-9-1)

Algorithmes LLM versus ML, [Préface](#page-9-2)

Chat copilote GitHub, [Interactif](#page-540-1) Chatbots

Google

Gémeaux, [Préface](#page-10-1)

Intégration de LangChain [avec, LangChain](#page-34-0) et pourquoi c'est

Important

graphiques, [Présentation](#page-243-1) Références de vérité terrain LangGraph (voir aussi LangGraph), Définition de vos critères d'[évaluation](#page-493-2)

#### **H**
hallucinations, RAG Partie I : [Indexation](#page-94-2) Vos données, ColBERT : Optimisation des intégrations, Requête [Transformation, Trimmi](#page-158-1)ng Messages, Test : [Évaluation, Surveillance et](#page-262-3) Évaluateurs heuristiques d'amélioration continue, Définition de votre [Évaluation](#page-493-3) Critères hiérarchiques Navigable Small World [\(HNSW\), Récupération](#page-172-0) Documents pertinents Étreignant le visage, Génération de texte [Intégrations](#page-122-3) évaluateurs humains, Définition de votre [Évaluation](#page-493-4) Critères d'interfaces homme-machine (HCI), [Construction](#page-537-0) avec des LLM

mode d'autorisation des modalités human-in-the-loop, [Human-in-the-Loop](#page-408-1) points de contrôle des modalités, [Human-in-the-Loop](#page-403-0) état d'édition des modalités, Modifier [state](#page-414-0) étape de fork, [Fork](#page-415-0) chatbots interactifs et, [Interactif](#page-542-1) Mode interruption des chatbots, [Human-in-the-Loop](#page-404-0) Modalités API de la plateforme LangGraph, [Human-in-the-loop](#page-445-0) étape de redémarrage, [Redémarrer](#page-412-1) étape de reprise, [Resume](#page-411-1) Interface HumanMessage, Utilisation des LLM dans [LangChain](#page-57-2) Embeddings de documents hypothétiques (HyDE), Document hypothétique [Embeddings-Hypothetical](#page-205-1) Embeddings de documents

### **Je**

composition impérative, Utilisation de l'interface [Runnable](#page-80-2) - Impératif [Composition,](#page-86-1) [Résumé](#page-91-2) inexactitudes, RAG Partie I : [Indexation](#page-94-3) Agents indépendants de vos données, Indexation multi-agents [Architectures](#page-374-2) (voir indexation des données ; index vectoriels) ingestions, l'objectif : choisir [pertinent] (#page-97-3) le contexte pour le format de discussion d'entrée des LLM et, [Dialogue-Tuned](#page-20-3) les entrées dynamiques des LLM, rendre les invites LLM [réutilisables](#page-60-0)

gestion simultanée, [Multitâche](#page-417-1) LLM-Fork et [fusion](#page-422-0) dans les LLM par rapport à l'apprentissage automatique, Brief [Primer](#page-17-0) sur le rôle des LLM dans les LLM, Brief [Primer](#page-12-1) sur le réglage des instructions des LLM, [Instruction-Tuned](#page-18-1) LLM interactifs chatbots, Sortie LLM en streaming [Jeton par jeton,](#page-400-2) [Interactif](#page-539-0) Sortie intermédiaire des Chatbots (voir aussi chatbots), [Intermédiaire](#page-395-0) Sortie-Intermédiaire [Sortie, Collaborative](#page-400-3) Édition avec le mode d'interruption des LLM, [Human-in-the-Loop](#page-404-0) Stratégie d'interruption des modalités, [Interruption](#page-419-0) méthode d'invocation, Utilisation des LLM dans [LangChain](#page-53-0)[, Rendre](#page-63-1) Les invites LLM réutilisables, Utilisation de l'interface [Runnable](#page-77-1), [Résumé](#page-91-0)

### **J**

jailbreaking, [Dialogue-Tuned](#page-20-4) Implémentation de l'architecture d'agent JavaScript LLM, Construction d'un [LangGraph](#page-325-0) sous-agents d'agent, Superviseur [Architecture](#page-381-0) superviseur, Superviseur [Architecture](#page-378-0) exécution asynchrone avec, Impératif [Composition](#page-86-2) conversation chatbot [configuration, Utilisation](#page-56-1) LLM dans les bords du chatbot LangChain, ajout, création d'un [StateGraph](#page-254-0)

mémoire de chatbot [systèmes, bâtiment](#page-240-0) un système de mémoire de chatbot

nœuds de chatbot, ajout, création d'un [StateGraph](#page-252-0)

Prise en charge du streaming chatbot, Impératif [Composition,](#page-85-0)

Déclarative [Composition](#page-90-0)

ChatPromptTemplate, Création d'invites LLM [Réutilisable-](#page-67-0)

Obtenir des [Formats] spécifiques (#page-71-0) à partir des LLM

architectures cognitives

chaîne, [Architecture](#page-293-0) #2 : Chaîne

Appel LLM, [Architecture](#page-284-0) #1 : Appel LLM

routeur, [Architecture](#page-304-0) #3 : Routeur

composition

déclaratif, Déclaratif [Composition](#page-88-0)

impératif, Impératif [Composition](#page-82-0)

indexation des données

exemple de bout en bout, Génération de texte [Embeddings](#page-127-0)

exemple de, Récupération de [Documents] pertinents (#page-168-0)

chargeurs de documents [et, Conversion](#page-112-0) Vos documents en

Texte

documents, récupération du contexte complet, [MultiVectorRetriever](#page-152-0)-

RAPTOR : Traitement récursif [Abstractif](#page-156-1) pour Tree-

Récupération organisée

entrées dynamiques

construction, Création d'invites LLM [Réutilisable](#page-61-0)

alimenter les LLM, rendre les invites LLM [réutilisables](#page-65-0) [intégrations, récupération](#page-172-1) pertinentes, récupérer les documents pertinents

Embeddings de documents hypothétiques (HyDE), Document hypothétique [Embeddings-Hypothetical](#page-207-0) Embeddings de documents

Configuration de LangChain à l'aide de, Configuration avec [LangChain](#page-51-0) LangGraph

installation, [Présentation](#page-248-1) LangGraph

représentation visuelle, Création d'un [StateGraph](#page-255-1)

messages
filtrage, Filtrage [Messages](#page-268-0)

fusion, Fusion [Consécutive](#page-273-0) Messages

découpage, [Découpage](#page-264-0) Messages

prédictions de modèle, appel, utilisation des LLM dans [LangChain,](#page-53-1)

Génération de LLM [Prédictions] (#page-177-0) à l'aide de documents pertinents-

Génération de LLM [Prédictions](#page-184-0) à l'aide de documents pertinents

récupération multi-requêtes dans, [Multi-Query](#page-192-0) [Retrieval-Multi-](#page-196-0)

Récupération de requête

sortie

intermédiaire, [Intermédiaire](#page-396-0) Sortie

streaming [jeton par jeton, Streaming](#page-401-0) Sortie LLM

Jeton par jeton

structuré, [Structuré](#page-393-0) Sortie

analyseurs de sortie dans, autres formats [lisibles par machine](#page-76-1) avec analyseurs de sortie

Stratégie RAG-Fusion, [RAG-Fusion](#page-198-0)-[RAG-Fusion](#page-205-2)

enregistrez [gestion] (#page-142-0) dans, Suivi des modifications apportées à votre

####Documents

technique d'incitation à la réflexion, [Réflexion](#page-358-0)

Stratégie Rewrite-Retrieve-Read, routage [Rewrite-Retrieve-Read](#page-188-0)

logique, Logique [Routage](#page-214-0)-Logique [Routage](#page-219-1)

sémantique, [Sémantique](#page-221-0) Routage-[Sémantique](#page-223-0) Interface exécutable de routage, Utilisation de [Runnable](#page-78-0) Création de schéma d'interface, [Structuré](#page-392-0) Inspection de l'état de sortie et [mise à jour, ajout](#page-261-0) Mémoire vers StateGraph

Graphique d'état

création, Création d'un [StateGraph](#page-250-0)

ajout de mémoire, ajout de mémoire aux sous-graphes [StateGraph](#page-258-0)

appeler directement, appeler un [sous-graphe](#page-369-0) directement

appeler avec [functions, Calling](#page-372-0) un sous-graphe avec une fonction

Instruction SystemMessage, Utilisation de LLM dans les intégrations de texte [LangChain](#page-58-0) avec, Génération de texte [Embeddings](#page-123-0) extraction de texte avec, Conversion de vos [Documents](#page-113-1) en texte

texte, fractionnement en morceaux, [Splitting](#page-116-0) Votre texte en morceaux-[Splitting](#page-122-2) Votre texte en morceaux texte en métadonnées [filter, T](#page-230-3)[ext-to-Metadata](#page-227-0) Filtrer le texte en métadonnées Filtrer les traductions texte en SQL, Les outils [Text-to-SQL](#page-232-0) appellent toujours en premier, [Toujours](#page-334-0) Appel d'un outil en premier traitant de plusieurs, [Traitement](#page-345-0) avec de nombreux magasins de vecteurs d'outils et, [Travail](#page-133-0) avec la sortie JSON des magasins de vecteurs, JSON [Sortie](#page-72-0), [Structured](#page-391-0) Sortie Notation JSONSchema, [Structured](#page-392-1) Sortie

### **K**

paramètre k, [RAG-Fusion](#page-202-0)

k-voisins les plus proches [\(k-NN\), RAPTOR :](#page-156-2) Traitement abstrait récursif pour la récupération organisée par arbre Kahneman, Daniel, [Réflexion](#page-354-1) recherches par mots clés, [Incorporations](#page-100-2) Avant l'ensemble de données kv (valeur-clé) des LLM, [Création](#page-488-1) Ensembles de données

#### **L**

LangChain (voir aussi LangGraph ; grands modèles de langage ; applications LLM ; génération augmentée par récupération)

assemblage d'applications LLM, Assemblage des nombreux éléments d'un LLM [Application-Résumé, Cognitif](#page-77-2) Architectures avec LangGraph-Cognitive [Architectures](#page-283-1) avec LangGraph débuts de, [Préface](#page-10-2)

avantages [de, P](#page-33-1)[refac](#page-8-2)[e-P](#page-33-1)[reface](#page-11-0)[, LangChain](#page-33-1) et pourquoi c'est important, LLM [Fundamentals](#page-46-1) avec [LangChain-LLM](#page-49-0) Fondamentaux avec LangChain

documentation pour, LLM [Principes de base] (#page-47-3) avec LangChain pour obtenir des formats spécifiques à partir des LLM, Obtenir des formats spécifiques à partir des LLM - Autres formats [lisibles par machine] (#page-71-1) avec les analyseurs de sortie

interfaces fournies, Utilisation des LLM dans [LangChain](#page-52-0) rendant les invites LLM [réutilisables, Création](#page-59-0) Invites LLM réutilisables - Obtention de [Formats] spécifiques (#page-71-0) à partir de la configuration des LLM, Configuration avec [LangChain](#page-49-1) utilisation des LLM dans, Utilisation des LLM dans [LangChai](#page-52-1)[n-Using](#page-59-1) LLM dans LangChain

Langage d'expression LangChain (LCEL)

impératif versus déclaratif [composition, Utilisation](#page-80-0) l'interface Runnable

plan d'exécution optimisé utilisant Declarative [Composition](#page-87-0) LangGraph (voir aussi architectures cognitives ; LangChain ; LangSmith)
ajout de mémoire aux chatbots, Ajout de mémoire à [StateGraph-Adding](#page-257-1) Mémoire à [StateGraph](#page-262-0) bases de, [Présentation](#page-243-2) LangGraph-[Présentation](#page-249-0) LangGraph crée une mémoire de chatbot [systèmes, Construction](#page-238-1) une mémoire de chatbot Système[-Building](#page-242-0) un système de mémoire Chatbot créant des agents LangGraph, Création d'un [LangGraph](#page-323-0) Agent-Création d'un fichier de configuration d'agent [LangGraph](#page-332-1), Créer une illustration du flux de contrôle de configuration d'API [LangGraph](#page-448-0), [Backend](#page-436-0) API créant un [StateGraph, Création](#page-257-3) d'un [StateGraph](#page-249-1) -Création d'installation d'un StateGraph, [Présentation](#page-248-2) Sortie intermédiaire LangGraph, [Intermédiaire](#page-396-1) Sortie modifiant l'historique des discussions, [Modification](#page-262-1) Historique des discussions[-Résumé](#page-276-0) à des fins, [Présentation](#page-243-2) RAG autocorrectif LangGraph, L'étape de conception : [Auto-correctif](#page-472-2) RAG-L'étape de conception : [Auto-correctif](#page-486-1) Modes de flux RAG pris en charge dans, [Intermédiaire](#page-399-0) Sortie de streaming LLM en sortie [jeton par jeton, Streaming](#page-401-1) Sortie LLM jeton par jeton [sous-graphiques, sous-graphes](#page-373-0) dans [LangGraph](#page-366-1) - Appel d'un sous-graphe avec une fonction Modèles de données de l'API de la plateforme LangGraph, Données [Modèles](#page-441-0)

déploiement à l'aide de l'API [Backend](#page-437-1)

fonctionnalités, [Fonctionnalités-](#page-443-1)[Webhooks](#page-448-1)

LangGraph [Studio, Lancement](#page-464-0) [LangGraph](#page-460-1) Lancement de Studio LangGraph Studio

Création de compte LangSmith (voir aussi LangChain; LangGraph), Créer un exemple d'évaluation d'agent de compte [LangSmith](#page-439-1), Test de la vue de comparaison/test de régression [trajectoire](#page-529-0) d'un agent, [Régression](#page-504-0) Test de la création d'ensembles de données, Création du déploiement de [Ensembles de données](#page-487-1) à partir de l'interface utilisateur LangSmith, Déployer à partir des variables LangSmith [UI-Environment] (#page-455-0) invites en quelques coups, amélioration des évaluateurs LLM-en tant que juge [amélioration des performances](#page-496-1) évaluation par paire des performances des évaluateurs LLM-en tant que juge, la trace par paire [évaluation] (#page-502-1) aboutit à, l'étape de conception : [Auto-correctif](#page-482-0) Traçage RAG, [Traçage](#page-532-1) modèles de langage, Brief [Amorce](#page-12-2) sur l'ensemble de données de grands modèles de langage (llm) des LLM, [Création](#page-489-1) Ensembles de données de grands modèles de langage (LLM) (voir aussi sortie structurée) fournisseurs alternatifs pour, LLM [Principes de base](#page-47-4) avec l'informatique ambiante LangChain avec, Ambient [Computing](#page-545-1) avantages et inconvénients de, [Building](#page-537-1) avec LLM

brève introduction sur, Brief [Primer](#page-12-3) sur [LLMs-Brief](#page-17-1) Introduction sur les LLM

bâtiment avec, [Bâtiment](#page-537-2) avec LLMs-Ambient [Computing](#page-548-0) Claude et Bard, [Préface](#page-10-4)

édition collaborative avec, édition collaborative avec

[LLMs-Collaborative](#page-542-0) Édition avec les LLM

exemple de déploiement, grand modèle [Langue](#page-426-0)

obtenir des formats spécifiques à partir des LLM, devenir spécifique

Formats hors LLM-Autres [Machine-Readable](#page-71-1) Formats

avec les analyseurs de sortie

limites des connaissances [corpus, RAG](#page-93-2) Partie I : Indexer votre

Données

Intégrations basées sur LLM, basées sur LLM [Embeddings](#page-101-0)

versus apprentissage automatique, [Préface](#page-9-2)

pour une sortie multilingue, Brief [Primer](#page-13-2) sur les LLM

LLM open source, brève introduction sur [Promptin](#page-22-0)[g, LangChain](#page-34-1)

et pourquoi c'est important

GPT-3 d'OpenAI, Brief [Primer](#page-12-4) sur les LLM

GPT-3.5 d'OpenAI, [Préface](#page-8-3)

contenu pertinent pour les LLM, The Goal: Picking Relevant

Contexte pour les [LLM, récupération] (#page-94-1) [Documents] pertinents (#page-166-1) -

Génération de LLM [Prédictions](#page-184-0) à l'aide de documents pertinents

types de, Brief [Primer](#page-17-2) sur les LLM[-Fine-Tuned](#page-21-1) LLM

utilisation dans [LangChain, Utilisation](#page-59-1) LLM dans [LangChain-](#page-52-1)Utilisation des LLM dans LangChain

latence, [Modèles](#page-387-1) pour tirer le meilleur parti des [LLM, Intermédiaire](#page-395-1) Sortie, [Interactif](#page-541-3) Chatbots

LCEL (voir Langage d'expression LangChain)

Lama, brève introduction sur [Promptin](#page-22-0)[g, LangChain](#page-34-1) et pourquoi c'est important

Ensemble de données llm (grand modèle de langage), [Création](#page-489-1) Ensembles de données

Applications LLM (voir aussi déploiement ; métriques d'évaluation ; tests)

agentique, Agent [Architecture](#page-315-2)

assemblage, Assemblage des nombreuses pièces d'un LLM

[Application-Résumé, Cognitif](#page-77-2) Architectures avec
LangGraph-Cognitive [Architectures](#page-283-1) avec LangGraph

avantages de LangChain pour la construction, principes fondamentaux du LLM

avec [LangChain-LLM](#page-46-1) [Principes de base](#page-49-0) avec LangChain

défi de créer de bonnes [applications, LLM](#page-44-2)

Fondamentaux avec LangChain

caractéristiques communes des [Architectures] cognitives (#page-277-2) avec

LangGraph

étapes clés de l'application [développement, tests](#page-470-0) Techniques tout au long du cycle de développement d'applications LLM

majeur LLM [architectures, Cognitive](#page-280-2) Architectures avec LangGraph

applications multiacteurs, [Présentation](#page-243-3) des LLM multitâches LangGraph, [Multitâches](#page-417-1) LLM-Fork et [fusion](#page-422-0) modèles et concepts clés pour les considérations de sécurité [réussies, structurées](#page-389-1) Output-Fork et [fusion](#page-422-0), [Sécurité](#page-464-1) compromis entre agence et fiabilité, Architectures cognitives avec [LangGraph, Patterns](#page-278-1) pour tirer le meilleur parti des LLM-[Patterns](#page-389-0) pour tirer le meilleur parti des LLM Appel LLM [architecture,](#page-289-2) [Architecture](#page-283-0) #1 : LLM Appel-Architecture n° 1 : LLM Appelez les évaluateurs LLM-as-a-juge, Définir vos critères d'[évaluation] (#page-494-1) Boucle pilotée par LLM, La boucle [Planifier-Faire] (#page-318-1)

LLM (voir grands modèles de langage)

routage logique, Logique [Routage](#page-212-1)-Logique [Routage](#page-219-1)

mémoire à long terme, Ambient [Informatique](#page-548-1)

boucles, La boucle [Plan-Do](#page-318-2)

#### **M**

Bases de l'apprentissage automatique (ML) de, [Préface](#page-9-3) applications actuelles de, [Préface](#page-9-4) par rapport aux LLM, [Préface](#page-9-2) paramètre max\_tokens, Utilisation des LLM dans les systèmes de mémoire [LangChain](#page-54-1)

ajout de mémoire à [StateGraph, Adding](#page-257-1) Mémoire à StateGraph-Ajout de mémoire à [StateGraph](#page-262-0) création de mémoire de chatbot [systèmes, Building](#page-238-1) un système de mémoire de chatbot[-Building](#page-242-0) mémoire à long terme d'un système de mémoire de chatbot, Ambient [Computing](#page-548-1) but de, Utilisation [LangGraph](#page-237-1) pour ajouter de la mémoire à votre chatbot en fusionnant des forks, [Collaboratif](#page-544-0) Modification avec l'ajout de messages LLM, Création d'un filtrage [StateGraph](#page-251-0), Filtrage de [Message](#page-267-0)[s-Merging](#page-272-0) Fusion de messages consécutifs, Fusion [Consécutif](#page-272-0) Messages-[Résumé](#page-276-0) découpage, [Coupage](#page-262-2) Messages[-Coupage](#page-267-1) Utilisation abusive des messages, anticipation du potentiel, [Sécurité](#page-465-1) stratégies d'atténuation, [Sécurité](#page-464-2) ML (voir machine learning) dérive du modèle, [Régression](#page-503-1) Test des paramètres du modèle, Utilisation des LLM dans [LangChain](#page-54-2) erreurs de surveillance, [Surveillance](#page-534-0) et correction des erreurs (voir aussi tests) des architectures multi-agents, Multi-agents [Architectures-](#page-374-0)Superviseur [Architecture](#page-383-0)

récupération multi-requêtes [stratégie, M](#page-196-0)[ulti-Query](#page-190-0) Récupération-Récupération multi-requêtes

applications multiacteurs, [Présentation](#page-243-3) Sortie multilingue LangGraph, Brief [Primer](#page-13-2) sur le multitâche des LLM, [Multitasking](#page-417-1) LLMs-Fork et [merge](#page-422-0) [MultiVectorRetriever, M](#page-156-1)[ultiVectorRetrieve](#page-147-2)[r-RAPTOR:](#page-156-1) Traitement abstractif récursif pour la récupération organisée par arborescence

#### **N**

réseaux de neurones, Brief [Primer](#page-12-5) sur les nœuds LLM, [Présentation](#page-247-0) LangGraph Norvig, Peter, Agent [Architecture](#page-315-3)

#### **O**

observabilité, [Production](#page-530-2) évaluation hors ligne, Définition de votre [Évaluation](#page-492-3) Critères Ollama, LLM [Fundamentals](#page-47-5) avec évaluation en ligne LangChain, [Production](#page-530-3) Création de compte OpenAI API, Brief Primer on [Prompting](#page-22-1)[, Obtenir](#page-49-2) Configuration avec les invites de copie de LangChain dans [Playground, Brief](#page-22-2) Introduction à

Invite

intégration avec [LangChain, LangChain](#page-34-0) et Pourquoi c'est important, Génération de texte [Embeddings](#page-122-4) lancement de ChatGPT et de l'API ChatGPT, [Préface](#page-8-1) aperçu des modèles proposés, Utilisation des LLM dans [LangChain](#page-54-3) tarification, [Préface](#page-8-4)

OpenSearch, LLM [Fundamentals](#page-48-0) avec plan d'exécution optimisé LangChain, Declarative [Composition](#page-87-1) orchestration [capacités, LLM](#page-48-1) Fundamentals avec

LangChaîne
sortie (voir aussi sortie structurée) précise, l'objectif : choisir le contexte [pertinent] (#page-95-3) pour les LLM, présentation de la [récupération-augmentée](#page-165-1) sortie attendue de la génération, brève [amorce](#page-17-0) sur la sortie JSON des LLM, JSON [Sortie](#page-72-0), [Structured](#page-391-0) Sortie sortie multilingue, Brief [Primer](#page-13-2) sur le rôle des LLM dans les LLM, Brief [Primer](#page-12-6) sur le streaming des LLM jeton par jeton, [Interactif](#page-541-4) Résumé des chatbots, Ambient [Computing](#page-548-2) analyseurs de sortie, Autres formats [lisibles par machine](#page-75-2) avec sortie Analyseurs

#### **P**

évaluation par paire, [évaluation par paire](#page-502-0) exécution parallèle, utilisation des paramètres d'interface [Runnable](#page-80-0)

bases de, Brief [Primer](#page-12-7) sur les LLM

paramètre k, [RAG-Fusion](#page-202-0)

max\_tokens, Utilisation des LLM dans [LangChain](#page-54-1)

paramètre de modèle, utilisation des LLM dans [LangChain](#page-54-2)

température, Utilisation des LLM dans [LangChain](#page-54-4)

autorisations, limitation, [Sécurité](#page-464-3)

Perplexité, [Présentation](#page-244-0) LangGraph

persistance, ajout de mémoire à [StateGraph](#page-257-4)

PGVector, configuration avec [PGVector](#page-130-1)

boucle planifier-faire, La boucle [Plan-Do](#page-318-0)-La boucle [Plan-Do](#page-322-1)

Playground (API OpenAI), brève introduction à [Invite] (#page-22-2)

Postgres, configuration avec [PGVector](#page-130-1)

prétraitement, L'objectif : Choisir [Pertinent](#page-95-1) Contexte pour les tests de l'étape de préproduction des LLM

ensemble de données [création, Création](#page-492-1) [Ensembles de données-](#page-486-0)Définir votre

Critères d'évaluation

définir l'évaluation [critères, Définir](#page-492-1) Votre évaluation

Critères-Paire à deux [évaluation](#page-503-2)

de bout en bout [performance, évaluation](#page-506-0) le système de bout en bout d'un agent

Performance-Test de la [trajectoire] d'un agent (#page-530-1)

but de, La scène [Préproduction](#page-486-2)

tests de régression, [Régression](#page-503-3) Tests

LLM pré-entraînés, Brief [Primer](#page-17-3) sur les LLM

primitives, [Bâtiment](#page-538-1) avec LLM

données privées, RAG Partie I : [Indexation](#page-93-3) Vos données

tests au stade de la production

classification et marquage, [Classification](#page-534-1) et marquage, collecte des commentaires, collecte des commentaires dans [Production](#page-533-0), surveillance et correction des [erreurs, surveillance](#page-534-0) et correction

Erreurs

traçage, [Traçage](#page-531-0)

invite [ingénierie,](#page-23-0) [Dialogue-Tuned](#page-20-5) LLMs-Brief Primer on Prompting

garde-corps d'injection rapide, [Sécurité](#page-467-1)

modèle d'invite [abstractions, LangChain](#page-34-2) et pourquoi c'est

Important

invite

avantages de LangChain pour [invite, LangChain](#page-33-2) et pourquoi

C'est important

meilleures pratiques pour, Brief [Primer](#page-17-4) sur les LLM

brève introduction sur l'invite, brève introduction sur [l'invite] (#page-22-3) -

Quelques tirs [Invite] (#page-33-3)

combinant des techniques d'incitation, l'outil [Callin](#page-30-0)[g, LangChain](#page-35-0) et pourquoi c'est important

définition du terme, Brief [Primer](#page-17-5) sur les LLM

exemple détaillé de création d'invites LLM [réutilisables] (#page-59-2)

le but de, Créer des invites LLM [Réutilisables](#page-59-0)

technique d'incitation à la réflexion, [Reflection](#page-354-0)[-Reflection](#page-366-0) [réutilisation, L](#page-59-0)[angChain](#page-34-2) et pourquoi c'est important, rendre les invites LLM réutilisables - obtenir des [formats] spécifiques (#page-71-0) à partir de la sortie structurée des LLM avec, [Structuré](#page-390-0) Sortie

Pydantic, JSON [Sortie](#page-74-0)

Python

architecture des agents

implémentation, création d'un agent [LangGraph](#page-323-2)

sous-agents, Superviseur [Architecture](#page-380-0)

superviseur, Superviseur [Architecture](#page-377-0)

exécution asynchrone avec, Impératif [Composition](#page-86-3)

conversation chatbot [configuration, Utilisation](#page-55-1) LLM dans

LangChaîne

bords du chatbot, ajout, création d'un [StateGraph](#page-253-0)

mémoire de chatbot [systèmes, bâtiment](#page-239-1) une mémoire de chatbot

Système

nœuds de chatbot, ajout, création d'un [StateGraph](#page-252-1)

Prise en charge du streaming chatbot, Impératif [Composition,](#page-84-0)

Déclarative [Composition](#page-89-0)

ChatPromptTemplate, Création d'invites LLM [Réutilisable-](#page-66-1)

Obtenir des [Formats] spécifiques (#page-71-0) à partir des LLM

architectures cognitives

chaîne, [Architecture](#page-290-0) #2 : Chaîne

Appel LLM, [Architecture](#page-283-2) #1 : Appel LLM

routeur, [Architecture](#page-300-0) #3 : Routeur

Modèle ColBERT, ColBERT : Optimisation de la composition des [Embeddings](#page-158-2)
déclaratif, Déclaratif [Composition](#page-87-2)

impératif, Impératif [Composition](#page-81-2)

indexation des données

exemple de bout en bout, Génération de texte [Embeddings](#page-125-2)

exemple de, Récupération de [Documents] pertinents (#page-168-1)

chargeurs de documents [et, Conversion](#page-111-0) Vos documents en texte

résumés de documents, génération, documents [MultiVectorRetriever](#page-149-0), récupération du contexte complet, entrées dynamiques [MultiVectorRetriever](#page-152-1)

construction, création d'invites LLM [réutilisables](#page-60-1)

alimenter les LLM, rendre les invites LLM [réutilisables](#page-63-2) [intégrations, récupération](#page-172-2) pertinentes, récupérer les documents pertinents

Syntaxe de chaîne f, Rendre les invites LLM [Réutilisables](#page-63-3) Embeddings de documents hypothétiques (HyDE), Document hypothétique [Embeddings-Hypothetical](#page-206-1) Embeddings de documents

Configuration de LangChain à l'aide de, Configuration avec [LangChain](#page-50-0) LangGraph

installation, [Présentation](#page-248-3) LangGraph

représentation visuelle, Création d'un message [StateGraph](#page-254-1)

filtrage, Filtrage [Messages](#page-267-2)

fusion, Fusion [Consécutive](#page-272-1) Messages

découpage, [Découpage](#page-263-0) Messages

prédictions de modèle, appel, utilisation des LLM dans [LangChain,](#page-53-2)

Génération de LLM [Prédictions] (#page-176-0) à l'aide de documents pertinents-

Génération de LLM [Prédictions](#page-184-0) à l'aide de documents pertinents

récupération multi-requêtes dans, [Multi-Query](#page-191-1) [Retrieval-Multi-](#page-196-0)

Récupération de requête

sortie

intermédiaire, [Intermédiaire](#page-396-2) Sortie

JSON, JSON [Sortie](#page-72-1)

streaming [jeton par jeton, Streaming](#page-401-2) Sortie LLM

Jeton par jeton

structuré, [Structuré](#page-393-1) Sortie

analyseurs de sortie dans, autres formats [lisibles par machine] (#page-76-2) avec

Analyseurs de sortie

Stratégie RAG-Fusion, [RAG-Fusion](#page-197-1)-[RAG-Fusion](#page-205-2)

enregistrez [gestion] (#page-140-0) dans, Suivi des modifications apportées à votre

Documents

technique d'incitation à la réflexion, [Réflexion](#page-356-0)

Stratégie Rewrite-Retrieve-Read, routage [Rewrite-Retrieve-Read](#page-187-0)

logique, Logique [Routage](#page-213-1)-Logique [Routage](#page-219-1)

sémantique, [Sémantique](#page-220-0) Routage-[Sémantique](#page-223-0) Routage

interface exécutable, Utilisation de l'interface [Runnable](#page-78-1)

création de schéma, [Structured](#page-391-1) Sortie

inspection de l'état et [mise à jour, ajout](#page-261-1) Mémoire sur StateGraph

Graphique d'état

création, Création d'un [StateGraph](#page-249-2)

ajout de mémoire, Ajout de mémoire aux sous-graphes [StateGraph](#page-258-1)

appeler directement, appeler un [sous-graphe](#page-368-0) directement

appeler avec [functions, Calling](#page-371-0) un sous-graphe avec un

Fonction

Instruction SystemMessage, Utilisation de LLM dans les intégrations de texte [LangChain](#page-57-3), Génération de texte [Embeddings](#page-123-1) Extraction de texte avec, Conversion de vos [Documents](#page-112-1) en texte texte, division en morceaux, [Divisation](#page-115-0) Votre texte en Chunks-[Splitting](#page-122-2) Votre texte en morceaux

texte vers métadonnées [filtre, T](#page-230-3)[ext-to-Metadata](#page-225-0) Filtrer-Texte-vers-

Filtre de métadonnées

traductions texte vers SQL, [Texte vers SQL](#page-231-1)

outils

appelant toujours en premier, [Toujours](#page-333-0) Appeler un outil Traitant d'abord de plusieurs, [Traitant](#page-343-0) de nombreux outils

magasins de vecteurs

stocker des résumés dans, [MultiVectorRetriever](#page-150-0) en travaillant avec, [Working](#page-132-0) avec Vector Stores

### **Q**

requêtes (voir requêtes de données)

construction de requêtes

processus de, Requête [Construction](#page-224-2)

but de, [Résumé](#page-235-3)

texte-en-métadonnées [filtre, T](#page-230-3)[ext-to-Metadata](#page-225-1) Filtrer-Texte-en-

Filtre de métadonnées

traductions texte vers SQL, [Texte vers SQL](#page-230-4)-[Texte vers SQL](#page-234-0)

stratégie de routage des requêtes

routage logique, Logique [Routage](#page-212-1)-Logique [Routage](#page-219-1)

but de, Requête [Routage](#page-212-2)

routage sémantique, [Sémantique](#page-219-2) Routage-[Sémantique](#page-223-0) Routage

transformation de requête

définition du terme, Requête [Transformation](#page-184-3)

Incorporations de documents hypothétiques (HyDE), hypothétiques

Document [Embeddings-Hypothetical](#page-205-1) Document

Intégrations

stratégie de récupération multi-requêtes, [Multi-Query](#page-190-0) Récupération-

[Multi-Requêtes](#page-196-0) Récupération

but de, [Résumé](#page-235-4)
Stratégie RAG-Fusion, [RAG-Fusion](#page-197-2)-[RAG-Fusion](#page-205-2) Stratégie de réécriture-récupération-lecture, [Rewrite-Retrieve-Read](#page-185-2)-[Rewrite-Retrieve-Read](#page-190-1) questions et commentaires, Comment nous [Contacter](#page-42-0)

mise en file d'attente, entrées de file d'attente [simultanées](#page-418-1)

#### **R**

RAG (voir génération augmentée par récupération)

Stratégie RAG-Fusion, [RAG-Fusion](#page-197-2)-[RAG-Fusion](#page-205-2)

RAPTOR (traitement abstrait récursif pour les systèmes organisés en arborescence)

[récupération\), RAPTOR :](#page-156-3) Traitement abstractif récursif pour

Récupération organisée par arbre

limitation de débit, [Sécurité](#page-467-2)

ReAct [architecture, L](#page-322-2)[angChain](#page-35-1) et pourquoi c'est important, le

Boucle Planifier-Faire

collaboration en temps réel, [Collaboratif](#page-543-1) Édition avec fusion de rangs réciproques (RRF) [algorithme,](#page-205-2) [RAG-Fusion](#page-197-2)[-RAG-](#page-205-2)

Fusion

gestion des enregistrements, suivi des modifications apportées à vos [documents](#page-138-2) -Suivi des modifications apportées à vos [documents](#page-147-1)

traitement abstrait récursif pour la récupération organisée sous forme d'arborescence

[\(RAPTOR\), RAPTOR:](#page-156-3) Traitement abstractif récursif pour

Récupération organisée par arbre

technique d'incitation à la réflexion, [Réflexion](#page-354-0)[-Réflexion](#page-366-0)

étape de réflexion, Ambient [Computing](#page-548-3)

tests de régression, [Régression](#page-503-3) Tests

apprentissage par renforcement à partir du feedback humain (RLHF),

[Instruction-Tuned](#page-19-1) LLM

fiabilité, Cognitive [Architectures](#page-278-2) avec [LangGraph, Patterns](#page-385-4)

pour tirer le meilleur parti des LLM, [Construire](#page-537-3) avec les LLM

reclassement/réorganisation, [RAG-Fusion](#page-199-0)

[réponse, évaluation, évaluation](#page-507-0) le processus de bout en bout d'un agent

Performances

processus de récupération, Récupération des [Documents] pertinents (#page-172-0)

génération augmentée par récupération (RAG)

construire des prédictions LLM RAG [systèmes, génération] robustes (#page-182-0) à l'aide de documents pertinents

étapes principales de, Récupération des [Documents] pertinents (#page-166-3)

[définition](#page-95-4) du terme, L'objectif : choisir un contexte pertinent pour

LLM

générer des prédictions LLM [prédictions, Génération](#page-175-1) Prédictions LLM à l'aide de documents pertinents [Génération de documents](#page-184-0) Prédictions LLM à l'aide de documents pertinents

introduction à, Présentation de [Retrieval-Augmented](#page-164-2)

Génération

processus de, RAG Partie II : [Chatter](#page-163-1) avec l'invite de vos données avec, [Récupération-Augmentée](#page-27-1) Gestion des requêtes de génération

construction, Requête [Construction-](#page-224-1)[Texte-vers-SQL](#page-234-0) routage, Requête [Routage-](#page-211-0)[Sémantique](#page-223-0) Transformation de routage, Requête [Transformatio](#page-184-1)[n-Hypothétique](#page-211-1) Document Intégrations

récupérer les [documents, Récupérer](#page-166-2) pertinents

Documents-Récupération de [Documents] pertinents (#page-174-0)

RAG autocorrectif, L'étape de conception : [Auto-corrective](#page-472-0) RAG-L'étape de conception : [Auto-corrective](#page-486-1) RAG

Stratégie Réécriture-Récupération-Lecture, [Réécriture-Récupération-Lecture](#page-185-2)-

[Réécrire-Récupérer-Lire](#page-190-1)

RLHF (apprentissage par renforcement à partir du feedback humain),

[Instruction-Tuned](#page-19-1) LLM

rôles, [Dialogue-Tuned](#page-20-6) LLM, Utilisation des LLM dans [LangChain](#page-55-2)

routeur [architecture, A](#page-313-0)[rchitecture](#page-298-0) #3 : Routeur-Architecture #3 :

Routeur

routage

routage logique, [Routage] Logique(#page-212-1)-Routage de requête [Routage]logique(#page-219-1), Requête [Routage](#page-211-0)[-Sémantique](#page-223-0) Routage routage sémantique, [Sémantique](#page-219-3) Routage-[Sémantique](#page-223-0) Routage Algorithme RRF (fusion de rangs réciproques), interface exécutable [RAG-Fusion](#page-197-2), utilisation de l'interface [Runnable](#page-77-3) (plateforme LangGraph), [Exécutions](#page-443-2) Russell, Stuart, agent [Architecture](#page-315-3)
sandboxing, [Sécurité](#page-465-2) enregistrer et envoyer, [Collaboratif](#page-542-2) Édition avec les meilleures pratiques de sécurité des LLM, [Sécurité](#page-464-2) autocorrection, L'étape de conception : [Auto-correction](#page-474-0) Technique d'invite d'autocritique RAG, [Réflexion](#page-354-2) sémantique intégrations, Sémantique [Embeddings](#page-103-0) Expliqué-Sémantique [Embeddings](#page-106-1) Relations sémantiques expliquées, [Splitting](#page-114-2) Routage sémantique de votre texte en morceaux, [Sémantique](#page-219-2) Routage-[Sémantique](#page-223-0) Routage des données sensibles, protection, [Sécurité](#page-466-3) [étapes, évaluation, évaluation](#page-507-1) uniques des performances de bout en bout d'un agent, intégrations éparses, [Incorporations](#page-100-3) Avant les LLM

sous-systèmes spécialisés, état Multi-Agent [Architectures](#page-374-3), [Présentation](#page-247-1) LangGraph, Création d'un [StateGraph,](#page-251-1)

[Human-in-the-Loop](#page-403-1) [Modalités, Collaboratif](#page-544-1) Édition avec

LLM

état, [Présentation](#page-243-4) LangGraph

Graphique d'état

ajout de mémoire à, Ajout de mémoire à [StateGraph](#page-257-1)[-Adding](#page-262-0) Mémoire à StateGraph

création, Création d'un [StateGraph-](#page-249-1)Création d'un [StateGraph](#page-257-3) exécutions sans état (LangGraph Platform), [Stateless](#page-447-0) exécutions

[apatridie, utilisation](#page-237-2) LangGraph pour ajouter de la mémoire à votre chatbot

invite statique à quelques tirs, méthode de flux Few-Shot [Prompting](#page-32-2), utilisation de l'interface [Runnable](#page-77-0), [Résumé](#page-91-0),

[Intermédiaire](#page-396-3) Sortie

diffusion en continu (plateforme LangGraph), [Streaming](#page-444-0)

chat en streaming, [Interactif](#page-540-2) Chatbots

sortie structurée

humain-dans-la-boucle [modalités, Humain-dans-la-boucle](#page-402-0)

Modalités[-Fork](#page-417-2)

intermédiaire [sortie, I](#page-400-3)[intermédiaire](#page-395-0) Sortie-Intermédiaire

Sortie

besoin, [Structuré](#page-389-1) Sortie

stratégies à atteindre, [Structuré](#page-390-1) Sortie

sortie LLM en streaming [jeton par jeton, Streaming](#page-400-4) LLM

Sortie jeton par jeton

sous-agents, Superviseur [Architecture](#page-379-0)

sous-graphiques

ajout aux graphiques parents, sous-graphiques dans [LangGraph](#page-367-0)

appeler directement des sous-graphes, appeler un [sous-graphe] (#page-367-1) directement-

Appel d'un [Subgraph](#page-370-0) avec une fonction

appeler des sous-graphes avec [functions, Calling](#page-370-0) un sous-graphe avec

une fonction

cas d'utilisation pour les sous-graphiques dans [LangGraph](#page-366-1)

sous-systèmes, spécialisés, Multi-Agent [Architectures](#page-374-3) Supabase, [Vecteur](#page-428-0) Architecture de superviseur de magasin, Multi-Agent [Architectures-](#page-376-0)Superviseur [Architecture](#page-383-0) données synthétiques, [Création](#page-487-2) Rôle système des ensembles de données, [Dialogue-Tuned](#page-20-7) LLM, utilisation des LLM dans [LangChain](#page-55-3) Interface SystemMessage, utilisation des LLM dans [LangChain](#page-57-4)

### **T**

tables, [MultiVectorRetriever](#page-147-2) tâches [gestionnaires,](#page-548-4) [Collaboratif](#page-544-2) Modification avec les LLM, ensembles de données spécifiques aux tâches Ambient Computing, [Instruction-Tuned](#page-18-0) Événements de tâche\_result des LLM, [Intermédiaire](#page-400-5) Température de sortie paramètre, Utilisation des LLM dans la phase de conception des tests [LangChain](#page-54-4), La phase de conception : [Auto-corrective](#page-472-0) RAG-La phase de conception : Autocorrective Étapes clés RAG de l'application [développement, test](#page-470-0) Techniques tout au long du cycle de développement de l'application LLM [prédéploiement, test](#page-455-1) Votre [LangGraph](#page-450-0) Application locale : testez votre application LangGraph localement [préproduction](#page-530-1), l'étape [Préproduction](#page-486-2) : test de la trajectoire d'un agent

production [étape, P](#page-535-0)[roduction](#page-530-4)[-Surveillance](#page-535-0) et correction des erreurs

texte

convertir des documents en texte, Conversion de votre

Documents en [Conversion de texte](#page-109-0) Vos [Documents](#page-114-0) en texte

conversion de texte en [nombres, incorporations :](#page-97-0) Conversion de texte

aux nombres-sémantiques [Embeddings] (#page-106-1) expliqué

générer des intégrations de texte, Génération de texte [Embeddings-](#page-122-1)

Génération de texte [Incrustations](#page-125-1)

mélangé avec des tableaux, [MultiVectorRetriever](#page-147-2)

diviser le texte en morceaux, [Diviser](#page-114-1) Votre texte en morceaux-

[Diviser](#page-122-2) Votre texte en morceaux

texte-en-métadonnées [filtre, T](#page-230-3)[ext-to-Metadata](#page-225-1) Filtrer-Texte-en-

Filtre de métadonnées

traductions texte vers SQL, [Texte vers SQL](#page-230-4)-[Texte vers SQL](#page-234-0)
services tiers, [LangChain](#page-34-3) et pourquoi c'est important

threads, ajout de mémoire à [StateGrap](#page-260-0)[h, Handle](#page-418-2)

indépendamment

fils de discussion (Plateforme LangGraph), [Threads](#page-442-1)

streaming jeton par jeton [sortie, Streaming](#page-400-4) Sortie LLM

Jeton par jeton

jetons, Brief [Primer](#page-15-0) sur les LLM

technique d'appel d'outils

applications LLM agentiques et, Agent [Architecture](#page-316-1)

toujours appeler les outils en premier, [Toujours](#page-332-0) Appeler un outil en premier-[Toujours](#page-342-1) Appeler un outil D'abord traiter avec de nombreux outils, [Gérer](#page-342-2) avec de nombreux outils-Gérer plusieurs [Outils, Multi-Agent](#page-352-0) [Architectures](#page-374-4) définition du terme, Outil [Appel](#page-28-0) intégrations fournies [pour, LangChain](#page-34-4) et Pourquoi c'est important les chatbots interactifs et, [Interactif](#page-541-5) Sortie structurée des chatbots avec, [Structuré](#page-390-2) Traçage de sortie, [Traçage](#page-531-0) [trajectoire, évaluation, Évaluation](#page-507-2) de bout en bout d'un agent [Performance, Test](#page-530-1) [trajectoire-] d'un agent(#page-520-1)Test du réseau neuronal de transformateur de trajectoire d'un agent [architecture, Brief](#page-16-2) Introduction aux déclencheurs LLM, Ambient [Informatique](#page-547-0) découpage messages, [Trimming](#page-262-2) Messages[-Trimming](#page-267-1) Instruction try-catch des messages, [Human-in-the-Loop](#page-408-2) Modalités

### **U**

annuler/rétablir des piles, [Collaboratif](#page-545-5) Modification avec des LLM Identifiants universellement uniques [\(UUIDs\), Ajout](#page-260-1) Mémoire à StateGraph

mode mises à jour (LangGraph), [Intermédiaire](#page-399-1) Sortie

rôle utilisateur, [Dialogue-Tuned](#page-20-8) LLM, Utilisation des LLM dans [LangChain](#page-55-4)

**V**

mode valeurs (LangGraph), [Intermédiaire](#page-399-2) Variance de sortie, [Modèles](#page-387-2) pour tirer le meilleur parti des index vectoriels LLM, [LangChain](#page-35-5) et Pourquoi il est important que les vecteurs stockent des fournisseurs alternatifs pour LLM [Principes de base](#page-48-2) avec la définition LangChain de [terme, L](#page-97-4)[angChain](#page-35-6) et Pourquoi c'est important, L'objectif : choisir un contexte pertinent pour un exemple de déploiement de LLM, [Vector](#page-427-2) Stocker les intégrations dans des magasins vectoriels, Stockage des intégrations dans un vecteur [Store-Working](#page-128-1) avec le contrôle de version des magasins vectoriels, [Collaboratif](#page-542-3) Édition avec l'éditeur de code LLM VSCode, [Interactif](#page-540-3) Chatbots

**W**

Weaviate, LLM [Fundamentals](#page-48-3) avec les webhooks LangChain (LangGraph Platform), [Webhooks](#page-448-2)

**X**

Format XML, autres formats [lisibles par machine](#page-75-3) avec analyseurs de sortie

#### **O**

Yao, Shunyu, La boucle [Plan-Do](#page-322-3)

#### **Z**

invite zéro-shot, Zero-Shot [Invite](#page-24-0) Zod, JSON [Sortie](#page-74-1)

## À propos des auteurs

**Mayo Oshin** est un entrepreneur technologique, un conseiller en IA et un investisseur providentiel. Mayo a été l'un des premiers contributeurs développeurs et défenseur de la bibliothèque open source LangChain et l'un des premiers pionniers du populaire « chat » d'IA avec mouvement de données (plus de 5 millions de personnes touchées grâce à ses idées de leadership éclairé jusqu'à présent).

Mayo a consulté, conseillé et formé des centaines d'ingénieurs et de chefs de produits dans diverses institutions de premier plan, notamment Amazon, LinkedIn, Evercore, Visa et BCG.

Vous pouvez en apprendre davantage sur lui sur son site Web, *[mayooshin.com](https://mayooshin.com/)*, et obtenir ses dernières idées sur l'IA et la technologie sur [X.](https://x.com/mayowaoshin)

**Nuno Campos** est l'un des ingénieurs logiciels fondateurs de LangChain, Inc. Nuno a une décennie d'expérience en tant qu'ingénieur logiciel Python et JavaScript, architecte et responsable de la maintenance open source. Il a travaillé pour diverses startups technologiques dans des rôles de génie logiciel et de science des données. Il est titulaire d'un MSc en Finance.

## Colophon

Les animaux sur la couverture de *Learning LangChain* sont des rainettes européennes (*Hyla arborea*).

On les trouve principalement en Europe continentale, généralement à proximité de la végétation. Leur peau verte peut changer sa couleur du vert au gris ou au brun, en fonction de divers facteurs. Cette capacité permet de les camoufler des prédateurs. Ils utilisent également leur langue collante (pour les repas, c'est-à-dire les insectes) et les coussinets collants de leurs pieds (pour se déplacer) pour naviguer dans la vie dans leur habitat.
Pendant la saison des amours, les rainettes européennes se rassemblent près des étangs afin de pouvoir pondre près de l'eau pour les futurs têtards. Les mâles émettent un cri d'accouplement qui frappe par son volume, en particulier lorsque de nombreuses grenouilles sont rassemblées au même endroit. Les femelles pondent alors des touffes de 800 à 1 000 œufs. Environ 10 à 14 jours plus tard, les têtards éclosent et le cycle de vie recommence.

De nombreux animaux figurant sur les couvertures d'O'Reilly sont en voie de disparition ; ils sont tous importants pour le monde.

L'illustration de la couverture est de Karen Montgomery, basée sur une gravure au trait antique du *Meyers Kleines Lexicon*. La conception de la série est signée Edie Freedman, Ellie Volckhausen et Karen Montgomery. Les polices de couverture sont Gilroy Semibold et Guardian Sans. La police du texte est Adobe Minion Pro ; la police du titre est Adobe Myriad Condensed ; et la police du code est Ubuntu Mono de Dalton Maag.

![](_page_599_Picture_1.jpeg)

*Votre passerelle vers la connaissance et la culture. Accessible à tous.* 

![](_page_599_Figure_3.jpeg)