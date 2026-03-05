"""End-to-end tests for the GET /interactions endpoint."""
import httpx

"""checking that interactions is available"""
def test_get_interactions_returns_200(client: httpx.Client) -> None:
    response = client.get("/interactions/")
    assert response.status_code == 200

"""checking that data exists in interations and this data has fields id, item_id, created_at"""
def test_get_interactions_response_items_have_expected_fields(client: httpx.Client) -> None:
    response = client.get("/interactions/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    item = data[0]
    assert "id" in item
    assert "item_id" in item
    assert "created_at" in item


"""getting every element in not empty data that has item_id <=1 """
def test_get_interactions_filter_includes_boundary(client: httpx.Client) -> None:
    response = client.get("/interactions/", params={"max_item_id": 1})
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    for item in data:
        assert item["item_id"] <= 1