from authorization.users.schemas import UserInDB
from authorization.users import utils as user_utils


john = UserInDB(username="john", hashed_password=user_utils.hash_password("qwerty"))
sam = UserInDB(username="sam", hashed_password=user_utils.hash_password("secret"))
users_db: dict[str, UserInDB] = {john.username: john, sam.username: sam}
