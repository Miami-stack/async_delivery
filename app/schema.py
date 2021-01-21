SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "identificator": "de3d4",
            "status": "processed"
        }
    ],
    "required": [
        "identificator",
        "status"
    ],
    "properties": {
        "identificator": {
            "$id": "#/properties/identificator",
            "type": "string",
            "pattern": "^[a-z0-9]{2,5}$",
            "title": "The identificator schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "de3d4"
            ]
        },
        "status": {
            "$id": "#/properties/status",
            "type": "string",
            "title": "The status schema",
            "pattern": "^.*(processed|performed|delivered).*$",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "processed"
            ]
        }
    }
}
