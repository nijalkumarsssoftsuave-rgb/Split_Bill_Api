from decouple import config

RATE_LIMIT_WINDOW_SECONDS = int(config("RATE_LIMIT_WINDOW_SECONDS", default=60))

RATE_LIMITS = {
    "GET": int(config("GET_RATE_LIMIT", default=3)),
    "POST": int(config("POST_RATE_LIMIT", default=2)),
}
