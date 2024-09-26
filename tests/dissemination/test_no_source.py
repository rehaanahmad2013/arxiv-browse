def test_no_source(client_with_test_fs, mocker):
    resp = client_with_test_fs.get("/pdf/1208.9998")
    assert resp.status_code == 404
    assert "1208.9998" in resp.text
    assert resp.headers.get('Surrogate-Control', None)=="max-age=86400"
    keys= " "+resp.headers["Surrogate-Key"]+" "
    expected_keys=["paper-unavailable", "paper-id-1208.9998", "paper-id-1208.9998-current"] #not found should be in here and is in practice but not in tests
    assert all(" "+item+" " in keys for item in expected_keys)


    resp = client_with_test_fs.get("/pdf/1208.9998v1")
    assert resp.status_code == 404
    assert "1208.9998v1" in resp.text
    assert resp.headers.get('Surrogate-Control', None)=='max-age=31536000'
    keys= " "+resp.headers["Surrogate-Key"]+" "
    expected_keys=["paper-unavailable", "paper-id-1208.9998", "paper-id-1208.9998v1"] #not found should be in here and is in practice but not in tests
    assert all(" "+item+" " in keys for item in expected_keys)

    resp = client_with_test_fs.get("/pdf/1208.9998v2")
    assert resp.status_code == 404
    assert "1208.9998v2" in resp.text
    assert resp.headers.get('Surrogate-Control', None)=='max-age=604800'
    keys= " "+resp.headers["Surrogate-Key"]+" "
    expected_keys=["paper-unavailable", "paper-id-1208.9998", "paper-id-1208.9998v2"] #not found should be in here and is in practice but not in tests
    assert all(" "+item+" " in keys for item in expected_keys)
