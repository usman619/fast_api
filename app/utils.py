from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], bcrypt__ident="2b", deprecated="auto")

def hash_password(password:str):
    return pwd_context.hash(password)

