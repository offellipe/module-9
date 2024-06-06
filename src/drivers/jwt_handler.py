import jwt
from typing import Dict
from datetime import datetime, timedelta, timezone
from configs.jwt_configs import jwt_infos

class JwtHandler:

    def create_jwt_token(self, body: Dict = {}) -> str:
        token = jwt.encode(
            payload={
                'exp': datetime.now(timezone.utc) + timedelta(hours=jwt_infos["JWT_HOURS"]),
                **body,
            },
            key=jwt_infos["KEY"],
            algorithm=jwt_infos["ALGORITHM"]
        )
        return token
    
    def decode_jwt_token(self, token: str) -> Dict:
        token_information =jwt.decode (
            token,
            key="minhaChave",
            algorithms="HS256"
        )
        return token_information
