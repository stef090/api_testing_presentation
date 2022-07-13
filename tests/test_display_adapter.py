from presentation.adapter import DisplayAdapter


def test_display_adapter():
    input_value = {
        "post code": "10000",
        "country": "Croatia",
        "country abbreviation": "HR",
        "places": [
            {
                "place name": "Sljeme",
                "longitude": "15.9667",
                "state": "Zagrebačka",
                "state abbreviation": "",
                "latitude": "45.7333",
            },
            {
                "place name": "Zagreb-dio",
                "longitude": "15.9667",
                "state": "Zagrebačka",
                "state abbreviation": "",
                "latitude": "45.7333",
            },
        ],
    }

    expected_value = {
        "code": "10000",
        "locations": [
            {"location_name": "Sljeme", "state_name": "Zagrebačka"},
            {"location_name": "Zagreb-dio", "state_name": "Zagrebačka"},
        ],
    }

    display_adapter = DisplayAdapter()
    return_value = display_adapter.adapt_for_display(data_dictionary=input_value)

    assert return_value == expected_value


def test_display_adapter_missing_values():
    input_value = {
        "post code": "10000",
        "country": "Croatia",
        "country abbreviation": "HR",
        "places": [
            {
                "place name": "Sljeme",
                "longitude": "15.9667",
                "state": "Zagrebačka",
                "state abbreviation": "",
                "latitude": "45.7333",
            },
            {
                "place name": "Zagreb-dio",
                "longitude": "15.9667",
                "state": "Zagrebačka",
                "state abbreviation": "",
                "latitude": "45.7333",
            },
        ],
    }
