from requests import Response, request


class PyTranslo:
    def __init__(self, token: str, api_domain: str = "translo.p.rapidapi.com"):
        self._token = token
        self._api_domain = api_domain
        self._api_url = f"https://{self._api_domain}/api/v3/"

    def _request(self, method: str, action: str,
                 content_type: str, **kwargs) -> Response:
        return request(
            method,
            f"{self._api_url}{action}",
            **kwargs,
            headers={"content-type": content_type,
                     "X-RapidAPI-Host": self._api_domain,
                     "X-RapidAPI-Key": self._token})

    def _get(self,
             action: str,
             content_type: str = "application/x-www-form-urlencoded",
             **kwargs) -> Response:
        return self._request("GET", action, content_type, **kwargs)

    def _post(self,
              action: str,
              content_type: str = "application/x-www-form-urlencoded",
              **kwargs) -> Response:
        return self._request("POST", action, content_type, **kwargs)

    def translate(self,
                  text: str,
                  to_lang: str,
                  from_lang: str = "",
                  fast: bool = False) -> str | dict:
        """
        Translate function

        :param text: text of translate
        :param from_lang: from the language of the text
        :param to_lang: to language of the text
        :param fast: fast mode translate
        :return:
        """
        response = self._post(
            "translate",
            data=f"text={text}&from={from_lang}&to={to_lang}"
                 f"&fast={str(fast).lower()}".encode('utf-8'))

        json = response.json()

        try:
            return json["translated_text"]
        except KeyError:
            raise Exception(json.get("message") or json.get("error"))

    def batch_translate(self, batch: list[dict]) -> list[dict]:
        """

        :param batch:
        :return:
        """
        response = self._post("batch_translate",
                              content_type="application/json", json=batch)

        json = response.json()

        try:
            return json["batch_translations"]
        except KeyError:
            raise Exception(json.get("message") or json.get("error"))

    def detect(self, text: str) -> str:
        """
        detects language of given text
        :param text:
        :return: language code
        """
        response = self._get("detect", params={"text": text})

        json = response.json()

        try:
            return json["lang"]
        except KeyError:
            raise Exception(json.get("message") or json.get("error"))
