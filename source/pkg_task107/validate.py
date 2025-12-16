def read_float(prompt: str = ""):
    prompt = prompt if prompt else "Digite um valor numérico: "

    while True:
        try:
            user = input(prompt).strip()

            if "," in user or user.count(".") > 1:
                user = user.replace(",", "_").replace(".", "_")
                dot = user.rfind("_")
                user = f"{user[:dot]}.{user[dot:]}"
                user = user.replace("_", "")

            return float(user)
        except:
            print("Por favor!", end=" ")
