Planet_Api_Key = "3d42933f4c284a3b8dd2c5200e97da00"
Resources = {
    "dev": {
        "s3": {
            "bucket": "gaia-dev-555194212901",
            "folder": "gaia-map-segment-fetcher",
        },
        "rds": {
            "host": "gaia-db.c7qv9zc9szdp.us-east-2.rds.amazonaws.com",
            "port": 3306,
            "db": "testdb",
            "user": "sorengoyal",
            "password": "FU4$dptrm"
        }
    },
    "prod": {
            "s3": {
                "bucket": "gaia-prod",
                "folder": "gaia-map-segment-fetcher",
            },
            "rds": {
                "host": "gaia-db.c7qv9zc9szdp.us-east-2.rds.amazonaws.com",
                "port": 3306,
                "db": "gaiadb",
                "user": "sorengoyal",
                "password": "FU4$dptrm"
            }
        }
}