from dotenv import dotenv_values


__all__ = ["load_config"]

def load_config(config):
    config = dict(dotenv_values(config))
    for k, v in config.items():
        if "port" in k.lower():
            config[k] = int(v)
    return config
