from fastapi import Request
from authlib.integrations.starlette_client import OAuth


__all__ = ("GoogleService",)


class GoogleService:
    # TODO: import the letters from gmail, use embedding + chunks, save it to pgvector use them as context for AI on requests

    def __init__(self, config):
        self.config = config

    @property
    def oauth(self) -> OAuth:
        oauth = OAuth()
        oauth.register(
            name="google",
            client_id=self.config["GOOGLE_CLIENT_ID"],
            client_secret=self.config["GOOGLE_CLIENT_SECRET"],
            server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
            client_kwargs={
                "scope": "openid email profile "
                        # "https://www.googleapis.com/auth/gmail.modify "
                        # "https://www.googleapis.com/auth/gmail.send "
                         "https://www.googleapis.com/auth/calendar.events.freebusy "
                         "https://www.googleapis.com/auth/calendar.freebusy "
                        # "https://www.googleapis.com/auth/calendar.events "
                        # "https://www.googleapis.com/auth/calendar.events.owned "
            },
        )
        return oauth

    async def authorize(self, request: Request):
        return await self.oauth.google.authorize_redirect(
            request,
            self.config["GOOGLE_REDIRECT_URL"],
            access_type="offline",
            prompt="consent",
            include_granted_scopes="true",
        )

    async def authorize_access_token(self, request: Request):
        token = await self.oauth.google.authorize_access_token(request)
        return token['userinfo'], token.get("refresh_token")
