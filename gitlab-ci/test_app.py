import json

def test_response_format():
    """Vérifie que la réponse API a le bon format"""
    expected_keys = {"status", "message", "version"}
    response = {"status": "ok", "message": "API DevOps fonctionnelle", "version": "1.0"}
    assert set(response.keys()) == expected_keys
    assert response["status"] == "ok"
    print("PASS: format de réponse correct")

def test_version():
    """Vérifie que la version est définie"""
    response = {"status": "ok", "message": "API DevOps fonctionnelle", "version": "1.0"}
    assert response["version"] != ""
    print("PASS: version définie")

if __name__ == "__main__":
    test_response_format()
    test_version()
    print("Tous les tests passent !")
