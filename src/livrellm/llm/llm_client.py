"""Le client de chat de LivreLLM — local par defaut (C48, decision 4).

Ce module reparait deux choses, et c'est a ce titre qu'il appartient a la
phase 0.

**Un : le fournisseur n'etait pas lu.** `config.settings` portait bien
`LLM_PROVIDER`, `OLLAMA_HOST` et `OLLAMA_MODEL`, mais ce client construisait un
`OpenAI(...)` sans jamais regarder le reglage. Le reglage existait, le choix
n'existait pas, et **chaque appel partait vers un service externe** — y compris,
le jour ou la phase 2 arrivera, avec du texte de norme, de Techniques de
l'Ingenieur ou de piece client dans le corps du message. La decision 4 de C48
dit l'inverse : *modele local par defaut ; aucun contenu de norme, de TI ou de
piece client n'est envoye a un service externe*. Le defaut est donc `ollama`, et
un fournisseur distant ne se joint que si le reglage le nomme.

**Deux : une panne rendait une reponse.** `chat()` attrapait toute exception et
rendait la chaine `f"Error: {e}"`. Pour l'appelant, c'etait une reponse du
modele comme une autre : il pouvait l'afficher, l'indexer, la citer. C'est la
forme exacte du faux succes que C44 vient de fermer ailleurs dans la machine —
un controle qui ne peut pas tourner echoue, il ne se tait jamais. Une panne leve
donc `ErreurDeChat`, et l'appelant decide.
"""

from __future__ import annotations

from config.settings import settings

FOURNISSEURS_ADMIS = ("ollama", "openai")
FOURNISSEUR_LOCAL = "ollama"


class ErreurDeChat(RuntimeError):
    """Le modele n'a pas repondu. Ce n'est pas une reponse : c'est une panne."""


class FournisseurInconnu(ValueError):
    """`LLM_PROVIDER` ne nomme aucun fournisseur admis."""


class LLMClient:
    """Client unifie de chat. Le fournisseur vient du reglage, jamais du code."""

    def __init__(self, fournisseur: str | None = None, modele: str | None = None) -> None:
        self.fournisseur = (fournisseur or settings.LLM_PROVIDER or FOURNISSEUR_LOCAL).lower()
        if self.fournisseur not in FOURNISSEURS_ADMIS:
            raise FournisseurInconnu(
                f"LLM_PROVIDER vaut {self.fournisseur!r} ; "
                f"admis : {', '.join(FOURNISSEURS_ADMIS)}"
            )
        self.modele = modele or (
            settings.OLLAMA_MODEL if self.fournisseur == FOURNISSEUR_LOCAL else settings.LLM_MODEL
        )

    @property
    def est_local(self) -> bool:
        """Vrai quand aucun octet ne quitte le poste."""
        return self.fournisseur == FOURNISSEUR_LOCAL

    def chat(self, messages: list[dict]) -> str:
        """Rend la reponse du modele, ou leve. Elle ne rend jamais une panne."""
        if self.est_local:
            return self._chat_ollama(messages)
        return self._chat_openai(messages)

    def _chat_ollama(self, messages: list[dict]) -> str:
        import ollama

        try:
            client = ollama.Client(host=settings.OLLAMA_HOST)
            reponse = client.chat(model=self.modele, messages=messages)
        except Exception as erreur:  # noqa: BLE001 - on retraduit, on n'avale pas
            raise ErreurDeChat(
                f"Ollama ({settings.OLLAMA_HOST}, modele {self.modele}) "
                f"n'a pas repondu : {erreur}"
            ) from erreur
        return reponse["message"]["content"]

    def _chat_openai(self, messages: list[dict]) -> str:
        from openai import OpenAI

        if not settings.OPENAI_API_KEY:
            raise ErreurDeChat(
                "LLM_PROVIDER vaut 'openai' mais OPENAI_API_KEY est absente : "
                "aucun appel n'est tente."
            )
        try:
            client = OpenAI(api_key=settings.OPENAI_API_KEY)
            completion = client.chat.completions.create(model=self.modele, messages=messages)
        except Exception as erreur:  # noqa: BLE001 - on retraduit, on n'avale pas
            raise ErreurDeChat(
                f"OpenAI (modele {self.modele}) n'a pas repondu : {erreur}"
            ) from erreur
        return completion.choices[0].message.content

    def translate(self, text: str, target_lang: str = "fr") -> str:
        """Traduction technique. Meme chemin, meme fournisseur, memes pannes."""
        prompt = (
            f"Translate the following technical text to {target_lang}. "
            "Preserve markdown formatting, code blocks, and math formulas exactly. "
            f"Text:\n\n{text}"
        )
        return self.chat(
            [
                {"role": "system", "content": "You are a professional technical translator."},
                {"role": "user", "content": prompt},
            ]
        )
